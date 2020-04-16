# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
import ibm_watson.natural_language_understanding_v1
from ibm_watson.natural_language_understanding_v1 import *

base_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api'

##############################################################################
# Start of Service: Analyze
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for analyze
#-----------------------------------------------------------------------------
class TestAnalyze():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_response(self):
        body = self.construct_full_body()
        response = fake_response_AnalysisResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AnalysisResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_empty(self):
        check_empty_required_params(self, fake_response_AnalysisResults_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/analyze'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NaturalLanguageUnderstandingV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-07-12',
            )
        service.set_service_url(base_url)
        output = service.analyze(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"features": Features._from_dict(json.loads("""{"concepts": {"limit": 5}, "emotion": {"document": true, "targets": []}, "entities": {"limit": 5, "mentions": true, "model": "fake_model", "sentiment": false, "emotion": false}, "keywords": {"limit": 5, "sentiment": false, "emotion": false}, "metadata": {}, "relations": {"model": "fake_model"}, "semantic_roles": {"limit": 5, "keywords": true, "entities": true}, "sentiment": {"document": true, "targets": []}, "categories": {"explanation": false, "limit": 5, "model": "fake_model"}, "syntax": {"tokens": {"lemma": false, "part_of_speech": true}, "sentences": false}}""")), "text": "string1", "html": "string1", "url": "string1", "clean": True, "xpath": "string1", "fallback_to_raw": True, "return_analyzed_text": True, "language": "string1", "limit_text_characters": 12345, })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"features": Features._from_dict(json.loads("""{"concepts": {"limit": 5}, "emotion": {"document": true, "targets": []}, "entities": {"limit": 5, "mentions": true, "model": "fake_model", "sentiment": false, "emotion": false}, "keywords": {"limit": 5, "sentiment": false, "emotion": false}, "metadata": {}, "relations": {"model": "fake_model"}, "semantic_roles": {"limit": 5, "keywords": true, "entities": true}, "sentiment": {"document": true, "targets": []}, "categories": {"explanation": false, "limit": 5, "model": "fake_model"}, "syntax": {"tokens": {"lemma": false, "part_of_speech": true}, "sentences": false}}""")), "text": "string1", "html": "string1", "url": "string1", "clean": True, "xpath": "string1", "fallback_to_raw": True, "return_analyzed_text": True, "language": "string1", "limit_text_characters": 12345, })
        return body


# endregion
##############################################################################
# End of Service: Analyze
##############################################################################

##############################################################################
# Start of Service: ManageModels
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_models
#-----------------------------------------------------------------------------
class TestListModels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_response(self):
        body = self.construct_full_body()
        response = fake_response_ListModelsResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListModelsResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/models'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NaturalLanguageUnderstandingV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-07-12',
            )
        service.set_service_url(base_url)
        output = service.list_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_model
#-----------------------------------------------------------------------------
class TestDeleteModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteModelResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteModelResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_empty(self):
        check_empty_required_params(self, fake_response_DeleteModelResults_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/models/{0}'.format(body['model_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = NaturalLanguageUnderstandingV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-07-12',
            )
        service.set_service_url(base_url)
        output = service.delete_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: ManageModels
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
fake_response_AnalysisResults_json = """{"language": "fake_language", "analyzed_text": "fake_analyzed_text", "retrieved_url": "fake_retrieved_url", "usage": {"features": 8, "text_characters": 15, "text_units": 10}, "concepts": [], "entities": [], "keywords": [], "categories": [], "emotion": {"document": {"emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}}, "targets": []}, "metadata": {"authors": [], "publication_date": "fake_publication_date", "title": "fake_title", "image": "fake_image", "feeds": []}, "relations": [], "semantic_roles": [], "sentiment": {"document": {"label": "fake_label", "score": 5}, "targets": []}, "syntax": {"tokens": [], "sentences": []}}"""
fake_response_ListModelsResults_json = """{"models": []}"""
fake_response_DeleteModelResults_json = """{"deleted": "fake_deleted"}"""
