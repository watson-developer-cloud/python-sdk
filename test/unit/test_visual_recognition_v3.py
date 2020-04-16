# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2016, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
import tempfile
import ibm_watson.visual_recognition_v3
from ibm_watson.visual_recognition_v3 import *

base_url = 'https://gateway.watsonplatform.net/visual-recognition/api'

##############################################################################
# Start of Service: General
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for classify
#-----------------------------------------------------------------------------
class TestClassify():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_response(self):
        body = self.construct_full_body()
        response = fake_response_ClassifiedImages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ClassifiedImages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classify'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.classify(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['images_file'] = tempfile.NamedTemporaryFile()
        body['images_filename'] = "string1"
        body['images_file_content_type'] = "string1"
        body['url'] = "string1"
        body['threshold'] = 12345.0
        body['owners'] = []
        body['classifier_ids'] = []
        body['accept_language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


# endregion
##############################################################################
# End of Service: General
##############################################################################

##############################################################################
# Start of Service: Custom
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_classifier
#-----------------------------------------------------------------------------
class TestCreateClassifier():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_classifier_response(self):
        body = self.construct_full_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_classifier_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_classifier_empty(self):
        check_empty_required_params(self, fake_response_Classifier_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.create_classifier(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['name'] = "string1"
        body['positive_examples'] = {"mock": "data"}
        body['negative_examples'] = tempfile.NamedTemporaryFile()
        body['negative_examples_filename'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['name'] = "string1"
        body['positive_examples'] = {"mock": "data"}
        return body


#-----------------------------------------------------------------------------
# Test Class for list_classifiers
#-----------------------------------------------------------------------------
class TestListClassifiers():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_classifiers_response(self):
        body = self.construct_full_body()
        response = fake_response_Classifiers_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_classifiers_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Classifiers_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_classifiers_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.list_classifiers(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['verbose'] = True
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_classifier
#-----------------------------------------------------------------------------
class TestGetClassifier():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_classifier_response(self):
        body = self.construct_full_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_classifier_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_classifier_empty(self):
        check_empty_required_params(self, fake_response_Classifier_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers/{0}'.format(body['classifier_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.get_classifier(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_classifier
#-----------------------------------------------------------------------------
class TestUpdateClassifier():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_classifier_response(self):
        body = self.construct_full_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_classifier_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Classifier_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_classifier_empty(self):
        check_empty_required_params(self, fake_response_Classifier_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers/{0}'.format(body['classifier_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.update_classifier(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        body['positive_examples'] = {"mock": "data"}
        body['negative_examples'] = tempfile.NamedTemporaryFile()
        body['negative_examples_filename'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_classifier
#-----------------------------------------------------------------------------
class TestDeleteClassifier():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_classifier_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_classifier_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_classifier_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers/{0}'.format(body['classifier_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.delete_classifier(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Custom
##############################################################################

##############################################################################
# Start of Service: CoreML
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_core_ml_model
#-----------------------------------------------------------------------------
class TestGetCoreMlModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_core_ml_model_response(self):
        body = self.construct_full_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_core_ml_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_core_ml_model_empty(self):
        check_empty_required_params(self, fake_response_BinaryIO_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/classifiers/{0}/core_ml_model'.format(body['classifier_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.get_core_ml_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['classifier_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CoreML
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for delete_user_data
#-----------------------------------------------------------------------------
class TestDeleteUserData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-03-19',
            )
        service.set_service_url(base_url)
        output = service.delete_user_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customer_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customer_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: UserData
##############################################################################


def check_empty_required_params(obj, response):
    """Test function to assert that the operation will throw an error when given empty required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    body = {k: None for k in body.keys()}
    error = False
    try:
        send_request(obj, body, response)
    except ValueError as e:
        error = True
    assert error

def check_missing_required_params(obj):
    """Test function to assert that the operation will throw an error when missing required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    error = False
    try:
        send_request(obj, {}, {}, url=url)
    except TypeError as e:
        error = True
    assert error

def check_empty_response(obj):
    """Test function to assert that the operation will return an empty response when given an empty request

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    send_request(obj, {}, {}, url=url)

def send_request(obj, body, response, url=None):
    """Test function to create a request, send it, and assert its accuracy to the mock response

    Args:
        obj: The generated test function
        body: Dict filled with fake data for calling the service
        response_str: Mock response string

    """
    if not url:
        url = obj.make_url(body)
    obj.add_mock_response(url, response)
    output = obj.call_service(body)
    assert responses.calls[0].request.url.startswith(url)
    assert output.get_result() == response

####################
## Mock Responses ##
####################

fake_response__json = None
fake_response_ClassifiedImages_json = """{"custom_classes": 14, "images_processed": 16, "images": [], "warnings": []}"""
fake_response_Classifier_json = """{"classifier_id": "fake_classifier_id", "name": "fake_name", "owner": "fake_owner", "status": "fake_status", "core_ml_enabled": false, "explanation": "fake_explanation", "created": "2017-05-16T13:56:54.957Z", "classes": [], "retrained": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Classifiers_json = """{"classifiers": []}"""
fake_response_Classifier_json = """{"classifier_id": "fake_classifier_id", "name": "fake_name", "owner": "fake_owner", "status": "fake_status", "core_ml_enabled": false, "explanation": "fake_explanation", "created": "2017-05-16T13:56:54.957Z", "classes": [], "retrained": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Classifier_json = """{"classifier_id": "fake_classifier_id", "name": "fake_name", "owner": "fake_owner", "status": "fake_status", "core_ml_enabled": false, "explanation": "fake_explanation", "created": "2017-05-16T13:56:54.957Z", "classes": [], "retrained": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_BinaryIO_json = """Contents of response byte-stream..."""
