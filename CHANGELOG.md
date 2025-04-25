# Changelog

## [0.9.12](https://github.com/tiborsimko/reana-commons/compare/v0.9.11...0.9.12) (2025-04-25)


### Build

* **python:** add support for Python 3.13 ([#480](https://github.com/tiborsimko/reana-commons/issues/480)) ([5de7605](https://github.com/tiborsimko/reana-commons/commit/5de760512a3aa86282a9dc31ac031773ddf49ef6))
* **python:** change extra names to comply with PEP 685 ([#446](https://github.com/tiborsimko/reana-commons/issues/446)) ([9dad6da](https://github.com/tiborsimko/reana-commons/commit/9dad6da7b80bc07423d45dab7b6799911740a082))
* **python:** require smart-open&lt;7 for Python 3.6 ([#446](https://github.com/tiborsimko/reana-commons/issues/446)) ([17fd581](https://github.com/tiborsimko/reana-commons/commit/17fd581d4928d5c377f67bcb77c4f245e661c395))
* **python:** restore snakemake `reports` extra ([#446](https://github.com/tiborsimko/reana-commons/issues/446)) ([904178f](https://github.com/tiborsimko/reana-commons/commit/904178fe454b9af39164a0c327f1ecd1663132af))
* **snakemake:** require pulp&lt;2.8.0 ([#444](https://github.com/tiborsimko/reana-commons/issues/444)) ([5daa109](https://github.com/tiborsimko/reana-commons/commit/5daa109a58066126c2d8a35e7cd7da70d4137f62))


### Features

* **config:** allow customisation of runtime group name ([#440](https://github.com/tiborsimko/reana-commons/issues/440)) ([5cec305](https://github.com/tiborsimko/reana-commons/commit/5cec30561ba21e2ea695e20eaea8171226f06e52))
* **openapi:** add K8s resource requests and limits in reana.yaml ([#486](https://github.com/tiborsimko/reana-commons/issues/486)) ([53457cb](https://github.com/tiborsimko/reana-commons/commit/53457cbc6a431561d299554842e2ad4affade13d))
* **schema:** allow Compute4PUNCH backend options ([#445](https://github.com/tiborsimko/reana-commons/issues/445)) ([0570f4a](https://github.com/tiborsimko/reana-commons/commit/0570f4ade9135a2d340009d2091c97dfc81a2e60))
* **snakemake:** upgrade to Snakemake 7.32.4 ([#435](https://github.com/tiborsimko/reana-commons/issues/435)) ([20ae9ce](https://github.com/tiborsimko/reana-commons/commit/20ae9cebf19a1fdb77ad08956db04ef026521b5d))


### Bug fixes

* **cache:** handle deleted files when calculating access times ([#437](https://github.com/tiborsimko/reana-commons/issues/437)) ([698900f](https://github.com/tiborsimko/reana-commons/commit/698900fc63e20bd54dcc4a5faa6cac0be5d0d8de))
* **config:** remove hard-coded component host name domain ([#458](https://github.com/tiborsimko/reana-commons/issues/458)) ([f2faeaa](https://github.com/tiborsimko/reana-commons/commit/f2faeaa76f42c4484db70766fc1d7a3a122ee38f)), closes [#457](https://github.com/tiborsimko/reana-commons/issues/457)
* **openapi:** update server and job controller schemas ([#488](https://github.com/tiborsimko/reana-commons/issues/488)) ([b7e6b98](https://github.com/tiborsimko/reana-commons/commit/b7e6b98650566ee15277058c7da6636c94f343ef))


### Code refactoring

* **docs:** move from reST to Markdown ([#441](https://github.com/tiborsimko/reana-commons/issues/441)) ([36ce4e0](https://github.com/tiborsimko/reana-commons/commit/36ce4e0a86484e3a7006e20545a892424ce0f3a2))


### Test suite

* fix calculate hash test ([95a719b](https://github.com/tiborsimko/reana-commons/commit/95a719b6bb67b7d981860018e0a8c509a8d1d54e))


### Continuous integration

* **actions:** pin setuptools 70 ([#479](https://github.com/tiborsimko/reana-commons/issues/479)) ([b80bc70](https://github.com/tiborsimko/reana-commons/commit/b80bc707fa9311e3e5d00ea71bb17f853845d6bf))
* added flake8 linter ([a48dcd8](https://github.com/tiborsimko/reana-commons/commit/a48dcd8d7b9260b8ddb973747f43104e9685bee3))
* added github actions workflow ([80b4c2a](https://github.com/tiborsimko/reana-commons/commit/80b4c2a3b4bc583073f2e6385d8aa3800ce8507d))
* added python 2.7 to github action python test strategy ([5b8c024](https://github.com/tiborsimko/reana-commons/commit/5b8c0246fe874290576a2738def2a44080e72112)), closes [#233](https://github.com/tiborsimko/reana-commons/issues/233)
* **commitlint:** addition of commit message linter ([#432](https://github.com/tiborsimko/reana-commons/issues/432)) ([a67906f](https://github.com/tiborsimko/reana-commons/commit/a67906fe8620e1f624e24e8a4511694a9b60378d))
* **commitlint:** allow release commit style ([#447](https://github.com/tiborsimko/reana-commons/issues/447)) ([1208ccf](https://github.com/tiborsimko/reana-commons/commit/1208ccf2de844afe788d7bbccbd4f63b24af427e))
* **commitlint:** check for the presence of concrete PR number ([#438](https://github.com/tiborsimko/reana-commons/issues/438)) ([d3035dc](https://github.com/tiborsimko/reana-commons/commit/d3035dc12cecf16edcbec462dfdb1386da16f6d6))
* pin ubuntu version in GA jobs ([cbfc143](https://github.com/tiborsimko/reana-commons/commit/cbfc143f1f32a7b88b6d180ca7a991b56d1b6ebe))
* **release-please:** initial configuration ([#432](https://github.com/tiborsimko/reana-commons/issues/432)) ([687f2f4](https://github.com/tiborsimko/reana-commons/commit/687f2f4ea8c5c49a70c6f121faf7e59a98dd3138))
* removed pip upgrade ([efe654b](https://github.com/tiborsimko/reana-commons/commit/efe654b566e7c4110c91762e6cc1b2ac43e90581))
* **runners:** upgrade CI runners to Ubuntu 22.04 ([#490](https://github.com/tiborsimko/reana-commons/issues/490)) ([6a582a9](https://github.com/tiborsimko/reana-commons/commit/6a582a946d52eae76b69d87ce3995a172867b8ba))
* **shellcheck:** check all shell scripts recursively ([#436](https://github.com/tiborsimko/reana-commons/issues/436)) ([709a685](https://github.com/tiborsimko/reana-commons/commit/709a685b3a8586b069a98c0338283a6bd2721005))
* **shellcheck:** fix exit code propagation ([#438](https://github.com/tiborsimko/reana-commons/issues/438)) ([85d9a2a](https://github.com/tiborsimko/reana-commons/commit/85d9a2a68e3929f442e03d5422a37ffd6b7169c6))
* update all actions ([dd3d0ba](https://github.com/tiborsimko/reana-commons/commit/dd3d0bab733071136ff0cdfdd54e36e2f5788b9d))
* use Python 3.12 stable release ([e49b0c7](https://github.com/tiborsimko/reana-commons/commit/e49b0c7fdd5b7428b359c946d468bbdff10d7b14))


### Documentation

* add .readthedocs.yaml to migrate to RTD v2 ([6682140](https://github.com/tiborsimko/reana-commons/commit/66821403d8b40a8929677b988c5a4262a13574e5))
* **authors:** complete list of contributors ([#442](https://github.com/tiborsimko/reana-commons/issues/442)) ([4a74c10](https://github.com/tiborsimko/reana-commons/commit/4a74c10e7a248f580778ebc772bffe94e533e7ed))
* fix docstrings for kombu class references ([8af0606](https://github.com/tiborsimko/reana-commons/commit/8af06066687207d334562e70a6abe146e4c79427))
* fix docstrings for kombu class references ([8c20f2e](https://github.com/tiborsimko/reana-commons/commit/8c20f2e75c5e9da9e65450244c387b0f8d57121c))
* install only docs required dependencies for RTD build ([77e0d9f](https://github.com/tiborsimko/reana-commons/commit/77e0d9f0d095d19b8dfe3ed8a1970a5733e85907)), closes [#210](https://github.com/tiborsimko/reana-commons/issues/210)
* remove reana-cluster references ([f558c06](https://github.com/tiborsimko/reana-commons/commit/f558c0603b086a84995ced122fd99d05852679bb))
* set default language to English ([0247a25](https://github.com/tiborsimko/reana-commons/commit/0247a25d9744f07c530459017c45fe9ab7bc9e99))
* single-page RTFD outline ([e387aba](https://github.com/tiborsimko/reana-commons/commit/e387aba8524298ad99e87612cd9cd7dd3e71f147))
* switch to stable version of kombu ([daf272e](https://github.com/tiborsimko/reana-commons/commit/daf272ec5f3a2f91220f9318be546ba4d542024d))
* switch to stable version of kombu ([12a44e2](https://github.com/tiborsimko/reana-commons/commit/12a44e23cae0f8802cd243c06d4d50f289bd9360))
* update changelog ([f79147a](https://github.com/tiborsimko/reana-commons/commit/f79147a060c1ef7d02b6857fef9579d72ced6414))

## [0.9.11](https://github.com/reanahub/reana-commons/compare/0.9.10...0.9.11) (2025-04-07)


### Bug fixes

* **openapi:** update server and job controller schemas ([#488](https://github.com/reanahub/reana-commons/issues/488)) ([b7e6b98](https://github.com/reanahub/reana-commons/commit/b7e6b98650566ee15277058c7da6636c94f343ef))

## [0.9.10](https://github.com/reanahub/reana-commons/compare/0.9.9...0.9.10) (2025-04-04)


### Features

* **openapi:** add K8s resource requests and limits in reana.yaml ([#486](https://github.com/reanahub/reana-commons/issues/486)) ([53457cb](https://github.com/reanahub/reana-commons/commit/53457cbc6a431561d299554842e2ad4affade13d))

## [0.9.9](https://github.com/reanahub/reana-commons/compare/0.9.8...0.9.9) (2024-11-28)


### Build

* **python:** add support for Python 3.13 ([#480](https://github.com/reanahub/reana-commons/issues/480)) ([5de7605](https://github.com/reanahub/reana-commons/commit/5de760512a3aa86282a9dc31ac031773ddf49ef6))


### Features

* **schema:** allow Compute4PUNCH backend options ([#445](https://github.com/reanahub/reana-commons/issues/445)) ([0570f4a](https://github.com/reanahub/reana-commons/commit/0570f4ade9135a2d340009d2091c97dfc81a2e60))


### Bug fixes

* **config:** remove hard-coded component host name domain ([#458](https://github.com/reanahub/reana-commons/issues/458)) ([f2faeaa](https://github.com/reanahub/reana-commons/commit/f2faeaa76f42c4484db70766fc1d7a3a122ee38f)), closes [#457](https://github.com/reanahub/reana-commons/issues/457)


### Continuous integration

* **actions:** pin setuptools 70 ([#479](https://github.com/reanahub/reana-commons/issues/479)) ([b80bc70](https://github.com/reanahub/reana-commons/commit/b80bc707fa9311e3e5d00ea71bb17f853845d6bf))

## [0.9.8](https://github.com/reanahub/reana-commons/compare/0.9.7...0.9.8) (2024-03-01)


### Build

* **python:** change extra names to comply with PEP 685 ([#446](https://github.com/reanahub/reana-commons/issues/446)) ([9dad6da](https://github.com/reanahub/reana-commons/commit/9dad6da7b80bc07423d45dab7b6799911740a082))
* **python:** require smart-open&lt;7 for Python 3.6 ([#446](https://github.com/reanahub/reana-commons/issues/446)) ([17fd581](https://github.com/reanahub/reana-commons/commit/17fd581d4928d5c377f67bcb77c4f245e661c395))
* **python:** restore snakemake `reports` extra ([#446](https://github.com/reanahub/reana-commons/issues/446)) ([904178f](https://github.com/reanahub/reana-commons/commit/904178fe454b9af39164a0c327f1ecd1663132af))


### Continuous integration

* **commitlint:** allow release commit style ([#447](https://github.com/reanahub/reana-commons/issues/447)) ([1208ccf](https://github.com/reanahub/reana-commons/commit/1208ccf2de844afe788d7bbccbd4f63b24af427e))

## [0.9.7](https://github.com/reanahub/reana-commons/compare/0.9.6...0.9.7) (2024-02-20)


### Build

* **snakemake:** require pulp&lt;2.8.0 ([#444](https://github.com/reanahub/reana-commons/issues/444)) ([5daa109](https://github.com/reanahub/reana-commons/commit/5daa109a58066126c2d8a35e7cd7da70d4137f62))


### Documentation

* **authors:** complete list of contributors ([#442](https://github.com/reanahub/reana-commons/issues/442)) ([4a74c10](https://github.com/reanahub/reana-commons/commit/4a74c10e7a248f580778ebc772bffe94e533e7ed))

## [0.9.6](https://github.com/reanahub/reana-commons/compare/0.9.5...0.9.6) (2024-02-13)


### Features

* **config:** allow customisation of runtime group name ([#440](https://github.com/reanahub/reana-commons/issues/440)) ([5cec305](https://github.com/reanahub/reana-commons/commit/5cec30561ba21e2ea695e20eaea8171226f06e52))
* **snakemake:** upgrade to Snakemake 7.32.4 ([#435](https://github.com/reanahub/reana-commons/issues/435)) ([20ae9ce](https://github.com/reanahub/reana-commons/commit/20ae9cebf19a1fdb77ad08956db04ef026521b5d))


### Bug fixes

* **cache:** handle deleted files when calculating access times ([#437](https://github.com/reanahub/reana-commons/issues/437)) ([698900f](https://github.com/reanahub/reana-commons/commit/698900fc63e20bd54dcc4a5faa6cac0be5d0d8de))


### Code refactoring

* **docs:** move from reST to Markdown ([#441](https://github.com/reanahub/reana-commons/issues/441)) ([36ce4e0](https://github.com/reanahub/reana-commons/commit/36ce4e0a86484e3a7006e20545a892424ce0f3a2))


### Continuous integration

* **commitlint:** addition of commit message linter ([#432](https://github.com/reanahub/reana-commons/issues/432)) ([a67906f](https://github.com/reanahub/reana-commons/commit/a67906fe8620e1f624e24e8a4511694a9b60378d))
* **commitlint:** check for the presence of concrete PR number ([#438](https://github.com/reanahub/reana-commons/issues/438)) ([d3035dc](https://github.com/reanahub/reana-commons/commit/d3035dc12cecf16edcbec462dfdb1386da16f6d6))
* **release-please:** initial configuration ([#432](https://github.com/reanahub/reana-commons/issues/432)) ([687f2f4](https://github.com/reanahub/reana-commons/commit/687f2f4ea8c5c49a70c6f121faf7e59a98dd3138))
* **shellcheck:** check all shell scripts recursively ([#436](https://github.com/reanahub/reana-commons/issues/436)) ([709a685](https://github.com/reanahub/reana-commons/commit/709a685b3a8586b069a98c0338283a6bd2721005))
* **shellcheck:** fix exit code propagation ([#438](https://github.com/reanahub/reana-commons/issues/438)) ([85d9a2a](https://github.com/reanahub/reana-commons/commit/85d9a2a68e3929f442e03d5422a37ffd6b7169c6))

## 0.9.5 (2023-12-15)

- Fixes installation by pinning `bravado-core` to versions lower than 6.1.1.

## 0.9.4 (2023-11-30)

- Changes the REANA specification schema to use the `draft-07` version of the JSON Schema specification.
- Changes validation of REANA specification to expose functions for loading workflow input parameters and workflow specifications.
- Changes validation of REANA specification to make the `environment` property mandatory for the steps of serial workflows.
- Changes validation of REANA specification to raise a warning for unexpected properties for the steps of serial workflows.
- Changes CVMFS support to allow users to automatically mount any available repository.
- Fixes the mounting of CVMFS volumes for the REANA deployments that use non-default Kubernetes namespace.

## 0.9.3 (2023-09-26)

- Adds support for Python 3.12.
- Adds the OpenAPI specification support for `prune_workspace` endpoint that allows to delete files that are neither inputs nor outputs from the workspace.
- Adds support for `tests.files` in `reana.yaml` allowing to specify Gherkin feature files for testing runnable examples.
- Changes the OpenAPI specification to include the `run_stopped_at` property in the workflow progress information returned by the workflow list and workflow status endpoints.
- Changes the OpenAPI specification to include the `maximum_interactive_session_inactivity_period` value to the `info` endpoint.
- Changes the email sending utility to allow configuring authentication and encryption options.
- Changes validation of REANA specification to emit warnings about unknown properties.
- Fixes the verbs used to describe changes to the status of a workflow in order to avoid incorrect grammatical phrases such as `workflow has been failed`.
- Fixes the loading of Snakemake and CWL workflow specifications when no parameters are specified.
- Fixes the OpenAPI specification of GitLab OAuth endpoint return statuses.
- Fixes container image names to be Podman-compatible.
- Fixes the email sending utility to not send emails when notifications are disabled globally.

## 0.9.2.1 (2023-07-19)

- Changes `PyYAML` dependency version bounds in order to fix installation on Python 3.10+.

## 0.9.2 (2023-02-10)

- Fixes `wcmatch` dependency version specification.

## 0.9.1 (2023-01-18)

- Changes Kerberos renew container's configuration to log each ticket renewal.

## 0.9.0 (2022-12-13)

- Adds support for Python 3.11.
- Adds support for Rucio.
- Adds REANA specification validation and loading logic from `reana-client`.
- Adds common utility functions for managing workspace files.
- Adds OpenAPI specification support for `launch` endpoint that allows running workflows from remote sources.
- Adds OpenAPI specification support for `get_workflow_retention_rules` endpoint that allows to retrieve the workspace file retention rules of a workflow.
- Adds generation of Kerberos init and renew container's configuration.
- Adds support for Unicode characters inside email body.
- Changes OpenAPI specification to include missing response schema elements and some other small enhancements.
- Changes the Kubernetes Python client to use the `networking/v1` API.
- Changes REANA specification loading functionality to allow specifying different working directories.
- Changes REANA specification to allow enabling Kerberos for the whole workflow.
- Changes REANA specification to allow specifying `retention_days` for the workflow.
- Changes REANA specification to allow specifying `slurm_partition` and `slurm_time` for Slurm compute backend jobs.
- Changes the loading of Snakemake specifications to preserve the current working directory.
- Fixes the submission of jobs by stripping potential leading and trailing whitespaces in Docker image names.

## 0.8.5 (2022-02-23)

- Adds `retry_count` parameter to WorkflowSubmissionPublisher.

## 0.8.4 (2022-02-08)

- Adds new configuration variable to toggle Kubernetes security context. (`K8S_USE_SECURITY_CONTEXT`)
- Changes installation to revert `Yadage` dependency versions.

## 0.8.3 (2022-02-04)

- Changes installation to remove upper version pin on `kombu`.

## 0.8.2 (2022-02-01)

- Adds support for Python 3.10.
- Adds workflow name validation utility.
- Changes `Snakemake` loaded specification to include compute backends.
- Changes OpenAPI specification with respect to return supported compute backends in `info` endpoint.
- Fixes file system usage calculation on CephFS shares in `get_disk_usage` utility function.

## 0.8.1 (2021-12-21)

- Adds OpenAPI specification support for `kubernetes_job_timeout` handling.
- Changes OpenAPI specification for cluster health status endpoint.
- Changes Yadage dependencies to allow 0.21.x patchlevel-version updates.
- Changes installation to require Python-3.6 or higher versions.

## 0.8.0 (2021-11-22)

- Adds `get_disk_usage` utility function to calculate disk usage for a directory.
- Adds `Yadage` workflow specification loading utilities.
- Adds workspace validation utilities.
- Adds `Snakemake` workflow engine integration.
- Adds custom objects API instance to k8s client.
- Adds available worklow engines configuration.
- Adds environment variable to define time between job controller connection checks.
- Adds cluster health status endpoint.
- Adds OpenAPI specifications with respect to user quotas.
- Changes `workflow-submission` queue as a priority queue and allows to set the priority number on workflow submission.
- Changes OpenAPI specifications with respect to turning `workspaces` endpoint into `info`.
- Changes publisher logging level on error callback.
- Removes support for Python 2.

## 0.7.5 (2021-07-02)

- Adds support for glob patterns when listing workflow files.
- Adds support for specifying `kubernetes_memory_limit` for Kubernetes compute backend jobs.

## 0.7.4 (2021-03-17)

- Adds new functions to serialise/deserialise job commands between REANA components.
- Changes `reana_ready` function location to REANA-Server.

## 0.7.3 (2021-02-22)

- Adds new configuration variable to toggle runtime user jobs clean up depending on their statuses. (`REANA_RUNTIME_KUBERNETES_KEEP_ALIVE_JOBS_WITH_STATUSES`)
- Adds central class to instantiate workflow engines with more resilience. (`workflow_engine.create_workflow_engine_command`)

## 0.7.2 (2021-02-02)

- Adds support for Python 3.9.
- Fixes minor code warnings.
- Fixes a helper function that calculates directory hashes.
- Changes OpenAPI specifications with respect to sign-up form.
- Changes OpenAPI specifications with respect to email confirmation.
- Changes CI system to include Python flake8 checker.

## 0.7.1 (2020-11-09)

- Adds support for restarting yadage workflows (through `accept_metadir` operational option).
- Allows `htcondor_max_runtime` and `htcondor_accounting_group` to be specified for HTC jobs.
- Adds new field in REANA-Server OpenAPI spec to return server version.
- Changes CI system from Travis to GitHub Actions.

## 0.7.0 (2020-10-20)

- Adds new utility to send emails.
- Adds centralised validation utility for workflow operational options.
- Adds new configuration variable to set the maximum number of running workflows. (`REANA_MAX_CONCURRENT_BATCH_WORKFLOWS`)
- Adds new configuration variable to set prefix of REANA cluster component names. (`REANA_COMPONENT_PREFIX`)
- Adds new configuration variable for the runtime pod node selector label. (`REANA_RUNTIME_KUBERNETES_NODE_LABEL`)
- Adds new configuration variable to define the Kubernetes namespace in which REANA infrastructure components run. (`REANA_INFRASTRUCTURE_KUBERNETES_NAMESPACE`)
- Adds new configuration variable to define the Kubernetes namespace in which REANA runtime components components run. (`REANA_RUNTIME_KUBERNETES_NAMESPACE`)
- Adds possibility to specify unpacked container images for running jobs.
- Adds support for `initfiles` operational option for the Yadage workflow engine.
- Fixes memory leak in Bravado client instantiation.
- Changes CephFS Persistent Volume Claim name. (`REANA_SHARED_PVC_NAME`)
- Changes default logging level to `INFO`.
- Changes default CVMFS volume list to include LHCb Gaudi related workflows.
- Changes code formatting to respect `black` coding style.
- Changes underlying requirements to use Kubernetes Python library version 11.
- Changes underlying requirements to use latest CVMFS CSI driver version.
- Changes documentation to single-page layout.

## 0.6.1 (2020-05-25)

- Upgrades Kubernetes Python client.

## 0.6.0 (2019-12-19)

- Adds new API for Gitlab integration.
- Adds new Kubernetes client API for ingresses.
- Adds new APIs for management of user secrets.
- Adds EOS storage Kubernetes configuration.
- Adds HTCondor and Slurm compute backends.
- Adds support for streaming file uploads.
- Allows unpacked CVMFS and CMS open data volumes.
- Adds Serial workflow step name and compute backend.
- Adds support for Python 3.8.

## 0.5.0 (2019-04-16)

- Centralises log level and log format configuration.
- Adds new utility to inspect the disk usage on a given workspace.
  (`get_workspace_disk_usage`)
- Introduces the module to share Celery tasks accross REANA
  components. (`tasks.py`)
- Introduces common Celery task to determine whether REANA can
  execute new workflows depending on a set of conditions
  such as running job count. (`reana_ready`, `check_predefined_conditions`,
  `check_running_job_count`)
- Allows the AMQP consumer to be configurable with multiple queues.
- Introduces new queue for workflow submission. (`workflow-submission`)
- Introduces new publisher for workflow submissions.
  (`WorkflowSubmissionPublisher`)
- Centralises Kubernetes API client configuration and initialisation.
- Adds Kubernetes specific configuration for CVMFS volumes as utils.
- Introduces a new method, `copy_openapi_specs`, to automatically move
  validated OpenAPI specifications from components to REANA Commons
  `openapi_specifications` directory.
- Centralises interactive session types.
- Introduces central REANA errors through the `errors.py` module.
- Skips SSL verification for all HTTPS requests performed with the
  `BaseAPIClient`.

## 0.4.0 (2018-11-06)

- Aggregates OpenAPI specifications of REANA components.
- Improves AMQP re-connection handling. Switches from `pika` to `kombu`.
- Enhances test suite and increases code coverage.
- Changes license to MIT.

## 0.3.1 (2018-09-04)

- Adds parameter expansion and validation utilities for parametrised Serial
  workflows.

## 0.3.0 (2018-08-10)

- Initial public release.
- Provides basic AMQP pub/sub methods for REANA components.
- Utilities for caching used in different REANA components.
- Click formatting helpers.
