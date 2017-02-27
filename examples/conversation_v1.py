import json
from watson_developer_cloud import ConversationV1

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
