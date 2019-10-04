Here are simple steps to move from `v3.0.0` to `v4.0.0`. Note that `v4.0,0` supports only python `3.5` and above

## AUTHENTICATION MECHANISM
The constructor no longer accepts individual credentials like `iam_apikey`, etc. We initialize authenticators from the [core](https://github.com/IBM/python-sdk-core). The core supports various authentication mechanisms, choose the one appropriate to your instance and use case.

For example, to pass a IAM apikey:
#### Before
```python
from ibm_watson import MyService

service = MyService(
    iam_apikey='{apikey}',
    url='{url}'
)
```

#### After(V4.0)
```python
from ibm_watson import MyService
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('{apikey}')
service = MyService(
    authenticator=authenticator
)
service.set_service_url('{url}')
```

There are 5 authentication variants supplied in the SDK (shown below), and it's possible now to create your own authentication implementation if you need something specific by implementing the Authenticator implementation.

#### BasicAuthenticator
```python
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator(<your_username>, <your_password>)
service = MyService(authenticator=authenticator)
```

#### BearerTokenAuthenticator
```python
from ibm_cloud_sdk_core.authenticators import BearerTokenAuthenticator

authenticator = BearerTokenAuthenticator(<your_bearer_token>)
service = MyService(authenticator=authenticator)

# can set bearer token
service.get_authenticator().set_bearer_token('xxx');
```

#### CloudPakForDataAuthenticator
```python
from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator

authenticator = CloudPakForDataAuthenticator(
                 'my_username',
                 'my_password',
                 'https://my-cp4d-url',
                 disable_ssl_verification=True)
service = MyService(authenticator=authenticator)
```

#### IAMAuthenticator
```python
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('my_apikey')
service = MyService(authenticator=authenticator)
```

#### NoAuthAuthenticator
```python
from ibm_cloud_sdk_core.authenticators import NoAuthAuthenticator

authenticator = NoAuthAuthenticator()
service = MyService(authenticator=authenticator)
```

#### Creating an Authenticator from Environmental Configuration
```python
from ibm_cloud_sdk_core import get_authenticator_from_environment

authenticator = get_authenticator_from_environment('Assistant')
service = MyService(authenticator=authenticator)
```

## SETTING THE SERVICE URL
We can set the service url using `set_service_url()` or from external configurations.

#### Before
```python
service = MyService(
    iam_apikey='{apikey}',
    url='{url}' # <= here
)
```

#### After(V4.0)
```python
service = MyService(
    authenticator=authenticator,
)
service.set_service_url('{url}')
```

OR, pass from external configurations like environment variable
```bash
export MY_SERVICE_URL="<your url>"
```

## METHOD OPTIONAL PARAM
The method params which are optional would need to be specified by name rather than position. For example

#### Before
The list_workspaces with page_limit as 10 was:

```python
assistant_service.list_workspaces(10)
```

#### After(V4.0)
We need to specify the optional param name:

```python
assistant_service.list_workspaces(page_limit=10)
```

## DISABLING SSL VERIFICATION
#### Before
```python
service.disable_ssl_verification(True)
```

#### After(v4.0)
```python
service.set_disable_ssl_verification(True)
```

## SUPPORT FOR CONSTANTS
Constants for methods and models are shown in the form of Enums

## SUPPORT FOR PYTHON 2.7 and 3.4 AND BELOW DROPPED
The SDK no longer supports Pyhton versions 2.7 and <=3.4.

## SERVICE CHANGES
#### AssistantV1
* `include_count` is no longer a parameter of the list_workspaces() method
* `include_count` is no longer a parameter of the list_intents() method
* `include_count` is no longer a parameter of the list_examples() method
* `include_count` is no longer a parameter of the list_counterexamples() method
* `include_count` is no longer a parameter of the list_entities() method
* `include_count` is no longer a parameter of the list_values() method
* `include_count` is no longer a parameter of the list_synonyms() method
* `include_count` is no longer a parameter of the list_dialog_nodes() method
* `value_type` was renamed to `type` in the create_value() method
* `new_value_type` was renamed to `new_type` in the update_value() method
* `node_type` was renamed to `type` in the create_dialog_node() method
* `new_node_type` was renamed to `new_type` in the update_dialog_node() method
* `value_type` was renamed to `type` in the CreateValue model
* `node_type` was renamed to `type` in the DialogNode model
* `action_type` was renamed to `type` in the DialogNodeAction model
* `query_type` property was added to the DialogNodeOutputGeneric model
* `query` property was added to the DialogNodeOutputGeneric model
* `filter` property was added to the DialogNodeOutputGeneric model
* `discovery_version` property was added to the DialogNodeOutputGeneric model
* LogMessage model no longer has `_additionalProperties`
* `DialogRuntimeResponseGeneric` was renamed to `RuntimeResponseGeneric`
* RuntimeEntity model no longer has `_additionalProperties`
* RuntimeIntent model no longer has `_additionalProperties`
* `value_type` was renamed to `type` in the Value model

#### AssistantV2
* `action_type` was renamed to `type` in the DialogNodeAction model
* DialogRuntimeResponseGeneric was renamed to RuntimeResponseGeneric

#### Compare and Comply
* `convert_to_html()` method does not require a filename parameter

#### DiscoveryV1
* `return_fields` was renamed to `return_` in the query() method
* `logging_opt_out` was renamed to `x_watson_logging_opt_out` in the query() method
* `spelling_suggestions` was added to the query() method
* `collection_ids` is no longer a parameter of the query() method
* `return_fields` was renamed to `return_` in the QueryNotices() method
* `logging_opt_out` was renamed to `x_watson_logging_opt_out` in the federated_query() method
* `collection_ids` is now required in the federated_query() method
* `collection_ids` changed position in the federated_query() method
* `return_fields` was renamed to `return_` in the federated_query() method
* `return_fields` was renamed to `return_` in the federated_query_notices() method
* `enrichment_name` was renamed to `enrichment` in the Enrichment model
* `field_type` was renamed to `type` in the Field model
* `field_name` was renamed to `field` in the Field model
* test_configuration_in_environment() method was removed
* query_entities() method was removed
* query_relations() method was removed

#### Language Translator V3
* `default_models` was renamed to `default` in the list_models() method
* `translation_output` was renamed to `translation` in the Translation model

#### Natural Language Classifier V1
* `metadata` was renamed to `training_metadata` in the `create_classifier()` method

#### Speech to Text V1
* `final_results` was renamed to `final` in the SpeakerLabelsResult model
* `final_results` was renamed to `final` in the SpeechRecognitionResult model

#### Visual Recognition V3
* `detect_faces()` method was removed
* `class_name` was renamed to `class_` in the ClassResult model
* `class_name` was renamed to `class_` in the ModelClass model

#### Visual Recognition V4
* New Service!


