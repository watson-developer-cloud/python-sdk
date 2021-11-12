from unittest import TestCase
import os
from ibm_watson.websocket import RecognizeCallback, AudioSource
import ibm_watson
import pytest
import threading


@pytest.mark.skipif(os.getenv('SPEECH_TO_TEXT_APIKEY') is None,
                    reason='requires SPEECH_TO_TEXT_APIKEY')
class TestSpeechToTextV1(TestCase):
    text_to_speech = None
    custom_models = None
    create_custom_model = None
    customization_id = None

    @classmethod
    def setup_class(cls):
        cls.speech_to_text = ibm_watson.SpeechToTextV1()
        cls.speech_to_text.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })
        cls.custom_models = cls.speech_to_text.list_language_models(
        ).get_result()
        cls.create_custom_model = cls.speech_to_text.create_language_model(
            name="integration_test_model",
            base_model_name="en-US_BroadbandModel").get_result()
        cls.customization_id = cls.create_custom_model.get('customization_id')

    @classmethod
    def teardown_class(cls):
        cls.speech_to_text.delete_language_model(
            customization_id=cls.create_custom_model.get('customization_id'))

    def test_models(self):
        output = self.speech_to_text.list_models().get_result()
        assert output is not None
        model = self.speech_to_text.get_model(
            'ko-KR_BroadbandModel').get_result()
        assert model is not None
        try:
            self.speech_to_text.get_model('bogus')
        except Exception as e:
            assert 'X-global-transaction-id:' in str(e)

    def test_create_custom_model(self):
        current_custom_models = self.speech_to_text.list_language_models(
        ).get_result()
        assert len(current_custom_models['customizations']) - len(
            self.custom_models.get('customizations')) >= 1

    def test_recognize(self):
        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/speech.wav'), 'rb') as audio_file:
            output = self.speech_to_text.recognize(
                audio=audio_file,
                content_type='audio/l16; rate=44100').get_result()
        assert output['results'][0]['alternatives'][0][
            'transcript'] == 'thunderstorms could produce large hail isolated tornadoes and heavy rain '

    def test_recognitions(self):
        output = self.speech_to_text.check_jobs().get_result()
        assert output is not None

    def test_custom_corpora(self):
        output = self.speech_to_text.list_corpora(
            self.customization_id).get_result()
        assert not output['corpora']

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

            def on_data(self, data):
                self.data = data

        test_callback = MyRecognizeCallback()
        with open(
                os.path.join(os.path.dirname(__file__),
                             '../../resources/speech.wav'), 'rb') as audio_file:
            audio_source = AudioSource(audio_file, False)
            t = threading.Thread(
                target=self.speech_to_text.recognize_using_websocket,
                args=(audio_source, "audio/l16; rate=44100", test_callback))
            t.start()
            t.join()
        assert test_callback.error is None
        assert test_callback.data is not None
        assert test_callback.data['results'][0]['alternatives'][0]
        ['transcript'] == 'thunderstorms could produce large hail isolated tornadoes and heavy rain '

    def test_on_transcription_interim_results_false(self):

        class MyRecognizeCallback(RecognizeCallback):

            def __init__(self):
                RecognizeCallback.__init__(self)
                self.error = None
                self.transcript = None

            def on_error(self, error):
                self.error = error

            def on_transcription(self, transcript):
                self.transcript = transcript

        test_callback = MyRecognizeCallback()
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech_with_pause.wav'), 'rb') as audio_file:
            audio_source = AudioSource(audio_file, False)
            self.speech_to_text.recognize_using_websocket(audio_source, "audio/wav", test_callback, model="en-US_Telephony",
             interim_results=False, low_latency=False)
            assert test_callback.error is None
            assert test_callback.transcript is not None
            assert test_callback.transcript[0][0]['transcript'] == 'isolated tornadoes '
            assert test_callback.transcript[1][0]['transcript'] == 'and heavy rain '

    def test_on_transcription_interim_results_true(self):

        class MyRecognizeCallback(RecognizeCallback):

            def __init__(self):
                RecognizeCallback.__init__(self)
                self.error = None
                self.transcript = None

            def on_error(self, error):
                self.error = error

            def on_transcription(self, transcript):
                self.transcript = transcript
                assert transcript[0]['confidence'] is not None
                assert transcript[0]['transcript'] is not None

        test_callback = MyRecognizeCallback()
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech_with_pause.wav'), 'rb') as audio_file:
            audio_source = AudioSource(audio_file, False)
            self.speech_to_text.recognize_using_websocket(audio_source, "audio/wav", test_callback, model="en-US_Telephony",
             interim_results=True, low_latency=True)
            assert test_callback.error is None
            assert test_callback.transcript is not None
            assert test_callback.transcript[0]['transcript'] == 'and heavy rain '

    def test_on_transcription_interim_results_true_low_latency_false(self):

        class MyRecognizeCallback(RecognizeCallback):

            def __init__(self):
                RecognizeCallback.__init__(self)
                self.error = None
                self.transcript = None

            def on_error(self, error):
                self.error = error

            def on_transcription(self, transcript):
                self.transcript = transcript
                assert transcript[0]['confidence'] is not None
                assert transcript[0]['transcript'] is not None

        test_callback = MyRecognizeCallback()
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech_with_pause.wav'), 'rb') as audio_file:
            audio_source = AudioSource(audio_file, False)
            self.speech_to_text.recognize_using_websocket(audio_source, "audio/wav", test_callback, model="en-US_Telephony",
             interim_results=True, low_latency=False)
            assert test_callback.error is None
            assert test_callback.transcript is not None
            assert test_callback.transcript[0]['transcript'] == 'and heavy rain '

    def test_custom_grammars(self):
        customization_id = None
        for custom_model in self.custom_models.get('customizations'):
            if custom_model['name'] == 'integration_test_model_for_grammar':
                customization_id = custom_model['customization_id']
                break

        if customization_id is None:
            print('Creating a new custom model')
            create_custom_model_for_grammar = self.speech_to_text.create_language_model(
                name="integration_test_model_for_grammar",
                base_model_name="en-US_BroadbandModel").get_result()
            customization_id = create_custom_model_for_grammar[
                'customization_id']

        grammars = self.speech_to_text.list_grammars(
            customization_id).get_result()['grammars']

        if not grammars:
            with open(
                    os.path.join(os.path.dirname(__file__),
                                 '../../resources/confirm-grammar.xml'),
                    'rb') as grammar_file:
                add_grammar_result = self.speech_to_text.add_grammar(
                    customization_id,
                    grammar_name='test-add-grammar-python',
                    grammar_file=grammar_file,
                    content_type='application/srgs+xml',
                    allow_overwrite=True).get_result()
                assert add_grammar_result is not None

            get_grammar_result = self.speech_to_text.get_grammar(
                customization_id,
                grammar_name='test-add-grammar-python').get_result()
            assert get_grammar_result is not None
        else:
            print('Deleting grammar')
            try:
                self.speech_to_text.delete_grammar(
                    customization_id, 'test-add-grammar-python').get_result()
            except ibm_watson.ApiException as ex:
                print('Could not delete grammar: {0}'.format(ex.message))

        try:
            self.speech_to_text.delete_language_model(customization_id)
        except ibm_watson.ApiException as ex:
            print('Could not delete model: {0}'.format(ex.message))
