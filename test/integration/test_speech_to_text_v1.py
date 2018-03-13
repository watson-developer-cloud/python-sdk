# coding: utf-8
from unittest import TestCase
import os
import watson_developer_cloud
import pytest


@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestSpeechToTextV1(TestCase):
    def setUp(self):
        self.speech_to_text = watson_developer_cloud.SpeechToTextV1(
            username=os.getenv('YOUR SERVICE USERNAME'),
            password=os.getenv('YOUR SERVICE PASSWORD'))
        self.speech_to_text.set_default_headers({
            'X-Watson-Learning-Opt-Out':
            '1',
            'X-Watson-Test':
            '1'
        })
        self.custom_models = self.speech_to_text.list_language_models()
        self.create_custom_model = self.speech_to_text.create_language_model(
            name="integration_test_model",
            base_model_name="en-US_BroadbandModel")
        self.customization_id = self.create_custom_model['customization_id']

    def tearDown(self):
        self.speech_to_text.delete_language_model(
            customization_id=self.create_custom_model['customization_id'])

    def test_models(self):
        output = self.speech_to_text.list_models()
        assert output is not None
        model = self.speech_to_text.get_model('ko-KR_BroadbandModel')
        assert model is not None
        try:
            self.speech_to_text.get_model('bogus')
        except Exception as e:
            assert 'X-global-transaction-id:' in str(e)

    def test_create_custom_model(self):
        current_custom_models = self.speech_to_text.list_language_models()
        assert len(current_custom_models['customizations']) - len(
            self.custom_models['customizations']) >= 1

    def test_recognize(self):
        with open(os.path.join(os.path.dirname(__file__), '../../resources/speech.wav'), 'rb') as audio_file:
            output = self.speech_to_text.recognize(
                audio=audio_file, content_type='audio/l16; rate=44100')
        assert output['results'][0]['alternatives'][0][
            'transcript'] == 'thunderstorms could produce large hail isolated tornadoes and heavy rain '

    def test_recognitions(self):
        output = self.speech_to_text.check_jobs()
        assert output is not None

    def test_custom_corpora(self):
        output = self.speech_to_text.list_corpora(self.customization_id)
        assert len(output['corpora']) == 0 # pylint: disable=len-as-condition

    def test_acoustic_model(self):
        list_models = self.speech_to_text.list_acoustic_models()
        assert list_models is not None

        create_acoustic_model = self.speech_to_text.create_acoustic_model(
            name="integration_test_model_python",
            base_model_name="en-US_BroadbandModel")
        assert create_acoustic_model is not None

        get_acoustic_model = self.speech_to_text.get_acoustic_model(
            create_acoustic_model['customization_id'])
        assert get_acoustic_model is not None

        self.speech_to_text.reset_acoustic_model(
            get_acoustic_model['customization_id'])

        self.speech_to_text.delete_acoustic_model(
            get_acoustic_model['customization_id'])
