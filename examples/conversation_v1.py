import json
from watson_developer_cloud import ConversationV1


conversation = ConversationV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2016-07-11')

# replace with your own workspace_id
workspace_id = '293b58fc-3c5b-4ac5-a8f4-8d52c393d875'

response = conversation.message(workspace_id=workspace_id, message_input={'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))
