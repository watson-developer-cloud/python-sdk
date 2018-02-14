from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

speech_to_text = SpeechToTextV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')
speech_to_text.set_default_headers({'X-Watson-Learning-Opt-Out': '1', 'X-Watson-Test': '1'})

print(json.dumps(speech_to_text.list_models(), indent=2))

print(json.dumps(speech_to_text.get_model('en-US_BroadbandModel'), indent=2))

with open(join(dirname(__file__), '../resources/speech.wav'),
          'rb') as audio_file:
    print(
        json.dumps(
            speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/wav',
                timestamps=True,
                word_confidence=True),
            indent=2))
