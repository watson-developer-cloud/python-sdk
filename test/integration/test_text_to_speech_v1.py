# coding: utf-8
import unittest
import watson_developer_cloud
import pytest
import os

@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestIntegrationTextToSpeechV1(unittest.TestCase):
    def setUp(self):
        self.text_to_speech = watson_developer_cloud.TextToSpeechV1(
            username="YOUR SERVICE USERNAME", password="YOUR SERVICE PASSWORD")
        self.text_to_speech.set_default_headers({
            'X-Watson-Learning-Opt-Out':
            '1',
            'X-Watson-Test':
            '1'
        })
        self.original_customizations = self.text_to_speech.list_voice_models()
        self.created_customization = self.text_to_speech.create_voice_model(
            name="test_integration_customization",
            description="customization for tests")

    def tearDown(self):
        custid = self.created_customization['customization_id']
        self.text_to_speech.delete_voice_model(customization_id=custid)

    def test_voices(self):
        output = self.text_to_speech.list_voices()
        assert output['voices'] is not None
        voice = self.text_to_speech.get_voice(output['voices'][0]['name'])
        assert voice is not None

    def test_speak(self):
        output = self.text_to_speech.synthesize(
            text="my voice is my passport",
            accept='audio/wav',
            voice='en-US_AllisonVoice')
        assert output.content is not None

    def test_pronunciation(self):
        output = self.text_to_speech.get_pronunciation('hello')
        assert output['pronunciation'] is not None

    def test_customizations(self):
        old_length = len(self.original_customizations['customizations'])
        new_length = len(
            self.text_to_speech.list_voice_models()['customizations'])
        assert new_length - old_length >= 1

    def test_custom_words(self):
        customization_id = self.created_customization['customization_id']
        words = self.text_to_speech.list_words(customization_id)['words']
        assert len(words) == 0 # pylint: disable=len-as-condition
        self.text_to_speech.add_word(
            customization_id, word="ACLs", translation="ackles")

        words = [{"word": "MACLs", "translation": "mackles"}]

        self.text_to_speech.add_words(customization_id, words)
        self.text_to_speech.delete_word(customization_id, 'ACLs')
        word = self.text_to_speech.get_word(customization_id, 'MACLs')
        assert word['translation'] == 'mackles'
