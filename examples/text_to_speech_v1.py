import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1 as TextToSpeech


text_to_speech = TextToSpeech(username='YOUR SERVICE USERNAME',
                              password='YOUR SERVICE PASSWORD')

print(json.dumps(text_to_speech.voices(), indent=2))

with open(join(dirname(__file__), '../resources/output.wav'), 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('Hello world!'))
