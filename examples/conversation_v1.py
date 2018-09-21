from __future__ import print_function
import json
from watson_developer_cloud import ConversationV1

## If service instance provides API key authentication
# conversation = ConversationV1(
#     version='2018-07-10',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/conversation/api',
#     iam_apikey='iam_apikey')

conversation = ConversationV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/conversation/api',
    version='2018-07-10')

# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))

#########################
# workspaces
#########################

create_workspace_data = {
    "name":
    "test_workspace",
    "description":
    "integration tests",
    "language":
    "en",
    "intents": [{
        "intent": "hello",
        "description": "string",
        "examples": [{
            "text": "good morning"
        }]
    }],
    "entities": [{
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "metadata": {
            "property": "value"
        }
    }],
    "counterexamples": [{
        "text": "string"
    }],
    "metadata": {},
}

response = conversation.create_workspace(
    name=create_workspace_data['name'],
    description=create_workspace_data['description'],
    language='en',
    intents=create_workspace_data['intents'],
    entities=create_workspace_data['entities'],
    counterexamples=create_workspace_data['counterexamples'],
    metadata=create_workspace_data['metadata']).get_result()
print(json.dumps(response, indent=2))

workspace_id = response['workspace_id']
print('Workspace id {0}'.format(workspace_id))

response = conversation.get_workspace(
    workspace_id=workspace_id, export=True).get_result()
print(json.dumps(response, indent=2))

#  message
response = conversation.message(
    workspace_id=workspace_id, input={
        'text': 'What\'s the weather like?'
    }).get_result()
print(json.dumps(response, indent=2))

response = conversation.list_workspaces().get_result()
print(json.dumps(response, indent=2))

response = conversation.update_workspace(
    workspace_id=workspace_id,
    description='Updated test workspace.').get_result()
print(json.dumps(response, indent=2))

# see cleanup section below for delete_workspace example

#########################
# intents
#########################

examples = [{"text": "good morning"}]
response = conversation.create_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    description='Test intent.',
    examples=examples).get_result()
print(json.dumps(response, indent=2))

response = conversation.get_intent(
    workspace_id=workspace_id, intent='test_intent', export=True).get_result()
print(json.dumps(response, indent=2))

response = conversation.list_intents(
    workspace_id=workspace_id, export=True).get_result()
print(json.dumps(response, indent=2))

response = conversation.update_intent(
    workspace_id=workspace_id,
    intent='test_intent',
    new_intent='updated_test_intent',
    new_description='Updated test intent.').get_result()
print(json.dumps(response, indent=2))

# see cleanup section below for delete_intent example

#########################
# examples
#########################

response = conversation.create_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni').get_result()
print(json.dumps(response, indent=2))

response = conversation.get_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni').get_result()
print(json.dumps(response, indent=2))

response = conversation.list_examples(
    workspace_id=workspace_id, intent='updated_test_intent').get_result()
print(json.dumps(response, indent=2))

response = conversation.update_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni',
    new_text='Gimme a pizza with pepperoni').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_example(
    workspace_id=workspace_id,
    intent='updated_test_intent',
    text='Gimme a pizza with pepperoni').get_result()
print(json.dumps(response, indent=2))

#########################
# counterexamples
#########################

response = conversation.create_counterexample(
    workspace_id=workspace_id,
    text='I want financial advice today.').get_result()
print(json.dumps(response, indent=2))

response = conversation.get_counterexample(
    workspace_id=workspace_id,
    text='I want financial advice today.').get_result()
print(json.dumps(response, indent=2))

response = conversation.list_counterexamples(
    workspace_id=workspace_id).get_result()
print(json.dumps(response, indent=2))

response = conversation.update_counterexample(
    workspace_id=workspace_id,
    text='I want financial advice today.',
    new_text='I want financial advice today.').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_counterexample(
    workspace_id=workspace_id,
    text='I want financial advice today.').get_result()
print(json.dumps(response, indent=2))

#########################
# entities
#########################

values = [{"value": "juice"}]
response = conversation.create_entity(
    workspace_id=workspace_id,
    entity='test_entity',
    description='A test entity.',
    values=values).get_result()
print(json.dumps(response, indent=2))

entities = [{
    'entity':
    'pattern_entity',
    'values': [{
        'value': 'value0',
        'patterns': ['\\d{6}\\w{1}\\d{7}'],
        'value_type': 'patterns'
    }, {
        'value':
        'value1',
        'patterns':
        ['[-9][0-9][0-9][0-9][0-9]~! [1-9][1-9][1-9][1-9][1-9][1-9]'],
        'value_type':
        'patterns'
    }, {
        'value': 'value2',
        'patterns': ['[a-z-9]{17}'],
        'value_type': 'patterns'
    }, {
        'value':
        'value3',
        'patterns': [
            '\\d{3}(\\ |-)\\d{3}(\\ |-)\\d{4}',
            '\\(\\d{3}\\)(\\ |-)\\d{3}(\\ |-)\\d{4}'
        ],
        'value_type':
        'patterns'
    }, {
        'value': 'value4',
        'patterns': ['\\b\\d{5}\\b'],
        'value_type': 'patterns'
    }]
}]
response = conversation.create_entity(
    workspace_id, entity=entities[0]['entity'],
    values=entities[0]['values']).get_result()
print(json.dumps(response, indent=2))

response = conversation.get_entity(
    workspace_id=workspace_id, entity=entities[0]['entity'],
    export=True).get_result()
print(json.dumps(response, indent=2))

response = conversation.list_entities(workspace_id=workspace_id).get_result()
print(json.dumps(response, indent=2))

response = conversation.update_entity(
    workspace_id=workspace_id,
    entity='test_entity',
    new_description='An updated test entity.').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_entity(
    workspace_id=workspace_id, entity='test_entity').get_result()
print(json.dumps(response, indent=2))

#########################
# synonyms
#########################

values = [{"value": "orange juice"}]
conversation.create_entity(workspace_id, 'beverage', values=values)

response = conversation.create_synonym(workspace_id, 'beverage', 'orange juice',
                                       'oj').get_result()
print(json.dumps(response, indent=2))

response = conversation.get_synonym(workspace_id, 'beverage', 'orange juice',
                                    'oj').get_result()
print(json.dumps(response, indent=2))

response = conversation.list_synonyms(workspace_id, 'beverage',
                                      'orange juice').get_result()
print(json.dumps(response, indent=2))

response = conversation.update_synonym(workspace_id, 'beverage', 'orange juice',
                                       'oj', 'OJ').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_synonym(workspace_id, 'beverage', 'orange juice',
                                       'OJ').get_result()
print(json.dumps(response, indent=2))

conversation.delete_entity(workspace_id, 'beverage')

#########################
# values
#########################

conversation.create_entity(workspace_id, 'test_entity')

response = conversation.create_value(workspace_id, 'test_entity',
                                     'test').get_result()
print(json.dumps(response, indent=2))

response = conversation.get_value(workspace_id, 'test_entity',
                                  'test').get_result()
print(json.dumps(response, indent=2))

response = conversation.list_values(workspace_id, 'test_entity').get_result()
print(json.dumps(response, indent=2))

response = conversation.update_value(workspace_id, 'test_entity', 'test',
                                     'example').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_value(workspace_id, 'test_entity',
                                     'example').get_result()
print(json.dumps(response, indent=2))

conversation.delete_entity(workspace_id, 'test_entity')

#########################
# Dialog nodes
#########################
create_dialog_node = {
    "dialog_node":
    "greeting",
    "description":
    "greeting messages",
    "actions": [{
        "name": "hello",
        "type": "client",
        "parameters": {},
        "result_variable": "string",
        "credentials": "string"
    }]
}
response = conversation.create_dialog_node(
    workspace_id,
    create_dialog_node['dialog_node'],
    create_dialog_node['description'],
    actions=create_dialog_node['actions']).get_result()
print(json.dumps(response, indent=2))

response = conversation.get_dialog_node(
    workspace_id, create_dialog_node['dialog_node']).get_result()
print(json.dumps(response, indent=2))

response = conversation.list_dialog_nodes(workspace_id).get_result()
print(json.dumps(response, indent=2))

response = conversation.update_dialog_node(
    workspace_id,
    create_dialog_node['dialog_node'],
    new_dialog_node='updated_node').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_dialog_node(workspace_id,
                                           'updated_node').get_result()
print(json.dumps(response, indent=2))

#########################
# logs
#########################

response = conversation.list_logs(workspace_id=workspace_id).get_result()
print(json.dumps(response, indent=2))

#########################
# clean-up
#########################

response = conversation.delete_intent(
    workspace_id=workspace_id, intent='updated_test_intent').get_result()
print(json.dumps(response, indent=2))

response = conversation.delete_workspace(workspace_id=workspace_id).get_result()
print(json.dumps(response, indent=2))
