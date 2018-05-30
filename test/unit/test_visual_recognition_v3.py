# coding: utf-8
import responses
import watson_developer_cloud
import json
import os

from unittest import TestCase

base_url = "https://gateway-a.watsonplatform.net/visual-recognition/api/"

class TestVisualRecognitionV3(TestCase):
    @responses.activate
    def test_get_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusnumber')

        response = {
            "classifier_id": "bogusnumber",
            "name": "Dog Breeds",
            "owner": "58b61352-678c-44d1-9f40-40edf4ea8d19",
            "status": "failed",
            "created": "2017-08-25T06:39:01.968Z",
            "classes": [{"class": "goldenretriever"}]
            }

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')
        vr_service.get_classifier(classifier_id='bogusnumber')

        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusnumber')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        vr_service.delete_classifier(classifier_id='bogusnumber')

        assert len(responses.calls) == 1

    @responses.activate
    def test_list_classifiers(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers')

        response = {"classifiers": [
            {
                "classifier_id": "InsuranceClaims_1362331461",
                "name": "Insurance Claims",
                "status": "ready"
            },
            {
                "classifier_id": "DogBreeds_1539707331",
                "name": "Dog Breeds",
                "status": "ready"
            }
        ]}

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')
        vr_service.list_classifiers()

        assert len(responses.calls) == 1

    @responses.activate
    def test_create_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers')

        response = {
            "classifier_id": "DogBreeds_2014254824",
            "name": "Dog Breeds",
            "owner": "58b61352-678c-44d1-9f40-40edf4ea8d19",
            "status": "failed",
            "created": "2017-08-25T06:39:01.968Z",
            "classes": [{"class": "goldenretriever"}]
            }

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        with open(os.path.join(os.path.dirname(__file__), '../../resources/cars.zip'), 'rb') as cars, \
            open(os.path.join(os.path.dirname(__file__), '../../resources/trucks.zip'), 'rb') as trucks:
            vr_service.create_classifier('Cars vs Trucks', cars_positive_examples=cars, negative_examples=trucks)

        assert len(responses.calls) == 1

    @responses.activate
    def test_update_classifier(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusid')

        response = {
            "classifier_id": "bogusid",
            "name": "Insurance Claims",
            "owner": "58b61352-678c-44d1-9f40-40edf4ea8d19",
            "status": "ready",
            "created": "2017-07-17T22:17:14.860Z",
            "classes": [
                {"class": "motorcycleaccident"},
                {"class": "flattire"},
                {"class": "brokenwinshield"}
                ]
            }

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        vr_service.update_classifier(classifier_id="bogusid")
        assert len(responses.calls) == 1

    @responses.activate
    def test_classify(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/classify')

        response = {"images": [
            {"image": "test.jpg",
             "classifiers": [
                 {"classes": [
                     {"score": 0.95, "class": "tiger", "type_hierarchy": "/animal/mammal/carnivore/feline/big cat/tiger"},
                     {"score": 0.997, "class": "big cat"},
                     {"score": 0.998, "class": "feline"},
                     {"score": 0.998, "class": "carnivore"},
                     {"score": 0.998, "class": "mammal"},
                     {"score": 0.999, "class": "animal"}
                     ],
                  "classifier_id": "default",
                  "name": "default"}
                 ]
            }
            ],
                    "custom_classes": 0,
                    "images_processed": 1
                   }

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')
        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        vr_service.classify(parameters='{"url": "http://google.com"}')

        vr_service.classify(parameters=json.dumps({'url': 'http://google.com', 'classifier_ids': ['one', 'two', 'three']}))
        vr_service.classify(parameters=json.dumps({'url': 'http://google.com', 'owners': ['me', 'IBM']}))

        with open(os.path.join(os.path.dirname(__file__), '../../resources/test.jpg'), 'rb') as image_file:
            vr_service.classify(images_file=image_file)
        assert len(responses.calls) == 4

    @responses.activate
    def test_detect_faces(self):
        vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')

        gc_url = "{0}{1}".format(base_url, 'v3/detect_faces')

        response = {
            "images": [
                {
                    "faces": [
                        {
                            "age": {
                                "max": 44,
                                "min": 35,
                                "score": 0.446989
                            },
                            "face_location": {
                                "height": 159,
                                "left": 256,
                                "top": 64,
                                "width": 92
                            },
                            "gender": {
                                "gender": "MALE",
                                "score": 0.99593
                            },
                            "identity": {
                                "name": "Barack Obama",
                                "score": 0.970688,
                                "type_hierarchy": "/people/politicians/democrats/barack obama"
                            }
                        }
                    ],
                    "resolved_url": "https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/prez.jpg",
                    "source_url": "https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/prez.jpg"
                }
            ],
            "images_processed": 1
        }

        responses.add(responses.GET,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        responses.add(responses.POST,
                      gc_url,
                      body=json.dumps(response),
                      status=200,
                      content_type='application/json')

        vr_service.detect_faces(parameters='{"url": "http://google.com"}')
        with open(os.path.join(os.path.dirname(__file__), '../../resources/test.jpg'), 'rb') as image_file:
            vr_service.detect_faces(images_file=image_file)
        assert len(responses.calls) == 2

@responses.activate
def test_delete_user_data():
    url = "{0}{1}".format(base_url, 'v3/user_data')
    responses.add(
        responses.DELETE,
        url,
        body='{"description": "success" }',
        status=200,
        content_type='application_json')

    vr_service = watson_developer_cloud.VisualRecognitionV3('2016-10-20', api_key='bogusapikey')
    response = vr_service.delete_user_data('id')
    assert response is None
    assert len(responses.calls) == 1
