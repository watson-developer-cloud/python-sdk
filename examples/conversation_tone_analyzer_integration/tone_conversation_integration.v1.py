import json
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3

# import tone detection
import tone_detection

# replace with your own conversation credentials
conversation = ConversationV1(
    username='YOUR SERVICE NAME', # YOUR SERVICE NAME
    password='YOUR PASSWORD',
    version='2016-07-11')

# replace with your own tone analyzer credentials
tone_analyzer = ToneAnalyzerV3(
    username='YOUR SERVICE NAME',
    password='YOUR PASSWORD',
    version='2016-02-11')

# replace with your own workspace_id
# the process.env probably won't work with python
workspace_id = process.env.WORKSPACE_ID or 'YOUR WORKSPACE ID'

# This example stores tone for each user utterance in conversation context.
# Change this to false, if you do not want to maintain history
maintainToneHistoryInContext = true

# Payload for the Watson Conversation Service
# <workspace-id> and user input text required.
payload = {
    'workspace_id':workspace_id,
    'input': {
      'text': "I am not happy today :("
    }
}

def invokeToneConversation (payload, maintainToneHistoryInContext):
    '''
     invokeToneConversation calls the the Tone Analyzer service to get the tone information for the user's
     input text (input['text'] in the payload json object), adds/updates the user's tone in the payload's context,
     and sends the payload to the conversation service to get a response which is printed to screen.
     :param payload: a json object containing the basic information needed to converse with the Conversation Service's message endpoint.
     :param maintainHistoryInContext:


     Note: as indicated below, the console.log statements can be replaced with application-specific code to process the err or data object returned by the Conversation Service.
    '''

    tone = tone_analyzer.tone({'text': payload['input']['text']})
    conversation_payload =  tone_detection.updateUserTone(payload, tone, maintainToneHistoryInContext)
    response = conversation.message(workspace_id=workspace_id, message_input=conversation_payload)
    print(json.dumps(response, indent=2))

invokeToneConversation(payload,maintainToneHistoryInContext);