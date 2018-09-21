from __future__ import print_function
import json
from watson_developer_cloud import AssistantV2

# If service instance provides API key authentication
# assistant = AssistantV2(
#     version='2017-04-21',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/assistant/api',
#     iam_apikey='iam_apikey')

assistant = AssistantV2(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/assistant/api',
    version='2017-04-21')

#########################
# Sessions
#########################

session = assistant.create_session("<YOUR ASSISTANT ID>").get_result()
print(json.dumps(session, indent=2))

assistant.delete_session("<YOUR ASSISTANT ID>", "<YOUR SESSION ID>").get_result()

#########################
# Message
#########################

message = assistant.message(
    "<YOUR ASSISTANT ID>",
    "<YOUR SESSION ID>",
    input={'text': 'What\'s the weather like?'},
    context={
        'metadata': {
            'deployment': 'myDeployment'
        }
    }).get_result()
print(json.dumps(message, indent=2))
