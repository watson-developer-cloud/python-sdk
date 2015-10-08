import json
import watson_developer_cloud


text_to_speech = watson_developer_cloud.TextToSpeechV1()

print(json.dumps(text_to_speech.voices(), indent=2))

with open('../resources/output.wav', 'wb') as audio_file:
    audio_file.write(text_to_speech.synthesize('Hello world!'))
