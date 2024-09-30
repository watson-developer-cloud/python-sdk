import pyaudio, os, json
from ibm_watson import NaturalLanguageUnderstandingV1, TextToSpeechV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import SynthesizeCallback
from dotenv import load_dotenv
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load authentication credentials
load_dotenv("../ibm-credentials.env")
NLU_API_KEY = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_APIKEY")
NLU_URL = os.getenv("NATURAL_LANGUAGE_UNDERSTANDING_URL")
T2S_API_KEY = os.getenv("TEXT_TO_SPEECH_APIKEY")
T2S_URL = os.getenv("TEXT_TO_SPEECH_URL")

# Authentication NLU
authenticator = IAMAuthenticator(NLU_API_KEY)
natural_language_understanding = NaturalLanguageUnderstandingV1(version='2022-04-07', authenticator=authenticator)
natural_language_understanding.set_service_url(NLU_URL)

# Authentication T2S
authenticator = IAMAuthenticator(T2S_API_KEY)
text_to_speech = TextToSpeechV1(authenticator=authenticator)
text_to_speech.set_service_url(T2S_URL)


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


@app.route("/", methods=["POST"])
def analyze_url_to_speech():
    """
    Analyse URL and return keywords
    """
    # set URL to be analysed and number of output keywords
    data = request.json
    analyse_url = data.get("url")
    keywords_num = data.get("keywords_num")

    # get NLU result
    response = natural_language_understanding.analyze(
        url=analyse_url,
        features=Features(keywords=KeywordsOptions(sentiment=True, emotion=True, limit=keywords_num))).get_result()
    print("NLU result: {}".format(json.dumps(response, indent=2)))

    # generate keywords and convert to SSML
    response_txt_list = [response['keywords'][i]['text'] for i in range(len(response['keywords']))]
    response_txt = ', '.join(response_txt_list)
    SSML_text = """
       <speak>
            I have been assigned to analyse the URL you gave me and return keywords of it.
          <express-as type=\"GoodNews\">
            {} keywords in the given URL are {}
          </express-as>
       </speak>""".format(keywords_num, response_txt)

    # run text-to-speech
    test_callback = MySynthesizeCallback()
    text_to_speech.synthesize_using_websocket(SSML_text,
                                              test_callback,
                                              accept='audio/wav',
                                              voice="en-US_AllisonVoice")

    return jsonify({"keywords": response_txt_list})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)