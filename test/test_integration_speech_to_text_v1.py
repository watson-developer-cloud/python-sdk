from unittest import TestCase
import pytest
import os
import watson_developer_cloud

@pytest.mark.skip("These are destructive, so run them manually")
class TestSpeechToTextV1(TestCase):
    def setUp(self):
        self.speech_to_text = watson_developer_cloud.SpeechToTextV1(username=os.getenv('SPEECH_TO_TEXT_USERNAME'),
                                                                    password=os.getenv('SPEECH_TO_TEXT_PASSWORD'))
        self.custom_models = self.speech_to_text.list_custom_models()
        self.create_custom_model = self.speech_to_text.create_custom_model(name="integration_test_model")

    def tearDown(self):
        self.speech_to_text.delete_custom_model(modelid=self.create_custom_model['customization_id'])

    def test_create_custom_model(self):
        current_custom_models = self.speech_to_text.list_custom_models()
        assert len(current_custom_models['customizations']) - len(self.custom_models['customizations']) == 1
