import json
import watson_developer_cloud


speech_to_text = watson_developer_cloud.SpeechToTextV1()

print(json.dumps(speech_to_text.models(), indent=2))

with open('../resources/speech.wav', 'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(audio_file, content_type='audio/l16; rate=44100'), indent=2))
