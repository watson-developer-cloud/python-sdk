# Upgrading to ibm-watson@8.0
 [Breaking Changes](#breaking-changes)
  - [Breaking changes by service](#breaking-changes-by-service)

- [New Features by Service](#new-features-by-service)

### Breaking changes by service

#### Assistant v2
- Parameter `createSession` removed from `createSession` function
- Class `Environment` property `language` removed
- Class `EnvironmentReleaseReference` renamed to `BaseEnvironmentReleaseReference`
- Class `EnvironmentOrchestration` renamed to `BaseEnvironmentOrchestration`
- Class `SkillReference` renamed to `EnvironmentSkill`

#### Discovery v2
- Parameter `smartDocumentUnderstanding` removed from `createCollection` function
- Class `QueryResponsePassage` and `QueryResultPassage` property `confidence` removed
- Class `DocumentClassifierEnrichment` property `enrichmentId` is no longer an optional
- QueryAggregation classes restructured

#### Natural Language Understanding
- All `sentiment_model` functions removed
- `create_classifications_model`, `update_classifications_model`, `create_categories_model`, and `update_categories_model` now require `training_data_content_type`

#### Speech to Text
- `AR_AR_BROADBANDMODEL` model removed in favor of `AR_MS_BROADBANDMODEL` model

### New Features by Service

#### Assistant v2
- `create_assistant` function
- `list_assistants` function
- `delete_assistant` function
- `update_environment` function
- `create_release` function
- `delete_release` function
- `get_skill` function
- `update_skill` function
- `export_skills` function
- `import_skills` function
- `import_skills_status` function
- Improved typing for `message` function call
See details of these functions on IBM's documentation site [here](https://cloud.ibm.com/apidocs/assistant-v2?code=python)

#### Discovery v2
- Aggregation types `QueryTopicAggregation` and `QueryTrendAggregation` added

#### Speech to Text
- added `FR_CA_MULTIMEDIA`, `JA_JP_TELEPHONY`, `NL_NL_MULTIMEDIA`, `SV_SE_TELEPHONY` models

#### Text to Speech
- added `EN_AU_HEIDIEXPRESSIVE`, `EN_AU_JACKEXPRESSIVE`, `EN_US_ALLISONEXPRESSIVE`, `EN_US_EMMAEXPRESSIVE`, `EN_US_LISAEXPRESSIVE`, `EN_US_MICHAELEXPRESSIVE`, `KO_KR_JINV3VOICE`
- Parameters `rate_percentage` and `pitch_percentage` added to `synthesize` function
See details of these new parameters on IBM's documentation site [here](https://cloud.ibm.com/apidocs/text-to-speech?code=python#synthesize)
