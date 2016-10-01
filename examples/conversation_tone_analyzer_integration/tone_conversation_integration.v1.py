import json
import os
from dotenv import load_dotenv, find_dotenv
import asyncio

from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3

# import tone detection
import tone_detection

# load the .env file containing your environment variables for the required services (conversation and tone)
load_dotenv(find_dotenv())

# replace with your own conversation credentials or put them in a .env file
conversation = ConversationV1(
    username=os.environ.get('CONVERSATION_USERNAME') or 'YOUR SERVICE NAME',
    password=os.environ.get('CONVERSATION_PASSWORD') or 'YOUR PASSWORD',
    version='2016-09-20')

# replace with your own tone analyzer credentials
tone_analyzer = ToneAnalyzerV3(
    username=os.environ.get('TONE_ANALYZER_USERNAME') or 'YOUR SERVICE NAME',
    password=os.environ.get('TONE_ANALYZER_PASSWORD') or 'YOUR SERVICE NAME',
    version='2016-02-11')

# replace with your own workspace_id
workspace_id = os.environ.get('WORKSPACE_ID') or 'YOUR WORKSPACE ID'

# This example stores tone for each user utterance in conversation context.
# Change this to false, if you do not want to maintain history
maintainToneHistoryInContext = True

# Payload for the Watson Conversation Service
# user input text required - replace "I am happy" with user input text.
payload = {
    'workspace_id':workspace_id,
    'input': {
      'text': "I am happy"
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
    tone = tone_analyzer.tone(text=payload['input']['text'])
    conversation_payload =  tone_detection.updateUserTone(payload, tone, maintainToneHistoryInContext)
    response = conversation.message(workspace_id=workspace_id, message_input=conversation_payload['input'], context=conversation_payload['context'])
    print(json.dumps(response, indent=2))

async def invokeToneConversationAsync (payload, maintainToneHistoryInContext):
    tone = await tone_detection.invokeToneAsync(payload,tone_analyzer)
    conversation_payload =  tone_detection.updateUserTone(payload, tone, maintainToneHistoryInContext)
    response = conversation.message(workspace_id=workspace_id, message_input=conversation_payload['input'], context=conversation_payload['context'])
    print(json.dumps(response, indent=2))


# invoke tone aware calls to conversation - either synchronously or asynchronously

# synchronous call to conversation with tone included in the context
invokeToneConversation(payload,maintainToneHistoryInContext)

# asynchronous call to conversation with tone included in the context
loop = asyncio.get_event_loop()
loop.run_until_complete(invokeToneConversationAsync(payload,maintainToneHistoryInContext))
loop.close()

