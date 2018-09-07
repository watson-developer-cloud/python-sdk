from unittest import TestCase
import os
from watson_developer_cloud.websocket import RecognizeCallback, AudioSource
import watson_developer_cloud
import pytest
import threading

@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestSpeechToTextV1(TestCase):
    text_to_speech = None
    custom_models = None
    create_custom_model = None
    customization_id = None

    @classmethod
    def setup_class(cls):
        cls.speech_to_text = watson_developer_cloud.SpeechToTextV1(
            username='YOUR SERVICE USERNAME',
            password='YOUR SERVICE PASSWORD')
        cls.speech_to_text.set_default_headers({
            'X-Watson-Learning-Opt-Out':
            '1',
            'X-Watson-Test':
            '1'
        })
        cls.custom_models = cls.speech_to_text.list_language_models().get_result()
        cls.create_custom_model = cls.speech_to_text.create_language_model(
            name="integration_test_model",
            base_model_name="en-US_BroadbandModel").get_result()
        cls.customization_id = cls.create_custom_model['customization_id']

    @classmethod
    def teardown_class(cls):
        cls.speech_to_text.delete_language_model(
            customization_id=cls.create_custom_model['customization_id'])

    def test_models(self):
        output = self.speech_to_text.list_models().get_result()
        assert output is not None
        model = self.speech_to_text.get_model('ko-KR_BroadbandModel').get_result()
        assert model is not None
        try:
            self.speech_to_text.get_model('bogus')
        except Exception as e:
            assert 'X-global-transaction-id:' in str(e)

    def test_create_custom_model(self):
        current_custom_models = self.speech_to_text.list_language_models().get_result()
        assert len(current_custom_models['customizations']) - len(
            self.custom_models['customizations']) >= 1

    def test_recognize(self):
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
            output = self.speech_to_text.recognize(
                audio=audio_file, content_type='audio/l16; rate=44100').get_result()
        assert output['results'][0]['alternatives'][0][
            'transcript'] == 'thunderstorms could produce large hail isolated tornadoes and heavy rain '

    def test_recognitions(self):
        output = self.speech_to_text.check_jobs().get_result()
        assert output is not None

    def test_custom_corpora(self):
        output = self.speech_to_text.list_corpora(self.customization_id).get_result()
        assert len(output['corpora']) == 0 # pylint: disable=len-as-condition

    def test_acoustic_model(self):
        list_models = self.speech_to_text.list_acoustic_models().get_result()
        assert list_models is not None

        create_acoustic_model = self.speech_to_text.create_acoustic_model(
            name="integration_test_model_python",
            base_model_name="en-US_BroadbandModel").get_result()
        assert create_acoustic_model is not None

        get_acoustic_model = self.speech_to_text.get_acoustic_model(
            create_acoustic_model['customization_id']).get_result()
        assert get_acoustic_model is not None

        self.speech_to_text.reset_acoustic_model(
            get_acoustic_model['customization_id']).get_result()

        self.speech_to_text.delete_acoustic_model(
            get_acoustic_model['customization_id']).get_result()

    def test_recognize_using_websocket(self):
        class MyRecognizeCallback(RecognizeCallback):
            def __init__(self):
                RecognizeCallback.__init__(self)
                self.error = None
                self.transcript = None

            def on_error(self, error):
                self.error = error

            def on_transcription(self, transcript):
                self.transcript = transcript

        testCallback = MyRecognizeCallback()
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
            audio_source = AudioSource(audio_file, False)
            t = threading.Thread(target=self.speech_to_text.recognize_using_websocket, args=(audio_source, "audio/l16; rate=44100", testCallback))
            t.start()
            t.join()
        assert testCallback.error is None
        assert testCallback.transcript is not None
        assert testCallback.transcript[0]['transcript'] == 'thunderstorms could produce large hail isolated tornadoes and heavy rain '
