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
import ibm_watson.assistant_v2
from ibm_watson.assistant_v2 import *

base_url = 'https://gateway.watsonplatform.net/assistant/api'

##############################################################################
# Start of Service: Sessions
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_session
#-----------------------------------------------------------------------------
class TestCreateSession():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_session_response(self):
        body = self.construct_full_body()
        response = fake_response_SessionResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_session_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_SessionResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_session_empty(self):
        check_empty_required_params(self, fake_response_SessionResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/assistants/{0}/sessions'.format(body['assistant_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV2(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_session(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_session
#-----------------------------------------------------------------------------
class TestDeleteSession():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_session_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_session_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_session_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/assistants/{0}/sessions/{1}'.format(body['assistant_id'], body['session_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV2(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_session(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        body['session_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        body['session_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Sessions
##############################################################################

##############################################################################
# Start of Service: Message
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for message
#-----------------------------------------------------------------------------
class TestMessage():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_message_response(self):
        body = self.construct_full_body()
        response = fake_response_MessageResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_message_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MessageResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_message_empty(self):
        check_empty_required_params(self, fake_response_MessageResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/assistants/{0}/sessions/{1}/message'.format(body['assistant_id'], body['session_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV2(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.message(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        body['session_id'] = "string1"
        body.update({"input": MessageInput._from_dict(json.loads("""{"message_type": "fake_message_type", "text": "fake_text", "options": {"debug": false, "restart": false, "alternate_intents": false, "return_context": true, "export": true}, "intents": [], "entities": [], "suggestion_id": "fake_suggestion_id"}""")), "context": MessageContext._from_dict(json.loads("""{"global": {"system": {"timezone": "fake_timezone", "user_id": "fake_user_id", "turn_count": 10, "locale": "fake_locale", "reference_time": "fake_reference_time"}}, "skills": {}}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body['assistant_id'] = "string1"
        body['session_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Message
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
fake_response_SessionResponse_json = """{"session_id": "fake_session_id"}"""
fake_response_MessageResponse_json = """{"output": {"generic": [], "intents": [], "entities": [], "actions": [], "debug": {"nodes_visited": [], "log_messages": [], "branch_exited": false, "branch_exited_reason": "fake_branch_exited_reason"}}, "context": {"global": {"system": {"timezone": "fake_timezone", "user_id": "fake_user_id", "turn_count": 10, "locale": "fake_locale", "reference_time": "fake_reference_time"}}, "skills": {}}}"""
