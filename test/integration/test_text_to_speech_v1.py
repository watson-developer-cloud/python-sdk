# coding: utf-8
import unittest
import ibm_watson
from ibm_watson.websocket import SynthesizeCallback
import pytest
import os


@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None,
                    reason='requires VCAP_SERVICES')
class TestIntegrationTextToSpeechV1(unittest.TestCase):
    text_to_speech = None
    original_customizations = None
    created_customization = None

    @classmethod
    def setup_class(cls):
        cls.text_to_speech = ibm_watson.TextToSpeechV1()
        cls.text_to_speech.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })
        cls.original_customizations = cls.text_to_speech.list_voice_models(
        ).get_result()
        cls.created_customization = cls.text_to_speech.create_voice_model(
            name="test_integration_customization",
            description="customization for tests").get_result()

    @classmethod
    def teardown_class(cls):
        custid = cls.created_customization.get('customization_id')
        cls.text_to_speech.delete_voice_model(customization_id=custid)

    def test_voices(self):
        output = self.text_to_speech.list_voices().get_result()
        assert output['voices'] is not None
        voice = self.text_to_speech.get_voice(
            output['voices'][0]['name']).get_result()
        assert voice is not None

    def test_speak(self):
        output = self.text_to_speech.synthesize(
            text="my voice is my passport",
            accept='audio/wav',
            voice='en-US_AllisonVoice').get_result()
        assert output.content is not None

    def test_pronunciation(self):
        output = self.text_to_speech.get_pronunciation('hello').get_result()
        assert output['pronunciation'] is not None

    def test_customizations(self):
        old_length = len(self.original_customizations.get('customizations'))
        new_length = len(self.text_to_speech.list_voice_models().get_result()
                         ['customizations'])
        assert new_length - old_length >= 1

    def test_custom_words(self):
        customization_id = self.created_customization.get('customization_id')
        words = self.text_to_speech.list_words(
            customization_id).get_result()['words']
        assert not words
        self.text_to_speech.add_word(customization_id,
                                     word="ACLs",
                                     translation="ackles")

        words = [{"word": "MACLs", "translation": "mackles"}]

        self.text_to_speech.add_words(customization_id, words)
        self.text_to_speech.delete_word(customization_id, 'ACLs')
        word = self.text_to_speech.get_word(customization_id,
                                            'MACLs').get_result()
        assert word['translation'] == 'mackles'

    def test_synthesize_using_websocket(self):
        file = 'tongue_twister.wav'

        class MySynthesizeCallback(SynthesizeCallback):

            def __init__(self):
                SynthesizeCallback.__init__(self)
                self.fd = None
                self.error = None

            def on_connected(self):
                self.fd = open(file, 'ab')

            def on_error(self, error):
                self.error = error

            def on_audio_stream(self, audio_stream):
                self.fd.write(audio_stream)

            def on_close(self):
                self.fd.close()

        test_callback = MySynthesizeCallback()
        self.text_to_speech.synthesize_using_websocket(
            'She sells seashells by the seashore',
            test_callback,
            accept='audio/wav',
            voice='en-GB_KateVoice')
        assert test_callback.error is None
        assert test_callback.fd is not None
        assert os.stat(file).st_size > 0
        os.remove(file)
