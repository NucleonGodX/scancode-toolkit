#
# Copyright (c) nexB Inc. and others. All rights reserved.
# ScanCode is a trademark of nexB Inc.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/scancode-toolkit for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#

import os
from packagedcode import buildpack
from commoncode.testcase import FileBasedTesting
from packageurl import PackageURL
from packagedcode import models
from packages_test_utils import compare_package_results
from scancode.cli_test_utils import check_json_scan
from scancode.cli_test_utils import run_scan_click
from scancode_config import REGEN_TEST_FIXTURES

class TestBuildpack(FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), 'data')


    def test_scanworks_on_buildpack_heroku_java(self):
        test_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-java/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-java/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_heroku_php(self):
        test_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-php/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-php/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_dotnet_execute(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/dotnet-execute/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/dotnet-execute/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_java_memory_assistant(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/java-memory-assistant/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/java-memory-assistant/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_git(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/git/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/git/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_opentelemetry(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/opentelemetry/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/opentelemetry/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_pipeline_builder_canary(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/pipeline-builder-canary/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/pipeline-builder-canary/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_scanworks_on_buildpack_paketo_source_removal(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/source-removal/buildpack.toml')
        expected_file = self.get_test_loc('buildpack/paketo-buildpacks/source-removal/expectedbuildpack.json')
        result_file = self.get_temp_file('results.json')
        run_scan_click(['--package', test_file, '--json-pp', result_file])
        check_json_scan(expected_file, result_file, regen=REGEN_TEST_FIXTURES)

    def test_parse_heroku_buildpack_java_toml(self):
        test_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-java/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                description="Heroku buildpack for Java",
                name="Java",
                version="unknown",
                extra_data={
                    "ignore_files": [
                        "etc/",
                        "spec/",
                        "test/",
                        ".gitignore",
                        ".github/",
                        "hatchet.json",
                        "Gemfile",
                        "Gemfile.lock"
                    ]
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_heroku_buildpack_php_toml(self):
        test_file = self.get_test_loc('buildpack/heroku-buildpacks/heroku-buildpack-php/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                description= "Heroku buildpack for PHP",
                name="PHP",
                version="unknown",
                extra_data={
                    "ignore_files": [
                        ".github/",
                        ".gitignore",
                        ".rspec_parallel",
                        "support/build/",
                        "support/devcenter/",
                        "test/",
                        "Gemfile",
                        "Gemfile.lock",
                        "hatchet.json",
                        "hatchet.lock",
                        "requirements.txt"
                    ]
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_dotnet_execute_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/dotnet-execute/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                name="dotnet-execute",
                version="unknown",
                description="A buildpack for running the `dotnet execute` command for an app",
                homepage_url="https://github.com/paketo-buildpacks/dotnet-execute",
                keywords=["dotnet"],
                declared_license_expression="apache-2.0",
                declared_license_expression_spdx= "Apache-2.0",
                extracted_license_statement= "type: Apache-2.0",
                license_detections= [
                    {
                    "license_expression": "apache-2.0",
                    "license_expression_spdx": "Apache-2.0",
                    "matches": [
                        {
                        "license_expression": "apache-2.0",
                        "license_expression_spdx": "Apache-2.0",
                        "from_file": None,
                        "start_line": 1,
                        "end_line": 1,
                        "matcher": "2-aho",
                        "score": 100.0,
                        "matched_length": 3,
                        "match_coverage": 100.0,
                        "rule_relevance": 100,
                        "rule_identifier": "spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "rule_url": "https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "matched_text": "type: Apache-2.0"
                        }
                    ],
                    "identifier": "apache_2_0-d66ab77d-a5cc-7104-e702-dc7df61fe9e8"
                    }
                ],
                extra_data={
                    "api_version": "0.8",
                    "id": "paketo-buildpacks/dotnet-execute"
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_java_memory_assistant_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/java-memory-assistant/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                name="java-memory-assistant",
                version="{{.version}}",
                description="A Cloud Native Buildpack that installs the Java Memory Assistant agent",
                homepage_url="https://github.com/paketo-buildpacks/java-memory-assistant",
                keywords=["agent"],
                dependencies=[
                    models.DependentPackage(
                        purl="pkg:generic/sap-java-memory-assistant@0.5.0?arch=amd64",
                        scope="runtime",
                        is_runtime=True,
                        is_optional=False,
                        extra_data= {
                        "cpes": [
                        "cpe:2.3:a:sap:java-memory-assistant:0.5.0:*:*:*:*:*:*:*"
                        ]
                        }
                    )
                ],
                declared_license_expression="apache-2.0",
                declared_license_expression_spdx= "Apache-2.0",
                extracted_license_statement= "type: Apache-2.0",
                license_detections= [
                    {
                    "license_expression": "apache-2.0",
                    "license_expression_spdx": "Apache-2.0",
                    "matches": [
                        {
                        "license_expression": "apache-2.0",
                        "license_expression_spdx": "Apache-2.0",
                        "from_file": None,
                        "start_line": 1,
                        "end_line": 1,
                        "matcher": "2-aho",
                        "score": 100.0,
                        "matched_length": 3,
                        "match_coverage": 100.0,
                        "rule_relevance": 100,
                        "rule_identifier": "spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "rule_url": "https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "matched_text": "type: Apache-2.0"
                        }
                    ],
                    "identifier": "apache_2_0-d66ab77d-a5cc-7104-e702-dc7df61fe9e8"
                    }
                ],
                extra_data={
                    "api_version": "0.7",
                    "id": "paketo-buildpacks/java-memory-assistant",
                    "targets": [
                    {
                        "arch": "amd64",
                        "os": "linux"
                    },
                    {
                        "arch": "arm64",
                        "os": "linux"
                    }
                    ]
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_git_buildpack_toml(self):
            test_file = self.get_test_loc('buildpack/paketo-buildpacks/git/buildpack.toml')
            result_packages = list(buildpack.BuildpackHandler.parse(test_file))
            expected_packages = [
                models.PackageData(
                    type=buildpack.BuildpackHandler.default_package_type,
                    datasource_id=buildpack.BuildpackHandler.datasource_id,
                    name="git",
                    version="unknown",
                    homepage_url="https://github.com/paketo-buildpacks/git",
                    extra_data={
                        "api_version": "0.7",
                        "id": "paketo-buildpacks/git"
                    }
                )
            ]
            compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_opentelemetry_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/opentelemetry/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                name="opentelemetry",
                version="{{.version}}",
                description="A Cloud Native Buildpack that contributes and configures the OpenTelemetry Agent",
                homepage_url="https://github.com/paketo-buildpacks/opentelemetry",
                keywords=["java", "apm", "trace", "opentelemetry"],
                dependencies=[
                    models.DependentPackage(
                        purl="pkg:generic/opentelemetry-java@2.10.0",
                        scope="runtime",
                        is_runtime=True,
                        is_optional=False,
                        extra_data= {
                        "cpes": [
                        "cpe:2.3:a:open-telemetry:opentelemetry-java-agent:2.10.0:*:*:*:*:*:*:*"
                        ]
                        }                    
                        )
                ],
                declared_license_expression="apache-2.0",
                declared_license_expression_spdx= "Apache-2.0",
                extracted_license_statement= "type: Apache-2.0",
                license_detections= [
                    {
                    "license_expression": "apache-2.0",
                    "license_expression_spdx": "Apache-2.0",
                    "matches": [
                        {
                        "license_expression": "apache-2.0",
                        "license_expression_spdx": "Apache-2.0",
                        "from_file": None,
                        "start_line": 1,
                        "end_line": 1,
                        "matcher": "2-aho",
                        "score": 100.0,
                        "matched_length": 3,
                        "match_coverage": 100.0,
                        "rule_relevance": 100,
                        "rule_identifier": "spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "rule_url": "https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "matched_text": "type: Apache-2.0"
                        }
                    ],
                    "identifier": "apache_2_0-d66ab77d-a5cc-7104-e702-dc7df61fe9e8"
                    }
                ],
                extra_data={
                    "api_version": "0.7",
                    "id": "paketo-buildpacks/opentelemetry",
                    "targets": [
                    {
                        "arch": "amd64",
                        "os": "linux"
                    },
                    {
                        "arch": "arm64",
                        "os": "linux"
                    }
                    ]
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_pipeline_builder_canary_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/pipeline-builder-canary/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                name="pipeline-builder-canary",
                version="{{.version}}",
                description="A Cloud Native Buildpack that provides/does nothing. For testing only.",
                homepage_url="https://github.com/paketo-buildpacks/pipeline-builder-canary",
                keywords=["nothing"],
                dependencies=[
                    models.DependentPackage(
                        purl="pkg:generic/apache-maven@3.9.9",
                        scope="runtime",
                        is_runtime=True,
                        is_optional=False,
                        extra_data= {
                        "cpes": [
                        "cpe:2.3:a:apache:maven:3.9.9:*:*:*:*:*:*:*"
                        ]
                        }
                    )
                ],
                declared_license_expression="apache-2.0",
                declared_license_expression_spdx= "Apache-2.0",
                extracted_license_statement= "type: Apache-2.0",
                license_detections= [
                    {
                    "license_expression": "apache-2.0",
                    "license_expression_spdx": "Apache-2.0",
                    "matches": [
                        {
                        "license_expression": "apache-2.0",
                        "license_expression_spdx": "Apache-2.0",
                        "from_file": None,
                        "start_line": 1,
                        "end_line": 1,
                        "matcher": "2-aho",
                        "score": 100.0,
                        "matched_length": 3,
                        "match_coverage": 100.0,
                        "rule_relevance": 100,
                        "rule_identifier": "spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "rule_url": "https://github.com/nexB/scancode-toolkit/tree/develop/src/licensedcode/data/rules/spdx_license_id_apache-2.0_for_apache-2.0.RULE",
                        "matched_text": "type: Apache-2.0"
                        }
                    ],
                    "identifier": "apache_2_0-d66ab77d-a5cc-7104-e702-dc7df61fe9e8"
                    }
                ],
                extra_data={
                    "api_version": "0.7",
                    "id": "paketo-buildpacks/pipeline-builder-canary",
                    "targets": [
                    {
                        "arch": "amd64",
                        "os": "linux"
                    },
                    {
                        "arch": "arm64",
                        "os": "linux"
                    }
                    ]
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)

    def test_parse_paketo_source_removal_buildpack_toml(self):
        test_file = self.get_test_loc('buildpack/paketo-buildpacks/source-removal/buildpack.toml')
        result_packages = list(buildpack.BuildpackHandler.parse(test_file))
        expected_packages = [
            models.PackageData(
                type=buildpack.BuildpackHandler.default_package_type,
                datasource_id=buildpack.BuildpackHandler.datasource_id,
                name="source-removal",
                version="unknown",
                extra_data={
                    "api_version": "0.7",
                    "id": "paketo-buildpacks/source-removal"
                }
            )
        ]
        compare_package_results(expected_packages, result_packages)
