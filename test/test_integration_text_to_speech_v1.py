import pytest
import unittest
import watson_developer_cloud
import os

@pytest.mark.skip("These are destructive, so run them manually")
class TestIntegrationTextToSpeechV1(unittest.TestCase):

    def setUp(self):
        self.text_to_speech = watson_developer_cloud.TextToSpeechV1(username=os.getenv('TEXT_TO_SPEECH_USERNAME'),
                                                                    password=os.getenv('TEXT_TO_SPEECH_PASSWORD'))
        self.original_customizations = self.text_to_speech.customizations()
        self.created_customization = self.text_to_speech.create_customization(name="test_integration_customization",
                                                                              description="customization for tests")

    def tearDown(self):
        custid = self.created_customization['customization_id']
        self.text_to_speech.delete_customization(customization_id=custid)

    def test_customizations(self):
        old_length = len(self.original_customizations['customizations'])
        new_length = len(self.text_to_speech.customizations()['customizations'])
        assert  new_length - old_length == 1

    def test_speak(self):
        output = self.text_to_speech.synthesize(text="my voice is my passport")
        assert not output
