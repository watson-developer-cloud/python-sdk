# coding=utf-8
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud.websocket import SynthesizeCallback

# If service instance provides API key authentication
# service = TextToSpeechV1(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://stream.watsonplatform.net/text-to-speech/api',
#     iam_apikey='your_apikey')

service = TextToSpeechV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://stream.watsonplatform.net/text-to-speech/api,
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

voices = service.list_voices().get_result()
print(json.dumps(voices, indent=2))

with open(join(dirname(__file__), '../resources/output.wav'),
          'wb') as audio_file:
    response = service.synthesize(
        'Hello world!', accept='audio/wav',
        voice="en-US_AllisonVoice").get_result()
    audio_file.write(response.content)

pronunciation = service.get_pronunciation('Watson', format='spr').get_result()
print(json.dumps(pronunciation, indent=2))

voice_models = service.list_voice_models().get_result()
print(json.dumps(voice_models, indent=2))

# voice_model = service.create_voice_model('test-customization').get_result()
# print(json.dumps(voice_model, indent=2))

# updated_voice_model = service.update_voice_model(
#     'YOUR CUSTOMIZATION ID', name='new name').get_result()
# print(updated_voice_model)

# voice_model = service.get_voice_model('YOUR CUSTOMIZATION ID').get_result()
# print(json.dumps(voice_model, indent=2))

# words = service.list_words('YOUR CUSTOMIZATIONID').get_result()
# print(json.dumps(words, indent=2))

# words = service.add_words('YOUR CUSTOMIZATION ID', [{
#     'word': 'resume',
#     'translation': 'rɛzʊmeɪ'
# }]).get_result()
# print(words)

# word = service.add_word(
#     'YOUR CUSTOMIZATION ID', word='resume', translation='rɛzʊmeɪ').get_result()
# print(word)

# word = service.get_word('YOUR CUSTOMIZATIONID', 'resume').get_result()
# print(json.dumps(word, indent=2))

# response = service.delete_word('YOUR CUSTOMIZATION ID', 'resume').get_result()
# print(response)

# response = service.delete_voice_model('YOUR CUSTOMIZATION ID').get_result()
# print(response)

# Synthesize using websocket. Note: The service accepts one request per connection
file_path = join(dirname(__file__), "../resources/dog.wav")
class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.fd = open(file_path, 'ab')

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_content_type(self, content_type):
        print('Content type: {}'.format(content_type))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.fd.write(audio_stream)

    def on_close(self):
        self.fd.close()
        print('Done synthesizing. Closing the connection')

my_callback = MySynthesizeCallback()
service.synthesize_using_websocket('I like to pet dogs',
                                   my_callback,
                                   accept='audio/wav',
                                   voice='en-US_AllisonVoice'
                                  )
