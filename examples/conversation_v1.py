import json
from watson_developer_cloud import ConversationV1

#########################
# message
#########################

conversation = ConversationV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2016-09-20')

# replace with your own workspace_id
workspace_id = '0a0c06c1-8e31-4655-9067-58fcac5134fc'

response = conversation.message(workspace_id=workspace_id, message_input={
    'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))

# When you send multiple requests for the same conversation, include the
# context object from the previous response.
# response = conversation.message(workspace_id=workspace_id, message_input={
# 'text': 'turn the wipers on'},
#                                context=response['context'])
# print(json.dumps(response, indent=2))

#########################
# workspaces
#########################

response = conversation.create_workspace(name='test_workspace',
                                         description='Test workspace.',
                                         language='en',
                                         metadata={})
print(json.dumps(response, indent=2))

workspace_id = response['workspace_id']

response = conversation.get_workspace(workspace_id=workspace_id, export=True)
print(json.dumps(response, indent=2))

response = conversation.list_workspaces()
print(json.dumps(response, indent=2))

response = conversation.update_workspace(workspace_id=workspace_id,
                                         description='Updated test workspace.')
print(json.dumps(response, indent=2))

# see cleanup section below for delete_workspace example

#########################
# intents
#########################

response = conversation.create_intent(workspace_id=workspace_id,
                                      intent='test_intent',
                                      description='Test intent.')
print(json.dumps(response, indent=2))

response = conversation.get_intent(workspace_id=workspace_id,
                                   intent='test_intent',
                                   export=True)
print(json.dumps(response, indent=2))

response = conversation.list_intents(workspace_id=workspace_id,
                                     export=True)
print(json.dumps(response, indent=2))

response = conversation.update_intent(workspace_id=workspace_id,
                                      intent='test_intent',
                                      new_intent='updated_test_intent',
                                      new_description='Updated test intent.')
print(json.dumps(response, indent=2))

# see cleanup section below for delete_intent example

#########################
# examples
#########################

response = conversation.create_example(workspace_id=workspace_id,
                                       intent='updated_test_intent',
                                       text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = conversation.get_example(workspace_id=workspace_id,
                                    intent='updated_test_intent',
                                    text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = conversation.list_examples(workspace_id=workspace_id,
                                      intent='updated_test_intent')
print(json.dumps(response, indent=2))

response = conversation.update_example(workspace_id=workspace_id,
                                       intent='updated_test_intent',
                                       text='Gimme a pizza with pepperoni',
                                       new_text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

response = conversation.delete_example(workspace_id=workspace_id,
                                       intent='updated_test_intent',
                                       text='Gimme a pizza with pepperoni')
print(json.dumps(response, indent=2))

#########################
# counterexamples
#########################

response = conversation.create_counterexample(workspace_id=workspace_id,
                                              text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = conversation.get_counterexample(workspace_id=workspace_id,
                                           text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = conversation.list_counterexamples(workspace_id=workspace_id)
print(json.dumps(response, indent=2))

response = conversation.update_counterexample(workspace_id=workspace_id,
                                              text='I want financial advice today.',
                                              new_text='I want financial advice today.')
print(json.dumps(response, indent=2))

response = conversation.delete_counterexample(workspace_id=workspace_id,
                                              text='I want financial advice today.')
print(json.dumps(response, indent=2))

#########################
# clean-up
#########################

response = conversation.delete_intent(workspace_id=workspace_id,
                                      intent='updated_test_intent')
print(json.dumps(response, indent=2))

response = conversation.delete_workspace(workspace_id=workspace_id)
print(json.dumps(response, indent=2))
