import os
from packagedcode import buildpack
from commoncode.testcase import FileBasedTesting
from packageurl import PackageURL

class TestBuildpack(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')

    def test_is_datafile_buildpack_toml1(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/java-memory-assistant/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_java_memory_assistant_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/java-memory-assistant/buildpack.toml')
        packages = list(buildpack.BuildpackHandler.parse(test_file))

        assert len(packages) == 1
        package = packages[0]
        assert package.name == "Paketo Buildpack for Java Memory Assistant"
        assert package.extra_data.get("id") == "paketo-buildpacks/java-memory-assistant"
        assert package.description == "A Cloud Native Buildpack that installs the Java Memory Assistant agent"
        assert package.homepage_url == "https://github.com/paketo-buildpacks/java-memory-assistant"
        assert package.keywords == ["agent"]
        assert package.declared_license_expression == "Apache-2.0"
        assert package.sbom_formats == ["application/vnd.syft+json", "application/vnd.cyclonedx+json"]
        assert package.version == "{{.version}}"
        assert len(package.dependencies) == 1

        dependency = package.dependencies[0]
        assert dependency.purl == "pkg:generic/sap-java-memory-assistant@0.5.0?arch=amd64"
        assert dependency.scope == "runtime"
        assert dependency.is_runtime is True
        assert dependency.is_optional is False

        parsed_purl = PackageURL.from_string(dependency.purl)
        assert parsed_purl.name == "sap-java-memory-assistant"
        assert parsed_purl.version == "0.5.0"

    def test_is_datafile_buildpack_toml2(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/dotnet-execute/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_dotnet_execute_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/dotnet-execute/buildpack.toml')
        packages = list(buildpack.BuildpackHandler.parse(test_file))
    
        package = packages[0]
        assert package.name == "Paketo Buildpack for .NET Execute"
        assert package.extra_data.get("id") == "paketo-buildpacks/dotnet-execute"
        assert package.description == "A buildpack for running the `dotnet execute` command for an app"
        assert package.homepage_url == "https://github.com/paketo-buildpacks/dotnet-execute"
        assert package.keywords == ["dotnet"]
        assert package.declared_license_expression == "Apache-2.0"
        assert package.sbom_formats == ["application/vnd.cyclonedx+json", "application/spdx+json", "application/vnd.syft+json"]
        assert package.version == "unknown"

    def test_is_datafile_buildpack_toml3(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/git/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_git_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/git/buildpack.toml')
        packages = list(buildpack.BuildpackHandler.parse(test_file))
    
        package = packages[0]
        assert package.name == "Paketo Buildpack for Git"
        assert package.extra_data.get("id") == "paketo-buildpacks/git"
        assert package.homepage_url == "https://github.com/paketo-buildpacks/git"
    
    def test_is_datafile_buildpack_toml4(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/opentelemetry/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_opentelemetry_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/opentelemetry/buildpack.toml')
        packages = list(buildpack.BuildpackHandler.parse(test_file))

        assert len(packages) == 1
        package = packages[0]
        assert package.name == "Paketo Buildpack for OpenTelemetry"
        assert package.extra_data.get("id") == "paketo-buildpacks/opentelemetry"
        assert package.description == "A Cloud Native Buildpack that contributes and configures the OpenTelemetry Agent"
        assert package.homepage_url == "https://github.com/paketo-buildpacks/opentelemetry"
        assert package.keywords == ["java", "apm", "trace", "opentelemetry"]
        assert package.declared_license_expression == "Apache-2.0"
        assert package.sbom_formats == ["application/vnd.cyclonedx+json", "application/vnd.syft+json"]
        assert package.version == "{{.version}}"
        assert len(package.dependencies) == 1

        dependency = package.dependencies[0]
        assert dependency.purl == "pkg:generic/opentelemetry-java@2.10.0"
        assert dependency.scope == "runtime"
        assert dependency.is_runtime is True
        assert dependency.is_optional is False

        parsed_purl = PackageURL.from_string(dependency.purl)
        assert parsed_purl.name == "opentelemetry-java"
        assert parsed_purl.version == "2.10.0"

    def test_is_datafile_buildpack_toml5(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/pipeline-builder-canary/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_pipeline_builder_canary_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/pipeline-builder-canary/buildpack.toml')

        packages = list(buildpack.BuildpackHandler.parse(test_file))
        
        assert len(packages) == 1
        package = packages[0]
        assert package.name == "Paketo Buildpack for Pipeline Builder Canary"
        assert package.extra_data.get("id") == "paketo-buildpacks/pipeline-builder-canary"
        assert package.description == "A Cloud Native Buildpack that provides/does nothing. For testing only."
        assert package.homepage_url == "https://github.com/paketo-buildpacks/pipeline-builder-canary"
        assert package.keywords == ["nothing"]
        assert package.declared_license_expression == "Apache-2.0"
        assert package.version == "{{.version}}"
        assert len(package.dependencies) == 1

        dependency = package.dependencies[0]
        assert dependency.purl == "pkg:generic/apache-maven@3.9.9"
        assert dependency.scope == "runtime"
        assert dependency.is_runtime is True
        assert dependency.is_optional is False

        parsed_purl = PackageURL.from_string(dependency.purl)
        assert parsed_purl.name == "apache-maven"
        assert parsed_purl.version == "3.9.9"
    
    def test_is_datafile_buildpack_toml6(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/source-removal/buildpack.toml')
        assert buildpack.BuildpackHandler.is_datafile(test_file)

    def test_parse_paketo_source_removal_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/source-removal/buildpack.toml')
        packages = list(buildpack.BuildpackHandler.parse(test_file))
    
        package = packages[0]
        assert package.name == "Paketo Buildpack for Source Removal"
        assert package.extra_data.get("id") == "paketo-buildpacks/source-removal"
