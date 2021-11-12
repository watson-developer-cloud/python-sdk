# coding: utf-8
import unittest
import ibm_watson
from ibm_watson.websocket import SynthesizeCallback
import pytest
import os


@pytest.mark.skipif(os.getenv('TEXT_TO_SPEECH_APIKEY') is None,
                    reason='requires TEXT_TO_SPEECH_APIKEY')
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
        cls.original_customizations = cls.text_to_speech.list_custom_models(
        ).get_result()
        cls.created_customization = cls.text_to_speech.create_custom_model(
            name="test_integration_customization",
            description="customization for tests").get_result()

    @classmethod
    def teardown_class(cls):
        custid = cls.created_customization.get('customization_id')
        cls.text_to_speech.delete_custom_model(customization_id=custid)

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
        new_length = len(self.text_to_speech.list_custom_models().get_result()
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

    def test_custom_prompts(self):
        customization_id = self.created_customization.get('customization_id')
        prompt_id = "Hello"
        metadata = {
            "prompt_text": "Hello how are you today?" 
        }
        
        with open("resources/tts_audio.wav", "rb") as audio_file:
            self.text_to_speech.add_custom_prompt(
                customization_id, prompt_id, metadata, audio_file
                ).get_result()
            prompts = self.text_to_speech.list_custom_prompts(customization_id).get_result()
            assert len(prompts) > 0
            prompt = self.text_to_speech.get_custom_prompt(customization_id, prompt_id).get_result()
            assert prompt["prompt_id"] == prompt_id
            self.text_to_speech.delete_custom_prompt(customization_id, prompt_id)

    def test_speaker_models(self):
        speaker_name = "Angelo"

        with open("resources/tts_audio.wav", "rb") as audio_file:
            speaker_id = self.text_to_speech.create_speaker_model(
                speaker_name, audio_file
            ).get_result()["speaker_id"]
            speaker_models = self.text_to_speech.list_speaker_models().get_result()
            assert len(speaker_models) > 0
            speaker_model = self.text_to_speech.get_speaker_model(speaker_id).get_result()
            self.text_to_speech.delete_speaker_model(speaker_id)

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

    # This is test will only be meaningful so long as en-AU_CraigVoice is a Neural type voice model
    # Check this url for all Neutral type voice models: https://cloud.ibm.com/docs/text-to-speech?topic=text-to-speech-voices#languageVoices
    def test_synthesize_using_websocket_neural(self):
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
            voice='en-AU_CraigVoice')
        assert test_callback.error is None
        assert test_callback.fd is not None
        assert os.stat(file).st_size > 0
        os.remove(file)
