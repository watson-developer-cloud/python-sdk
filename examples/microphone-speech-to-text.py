# You need to install pyaudio to run this example
# pip install pyaudio

from __future__ import print_function
import pyaudio
import tempfile
from watson_developer_cloud import SpeechToTextV1
from watson_developer_cloud.websocket import RecognizeCallback

speech_to_text = SpeechToTextV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD',
    url='https://stream.watsonplatform.net/speech-to-text/api')


# Example using websockets
class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_transcription(self, transcript):
        print(transcript)

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_listening(self):
        print('Service is listening')

    def on_transcription_complete(self):
        print('Transcription completed')

    def on_hypothesis(self, hypothesis):
        print(hypothesis)


mycallback = MyRecognizeCallback()
tmp = tempfile.NamedTemporaryFile()

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5

audio = pyaudio.PyAudio()
stream = audio.open(
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK)

print('recording....')
with open(tmp.name, 'w') as f:
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        f.write(data)

stream.stop_stream()
stream.close()
audio.terminate()
print('Done recording...')

with open(tmp.name) as f:
    speech_to_text.recognize_with_websocket(
        audio=f, recognize_callback=mycallback)
