import json
import os
from dotenv import load_dotenv, find_dotenv

from ibm_watson import AssistantV1
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# import tone detection
import tone_detection

# load the .env file containing your environment variables for the required
# services (conversation and tone)
load_dotenv(find_dotenv())

# replace with your own assistant credentials or put them in a .env file
assistant_authenticator = IAMAuthenticator(os.environ.get('ASSISTANT_APIKEY') or 'YOUR ASSISTANT APIKEY')
assistant = AssistantV1(
    version='2018-07-10',
    authenticator=assistant_authenticator)

# replace with your own tone analyzer credentials
tone_analyzer_authenticator = IAMAuthenticator(os.environ.get('TONE_ANALYZER_APIKEY') or 'YOUR TONE ANALYZER APIKEY')
tone_analyzer = ToneAnalyzerV3(
    version='2016-05-19',
    authenticator=tone_analyzer_authenticator)

# replace with your own workspace_id
workspace_id = os.environ.get('WORKSPACE_ID') or 'YOUR WORKSPACE ID'

# This example stores tone for each user utterance in conversation context.
# Change this to false, if you do not want to maintain history
global_maintainToneHistoryInContext = True

# Payload for the Watson Conversation Service
# user input text required - replace "I am happy" with user input text.
global_payload = {
    'workspace_id': workspace_id,
    'input': {
        'text': "I am happy"
    }
}


def invokeToneConversation(payload, maintainToneHistoryInContext):
    """
     invokeToneConversation calls the Tone Analyzer service to get the
     tone information for the user's input text (input['text'] in the payload
     json object), adds/updates the user's tone in the payload's context,
     and sends the payload to the
     conversation service to get a response which is printed to screen.
     :param payload: a json object containing the basic information needed to
     converse with the Conversation Service's message endpoint.
     :param maintainHistoryInContext:


     Note: as indicated below, the console.log statements can be replaced
     with application-specific code to process the err or data object
     returned by the Conversation Service.
    """
    tone = tone_analyzer.tone(tone_input=payload['input'], content_type='application/json').get_result()
    conversation_payload = tone_detection.\
        updateUserTone(payload, tone, maintainToneHistoryInContext)
    response = assistant.message(workspace_id=workspace_id,
                                 input=conversation_payload['input'],
                                 context=conversation_payload['context']).get_result()
    print(json.dumps(response, indent=2))


# synchronous call to conversation with tone included in the context
invokeToneConversation(global_payload, global_maintainToneHistoryInContext)
