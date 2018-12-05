# You need to install pyaudio to run this example
# pip install pyaudio

# In this example, the websocket connection is opened with a text
# passed in the request. When the service responds with the synthesized
# audio, the pyaudio would play it in a blocking mode

from __future__ import print_function
from watson_developer_cloud import TextToSpeechV1
from watson_developer_cloud.websocket import SynthesizeCallback
import pyaudio

# If service instance provides API key authentication
service = TextToSpeechV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://stream.watsonplatform.net/text-to-speech/api',
    iam_apikey='your_apikey')

# service = TextToSpeechV1(
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://stream.watsonplatform.net/text-to-speech/api,
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD')

class Play(object):
    """
    Wrapper to play the audio in a blocking mode
    """
    def __init__(self):
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 22050
        self.chunk = 1024
        self.pyaudio = None
        self.stream = None

    def start_streaming(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self._open_stream()
        self._start_stream()

    def _open_stream(self):
        stream = self.pyaudio.open(
            format=self.format,
            channels=self.channels,
            rate=self.rate,
            output=True,
            frames_per_buffer=self.chunk,
            start=False
        )
        return stream

    def _start_stream(self):
        self.stream.start_stream()

    def write_stream(self, audio_stream):
        self.stream.write(audio_stream)

    def complete_playing(self):
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio.terminate()

class MySynthesizeCallback(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.play = Play()

    def on_connected(self):
        print('Opening stream to play')
        self.play.start_streaming()

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.play.write_stream(audio_stream)

    def on_close(self):
        print('Completed synthesizing')
        self.play.complete_playing()

test_callback = MySynthesizeCallback()

# An example SSML text
SSML_sorry_text = """<speak version=\"1.0\">
        <emphasis> I am sorry, I know how it feels.</emphasis>
        </speak>"""

# Another example of SSML text
SSML_text = """
   <speak>
        I have been assigned to handle your order status request.
       <express-as type=\"Apology\">
        I am sorry to inform you that the items you requested are backordered.
        We apologize for the inconvenience.
       </express-as>
      <express-as type=\"Uncertainty\">
        We don't know when the items will become available. Maybe next week,
        but we are not sure at this time.
      </express-as>
      <express-as type=\"GoodNews\">
        But because we want you to be a satisfied customer, we are giving you
        a 50% discount on your order!
      </express-as>
   </speak>"""

service.synthesize_using_websocket(SSML_text,
                                   test_callback,
                                   accept='audio/wav',
                                   voice="en-US_AllisonVoice"
                                  )
