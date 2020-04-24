# [4.4.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.3.0...v4.4.0) (2020-04-24)


### Features

* **AssistantV2:** regenerate based on current API def ([46a812c](https://github.com/watson-developer-cloud/python-sdk/commit/46a812c6f74a9d32a96ad566e2d25d883c24d2f7))
* regenerate services using current API def ([e9ea20c](https://github.com/watson-developer-cloud/python-sdk/commit/e9ea20cc68a09da4e948c0622e254c31b27b481b))
* **LanguageTranslator:** add support for auto correct ([230878a](https://github.com/watson-developer-cloud/python-sdk/commit/230878a256d375c92cef0647e2f5efa51b8a5cf0))
* **SpeechToText:** add support for speech_detector_sensitivity and background_audio_suppression in ([9aa13e9](https://github.com/watson-developer-cloud/python-sdk/commit/9aa13e94558c37ca815d61ff36d0988943c55bf7))

# [4.3.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.2.1...v4.3.0) (2020-02-13)


### Features

* **assistantv1:** New param `include_audi` in `create_synonym` and `update_synonym` and  `update_dialog_node ` ([fbe1081](https://github.com/watson-developer-cloud/python-sdk/commit/fbe1081309aaa380d47b3c9016aaedc0a7bb5005))
* **assistantv1:** New param `include_audit` in `create_example`, `update_example`, `create_counterexample`, `update_counterexample`, `create_entity` ([b1f99ec](https://github.com/watson-developer-cloud/python-sdk/commit/b1f99ec1e4fad3655ff526cab7de5f18e29607a0))
* **assistantv1:** New param `include_audit` in `create_intent` ([d523706](https://github.com/watson-developer-cloud/python-sdk/commit/d52370646cd9d5aa88bfd67da294dfd5f8ba9800))
* **assistantv1:** New param `include_audit` in `create_value` ([4d32257](https://github.com/watson-developer-cloud/python-sdk/commit/4d32257464bd87886934c00f5a4e569896a4ac32))
* **assistantv1:** New param `include_audit` in `create_workspace` and `update_workspace` ([e44cb16](https://github.com/watson-developer-cloud/python-sdk/commit/e44cb16771620f0cbc6f6c03e215c088c5a1beb6))
* **assistantv1:** New params `append` and `include_audit` in `update_intent` ([3b015f9](https://github.com/watson-developer-cloud/python-sdk/commit/3b015f9b660241c2ab6f6b7f371843edf2c12c59))
* **assistantv1:** New params `audit` and `include_audit` in `update_value` ([8bac230](https://github.com/watson-developer-cloud/python-sdk/commit/8bac230a824d996f7807f943650c737ca3ae553d))
* **assistantv1:** New params `include_audit` and `append` in `update_entity` ([e36783d](https://github.com/watson-developer-cloud/python-sdk/commit/e36783d015e7681b626a1cc8c99ee68a9cbf614f))
* **assistantv1:** New params `interpretation` and `role` in `RuntimeEntity` model ([a44ace8](https://github.com/watson-developer-cloud/python-sdk/commit/a44ace8638db57f17d319932863aa5c5af51dd93))
* **assistantv2:** `interpretation`, `alternatives` and `role` properties in `RuntimeEntity` ([5ef087f](https://github.com/watson-developer-cloud/python-sdk/commit/5ef087f4b27b0771e098aaec8488e42d94ecd1ce))
* **assistantv2:** New params `locale` and `reference_time` in `MessageContextGlobalSystem` ([9b7e56e](https://github.com/watson-developer-cloud/python-sdk/commit/9b7e56e85d9fdec8b264c1a2865882c031046998))
* **vr4:** New objects operations ([cc9eace](https://github.com/watson-developer-cloud/python-sdk/commit/cc9eaced7ac1e693392e0ea2e6eb2ed27c63af9a))

## [4.2.1](https://github.com/watson-developer-cloud/python-sdk/compare/v4.2.0...v4.2.1) (2020-01-17)


### Bug Fixes

* **nlu:** Add model property back in CategoriesOptions ([6d5ed34](https://github.com/watson-developer-cloud/python-sdk/commit/6d5ed3404408a32daa90490daa9be24f53512998))

# [4.2.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.1.0...v4.2.0) (2020-01-16)


### Features

* **core:** Update core version ([88106fb](https://github.com/watson-developer-cloud/python-sdk/commit/88106fb9c9460e60363a814565b51a512805f8b9))
* **stt:** New param `end_of_phrase_silence_time` and `split_transcript_at_phrase_end` in `recognize` ([776dc86](https://github.com/watson-developer-cloud/python-sdk/commit/776dc8635a98489a9ceb8abf155947bb0f39ad8a))
* **stt:** New param `end_of_phrase_silence_time` and `split_transcription` in recognize_using_websocket ([040946f](https://github.com/watson-developer-cloud/python-sdk/commit/040946f88d6b652f8b8e5638429b69fb1035e79a))

# [4.1.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.0.4...v4.1.0) (2019-11-27)


### Features

* **assistantv1:** New param `new_disambiguation_opt_out ` in `create_dialog_node` ([5a5b840](https://github.com/watson-developer-cloud/python-sdk/commit/5a5b84076ff4b0d87355ed71cf7a2cbb9612c866))
* **assistantv1:** New param `new_disambiguation_opt_out ` in `update_dialog_node() ` ([6e52e07](https://github.com/watson-developer-cloud/python-sdk/commit/6e52e07b3e3ab0a9bc2687406b8a98c5e5826e33))
* **assistantv1:** New param `webhooks` in `create_workspace()` and `update_workspace()` ([0134b69](https://github.com/watson-developer-cloud/python-sdk/commit/0134b6981c09fc7132297aeb161eb75029bbd54d))
* **assistantv1:** New properties `randomize` and `max_ssuggestions` in `WorkspaceSystemSettingsDisambiguation` ([27a8cd7](https://github.com/watson-developer-cloud/python-sdk/commit/27a8cd7173a48fb6aaf909598fc3eb34e1320fe4))
* **assistantv1:** New property `off_topic` in `WorkspaceSystemSettings` ([5f93c55](https://github.com/watson-developer-cloud/python-sdk/commit/5f93c552828b539b846c9a44df4f69ed888d27b4))
* **discoveryv1:** `title` property not part of `QueryNoticesResult` and `QueryResult` ([2ce0ad3](https://github.com/watson-developer-cloud/python-sdk/commit/2ce0ad33c91714eb6d9b2adb7ac44ff70ad378e9))
* **discoveryv2:** Add examples for discoveryv2 ([2b54527](https://github.com/watson-developer-cloud/python-sdk/commit/2b54527725438d229e4acd80dc31d0869bdaa464))
* **discoveryv2:** New discovery v2 available on CP4D ([73df7e4](https://github.com/watson-developer-cloud/python-sdk/commit/73df7e4a53ef83ad1271b71215ab357f7a538177))
* **VisualRecognitionv4:** New method `get_training_usage` ([a5bec46](https://github.com/watson-developer-cloud/python-sdk/commit/a5bec467005db9340f6983654c293c94587258d9))

## [4.0.4](https://github.com/watson-developer-cloud/python-sdk/compare/v4.0.3...v4.0.4) (2019-11-22)


### Bug Fixes

* **semrelease:** Provide proper git message for semantic release ([88e2c08](https://github.com/watson-developer-cloud/python-sdk/commit/88e2c0806882693d175c5b8aedb1bf187223db79))

## [4.0.3](https://github.com/watson-developer-cloud/python-sdk/compare/v4.0.2...v4.0.3) (2019-11-20)


### Bug Fixes

* **bumpversion:** Skip for bumpversion ([fd38d73](https://github.com/watson-developer-cloud/python-sdk/commit/fd38d7395daf3d28e8dd085b0a1c8e9d4358a1b5))
* **semantic:** remove tag in bumpversion ([bb1a6a9](https://github.com/watson-developer-cloud/python-sdk/commit/bb1a6a93fcbc8ac13df45d78fc2b97b071267699))
* **semrelease:** Reorder semantic release steps ([1a13a0c](https://github.com/watson-developer-cloud/python-sdk/commit/1a13a0c0bf8522b8ea10146d4daf9059f2595c35))

## [4.0.3](https://github.com/watson-developer-cloud/python-sdk/compare/v4.0.2...v4.0.3) (2019-11-20)


### Bug Fixes

* **bumpversion:** Skip for bumpversion ([fd38d73](https://github.com/watson-developer-cloud/python-sdk/commit/fd38d7395daf3d28e8dd085b0a1c8e9d4358a1b5))
* **semrelease:** Reorder semantic release steps ([1a13a0c](https://github.com/watson-developer-cloud/python-sdk/commit/1a13a0c0bf8522b8ea10146d4daf9059f2595c35))

## [4.0.2](https://github.com/watson-developer-cloud/python-sdk/compare/v4.0.1...v4.0.2) (2019-11-11)


### Bug Fixes

* **semantic:** Fix semantic release stale commit ([f0eaafa](https://github.com/watson-developer-cloud/python-sdk/commit/f0eaafa2731b12847c9941687f0f91d73c43d94f))

Moved to [https://github.com/watson-developer-cloud/python-sdk/wiki/Changelog](https://github.com/watson-developer-cloud/python-sdk/wiki/Changelog)
