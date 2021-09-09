# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2016, 2021.
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

"""
Unit Tests for VisualRecognitionV3
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watson.visual_recognition_v3 import *

version = 'testString'

_service = VisualRecognitionV3(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: General
##############################################################################
# region

class TestClassify():
    """
    Test Class for classify
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_classify_all_params(self):
        """
        classify()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classify')
        mock_response = '{"custom_classes": 14, "images_processed": 16, "images": [{"source_url": "source_url", "resolved_url": "resolved_url", "image": "image", "error": {"code": 4, "description": "description", "error_id": "error_id"}, "classifiers": [{"name": "name", "classifier_id": "classifier_id", "classes": [{"class": "class_", "score": 0, "type_hierarchy": "type_hierarchy"}]}]}], "warnings": [{"warning_id": "warning_id", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        images_file = io.BytesIO(b'This is a mock file.').getvalue()
        images_filename = 'testString'
        images_file_content_type = 'testString'
        url = 'testString'
        threshold = 72.5
        owners = ['testString']
        classifier_ids = ['testString']
        accept_language = 'en'

        # Invoke method
        response = _service.classify(
            images_file=images_file,
            images_filename=images_filename,
            images_file_content_type=images_file_content_type,
            url=url,
            threshold=threshold,
            owners=owners,
            classifier_ids=classifier_ids,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_classify_required_params(self):
        """
        test_classify_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classify')
        mock_response = '{"custom_classes": 14, "images_processed": 16, "images": [{"source_url": "source_url", "resolved_url": "resolved_url", "image": "image", "error": {"code": 4, "description": "description", "error_id": "error_id"}, "classifiers": [{"name": "name", "classifier_id": "classifier_id", "classes": [{"class": "class_", "score": 0, "type_hierarchy": "type_hierarchy"}]}]}], "warnings": [{"warning_id": "warning_id", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.classify()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_classify_value_error(self):
        """
        test_classify_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classify')
        mock_response = '{"custom_classes": 14, "images_processed": 16, "images": [{"source_url": "source_url", "resolved_url": "resolved_url", "image": "image", "error": {"code": 4, "description": "description", "error_id": "error_id"}, "classifiers": [{"name": "name", "classifier_id": "classifier_id", "classes": [{"class": "class_", "score": 0, "type_hierarchy": "type_hierarchy"}]}]}], "warnings": [{"warning_id": "warning_id", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.classify(**req_copy)



# endregion
##############################################################################
# End of Service: General
##############################################################################

##############################################################################
# Start of Service: Custom
##############################################################################
# region

class TestCreateClassifier():
    """
    Test Class for create_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_classifier_all_params(self):
        """
        create_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'
        positive_examples = { 'key': io.BytesIO(b'This is a mock file.').getvalue() }
        negative_examples = io.BytesIO(b'This is a mock file.').getvalue()
        negative_examples_filename = 'testString'

        # Invoke method
        response = _service.create_classifier(
            name,
            positive_examples,
            negative_examples=negative_examples,
            negative_examples_filename=negative_examples_filename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_classifier_required_params(self):
        """
        test_create_classifier_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'
        positive_examples = { 'key': io.BytesIO(b'This is a mock file.').getvalue() }

        # Invoke method
        response = _service.create_classifier(
            name,
            positive_examples,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_classifier_value_error(self):
        """
        test_create_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'
        positive_examples = { 'key': io.BytesIO(b'This is a mock file.').getvalue() }

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "positive_examples": positive_examples,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_classifier(**req_copy)



class TestListClassifiers():
    """
    Test Class for list_classifiers
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_classifiers_all_params(self):
        """
        list_classifiers()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifiers": [{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        verbose = True

        # Invoke method
        response = _service.list_classifiers(
            verbose=verbose,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'verbose={}'.format('true' if verbose else 'false') in query_string


    @responses.activate
    def test_list_classifiers_required_params(self):
        """
        test_list_classifiers_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifiers": [{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_classifiers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_classifiers_value_error(self):
        """
        test_list_classifiers_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers')
        mock_response = '{"classifiers": [{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_classifiers(**req_copy)



class TestGetClassifier():
    """
    Test Class for get_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_classifier_all_params(self):
        """
        get_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.get_classifier(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_classifier_value_error(self):
        """
        test_get_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_classifier(**req_copy)



class TestUpdateClassifier():
    """
    Test Class for update_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_classifier_all_params(self):
        """
        update_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'
        positive_examples = { 'key': io.BytesIO(b'This is a mock file.').getvalue() }
        negative_examples = io.BytesIO(b'This is a mock file.').getvalue()
        negative_examples_filename = 'testString'

        # Invoke method
        response = _service.update_classifier(
            classifier_id,
            positive_examples=positive_examples,
            negative_examples=negative_examples,
            negative_examples_filename=negative_examples_filename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_classifier_required_params(self):
        """
        test_update_classifier_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.update_classifier(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_classifier_value_error(self):
        """
        test_update_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        mock_response = '{"classifier_id": "classifier_id", "name": "name", "owner": "owner", "status": "ready", "core_ml_enabled": false, "explanation": "explanation", "created": "2019-01-01T12:00:00.000Z", "classes": [{"class": "class_"}], "retrained": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_classifier(**req_copy)



class TestDeleteClassifier():
    """
    Test Class for delete_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_classifier_all_params(self):
        """
        delete_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.delete_classifier(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_classifier_value_error(self):
        """
        test_delete_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_classifier(**req_copy)



# endregion
##############################################################################
# End of Service: Custom
##############################################################################

##############################################################################
# Start of Service: CoreML
##############################################################################
# region

class TestGetCoreMlModel():
    """
    Test Class for get_core_ml_model
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_core_ml_model_all_params(self):
        """
        get_core_ml_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString/core_ml_model')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.get_core_ml_model(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_core_ml_model_value_error(self):
        """
        test_get_core_ml_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/classifiers/testString/core_ml_model')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_core_ml_model(**req_copy)



# endregion
##############################################################################
# End of Service: CoreML
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

class TestDeleteUserData():
    """
    Test Class for delete_user_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_user_data_all_params(self):
        """
        delete_user_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'customer_id={}'.format(customer_id) in query_string


    @responses.activate
    def test_delete_user_data_value_error(self):
        """
        test_delete_user_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        customer_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customer_id": customer_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_user_data(**req_copy)



# endregion
##############################################################################
# End of Service: UserData
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Class():
    """
    Test Class for Class
    """

    def test_class_serialization(self):
        """
        Test serialization/deserialization for Class
        """

        # Construct a json representation of a Class model
        class_model_json = {}
        class_model_json['class'] = 'testString'

        # Construct a model instance of Class by calling from_dict on the json representation
        class_model = Class.from_dict(class_model_json)
        assert class_model != False

        # Construct a model instance of Class by calling from_dict on the json representation
        class_model_dict = Class.from_dict(class_model_json).__dict__
        class_model2 = Class(**class_model_dict)

        # Verify the model instances are equivalent
        assert class_model == class_model2

        # Convert model instance back to dict and verify no loss of data
        class_model_json2 = class_model.to_dict()
        assert class_model_json2 == class_model_json

class TestModel_ClassResult():
    """
    Test Class for ClassResult
    """

    def test_class_result_serialization(self):
        """
        Test serialization/deserialization for ClassResult
        """

        # Construct a json representation of a ClassResult model
        class_result_model_json = {}
        class_result_model_json['class'] = 'testString'
        class_result_model_json['score'] = 0
        class_result_model_json['type_hierarchy'] = 'testString'

        # Construct a model instance of ClassResult by calling from_dict on the json representation
        class_result_model = ClassResult.from_dict(class_result_model_json)
        assert class_result_model != False

        # Construct a model instance of ClassResult by calling from_dict on the json representation
        class_result_model_dict = ClassResult.from_dict(class_result_model_json).__dict__
        class_result_model2 = ClassResult(**class_result_model_dict)

        # Verify the model instances are equivalent
        assert class_result_model == class_result_model2

        # Convert model instance back to dict and verify no loss of data
        class_result_model_json2 = class_result_model.to_dict()
        assert class_result_model_json2 == class_result_model_json

class TestModel_ClassifiedImage():
    """
    Test Class for ClassifiedImage
    """

    def test_classified_image_serialization(self):
        """
        Test serialization/deserialization for ClassifiedImage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_info_model = {} # ErrorInfo
        error_info_model['code'] = 38
        error_info_model['description'] = 'testString'
        error_info_model['error_id'] = 'testString'

        class_result_model = {} # ClassResult
        class_result_model['class'] = 'testString'
        class_result_model['score'] = 0
        class_result_model['type_hierarchy'] = 'testString'

        classifier_result_model = {} # ClassifierResult
        classifier_result_model['name'] = 'testString'
        classifier_result_model['classifier_id'] = 'testString'
        classifier_result_model['classes'] = [class_result_model]

        # Construct a json representation of a ClassifiedImage model
        classified_image_model_json = {}
        classified_image_model_json['source_url'] = 'testString'
        classified_image_model_json['resolved_url'] = 'testString'
        classified_image_model_json['image'] = 'testString'
        classified_image_model_json['error'] = error_info_model
        classified_image_model_json['classifiers'] = [classifier_result_model]

        # Construct a model instance of ClassifiedImage by calling from_dict on the json representation
        classified_image_model = ClassifiedImage.from_dict(classified_image_model_json)
        assert classified_image_model != False

        # Construct a model instance of ClassifiedImage by calling from_dict on the json representation
        classified_image_model_dict = ClassifiedImage.from_dict(classified_image_model_json).__dict__
        classified_image_model2 = ClassifiedImage(**classified_image_model_dict)

        # Verify the model instances are equivalent
        assert classified_image_model == classified_image_model2

        # Convert model instance back to dict and verify no loss of data
        classified_image_model_json2 = classified_image_model.to_dict()
        assert classified_image_model_json2 == classified_image_model_json

class TestModel_ClassifiedImages():
    """
    Test Class for ClassifiedImages
    """

    def test_classified_images_serialization(self):
        """
        Test serialization/deserialization for ClassifiedImages
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_info_model = {} # ErrorInfo
        error_info_model['code'] = 38
        error_info_model['description'] = 'testString'
        error_info_model['error_id'] = 'testString'

        class_result_model = {} # ClassResult
        class_result_model['class'] = 'testString'
        class_result_model['score'] = 0
        class_result_model['type_hierarchy'] = 'testString'

        classifier_result_model = {} # ClassifierResult
        classifier_result_model['name'] = 'testString'
        classifier_result_model['classifier_id'] = 'testString'
        classifier_result_model['classes'] = [class_result_model]

        classified_image_model = {} # ClassifiedImage
        classified_image_model['source_url'] = 'testString'
        classified_image_model['resolved_url'] = 'testString'
        classified_image_model['image'] = 'testString'
        classified_image_model['error'] = error_info_model
        classified_image_model['classifiers'] = [classifier_result_model]

        warning_info_model = {} # WarningInfo
        warning_info_model['warning_id'] = 'testString'
        warning_info_model['description'] = 'testString'

        # Construct a json representation of a ClassifiedImages model
        classified_images_model_json = {}
        classified_images_model_json['custom_classes'] = 38
        classified_images_model_json['images_processed'] = 38
        classified_images_model_json['images'] = [classified_image_model]
        classified_images_model_json['warnings'] = [warning_info_model]

        # Construct a model instance of ClassifiedImages by calling from_dict on the json representation
        classified_images_model = ClassifiedImages.from_dict(classified_images_model_json)
        assert classified_images_model != False

        # Construct a model instance of ClassifiedImages by calling from_dict on the json representation
        classified_images_model_dict = ClassifiedImages.from_dict(classified_images_model_json).__dict__
        classified_images_model2 = ClassifiedImages(**classified_images_model_dict)

        # Verify the model instances are equivalent
        assert classified_images_model == classified_images_model2

        # Convert model instance back to dict and verify no loss of data
        classified_images_model_json2 = classified_images_model.to_dict()
        assert classified_images_model_json2 == classified_images_model_json

class TestModel_Classifier():
    """
    Test Class for Classifier
    """

    def test_classifier_serialization(self):
        """
        Test serialization/deserialization for Classifier
        """

        # Construct dict forms of any model objects needed in order to build this model.

        class_model = {} # Class
        class_model['class'] = 'testString'

        # Construct a json representation of a Classifier model
        classifier_model_json = {}
        classifier_model_json['classifier_id'] = 'testString'
        classifier_model_json['name'] = 'testString'
        classifier_model_json['owner'] = 'testString'
        classifier_model_json['status'] = 'ready'
        classifier_model_json['core_ml_enabled'] = True
        classifier_model_json['explanation'] = 'testString'
        classifier_model_json['created'] = "2019-01-01T12:00:00Z"
        classifier_model_json['classes'] = [class_model]
        classifier_model_json['retrained'] = "2019-01-01T12:00:00Z"
        classifier_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Classifier by calling from_dict on the json representation
        classifier_model = Classifier.from_dict(classifier_model_json)
        assert classifier_model != False

        # Construct a model instance of Classifier by calling from_dict on the json representation
        classifier_model_dict = Classifier.from_dict(classifier_model_json).__dict__
        classifier_model2 = Classifier(**classifier_model_dict)

        # Verify the model instances are equivalent
        assert classifier_model == classifier_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_model_json2 = classifier_model.to_dict()
        assert classifier_model_json2 == classifier_model_json

class TestModel_ClassifierResult():
    """
    Test Class for ClassifierResult
    """

    def test_classifier_result_serialization(self):
        """
        Test serialization/deserialization for ClassifierResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        class_result_model = {} # ClassResult
        class_result_model['class'] = 'testString'
        class_result_model['score'] = 0
        class_result_model['type_hierarchy'] = 'testString'

        # Construct a json representation of a ClassifierResult model
        classifier_result_model_json = {}
        classifier_result_model_json['name'] = 'testString'
        classifier_result_model_json['classifier_id'] = 'testString'
        classifier_result_model_json['classes'] = [class_result_model]

        # Construct a model instance of ClassifierResult by calling from_dict on the json representation
        classifier_result_model = ClassifierResult.from_dict(classifier_result_model_json)
        assert classifier_result_model != False

        # Construct a model instance of ClassifierResult by calling from_dict on the json representation
        classifier_result_model_dict = ClassifierResult.from_dict(classifier_result_model_json).__dict__
        classifier_result_model2 = ClassifierResult(**classifier_result_model_dict)

        # Verify the model instances are equivalent
        assert classifier_result_model == classifier_result_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_result_model_json2 = classifier_result_model.to_dict()
        assert classifier_result_model_json2 == classifier_result_model_json

class TestModel_Classifiers():
    """
    Test Class for Classifiers
    """

    def test_classifiers_serialization(self):
        """
        Test serialization/deserialization for Classifiers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        class_model = {} # Class
        class_model['class'] = 'testString'

        classifier_model = {} # Classifier
        classifier_model['classifier_id'] = 'testString'
        classifier_model['name'] = 'testString'
        classifier_model['owner'] = 'testString'
        classifier_model['status'] = 'ready'
        classifier_model['core_ml_enabled'] = True
        classifier_model['explanation'] = 'testString'
        classifier_model['created'] = "2019-01-01T12:00:00Z"
        classifier_model['classes'] = [class_model]
        classifier_model['retrained'] = "2019-01-01T12:00:00Z"
        classifier_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a Classifiers model
        classifiers_model_json = {}
        classifiers_model_json['classifiers'] = [classifier_model]

        # Construct a model instance of Classifiers by calling from_dict on the json representation
        classifiers_model = Classifiers.from_dict(classifiers_model_json)
        assert classifiers_model != False

        # Construct a model instance of Classifiers by calling from_dict on the json representation
        classifiers_model_dict = Classifiers.from_dict(classifiers_model_json).__dict__
        classifiers_model2 = Classifiers(**classifiers_model_dict)

        # Verify the model instances are equivalent
        assert classifiers_model == classifiers_model2

        # Convert model instance back to dict and verify no loss of data
        classifiers_model_json2 = classifiers_model.to_dict()
        assert classifiers_model_json2 == classifiers_model_json

class TestModel_ErrorInfo():
    """
    Test Class for ErrorInfo
    """

    def test_error_info_serialization(self):
        """
        Test serialization/deserialization for ErrorInfo
        """

        # Construct a json representation of a ErrorInfo model
        error_info_model_json = {}
        error_info_model_json['code'] = 38
        error_info_model_json['description'] = 'testString'
        error_info_model_json['error_id'] = 'testString'

        # Construct a model instance of ErrorInfo by calling from_dict on the json representation
        error_info_model = ErrorInfo.from_dict(error_info_model_json)
        assert error_info_model != False

        # Construct a model instance of ErrorInfo by calling from_dict on the json representation
        error_info_model_dict = ErrorInfo.from_dict(error_info_model_json).__dict__
        error_info_model2 = ErrorInfo(**error_info_model_dict)

        # Verify the model instances are equivalent
        assert error_info_model == error_info_model2

        # Convert model instance back to dict and verify no loss of data
        error_info_model_json2 = error_info_model.to_dict()
        assert error_info_model_json2 == error_info_model_json

class TestModel_WarningInfo():
    """
    Test Class for WarningInfo
    """

    def test_warning_info_serialization(self):
        """
        Test serialization/deserialization for WarningInfo
        """

        # Construct a json representation of a WarningInfo model
        warning_info_model_json = {}
        warning_info_model_json['warning_id'] = 'testString'
        warning_info_model_json['description'] = 'testString'

        # Construct a model instance of WarningInfo by calling from_dict on the json representation
        warning_info_model = WarningInfo.from_dict(warning_info_model_json)
        assert warning_info_model != False

        # Construct a model instance of WarningInfo by calling from_dict on the json representation
        warning_info_model_dict = WarningInfo.from_dict(warning_info_model_json).__dict__
        warning_info_model2 = WarningInfo(**warning_info_model_dict)

        # Verify the model instances are equivalent
        assert warning_info_model == warning_info_model2

        # Convert model instance back to dict and verify no loss of data
        warning_info_model_json2 = warning_info_model.to_dict()
        assert warning_info_model_json2 == warning_info_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
