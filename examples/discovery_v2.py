import json
import os
from ibm_watson import DiscoveryV2
from ibm_watson.discovery_v2 import TrainingExample
from ibm_cloud_sdk_core.authenticators import CloudPakForDataAuthenticator, BearerTokenAuthenticator

## Important: Discovery v2 is only available on Cloud Pak for Data. ##

## Authentication ##
## Option 1: username/password
authenticator = CloudPakForDataAuthenticator('<your username>',
                                             '<your password>',
                                             '<url for authentication>',
                                             disable_ssl_verification=True)

## Option 2: bearer token
authenticator = BearerTokenAuthenticator('your bearer token')

## Initialize discovery instance ##
discovery = DiscoveryV2(version='2019-11-22', authenticator=authenticator)
discovery.set_service_url(
    '<service url>'
)
discovery.set_disable_ssl_verification(True)

PROJECT_ID = 'your project id'
## List Collections ##
collections = discovery.list_collections(project_id=PROJECT_ID).get_result()
print(json.dumps(collections, indent=2))

## Component settings ##
settings_result = discovery.get_component_settings(
    project_id=PROJECT_ID).get_result()
print(json.dumps(settings_result, indent=2))

## Add Document ##
COLLECTION_ID = 'your collection id'
with open(os.path.join(os.getcwd(), '..', 'resources',
                       'simple.html')) as fileinfo:
    add_document_result = discovery.add_document(project_id=PROJECT_ID,
                                                 collection_id=COLLECTION_ID,
                                                 file=fileinfo).get_result()
print(json.dumps(add_document_result, indent=2))
document_id = add_document_result.get('document_id')

## Create Training Data ##
training_example = TrainingExample(document_id=document_id,
                                   collection_id=COLLECTION_ID,
                                   relevance=1)
create_query = discovery.create_training_query(
    project_id=PROJECT_ID,
    natural_language_query='How is the weather today?',
    examples=[training_example]).get_result()
print(json.dumps(create_query, indent=2))

training_queries = discovery.list_training_queries(
    project_id=PROJECT_ID).get_result()
print(json.dumps(training_queries, indent=2))

## Queries ##
query_result = discovery.query(
    project_id=PROJECT_ID,
    collection_ids=[COLLECTION_ID],
    natural_language_query='How is the weather today?').get_result()
print(json.dumps(query_result, indent=2))

autocomplete_result = discovery.get_autocompletion(
    project_id=PROJECT_ID, prefix="The content").get_result()
print(json.dumps(autocomplete_result, indent=2))

query_notices_result = discovery.query_notices(
    project_id=PROJECT_ID, natural_language_query='warning').get_result()
print(json.dumps(query_notices_result, indent=2))

list_fields = discovery.list_fields(project_id=PROJECT_ID).get_result()
print(json.dumps(list_fields, indent=2))

## Cleanup ##
discovery.delete_training_queries(project_id=PROJECT_ID).get_result()

delete_document_result = discovery.delete_document(
    project_id=PROJECT_ID, collection_id=COLLECTION_ID,
    document_id=document_id).get_result()
print(json.dumps(delete_document_result, indent=2))
