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

from datetime import datetime
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
import ibm_watson.assistant_v1
from ibm_watson.assistant_v1 import *

base_url = 'https://gateway.watsonplatform.net/assistant/api'

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
        endpoint = '/v1/workspaces/{0}/message'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.message(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"input": MessageInput._from_dict(json.loads("""{"text": "fake_text"}""")), "intents": [], "entities": [], "alternate_intents": True, "context": Context._from_dict(json.loads("""{"conversation_id": "fake_conversation_id", "system": {}, "metadata": {"deployment": "fake_deployment", "user_id": "fake_user_id"}}""")), "output": OutputData._from_dict(json.loads("""{"nodes_visited": [], "nodes_visited_details": [], "log_messages": [], "text": [], "generic": []}""")), })
        body['nodes_visited_details'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Message
##############################################################################

##############################################################################
# Start of Service: Workspaces
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_workspaces
#-----------------------------------------------------------------------------
class TestListWorkspaces():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_workspaces_response(self):
        body = self.construct_full_body()
        response = fake_response_WorkspaceCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_workspaces_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_WorkspaceCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_workspaces_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_workspaces(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for create_workspace
#-----------------------------------------------------------------------------
class TestCreateWorkspace():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_workspace_response(self):
        body = self.construct_full_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_workspace_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_workspace_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_workspace(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "description": "string1", "language": "string1", "metadata": {"mock": "data"}, "learning_opt_out": True, "system_settings": WorkspaceSystemSettings._from_dict(json.loads("""{"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "fake_prompt", "none_of_the_above_prompt": "fake_none_of_the_above_prompt", "enabled": false, "sensitivity": "fake_sensitivity", "randomize": false, "max_suggestions": 15, "suggestion_text_policy": "fake_suggestion_text_policy"}, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}""")), "intents": [], "entities": [], "dialog_nodes": [], "counterexamples": [], "webhooks": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_workspace
#-----------------------------------------------------------------------------
class TestGetWorkspace():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_workspace_response(self):
        body = self.construct_full_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_workspace_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_workspace_empty(self):
        check_empty_required_params(self, fake_response_Workspace_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_workspace(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['export'] = True
        body['include_audit'] = True
        body['sort'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_workspace
#-----------------------------------------------------------------------------
class TestUpdateWorkspace():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_workspace_response(self):
        body = self.construct_full_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_workspace_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Workspace_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_workspace_empty(self):
        check_empty_required_params(self, fake_response_Workspace_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_workspace(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "language": "string1", "metadata": {"mock": "data"}, "learning_opt_out": True, "system_settings": WorkspaceSystemSettings._from_dict(json.loads("""{"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "fake_prompt", "none_of_the_above_prompt": "fake_none_of_the_above_prompt", "enabled": false, "sensitivity": "fake_sensitivity", "randomize": false, "max_suggestions": 15, "suggestion_text_policy": "fake_suggestion_text_policy"}, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}""")), "intents": [], "entities": [], "dialog_nodes": [], "counterexamples": [], "webhooks": [], })
        body['append'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_workspace
#-----------------------------------------------------------------------------
class TestDeleteWorkspace():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_workspace_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_workspace_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_workspace_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_workspace(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Workspaces
##############################################################################

##############################################################################
# Start of Service: Intents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_intents
#-----------------------------------------------------------------------------
class TestListIntents():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_intents_response(self):
        body = self.construct_full_body()
        response = fake_response_IntentCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_intents_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_IntentCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_intents_empty(self):
        check_empty_required_params(self, fake_response_IntentCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_intents(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['export'] = True
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_intent
#-----------------------------------------------------------------------------
class TestCreateIntent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_intent_response(self):
        body = self.construct_full_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_intent_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_intent_empty(self):
        check_empty_required_params(self, fake_response_Intent_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_intent(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"intent": "string1", "description": "string1", "examples": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"intent": "string1", "description": "string1", "examples": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_intent
#-----------------------------------------------------------------------------
class TestGetIntent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_intent_response(self):
        body = self.construct_full_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_intent_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_intent_empty(self):
        check_empty_required_params(self, fake_response_Intent_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}'.format(body['workspace_id'], body['intent'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_intent(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['export'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_intent
#-----------------------------------------------------------------------------
class TestUpdateIntent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_intent_response(self):
        body = self.construct_full_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_intent_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Intent_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_intent_empty(self):
        check_empty_required_params(self, fake_response_Intent_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}'.format(body['workspace_id'], body['intent'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_intent(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body.update({"new_intent": "string1", "new_description": "string1", "new_examples": [], })
        body['append'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body.update({"new_intent": "string1", "new_description": "string1", "new_examples": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_intent
#-----------------------------------------------------------------------------
class TestDeleteIntent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_intent_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_intent_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_intent_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}'.format(body['workspace_id'], body['intent'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_intent(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Intents
##############################################################################

##############################################################################
# Start of Service: Examples
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_examples
#-----------------------------------------------------------------------------
class TestListExamples():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_examples_response(self):
        body = self.construct_full_body()
        response = fake_response_ExampleCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_examples_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ExampleCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_examples_empty(self):
        check_empty_required_params(self, fake_response_ExampleCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}/examples'.format(body['workspace_id'], body['intent'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_examples(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_example
#-----------------------------------------------------------------------------
class TestCreateExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_example_response(self):
        body = self.construct_full_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_example_empty(self):
        check_empty_required_params(self, fake_response_Example_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}/examples'.format(body['workspace_id'], body['intent'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body.update({"text": "string1", "mentions": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body.update({"text": "string1", "mentions": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_example
#-----------------------------------------------------------------------------
class TestGetExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_example_response(self):
        body = self.construct_full_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_example_empty(self):
        check_empty_required_params(self, fake_response_Example_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(body['workspace_id'], body['intent'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_example
#-----------------------------------------------------------------------------
class TestUpdateExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_example_response(self):
        body = self.construct_full_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Example_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_example_empty(self):
        check_empty_required_params(self, fake_response_Example_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(body['workspace_id'], body['intent'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        body.update({"new_text": "string1", "new_mentions": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        body.update({"new_text": "string1", "new_mentions": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_example
#-----------------------------------------------------------------------------
class TestDeleteExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_example_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_example_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(body['workspace_id'], body['intent'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['intent'] = "string1"
        body['text'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Examples
##############################################################################

##############################################################################
# Start of Service: Counterexamples
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_counterexamples
#-----------------------------------------------------------------------------
class TestListCounterexamples():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_counterexamples_response(self):
        body = self.construct_full_body()
        response = fake_response_CounterexampleCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_counterexamples_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CounterexampleCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_counterexamples_empty(self):
        check_empty_required_params(self, fake_response_CounterexampleCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/counterexamples'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_counterexamples(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_counterexample
#-----------------------------------------------------------------------------
class TestCreateCounterexample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_counterexample_response(self):
        body = self.construct_full_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_counterexample_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_counterexample_empty(self):
        check_empty_required_params(self, fake_response_Counterexample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/counterexamples'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_counterexample(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"text": "string1", })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"text": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_counterexample
#-----------------------------------------------------------------------------
class TestGetCounterexample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_counterexample_response(self):
        body = self.construct_full_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_counterexample_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_counterexample_empty(self):
        check_empty_required_params(self, fake_response_Counterexample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(body['workspace_id'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_counterexample(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_counterexample
#-----------------------------------------------------------------------------
class TestUpdateCounterexample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_counterexample_response(self):
        body = self.construct_full_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_counterexample_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Counterexample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_counterexample_empty(self):
        check_empty_required_params(self, fake_response_Counterexample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(body['workspace_id'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_counterexample(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        body.update({"new_text": "string1", })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        body.update({"new_text": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_counterexample
#-----------------------------------------------------------------------------
class TestDeleteCounterexample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_counterexample_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_counterexample_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_counterexample_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(body['workspace_id'], body['text'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_counterexample(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['text'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Counterexamples
##############################################################################

##############################################################################
# Start of Service: Entities
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_entities
#-----------------------------------------------------------------------------
class TestListEntities():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_entities_response(self):
        body = self.construct_full_body()
        response = fake_response_EntityCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_entities_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_EntityCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_entities_empty(self):
        check_empty_required_params(self, fake_response_EntityCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_entities(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['export'] = True
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_entity
#-----------------------------------------------------------------------------
class TestCreateEntity():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_entity_response(self):
        body = self.construct_full_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_entity_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_entity_empty(self):
        check_empty_required_params(self, fake_response_Entity_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_entity(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"entity": "string1", "description": "string1", "metadata": {"mock": "data"}, "fuzzy_match": True, "values": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"entity": "string1", "description": "string1", "metadata": {"mock": "data"}, "fuzzy_match": True, "values": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_entity
#-----------------------------------------------------------------------------
class TestGetEntity():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_entity_response(self):
        body = self.construct_full_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_entity_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_entity_empty(self):
        check_empty_required_params(self, fake_response_Entity_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_entity(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['export'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_entity
#-----------------------------------------------------------------------------
class TestUpdateEntity():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_entity_response(self):
        body = self.construct_full_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_entity_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Entity_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_entity_empty(self):
        check_empty_required_params(self, fake_response_Entity_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_entity(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body.update({"new_entity": "string1", "new_description": "string1", "new_metadata": {"mock": "data"}, "new_fuzzy_match": True, "new_values": [], })
        body['append'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body.update({"new_entity": "string1", "new_description": "string1", "new_metadata": {"mock": "data"}, "new_fuzzy_match": True, "new_values": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_entity
#-----------------------------------------------------------------------------
class TestDeleteEntity():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_entity_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_entity_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_entity_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_entity(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Entities
##############################################################################

##############################################################################
# Start of Service: Mentions
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_mentions
#-----------------------------------------------------------------------------
class TestListMentions():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_mentions_response(self):
        body = self.construct_full_body()
        response = fake_response_EntityMentionCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_mentions_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_EntityMentionCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_mentions_empty(self):
        check_empty_required_params(self, fake_response_EntityMentionCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/mentions'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_mentions(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['export'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Mentions
##############################################################################

##############################################################################
# Start of Service: Values
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_values
#-----------------------------------------------------------------------------
class TestListValues():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_values_response(self):
        body = self.construct_full_body()
        response = fake_response_ValueCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_values_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ValueCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_values_empty(self):
        check_empty_required_params(self, fake_response_ValueCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_values(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['export'] = True
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_value
#-----------------------------------------------------------------------------
class TestCreateValue():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_value_response(self):
        body = self.construct_full_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_value_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_value_empty(self):
        check_empty_required_params(self, fake_response_Value_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values'.format(body['workspace_id'], body['entity'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_value(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body.update({"value": "string1", "metadata": {"mock": "data"}, "type": "string1", "synonyms": [], "patterns": [], })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body.update({"value": "string1", "metadata": {"mock": "data"}, "type": "string1", "synonyms": [], "patterns": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_value
#-----------------------------------------------------------------------------
class TestGetValue():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_value_response(self):
        body = self.construct_full_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_value_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_value_empty(self):
        check_empty_required_params(self, fake_response_Value_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(body['workspace_id'], body['entity'], body['value'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_value(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['export'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_value
#-----------------------------------------------------------------------------
class TestUpdateValue():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_value_response(self):
        body = self.construct_full_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_value_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Value_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_value_empty(self):
        check_empty_required_params(self, fake_response_Value_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(body['workspace_id'], body['entity'], body['value'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_value(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body.update({"new_value": "string1", "new_metadata": {"mock": "data"}, "new_type": "string1", "new_synonyms": [], "new_patterns": [], })
        body['append'] = True
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body.update({"new_value": "string1", "new_metadata": {"mock": "data"}, "new_type": "string1", "new_synonyms": [], "new_patterns": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_value
#-----------------------------------------------------------------------------
class TestDeleteValue():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_value_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_value_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_value_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(body['workspace_id'], body['entity'], body['value'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_value(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Values
##############################################################################

##############################################################################
# Start of Service: Synonyms
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_synonyms
#-----------------------------------------------------------------------------
class TestListSynonyms():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_synonyms_response(self):
        body = self.construct_full_body()
        response = fake_response_SynonymCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_synonyms_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_SynonymCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_synonyms_empty(self):
        check_empty_required_params(self, fake_response_SynonymCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(body['workspace_id'], body['entity'], body['value'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_synonyms(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_synonym
#-----------------------------------------------------------------------------
class TestCreateSynonym():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_synonym_response(self):
        body = self.construct_full_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_synonym_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_synonym_empty(self):
        check_empty_required_params(self, fake_response_Synonym_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(body['workspace_id'], body['entity'], body['value'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_synonym(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body.update({"synonym": "string1", })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body.update({"synonym": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_synonym
#-----------------------------------------------------------------------------
class TestGetSynonym():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_synonym_response(self):
        body = self.construct_full_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_synonym_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_synonym_empty(self):
        check_empty_required_params(self, fake_response_Synonym_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(body['workspace_id'], body['entity'], body['value'], body['synonym'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_synonym(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_synonym
#-----------------------------------------------------------------------------
class TestUpdateSynonym():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_synonym_response(self):
        body = self.construct_full_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_synonym_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Synonym_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_synonym_empty(self):
        check_empty_required_params(self, fake_response_Synonym_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(body['workspace_id'], body['entity'], body['value'], body['synonym'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_synonym(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        body.update({"new_synonym": "string1", })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        body.update({"new_synonym": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_synonym
#-----------------------------------------------------------------------------
class TestDeleteSynonym():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_synonym_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_synonym_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_synonym_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(body['workspace_id'], body['entity'], body['value'], body['synonym'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_synonym(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['entity'] = "string1"
        body['value'] = "string1"
        body['synonym'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Synonyms
##############################################################################

##############################################################################
# Start of Service: DialogNodes
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_dialog_nodes
#-----------------------------------------------------------------------------
class TestListDialogNodes():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_dialog_nodes_response(self):
        body = self.construct_full_body()
        response = fake_response_DialogNodeCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_dialog_nodes_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DialogNodeCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_dialog_nodes_empty(self):
        check_empty_required_params(self, fake_response_DialogNodeCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/dialog_nodes'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_dialog_nodes(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['page_limit'] = 12345
        body['sort'] = "string1"
        body['cursor'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_dialog_node
#-----------------------------------------------------------------------------
class TestCreateDialogNode():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_dialog_node_response(self):
        body = self.construct_full_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_dialog_node_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_dialog_node_empty(self):
        check_empty_required_params(self, fake_response_DialogNode_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/dialog_nodes'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.create_dialog_node(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"dialog_node": "string1", "description": "string1", "conditions": "string1", "parent": "string1", "previous_sibling": "string1", "output": DialogNodeOutput._from_dict(json.loads("""{"generic": [], "modifiers": {"overwrite": false}}""")), "context": {"mock": "data"}, "metadata": {"mock": "data"}, "next_step": DialogNodeNextStep._from_dict(json.loads("""{"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}""")), "title": "string1", "type": "string1", "event_name": "string1", "variable": "string1", "actions": [], "digress_in": "string1", "digress_out": "string1", "digress_out_slots": "string1", "user_label": "string1", "disambiguation_opt_out": True, })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body.update({"dialog_node": "string1", "description": "string1", "conditions": "string1", "parent": "string1", "previous_sibling": "string1", "output": DialogNodeOutput._from_dict(json.loads("""{"generic": [], "modifiers": {"overwrite": false}}""")), "context": {"mock": "data"}, "metadata": {"mock": "data"}, "next_step": DialogNodeNextStep._from_dict(json.loads("""{"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}""")), "title": "string1", "type": "string1", "event_name": "string1", "variable": "string1", "actions": [], "digress_in": "string1", "digress_out": "string1", "digress_out_slots": "string1", "user_label": "string1", "disambiguation_opt_out": True, })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_dialog_node
#-----------------------------------------------------------------------------
class TestGetDialogNode():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_dialog_node_response(self):
        body = self.construct_full_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_dialog_node_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_dialog_node_empty(self):
        check_empty_required_params(self, fake_response_DialogNode_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(body['workspace_id'], body['dialog_node'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.get_dialog_node(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_dialog_node
#-----------------------------------------------------------------------------
class TestUpdateDialogNode():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_dialog_node_response(self):
        body = self.construct_full_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_dialog_node_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DialogNode_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_dialog_node_empty(self):
        check_empty_required_params(self, fake_response_DialogNode_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(body['workspace_id'], body['dialog_node'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.update_dialog_node(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        body.update({"new_dialog_node": "string1", "new_description": "string1", "new_conditions": "string1", "new_parent": "string1", "new_previous_sibling": "string1", "new_output": DialogNodeOutput._from_dict(json.loads("""{"generic": [], "modifiers": {"overwrite": false}}""")), "new_context": {"mock": "data"}, "new_metadata": {"mock": "data"}, "new_next_step": DialogNodeNextStep._from_dict(json.loads("""{"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}""")), "new_title": "string1", "new_type": "string1", "new_event_name": "string1", "new_variable": "string1", "new_actions": [], "new_digress_in": "string1", "new_digress_out": "string1", "new_digress_out_slots": "string1", "new_user_label": "string1", "new_disambiguation_opt_out": True, })
        body['include_audit'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        body.update({"new_dialog_node": "string1", "new_description": "string1", "new_conditions": "string1", "new_parent": "string1", "new_previous_sibling": "string1", "new_output": DialogNodeOutput._from_dict(json.loads("""{"generic": [], "modifiers": {"overwrite": false}}""")), "new_context": {"mock": "data"}, "new_metadata": {"mock": "data"}, "new_next_step": DialogNodeNextStep._from_dict(json.loads("""{"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}""")), "new_title": "string1", "new_type": "string1", "new_event_name": "string1", "new_variable": "string1", "new_actions": [], "new_digress_in": "string1", "new_digress_out": "string1", "new_digress_out_slots": "string1", "new_user_label": "string1", "new_disambiguation_opt_out": True, })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_dialog_node
#-----------------------------------------------------------------------------
class TestDeleteDialogNode():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dialog_node_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dialog_node_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_dialog_node_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(body['workspace_id'], body['dialog_node'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.delete_dialog_node(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['dialog_node'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: DialogNodes
##############################################################################

##############################################################################
# Start of Service: Logs
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_logs
#-----------------------------------------------------------------------------
class TestListLogs():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_logs_response(self):
        body = self.construct_full_body()
        response = fake_response_LogCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_logs_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LogCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_logs_empty(self):
        check_empty_required_params(self, fake_response_LogCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/workspaces/{0}/logs'.format(body['workspace_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_logs(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        body['sort'] = "string1"
        body['filter'] = "string1"
        body['page_limit'] = 12345
        body['cursor'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['workspace_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_all_logs
#-----------------------------------------------------------------------------
class TestListAllLogs():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_logs_response(self):
        body = self.construct_full_body()
        response = fake_response_LogCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_logs_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LogCollection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_all_logs_empty(self):
        check_empty_required_params(self, fake_response_LogCollection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/logs'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
            )
        service.set_service_url(base_url)
        output = service.list_all_logs(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['filter'] = "string1"
        body['sort'] = "string1"
        body['page_limit'] = 12345
        body['cursor'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['filter'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Logs
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
        endpoint = '/v1/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='')
    
    def call_service(self, body):
        service = AssistantV1(
            authenticator=NoAuthAuthenticator(),
            version='2020-04-01',
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
fake_response_MessageResponse_json = """{"input": {"text": "fake_text"}, "intents": [], "entities": [], "alternate_intents": false, "context": {"conversation_id": "fake_conversation_id", "system": {}, "metadata": {"deployment": "fake_deployment", "user_id": "fake_user_id"}}, "output": {"nodes_visited": [], "nodes_visited_details": [], "log_messages": [], "text": [], "generic": []}, "actions": []}"""
fake_response_WorkspaceCollection_json = """{"workspaces": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Workspace_json = """{"name": "fake_name", "description": "fake_description", "language": "fake_language", "learning_opt_out": true, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "fake_prompt", "none_of_the_above_prompt": "fake_none_of_the_above_prompt", "enabled": false, "sensitivity": "fake_sensitivity", "randomize": false, "max_suggestions": 15, "suggestion_text_policy": "fake_suggestion_text_policy"}, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "workspace_id": "fake_workspace_id", "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "intents": [], "entities": [], "dialog_nodes": [], "counterexamples": [], "webhooks": []}"""
fake_response_Workspace_json = """{"name": "fake_name", "description": "fake_description", "language": "fake_language", "learning_opt_out": true, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "fake_prompt", "none_of_the_above_prompt": "fake_none_of_the_above_prompt", "enabled": false, "sensitivity": "fake_sensitivity", "randomize": false, "max_suggestions": 15, "suggestion_text_policy": "fake_suggestion_text_policy"}, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "workspace_id": "fake_workspace_id", "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "intents": [], "entities": [], "dialog_nodes": [], "counterexamples": [], "webhooks": []}"""
fake_response_Workspace_json = """{"name": "fake_name", "description": "fake_description", "language": "fake_language", "learning_opt_out": true, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "fake_prompt", "none_of_the_above_prompt": "fake_none_of_the_above_prompt", "enabled": false, "sensitivity": "fake_sensitivity", "randomize": false, "max_suggestions": 15, "suggestion_text_policy": "fake_suggestion_text_policy"}, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "workspace_id": "fake_workspace_id", "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "intents": [], "entities": [], "dialog_nodes": [], "counterexamples": [], "webhooks": []}"""
fake_response_IntentCollection_json = """{"intents": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Intent_json = """{"intent": "fake_intent", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_Intent_json = """{"intent": "fake_intent", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_Intent_json = """{"intent": "fake_intent", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_ExampleCollection_json = """{"examples": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Example_json = """{"text": "fake_text", "mentions": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Example_json = """{"text": "fake_text", "mentions": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Example_json = """{"text": "fake_text", "mentions": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_CounterexampleCollection_json = """{"counterexamples": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Counterexample_json = """{"text": "fake_text", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Counterexample_json = """{"text": "fake_text", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Counterexample_json = """{"text": "fake_text", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_EntityCollection_json = """{"entities": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Entity_json = """{"entity": "fake_entity", "description": "fake_description", "fuzzy_match": false, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "values": []}"""
fake_response_Entity_json = """{"entity": "fake_entity", "description": "fake_description", "fuzzy_match": false, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "values": []}"""
fake_response_Entity_json = """{"entity": "fake_entity", "description": "fake_description", "fuzzy_match": false, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "values": []}"""
fake_response_EntityMentionCollection_json = """{"examples": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_ValueCollection_json = """{"values": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Value_json = """{"value": "fake_value", "type": "fake_type", "synonyms": [], "patterns": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Value_json = """{"value": "fake_value", "type": "fake_type", "synonyms": [], "patterns": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Value_json = """{"value": "fake_value", "type": "fake_type", "synonyms": [], "patterns": [], "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_SynonymCollection_json = """{"synonyms": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_Synonym_json = """{"synonym": "fake_synonym", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Synonym_json = """{"synonym": "fake_synonym", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Synonym_json = """{"synonym": "fake_synonym", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_DialogNodeCollection_json = """{"dialog_nodes": [], "pagination": {"refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5, "matched": 7, "refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor"}}"""
fake_response_DialogNode_json = """{"dialog_node": "fake_dialog_node", "description": "fake_description", "conditions": "fake_conditions", "parent": "fake_parent", "previous_sibling": "fake_previous_sibling", "output": {"generic": [], "modifiers": {"overwrite": false}}, "next_step": {"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}, "title": "fake_title", "type": "fake_type", "event_name": "fake_event_name", "variable": "fake_variable", "actions": [], "digress_in": "fake_digress_in", "digress_out": "fake_digress_out", "digress_out_slots": "fake_digress_out_slots", "user_label": "fake_user_label", "disambiguation_opt_out": true, "disabled": true, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_DialogNode_json = """{"dialog_node": "fake_dialog_node", "description": "fake_description", "conditions": "fake_conditions", "parent": "fake_parent", "previous_sibling": "fake_previous_sibling", "output": {"generic": [], "modifiers": {"overwrite": false}}, "next_step": {"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}, "title": "fake_title", "type": "fake_type", "event_name": "fake_event_name", "variable": "fake_variable", "actions": [], "digress_in": "fake_digress_in", "digress_out": "fake_digress_out", "digress_out_slots": "fake_digress_out_slots", "user_label": "fake_user_label", "disambiguation_opt_out": true, "disabled": true, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_DialogNode_json = """{"dialog_node": "fake_dialog_node", "description": "fake_description", "conditions": "fake_conditions", "parent": "fake_parent", "previous_sibling": "fake_previous_sibling", "output": {"generic": [], "modifiers": {"overwrite": false}}, "next_step": {"behavior": "fake_behavior", "dialog_node": "fake_dialog_node", "selector": "fake_selector"}, "title": "fake_title", "type": "fake_type", "event_name": "fake_event_name", "variable": "fake_variable", "actions": [], "digress_in": "fake_digress_in", "digress_out": "fake_digress_out", "digress_out_slots": "fake_digress_out_slots", "user_label": "fake_user_label", "disambiguation_opt_out": true, "disabled": true, "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_LogCollection_json = """{"logs": [], "pagination": {"next_url": "fake_next_url", "matched": 7, "next_cursor": "fake_next_cursor"}}"""
fake_response_LogCollection_json = """{"logs": [], "pagination": {"next_url": "fake_next_url", "matched": 7, "next_cursor": "fake_next_cursor"}}"""
