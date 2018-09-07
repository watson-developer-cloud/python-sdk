# coding=utf-8
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

# If service instance provides API key authentication
text_to_speech = TextToSpeechV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://stream.watsonplatform.net/text-to-speech/api',
    iam_apikey='your_apikey')

text_to_speech = TextToSpeechV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://stream.watsonplatform.net/text-to-speech/api,
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

print(json.dumps(text_to_speech.list_voices().get_result(), indent=2))

with open(join(dirname(__file__), '../resources/output.wav'),
          'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize('Hello world!', accept='audio/wav',
                                  voice="en-US_AllisonVoice").get_result().content)

print(json.dumps(text_to_speech.get_pronunciation('Watson', format='spr').get_result(), indent=2))

print(json.dumps(text_to_speech.list_voice_models().get_result(), indent=2))

# print(json.dumps(text_to_speech.create_customization('test-customization').get_result(),
#  indent=2))

# print(text_to_speech.update_customization('YOUR CUSTOMIZATION ID',
# name='new name').get_result())

# print(json.dumps(text_to_speech.get_customization('YOUR CUSTOMIZATION ID').get_result(),
#  indent=2))

# print(json.dumps(text_to_speech.get_customization_words('YOUR CUSTOMIZATION
#  ID').get_result(), indent=2))

# print(text_to_speech.add_customization_words('YOUR CUSTOMIZATION ID',
#                                              [{'word': 'resume',
# 'translation': 'rɛzʊmeɪ'}]).get_result())

# print(text_to_speech.set_customization_word('YOUR CUSTOMIZATION ID',
# word='resume',
#                                             translation='rɛzʊmeɪ').get_result())

# print(json.dumps(text_to_speech.get_customization_word('YOUR CUSTOMIZATION
# ID', 'resume').get_result(), indent=2))

# print(text_to_speech.delete_customization_word('YOUR CUSTOMIZATION ID',
# 'resume').get_result())

# print(text_to_speech.delete_customization('YOUR CUSTOMIZATION ID').get_result())
