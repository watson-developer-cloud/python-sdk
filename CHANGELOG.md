# [5.3.0](https://github.com/watson-developer-cloud/python-sdk/compare/v5.2.3...v5.3.0) (2021-09-14)


### Bug Fixes

* **disco_v1:** update type of status to reflect service changes ([ab880f0](https://github.com/watson-developer-cloud/python-sdk/commit/ab880f04ae2ec5983e74175cd7b1dc83bd24f022))
* **disco_v2:** project types enum updated/fixed ([a598231](https://github.com/watson-developer-cloud/python-sdk/commit/a598231df416e8cbf4453342b42ce5a5d8c6be85))
* **nlu:** fix listClassificationsModels response model ([9954e59](https://github.com/watson-developer-cloud/python-sdk/commit/9954e59df889b45b761ef206ad8dedd9502e762a))
* **wss:** fix on_transcription parsing issue including tests ([1b05e1b](https://github.com/watson-developer-cloud/python-sdk/commit/1b05e1b3169b8c904fd17c3834d4e61779fa511c))


### Features

* **assistant_v1:** add alt_text and sensitivity options, location now optional ([0a6c540](https://github.com/watson-developer-cloud/python-sdk/commit/0a6c540f4a5d6abf25e35f9b8b20d6d191744a43))
* **assistant_v2:** same as v1, add more properties ([c2ca53b](https://github.com/watson-developer-cloud/python-sdk/commit/c2ca53bf1bdc55790787d926ffa23f1cc12b3cee))
* **assistant_v2,disco_v1:** add answers property to response model, fix typo ([611b7c9](https://github.com/watson-developer-cloud/python-sdk/commit/611b7c91644fb2238712cfed964ea7376b0d076a))
* **stt&tts:** new models added ([67ee967](https://github.com/watson-developer-cloud/python-sdk/commit/67ee967726c022b9e883bef786cb82a59b86be28))


## [5.2.3](https://github.com/watson-developer-cloud/python-sdk/compare/v5.2.2...v5.2.3) (2021-08-26)


### Bug Fixes

* **nlc:** add deprecation warning ([d1ec209](https://github.com/watson-developer-cloud/python-sdk/commit/d1ec209484320c2a61c735721148a66f58e6f7b1)), closes [#9624](https://github.com/watson-developer-cloud/python-sdk/issues/9624)
* **nlc:** move deprecation warning ([09a6dd4](https://github.com/watson-developer-cloud/python-sdk/commit/09a6dd4d7b26664cb92d8652f8d54ca96d9404a9))
* **nlc:** move deprecation warning ([3658ee8](https://github.com/watson-developer-cloud/python-sdk/commit/3658ee856c3ddba77a64589631b4605ae3c8c86c))

## [5.2.2](https://github.com/watson-developer-cloud/python-sdk/compare/v5.2.1...v5.2.2) (2021-07-06)


### Bug Fixes

* robustify the STT streaming results handling ([#768](https://github.com/watson-developer-cloud/python-sdk/issues/768)) ([264807d](https://github.com/watson-developer-cloud/python-sdk/commit/264807d7eb3287bbca56328496a477e042a9b2ca))

## [5.2.1](https://github.com/watson-developer-cloud/python-sdk/compare/v5.2.0...v5.2.1) (2021-06-28)


### Bug Fixes

* **tts:** remove origin header from websocket request ([e151e82](https://github.com/watson-developer-cloud/python-sdk/commit/e151e8271f4ddc2d0217beec8e84896e0e44539f))

# [5.2.0](https://github.com/watson-developer-cloud/python-sdk/compare/v5.1.0...v5.2.0) (2021-06-10)


### Bug Fixes

* **compare-comply:** add deprecation notice for CC ([d006937](https://github.com/watson-developer-cloud/python-sdk/commit/d0069376dcd1e23076c12130feeea1b20010de06))
* **lt:** fix character encoding for non latin langs ([900bd79](https://github.com/watson-developer-cloud/python-sdk/commit/900bd79bbeb7a28b82aa47d2e3345837f62fc306))
* **nlu:** remove ListCategoriesModelsResponse ([c09022f](https://github.com/watson-developer-cloud/python-sdk/commit/c09022f8841104262351447ac5dccba6ef159805))
* **tts:** remove extraneous filename param ([d6f9c5d](https://github.com/watson-developer-cloud/python-sdk/commit/d6f9c5d4b75bf303f363dfac68180351d7bcbc26))


### Features

* **assistantv1:** generation release changes ([ac146a1](https://github.com/watson-developer-cloud/python-sdk/commit/ac146a1efc5e148a636b17540399898c74222a29))
* **assistantv2:** generation release changes ([d33caba](https://github.com/watson-developer-cloud/python-sdk/commit/d33caba954e764e4b512e4fce62750c2fd9b8cf1))
* **discov2:** generation release changes ([0ea3ac0](https://github.com/watson-developer-cloud/python-sdk/commit/0ea3ac0ce1024138097e1777f8ecde5b45eaa92d))
* **nlu:** generation release changes ([e5e71b6](https://github.com/watson-developer-cloud/python-sdk/commit/e5e71b655bc3d7477fd4244df28651fa91a82cd4))
* **stt-tts:** generation release changes ([0600855](https://github.com/watson-developer-cloud/python-sdk/commit/06008553bdae0d2c0768d41a1d1878523e5bd810))

# [5.1.0](https://github.com/watson-developer-cloud/python-sdk/compare/v5.0.2...v5.1.0) (2021-01-12)


### Features

* upate core to use 3.3.6 ([83d5f6a](https://github.com/watson-developer-cloud/python-sdk/commit/83d5f6a7ad4c69fc3c2dbecc6cadee0dc69eeadf))

## [5.0.2](https://github.com/watson-developer-cloud/python-sdk/compare/v5.0.1...v5.0.2) (2020-12-28)


### Bug Fixes

* lock JWT version to 1.7.1 ([8fcdfc6](https://github.com/watson-developer-cloud/python-sdk/commit/8fcdfc64db1bcf6a230e8be80de6dfcad8e8811f))

## [5.0.1](https://github.com/watson-developer-cloud/python-sdk/compare/v5.0.0...v5.0.1) (2020-12-22)


### Bug Fixes

* **Assistant:** node dialog response should have agent props ([53e532e](https://github.com/watson-developer-cloud/python-sdk/commit/53e532e04ab141d93e54f040965dbca993186543))

# [5.0.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.7.1...v5.0.0) (2020-12-11)


### Features

* regenerate services using latest api def and generator ([59e7ded](https://github.com/watson-developer-cloud/python-sdk/commit/59e7dede81f530ea027b480fd007f9df67180ab1))
* regenerate using current api def and add deprecation warnings ([c3e1f07](https://github.com/watson-developer-cloud/python-sdk/commit/c3e1f07697b15d05f87cec39e36a9a2d28db7b91))
* regenerate with current API and add deprecation warnings ([4faa938](https://github.com/watson-developer-cloud/python-sdk/commit/4faa9380a606eeb8e8794b918b0f72313e4b1d86))
* regenrate language translator ([8fdebc4](https://github.com/watson-developer-cloud/python-sdk/commit/8fdebc45f0dfd1044d848969cb5cb3b8cb15a313))
* regenrate services using current api def and generator ([e84a0cb](https://github.com/watson-developer-cloud/python-sdk/commit/e84a0cb0636cd0add767903391de150bd65a4cd2))
* regenrate using current api def and generator 3.21 ([33e0d93](https://github.com/watson-developer-cloud/python-sdk/commit/33e0d9356ac43b7f988200c853b46b6cf4f703ab))
* **AssistantV1:** add support for bulkClassify ([e17b24c](https://github.com/watson-developer-cloud/python-sdk/commit/e17b24cc565bf6ee603497aeb5c11436ee09b0dc))
* **AssistantV2:** add support for bulkClassify ([8b14dda](https://github.com/watson-developer-cloud/python-sdk/commit/8b14dda82de980f09a031b1e15ab53573a5b55d8))
* **CompareComply:** remove before and after from list feedback ([5af17b7](https://github.com/watson-developer-cloud/python-sdk/commit/5af17b7557b2bd3f178c17b7ba7de907c0a3045e))
* **TextToSpeechV1:** change voice model signaturess to custom models ([12ee072](https://github.com/watson-developer-cloud/python-sdk/commit/12ee072189d54a7b6462c82cb0e5d4d123822ea5))
* **VisRecV4:** change  start time and end time to date from string ([f2f40e7](https://github.com/watson-developer-cloud/python-sdk/commit/f2f40e7a6e9aa90f3938d576081998cb5667a0f8))


### BREAKING CHANGES

* **VisRecV4:** change start and end time for training usage to date time format
* **CompareComply:** remove before and after from list feedback
* **TextToSpeechV1:** This update breaks the users using any methods of type _voice_models

## [4.7.1](https://github.com/watson-developer-cloud/python-sdk/compare/v4.7.0...v4.7.1) (2020-09-03)


### Bug Fixes

* lock the cloud sdk library version ([18d5997](https://github.com/watson-developer-cloud/python-sdk/commit/18d5997faa44af4e3c11b217f598dd4e3c75115c))

# [4.7.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.6.0...v4.7.0) (2020-09-03)


### Features

* **DiscoveryV2:** add support for analyze document ([6353f53](https://github.com/watson-developer-cloud/python-sdk/commit/6353f53361f0c1998b746308a7713f1c0dbc172d))

# [4.6.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.5.0...v4.6.0) (2020-08-25)


### Features

* generate unit tests using current api defs ([99555f0](https://github.com/watson-developer-cloud/python-sdk/commit/99555f017a08fa42457fbebdaf4d03a854482683))
* regenrate all services using current api def ([9ef3c6e](https://github.com/watson-developer-cloud/python-sdk/commit/9ef3c6e2df323a2bb7403bef417ddbd34ca6b462))
* **AssistantV2:** add support for list logs and delete user data ([6b87f9b](https://github.com/watson-developer-cloud/python-sdk/commit/6b87f9bc834f9b23e62a1d7047e8024839a50e36))
* **discoV2:** add new apis for enrichments, collections and projects ([4388ea2](https://github.com/watson-developer-cloud/python-sdk/commit/4388ea276b5473b13249592127a51e2004a1d82c))
* **languageTranslatorV3:** add support for list languages ([de83e96](https://github.com/watson-developer-cloud/python-sdk/commit/de83e96e5d4b0a9f2221fc48ca38ef66b0a0c68d))

# [4.5.0](https://github.com/watson-developer-cloud/python-sdk/compare/v4.4.1...v4.5.0) (2020-06-04)


### Features

* regenerate services based on current API def ([c538bd2](https://github.com/watson-developer-cloud/python-sdk/commit/c538bd23b28c220cec2261e9d2a770ebedbba860))
* **AssistantV1:** add support for spelling suggestions ([858af78](https://github.com/watson-developer-cloud/python-sdk/commit/858af780c60edcff5e6c47281f23d3d9c5011861))
* **AssistantV2:** add support for stateless messages ([c57f248](https://github.com/watson-developer-cloud/python-sdk/commit/c57f248ea920c12bb439b5571ae78fcce144707b))
* **VisualRecognitionV4:** add support for downloading a model file ([fa2cd1b](https://github.com/watson-developer-cloud/python-sdk/commit/fa2cd1b8e8c0a867e6c509875418d8c32e9e4d06))

## [4.4.1](https://github.com/watson-developer-cloud/python-sdk/compare/v4.4.0...v4.4.1) (2020-05-11)


### Bug Fixes

* loading creds from top level directory ([03a3509](https://github.com/watson-developer-cloud/python-sdk/commit/03a3509f497dca9a534fc19cc59498ce80f2f51e))

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
