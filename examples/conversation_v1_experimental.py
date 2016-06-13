import json
from watson_developer_cloud import ConversationV1Experimental


conversation = ConversationV1Experimental(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    version='2016-05-09')

# replace with your own workspace_id
workspace_id = '25dfa8a0-0263-471b-8980-317e68c30488'

response = conversation.message(workspace_id=workspace_id, message_input={'text': 'What\'s the weather like?'})
print(json.dumps(response, indent=2))
