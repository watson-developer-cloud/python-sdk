# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2021.
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
Unit Tests for AssistantV2
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_watson.assistant_v2 import *

version = 'testString'

_service = AssistantV2(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.assistant.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Sessions
##############################################################################
# region

class TestCreateSession():
    """
    Test Class for create_session
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
    def test_create_session_all_params(self):
        """
        create_session()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions')
        mock_response = '{"session_id": "session_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.create_session(
            assistant_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_session_value_error(self):
        """
        test_create_session_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions')
        mock_response = '{"session_id": "session_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_session(**req_copy)



class TestDeleteSession():
    """
    Test Class for delete_session
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
    def test_delete_session_all_params(self):
        """
        delete_session()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Invoke method
        response = _service.delete_session(
            assistant_id,
            session_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_session_value_error(self):
        """
        test_delete_session_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_session(**req_copy)



# endregion
##############################################################################
# End of Service: Sessions
##############################################################################

##############################################################################
# Start of Service: Message
##############################################################################
# region

class TestMessage():
    """
    Test Class for message
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
    def test_message_all_params(self):
        """
        message()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a MessageInputOptions model
        message_input_options_model = {}
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a dict representation of a MessageInput model
        message_input_model = {}
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        # Construct a dict representation of a MessageContextGlobal model
        message_context_global_model = {}
        message_context_global_model['system'] = message_context_global_system_model

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextSkill model
        message_context_skill_model = {}
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a MessageContext model
        message_context_model = {}
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = {}

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'
        input = message_input_model
        context = message_context_model
        user_id = 'testString'

        # Invoke method
        response = _service.message(
            assistant_id,
            session_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_model
        assert req_body['context'] == message_context_model
        assert req_body['user_id'] == 'testString'


    @responses.activate
    def test_message_required_params(self):
        """
        test_message_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Invoke method
        response = _service.message(
            assistant_id,
            session_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_message_value_error(self):
        """
        test_message_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/sessions/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'
        session_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message(**req_copy)



class TestMessageStateless():
    """
    Test Class for message_stateless
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
    def test_message_stateless_all_params(self):
        """
        message_stateless()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a RuntimeIntent model
        runtime_intent_model = {}
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        # Construct a dict representation of a CaptureGroup model
        capture_group_model = {}
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        # Construct a dict representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model = {}
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        # Construct a dict representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model = {}
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        # Construct a dict representation of a RuntimeEntityRole model
        runtime_entity_role_model = {}
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a dict representation of a RuntimeEntity model
        runtime_entity_model = {}
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        # Construct a dict representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model = {}
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a dict representation of a MessageInputOptionsStateless model
        message_input_options_stateless_model = {}
        message_input_options_stateless_model['restart'] = False
        message_input_options_stateless_model['alternate_intents'] = False
        message_input_options_stateless_model['spelling'] = message_input_options_spelling_model
        message_input_options_stateless_model['debug'] = False

        # Construct a dict representation of a MessageInputStateless model
        message_input_stateless_model = {}
        message_input_stateless_model['message_type'] = 'text'
        message_input_stateless_model['text'] = 'testString'
        message_input_stateless_model['intents'] = [runtime_intent_model]
        message_input_stateless_model['entities'] = [runtime_entity_model]
        message_input_stateless_model['suggestion_id'] = 'testString'
        message_input_stateless_model['options'] = message_input_options_stateless_model

        # Construct a dict representation of a MessageContextGlobalSystem model
        message_context_global_system_model = {}
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        # Construct a dict representation of a MessageContextGlobalStateless model
        message_context_global_stateless_model = {}
        message_context_global_stateless_model['system'] = message_context_global_system_model
        message_context_global_stateless_model['session_id'] = 'testString'

        # Construct a dict representation of a MessageContextSkillSystem model
        message_context_skill_system_model = {}
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a dict representation of a MessageContextSkill model
        message_context_skill_model = {}
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        # Construct a dict representation of a MessageContextStateless model
        message_context_stateless_model = {}
        message_context_stateless_model['global'] = message_context_global_stateless_model
        message_context_stateless_model['skills'] = {}

        # Set up parameter values
        assistant_id = 'testString'
        input = message_input_stateless_model
        context = message_context_stateless_model
        user_id = 'testString'

        # Invoke method
        response = _service.message_stateless(
            assistant_id,
            input=input,
            context=context,
            user_id=user_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_stateless_model
        assert req_body['context'] == message_context_stateless_model
        assert req_body['user_id'] == 'testString'


    @responses.activate
    def test_message_stateless_required_params(self):
        """
        test_message_stateless_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.message_stateless(
            assistant_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_message_stateless_value_error(self):
        """
        test_message_stateless_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/message')
        mock_response = '{"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message_stateless(**req_copy)



# endregion
##############################################################################
# End of Service: Message
##############################################################################

##############################################################################
# Start of Service: BulkClassify
##############################################################################
# region

class TestBulkClassify():
    """
    Test Class for bulk_classify
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
    def test_bulk_classify_all_params(self):
        """
        bulk_classify()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/skills/testString/workspace/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "intents": [{"intent": "intent", "confidence": 10}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a BulkClassifyUtterance model
        bulk_classify_utterance_model = {}
        bulk_classify_utterance_model['text'] = 'testString'

        # Set up parameter values
        skill_id = 'testString'
        input = [bulk_classify_utterance_model]

        # Invoke method
        response = _service.bulk_classify(
            skill_id,
            input=input,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == [bulk_classify_utterance_model]


    @responses.activate
    def test_bulk_classify_required_params(self):
        """
        test_bulk_classify_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/skills/testString/workspace/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "intents": [{"intent": "intent", "confidence": 10}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        skill_id = 'testString'

        # Invoke method
        response = _service.bulk_classify(
            skill_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_bulk_classify_value_error(self):
        """
        test_bulk_classify_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/skills/testString/workspace/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "intents": [{"intent": "intent", "confidence": 10}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        skill_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "skill_id": skill_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.bulk_classify(**req_copy)



# endregion
##############################################################################
# End of Service: BulkClassify
##############################################################################

##############################################################################
# Start of Service: Logs
##############################################################################
# region

class TestListLogs():
    """
    Test Class for list_logs
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
    def test_list_logs_all_params(self):
        """
        list_logs()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'
        sort = 'testString'
        filter = 'testString'
        page_limit = 38
        cursor = 'testString'

        # Invoke method
        response = _service.list_logs(
            assistant_id,
            sort=sort,
            filter=filter,
            page_limit=page_limit,
            cursor=cursor,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'sort={}'.format(sort) in query_string
        assert 'filter={}'.format(filter) in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'cursor={}'.format(cursor) in query_string


    @responses.activate
    def test_list_logs_required_params(self):
        """
        test_list_logs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'

        # Invoke method
        response = _service.list_logs(
            assistant_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_logs_value_error(self):
        """
        test_list_logs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v2/assistants/testString/logs')
        mock_response = '{"logs": [{"log_id": "log_id", "request": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "response": {"output": {"generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"message_type": "text", "text": "text", "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "suggestion_id": "suggestion_id", "options": {"restart": false, "alternate_intents": false, "spelling": {"suggestions": false, "auto_correct": true}, "debug": false, "return_context": false, "export": false}}}}], "channels": [{"channel": "channel"}]}], "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "debug": {"nodes_visited": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "message": "message", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "branch_exited": false, "branch_exited_reason": "completed"}, "user_defined": {"mapKey": "anyValue"}, "spelling": {"text": "text", "original_text": "original_text", "suggested_text": "suggested_text"}}, "context": {"global": {"system": {"timezone": "timezone", "user_id": "user_id", "turn_count": 10, "locale": "en-us", "reference_time": "reference_time", "session_start_time": "session_start_time", "state": "state"}, "session_id": "session_id"}, "skills": {"mapKey": {"user_defined": {"mapKey": {"anyKey": "anyValue"}}, "system": {"state": "state"}}}}, "user_id": "user_id"}, "assistant_id": "assistant_id", "session_id": "session_id", "skill_id": "skill_id", "snapshot": "snapshot", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "language": "language", "customer_id": "customer_id"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        assistant_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "assistant_id": assistant_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_logs(**req_copy)



# endregion
##############################################################################
# End of Service: Logs
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
        url = self.preprocess_url(_base_url + '/v2/user_data')
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
        url = self.preprocess_url(_base_url + '/v2/user_data')
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
class TestModel_AgentAvailabilityMessage():
    """
    Test Class for AgentAvailabilityMessage
    """

    def test_agent_availability_message_serialization(self):
        """
        Test serialization/deserialization for AgentAvailabilityMessage
        """

        # Construct a json representation of a AgentAvailabilityMessage model
        agent_availability_message_model_json = {}
        agent_availability_message_model_json['message'] = 'testString'

        # Construct a model instance of AgentAvailabilityMessage by calling from_dict on the json representation
        agent_availability_message_model = AgentAvailabilityMessage.from_dict(agent_availability_message_model_json)
        assert agent_availability_message_model != False

        # Construct a model instance of AgentAvailabilityMessage by calling from_dict on the json representation
        agent_availability_message_model_dict = AgentAvailabilityMessage.from_dict(agent_availability_message_model_json).__dict__
        agent_availability_message_model2 = AgentAvailabilityMessage(**agent_availability_message_model_dict)

        # Verify the model instances are equivalent
        assert agent_availability_message_model == agent_availability_message_model2

        # Convert model instance back to dict and verify no loss of data
        agent_availability_message_model_json2 = agent_availability_message_model.to_dict()
        assert agent_availability_message_model_json2 == agent_availability_message_model_json

class TestModel_BulkClassifyOutput():
    """
    Test Class for BulkClassifyOutput
    """

    def test_bulk_classify_output_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bulk_classify_utterance_model = {} # BulkClassifyUtterance
        bulk_classify_utterance_model['text'] = 'testString'

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        # Construct a json representation of a BulkClassifyOutput model
        bulk_classify_output_model_json = {}
        bulk_classify_output_model_json['input'] = bulk_classify_utterance_model
        bulk_classify_output_model_json['entities'] = [runtime_entity_model]
        bulk_classify_output_model_json['intents'] = [runtime_intent_model]

        # Construct a model instance of BulkClassifyOutput by calling from_dict on the json representation
        bulk_classify_output_model = BulkClassifyOutput.from_dict(bulk_classify_output_model_json)
        assert bulk_classify_output_model != False

        # Construct a model instance of BulkClassifyOutput by calling from_dict on the json representation
        bulk_classify_output_model_dict = BulkClassifyOutput.from_dict(bulk_classify_output_model_json).__dict__
        bulk_classify_output_model2 = BulkClassifyOutput(**bulk_classify_output_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_output_model == bulk_classify_output_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_output_model_json2 = bulk_classify_output_model.to_dict()
        assert bulk_classify_output_model_json2 == bulk_classify_output_model_json

class TestModel_BulkClassifyResponse():
    """
    Test Class for BulkClassifyResponse
    """

    def test_bulk_classify_response_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        bulk_classify_utterance_model = {} # BulkClassifyUtterance
        bulk_classify_utterance_model['text'] = 'testString'

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        bulk_classify_output_model = {} # BulkClassifyOutput
        bulk_classify_output_model['input'] = bulk_classify_utterance_model
        bulk_classify_output_model['entities'] = [runtime_entity_model]
        bulk_classify_output_model['intents'] = [runtime_intent_model]

        # Construct a json representation of a BulkClassifyResponse model
        bulk_classify_response_model_json = {}
        bulk_classify_response_model_json['output'] = [bulk_classify_output_model]

        # Construct a model instance of BulkClassifyResponse by calling from_dict on the json representation
        bulk_classify_response_model = BulkClassifyResponse.from_dict(bulk_classify_response_model_json)
        assert bulk_classify_response_model != False

        # Construct a model instance of BulkClassifyResponse by calling from_dict on the json representation
        bulk_classify_response_model_dict = BulkClassifyResponse.from_dict(bulk_classify_response_model_json).__dict__
        bulk_classify_response_model2 = BulkClassifyResponse(**bulk_classify_response_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_response_model == bulk_classify_response_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_response_model_json2 = bulk_classify_response_model.to_dict()
        assert bulk_classify_response_model_json2 == bulk_classify_response_model_json

class TestModel_BulkClassifyUtterance():
    """
    Test Class for BulkClassifyUtterance
    """

    def test_bulk_classify_utterance_serialization(self):
        """
        Test serialization/deserialization for BulkClassifyUtterance
        """

        # Construct a json representation of a BulkClassifyUtterance model
        bulk_classify_utterance_model_json = {}
        bulk_classify_utterance_model_json['text'] = 'testString'

        # Construct a model instance of BulkClassifyUtterance by calling from_dict on the json representation
        bulk_classify_utterance_model = BulkClassifyUtterance.from_dict(bulk_classify_utterance_model_json)
        assert bulk_classify_utterance_model != False

        # Construct a model instance of BulkClassifyUtterance by calling from_dict on the json representation
        bulk_classify_utterance_model_dict = BulkClassifyUtterance.from_dict(bulk_classify_utterance_model_json).__dict__
        bulk_classify_utterance_model2 = BulkClassifyUtterance(**bulk_classify_utterance_model_dict)

        # Verify the model instances are equivalent
        assert bulk_classify_utterance_model == bulk_classify_utterance_model2

        # Convert model instance back to dict and verify no loss of data
        bulk_classify_utterance_model_json2 = bulk_classify_utterance_model.to_dict()
        assert bulk_classify_utterance_model_json2 == bulk_classify_utterance_model_json

class TestModel_CaptureGroup():
    """
    Test Class for CaptureGroup
    """

    def test_capture_group_serialization(self):
        """
        Test serialization/deserialization for CaptureGroup
        """

        # Construct a json representation of a CaptureGroup model
        capture_group_model_json = {}
        capture_group_model_json['group'] = 'testString'
        capture_group_model_json['location'] = [38]

        # Construct a model instance of CaptureGroup by calling from_dict on the json representation
        capture_group_model = CaptureGroup.from_dict(capture_group_model_json)
        assert capture_group_model != False

        # Construct a model instance of CaptureGroup by calling from_dict on the json representation
        capture_group_model_dict = CaptureGroup.from_dict(capture_group_model_json).__dict__
        capture_group_model2 = CaptureGroup(**capture_group_model_dict)

        # Verify the model instances are equivalent
        assert capture_group_model == capture_group_model2

        # Convert model instance back to dict and verify no loss of data
        capture_group_model_json2 = capture_group_model.to_dict()
        assert capture_group_model_json2 == capture_group_model_json

class TestModel_ChannelTransferInfo():
    """
    Test Class for ChannelTransferInfo
    """

    def test_channel_transfer_info_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferInfo
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a json representation of a ChannelTransferInfo model
        channel_transfer_info_model_json = {}
        channel_transfer_info_model_json['target'] = channel_transfer_target_model

        # Construct a model instance of ChannelTransferInfo by calling from_dict on the json representation
        channel_transfer_info_model = ChannelTransferInfo.from_dict(channel_transfer_info_model_json)
        assert channel_transfer_info_model != False

        # Construct a model instance of ChannelTransferInfo by calling from_dict on the json representation
        channel_transfer_info_model_dict = ChannelTransferInfo.from_dict(channel_transfer_info_model_json).__dict__
        channel_transfer_info_model2 = ChannelTransferInfo(**channel_transfer_info_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_info_model == channel_transfer_info_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_info_model_json2 = channel_transfer_info_model.to_dict()
        assert channel_transfer_info_model_json2 == channel_transfer_info_model_json

class TestModel_ChannelTransferTarget():
    """
    Test Class for ChannelTransferTarget
    """

    def test_channel_transfer_target_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferTarget
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a json representation of a ChannelTransferTarget model
        channel_transfer_target_model_json = {}
        channel_transfer_target_model_json['chat'] = channel_transfer_target_chat_model

        # Construct a model instance of ChannelTransferTarget by calling from_dict on the json representation
        channel_transfer_target_model = ChannelTransferTarget.from_dict(channel_transfer_target_model_json)
        assert channel_transfer_target_model != False

        # Construct a model instance of ChannelTransferTarget by calling from_dict on the json representation
        channel_transfer_target_model_dict = ChannelTransferTarget.from_dict(channel_transfer_target_model_json).__dict__
        channel_transfer_target_model2 = ChannelTransferTarget(**channel_transfer_target_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_target_model == channel_transfer_target_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_target_model_json2 = channel_transfer_target_model.to_dict()
        assert channel_transfer_target_model_json2 == channel_transfer_target_model_json

class TestModel_ChannelTransferTargetChat():
    """
    Test Class for ChannelTransferTargetChat
    """

    def test_channel_transfer_target_chat_serialization(self):
        """
        Test serialization/deserialization for ChannelTransferTargetChat
        """

        # Construct a json representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model_json = {}
        channel_transfer_target_chat_model_json['url'] = 'testString'

        # Construct a model instance of ChannelTransferTargetChat by calling from_dict on the json representation
        channel_transfer_target_chat_model = ChannelTransferTargetChat.from_dict(channel_transfer_target_chat_model_json)
        assert channel_transfer_target_chat_model != False

        # Construct a model instance of ChannelTransferTargetChat by calling from_dict on the json representation
        channel_transfer_target_chat_model_dict = ChannelTransferTargetChat.from_dict(channel_transfer_target_chat_model_json).__dict__
        channel_transfer_target_chat_model2 = ChannelTransferTargetChat(**channel_transfer_target_chat_model_dict)

        # Verify the model instances are equivalent
        assert channel_transfer_target_chat_model == channel_transfer_target_chat_model2

        # Convert model instance back to dict and verify no loss of data
        channel_transfer_target_chat_model_json2 = channel_transfer_target_chat_model.to_dict()
        assert channel_transfer_target_chat_model_json2 == channel_transfer_target_chat_model_json

class TestModel_DialogLogMessage():
    """
    Test Class for DialogLogMessage
    """

    def test_dialog_log_message_serialization(self):
        """
        Test serialization/deserialization for DialogLogMessage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        # Construct a json representation of a DialogLogMessage model
        dialog_log_message_model_json = {}
        dialog_log_message_model_json['level'] = 'info'
        dialog_log_message_model_json['message'] = 'testString'
        dialog_log_message_model_json['code'] = 'testString'
        dialog_log_message_model_json['source'] = log_message_source_model

        # Construct a model instance of DialogLogMessage by calling from_dict on the json representation
        dialog_log_message_model = DialogLogMessage.from_dict(dialog_log_message_model_json)
        assert dialog_log_message_model != False

        # Construct a model instance of DialogLogMessage by calling from_dict on the json representation
        dialog_log_message_model_dict = DialogLogMessage.from_dict(dialog_log_message_model_json).__dict__
        dialog_log_message_model2 = DialogLogMessage(**dialog_log_message_model_dict)

        # Verify the model instances are equivalent
        assert dialog_log_message_model == dialog_log_message_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_log_message_model_json2 = dialog_log_message_model.to_dict()
        assert dialog_log_message_model_json2 == dialog_log_message_model_json

class TestModel_DialogNodeAction():
    """
    Test Class for DialogNodeAction
    """

    def test_dialog_node_action_serialization(self):
        """
        Test serialization/deserialization for DialogNodeAction
        """

        # Construct a json representation of a DialogNodeAction model
        dialog_node_action_model_json = {}
        dialog_node_action_model_json['name'] = 'testString'
        dialog_node_action_model_json['type'] = 'client'
        dialog_node_action_model_json['parameters'] = {}
        dialog_node_action_model_json['result_variable'] = 'testString'
        dialog_node_action_model_json['credentials'] = 'testString'

        # Construct a model instance of DialogNodeAction by calling from_dict on the json representation
        dialog_node_action_model = DialogNodeAction.from_dict(dialog_node_action_model_json)
        assert dialog_node_action_model != False

        # Construct a model instance of DialogNodeAction by calling from_dict on the json representation
        dialog_node_action_model_dict = DialogNodeAction.from_dict(dialog_node_action_model_json).__dict__
        dialog_node_action_model2 = DialogNodeAction(**dialog_node_action_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_action_model == dialog_node_action_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_action_model_json2 = dialog_node_action_model.to_dict()
        assert dialog_node_action_model_json2 == dialog_node_action_model_json

class TestModel_DialogNodeOutputConnectToAgentTransferInfo():
    """
    Test Class for DialogNodeOutputConnectToAgentTransferInfo
    """

    def test_dialog_node_output_connect_to_agent_transfer_info_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputConnectToAgentTransferInfo
        """

        # Construct a json representation of a DialogNodeOutputConnectToAgentTransferInfo model
        dialog_node_output_connect_to_agent_transfer_info_model_json = {}
        dialog_node_output_connect_to_agent_transfer_info_model_json['target'] = {}

        # Construct a model instance of DialogNodeOutputConnectToAgentTransferInfo by calling from_dict on the json representation
        dialog_node_output_connect_to_agent_transfer_info_model = DialogNodeOutputConnectToAgentTransferInfo.from_dict(dialog_node_output_connect_to_agent_transfer_info_model_json)
        assert dialog_node_output_connect_to_agent_transfer_info_model != False

        # Construct a model instance of DialogNodeOutputConnectToAgentTransferInfo by calling from_dict on the json representation
        dialog_node_output_connect_to_agent_transfer_info_model_dict = DialogNodeOutputConnectToAgentTransferInfo.from_dict(dialog_node_output_connect_to_agent_transfer_info_model_json).__dict__
        dialog_node_output_connect_to_agent_transfer_info_model2 = DialogNodeOutputConnectToAgentTransferInfo(**dialog_node_output_connect_to_agent_transfer_info_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_connect_to_agent_transfer_info_model == dialog_node_output_connect_to_agent_transfer_info_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_connect_to_agent_transfer_info_model_json2 = dialog_node_output_connect_to_agent_transfer_info_model.to_dict()
        assert dialog_node_output_connect_to_agent_transfer_info_model_json2 == dialog_node_output_connect_to_agent_transfer_info_model_json

class TestModel_DialogNodeOutputOptionsElement():
    """
    Test Class for DialogNodeOutputOptionsElement
    """

    def test_dialog_node_output_options_element_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputOptionsElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        # Construct a json representation of a DialogNodeOutputOptionsElement model
        dialog_node_output_options_element_model_json = {}
        dialog_node_output_options_element_model_json['label'] = 'testString'
        dialog_node_output_options_element_model_json['value'] = dialog_node_output_options_element_value_model

        # Construct a model instance of DialogNodeOutputOptionsElement by calling from_dict on the json representation
        dialog_node_output_options_element_model = DialogNodeOutputOptionsElement.from_dict(dialog_node_output_options_element_model_json)
        assert dialog_node_output_options_element_model != False

        # Construct a model instance of DialogNodeOutputOptionsElement by calling from_dict on the json representation
        dialog_node_output_options_element_model_dict = DialogNodeOutputOptionsElement.from_dict(dialog_node_output_options_element_model_json).__dict__
        dialog_node_output_options_element_model2 = DialogNodeOutputOptionsElement(**dialog_node_output_options_element_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_options_element_model == dialog_node_output_options_element_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_options_element_model_json2 = dialog_node_output_options_element_model.to_dict()
        assert dialog_node_output_options_element_model_json2 == dialog_node_output_options_element_model_json

class TestModel_DialogNodeOutputOptionsElementValue():
    """
    Test Class for DialogNodeOutputOptionsElementValue
    """

    def test_dialog_node_output_options_element_value_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputOptionsElementValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a DialogNodeOutputOptionsElementValue model
        dialog_node_output_options_element_value_model_json = {}
        dialog_node_output_options_element_value_model_json['input'] = message_input_model

        # Construct a model instance of DialogNodeOutputOptionsElementValue by calling from_dict on the json representation
        dialog_node_output_options_element_value_model = DialogNodeOutputOptionsElementValue.from_dict(dialog_node_output_options_element_value_model_json)
        assert dialog_node_output_options_element_value_model != False

        # Construct a model instance of DialogNodeOutputOptionsElementValue by calling from_dict on the json representation
        dialog_node_output_options_element_value_model_dict = DialogNodeOutputOptionsElementValue.from_dict(dialog_node_output_options_element_value_model_json).__dict__
        dialog_node_output_options_element_value_model2 = DialogNodeOutputOptionsElementValue(**dialog_node_output_options_element_value_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_options_element_value_model == dialog_node_output_options_element_value_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_options_element_value_model_json2 = dialog_node_output_options_element_value_model.to_dict()
        assert dialog_node_output_options_element_value_model_json2 == dialog_node_output_options_element_value_model_json

class TestModel_DialogNodesVisited():
    """
    Test Class for DialogNodesVisited
    """

    def test_dialog_nodes_visited_serialization(self):
        """
        Test serialization/deserialization for DialogNodesVisited
        """

        # Construct a json representation of a DialogNodesVisited model
        dialog_nodes_visited_model_json = {}
        dialog_nodes_visited_model_json['dialog_node'] = 'testString'
        dialog_nodes_visited_model_json['title'] = 'testString'
        dialog_nodes_visited_model_json['conditions'] = 'testString'

        # Construct a model instance of DialogNodesVisited by calling from_dict on the json representation
        dialog_nodes_visited_model = DialogNodesVisited.from_dict(dialog_nodes_visited_model_json)
        assert dialog_nodes_visited_model != False

        # Construct a model instance of DialogNodesVisited by calling from_dict on the json representation
        dialog_nodes_visited_model_dict = DialogNodesVisited.from_dict(dialog_nodes_visited_model_json).__dict__
        dialog_nodes_visited_model2 = DialogNodesVisited(**dialog_nodes_visited_model_dict)

        # Verify the model instances are equivalent
        assert dialog_nodes_visited_model == dialog_nodes_visited_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_nodes_visited_model_json2 = dialog_nodes_visited_model.to_dict()
        assert dialog_nodes_visited_model_json2 == dialog_nodes_visited_model_json

class TestModel_DialogSuggestion():
    """
    Test Class for DialogSuggestion
    """

    def test_dialog_suggestion_serialization(self):
        """
        Test serialization/deserialization for DialogSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_suggestion_value_model = {} # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model

        # Construct a json representation of a DialogSuggestion model
        dialog_suggestion_model_json = {}
        dialog_suggestion_model_json['label'] = 'testString'
        dialog_suggestion_model_json['value'] = dialog_suggestion_value_model
        dialog_suggestion_model_json['output'] = {}

        # Construct a model instance of DialogSuggestion by calling from_dict on the json representation
        dialog_suggestion_model = DialogSuggestion.from_dict(dialog_suggestion_model_json)
        assert dialog_suggestion_model != False

        # Construct a model instance of DialogSuggestion by calling from_dict on the json representation
        dialog_suggestion_model_dict = DialogSuggestion.from_dict(dialog_suggestion_model_json).__dict__
        dialog_suggestion_model2 = DialogSuggestion(**dialog_suggestion_model_dict)

        # Verify the model instances are equivalent
        assert dialog_suggestion_model == dialog_suggestion_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_suggestion_model_json2 = dialog_suggestion_model.to_dict()
        assert dialog_suggestion_model_json2 == dialog_suggestion_model_json

class TestModel_DialogSuggestionValue():
    """
    Test Class for DialogSuggestionValue
    """

    def test_dialog_suggestion_value_serialization(self):
        """
        Test serialization/deserialization for DialogSuggestionValue
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        # Construct a json representation of a DialogSuggestionValue model
        dialog_suggestion_value_model_json = {}
        dialog_suggestion_value_model_json['input'] = message_input_model

        # Construct a model instance of DialogSuggestionValue by calling from_dict on the json representation
        dialog_suggestion_value_model = DialogSuggestionValue.from_dict(dialog_suggestion_value_model_json)
        assert dialog_suggestion_value_model != False

        # Construct a model instance of DialogSuggestionValue by calling from_dict on the json representation
        dialog_suggestion_value_model_dict = DialogSuggestionValue.from_dict(dialog_suggestion_value_model_json).__dict__
        dialog_suggestion_value_model2 = DialogSuggestionValue(**dialog_suggestion_value_model_dict)

        # Verify the model instances are equivalent
        assert dialog_suggestion_value_model == dialog_suggestion_value_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_suggestion_value_model_json2 = dialog_suggestion_value_model.to_dict()
        assert dialog_suggestion_value_model_json2 == dialog_suggestion_value_model_json

class TestModel_Log():
    """
    Test Class for Log
    """

    def test_log_serialization(self):
        """
        Test serialization/deserialization for Log
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_model = {} # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model
        message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        message_context_model = {} # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = {}

        message_request_model = {} # MessageRequest
        message_request_model['input'] = message_input_model
        message_request_model['context'] = message_context_model
        message_request_model['user_id'] = 'testString'

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        message_output_debug_model = {} # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'

        message_output_spelling_model = {} # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {} # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {}
        message_output_model['spelling'] = message_output_spelling_model

        message_response_model = {} # MessageResponse
        message_response_model['output'] = message_output_model
        message_response_model['context'] = message_context_model
        message_response_model['user_id'] = 'testString'

        # Construct a json representation of a Log model
        log_model_json = {}
        log_model_json['log_id'] = 'testString'
        log_model_json['request'] = message_request_model
        log_model_json['response'] = message_response_model
        log_model_json['assistant_id'] = 'testString'
        log_model_json['session_id'] = 'testString'
        log_model_json['skill_id'] = 'testString'
        log_model_json['snapshot'] = 'testString'
        log_model_json['request_timestamp'] = 'testString'
        log_model_json['response_timestamp'] = 'testString'
        log_model_json['language'] = 'testString'
        log_model_json['customer_id'] = 'testString'

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model = Log.from_dict(log_model_json)
        assert log_model != False

        # Construct a model instance of Log by calling from_dict on the json representation
        log_model_dict = Log.from_dict(log_model_json).__dict__
        log_model2 = Log(**log_model_dict)

        # Verify the model instances are equivalent
        assert log_model == log_model2

        # Convert model instance back to dict and verify no loss of data
        log_model_json2 = log_model.to_dict()
        assert log_model_json2 == log_model_json

class TestModel_LogCollection():
    """
    Test Class for LogCollection
    """

    def test_log_collection_serialization(self):
        """
        Test serialization/deserialization for LogCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_model = {} # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model
        message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        message_context_model = {} # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = {}

        message_request_model = {} # MessageRequest
        message_request_model['input'] = message_input_model
        message_request_model['context'] = message_context_model
        message_request_model['user_id'] = 'testString'

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        message_output_debug_model = {} # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'

        message_output_spelling_model = {} # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {} # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {}
        message_output_model['spelling'] = message_output_spelling_model

        message_response_model = {} # MessageResponse
        message_response_model['output'] = message_output_model
        message_response_model['context'] = message_context_model
        message_response_model['user_id'] = 'testString'

        log_model = {} # Log
        log_model['log_id'] = 'testString'
        log_model['request'] = message_request_model
        log_model['response'] = message_response_model
        log_model['assistant_id'] = 'testString'
        log_model['session_id'] = 'testString'
        log_model['skill_id'] = 'testString'
        log_model['snapshot'] = 'testString'
        log_model['request_timestamp'] = 'testString'
        log_model['response_timestamp'] = 'testString'
        log_model['language'] = 'testString'
        log_model['customer_id'] = 'testString'

        log_pagination_model = {} # LogPagination
        log_pagination_model['next_url'] = 'testString'
        log_pagination_model['matched'] = 38
        log_pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a LogCollection model
        log_collection_model_json = {}
        log_collection_model_json['logs'] = [log_model]
        log_collection_model_json['pagination'] = log_pagination_model

        # Construct a model instance of LogCollection by calling from_dict on the json representation
        log_collection_model = LogCollection.from_dict(log_collection_model_json)
        assert log_collection_model != False

        # Construct a model instance of LogCollection by calling from_dict on the json representation
        log_collection_model_dict = LogCollection.from_dict(log_collection_model_json).__dict__
        log_collection_model2 = LogCollection(**log_collection_model_dict)

        # Verify the model instances are equivalent
        assert log_collection_model == log_collection_model2

        # Convert model instance back to dict and verify no loss of data
        log_collection_model_json2 = log_collection_model.to_dict()
        assert log_collection_model_json2 == log_collection_model_json

class TestModel_LogPagination():
    """
    Test Class for LogPagination
    """

    def test_log_pagination_serialization(self):
        """
        Test serialization/deserialization for LogPagination
        """

        # Construct a json representation of a LogPagination model
        log_pagination_model_json = {}
        log_pagination_model_json['next_url'] = 'testString'
        log_pagination_model_json['matched'] = 38
        log_pagination_model_json['next_cursor'] = 'testString'

        # Construct a model instance of LogPagination by calling from_dict on the json representation
        log_pagination_model = LogPagination.from_dict(log_pagination_model_json)
        assert log_pagination_model != False

        # Construct a model instance of LogPagination by calling from_dict on the json representation
        log_pagination_model_dict = LogPagination.from_dict(log_pagination_model_json).__dict__
        log_pagination_model2 = LogPagination(**log_pagination_model_dict)

        # Verify the model instances are equivalent
        assert log_pagination_model == log_pagination_model2

        # Convert model instance back to dict and verify no loss of data
        log_pagination_model_json2 = log_pagination_model.to_dict()
        assert log_pagination_model_json2 == log_pagination_model_json

class TestModel_MessageContext():
    """
    Test Class for MessageContext
    """

    def test_message_context_serialization(self):
        """
        Test serialization/deserialization for MessageContext
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_model = {} # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model
        message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        # Construct a json representation of a MessageContext model
        message_context_model_json = {}
        message_context_model_json['global'] = message_context_global_model
        message_context_model_json['skills'] = {}

        # Construct a model instance of MessageContext by calling from_dict on the json representation
        message_context_model = MessageContext.from_dict(message_context_model_json)
        assert message_context_model != False

        # Construct a model instance of MessageContext by calling from_dict on the json representation
        message_context_model_dict = MessageContext.from_dict(message_context_model_json).__dict__
        message_context_model2 = MessageContext(**message_context_model_dict)

        # Verify the model instances are equivalent
        assert message_context_model == message_context_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_model_json2 = message_context_model.to_dict()
        assert message_context_model_json2 == message_context_model_json

class TestModel_MessageContextGlobal():
    """
    Test Class for MessageContextGlobal
    """

    def test_message_context_global_serialization(self):
        """
        Test serialization/deserialization for MessageContextGlobal
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        # Construct a json representation of a MessageContextGlobal model
        message_context_global_model_json = {}
        message_context_global_model_json['system'] = message_context_global_system_model
        message_context_global_model_json['session_id'] = 'testString'

        # Construct a model instance of MessageContextGlobal by calling from_dict on the json representation
        message_context_global_model = MessageContextGlobal.from_dict(message_context_global_model_json)
        assert message_context_global_model != False

        # Construct a model instance of MessageContextGlobal by calling from_dict on the json representation
        message_context_global_model_dict = MessageContextGlobal.from_dict(message_context_global_model_json).__dict__
        message_context_global_model2 = MessageContextGlobal(**message_context_global_model_dict)

        # Verify the model instances are equivalent
        assert message_context_global_model == message_context_global_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_global_model_json2 = message_context_global_model.to_dict()
        assert message_context_global_model_json2 == message_context_global_model_json

class TestModel_MessageContextGlobalStateless():
    """
    Test Class for MessageContextGlobalStateless
    """

    def test_message_context_global_stateless_serialization(self):
        """
        Test serialization/deserialization for MessageContextGlobalStateless
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        # Construct a json representation of a MessageContextGlobalStateless model
        message_context_global_stateless_model_json = {}
        message_context_global_stateless_model_json['system'] = message_context_global_system_model
        message_context_global_stateless_model_json['session_id'] = 'testString'

        # Construct a model instance of MessageContextGlobalStateless by calling from_dict on the json representation
        message_context_global_stateless_model = MessageContextGlobalStateless.from_dict(message_context_global_stateless_model_json)
        assert message_context_global_stateless_model != False

        # Construct a model instance of MessageContextGlobalStateless by calling from_dict on the json representation
        message_context_global_stateless_model_dict = MessageContextGlobalStateless.from_dict(message_context_global_stateless_model_json).__dict__
        message_context_global_stateless_model2 = MessageContextGlobalStateless(**message_context_global_stateless_model_dict)

        # Verify the model instances are equivalent
        assert message_context_global_stateless_model == message_context_global_stateless_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_global_stateless_model_json2 = message_context_global_stateless_model.to_dict()
        assert message_context_global_stateless_model_json2 == message_context_global_stateless_model_json

class TestModel_MessageContextGlobalSystem():
    """
    Test Class for MessageContextGlobalSystem
    """

    def test_message_context_global_system_serialization(self):
        """
        Test serialization/deserialization for MessageContextGlobalSystem
        """

        # Construct a json representation of a MessageContextGlobalSystem model
        message_context_global_system_model_json = {}
        message_context_global_system_model_json['timezone'] = 'testString'
        message_context_global_system_model_json['user_id'] = 'testString'
        message_context_global_system_model_json['turn_count'] = 38
        message_context_global_system_model_json['locale'] = 'en-us'
        message_context_global_system_model_json['reference_time'] = 'testString'
        message_context_global_system_model_json['session_start_time'] = 'testString'
        message_context_global_system_model_json['state'] = 'testString'

        # Construct a model instance of MessageContextGlobalSystem by calling from_dict on the json representation
        message_context_global_system_model = MessageContextGlobalSystem.from_dict(message_context_global_system_model_json)
        assert message_context_global_system_model != False

        # Construct a model instance of MessageContextGlobalSystem by calling from_dict on the json representation
        message_context_global_system_model_dict = MessageContextGlobalSystem.from_dict(message_context_global_system_model_json).__dict__
        message_context_global_system_model2 = MessageContextGlobalSystem(**message_context_global_system_model_dict)

        # Verify the model instances are equivalent
        assert message_context_global_system_model == message_context_global_system_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_global_system_model_json2 = message_context_global_system_model.to_dict()
        assert message_context_global_system_model_json2 == message_context_global_system_model_json

class TestModel_MessageContextSkill():
    """
    Test Class for MessageContextSkill
    """

    def test_message_context_skill_serialization(self):
        """
        Test serialization/deserialization for MessageContextSkill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        # Construct a json representation of a MessageContextSkill model
        message_context_skill_model_json = {}
        message_context_skill_model_json['user_defined'] = {}
        message_context_skill_model_json['system'] = message_context_skill_system_model

        # Construct a model instance of MessageContextSkill by calling from_dict on the json representation
        message_context_skill_model = MessageContextSkill.from_dict(message_context_skill_model_json)
        assert message_context_skill_model != False

        # Construct a model instance of MessageContextSkill by calling from_dict on the json representation
        message_context_skill_model_dict = MessageContextSkill.from_dict(message_context_skill_model_json).__dict__
        message_context_skill_model2 = MessageContextSkill(**message_context_skill_model_dict)

        # Verify the model instances are equivalent
        assert message_context_skill_model == message_context_skill_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_skill_model_json2 = message_context_skill_model.to_dict()
        assert message_context_skill_model_json2 == message_context_skill_model_json

class TestModel_MessageContextSkillSystem():
    """
    Test Class for MessageContextSkillSystem
    """

    def test_message_context_skill_system_serialization(self):
        """
        Test serialization/deserialization for MessageContextSkillSystem
        """

        # Construct a json representation of a MessageContextSkillSystem model
        message_context_skill_system_model_json = {}
        message_context_skill_system_model_json['state'] = 'testString'
        message_context_skill_system_model_json['foo'] = 'testString'

        # Construct a model instance of MessageContextSkillSystem by calling from_dict on the json representation
        message_context_skill_system_model = MessageContextSkillSystem.from_dict(message_context_skill_system_model_json)
        assert message_context_skill_system_model != False

        # Construct a model instance of MessageContextSkillSystem by calling from_dict on the json representation
        message_context_skill_system_model_dict = MessageContextSkillSystem.from_dict(message_context_skill_system_model_json).__dict__
        message_context_skill_system_model2 = MessageContextSkillSystem(**message_context_skill_system_model_dict)

        # Verify the model instances are equivalent
        assert message_context_skill_system_model == message_context_skill_system_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_skill_system_model_json2 = message_context_skill_system_model.to_dict()
        assert message_context_skill_system_model_json2 == message_context_skill_system_model_json

        # Test get_properties and set_properties methods.
        message_context_skill_system_model.set_properties({})
        actual_dict = message_context_skill_system_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        message_context_skill_system_model.set_properties(expected_dict)
        actual_dict = message_context_skill_system_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_MessageContextStateless():
    """
    Test Class for MessageContextStateless
    """

    def test_message_context_stateless_serialization(self):
        """
        Test serialization/deserialization for MessageContextStateless
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_stateless_model = {} # MessageContextGlobalStateless
        message_context_global_stateless_model['system'] = message_context_global_system_model
        message_context_global_stateless_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        # Construct a json representation of a MessageContextStateless model
        message_context_stateless_model_json = {}
        message_context_stateless_model_json['global'] = message_context_global_stateless_model
        message_context_stateless_model_json['skills'] = {}

        # Construct a model instance of MessageContextStateless by calling from_dict on the json representation
        message_context_stateless_model = MessageContextStateless.from_dict(message_context_stateless_model_json)
        assert message_context_stateless_model != False

        # Construct a model instance of MessageContextStateless by calling from_dict on the json representation
        message_context_stateless_model_dict = MessageContextStateless.from_dict(message_context_stateless_model_json).__dict__
        message_context_stateless_model2 = MessageContextStateless(**message_context_stateless_model_dict)

        # Verify the model instances are equivalent
        assert message_context_stateless_model == message_context_stateless_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_stateless_model_json2 = message_context_stateless_model.to_dict()
        assert message_context_stateless_model_json2 == message_context_stateless_model_json

class TestModel_MessageInput():
    """
    Test Class for MessageInput
    """

    def test_message_input_serialization(self):
        """
        Test serialization/deserialization for MessageInput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        # Construct a json representation of a MessageInput model
        message_input_model_json = {}
        message_input_model_json['message_type'] = 'text'
        message_input_model_json['text'] = 'testString'
        message_input_model_json['intents'] = [runtime_intent_model]
        message_input_model_json['entities'] = [runtime_entity_model]
        message_input_model_json['suggestion_id'] = 'testString'
        message_input_model_json['options'] = message_input_options_model

        # Construct a model instance of MessageInput by calling from_dict on the json representation
        message_input_model = MessageInput.from_dict(message_input_model_json)
        assert message_input_model != False

        # Construct a model instance of MessageInput by calling from_dict on the json representation
        message_input_model_dict = MessageInput.from_dict(message_input_model_json).__dict__
        message_input_model2 = MessageInput(**message_input_model_dict)

        # Verify the model instances are equivalent
        assert message_input_model == message_input_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_model_json2 = message_input_model.to_dict()
        assert message_input_model_json2 == message_input_model_json

class TestModel_MessageInputOptions():
    """
    Test Class for MessageInputOptions
    """

    def test_message_input_options_serialization(self):
        """
        Test serialization/deserialization for MessageInputOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a json representation of a MessageInputOptions model
        message_input_options_model_json = {}
        message_input_options_model_json['restart'] = False
        message_input_options_model_json['alternate_intents'] = False
        message_input_options_model_json['spelling'] = message_input_options_spelling_model
        message_input_options_model_json['debug'] = False
        message_input_options_model_json['return_context'] = False
        message_input_options_model_json['export'] = False

        # Construct a model instance of MessageInputOptions by calling from_dict on the json representation
        message_input_options_model = MessageInputOptions.from_dict(message_input_options_model_json)
        assert message_input_options_model != False

        # Construct a model instance of MessageInputOptions by calling from_dict on the json representation
        message_input_options_model_dict = MessageInputOptions.from_dict(message_input_options_model_json).__dict__
        message_input_options_model2 = MessageInputOptions(**message_input_options_model_dict)

        # Verify the model instances are equivalent
        assert message_input_options_model == message_input_options_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_options_model_json2 = message_input_options_model.to_dict()
        assert message_input_options_model_json2 == message_input_options_model_json

class TestModel_MessageInputOptionsSpelling():
    """
    Test Class for MessageInputOptionsSpelling
    """

    def test_message_input_options_spelling_serialization(self):
        """
        Test serialization/deserialization for MessageInputOptionsSpelling
        """

        # Construct a json representation of a MessageInputOptionsSpelling model
        message_input_options_spelling_model_json = {}
        message_input_options_spelling_model_json['suggestions'] = True
        message_input_options_spelling_model_json['auto_correct'] = True

        # Construct a model instance of MessageInputOptionsSpelling by calling from_dict on the json representation
        message_input_options_spelling_model = MessageInputOptionsSpelling.from_dict(message_input_options_spelling_model_json)
        assert message_input_options_spelling_model != False

        # Construct a model instance of MessageInputOptionsSpelling by calling from_dict on the json representation
        message_input_options_spelling_model_dict = MessageInputOptionsSpelling.from_dict(message_input_options_spelling_model_json).__dict__
        message_input_options_spelling_model2 = MessageInputOptionsSpelling(**message_input_options_spelling_model_dict)

        # Verify the model instances are equivalent
        assert message_input_options_spelling_model == message_input_options_spelling_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_options_spelling_model_json2 = message_input_options_spelling_model.to_dict()
        assert message_input_options_spelling_model_json2 == message_input_options_spelling_model_json

class TestModel_MessageInputOptionsStateless():
    """
    Test Class for MessageInputOptionsStateless
    """

    def test_message_input_options_stateless_serialization(self):
        """
        Test serialization/deserialization for MessageInputOptionsStateless
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        # Construct a json representation of a MessageInputOptionsStateless model
        message_input_options_stateless_model_json = {}
        message_input_options_stateless_model_json['restart'] = False
        message_input_options_stateless_model_json['alternate_intents'] = False
        message_input_options_stateless_model_json['spelling'] = message_input_options_spelling_model
        message_input_options_stateless_model_json['debug'] = False

        # Construct a model instance of MessageInputOptionsStateless by calling from_dict on the json representation
        message_input_options_stateless_model = MessageInputOptionsStateless.from_dict(message_input_options_stateless_model_json)
        assert message_input_options_stateless_model != False

        # Construct a model instance of MessageInputOptionsStateless by calling from_dict on the json representation
        message_input_options_stateless_model_dict = MessageInputOptionsStateless.from_dict(message_input_options_stateless_model_json).__dict__
        message_input_options_stateless_model2 = MessageInputOptionsStateless(**message_input_options_stateless_model_dict)

        # Verify the model instances are equivalent
        assert message_input_options_stateless_model == message_input_options_stateless_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_options_stateless_model_json2 = message_input_options_stateless_model.to_dict()
        assert message_input_options_stateless_model_json2 == message_input_options_stateless_model_json

class TestModel_MessageInputStateless():
    """
    Test Class for MessageInputStateless
    """

    def test_message_input_stateless_serialization(self):
        """
        Test serialization/deserialization for MessageInputStateless
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_stateless_model = {} # MessageInputOptionsStateless
        message_input_options_stateless_model['restart'] = False
        message_input_options_stateless_model['alternate_intents'] = False
        message_input_options_stateless_model['spelling'] = message_input_options_spelling_model
        message_input_options_stateless_model['debug'] = False

        # Construct a json representation of a MessageInputStateless model
        message_input_stateless_model_json = {}
        message_input_stateless_model_json['message_type'] = 'text'
        message_input_stateless_model_json['text'] = 'testString'
        message_input_stateless_model_json['intents'] = [runtime_intent_model]
        message_input_stateless_model_json['entities'] = [runtime_entity_model]
        message_input_stateless_model_json['suggestion_id'] = 'testString'
        message_input_stateless_model_json['options'] = message_input_options_stateless_model

        # Construct a model instance of MessageInputStateless by calling from_dict on the json representation
        message_input_stateless_model = MessageInputStateless.from_dict(message_input_stateless_model_json)
        assert message_input_stateless_model != False

        # Construct a model instance of MessageInputStateless by calling from_dict on the json representation
        message_input_stateless_model_dict = MessageInputStateless.from_dict(message_input_stateless_model_json).__dict__
        message_input_stateless_model2 = MessageInputStateless(**message_input_stateless_model_dict)

        # Verify the model instances are equivalent
        assert message_input_stateless_model == message_input_stateless_model2

        # Convert model instance back to dict and verify no loss of data
        message_input_stateless_model_json2 = message_input_stateless_model.to_dict()
        assert message_input_stateless_model_json2 == message_input_stateless_model_json

class TestModel_MessageOutput():
    """
    Test Class for MessageOutput
    """

    def test_message_output_serialization(self):
        """
        Test serialization/deserialization for MessageOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        message_output_debug_model = {} # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'

        message_output_spelling_model = {} # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        # Construct a json representation of a MessageOutput model
        message_output_model_json = {}
        message_output_model_json['generic'] = [runtime_response_generic_model]
        message_output_model_json['intents'] = [runtime_intent_model]
        message_output_model_json['entities'] = [runtime_entity_model]
        message_output_model_json['actions'] = [dialog_node_action_model]
        message_output_model_json['debug'] = message_output_debug_model
        message_output_model_json['user_defined'] = {}
        message_output_model_json['spelling'] = message_output_spelling_model

        # Construct a model instance of MessageOutput by calling from_dict on the json representation
        message_output_model = MessageOutput.from_dict(message_output_model_json)
        assert message_output_model != False

        # Construct a model instance of MessageOutput by calling from_dict on the json representation
        message_output_model_dict = MessageOutput.from_dict(message_output_model_json).__dict__
        message_output_model2 = MessageOutput(**message_output_model_dict)

        # Verify the model instances are equivalent
        assert message_output_model == message_output_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_model_json2 = message_output_model.to_dict()
        assert message_output_model_json2 == message_output_model_json

class TestModel_MessageOutputDebug():
    """
    Test Class for MessageOutputDebug
    """

    def test_message_output_debug_serialization(self):
        """
        Test serialization/deserialization for MessageOutputDebug
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        # Construct a json representation of a MessageOutputDebug model
        message_output_debug_model_json = {}
        message_output_debug_model_json['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model_json['log_messages'] = [dialog_log_message_model]
        message_output_debug_model_json['branch_exited'] = True
        message_output_debug_model_json['branch_exited_reason'] = 'completed'

        # Construct a model instance of MessageOutputDebug by calling from_dict on the json representation
        message_output_debug_model = MessageOutputDebug.from_dict(message_output_debug_model_json)
        assert message_output_debug_model != False

        # Construct a model instance of MessageOutputDebug by calling from_dict on the json representation
        message_output_debug_model_dict = MessageOutputDebug.from_dict(message_output_debug_model_json).__dict__
        message_output_debug_model2 = MessageOutputDebug(**message_output_debug_model_dict)

        # Verify the model instances are equivalent
        assert message_output_debug_model == message_output_debug_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_debug_model_json2 = message_output_debug_model.to_dict()
        assert message_output_debug_model_json2 == message_output_debug_model_json

class TestModel_MessageOutputSpelling():
    """
    Test Class for MessageOutputSpelling
    """

    def test_message_output_spelling_serialization(self):
        """
        Test serialization/deserialization for MessageOutputSpelling
        """

        # Construct a json representation of a MessageOutputSpelling model
        message_output_spelling_model_json = {}
        message_output_spelling_model_json['text'] = 'testString'
        message_output_spelling_model_json['original_text'] = 'testString'
        message_output_spelling_model_json['suggested_text'] = 'testString'

        # Construct a model instance of MessageOutputSpelling by calling from_dict on the json representation
        message_output_spelling_model = MessageOutputSpelling.from_dict(message_output_spelling_model_json)
        assert message_output_spelling_model != False

        # Construct a model instance of MessageOutputSpelling by calling from_dict on the json representation
        message_output_spelling_model_dict = MessageOutputSpelling.from_dict(message_output_spelling_model_json).__dict__
        message_output_spelling_model2 = MessageOutputSpelling(**message_output_spelling_model_dict)

        # Verify the model instances are equivalent
        assert message_output_spelling_model == message_output_spelling_model2

        # Convert model instance back to dict and verify no loss of data
        message_output_spelling_model_json2 = message_output_spelling_model.to_dict()
        assert message_output_spelling_model_json2 == message_output_spelling_model_json

class TestModel_MessageRequest():
    """
    Test Class for MessageRequest
    """

    def test_message_request_serialization(self):
        """
        Test serialization/deserialization for MessageRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = True
        message_input_options_model['export'] = True

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'Hello'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'my_user_id'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_model = {} # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model
        message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        message_context_model = {} # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = {}

        # Construct a json representation of a MessageRequest model
        message_request_model_json = {}
        message_request_model_json['input'] = message_input_model
        message_request_model_json['context'] = message_context_model
        message_request_model_json['user_id'] = 'testString'

        # Construct a model instance of MessageRequest by calling from_dict on the json representation
        message_request_model = MessageRequest.from_dict(message_request_model_json)
        assert message_request_model != False

        # Construct a model instance of MessageRequest by calling from_dict on the json representation
        message_request_model_dict = MessageRequest.from_dict(message_request_model_json).__dict__
        message_request_model2 = MessageRequest(**message_request_model_dict)

        # Verify the model instances are equivalent
        assert message_request_model == message_request_model2

        # Convert model instance back to dict and verify no loss of data
        message_request_model_json2 = message_request_model.to_dict()
        assert message_request_model_json2 == message_request_model_json

class TestModel_MessageResponse():
    """
    Test Class for MessageResponse
    """

    def test_message_response_serialization(self):
        """
        Test serialization/deserialization for MessageResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        message_output_debug_model = {} # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'

        message_output_spelling_model = {} # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {} # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {}
        message_output_model['spelling'] = message_output_spelling_model

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_model = {} # MessageContextGlobal
        message_context_global_model['system'] = message_context_global_system_model
        message_context_global_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        message_context_model = {} # MessageContext
        message_context_model['global'] = message_context_global_model
        message_context_model['skills'] = {}

        # Construct a json representation of a MessageResponse model
        message_response_model_json = {}
        message_response_model_json['output'] = message_output_model
        message_response_model_json['context'] = message_context_model
        message_response_model_json['user_id'] = 'testString'

        # Construct a model instance of MessageResponse by calling from_dict on the json representation
        message_response_model = MessageResponse.from_dict(message_response_model_json)
        assert message_response_model != False

        # Construct a model instance of MessageResponse by calling from_dict on the json representation
        message_response_model_dict = MessageResponse.from_dict(message_response_model_json).__dict__
        message_response_model2 = MessageResponse(**message_response_model_dict)

        # Verify the model instances are equivalent
        assert message_response_model == message_response_model2

        # Convert model instance back to dict and verify no loss of data
        message_response_model_json2 = message_response_model.to_dict()
        assert message_response_model_json2 == message_response_model_json

class TestModel_MessageResponseStateless():
    """
    Test Class for MessageResponseStateless
    """

    def test_message_response_stateless_serialization(self):
        """
        Test serialization/deserialization for MessageResponseStateless
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_nodes_visited_model = {} # DialogNodesVisited
        dialog_nodes_visited_model['dialog_node'] = 'testString'
        dialog_nodes_visited_model['title'] = 'testString'
        dialog_nodes_visited_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSourceDialogNode
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        dialog_log_message_model = {} # DialogLogMessage
        dialog_log_message_model['level'] = 'info'
        dialog_log_message_model['message'] = 'testString'
        dialog_log_message_model['code'] = 'testString'
        dialog_log_message_model['source'] = log_message_source_model

        message_output_debug_model = {} # MessageOutputDebug
        message_output_debug_model['nodes_visited'] = [dialog_nodes_visited_model]
        message_output_debug_model['log_messages'] = [dialog_log_message_model]
        message_output_debug_model['branch_exited'] = True
        message_output_debug_model['branch_exited_reason'] = 'completed'

        message_output_spelling_model = {} # MessageOutputSpelling
        message_output_spelling_model['text'] = 'testString'
        message_output_spelling_model['original_text'] = 'testString'
        message_output_spelling_model['suggested_text'] = 'testString'

        message_output_model = {} # MessageOutput
        message_output_model['generic'] = [runtime_response_generic_model]
        message_output_model['intents'] = [runtime_intent_model]
        message_output_model['entities'] = [runtime_entity_model]
        message_output_model['actions'] = [dialog_node_action_model]
        message_output_model['debug'] = message_output_debug_model
        message_output_model['user_defined'] = {}
        message_output_model['spelling'] = message_output_spelling_model

        message_context_global_system_model = {} # MessageContextGlobalSystem
        message_context_global_system_model['timezone'] = 'testString'
        message_context_global_system_model['user_id'] = 'testString'
        message_context_global_system_model['turn_count'] = 38
        message_context_global_system_model['locale'] = 'en-us'
        message_context_global_system_model['reference_time'] = 'testString'
        message_context_global_system_model['session_start_time'] = 'testString'
        message_context_global_system_model['state'] = 'testString'

        message_context_global_stateless_model = {} # MessageContextGlobalStateless
        message_context_global_stateless_model['system'] = message_context_global_system_model
        message_context_global_stateless_model['session_id'] = 'testString'

        message_context_skill_system_model = {} # MessageContextSkillSystem
        message_context_skill_system_model['state'] = 'testString'
        message_context_skill_system_model['foo'] = 'testString'

        message_context_skill_model = {} # MessageContextSkill
        message_context_skill_model['user_defined'] = {}
        message_context_skill_model['system'] = message_context_skill_system_model

        message_context_stateless_model = {} # MessageContextStateless
        message_context_stateless_model['global'] = message_context_global_stateless_model
        message_context_stateless_model['skills'] = {}

        # Construct a json representation of a MessageResponseStateless model
        message_response_stateless_model_json = {}
        message_response_stateless_model_json['output'] = message_output_model
        message_response_stateless_model_json['context'] = message_context_stateless_model
        message_response_stateless_model_json['user_id'] = 'testString'

        # Construct a model instance of MessageResponseStateless by calling from_dict on the json representation
        message_response_stateless_model = MessageResponseStateless.from_dict(message_response_stateless_model_json)
        assert message_response_stateless_model != False

        # Construct a model instance of MessageResponseStateless by calling from_dict on the json representation
        message_response_stateless_model_dict = MessageResponseStateless.from_dict(message_response_stateless_model_json).__dict__
        message_response_stateless_model2 = MessageResponseStateless(**message_response_stateless_model_dict)

        # Verify the model instances are equivalent
        assert message_response_stateless_model == message_response_stateless_model2

        # Convert model instance back to dict and verify no loss of data
        message_response_stateless_model_json2 = message_response_stateless_model.to_dict()
        assert message_response_stateless_model_json2 == message_response_stateless_model_json

class TestModel_ResponseGenericChannel():
    """
    Test Class for ResponseGenericChannel
    """

    def test_response_generic_channel_serialization(self):
        """
        Test serialization/deserialization for ResponseGenericChannel
        """

        # Construct a json representation of a ResponseGenericChannel model
        response_generic_channel_model_json = {}
        response_generic_channel_model_json['channel'] = 'testString'

        # Construct a model instance of ResponseGenericChannel by calling from_dict on the json representation
        response_generic_channel_model = ResponseGenericChannel.from_dict(response_generic_channel_model_json)
        assert response_generic_channel_model != False

        # Construct a model instance of ResponseGenericChannel by calling from_dict on the json representation
        response_generic_channel_model_dict = ResponseGenericChannel.from_dict(response_generic_channel_model_json).__dict__
        response_generic_channel_model2 = ResponseGenericChannel(**response_generic_channel_model_dict)

        # Verify the model instances are equivalent
        assert response_generic_channel_model == response_generic_channel_model2

        # Convert model instance back to dict and verify no loss of data
        response_generic_channel_model_json2 = response_generic_channel_model.to_dict()
        assert response_generic_channel_model_json2 == response_generic_channel_model_json

class TestModel_RuntimeEntity():
    """
    Test Class for RuntimeEntity
    """

    def test_runtime_entity_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        # Construct a json representation of a RuntimeEntity model
        runtime_entity_model_json = {}
        runtime_entity_model_json['entity'] = 'testString'
        runtime_entity_model_json['location'] = [38]
        runtime_entity_model_json['value'] = 'testString'
        runtime_entity_model_json['confidence'] = 72.5
        runtime_entity_model_json['metadata'] = {}
        runtime_entity_model_json['groups'] = [capture_group_model]
        runtime_entity_model_json['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model_json['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model_json['role'] = runtime_entity_role_model

        # Construct a model instance of RuntimeEntity by calling from_dict on the json representation
        runtime_entity_model = RuntimeEntity.from_dict(runtime_entity_model_json)
        assert runtime_entity_model != False

        # Construct a model instance of RuntimeEntity by calling from_dict on the json representation
        runtime_entity_model_dict = RuntimeEntity.from_dict(runtime_entity_model_json).__dict__
        runtime_entity_model2 = RuntimeEntity(**runtime_entity_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_model == runtime_entity_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_model_json2 = runtime_entity_model.to_dict()
        assert runtime_entity_model_json2 == runtime_entity_model_json

class TestModel_RuntimeEntityAlternative():
    """
    Test Class for RuntimeEntityAlternative
    """

    def test_runtime_entity_alternative_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityAlternative
        """

        # Construct a json representation of a RuntimeEntityAlternative model
        runtime_entity_alternative_model_json = {}
        runtime_entity_alternative_model_json['value'] = 'testString'
        runtime_entity_alternative_model_json['confidence'] = 72.5

        # Construct a model instance of RuntimeEntityAlternative by calling from_dict on the json representation
        runtime_entity_alternative_model = RuntimeEntityAlternative.from_dict(runtime_entity_alternative_model_json)
        assert runtime_entity_alternative_model != False

        # Construct a model instance of RuntimeEntityAlternative by calling from_dict on the json representation
        runtime_entity_alternative_model_dict = RuntimeEntityAlternative.from_dict(runtime_entity_alternative_model_json).__dict__
        runtime_entity_alternative_model2 = RuntimeEntityAlternative(**runtime_entity_alternative_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_alternative_model == runtime_entity_alternative_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_alternative_model_json2 = runtime_entity_alternative_model.to_dict()
        assert runtime_entity_alternative_model_json2 == runtime_entity_alternative_model_json

class TestModel_RuntimeEntityInterpretation():
    """
    Test Class for RuntimeEntityInterpretation
    """

    def test_runtime_entity_interpretation_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityInterpretation
        """

        # Construct a json representation of a RuntimeEntityInterpretation model
        runtime_entity_interpretation_model_json = {}
        runtime_entity_interpretation_model_json['calendar_type'] = 'testString'
        runtime_entity_interpretation_model_json['datetime_link'] = 'testString'
        runtime_entity_interpretation_model_json['festival'] = 'testString'
        runtime_entity_interpretation_model_json['granularity'] = 'day'
        runtime_entity_interpretation_model_json['range_link'] = 'testString'
        runtime_entity_interpretation_model_json['range_modifier'] = 'testString'
        runtime_entity_interpretation_model_json['relative_day'] = 72.5
        runtime_entity_interpretation_model_json['relative_month'] = 72.5
        runtime_entity_interpretation_model_json['relative_week'] = 72.5
        runtime_entity_interpretation_model_json['relative_weekend'] = 72.5
        runtime_entity_interpretation_model_json['relative_year'] = 72.5
        runtime_entity_interpretation_model_json['specific_day'] = 72.5
        runtime_entity_interpretation_model_json['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model_json['specific_month'] = 72.5
        runtime_entity_interpretation_model_json['specific_quarter'] = 72.5
        runtime_entity_interpretation_model_json['specific_year'] = 72.5
        runtime_entity_interpretation_model_json['numeric_value'] = 72.5
        runtime_entity_interpretation_model_json['subtype'] = 'testString'
        runtime_entity_interpretation_model_json['part_of_day'] = 'testString'
        runtime_entity_interpretation_model_json['relative_hour'] = 72.5
        runtime_entity_interpretation_model_json['relative_minute'] = 72.5
        runtime_entity_interpretation_model_json['relative_second'] = 72.5
        runtime_entity_interpretation_model_json['specific_hour'] = 72.5
        runtime_entity_interpretation_model_json['specific_minute'] = 72.5
        runtime_entity_interpretation_model_json['specific_second'] = 72.5
        runtime_entity_interpretation_model_json['timezone'] = 'testString'

        # Construct a model instance of RuntimeEntityInterpretation by calling from_dict on the json representation
        runtime_entity_interpretation_model = RuntimeEntityInterpretation.from_dict(runtime_entity_interpretation_model_json)
        assert runtime_entity_interpretation_model != False

        # Construct a model instance of RuntimeEntityInterpretation by calling from_dict on the json representation
        runtime_entity_interpretation_model_dict = RuntimeEntityInterpretation.from_dict(runtime_entity_interpretation_model_json).__dict__
        runtime_entity_interpretation_model2 = RuntimeEntityInterpretation(**runtime_entity_interpretation_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_interpretation_model == runtime_entity_interpretation_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_interpretation_model_json2 = runtime_entity_interpretation_model.to_dict()
        assert runtime_entity_interpretation_model_json2 == runtime_entity_interpretation_model_json

class TestModel_RuntimeEntityRole():
    """
    Test Class for RuntimeEntityRole
    """

    def test_runtime_entity_role_serialization(self):
        """
        Test serialization/deserialization for RuntimeEntityRole
        """

        # Construct a json representation of a RuntimeEntityRole model
        runtime_entity_role_model_json = {}
        runtime_entity_role_model_json['type'] = 'date_from'

        # Construct a model instance of RuntimeEntityRole by calling from_dict on the json representation
        runtime_entity_role_model = RuntimeEntityRole.from_dict(runtime_entity_role_model_json)
        assert runtime_entity_role_model != False

        # Construct a model instance of RuntimeEntityRole by calling from_dict on the json representation
        runtime_entity_role_model_dict = RuntimeEntityRole.from_dict(runtime_entity_role_model_json).__dict__
        runtime_entity_role_model2 = RuntimeEntityRole(**runtime_entity_role_model_dict)

        # Verify the model instances are equivalent
        assert runtime_entity_role_model == runtime_entity_role_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_entity_role_model_json2 = runtime_entity_role_model.to_dict()
        assert runtime_entity_role_model_json2 == runtime_entity_role_model_json

class TestModel_RuntimeIntent():
    """
    Test Class for RuntimeIntent
    """

    def test_runtime_intent_serialization(self):
        """
        Test serialization/deserialization for RuntimeIntent
        """

        # Construct a json representation of a RuntimeIntent model
        runtime_intent_model_json = {}
        runtime_intent_model_json['intent'] = 'testString'
        runtime_intent_model_json['confidence'] = 72.5

        # Construct a model instance of RuntimeIntent by calling from_dict on the json representation
        runtime_intent_model = RuntimeIntent.from_dict(runtime_intent_model_json)
        assert runtime_intent_model != False

        # Construct a model instance of RuntimeIntent by calling from_dict on the json representation
        runtime_intent_model_dict = RuntimeIntent.from_dict(runtime_intent_model_json).__dict__
        runtime_intent_model2 = RuntimeIntent(**runtime_intent_model_dict)

        # Verify the model instances are equivalent
        assert runtime_intent_model == runtime_intent_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_intent_model_json2 = runtime_intent_model.to_dict()
        assert runtime_intent_model_json2 == runtime_intent_model_json

class TestModel_SearchResult():
    """
    Test Class for SearchResult
    """

    def test_search_result_serialization(self):
        """
        Test serialization/deserialization for SearchResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_result_metadata_model = {} # SearchResultMetadata
        search_result_metadata_model['confidence'] = 72.5
        search_result_metadata_model['score'] = 72.5

        search_result_highlight_model = {} # SearchResultHighlight
        search_result_highlight_model['body'] = ['testString']
        search_result_highlight_model['title'] = ['testString']
        search_result_highlight_model['url'] = ['testString']
        search_result_highlight_model['foo'] = ['testString']

        search_result_answer_model = {} # SearchResultAnswer
        search_result_answer_model['text'] = 'testString'
        search_result_answer_model['confidence'] = 0

        # Construct a json representation of a SearchResult model
        search_result_model_json = {}
        search_result_model_json['id'] = 'testString'
        search_result_model_json['result_metadata'] = search_result_metadata_model
        search_result_model_json['body'] = 'testString'
        search_result_model_json['title'] = 'testString'
        search_result_model_json['url'] = 'testString'
        search_result_model_json['highlight'] = search_result_highlight_model
        search_result_model_json['answers'] = [search_result_answer_model]

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model = SearchResult.from_dict(search_result_model_json)
        assert search_result_model != False

        # Construct a model instance of SearchResult by calling from_dict on the json representation
        search_result_model_dict = SearchResult.from_dict(search_result_model_json).__dict__
        search_result_model2 = SearchResult(**search_result_model_dict)

        # Verify the model instances are equivalent
        assert search_result_model == search_result_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_model_json2 = search_result_model.to_dict()
        assert search_result_model_json2 == search_result_model_json

class TestModel_SearchResultAnswer():
    """
    Test Class for SearchResultAnswer
    """

    def test_search_result_answer_serialization(self):
        """
        Test serialization/deserialization for SearchResultAnswer
        """

        # Construct a json representation of a SearchResultAnswer model
        search_result_answer_model_json = {}
        search_result_answer_model_json['text'] = 'testString'
        search_result_answer_model_json['confidence'] = 0

        # Construct a model instance of SearchResultAnswer by calling from_dict on the json representation
        search_result_answer_model = SearchResultAnswer.from_dict(search_result_answer_model_json)
        assert search_result_answer_model != False

        # Construct a model instance of SearchResultAnswer by calling from_dict on the json representation
        search_result_answer_model_dict = SearchResultAnswer.from_dict(search_result_answer_model_json).__dict__
        search_result_answer_model2 = SearchResultAnswer(**search_result_answer_model_dict)

        # Verify the model instances are equivalent
        assert search_result_answer_model == search_result_answer_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_answer_model_json2 = search_result_answer_model.to_dict()
        assert search_result_answer_model_json2 == search_result_answer_model_json

class TestModel_SearchResultHighlight():
    """
    Test Class for SearchResultHighlight
    """

    def test_search_result_highlight_serialization(self):
        """
        Test serialization/deserialization for SearchResultHighlight
        """

        # Construct a json representation of a SearchResultHighlight model
        search_result_highlight_model_json = {}
        search_result_highlight_model_json['body'] = ['testString']
        search_result_highlight_model_json['title'] = ['testString']
        search_result_highlight_model_json['url'] = ['testString']
        search_result_highlight_model_json['foo'] = ['testString']

        # Construct a model instance of SearchResultHighlight by calling from_dict on the json representation
        search_result_highlight_model = SearchResultHighlight.from_dict(search_result_highlight_model_json)
        assert search_result_highlight_model != False

        # Construct a model instance of SearchResultHighlight by calling from_dict on the json representation
        search_result_highlight_model_dict = SearchResultHighlight.from_dict(search_result_highlight_model_json).__dict__
        search_result_highlight_model2 = SearchResultHighlight(**search_result_highlight_model_dict)

        # Verify the model instances are equivalent
        assert search_result_highlight_model == search_result_highlight_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_highlight_model_json2 = search_result_highlight_model.to_dict()
        assert search_result_highlight_model_json2 == search_result_highlight_model_json

        # Test get_properties and set_properties methods.
        search_result_highlight_model.set_properties({})
        actual_dict = search_result_highlight_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': ['testString']}
        search_result_highlight_model.set_properties(expected_dict)
        actual_dict = search_result_highlight_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_SearchResultMetadata():
    """
    Test Class for SearchResultMetadata
    """

    def test_search_result_metadata_serialization(self):
        """
        Test serialization/deserialization for SearchResultMetadata
        """

        # Construct a json representation of a SearchResultMetadata model
        search_result_metadata_model_json = {}
        search_result_metadata_model_json['confidence'] = 72.5
        search_result_metadata_model_json['score'] = 72.5

        # Construct a model instance of SearchResultMetadata by calling from_dict on the json representation
        search_result_metadata_model = SearchResultMetadata.from_dict(search_result_metadata_model_json)
        assert search_result_metadata_model != False

        # Construct a model instance of SearchResultMetadata by calling from_dict on the json representation
        search_result_metadata_model_dict = SearchResultMetadata.from_dict(search_result_metadata_model_json).__dict__
        search_result_metadata_model2 = SearchResultMetadata(**search_result_metadata_model_dict)

        # Verify the model instances are equivalent
        assert search_result_metadata_model == search_result_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        search_result_metadata_model_json2 = search_result_metadata_model.to_dict()
        assert search_result_metadata_model_json2 == search_result_metadata_model_json

class TestModel_SessionResponse():
    """
    Test Class for SessionResponse
    """

    def test_session_response_serialization(self):
        """
        Test serialization/deserialization for SessionResponse
        """

        # Construct a json representation of a SessionResponse model
        session_response_model_json = {}
        session_response_model_json['session_id'] = 'testString'

        # Construct a model instance of SessionResponse by calling from_dict on the json representation
        session_response_model = SessionResponse.from_dict(session_response_model_json)
        assert session_response_model != False

        # Construct a model instance of SessionResponse by calling from_dict on the json representation
        session_response_model_dict = SessionResponse.from_dict(session_response_model_json).__dict__
        session_response_model2 = SessionResponse(**session_response_model_dict)

        # Verify the model instances are equivalent
        assert session_response_model == session_response_model2

        # Convert model instance back to dict and verify no loss of data
        session_response_model_json2 = session_response_model.to_dict()
        assert session_response_model_json2 == session_response_model_json

class TestModel_LogMessageSourceAction():
    """
    Test Class for LogMessageSourceAction
    """

    def test_log_message_source_action_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceAction
        """

        # Construct a json representation of a LogMessageSourceAction model
        log_message_source_action_model_json = {}
        log_message_source_action_model_json['type'] = 'action'
        log_message_source_action_model_json['action'] = 'testString'

        # Construct a model instance of LogMessageSourceAction by calling from_dict on the json representation
        log_message_source_action_model = LogMessageSourceAction.from_dict(log_message_source_action_model_json)
        assert log_message_source_action_model != False

        # Construct a model instance of LogMessageSourceAction by calling from_dict on the json representation
        log_message_source_action_model_dict = LogMessageSourceAction.from_dict(log_message_source_action_model_json).__dict__
        log_message_source_action_model2 = LogMessageSourceAction(**log_message_source_action_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_action_model == log_message_source_action_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_action_model_json2 = log_message_source_action_model.to_dict()
        assert log_message_source_action_model_json2 == log_message_source_action_model_json

class TestModel_LogMessageSourceDialogNode():
    """
    Test Class for LogMessageSourceDialogNode
    """

    def test_log_message_source_dialog_node_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceDialogNode
        """

        # Construct a json representation of a LogMessageSourceDialogNode model
        log_message_source_dialog_node_model_json = {}
        log_message_source_dialog_node_model_json['type'] = 'dialog_node'
        log_message_source_dialog_node_model_json['dialog_node'] = 'testString'

        # Construct a model instance of LogMessageSourceDialogNode by calling from_dict on the json representation
        log_message_source_dialog_node_model = LogMessageSourceDialogNode.from_dict(log_message_source_dialog_node_model_json)
        assert log_message_source_dialog_node_model != False

        # Construct a model instance of LogMessageSourceDialogNode by calling from_dict on the json representation
        log_message_source_dialog_node_model_dict = LogMessageSourceDialogNode.from_dict(log_message_source_dialog_node_model_json).__dict__
        log_message_source_dialog_node_model2 = LogMessageSourceDialogNode(**log_message_source_dialog_node_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_dialog_node_model == log_message_source_dialog_node_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_dialog_node_model_json2 = log_message_source_dialog_node_model.to_dict()
        assert log_message_source_dialog_node_model_json2 == log_message_source_dialog_node_model_json

class TestModel_LogMessageSourceHandler():
    """
    Test Class for LogMessageSourceHandler
    """

    def test_log_message_source_handler_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceHandler
        """

        # Construct a json representation of a LogMessageSourceHandler model
        log_message_source_handler_model_json = {}
        log_message_source_handler_model_json['type'] = 'handler'
        log_message_source_handler_model_json['action'] = 'testString'
        log_message_source_handler_model_json['step'] = 'testString'
        log_message_source_handler_model_json['handler'] = 'testString'

        # Construct a model instance of LogMessageSourceHandler by calling from_dict on the json representation
        log_message_source_handler_model = LogMessageSourceHandler.from_dict(log_message_source_handler_model_json)
        assert log_message_source_handler_model != False

        # Construct a model instance of LogMessageSourceHandler by calling from_dict on the json representation
        log_message_source_handler_model_dict = LogMessageSourceHandler.from_dict(log_message_source_handler_model_json).__dict__
        log_message_source_handler_model2 = LogMessageSourceHandler(**log_message_source_handler_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_handler_model == log_message_source_handler_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_handler_model_json2 = log_message_source_handler_model.to_dict()
        assert log_message_source_handler_model_json2 == log_message_source_handler_model_json

class TestModel_LogMessageSourceStep():
    """
    Test Class for LogMessageSourceStep
    """

    def test_log_message_source_step_serialization(self):
        """
        Test serialization/deserialization for LogMessageSourceStep
        """

        # Construct a json representation of a LogMessageSourceStep model
        log_message_source_step_model_json = {}
        log_message_source_step_model_json['type'] = 'step'
        log_message_source_step_model_json['action'] = 'testString'
        log_message_source_step_model_json['step'] = 'testString'

        # Construct a model instance of LogMessageSourceStep by calling from_dict on the json representation
        log_message_source_step_model = LogMessageSourceStep.from_dict(log_message_source_step_model_json)
        assert log_message_source_step_model != False

        # Construct a model instance of LogMessageSourceStep by calling from_dict on the json representation
        log_message_source_step_model_dict = LogMessageSourceStep.from_dict(log_message_source_step_model_json).__dict__
        log_message_source_step_model2 = LogMessageSourceStep(**log_message_source_step_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_step_model == log_message_source_step_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_step_model_json2 = log_message_source_step_model.to_dict()
        assert log_message_source_step_model_json2 == log_message_source_step_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeChannelTransfer():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeChannelTransfer
    """

    def test_runtime_response_generic_runtime_response_type_channel_transfer_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeChannelTransfer
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeChannelTransfer model
        runtime_response_generic_runtime_response_type_channel_transfer_model_json = {}
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['response_type'] = 'channel_transfer'
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['message_to_user'] = 'testString'
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['transfer_info'] = channel_transfer_info_model
        runtime_response_generic_runtime_response_type_channel_transfer_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeChannelTransfer by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_channel_transfer_model = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer.from_dict(runtime_response_generic_runtime_response_type_channel_transfer_model_json)
        assert runtime_response_generic_runtime_response_type_channel_transfer_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeChannelTransfer by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_channel_transfer_model_dict = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer.from_dict(runtime_response_generic_runtime_response_type_channel_transfer_model_json).__dict__
        runtime_response_generic_runtime_response_type_channel_transfer_model2 = RuntimeResponseGenericRuntimeResponseTypeChannelTransfer(**runtime_response_generic_runtime_response_type_channel_transfer_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_channel_transfer_model == runtime_response_generic_runtime_response_type_channel_transfer_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_channel_transfer_model_json2 = runtime_response_generic_runtime_response_type_channel_transfer_model.to_dict()
        assert runtime_response_generic_runtime_response_type_channel_transfer_model_json2 == runtime_response_generic_runtime_response_type_channel_transfer_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeConnectToAgent():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeConnectToAgent
    """

    def test_runtime_response_generic_runtime_response_type_connect_to_agent_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeConnectToAgent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        agent_availability_message_model = {} # AgentAvailabilityMessage
        agent_availability_message_model['message'] = 'testString'

        dialog_node_output_connect_to_agent_transfer_info_model = {} # DialogNodeOutputConnectToAgentTransferInfo
        dialog_node_output_connect_to_agent_transfer_info_model['target'] = {}

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json = {}
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['response_type'] = 'connect_to_agent'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['message_to_human_agent'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_available'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_unavailable'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['transfer_info'] = dialog_node_output_connect_to_agent_transfer_info_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['topic'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeConnectToAgent by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_connect_to_agent_model = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent.from_dict(runtime_response_generic_runtime_response_type_connect_to_agent_model_json)
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeConnectToAgent by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_connect_to_agent_model_dict = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent.from_dict(runtime_response_generic_runtime_response_type_connect_to_agent_model_json).__dict__
        runtime_response_generic_runtime_response_type_connect_to_agent_model2 = RuntimeResponseGenericRuntimeResponseTypeConnectToAgent(**runtime_response_generic_runtime_response_type_connect_to_agent_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model == runtime_response_generic_runtime_response_type_connect_to_agent_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json2 = runtime_response_generic_runtime_response_type_connect_to_agent_model.to_dict()
        assert runtime_response_generic_runtime_response_type_connect_to_agent_model_json2 == runtime_response_generic_runtime_response_type_connect_to_agent_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeImage():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeImage
    """

    def test_runtime_response_generic_runtime_response_type_image_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeImage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeImage model
        runtime_response_generic_runtime_response_type_image_model_json = {}
        runtime_response_generic_runtime_response_type_image_model_json['response_type'] = 'image'
        runtime_response_generic_runtime_response_type_image_model_json['source'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_image_model_json['channels'] = [response_generic_channel_model]
        runtime_response_generic_runtime_response_type_image_model_json['alt_text'] = 'testString'

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeImage by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_image_model = RuntimeResponseGenericRuntimeResponseTypeImage.from_dict(runtime_response_generic_runtime_response_type_image_model_json)
        assert runtime_response_generic_runtime_response_type_image_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeImage by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_image_model_dict = RuntimeResponseGenericRuntimeResponseTypeImage.from_dict(runtime_response_generic_runtime_response_type_image_model_json).__dict__
        runtime_response_generic_runtime_response_type_image_model2 = RuntimeResponseGenericRuntimeResponseTypeImage(**runtime_response_generic_runtime_response_type_image_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_image_model == runtime_response_generic_runtime_response_type_image_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_image_model_json2 = runtime_response_generic_runtime_response_type_image_model.to_dict()
        assert runtime_response_generic_runtime_response_type_image_model_json2 == runtime_response_generic_runtime_response_type_image_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeOption():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeOption
    """

    def test_runtime_response_generic_runtime_response_type_option_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeOption
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeOption model
        runtime_response_generic_runtime_response_type_option_model_json = {}
        runtime_response_generic_runtime_response_type_option_model_json['response_type'] = 'option'
        runtime_response_generic_runtime_response_type_option_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_option_model_json['description'] = 'testString'
        runtime_response_generic_runtime_response_type_option_model_json['preference'] = 'dropdown'
        runtime_response_generic_runtime_response_type_option_model_json['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_runtime_response_type_option_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeOption by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_option_model = RuntimeResponseGenericRuntimeResponseTypeOption.from_dict(runtime_response_generic_runtime_response_type_option_model_json)
        assert runtime_response_generic_runtime_response_type_option_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeOption by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_option_model_dict = RuntimeResponseGenericRuntimeResponseTypeOption.from_dict(runtime_response_generic_runtime_response_type_option_model_json).__dict__
        runtime_response_generic_runtime_response_type_option_model2 = RuntimeResponseGenericRuntimeResponseTypeOption(**runtime_response_generic_runtime_response_type_option_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_option_model == runtime_response_generic_runtime_response_type_option_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_option_model_json2 = runtime_response_generic_runtime_response_type_option_model.to_dict()
        assert runtime_response_generic_runtime_response_type_option_model_json2 == runtime_response_generic_runtime_response_type_option_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypePause():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypePause
    """

    def test_runtime_response_generic_runtime_response_type_pause_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypePause
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypePause model
        runtime_response_generic_runtime_response_type_pause_model_json = {}
        runtime_response_generic_runtime_response_type_pause_model_json['response_type'] = 'pause'
        runtime_response_generic_runtime_response_type_pause_model_json['time'] = 38
        runtime_response_generic_runtime_response_type_pause_model_json['typing'] = True
        runtime_response_generic_runtime_response_type_pause_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypePause by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_pause_model = RuntimeResponseGenericRuntimeResponseTypePause.from_dict(runtime_response_generic_runtime_response_type_pause_model_json)
        assert runtime_response_generic_runtime_response_type_pause_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypePause by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_pause_model_dict = RuntimeResponseGenericRuntimeResponseTypePause.from_dict(runtime_response_generic_runtime_response_type_pause_model_json).__dict__
        runtime_response_generic_runtime_response_type_pause_model2 = RuntimeResponseGenericRuntimeResponseTypePause(**runtime_response_generic_runtime_response_type_pause_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_pause_model == runtime_response_generic_runtime_response_type_pause_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_pause_model_json2 = runtime_response_generic_runtime_response_type_pause_model.to_dict()
        assert runtime_response_generic_runtime_response_type_pause_model_json2 == runtime_response_generic_runtime_response_type_pause_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeSearch():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeSearch
    """

    def test_runtime_response_generic_runtime_response_type_search_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeSearch
        """

        # Construct dict forms of any model objects needed in order to build this model.

        search_result_metadata_model = {} # SearchResultMetadata
        search_result_metadata_model['confidence'] = 72.5
        search_result_metadata_model['score'] = 72.5

        search_result_highlight_model = {} # SearchResultHighlight
        search_result_highlight_model['body'] = ['testString']
        search_result_highlight_model['title'] = ['testString']
        search_result_highlight_model['url'] = ['testString']
        search_result_highlight_model['foo'] = ['testString']

        search_result_answer_model = {} # SearchResultAnswer
        search_result_answer_model['text'] = 'testString'
        search_result_answer_model['confidence'] = 0

        search_result_model = {} # SearchResult
        search_result_model['id'] = 'testString'
        search_result_model['result_metadata'] = search_result_metadata_model
        search_result_model['body'] = 'testString'
        search_result_model['title'] = 'testString'
        search_result_model['url'] = 'testString'
        search_result_model['highlight'] = search_result_highlight_model
        search_result_model['answers'] = [search_result_answer_model]

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeSearch model
        runtime_response_generic_runtime_response_type_search_model_json = {}
        runtime_response_generic_runtime_response_type_search_model_json['response_type'] = 'search'
        runtime_response_generic_runtime_response_type_search_model_json['header'] = 'testString'
        runtime_response_generic_runtime_response_type_search_model_json['primary_results'] = [search_result_model]
        runtime_response_generic_runtime_response_type_search_model_json['additional_results'] = [search_result_model]
        runtime_response_generic_runtime_response_type_search_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSearch by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_search_model = RuntimeResponseGenericRuntimeResponseTypeSearch.from_dict(runtime_response_generic_runtime_response_type_search_model_json)
        assert runtime_response_generic_runtime_response_type_search_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSearch by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_search_model_dict = RuntimeResponseGenericRuntimeResponseTypeSearch.from_dict(runtime_response_generic_runtime_response_type_search_model_json).__dict__
        runtime_response_generic_runtime_response_type_search_model2 = RuntimeResponseGenericRuntimeResponseTypeSearch(**runtime_response_generic_runtime_response_type_search_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_search_model == runtime_response_generic_runtime_response_type_search_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_search_model_json2 = runtime_response_generic_runtime_response_type_search_model.to_dict()
        assert runtime_response_generic_runtime_response_type_search_model_json2 == runtime_response_generic_runtime_response_type_search_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeSuggestion():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeSuggestion
    """

    def test_runtime_response_generic_runtime_response_type_suggestion_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        runtime_intent_model = {} # RuntimeIntent
        runtime_intent_model['intent'] = 'testString'
        runtime_intent_model['confidence'] = 72.5

        capture_group_model = {} # CaptureGroup
        capture_group_model['group'] = 'testString'
        capture_group_model['location'] = [38]

        runtime_entity_interpretation_model = {} # RuntimeEntityInterpretation
        runtime_entity_interpretation_model['calendar_type'] = 'testString'
        runtime_entity_interpretation_model['datetime_link'] = 'testString'
        runtime_entity_interpretation_model['festival'] = 'testString'
        runtime_entity_interpretation_model['granularity'] = 'day'
        runtime_entity_interpretation_model['range_link'] = 'testString'
        runtime_entity_interpretation_model['range_modifier'] = 'testString'
        runtime_entity_interpretation_model['relative_day'] = 72.5
        runtime_entity_interpretation_model['relative_month'] = 72.5
        runtime_entity_interpretation_model['relative_week'] = 72.5
        runtime_entity_interpretation_model['relative_weekend'] = 72.5
        runtime_entity_interpretation_model['relative_year'] = 72.5
        runtime_entity_interpretation_model['specific_day'] = 72.5
        runtime_entity_interpretation_model['specific_day_of_week'] = 'testString'
        runtime_entity_interpretation_model['specific_month'] = 72.5
        runtime_entity_interpretation_model['specific_quarter'] = 72.5
        runtime_entity_interpretation_model['specific_year'] = 72.5
        runtime_entity_interpretation_model['numeric_value'] = 72.5
        runtime_entity_interpretation_model['subtype'] = 'testString'
        runtime_entity_interpretation_model['part_of_day'] = 'testString'
        runtime_entity_interpretation_model['relative_hour'] = 72.5
        runtime_entity_interpretation_model['relative_minute'] = 72.5
        runtime_entity_interpretation_model['relative_second'] = 72.5
        runtime_entity_interpretation_model['specific_hour'] = 72.5
        runtime_entity_interpretation_model['specific_minute'] = 72.5
        runtime_entity_interpretation_model['specific_second'] = 72.5
        runtime_entity_interpretation_model['timezone'] = 'testString'

        runtime_entity_alternative_model = {} # RuntimeEntityAlternative
        runtime_entity_alternative_model['value'] = 'testString'
        runtime_entity_alternative_model['confidence'] = 72.5

        runtime_entity_role_model = {} # RuntimeEntityRole
        runtime_entity_role_model['type'] = 'date_from'

        runtime_entity_model = {} # RuntimeEntity
        runtime_entity_model['entity'] = 'testString'
        runtime_entity_model['location'] = [38]
        runtime_entity_model['value'] = 'testString'
        runtime_entity_model['confidence'] = 72.5
        runtime_entity_model['metadata'] = {}
        runtime_entity_model['groups'] = [capture_group_model]
        runtime_entity_model['interpretation'] = runtime_entity_interpretation_model
        runtime_entity_model['alternatives'] = [runtime_entity_alternative_model]
        runtime_entity_model['role'] = runtime_entity_role_model

        message_input_options_spelling_model = {} # MessageInputOptionsSpelling
        message_input_options_spelling_model['suggestions'] = True
        message_input_options_spelling_model['auto_correct'] = True

        message_input_options_model = {} # MessageInputOptions
        message_input_options_model['restart'] = False
        message_input_options_model['alternate_intents'] = False
        message_input_options_model['spelling'] = message_input_options_spelling_model
        message_input_options_model['debug'] = False
        message_input_options_model['return_context'] = False
        message_input_options_model['export'] = False

        message_input_model = {} # MessageInput
        message_input_model['message_type'] = 'text'
        message_input_model['text'] = 'testString'
        message_input_model['intents'] = [runtime_intent_model]
        message_input_model['entities'] = [runtime_entity_model]
        message_input_model['suggestion_id'] = 'testString'
        message_input_model['options'] = message_input_options_model

        dialog_suggestion_value_model = {} # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model

        dialog_suggestion_model = {} # DialogSuggestion
        dialog_suggestion_model['label'] = 'testString'
        dialog_suggestion_model['value'] = dialog_suggestion_value_model
        dialog_suggestion_model['output'] = {}

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeSuggestion model
        runtime_response_generic_runtime_response_type_suggestion_model_json = {}
        runtime_response_generic_runtime_response_type_suggestion_model_json['response_type'] = 'suggestion'
        runtime_response_generic_runtime_response_type_suggestion_model_json['title'] = 'testString'
        runtime_response_generic_runtime_response_type_suggestion_model_json['suggestions'] = [dialog_suggestion_model]
        runtime_response_generic_runtime_response_type_suggestion_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSuggestion by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_suggestion_model = RuntimeResponseGenericRuntimeResponseTypeSuggestion.from_dict(runtime_response_generic_runtime_response_type_suggestion_model_json)
        assert runtime_response_generic_runtime_response_type_suggestion_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeSuggestion by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_suggestion_model_dict = RuntimeResponseGenericRuntimeResponseTypeSuggestion.from_dict(runtime_response_generic_runtime_response_type_suggestion_model_json).__dict__
        runtime_response_generic_runtime_response_type_suggestion_model2 = RuntimeResponseGenericRuntimeResponseTypeSuggestion(**runtime_response_generic_runtime_response_type_suggestion_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_suggestion_model == runtime_response_generic_runtime_response_type_suggestion_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_suggestion_model_json2 = runtime_response_generic_runtime_response_type_suggestion_model.to_dict()
        assert runtime_response_generic_runtime_response_type_suggestion_model_json2 == runtime_response_generic_runtime_response_type_suggestion_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeText():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeText
    """

    def test_runtime_response_generic_runtime_response_type_text_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeText
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeText model
        runtime_response_generic_runtime_response_type_text_model_json = {}
        runtime_response_generic_runtime_response_type_text_model_json['response_type'] = 'text'
        runtime_response_generic_runtime_response_type_text_model_json['text'] = 'testString'
        runtime_response_generic_runtime_response_type_text_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeText by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_text_model = RuntimeResponseGenericRuntimeResponseTypeText.from_dict(runtime_response_generic_runtime_response_type_text_model_json)
        assert runtime_response_generic_runtime_response_type_text_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeText by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_text_model_dict = RuntimeResponseGenericRuntimeResponseTypeText.from_dict(runtime_response_generic_runtime_response_type_text_model_json).__dict__
        runtime_response_generic_runtime_response_type_text_model2 = RuntimeResponseGenericRuntimeResponseTypeText(**runtime_response_generic_runtime_response_type_text_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_text_model == runtime_response_generic_runtime_response_type_text_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_text_model_json2 = runtime_response_generic_runtime_response_type_text_model.to_dict()
        assert runtime_response_generic_runtime_response_type_text_model_json2 == runtime_response_generic_runtime_response_type_text_model_json

class TestModel_RuntimeResponseGenericRuntimeResponseTypeUserDefined():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeUserDefined
    """

    def test_runtime_response_generic_runtime_response_type_user_defined_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeUserDefined
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'testString'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeUserDefined model
        runtime_response_generic_runtime_response_type_user_defined_model_json = {}
        runtime_response_generic_runtime_response_type_user_defined_model_json['response_type'] = 'user_defined'
        runtime_response_generic_runtime_response_type_user_defined_model_json['user_defined'] = {}
        runtime_response_generic_runtime_response_type_user_defined_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeUserDefined by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_user_defined_model = RuntimeResponseGenericRuntimeResponseTypeUserDefined.from_dict(runtime_response_generic_runtime_response_type_user_defined_model_json)
        assert runtime_response_generic_runtime_response_type_user_defined_model != False

        # Construct a model instance of RuntimeResponseGenericRuntimeResponseTypeUserDefined by calling from_dict on the json representation
        runtime_response_generic_runtime_response_type_user_defined_model_dict = RuntimeResponseGenericRuntimeResponseTypeUserDefined.from_dict(runtime_response_generic_runtime_response_type_user_defined_model_json).__dict__
        runtime_response_generic_runtime_response_type_user_defined_model2 = RuntimeResponseGenericRuntimeResponseTypeUserDefined(**runtime_response_generic_runtime_response_type_user_defined_model_dict)

        # Verify the model instances are equivalent
        assert runtime_response_generic_runtime_response_type_user_defined_model == runtime_response_generic_runtime_response_type_user_defined_model2

        # Convert model instance back to dict and verify no loss of data
        runtime_response_generic_runtime_response_type_user_defined_model_json2 = runtime_response_generic_runtime_response_type_user_defined_model.to_dict()
        assert runtime_response_generic_runtime_response_type_user_defined_model_json2 == runtime_response_generic_runtime_response_type_user_defined_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
