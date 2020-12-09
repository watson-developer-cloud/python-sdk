## Python SDK V5 Migration guide

### Service changes

#### Assistant v1

* `include_count` is now a parameter of the `list_workspaces()` method
* `include_count` is now a parameter of the `list_intents()` method
* `include_count` is now a parameter of the `list_examples()` method
* `include_count` is now a parameter of the `list_counterexamples()` method
* `include_count` is now a parameter of the `list_entities()` method
* `include_count` is now a parameter of the `list_values()` method
* `include_count` is now a parameter of the `list_synonyms()` method
* `include_count` is now a parameter of the `list_dialogNodes()` method
* `context` type was changed from `dict` to `DialogNodeContext` in the `create_dialog_node()` method
* `new_context` type was changed from `dict` to `DialogNodeContext` in the `update_dialog_node()` method
* `bulk_classify()` method was addded

##### Models Added

`BulkClassifyOutput`,
`BulkClassifyResponse`,
`BulkClassifyUtterance`,
`DialogNodeContext`,
`DialogNodeOutputConnectToAgentTransferInfo`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypeImage`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypeOption`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypePause`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill`,
`DialogNodeOutputGenericDialogNodeOutputResponseTypeText`,
`RuntimeResponseGenericRuntimeResponseTypeConnectToAgent`,
`RuntimeResponseGenericRuntimeResponseTypeImage`,
`RuntimeResponseGenericRuntimeResponseTypeOption`,
`RuntimeResponseGenericRuntimeResponseTypePause`,
`RuntimeResponseGenericRuntimeResponseTypeSuggestion`,
`RuntimeResponseGenericRuntimeResponseTypeText`

##### Models Removed

`DialogSuggestionOutput`,
`DialogSuggestionResponseGeneric`

##### Model Properties Changed

`DialogNode`
* `context` property type changed from `Dictionary<string, object>` to `DialogNodeContext`

`DialogNodeOutput`
* Added `Integrations` property with getter and setter

`DialogNodeOutputGeneric`, `RuntimeResponseGeneric`
* Added `agent_available`, `agent_unavailable`, and `transfer_info` properties

`DialogSuggestion`
* `output` property type changed from `DialogSuggestionOutput` to `Dictionary<string, object>`

#### Assistant v2

* `bulk_classify()` method was addded

##### Models Added

`BulkClassifyOutput`,
`BulkClassifyResponse`,
`BulkClassifyUtterance`,
`DialogNodeOutputConnectToAgentTransferInfo`,
`RuntimeResponseGenericRuntimeResponseTypeConnectToAgent`,
`RuntimeResponseGenericRuntimeResponseTypeImage`,
`RuntimeResponseGenericRuntimeResponseTypeOption`,
`RuntimeResponseGenericRuntimeResponseTypePause`,
`RuntimeResponseGenericRuntimeResponseTypeSearch`,
`RuntimeResponseGenericRuntimeResponseTypeSuggestion`,
`RuntimeResponseGenericRuntimeResponseTypeText`

##### Model Properties Changed

`MessageContext`, `MessageContextStateless`
* `Skills` property type changed from `MessageContextSkills` to `Dictionary<string, MessageContextSkill>`

`MessageContextSkill`
* `System` property type changed from `Dictionary<string, object>` to `MessageContextSkillSystem`

`RuntimeResponseGeneric`
* Added `agent_available`, `agent_unavailable`, and `transfer_info` properties

#### Compare Comply v1

* `before` and `after` parameters were removed from `list_feedback` method

##### Model Properties Changed

`Category`, `TypeLabel`
* Added `modification` property

`OriginalLabelsOut`, `UpdatedLabelsOut`
* Removed `modification` property

#### Discovery v1

No changes

#### Discovery v2

##### Models Added

`QueryResponsePassage`

##### Models Removed

`QueryNoticesResult`

##### Model Properties Changed

`QueryResponse`
* Added `Passages` property

#### Language Translator v3

No changes

#### Natural Language Classifier v1

No changes

#### Natural Language Understanding v1

No changes

#### Personality Insights

No changes

#### Speech To Text v1

No changes

#### Text To Speech v1

* Renamed `CreateVoiceModel()` method to `CreateCustomModel()`

* Renamed `ListVoiceModels()` method to `ListCustomModels()`

* Renamed `UpdateVoiceModel()` method to `UpdateCustomModel()`

* Renamed `GetVoiceModel()` method to `GetCustomModel()`

* Renamed `DeleteVoiceModel()` method to `GetCustomModel()`

##### Models Added

`CustomModel`,
`CustomModels`

##### Models Removed

`VoiceModel`,
`VoiceModels`

##### Model Properties Changed

`Voice`
* Change return type of `customization` from `VoiceModel` to `CustomModel`

#### Tone Analyzer v3

No changes

#### Visual Recognition v3

No changes

#### Visual Recognition v4

* Changed `start_time` and `end_time` parameter types from `string` to `date` in `get_training_usage()` method