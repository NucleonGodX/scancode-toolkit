# SPDX-License-Identifier: Apache-2.0

import tomlkit
from packagedcode import models
from packageurl import PackageURL

class BuildpackHandler(models.DatafileHandler):
    """
    Handle buildpack.toml manifests.
    See https://buildpacks.io/ for details on buildpack format.
    """
    datasource_id = "buildpack_toml"
    path_patterns = ("*buildpack.toml",)
    default_package_type = "buildpack"
    description = "Cloud Native Buildpack manifest"
    documentation_url = "https://buildpacks.io/"

    @classmethod
    def parse(cls, location, package_only=False):
        """
        Parse the buildpack.toml file at `location` and yield PackageData.
        """
        with open(location, "r", encoding="utf-8") as f:
            data = tomlkit.parse(f.read())

        # Extract required fields
        api_version = data.get("api")
        buildpack = data.get("buildpack", {})
        if not buildpack:
            return  # Skip files missing required fields

        buildpack_id = buildpack.get("id")
        buildpack_version = buildpack.get("version", "unknown")
        buildpack_name = buildpack.get("name")

        if not (api_version and buildpack_id and buildpack_version and buildpack_name):
            return  # Skip incomplete data

        # Optional fields
        description = buildpack.get("description")
        homepage_url = buildpack.get("homepage")
        licenses = buildpack.get("licenses", [])
        keywords = buildpack.get("keywords", [])
        sbom_formats = buildpack.get("sbom-formats", [])

        # Parse licenses
        license_expressions = []
        for license_entry in licenses:
            license_type = license_entry.get("type")
            license_uri = license_entry.get("uri")
            if license_type:
                license_expressions.append(license_type)

        # Parse dependencies from "metadata.dependencies"
        dependencies = []
        metadata = data.get("metadata", {})
        metadata_dependencies = metadata.get("dependencies", [])
        for dep in metadata_dependencies:
            dep_purl = dep.get("purl")
            dep_name = dep.get("name")
            dep_version = dep.get("version")
            if dep_purl:
                dependencies.append(
                    models.DependentPackage(
                        purl=dep_purl,
                        scope="runtime",
                        is_runtime=True,
                        is_optional=False,
                    )
                )
            elif dep_name and dep_version:
                dependencies.append(
                    models.DependentPackage(
                        purl=PackageURL(type="generic", name=dep_name, version=dep_version).to_string(),
                        scope="runtime",
                        is_runtime=True,
                        is_optional=False,
                    )
                )

        # Parse "order" section for additional dependencies
        orders = data.get("order", [])
        for order in orders:
            for group in order.get("group", []):
                group_id = group.get("id")
                group_version = group.get("version")
                if group_id and group_version:
                    dependencies.append(
                        models.DependentPackage(
                            purl=PackageURL(type="buildpack", name=group_id, version=group_version).to_string(),
                            scope="runtime",
                            is_runtime=True,
                            is_optional=group.get("optional", False),
                        )
                    )

        package_data = dict(
            datasource_id=cls.datasource_id,
            type=cls.default_package_type,
            name=buildpack_name,
            version=buildpack_version,
            description=description,
            homepage_url=homepage_url,
            keywords=keywords,
            sbom_formats=sbom_formats,
            declared_license_expression=" AND ".join(license_expressions) if license_expressions else None,
            dependencies=dependencies,
            extra_data={"id": buildpack_id},  # Store the id in extra_data
        )

        yield models.PackageData.from_data(package_data, package_only)
