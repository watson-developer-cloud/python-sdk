# coding: utf-8
from unittest import TestCase
import os
import watson_developer_cloud
import pytest
import json
import time

FIVE_SECONDS = 5

@pytest.mark.skipif(os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestNaturalLanguageClassifierV1(TestCase):
    def setUp(self):
        self.natural_language_classifier = watson_developer_cloud.NaturalLanguageClassifierV1(
            username='YOUR SERVICE USERNAME',
            password='YOUR SERVICE PASSWORD')
        self.natural_language_classifier.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

        # Create a classifier
        with open(os.path.join(os.path.dirname(__file__), '../../resources/weather_data_train.csv'), 'rb') as training_data:
            metadata = json.dumps({'name': 'my-classifier', 'language': 'en'})
            classifier = self.natural_language_classifier.create_classifier(
                metadata=metadata,
                training_data=training_data
            )
            self.classifier_id = classifier['classifier_id']

    def tearDown(self):
        self.natural_language_classifier.delete_classifier(self.classifier_id)

    def test_list_classifier(self):
        list_classifiers = self.natural_language_classifier.list_classifiers()
        assert list_classifiers is not None

    @pytest.mark.skip(reason="The classifier takes more than a minute")
    def test_classify_text(self):
        iterations = 0
        while iterations < 15:
            status = self.natural_language_classifier.get_classifier(self.classifier_id)
            iterations += 1
            if status['status'] != 'Available':
                time.sleep(FIVE_SECONDS)

        if status['status'] != 'Available':
            assert False, 'Classifier is not available'

        classes = self.natural_language_classifier.classify(self.classifier_id, 'How hot will it be tomorrow?')
        assert classes is not None

        collection = ['{"text":"How hot will it be today?"}', '{"text":"Is it hot outside?"}']
        classes = self.natural_language_classifier.classify_collection(
            self.classifier_id, collection)
        assert classes is not None
