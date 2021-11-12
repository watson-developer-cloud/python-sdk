# coding: utf-8
import pytest
import ibm_watson
import os
from os.path import abspath
from unittest import TestCase


@pytest.mark.skipif(os.getenv('VISUAL_RECOGNITION_APIKEY') is None,
                    reason='requires VISUAL_RECOGNITION_APIKEY')
class IntegrationTestVisualRecognitionV3(TestCase):
    visual_recognition = None
    classifier_id = None

    @classmethod
    def setup_class(cls):
        cls.visual_recognition = ibm_watson.VisualRecognitionV3('2018-03-19')
        cls.visual_recognition.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })
        cls.classifier_id = 'sdk-classifier-do-not-delete_1118105040'

    def test_classify(self):
        dog_path = abspath('resources/dog.jpg')
        with open(dog_path, 'rb') as image_file:
            dog_results = self.visual_recognition.classify(
                images_file=image_file,
                threshold='0.1',
                classifier_ids=['default']).get_result()
        assert dog_results is not None

    @pytest.mark.skip(reason="Time consuming")
    def test_custom_classifier(self):
        with open(abspath('resources/cars.zip'), 'rb') as cars, \
            open(abspath('resources/trucks.zip'), 'rb') as trucks:
            classifier = self.visual_recognition.create_classifier(
                'CarsVsTrucks',
                positive_examples={
                    'cars': cars
                },
                negative_examples=trucks,
            ).get_result()

        assert classifier is not None

        classifier_id = classifier['classifier_id']
        output = self.visual_recognition.get_classifier(
            classifier_id).get_result()
        assert output is not None

        output = self.visual_recognition.delete_classifier(
            classifier_id).get_result()

    @pytest.mark.skip(reason="temporay disable")
    def test_core_ml_model(self):
        core_ml_model = self.visual_recognition.get_core_ml_model(
            self.classifier_id).get_result()
        assert core_ml_model.ok
