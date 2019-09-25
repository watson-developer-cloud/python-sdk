# coding: utf-8
import responses
import ibm_watson
import json
import os
import jwt
import time

from unittest import TestCase
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

base_url = "https://gateway.watsonplatform.net/visual-recognition/api/"

def get_access_token():
    access_token_layout = {
        "username": "dummy",
        "role": "Admin",
        "permissions": [
            "administrator",
            "manage_catalog"
        ],
        "sub": "admin",
        "iss": "sss",
        "aud": "sss",
        "uid": "sss",
        "iat": 3600,
        "exp": int(time.time())
    }

    access_token = jwt.encode(access_token_layout, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
    return access_token.decode('utf-8')

class TestVisualRecognitionV3(TestCase):
    @classmethod
    def setUp(cls):
        iam_url = "https://iam.cloud.ibm.com/identity/token"
        iam_token_response = {
            "access_token": get_access_token(),
            "token_type": "Bearer",
            "expires_in": 3600,
            "expiration": 1524167011,
            "refresh_token": "jy4gl91BQ"
        }
        responses.add(responses.POST, url=iam_url, body=json.dumps(iam_token_response), status=200)

    @responses.activate
    def test_get_classifier(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)
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

        assert len(responses.calls) == 2

    @responses.activate
    def test_delete_classifier(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)

        gc_url = "{0}{1}".format(base_url, 'v3/classifiers/bogusnumber')

        responses.add(responses.DELETE,
                      gc_url,
                      body=json.dumps({'response': 200}),
                      status=200,
                      content_type='application/json')
        vr_service.delete_classifier(classifier_id='bogusnumber')

        assert len(responses.calls) == 2

    @responses.activate
    def test_list_classifiers(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)

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

        assert len(responses.calls) == 2

    @responses.activate
    def test_create_classifier(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)

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
            vr_service.create_classifier('Cars vs Trucks', positive_examples={'cars': cars}, negative_examples=trucks)

        assert len(responses.calls) == 2

    @responses.activate
    def test_update_classifier(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)

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
        assert len(responses.calls) == 2

    @responses.activate
    def test_classify(self):
        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)

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
        assert len(responses.calls) == 8

    @responses.activate
    def test_delete_user_data(self):
        url = "{0}{1}".format(base_url, 'v3/user_data')
        responses.add(
            responses.DELETE,
            url,
            body='{"description": "success" }',
            status=204,
            content_type='application_json')

        authenticator = IAMAuthenticator('bogusapikey')
        vr_service = ibm_watson.VisualRecognitionV3('2016-10-20', authenticator=authenticator)
        response = vr_service.delete_user_data('id').get_result()
        assert response is None
        assert len(responses.calls) == 2
