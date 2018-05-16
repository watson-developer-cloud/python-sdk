# coding: utf-8
import pytest
import watson_developer_cloud
import os
from os.path import join, dirname
from unittest import TestCase
import json

@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class IntegrationTestVisualRecognitionV3(TestCase):
    visual_recognition = None
    classifier_id = None

    @classmethod
    def setup_class(cls):
        cls.visual_recognition = watson_developer_cloud.VisualRecognitionV3(
            '2016-05-20', api_key='YOUR API KEY')
        cls.visual_recognition.set_default_headers({
            'X-Watson-Learning-Opt-Out':
            '1',
            'X-Watson-Test':
            '1'
        })
        cls.classifier_id = 'doxnotxdeletexintegrationxtest_397877192'

    def test_classify(self):
        dog_path = join(dirname(__file__), '../../resources/dog.jpg')
        with open(dog_path, 'rb') as image_file:
            dog_results = self.visual_recognition.classify(
                images_file=image_file,
                threshold='0.1',
                classifier_ids=['default'])
        assert dog_results is not None

    def test_detect_faces(self):
        output = self.visual_recognition.detect_faces(
            parameters=json.dumps({
                'url':
                'https://www.ibm.com/ibm/ginni/images/ginni_bio_780x981_v4_03162016.jpg'
            }))
        assert output is not None

    @pytest.mark.skip(reason="Time consuming")
    def test_custom_classifier(self):
        with open(os.path.join(os.path.dirname(__file__), '../../resources/cars.zip'), 'rb') as cars, \
            open(os.path.join(os.path.dirname(__file__), '../../resources/trucks.zip'), 'rb') as trucks:
            classifier = self.visual_recognition.create_classifier(
                'CarsVsTrucks',
                cars_positive_examples=cars,
                negative_examples=trucks,
                )

        assert classifier is not None

        classifier_id = classifier['classifier_id']
        output = self.visual_recognition.get_classifier(classifier_id)
        assert output is not None

        output = self.visual_recognition.delete_classifier(classifier_id)

    def test_core_ml_model(self):
        core_ml_model = self.visual_recognition.get_core_ml_model(self.classifier_id)
        assert core_ml_model.ok
