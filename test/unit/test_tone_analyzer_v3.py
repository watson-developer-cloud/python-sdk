# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
import ibm_watson.tone_analyzer_v3
from ibm_watson.tone_analyzer_v3 import *

base_url = 'https://gateway.watsonplatform.net/tone-analyzer/api'

##############################################################################
# Start of Service: Methods
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for tone
#-----------------------------------------------------------------------------
class TestTone():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_response(self):
        body = self.construct_full_body()
        response = fake_response_ToneAnalysis_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ToneAnalysis_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_empty(self):
        check_empty_required_params(self, fake_response_ToneAnalysis_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/tone'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = ToneAnalyzerV3(
            authenticator=NoAuthAuthenticator(),
            version='2017-09-21',
            )
        service.set_service_url(base_url)
        output = service.tone(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"tone_input": {"mock": "data"}})
        body['content_type'] = "string1"
        body['sentences'] = True
        body['tones'] = []
        body['content_language'] = "string1"
        body['accept_language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"tone_input": {"mock": "data"}})
        return body


#-----------------------------------------------------------------------------
# Test Class for tone_chat
#-----------------------------------------------------------------------------
class TestToneChat():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_chat_response(self):
        body = self.construct_full_body()
        response = fake_response_UtteranceAnalyses_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_chat_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_UtteranceAnalyses_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_tone_chat_empty(self):
        check_empty_required_params(self, fake_response_UtteranceAnalyses_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/tone_chat'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = ToneAnalyzerV3(
            authenticator=NoAuthAuthenticator(),
            version='2017-09-21',
            )
        service.set_service_url(base_url)
        output = service.tone_chat(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"utterances": [], })
        body['content_language'] = "string1"
        body['accept_language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"utterances": [], })
        return body


# endregion
##############################################################################
# End of Service: Methods
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
fake_response_ToneAnalysis_json = """{"document_tone": {"tones": [], "tone_categories": [], "warning": "fake_warning"}, "sentences_tone": []}"""
fake_response_UtteranceAnalyses_json = """{"utterances_tone": [], "warning": "fake_warning"}"""
