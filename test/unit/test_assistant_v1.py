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
Unit Tests for AssistantV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_watson.assistant_v1 import *

version = 'testString'

_service = AssistantV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.assistant.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/message')
        mock_response = '{"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a MessageInput model
        message_input_model = {}
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['foo'] = 'testString'

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

        # Construct a dict representation of a MessageContextMetadata model
        message_context_metadata_model = {}
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        # Construct a dict representation of a Context model
        context_model = {}
        context_model['conversation_id'] = 'testString'
        context_model['system'] = {}
        context_model['metadata'] = message_context_metadata_model
        context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeVisitedDetails model
        dialog_node_visited_details_model = {}
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        # Construct a dict representation of a LogMessageSource model
        log_message_source_model = {}
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        # Construct a dict representation of a LogMessage model
        log_message_model = {}
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        # Construct a dict representation of a DialogNodeOutputOptionsElementValue model
        dialog_node_output_options_element_value_model = {}
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        # Construct a dict representation of a DialogNodeOutputOptionsElement model
        dialog_node_output_options_element_model = {}
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a RuntimeResponseGenericRuntimeResponseTypeOption model
        runtime_response_generic_model = {}
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a OutputData model
        output_data_model = {}
        output_data_model['nodes_visited'] = ['testString']
        output_data_model['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model['log_messages'] = [log_message_model]
        output_data_model['text'] = ['testString']
        output_data_model['generic'] = [runtime_response_generic_model]
        output_data_model['foo'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        input = message_input_model
        intents = [runtime_intent_model]
        entities = [runtime_entity_model]
        alternate_intents = False
        context = context_model
        output = output_data_model
        user_id = 'testString'
        nodes_visited_details = False

        # Invoke method
        response = _service.message(
            workspace_id,
            input=input,
            intents=intents,
            entities=entities,
            alternate_intents=alternate_intents,
            context=context,
            output=output,
            user_id=user_id,
            nodes_visited_details=nodes_visited_details,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'nodes_visited_details={}'.format('true' if nodes_visited_details else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['input'] == message_input_model
        assert req_body['intents'] == [runtime_intent_model]
        assert req_body['entities'] == [runtime_entity_model]
        assert req_body['alternate_intents'] == False
        assert req_body['context'] == context_model
        assert req_body['output'] == output_data_model
        assert req_body['user_id'] == 'testString'


    @responses.activate
    def test_message_required_params(self):
        """
        test_message_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/message')
        mock_response = '{"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.message(
            workspace_id,
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/message')
        mock_response = '{"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.message(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/bulk_classify')
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
        workspace_id = 'testString'
        input = [bulk_classify_utterance_model]

        # Invoke method
        response = _service.bulk_classify(
            workspace_id,
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "intents": [{"intent": "intent", "confidence": 10}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.bulk_classify(
            workspace_id,
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/bulk_classify')
        mock_response = '{"output": [{"input": {"text": "text"}, "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "intents": [{"intent": "intent", "confidence": 10}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
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
# Start of Service: Workspaces
##############################################################################
# region

class TestListWorkspaces():
    """
    Test Class for list_workspaces
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
    def test_list_workspaces_all_params(self):
        """
        list_workspaces()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"workspaces": [{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        page_limit = 38
        include_count = False
        sort = 'name'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_workspaces(
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_workspaces_required_params(self):
        """
        test_list_workspaces_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"workspaces": [{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_workspaces()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_workspaces_value_error(self):
        """
        test_list_workspaces_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"workspaces": [{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
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
                _service.list_workspaces(**req_copy)



class TestCreateWorkspace():
    """
    Test Class for create_workspace
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
    def test_create_workspace_all_params(self):
        """
        create_workspace()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Construct a dict representation of a DialogNode model
        dialog_node_model = {}
        dialog_node_model['dialog_node'] = 'testString'
        dialog_node_model['description'] = 'testString'
        dialog_node_model['conditions'] = 'testString'
        dialog_node_model['parent'] = 'testString'
        dialog_node_model['previous_sibling'] = 'testString'
        dialog_node_model['output'] = dialog_node_output_model
        dialog_node_model['context'] = dialog_node_context_model
        dialog_node_model['metadata'] = {}
        dialog_node_model['next_step'] = dialog_node_next_step_model
        dialog_node_model['title'] = 'testString'
        dialog_node_model['type'] = 'standard'
        dialog_node_model['event_name'] = 'focus'
        dialog_node_model['variable'] = 'testString'
        dialog_node_model['actions'] = [dialog_node_action_model]
        dialog_node_model['digress_in'] = 'not_available'
        dialog_node_model['digress_out'] = 'allow_returning'
        dialog_node_model['digress_out_slots'] = 'not_allowed'
        dialog_node_model['user_label'] = 'testString'
        dialog_node_model['disambiguation_opt_out'] = False

        # Construct a dict representation of a Counterexample model
        counterexample_model = {}
        counterexample_model['text'] = 'testString'

        # Construct a dict representation of a WorkspaceSystemSettingsTooling model
        workspace_system_settings_tooling_model = {}
        workspace_system_settings_tooling_model['store_generic_responses'] = True

        # Construct a dict representation of a WorkspaceSystemSettingsDisambiguation model
        workspace_system_settings_disambiguation_model = {}
        workspace_system_settings_disambiguation_model['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['enabled'] = False
        workspace_system_settings_disambiguation_model['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model['randomize'] = True
        workspace_system_settings_disambiguation_model['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model['suggestion_text_policy'] = 'testString'

        # Construct a dict representation of a WorkspaceSystemSettingsSystemEntities model
        workspace_system_settings_system_entities_model = {}
        workspace_system_settings_system_entities_model['enabled'] = False

        # Construct a dict representation of a WorkspaceSystemSettingsOffTopic model
        workspace_system_settings_off_topic_model = {}
        workspace_system_settings_off_topic_model['enabled'] = False

        # Construct a dict representation of a WorkspaceSystemSettings model
        workspace_system_settings_model = {}
        workspace_system_settings_model['tooling'] = workspace_system_settings_tooling_model
        workspace_system_settings_model['disambiguation'] = workspace_system_settings_disambiguation_model
        workspace_system_settings_model['human_agent_assist'] = {}
        workspace_system_settings_model['spelling_suggestions'] = False
        workspace_system_settings_model['spelling_auto_correct'] = False
        workspace_system_settings_model['system_entities'] = workspace_system_settings_system_entities_model
        workspace_system_settings_model['off_topic'] = workspace_system_settings_off_topic_model

        # Construct a dict representation of a WebhookHeader model
        webhook_header_model = {}
        webhook_header_model['name'] = 'testString'
        webhook_header_model['value'] = 'testString'

        # Construct a dict representation of a Webhook model
        webhook_model = {}
        webhook_model['url'] = 'testString'
        webhook_model['name'] = 'testString'
        webhook_model['headers'] = [webhook_header_model]

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Construct a dict representation of a CreateIntent model
        create_intent_model = {}
        create_intent_model['intent'] = 'testString'
        create_intent_model['description'] = 'testString'
        create_intent_model['examples'] = [example_model]

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Construct a dict representation of a CreateEntity model
        create_entity_model = {}
        create_entity_model['entity'] = 'testString'
        create_entity_model['description'] = 'testString'
        create_entity_model['metadata'] = {}
        create_entity_model['fuzzy_match'] = True
        create_entity_model['values'] = [create_value_model]

        # Set up parameter values
        name = 'testString'
        description = 'testString'
        language = 'testString'
        dialog_nodes = [dialog_node_model]
        counterexamples = [counterexample_model]
        metadata = {}
        learning_opt_out = False
        system_settings = workspace_system_settings_model
        webhooks = [webhook_model]
        intents = [create_intent_model]
        entities = [create_entity_model]
        include_audit = False

        # Invoke method
        response = _service.create_workspace(
            name=name,
            description=description,
            language=language,
            dialog_nodes=dialog_nodes,
            counterexamples=counterexamples,
            metadata=metadata,
            learning_opt_out=learning_opt_out,
            system_settings=system_settings,
            webhooks=webhooks,
            intents=intents,
            entities=entities,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['language'] == 'testString'
        assert req_body['dialog_nodes'] == [dialog_node_model]
        assert req_body['counterexamples'] == [counterexample_model]
        assert req_body['metadata'] == {}
        assert req_body['learning_opt_out'] == False
        assert req_body['system_settings'] == workspace_system_settings_model
        assert req_body['webhooks'] == [webhook_model]
        assert req_body['intents'] == [create_intent_model]
        assert req_body['entities'] == [create_entity_model]


    @responses.activate
    def test_create_workspace_required_params(self):
        """
        test_create_workspace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Invoke method
        response = _service.create_workspace()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_create_workspace_value_error(self):
        """
        test_create_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_workspace(**req_copy)



class TestGetWorkspace():
    """
    Test Class for get_workspace
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
    def test_get_workspace_all_params(self):
        """
        get_workspace()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        export = False
        include_audit = False
        sort = 'stable'

        # Invoke method
        response = _service.get_workspace(
            workspace_id,
            export=export,
            include_audit=include_audit,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string


    @responses.activate
    def test_get_workspace_required_params(self):
        """
        test_get_workspace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.get_workspace(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_workspace_value_error(self):
        """
        test_get_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_workspace(**req_copy)



class TestUpdateWorkspace():
    """
    Test Class for update_workspace
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
    def test_update_workspace_all_params(self):
        """
        update_workspace()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Construct a dict representation of a DialogNode model
        dialog_node_model = {}
        dialog_node_model['dialog_node'] = 'testString'
        dialog_node_model['description'] = 'testString'
        dialog_node_model['conditions'] = 'testString'
        dialog_node_model['parent'] = 'testString'
        dialog_node_model['previous_sibling'] = 'testString'
        dialog_node_model['output'] = dialog_node_output_model
        dialog_node_model['context'] = dialog_node_context_model
        dialog_node_model['metadata'] = {}
        dialog_node_model['next_step'] = dialog_node_next_step_model
        dialog_node_model['title'] = 'testString'
        dialog_node_model['type'] = 'standard'
        dialog_node_model['event_name'] = 'focus'
        dialog_node_model['variable'] = 'testString'
        dialog_node_model['actions'] = [dialog_node_action_model]
        dialog_node_model['digress_in'] = 'not_available'
        dialog_node_model['digress_out'] = 'allow_returning'
        dialog_node_model['digress_out_slots'] = 'not_allowed'
        dialog_node_model['user_label'] = 'testString'
        dialog_node_model['disambiguation_opt_out'] = False

        # Construct a dict representation of a Counterexample model
        counterexample_model = {}
        counterexample_model['text'] = 'testString'

        # Construct a dict representation of a WorkspaceSystemSettingsTooling model
        workspace_system_settings_tooling_model = {}
        workspace_system_settings_tooling_model['store_generic_responses'] = True

        # Construct a dict representation of a WorkspaceSystemSettingsDisambiguation model
        workspace_system_settings_disambiguation_model = {}
        workspace_system_settings_disambiguation_model['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['enabled'] = False
        workspace_system_settings_disambiguation_model['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model['randomize'] = True
        workspace_system_settings_disambiguation_model['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model['suggestion_text_policy'] = 'testString'

        # Construct a dict representation of a WorkspaceSystemSettingsSystemEntities model
        workspace_system_settings_system_entities_model = {}
        workspace_system_settings_system_entities_model['enabled'] = False

        # Construct a dict representation of a WorkspaceSystemSettingsOffTopic model
        workspace_system_settings_off_topic_model = {}
        workspace_system_settings_off_topic_model['enabled'] = False

        # Construct a dict representation of a WorkspaceSystemSettings model
        workspace_system_settings_model = {}
        workspace_system_settings_model['tooling'] = workspace_system_settings_tooling_model
        workspace_system_settings_model['disambiguation'] = workspace_system_settings_disambiguation_model
        workspace_system_settings_model['human_agent_assist'] = {}
        workspace_system_settings_model['spelling_suggestions'] = False
        workspace_system_settings_model['spelling_auto_correct'] = False
        workspace_system_settings_model['system_entities'] = workspace_system_settings_system_entities_model
        workspace_system_settings_model['off_topic'] = workspace_system_settings_off_topic_model

        # Construct a dict representation of a WebhookHeader model
        webhook_header_model = {}
        webhook_header_model['name'] = 'testString'
        webhook_header_model['value'] = 'testString'

        # Construct a dict representation of a Webhook model
        webhook_model = {}
        webhook_model['url'] = 'testString'
        webhook_model['name'] = 'testString'
        webhook_model['headers'] = [webhook_header_model]

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Construct a dict representation of a CreateIntent model
        create_intent_model = {}
        create_intent_model['intent'] = 'testString'
        create_intent_model['description'] = 'testString'
        create_intent_model['examples'] = [example_model]

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Construct a dict representation of a CreateEntity model
        create_entity_model = {}
        create_entity_model['entity'] = 'testString'
        create_entity_model['description'] = 'testString'
        create_entity_model['metadata'] = {}
        create_entity_model['fuzzy_match'] = True
        create_entity_model['values'] = [create_value_model]

        # Set up parameter values
        workspace_id = 'testString'
        name = 'testString'
        description = 'testString'
        language = 'testString'
        dialog_nodes = [dialog_node_model]
        counterexamples = [counterexample_model]
        metadata = {}
        learning_opt_out = False
        system_settings = workspace_system_settings_model
        webhooks = [webhook_model]
        intents = [create_intent_model]
        entities = [create_entity_model]
        append = False
        include_audit = False

        # Invoke method
        response = _service.update_workspace(
            workspace_id,
            name=name,
            description=description,
            language=language,
            dialog_nodes=dialog_nodes,
            counterexamples=counterexamples,
            metadata=metadata,
            learning_opt_out=learning_opt_out,
            system_settings=system_settings,
            webhooks=webhooks,
            intents=intents,
            entities=entities,
            append=append,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'append={}'.format('true' if append else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['language'] == 'testString'
        assert req_body['dialog_nodes'] == [dialog_node_model]
        assert req_body['counterexamples'] == [counterexample_model]
        assert req_body['metadata'] == {}
        assert req_body['learning_opt_out'] == False
        assert req_body['system_settings'] == workspace_system_settings_model
        assert req_body['webhooks'] == [webhook_model]
        assert req_body['intents'] == [create_intent_model]
        assert req_body['entities'] == [create_entity_model]


    @responses.activate
    def test_update_workspace_required_params(self):
        """
        test_update_workspace_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.update_workspace(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_workspace_value_error(self):
        """
        test_update_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        mock_response = '{"name": "name", "description": "description", "language": "language", "workspace_id": "workspace_id", "dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "metadata": {"mapKey": "anyValue"}, "learning_opt_out": false, "system_settings": {"tooling": {"store_generic_responses": false}, "disambiguation": {"prompt": "prompt", "none_of_the_above_prompt": "none_of_the_above_prompt", "enabled": false, "sensitivity": "auto", "randomize": false, "max_suggestions": 1, "suggestion_text_policy": "suggestion_text_policy"}, "human_agent_assist": {"mapKey": "anyValue"}, "spelling_suggestions": false, "spelling_auto_correct": false, "system_entities": {"enabled": false}, "off_topic": {"enabled": false}}, "status": "Non Existent", "webhooks": [{"url": "url", "name": "name", "headers": [{"name": "name", "value": "value"}]}], "intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_workspace(**req_copy)



class TestDeleteWorkspace():
    """
    Test Class for delete_workspace
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
    def test_delete_workspace_all_params(self):
        """
        delete_workspace()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.delete_workspace(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_workspace_value_error(self):
        """
        test_delete_workspace_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_workspace(**req_copy)



# endregion
##############################################################################
# End of Service: Workspaces
##############################################################################

##############################################################################
# Start of Service: Intents
##############################################################################
# region

class TestListIntents():
    """
    Test Class for list_intents
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
    def test_list_intents_all_params(self):
        """
        list_intents()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        export = False
        page_limit = 38
        include_count = False
        sort = 'intent'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_intents(
            workspace_id,
            export=export,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_intents_required_params(self):
        """
        test_list_intents_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.list_intents(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_intents_value_error(self):
        """
        test_list_intents_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intents": [{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_intents(**req_copy)



class TestCreateIntent():
    """
    Test Class for create_intent
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
    def test_create_intent_all_params(self):
        """
        create_intent()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        description = 'testString'
        examples = [example_model]
        include_audit = False

        # Invoke method
        response = _service.create_intent(
            workspace_id,
            intent,
            description=description,
            examples=examples,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['intent'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['examples'] == [example_model]


    @responses.activate
    def test_create_intent_required_params(self):
        """
        test_create_intent_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        description = 'testString'
        examples = [example_model]

        # Invoke method
        response = _service.create_intent(
            workspace_id,
            intent,
            description=description,
            examples=examples,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['intent'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['examples'] == [example_model]


    @responses.activate
    def test_create_intent_value_error(self):
        """
        test_create_intent_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        description = 'testString'
        examples = [example_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_intent(**req_copy)



class TestGetIntent():
    """
    Test Class for get_intent
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
    def test_get_intent_all_params(self):
        """
        get_intent()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        export = False
        include_audit = False

        # Invoke method
        response = _service.get_intent(
            workspace_id,
            intent,
            export=export,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_intent_required_params(self):
        """
        test_get_intent_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Invoke method
        response = _service.get_intent(
            workspace_id,
            intent,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_intent_value_error(self):
        """
        test_get_intent_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_intent(**req_copy)



class TestUpdateIntent():
    """
    Test Class for update_intent
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
    def test_update_intent_all_params(self):
        """
        update_intent()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        new_intent = 'testString'
        new_description = 'testString'
        new_examples = [example_model]
        append = False
        include_audit = False

        # Invoke method
        response = _service.update_intent(
            workspace_id,
            intent,
            new_intent=new_intent,
            new_description=new_description,
            new_examples=new_examples,
            append=append,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'append={}'.format('true' if append else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['intent'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['examples'] == [example_model]


    @responses.activate
    def test_update_intent_required_params(self):
        """
        test_update_intent_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        new_intent = 'testString'
        new_description = 'testString'
        new_examples = [example_model]

        # Invoke method
        response = _service.update_intent(
            workspace_id,
            intent,
            new_intent=new_intent,
            new_description=new_description,
            new_examples=new_examples,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['intent'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['examples'] == [example_model]


    @responses.activate
    def test_update_intent_value_error(self):
        """
        test_update_intent_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        mock_response = '{"intent": "intent", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a dict representation of a Example model
        example_model = {}
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        new_intent = 'testString'
        new_description = 'testString'
        new_examples = [example_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_intent(**req_copy)



class TestDeleteIntent():
    """
    Test Class for delete_intent
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
    def test_delete_intent_all_params(self):
        """
        delete_intent()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Invoke method
        response = _service.delete_intent(
            workspace_id,
            intent,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_intent_value_error(self):
        """
        test_delete_intent_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_intent(**req_copy)



# endregion
##############################################################################
# End of Service: Intents
##############################################################################

##############################################################################
# Start of Service: Examples
##############################################################################
# region

class TestListExamples():
    """
    Test Class for list_examples
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
    def test_list_examples_all_params(self):
        """
        list_examples()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        page_limit = 38
        include_count = False
        sort = 'text'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_examples(
            workspace_id,
            intent,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_examples_required_params(self):
        """
        test_list_examples_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Invoke method
        response = _service.list_examples(
            workspace_id,
            intent,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_examples_value_error(self):
        """
        test_list_examples_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"examples": [{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_examples(**req_copy)



class TestCreateExample():
    """
    Test Class for create_example
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
    def test_create_example_all_params(self):
        """
        create_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        mentions = [mention_model]
        include_audit = False

        # Invoke method
        response = _service.create_example(
            workspace_id,
            intent,
            text,
            mentions=mentions,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'
        assert req_body['mentions'] == [mention_model]


    @responses.activate
    def test_create_example_required_params(self):
        """
        test_create_example_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        mentions = [mention_model]

        # Invoke method
        response = _service.create_example(
            workspace_id,
            intent,
            text,
            mentions=mentions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'
        assert req_body['mentions'] == [mention_model]


    @responses.activate
    def test_create_example_value_error(self):
        """
        test_create_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        mentions = [mention_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_example(**req_copy)



class TestGetExample():
    """
    Test Class for get_example
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
    def test_get_example_all_params(self):
        """
        get_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_example(
            workspace_id,
            intent,
            text,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_example_required_params(self):
        """
        test_get_example_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.get_example(
            workspace_id,
            intent,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_example_value_error(self):
        """
        test_get_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_example(**req_copy)



class TestUpdateExample():
    """
    Test Class for update_example
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
    def test_update_example_all_params(self):
        """
        update_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        new_text = 'testString'
        new_mentions = [mention_model]
        include_audit = False

        # Invoke method
        response = _service.update_example(
            workspace_id,
            intent,
            text,
            new_text=new_text,
            new_mentions=new_mentions,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'
        assert req_body['mentions'] == [mention_model]


    @responses.activate
    def test_update_example_required_params(self):
        """
        test_update_example_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        new_text = 'testString'
        new_mentions = [mention_model]

        # Invoke method
        response = _service.update_example(
            workspace_id,
            intent,
            text,
            new_text=new_text,
            new_mentions=new_mentions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'
        assert req_body['mentions'] == [mention_model]


    @responses.activate
    def test_update_example_value_error(self):
        """
        test_update_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        mock_response = '{"text": "text", "mentions": [{"entity": "entity", "location": [8]}], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Mention model
        mention_model = {}
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'
        new_text = 'testString'
        new_mentions = [mention_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_example(**req_copy)



class TestDeleteExample():
    """
    Test Class for delete_example
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
    def test_delete_example_all_params(self):
        """
        delete_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.delete_example(
            workspace_id,
            intent,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_example_value_error(self):
        """
        test_delete_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/intents/testString/examples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        intent = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "intent": intent,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_example(**req_copy)



# endregion
##############################################################################
# End of Service: Examples
##############################################################################

##############################################################################
# Start of Service: Counterexamples
##############################################################################
# region

class TestListCounterexamples():
    """
    Test Class for list_counterexamples
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
    def test_list_counterexamples_all_params(self):
        """
        list_counterexamples()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        page_limit = 38
        include_count = False
        sort = 'text'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_counterexamples(
            workspace_id,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_counterexamples_required_params(self):
        """
        test_list_counterexamples_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.list_counterexamples(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_counterexamples_value_error(self):
        """
        test_list_counterexamples_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"counterexamples": [{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_counterexamples(**req_copy)



class TestCreateCounterexample():
    """
    Test Class for create_counterexample
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
    def test_create_counterexample_all_params(self):
        """
        create_counterexample()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'
        include_audit = False

        # Invoke method
        response = _service.create_counterexample(
            workspace_id,
            text,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_create_counterexample_required_params(self):
        """
        test_create_counterexample_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.create_counterexample(
            workspace_id,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_create_counterexample_value_error(self):
        """
        test_create_counterexample_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_counterexample(**req_copy)



class TestGetCounterexample():
    """
    Test Class for get_counterexample
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
    def test_get_counterexample_all_params(self):
        """
        get_counterexample()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_counterexample(
            workspace_id,
            text,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_counterexample_required_params(self):
        """
        test_get_counterexample_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.get_counterexample(
            workspace_id,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_counterexample_value_error(self):
        """
        test_get_counterexample_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_counterexample(**req_copy)



class TestUpdateCounterexample():
    """
    Test Class for update_counterexample
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
    def test_update_counterexample_all_params(self):
        """
        update_counterexample()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'
        new_text = 'testString'
        include_audit = False

        # Invoke method
        response = _service.update_counterexample(
            workspace_id,
            text,
            new_text=new_text,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_update_counterexample_required_params(self):
        """
        test_update_counterexample_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'
        new_text = 'testString'

        # Invoke method
        response = _service.update_counterexample(
            workspace_id,
            text,
            new_text=new_text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_update_counterexample_value_error(self):
        """
        test_update_counterexample_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        mock_response = '{"text": "text", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'
        new_text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_counterexample(**req_copy)



class TestDeleteCounterexample():
    """
    Test Class for delete_counterexample
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
    def test_delete_counterexample_all_params(self):
        """
        delete_counterexample()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.delete_counterexample(
            workspace_id,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_counterexample_value_error(self):
        """
        test_delete_counterexample_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/counterexamples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_counterexample(**req_copy)



# endregion
##############################################################################
# End of Service: Counterexamples
##############################################################################

##############################################################################
# Start of Service: Entities
##############################################################################
# region

class TestListEntities():
    """
    Test Class for list_entities
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
    def test_list_entities_all_params(self):
        """
        list_entities()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        export = False
        page_limit = 38
        include_count = False
        sort = 'entity'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_entities(
            workspace_id,
            export=export,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_entities_required_params(self):
        """
        test_list_entities_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.list_entities(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_entities_value_error(self):
        """
        test_list_entities_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entities": [{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_entities(**req_copy)



class TestCreateEntity():
    """
    Test Class for create_entity
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
    def test_create_entity_all_params(self):
        """
        create_entity()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        description = 'testString'
        metadata = {}
        fuzzy_match = True
        values = [create_value_model]
        include_audit = False

        # Invoke method
        response = _service.create_entity(
            workspace_id,
            entity,
            description=description,
            metadata=metadata,
            fuzzy_match=fuzzy_match,
            values=values,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['entity'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['fuzzy_match'] == True
        assert req_body['values'] == [create_value_model]


    @responses.activate
    def test_create_entity_required_params(self):
        """
        test_create_entity_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        description = 'testString'
        metadata = {}
        fuzzy_match = True
        values = [create_value_model]

        # Invoke method
        response = _service.create_entity(
            workspace_id,
            entity,
            description=description,
            metadata=metadata,
            fuzzy_match=fuzzy_match,
            values=values,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['entity'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['fuzzy_match'] == True
        assert req_body['values'] == [create_value_model]


    @responses.activate
    def test_create_entity_value_error(self):
        """
        test_create_entity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        description = 'testString'
        metadata = {}
        fuzzy_match = True
        values = [create_value_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_entity(**req_copy)



class TestGetEntity():
    """
    Test Class for get_entity
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
    def test_get_entity_all_params(self):
        """
        get_entity()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        export = False
        include_audit = False

        # Invoke method
        response = _service.get_entity(
            workspace_id,
            entity,
            export=export,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_entity_required_params(self):
        """
        test_get_entity_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Invoke method
        response = _service.get_entity(
            workspace_id,
            entity,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_entity_value_error(self):
        """
        test_get_entity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_entity(**req_copy)



class TestUpdateEntity():
    """
    Test Class for update_entity
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
    def test_update_entity_all_params(self):
        """
        update_entity()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        new_entity = 'testString'
        new_description = 'testString'
        new_metadata = {}
        new_fuzzy_match = True
        new_values = [create_value_model]
        append = False
        include_audit = False

        # Invoke method
        response = _service.update_entity(
            workspace_id,
            entity,
            new_entity=new_entity,
            new_description=new_description,
            new_metadata=new_metadata,
            new_fuzzy_match=new_fuzzy_match,
            new_values=new_values,
            append=append,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'append={}'.format('true' if append else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['entity'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['fuzzy_match'] == True
        assert req_body['values'] == [create_value_model]


    @responses.activate
    def test_update_entity_required_params(self):
        """
        test_update_entity_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        new_entity = 'testString'
        new_description = 'testString'
        new_metadata = {}
        new_fuzzy_match = True
        new_values = [create_value_model]

        # Invoke method
        response = _service.update_entity(
            workspace_id,
            entity,
            new_entity=new_entity,
            new_description=new_description,
            new_metadata=new_metadata,
            new_fuzzy_match=new_fuzzy_match,
            new_values=new_values,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['entity'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['fuzzy_match'] == True
        assert req_body['values'] == [create_value_model]


    @responses.activate
    def test_update_entity_value_error(self):
        """
        test_update_entity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        mock_response = '{"entity": "entity", "description": "description", "metadata": {"mapKey": "anyValue"}, "fuzzy_match": false, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CreateValue model
        create_value_model = {}
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        new_entity = 'testString'
        new_description = 'testString'
        new_metadata = {}
        new_fuzzy_match = True
        new_values = [create_value_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_entity(**req_copy)



class TestDeleteEntity():
    """
    Test Class for delete_entity
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
    def test_delete_entity_all_params(self):
        """
        delete_entity()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Invoke method
        response = _service.delete_entity(
            workspace_id,
            entity,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_entity_value_error(self):
        """
        test_delete_entity_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_entity(**req_copy)



# endregion
##############################################################################
# End of Service: Entities
##############################################################################

##############################################################################
# Start of Service: Mentions
##############################################################################
# region

class TestListMentions():
    """
    Test Class for list_mentions
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
    def test_list_mentions_all_params(self):
        """
        list_mentions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/mentions')
        mock_response = '{"examples": [{"text": "text", "intent": "intent", "location": [8]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        export = False
        include_audit = False

        # Invoke method
        response = _service.list_mentions(
            workspace_id,
            entity,
            export=export,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_mentions_required_params(self):
        """
        test_list_mentions_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/mentions')
        mock_response = '{"examples": [{"text": "text", "intent": "intent", "location": [8]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Invoke method
        response = _service.list_mentions(
            workspace_id,
            entity,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_mentions_value_error(self):
        """
        test_list_mentions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/mentions')
        mock_response = '{"examples": [{"text": "text", "intent": "intent", "location": [8]}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_mentions(**req_copy)



# endregion
##############################################################################
# End of Service: Mentions
##############################################################################

##############################################################################
# Start of Service: Values
##############################################################################
# region

class TestListValues():
    """
    Test Class for list_values
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
    def test_list_values_all_params(self):
        """
        list_values()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        export = False
        page_limit = 38
        include_count = False
        sort = 'value'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_values(
            workspace_id,
            entity,
            export=export,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_values_required_params(self):
        """
        test_list_values_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Invoke method
        response = _service.list_values(
            workspace_id,
            entity,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_values_value_error(self):
        """
        test_list_values_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"values": [{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_values(**req_copy)



class TestCreateValue():
    """
    Test Class for create_value
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
    def test_create_value_all_params(self):
        """
        create_value()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        metadata = {}
        type = 'synonyms'
        synonyms = ['testString']
        patterns = ['testString']
        include_audit = False

        # Invoke method
        response = _service.create_value(
            workspace_id,
            entity,
            value,
            metadata=metadata,
            type=type,
            synonyms=synonyms,
            patterns=patterns,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['type'] == 'synonyms'
        assert req_body['synonyms'] == ['testString']
        assert req_body['patterns'] == ['testString']


    @responses.activate
    def test_create_value_required_params(self):
        """
        test_create_value_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        metadata = {}
        type = 'synonyms'
        synonyms = ['testString']
        patterns = ['testString']

        # Invoke method
        response = _service.create_value(
            workspace_id,
            entity,
            value,
            metadata=metadata,
            type=type,
            synonyms=synonyms,
            patterns=patterns,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['type'] == 'synonyms'
        assert req_body['synonyms'] == ['testString']
        assert req_body['patterns'] == ['testString']


    @responses.activate
    def test_create_value_value_error(self):
        """
        test_create_value_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        metadata = {}
        type = 'synonyms'
        synonyms = ['testString']
        patterns = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_value(**req_copy)



class TestGetValue():
    """
    Test Class for get_value
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
    def test_get_value_all_params(self):
        """
        get_value()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        export = False
        include_audit = False

        # Invoke method
        response = _service.get_value(
            workspace_id,
            entity,
            value,
            export=export,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'export={}'.format('true' if export else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_value_required_params(self):
        """
        test_get_value_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Invoke method
        response = _service.get_value(
            workspace_id,
            entity,
            value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_value_value_error(self):
        """
        test_get_value_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_value(**req_copy)



class TestUpdateValue():
    """
    Test Class for update_value
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
    def test_update_value_all_params(self):
        """
        update_value()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        new_value = 'testString'
        new_metadata = {}
        new_type = 'synonyms'
        new_synonyms = ['testString']
        new_patterns = ['testString']
        append = False
        include_audit = False

        # Invoke method
        response = _service.update_value(
            workspace_id,
            entity,
            value,
            new_value=new_value,
            new_metadata=new_metadata,
            new_type=new_type,
            new_synonyms=new_synonyms,
            new_patterns=new_patterns,
            append=append,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'append={}'.format('true' if append else 'false') in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['type'] == 'synonyms'
        assert req_body['synonyms'] == ['testString']
        assert req_body['patterns'] == ['testString']


    @responses.activate
    def test_update_value_required_params(self):
        """
        test_update_value_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        new_value = 'testString'
        new_metadata = {}
        new_type = 'synonyms'
        new_synonyms = ['testString']
        new_patterns = ['testString']

        # Invoke method
        response = _service.update_value(
            workspace_id,
            entity,
            value,
            new_value=new_value,
            new_metadata=new_metadata,
            new_type=new_type,
            new_synonyms=new_synonyms,
            new_patterns=new_patterns,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['value'] == 'testString'
        assert req_body['metadata'] == {}
        assert req_body['type'] == 'synonyms'
        assert req_body['synonyms'] == ['testString']
        assert req_body['patterns'] == ['testString']


    @responses.activate
    def test_update_value_value_error(self):
        """
        test_update_value_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        mock_response = '{"value": "value", "metadata": {"mapKey": "anyValue"}, "type": "synonyms", "synonyms": ["synonym"], "patterns": ["pattern"], "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        new_value = 'testString'
        new_metadata = {}
        new_type = 'synonyms'
        new_synonyms = ['testString']
        new_patterns = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_value(**req_copy)



class TestDeleteValue():
    """
    Test Class for delete_value
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
    def test_delete_value_all_params(self):
        """
        delete_value()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Invoke method
        response = _service.delete_value(
            workspace_id,
            entity,
            value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_value_value_error(self):
        """
        test_delete_value_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_value(**req_copy)



# endregion
##############################################################################
# End of Service: Values
##############################################################################

##############################################################################
# Start of Service: Synonyms
##############################################################################
# region

class TestListSynonyms():
    """
    Test Class for list_synonyms
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
    def test_list_synonyms_all_params(self):
        """
        list_synonyms()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonyms": [{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        page_limit = 38
        include_count = False
        sort = 'synonym'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_synonyms(
            workspace_id,
            entity,
            value,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_synonyms_required_params(self):
        """
        test_list_synonyms_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonyms": [{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Invoke method
        response = _service.list_synonyms(
            workspace_id,
            entity,
            value,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_synonyms_value_error(self):
        """
        test_list_synonyms_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonyms": [{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_synonyms(**req_copy)



class TestCreateSynonym():
    """
    Test Class for create_synonym
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
    def test_create_synonym_all_params(self):
        """
        create_synonym()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'
        include_audit = False

        # Invoke method
        response = _service.create_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['synonym'] == 'testString'


    @responses.activate
    def test_create_synonym_required_params(self):
        """
        test_create_synonym_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Invoke method
        response = _service.create_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['synonym'] == 'testString'


    @responses.activate
    def test_create_synonym_value_error(self):
        """
        test_create_synonym_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
            "synonym": synonym,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_synonym(**req_copy)



class TestGetSynonym():
    """
    Test Class for get_synonym
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
    def test_get_synonym_all_params(self):
        """
        get_synonym()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_synonym_required_params(self):
        """
        test_get_synonym_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Invoke method
        response = _service.get_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_synonym_value_error(self):
        """
        test_get_synonym_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
            "synonym": synonym,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_synonym(**req_copy)



class TestUpdateSynonym():
    """
    Test Class for update_synonym
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
    def test_update_synonym_all_params(self):
        """
        update_synonym()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'
        new_synonym = 'testString'
        include_audit = False

        # Invoke method
        response = _service.update_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            new_synonym=new_synonym,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['synonym'] == 'testString'


    @responses.activate
    def test_update_synonym_required_params(self):
        """
        test_update_synonym_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'
        new_synonym = 'testString'

        # Invoke method
        response = _service.update_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            new_synonym=new_synonym,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['synonym'] == 'testString'


    @responses.activate
    def test_update_synonym_value_error(self):
        """
        test_update_synonym_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        mock_response = '{"synonym": "synonym", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'
        new_synonym = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
            "synonym": synonym,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_synonym(**req_copy)



class TestDeleteSynonym():
    """
    Test Class for delete_synonym
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
    def test_delete_synonym_all_params(self):
        """
        delete_synonym()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Invoke method
        response = _service.delete_synonym(
            workspace_id,
            entity,
            value,
            synonym,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_synonym_value_error(self):
        """
        test_delete_synonym_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/entities/testString/values/testString/synonyms/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        entity = 'testString'
        value = 'testString'
        synonym = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "entity": entity,
            "value": value,
            "synonym": synonym,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_synonym(**req_copy)



# endregion
##############################################################################
# End of Service: Synonyms
##############################################################################

##############################################################################
# Start of Service: DialogNodes
##############################################################################
# region

class TestListDialogNodes():
    """
    Test Class for list_dialog_nodes
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
    def test_list_dialog_nodes_all_params(self):
        """
        list_dialog_nodes()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        page_limit = 38
        include_count = False
        sort = 'dialog_node'
        cursor = 'testString'
        include_audit = False

        # Invoke method
        response = _service.list_dialog_nodes(
            workspace_id,
            page_limit=page_limit,
            include_count=include_count,
            sort=sort,
            cursor=cursor,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'include_count={}'.format('true' if include_count else 'false') in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'cursor={}'.format(cursor) in query_string
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_list_dialog_nodes_required_params(self):
        """
        test_list_dialog_nodes_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.list_dialog_nodes(
            workspace_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_dialog_nodes_value_error(self):
        """
        test_list_dialog_nodes_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_nodes": [{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}], "pagination": {"refresh_url": "refresh_url", "next_url": "next_url", "total": 5, "matched": 7, "refresh_cursor": "refresh_cursor", "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_dialog_nodes(**req_copy)



class TestCreateDialogNode():
    """
    Test Class for create_dialog_node
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
    def test_create_dialog_node_all_params(self):
        """
        create_dialog_node()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        description = 'testString'
        conditions = 'testString'
        parent = 'testString'
        previous_sibling = 'testString'
        output = dialog_node_output_model
        context = dialog_node_context_model
        metadata = {}
        next_step = dialog_node_next_step_model
        title = 'testString'
        type = 'standard'
        event_name = 'focus'
        variable = 'testString'
        actions = [dialog_node_action_model]
        digress_in = 'not_available'
        digress_out = 'allow_returning'
        digress_out_slots = 'not_allowed'
        user_label = 'testString'
        disambiguation_opt_out = False
        include_audit = False

        # Invoke method
        response = _service.create_dialog_node(
            workspace_id,
            dialog_node,
            description=description,
            conditions=conditions,
            parent=parent,
            previous_sibling=previous_sibling,
            output=output,
            context=context,
            metadata=metadata,
            next_step=next_step,
            title=title,
            type=type,
            event_name=event_name,
            variable=variable,
            actions=actions,
            digress_in=digress_in,
            digress_out=digress_out,
            digress_out_slots=digress_out_slots,
            user_label=user_label,
            disambiguation_opt_out=disambiguation_opt_out,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['dialog_node'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conditions'] == 'testString'
        assert req_body['parent'] == 'testString'
        assert req_body['previous_sibling'] == 'testString'
        assert req_body['output'] == dialog_node_output_model
        assert req_body['context'] == dialog_node_context_model
        assert req_body['metadata'] == {}
        assert req_body['next_step'] == dialog_node_next_step_model
        assert req_body['title'] == 'testString'
        assert req_body['type'] == 'standard'
        assert req_body['event_name'] == 'focus'
        assert req_body['variable'] == 'testString'
        assert req_body['actions'] == [dialog_node_action_model]
        assert req_body['digress_in'] == 'not_available'
        assert req_body['digress_out'] == 'allow_returning'
        assert req_body['digress_out_slots'] == 'not_allowed'
        assert req_body['user_label'] == 'testString'
        assert req_body['disambiguation_opt_out'] == False


    @responses.activate
    def test_create_dialog_node_required_params(self):
        """
        test_create_dialog_node_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        description = 'testString'
        conditions = 'testString'
        parent = 'testString'
        previous_sibling = 'testString'
        output = dialog_node_output_model
        context = dialog_node_context_model
        metadata = {}
        next_step = dialog_node_next_step_model
        title = 'testString'
        type = 'standard'
        event_name = 'focus'
        variable = 'testString'
        actions = [dialog_node_action_model]
        digress_in = 'not_available'
        digress_out = 'allow_returning'
        digress_out_slots = 'not_allowed'
        user_label = 'testString'
        disambiguation_opt_out = False

        # Invoke method
        response = _service.create_dialog_node(
            workspace_id,
            dialog_node,
            description=description,
            conditions=conditions,
            parent=parent,
            previous_sibling=previous_sibling,
            output=output,
            context=context,
            metadata=metadata,
            next_step=next_step,
            title=title,
            type=type,
            event_name=event_name,
            variable=variable,
            actions=actions,
            digress_in=digress_in,
            digress_out=digress_out,
            digress_out_slots=digress_out_slots,
            user_label=user_label,
            disambiguation_opt_out=disambiguation_opt_out,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['dialog_node'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conditions'] == 'testString'
        assert req_body['parent'] == 'testString'
        assert req_body['previous_sibling'] == 'testString'
        assert req_body['output'] == dialog_node_output_model
        assert req_body['context'] == dialog_node_context_model
        assert req_body['metadata'] == {}
        assert req_body['next_step'] == dialog_node_next_step_model
        assert req_body['title'] == 'testString'
        assert req_body['type'] == 'standard'
        assert req_body['event_name'] == 'focus'
        assert req_body['variable'] == 'testString'
        assert req_body['actions'] == [dialog_node_action_model]
        assert req_body['digress_in'] == 'not_available'
        assert req_body['digress_out'] == 'allow_returning'
        assert req_body['digress_out_slots'] == 'not_allowed'
        assert req_body['user_label'] == 'testString'
        assert req_body['disambiguation_opt_out'] == False


    @responses.activate
    def test_create_dialog_node_value_error(self):
        """
        test_create_dialog_node_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        description = 'testString'
        conditions = 'testString'
        parent = 'testString'
        previous_sibling = 'testString'
        output = dialog_node_output_model
        context = dialog_node_context_model
        metadata = {}
        next_step = dialog_node_next_step_model
        title = 'testString'
        type = 'standard'
        event_name = 'focus'
        variable = 'testString'
        actions = [dialog_node_action_model]
        digress_in = 'not_available'
        digress_out = 'allow_returning'
        digress_out_slots = 'not_allowed'
        user_label = 'testString'
        disambiguation_opt_out = False

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "dialog_node": dialog_node,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_dialog_node(**req_copy)



class TestGetDialogNode():
    """
    Test Class for get_dialog_node
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
    def test_get_dialog_node_all_params(self):
        """
        get_dialog_node()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        include_audit = False

        # Invoke method
        response = _service.get_dialog_node(
            workspace_id,
            dialog_node,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string


    @responses.activate
    def test_get_dialog_node_required_params(self):
        """
        test_get_dialog_node_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'

        # Invoke method
        response = _service.get_dialog_node(
            workspace_id,
            dialog_node,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_dialog_node_value_error(self):
        """
        test_get_dialog_node_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "dialog_node": dialog_node,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_dialog_node(**req_copy)



class TestUpdateDialogNode():
    """
    Test Class for update_dialog_node
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
    def test_update_dialog_node_all_params(self):
        """
        update_dialog_node()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        new_dialog_node = 'testString'
        new_description = 'testString'
        new_conditions = 'testString'
        new_parent = 'testString'
        new_previous_sibling = 'testString'
        new_output = dialog_node_output_model
        new_context = dialog_node_context_model
        new_metadata = {}
        new_next_step = dialog_node_next_step_model
        new_title = 'testString'
        new_type = 'standard'
        new_event_name = 'focus'
        new_variable = 'testString'
        new_actions = [dialog_node_action_model]
        new_digress_in = 'not_available'
        new_digress_out = 'allow_returning'
        new_digress_out_slots = 'not_allowed'
        new_user_label = 'testString'
        new_disambiguation_opt_out = False
        include_audit = False

        # Invoke method
        response = _service.update_dialog_node(
            workspace_id,
            dialog_node,
            new_dialog_node=new_dialog_node,
            new_description=new_description,
            new_conditions=new_conditions,
            new_parent=new_parent,
            new_previous_sibling=new_previous_sibling,
            new_output=new_output,
            new_context=new_context,
            new_metadata=new_metadata,
            new_next_step=new_next_step,
            new_title=new_title,
            new_type=new_type,
            new_event_name=new_event_name,
            new_variable=new_variable,
            new_actions=new_actions,
            new_digress_in=new_digress_in,
            new_digress_out=new_digress_out,
            new_digress_out_slots=new_digress_out_slots,
            new_user_label=new_user_label,
            new_disambiguation_opt_out=new_disambiguation_opt_out,
            include_audit=include_audit,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'include_audit={}'.format('true' if include_audit else 'false') in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['dialog_node'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conditions'] == 'testString'
        assert req_body['parent'] == 'testString'
        assert req_body['previous_sibling'] == 'testString'
        assert req_body['output'] == dialog_node_output_model
        assert req_body['context'] == dialog_node_context_model
        assert req_body['metadata'] == {}
        assert req_body['next_step'] == dialog_node_next_step_model
        assert req_body['title'] == 'testString'
        assert req_body['type'] == 'standard'
        assert req_body['event_name'] == 'focus'
        assert req_body['variable'] == 'testString'
        assert req_body['actions'] == [dialog_node_action_model]
        assert req_body['digress_in'] == 'not_available'
        assert req_body['digress_out'] == 'allow_returning'
        assert req_body['digress_out_slots'] == 'not_allowed'
        assert req_body['user_label'] == 'testString'
        assert req_body['disambiguation_opt_out'] == False


    @responses.activate
    def test_update_dialog_node_required_params(self):
        """
        test_update_dialog_node_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        new_dialog_node = 'testString'
        new_description = 'testString'
        new_conditions = 'testString'
        new_parent = 'testString'
        new_previous_sibling = 'testString'
        new_output = dialog_node_output_model
        new_context = dialog_node_context_model
        new_metadata = {}
        new_next_step = dialog_node_next_step_model
        new_title = 'testString'
        new_type = 'standard'
        new_event_name = 'focus'
        new_variable = 'testString'
        new_actions = [dialog_node_action_model]
        new_digress_in = 'not_available'
        new_digress_out = 'allow_returning'
        new_digress_out_slots = 'not_allowed'
        new_user_label = 'testString'
        new_disambiguation_opt_out = False

        # Invoke method
        response = _service.update_dialog_node(
            workspace_id,
            dialog_node,
            new_dialog_node=new_dialog_node,
            new_description=new_description,
            new_conditions=new_conditions,
            new_parent=new_parent,
            new_previous_sibling=new_previous_sibling,
            new_output=new_output,
            new_context=new_context,
            new_metadata=new_metadata,
            new_next_step=new_next_step,
            new_title=new_title,
            new_type=new_type,
            new_event_name=new_event_name,
            new_variable=new_variable,
            new_actions=new_actions,
            new_digress_in=new_digress_in,
            new_digress_out=new_digress_out,
            new_digress_out_slots=new_digress_out_slots,
            new_user_label=new_user_label,
            new_disambiguation_opt_out=new_disambiguation_opt_out,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['dialog_node'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conditions'] == 'testString'
        assert req_body['parent'] == 'testString'
        assert req_body['previous_sibling'] == 'testString'
        assert req_body['output'] == dialog_node_output_model
        assert req_body['context'] == dialog_node_context_model
        assert req_body['metadata'] == {}
        assert req_body['next_step'] == dialog_node_next_step_model
        assert req_body['title'] == 'testString'
        assert req_body['type'] == 'standard'
        assert req_body['event_name'] == 'focus'
        assert req_body['variable'] == 'testString'
        assert req_body['actions'] == [dialog_node_action_model]
        assert req_body['digress_in'] == 'not_available'
        assert req_body['digress_out'] == 'allow_returning'
        assert req_body['digress_out_slots'] == 'not_allowed'
        assert req_body['user_label'] == 'testString'
        assert req_body['disambiguation_opt_out'] == False


    @responses.activate
    def test_update_dialog_node_value_error(self):
        """
        test_update_dialog_node_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        mock_response = '{"dialog_node": "dialog_node", "description": "description", "conditions": "conditions", "parent": "parent", "previous_sibling": "previous_sibling", "output": {"generic": [{"response_type": "channel_transfer", "message_to_user": "message_to_user", "transfer_info": {"target": {"chat": {"url": "url"}}}, "channels": [{"channel": "chat"}]}], "integrations": {"mapKey": {"mapKey": "anyValue"}}, "modifiers": {"overwrite": true}}, "context": {"integrations": {"mapKey": {"mapKey": "anyValue"}}}, "metadata": {"mapKey": "anyValue"}, "next_step": {"behavior": "get_user_input", "dialog_node": "dialog_node", "selector": "condition"}, "title": "title", "type": "standard", "event_name": "focus", "variable": "variable", "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "digress_in": "not_available", "digress_out": "allow_returning", "digress_out_slots": "not_allowed", "user_label": "user_label", "disambiguation_opt_out": false, "disabled": true, "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ChannelTransferTargetChat model
        channel_transfer_target_chat_model = {}
        channel_transfer_target_chat_model['url'] = 'testString'

        # Construct a dict representation of a ChannelTransferTarget model
        channel_transfer_target_model = {}
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        # Construct a dict representation of a ChannelTransferInfo model
        channel_transfer_info_model = {}
        channel_transfer_info_model['target'] = channel_transfer_target_model

        # Construct a dict representation of a ResponseGenericChannel model
        response_generic_channel_model = {}
        response_generic_channel_model['channel'] = 'chat'

        # Construct a dict representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_model = {}
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        # Construct a dict representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model = {}
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a dict representation of a DialogNodeOutput model
        dialog_node_output_model = {}
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeContext model
        dialog_node_context_model = {}
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        # Construct a dict representation of a DialogNodeNextStep model
        dialog_node_next_step_model = {}
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        # Construct a dict representation of a DialogNodeAction model
        dialog_node_action_model = {}
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'
        new_dialog_node = 'testString'
        new_description = 'testString'
        new_conditions = 'testString'
        new_parent = 'testString'
        new_previous_sibling = 'testString'
        new_output = dialog_node_output_model
        new_context = dialog_node_context_model
        new_metadata = {}
        new_next_step = dialog_node_next_step_model
        new_title = 'testString'
        new_type = 'standard'
        new_event_name = 'focus'
        new_variable = 'testString'
        new_actions = [dialog_node_action_model]
        new_digress_in = 'not_available'
        new_digress_out = 'allow_returning'
        new_digress_out_slots = 'not_allowed'
        new_user_label = 'testString'
        new_disambiguation_opt_out = False

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "dialog_node": dialog_node,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_dialog_node(**req_copy)



class TestDeleteDialogNode():
    """
    Test Class for delete_dialog_node
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
    def test_delete_dialog_node_all_params(self):
        """
        delete_dialog_node()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'

        # Invoke method
        response = _service.delete_dialog_node(
            workspace_id,
            dialog_node,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_dialog_node_value_error(self):
        """
        test_delete_dialog_node_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/dialog_nodes/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        dialog_node = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
            "dialog_node": dialog_node,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_dialog_node(**req_copy)



# endregion
##############################################################################
# End of Service: DialogNodes
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'
        sort = 'testString'
        filter = 'testString'
        page_limit = 38
        cursor = 'testString'

        # Invoke method
        response = _service.list_logs(
            workspace_id,
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Invoke method
        response = _service.list_logs(
            workspace_id,
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
        url = self.preprocess_url(_base_url + '/v1/workspaces/testString/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        workspace_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "workspace_id": workspace_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_logs(**req_copy)



class TestListAllLogs():
    """
    Test Class for list_all_logs
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
    def test_list_all_logs_all_params(self):
        """
        list_all_logs()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        filter = 'testString'
        sort = 'testString'
        page_limit = 38
        cursor = 'testString'

        # Invoke method
        response = _service.list_all_logs(
            filter,
            sort=sort,
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
        assert 'filter={}'.format(filter) in query_string
        assert 'sort={}'.format(sort) in query_string
        assert 'page_limit={}'.format(page_limit) in query_string
        assert 'cursor={}'.format(cursor) in query_string


    @responses.activate
    def test_list_all_logs_required_params(self):
        """
        test_list_all_logs_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        filter = 'testString'

        # Invoke method
        response = _service.list_all_logs(
            filter,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string


    @responses.activate
    def test_list_all_logs_value_error(self):
        """
        test_list_all_logs_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"logs": [{"request": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "response": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}], "alternate_intents": false, "context": {"conversation_id": "conversation_id", "system": {"mapKey": "anyValue"}, "metadata": {"deployment": "deployment", "user_id": "user_id"}}, "output": {"nodes_visited": ["nodes_visited"], "nodes_visited_details": [{"dialog_node": "dialog_node", "title": "title", "conditions": "conditions"}], "log_messages": [{"level": "info", "msg": "msg", "code": "code", "source": {"type": "dialog_node", "dialog_node": "dialog_node"}}], "text": ["text"], "generic": [{"response_type": "option", "title": "title", "description": "description", "preference": "dropdown", "options": [{"label": "label", "value": {"input": {"text": "text", "spelling_suggestions": false, "spelling_auto_correct": false, "suggested_text": "suggested_text", "original_text": "original_text"}, "intents": [{"intent": "intent", "confidence": 10}], "entities": [{"entity": "entity", "location": [8], "value": "value", "confidence": 10, "metadata": {"mapKey": "anyValue"}, "groups": [{"group": "group", "location": [8]}], "interpretation": {"calendar_type": "calendar_type", "datetime_link": "datetime_link", "festival": "festival", "granularity": "day", "range_link": "range_link", "range_modifier": "range_modifier", "relative_day": 12, "relative_month": 14, "relative_week": 13, "relative_weekend": 16, "relative_year": 13, "specific_day": 12, "specific_day_of_week": "specific_day_of_week", "specific_month": 14, "specific_quarter": 16, "specific_year": 13, "numeric_value": 13, "subtype": "subtype", "part_of_day": "part_of_day", "relative_hour": 13, "relative_minute": 15, "relative_second": 15, "specific_hour": 13, "specific_minute": 15, "specific_second": 15, "timezone": "timezone"}, "alternatives": [{"value": "value", "confidence": 10}], "role": {"type": "date_from"}}]}}], "channels": [{"channel": "chat"}]}]}, "actions": [{"name": "name", "type": "client", "parameters": {"mapKey": "anyValue"}, "result_variable": "result_variable", "credentials": "credentials"}], "user_id": "user_id"}, "log_id": "log_id", "request_timestamp": "request_timestamp", "response_timestamp": "response_timestamp", "workspace_id": "workspace_id", "language": "language"}], "pagination": {"next_url": "next_url", "matched": 7, "next_cursor": "next_cursor"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        filter = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "filter": filter,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_all_logs(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v1/user_data')
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
        url = self.preprocess_url(_base_url + '/v1/user_data')
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

class TestModel_Context():
    """
    Test Class for Context
    """

    def test_context_serialization(self):
        """
        Test serialization/deserialization for Context
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_context_metadata_model = {} # MessageContextMetadata
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        # Construct a json representation of a Context model
        context_model_json = {}
        context_model_json['conversation_id'] = 'testString'
        context_model_json['system'] = {}
        context_model_json['metadata'] = message_context_metadata_model
        context_model_json['foo'] = 'testString'

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model = Context.from_dict(context_model_json)
        assert context_model != False

        # Construct a model instance of Context by calling from_dict on the json representation
        context_model_dict = Context.from_dict(context_model_json).__dict__
        context_model2 = Context(**context_model_dict)

        # Verify the model instances are equivalent
        assert context_model == context_model2

        # Convert model instance back to dict and verify no loss of data
        context_model_json2 = context_model.to_dict()
        assert context_model_json2 == context_model_json

        # Test get_properties and set_properties methods.
        context_model.set_properties({})
        actual_dict = context_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        context_model.set_properties(expected_dict)
        actual_dict = context_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_Counterexample():
    """
    Test Class for Counterexample
    """

    def test_counterexample_serialization(self):
        """
        Test serialization/deserialization for Counterexample
        """

        # Construct a json representation of a Counterexample model
        counterexample_model_json = {}
        counterexample_model_json['text'] = 'testString'
        counterexample_model_json['created'] = "2019-01-01T12:00:00Z"
        counterexample_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Counterexample by calling from_dict on the json representation
        counterexample_model = Counterexample.from_dict(counterexample_model_json)
        assert counterexample_model != False

        # Construct a model instance of Counterexample by calling from_dict on the json representation
        counterexample_model_dict = Counterexample.from_dict(counterexample_model_json).__dict__
        counterexample_model2 = Counterexample(**counterexample_model_dict)

        # Verify the model instances are equivalent
        assert counterexample_model == counterexample_model2

        # Convert model instance back to dict and verify no loss of data
        counterexample_model_json2 = counterexample_model.to_dict()
        assert counterexample_model_json2 == counterexample_model_json

class TestModel_CounterexampleCollection():
    """
    Test Class for CounterexampleCollection
    """

    def test_counterexample_collection_serialization(self):
        """
        Test serialization/deserialization for CounterexampleCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        counterexample_model = {} # Counterexample
        counterexample_model['text'] = 'testString'
        counterexample_model['created'] = "2019-01-01T12:00:00Z"
        counterexample_model['updated'] = "2019-01-01T12:00:00Z"

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a CounterexampleCollection model
        counterexample_collection_model_json = {}
        counterexample_collection_model_json['counterexamples'] = [counterexample_model]
        counterexample_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of CounterexampleCollection by calling from_dict on the json representation
        counterexample_collection_model = CounterexampleCollection.from_dict(counterexample_collection_model_json)
        assert counterexample_collection_model != False

        # Construct a model instance of CounterexampleCollection by calling from_dict on the json representation
        counterexample_collection_model_dict = CounterexampleCollection.from_dict(counterexample_collection_model_json).__dict__
        counterexample_collection_model2 = CounterexampleCollection(**counterexample_collection_model_dict)

        # Verify the model instances are equivalent
        assert counterexample_collection_model == counterexample_collection_model2

        # Convert model instance back to dict and verify no loss of data
        counterexample_collection_model_json2 = counterexample_collection_model.to_dict()
        assert counterexample_collection_model_json2 == counterexample_collection_model_json

class TestModel_CreateEntity():
    """
    Test Class for CreateEntity
    """

    def test_create_entity_serialization(self):
        """
        Test serialization/deserialization for CreateEntity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        create_value_model = {} # CreateValue
        create_value_model['value'] = 'testString'
        create_value_model['metadata'] = {}
        create_value_model['type'] = 'synonyms'
        create_value_model['synonyms'] = ['testString']
        create_value_model['patterns'] = ['testString']
        create_value_model['created'] = "2019-01-01T12:00:00Z"
        create_value_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a CreateEntity model
        create_entity_model_json = {}
        create_entity_model_json['entity'] = 'testString'
        create_entity_model_json['description'] = 'testString'
        create_entity_model_json['metadata'] = {}
        create_entity_model_json['fuzzy_match'] = True
        create_entity_model_json['created'] = "2019-01-01T12:00:00Z"
        create_entity_model_json['updated'] = "2019-01-01T12:00:00Z"
        create_entity_model_json['values'] = [create_value_model]

        # Construct a model instance of CreateEntity by calling from_dict on the json representation
        create_entity_model = CreateEntity.from_dict(create_entity_model_json)
        assert create_entity_model != False

        # Construct a model instance of CreateEntity by calling from_dict on the json representation
        create_entity_model_dict = CreateEntity.from_dict(create_entity_model_json).__dict__
        create_entity_model2 = CreateEntity(**create_entity_model_dict)

        # Verify the model instances are equivalent
        assert create_entity_model == create_entity_model2

        # Convert model instance back to dict and verify no loss of data
        create_entity_model_json2 = create_entity_model.to_dict()
        assert create_entity_model_json2 == create_entity_model_json

class TestModel_CreateIntent():
    """
    Test Class for CreateIntent
    """

    def test_create_intent_serialization(self):
        """
        Test serialization/deserialization for CreateIntent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a CreateIntent model
        create_intent_model_json = {}
        create_intent_model_json['intent'] = 'testString'
        create_intent_model_json['description'] = 'testString'
        create_intent_model_json['created'] = "2019-01-01T12:00:00Z"
        create_intent_model_json['updated'] = "2019-01-01T12:00:00Z"
        create_intent_model_json['examples'] = [example_model]

        # Construct a model instance of CreateIntent by calling from_dict on the json representation
        create_intent_model = CreateIntent.from_dict(create_intent_model_json)
        assert create_intent_model != False

        # Construct a model instance of CreateIntent by calling from_dict on the json representation
        create_intent_model_dict = CreateIntent.from_dict(create_intent_model_json).__dict__
        create_intent_model2 = CreateIntent(**create_intent_model_dict)

        # Verify the model instances are equivalent
        assert create_intent_model == create_intent_model2

        # Convert model instance back to dict and verify no loss of data
        create_intent_model_json2 = create_intent_model.to_dict()
        assert create_intent_model_json2 == create_intent_model_json

class TestModel_CreateValue():
    """
    Test Class for CreateValue
    """

    def test_create_value_serialization(self):
        """
        Test serialization/deserialization for CreateValue
        """

        # Construct a json representation of a CreateValue model
        create_value_model_json = {}
        create_value_model_json['value'] = 'testString'
        create_value_model_json['metadata'] = {}
        create_value_model_json['type'] = 'synonyms'
        create_value_model_json['synonyms'] = ['testString']
        create_value_model_json['patterns'] = ['testString']
        create_value_model_json['created'] = "2019-01-01T12:00:00Z"
        create_value_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of CreateValue by calling from_dict on the json representation
        create_value_model = CreateValue.from_dict(create_value_model_json)
        assert create_value_model != False

        # Construct a model instance of CreateValue by calling from_dict on the json representation
        create_value_model_dict = CreateValue.from_dict(create_value_model_json).__dict__
        create_value_model2 = CreateValue(**create_value_model_dict)

        # Verify the model instances are equivalent
        assert create_value_model == create_value_model2

        # Convert model instance back to dict and verify no loss of data
        create_value_model_json2 = create_value_model.to_dict()
        assert create_value_model_json2 == create_value_model_json

class TestModel_DialogNode():
    """
    Test Class for DialogNode
    """

    def test_dialog_node_serialization(self):
        """
        Test serialization/deserialization for DialogNode
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        dialog_node_output_generic_model = {} # DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_output_modifiers_model = {} # DialogNodeOutputModifiers
        dialog_node_output_modifiers_model['overwrite'] = True

        dialog_node_output_model = {} # DialogNodeOutput
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        dialog_node_context_model = {} # DialogNodeContext
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        dialog_node_next_step_model = {} # DialogNodeNextStep
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Construct a json representation of a DialogNode model
        dialog_node_model_json = {}
        dialog_node_model_json['dialog_node'] = 'testString'
        dialog_node_model_json['description'] = 'testString'
        dialog_node_model_json['conditions'] = 'testString'
        dialog_node_model_json['parent'] = 'testString'
        dialog_node_model_json['previous_sibling'] = 'testString'
        dialog_node_model_json['output'] = dialog_node_output_model
        dialog_node_model_json['context'] = dialog_node_context_model
        dialog_node_model_json['metadata'] = {}
        dialog_node_model_json['next_step'] = dialog_node_next_step_model
        dialog_node_model_json['title'] = 'testString'
        dialog_node_model_json['type'] = 'standard'
        dialog_node_model_json['event_name'] = 'focus'
        dialog_node_model_json['variable'] = 'testString'
        dialog_node_model_json['actions'] = [dialog_node_action_model]
        dialog_node_model_json['digress_in'] = 'not_available'
        dialog_node_model_json['digress_out'] = 'allow_returning'
        dialog_node_model_json['digress_out_slots'] = 'not_allowed'
        dialog_node_model_json['user_label'] = 'testString'
        dialog_node_model_json['disambiguation_opt_out'] = False
        dialog_node_model_json['disabled'] = True
        dialog_node_model_json['created'] = "2019-01-01T12:00:00Z"
        dialog_node_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of DialogNode by calling from_dict on the json representation
        dialog_node_model = DialogNode.from_dict(dialog_node_model_json)
        assert dialog_node_model != False

        # Construct a model instance of DialogNode by calling from_dict on the json representation
        dialog_node_model_dict = DialogNode.from_dict(dialog_node_model_json).__dict__
        dialog_node_model2 = DialogNode(**dialog_node_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_model == dialog_node_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_model_json2 = dialog_node_model.to_dict()
        assert dialog_node_model_json2 == dialog_node_model_json

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

class TestModel_DialogNodeCollection():
    """
    Test Class for DialogNodeCollection
    """

    def test_dialog_node_collection_serialization(self):
        """
        Test serialization/deserialization for DialogNodeCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        dialog_node_output_generic_model = {} # DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_output_modifiers_model = {} # DialogNodeOutputModifiers
        dialog_node_output_modifiers_model['overwrite'] = True

        dialog_node_output_model = {} # DialogNodeOutput
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        dialog_node_context_model = {} # DialogNodeContext
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        dialog_node_next_step_model = {} # DialogNodeNextStep
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_model = {} # DialogNode
        dialog_node_model['dialog_node'] = 'testString'
        dialog_node_model['description'] = 'testString'
        dialog_node_model['conditions'] = 'testString'
        dialog_node_model['parent'] = 'testString'
        dialog_node_model['previous_sibling'] = 'testString'
        dialog_node_model['output'] = dialog_node_output_model
        dialog_node_model['context'] = dialog_node_context_model
        dialog_node_model['metadata'] = {}
        dialog_node_model['next_step'] = dialog_node_next_step_model
        dialog_node_model['title'] = 'testString'
        dialog_node_model['type'] = 'standard'
        dialog_node_model['event_name'] = 'focus'
        dialog_node_model['variable'] = 'testString'
        dialog_node_model['actions'] = [dialog_node_action_model]
        dialog_node_model['digress_in'] = 'not_available'
        dialog_node_model['digress_out'] = 'allow_returning'
        dialog_node_model['digress_out_slots'] = 'not_allowed'
        dialog_node_model['user_label'] = 'testString'
        dialog_node_model['disambiguation_opt_out'] = False
        dialog_node_model['disabled'] = True
        dialog_node_model['created'] = "2019-01-01T12:00:00Z"
        dialog_node_model['updated'] = "2019-01-01T12:00:00Z"

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a DialogNodeCollection model
        dialog_node_collection_model_json = {}
        dialog_node_collection_model_json['dialog_nodes'] = [dialog_node_model]
        dialog_node_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of DialogNodeCollection by calling from_dict on the json representation
        dialog_node_collection_model = DialogNodeCollection.from_dict(dialog_node_collection_model_json)
        assert dialog_node_collection_model != False

        # Construct a model instance of DialogNodeCollection by calling from_dict on the json representation
        dialog_node_collection_model_dict = DialogNodeCollection.from_dict(dialog_node_collection_model_json).__dict__
        dialog_node_collection_model2 = DialogNodeCollection(**dialog_node_collection_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_collection_model == dialog_node_collection_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_collection_model_json2 = dialog_node_collection_model.to_dict()
        assert dialog_node_collection_model_json2 == dialog_node_collection_model_json

class TestModel_DialogNodeContext():
    """
    Test Class for DialogNodeContext
    """

    def test_dialog_node_context_serialization(self):
        """
        Test serialization/deserialization for DialogNodeContext
        """

        # Construct a json representation of a DialogNodeContext model
        dialog_node_context_model_json = {}
        dialog_node_context_model_json['integrations'] = {}
        dialog_node_context_model_json['foo'] = 'testString'

        # Construct a model instance of DialogNodeContext by calling from_dict on the json representation
        dialog_node_context_model = DialogNodeContext.from_dict(dialog_node_context_model_json)
        assert dialog_node_context_model != False

        # Construct a model instance of DialogNodeContext by calling from_dict on the json representation
        dialog_node_context_model_dict = DialogNodeContext.from_dict(dialog_node_context_model_json).__dict__
        dialog_node_context_model2 = DialogNodeContext(**dialog_node_context_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_context_model == dialog_node_context_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_context_model_json2 = dialog_node_context_model.to_dict()
        assert dialog_node_context_model_json2 == dialog_node_context_model_json

        # Test get_properties and set_properties methods.
        dialog_node_context_model.set_properties({})
        actual_dict = dialog_node_context_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        dialog_node_context_model.set_properties(expected_dict)
        actual_dict = dialog_node_context_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_DialogNodeNextStep():
    """
    Test Class for DialogNodeNextStep
    """

    def test_dialog_node_next_step_serialization(self):
        """
        Test serialization/deserialization for DialogNodeNextStep
        """

        # Construct a json representation of a DialogNodeNextStep model
        dialog_node_next_step_model_json = {}
        dialog_node_next_step_model_json['behavior'] = 'get_user_input'
        dialog_node_next_step_model_json['dialog_node'] = 'testString'
        dialog_node_next_step_model_json['selector'] = 'condition'

        # Construct a model instance of DialogNodeNextStep by calling from_dict on the json representation
        dialog_node_next_step_model = DialogNodeNextStep.from_dict(dialog_node_next_step_model_json)
        assert dialog_node_next_step_model != False

        # Construct a model instance of DialogNodeNextStep by calling from_dict on the json representation
        dialog_node_next_step_model_dict = DialogNodeNextStep.from_dict(dialog_node_next_step_model_json).__dict__
        dialog_node_next_step_model2 = DialogNodeNextStep(**dialog_node_next_step_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_next_step_model == dialog_node_next_step_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_next_step_model_json2 = dialog_node_next_step_model.to_dict()
        assert dialog_node_next_step_model_json2 == dialog_node_next_step_model_json

class TestModel_DialogNodeOutput():
    """
    Test Class for DialogNodeOutput
    """

    def test_dialog_node_output_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutput
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        dialog_node_output_generic_model = {} # DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_output_modifiers_model = {} # DialogNodeOutputModifiers
        dialog_node_output_modifiers_model['overwrite'] = True

        # Construct a json representation of a DialogNodeOutput model
        dialog_node_output_model_json = {}
        dialog_node_output_model_json['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model_json['integrations'] = {}
        dialog_node_output_model_json['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model_json['foo'] = 'testString'

        # Construct a model instance of DialogNodeOutput by calling from_dict on the json representation
        dialog_node_output_model = DialogNodeOutput.from_dict(dialog_node_output_model_json)
        assert dialog_node_output_model != False

        # Construct a model instance of DialogNodeOutput by calling from_dict on the json representation
        dialog_node_output_model_dict = DialogNodeOutput.from_dict(dialog_node_output_model_json).__dict__
        dialog_node_output_model2 = DialogNodeOutput(**dialog_node_output_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_model == dialog_node_output_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_model_json2 = dialog_node_output_model.to_dict()
        assert dialog_node_output_model_json2 == dialog_node_output_model_json

        # Test get_properties and set_properties methods.
        dialog_node_output_model.set_properties({})
        actual_dict = dialog_node_output_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        dialog_node_output_model.set_properties(expected_dict)
        actual_dict = dialog_node_output_model.get_properties()
        assert actual_dict == expected_dict

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

class TestModel_DialogNodeOutputModifiers():
    """
    Test Class for DialogNodeOutputModifiers
    """

    def test_dialog_node_output_modifiers_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputModifiers
        """

        # Construct a json representation of a DialogNodeOutputModifiers model
        dialog_node_output_modifiers_model_json = {}
        dialog_node_output_modifiers_model_json['overwrite'] = True

        # Construct a model instance of DialogNodeOutputModifiers by calling from_dict on the json representation
        dialog_node_output_modifiers_model = DialogNodeOutputModifiers.from_dict(dialog_node_output_modifiers_model_json)
        assert dialog_node_output_modifiers_model != False

        # Construct a model instance of DialogNodeOutputModifiers by calling from_dict on the json representation
        dialog_node_output_modifiers_model_dict = DialogNodeOutputModifiers.from_dict(dialog_node_output_modifiers_model_json).__dict__
        dialog_node_output_modifiers_model2 = DialogNodeOutputModifiers(**dialog_node_output_modifiers_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_modifiers_model == dialog_node_output_modifiers_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_modifiers_model_json2 = dialog_node_output_modifiers_model.to_dict()
        assert dialog_node_output_modifiers_model_json2 == dialog_node_output_modifiers_model_json

class TestModel_DialogNodeOutputOptionsElement():
    """
    Test Class for DialogNodeOutputOptionsElement
    """

    def test_dialog_node_output_options_element_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputOptionsElement
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

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

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        # Construct a json representation of a DialogNodeOutputOptionsElementValue model
        dialog_node_output_options_element_value_model_json = {}
        dialog_node_output_options_element_value_model_json['input'] = message_input_model
        dialog_node_output_options_element_value_model_json['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model_json['entities'] = [runtime_entity_model]

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

class TestModel_DialogNodeOutputTextValuesElement():
    """
    Test Class for DialogNodeOutputTextValuesElement
    """

    def test_dialog_node_output_text_values_element_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputTextValuesElement
        """

        # Construct a json representation of a DialogNodeOutputTextValuesElement model
        dialog_node_output_text_values_element_model_json = {}
        dialog_node_output_text_values_element_model_json['text'] = 'testString'

        # Construct a model instance of DialogNodeOutputTextValuesElement by calling from_dict on the json representation
        dialog_node_output_text_values_element_model = DialogNodeOutputTextValuesElement.from_dict(dialog_node_output_text_values_element_model_json)
        assert dialog_node_output_text_values_element_model != False

        # Construct a model instance of DialogNodeOutputTextValuesElement by calling from_dict on the json representation
        dialog_node_output_text_values_element_model_dict = DialogNodeOutputTextValuesElement.from_dict(dialog_node_output_text_values_element_model_json).__dict__
        dialog_node_output_text_values_element_model2 = DialogNodeOutputTextValuesElement(**dialog_node_output_text_values_element_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_text_values_element_model == dialog_node_output_text_values_element_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_text_values_element_model_json2 = dialog_node_output_text_values_element_model.to_dict()
        assert dialog_node_output_text_values_element_model_json2 == dialog_node_output_text_values_element_model_json

class TestModel_DialogNodeVisitedDetails():
    """
    Test Class for DialogNodeVisitedDetails
    """

    def test_dialog_node_visited_details_serialization(self):
        """
        Test serialization/deserialization for DialogNodeVisitedDetails
        """

        # Construct a json representation of a DialogNodeVisitedDetails model
        dialog_node_visited_details_model_json = {}
        dialog_node_visited_details_model_json['dialog_node'] = 'testString'
        dialog_node_visited_details_model_json['title'] = 'testString'
        dialog_node_visited_details_model_json['conditions'] = 'testString'

        # Construct a model instance of DialogNodeVisitedDetails by calling from_dict on the json representation
        dialog_node_visited_details_model = DialogNodeVisitedDetails.from_dict(dialog_node_visited_details_model_json)
        assert dialog_node_visited_details_model != False

        # Construct a model instance of DialogNodeVisitedDetails by calling from_dict on the json representation
        dialog_node_visited_details_model_dict = DialogNodeVisitedDetails.from_dict(dialog_node_visited_details_model_json).__dict__
        dialog_node_visited_details_model2 = DialogNodeVisitedDetails(**dialog_node_visited_details_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_visited_details_model == dialog_node_visited_details_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_visited_details_model_json2 = dialog_node_visited_details_model.to_dict()
        assert dialog_node_visited_details_model_json2 == dialog_node_visited_details_model_json

class TestModel_DialogSuggestion():
    """
    Test Class for DialogSuggestion
    """

    def test_dialog_suggestion_serialization(self):
        """
        Test serialization/deserialization for DialogSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_suggestion_value_model = {} # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model
        dialog_suggestion_value_model['intents'] = [runtime_intent_model]
        dialog_suggestion_value_model['entities'] = [runtime_entity_model]

        # Construct a json representation of a DialogSuggestion model
        dialog_suggestion_model_json = {}
        dialog_suggestion_model_json['label'] = 'testString'
        dialog_suggestion_model_json['value'] = dialog_suggestion_value_model
        dialog_suggestion_model_json['output'] = {}
        dialog_suggestion_model_json['dialog_node'] = 'testString'

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

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        # Construct a json representation of a DialogSuggestionValue model
        dialog_suggestion_value_model_json = {}
        dialog_suggestion_value_model_json['input'] = message_input_model
        dialog_suggestion_value_model_json['intents'] = [runtime_intent_model]
        dialog_suggestion_value_model_json['entities'] = [runtime_entity_model]

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

class TestModel_Entity():
    """
    Test Class for Entity
    """

    def test_entity_serialization(self):
        """
        Test serialization/deserialization for Entity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_model = {} # Value
        value_model['value'] = 'testString'
        value_model['metadata'] = {}
        value_model['type'] = 'synonyms'
        value_model['synonyms'] = ['testString']
        value_model['patterns'] = ['testString']
        value_model['created'] = "2019-01-01T12:00:00Z"
        value_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a Entity model
        entity_model_json = {}
        entity_model_json['entity'] = 'testString'
        entity_model_json['description'] = 'testString'
        entity_model_json['metadata'] = {}
        entity_model_json['fuzzy_match'] = True
        entity_model_json['created'] = "2019-01-01T12:00:00Z"
        entity_model_json['updated'] = "2019-01-01T12:00:00Z"
        entity_model_json['values'] = [value_model]

        # Construct a model instance of Entity by calling from_dict on the json representation
        entity_model = Entity.from_dict(entity_model_json)
        assert entity_model != False

        # Construct a model instance of Entity by calling from_dict on the json representation
        entity_model_dict = Entity.from_dict(entity_model_json).__dict__
        entity_model2 = Entity(**entity_model_dict)

        # Verify the model instances are equivalent
        assert entity_model == entity_model2

        # Convert model instance back to dict and verify no loss of data
        entity_model_json2 = entity_model.to_dict()
        assert entity_model_json2 == entity_model_json

class TestModel_EntityCollection():
    """
    Test Class for EntityCollection
    """

    def test_entity_collection_serialization(self):
        """
        Test serialization/deserialization for EntityCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_model = {} # Value
        value_model['value'] = 'testString'
        value_model['metadata'] = {}
        value_model['type'] = 'synonyms'
        value_model['synonyms'] = ['testString']
        value_model['patterns'] = ['testString']
        value_model['created'] = "2019-01-01T12:00:00Z"
        value_model['updated'] = "2019-01-01T12:00:00Z"

        entity_model = {} # Entity
        entity_model['entity'] = 'testString'
        entity_model['description'] = 'testString'
        entity_model['metadata'] = {}
        entity_model['fuzzy_match'] = True
        entity_model['created'] = "2019-01-01T12:00:00Z"
        entity_model['updated'] = "2019-01-01T12:00:00Z"
        entity_model['values'] = [value_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a EntityCollection model
        entity_collection_model_json = {}
        entity_collection_model_json['entities'] = [entity_model]
        entity_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of EntityCollection by calling from_dict on the json representation
        entity_collection_model = EntityCollection.from_dict(entity_collection_model_json)
        assert entity_collection_model != False

        # Construct a model instance of EntityCollection by calling from_dict on the json representation
        entity_collection_model_dict = EntityCollection.from_dict(entity_collection_model_json).__dict__
        entity_collection_model2 = EntityCollection(**entity_collection_model_dict)

        # Verify the model instances are equivalent
        assert entity_collection_model == entity_collection_model2

        # Convert model instance back to dict and verify no loss of data
        entity_collection_model_json2 = entity_collection_model.to_dict()
        assert entity_collection_model_json2 == entity_collection_model_json

class TestModel_EntityMention():
    """
    Test Class for EntityMention
    """

    def test_entity_mention_serialization(self):
        """
        Test serialization/deserialization for EntityMention
        """

        # Construct a json representation of a EntityMention model
        entity_mention_model_json = {}
        entity_mention_model_json['text'] = 'testString'
        entity_mention_model_json['intent'] = 'testString'
        entity_mention_model_json['location'] = [38]

        # Construct a model instance of EntityMention by calling from_dict on the json representation
        entity_mention_model = EntityMention.from_dict(entity_mention_model_json)
        assert entity_mention_model != False

        # Construct a model instance of EntityMention by calling from_dict on the json representation
        entity_mention_model_dict = EntityMention.from_dict(entity_mention_model_json).__dict__
        entity_mention_model2 = EntityMention(**entity_mention_model_dict)

        # Verify the model instances are equivalent
        assert entity_mention_model == entity_mention_model2

        # Convert model instance back to dict and verify no loss of data
        entity_mention_model_json2 = entity_mention_model.to_dict()
        assert entity_mention_model_json2 == entity_mention_model_json

class TestModel_EntityMentionCollection():
    """
    Test Class for EntityMentionCollection
    """

    def test_entity_mention_collection_serialization(self):
        """
        Test serialization/deserialization for EntityMentionCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        entity_mention_model = {} # EntityMention
        entity_mention_model['text'] = 'testString'
        entity_mention_model['intent'] = 'testString'
        entity_mention_model['location'] = [38]

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a EntityMentionCollection model
        entity_mention_collection_model_json = {}
        entity_mention_collection_model_json['examples'] = [entity_mention_model]
        entity_mention_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of EntityMentionCollection by calling from_dict on the json representation
        entity_mention_collection_model = EntityMentionCollection.from_dict(entity_mention_collection_model_json)
        assert entity_mention_collection_model != False

        # Construct a model instance of EntityMentionCollection by calling from_dict on the json representation
        entity_mention_collection_model_dict = EntityMentionCollection.from_dict(entity_mention_collection_model_json).__dict__
        entity_mention_collection_model2 = EntityMentionCollection(**entity_mention_collection_model_dict)

        # Verify the model instances are equivalent
        assert entity_mention_collection_model == entity_mention_collection_model2

        # Convert model instance back to dict and verify no loss of data
        entity_mention_collection_model_json2 = entity_mention_collection_model.to_dict()
        assert entity_mention_collection_model_json2 == entity_mention_collection_model_json

class TestModel_Example():
    """
    Test Class for Example
    """

    def test_example_serialization(self):
        """
        Test serialization/deserialization for Example
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        # Construct a json representation of a Example model
        example_model_json = {}
        example_model_json['text'] = 'testString'
        example_model_json['mentions'] = [mention_model]
        example_model_json['created'] = "2019-01-01T12:00:00Z"
        example_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Example by calling from_dict on the json representation
        example_model = Example.from_dict(example_model_json)
        assert example_model != False

        # Construct a model instance of Example by calling from_dict on the json representation
        example_model_dict = Example.from_dict(example_model_json).__dict__
        example_model2 = Example(**example_model_dict)

        # Verify the model instances are equivalent
        assert example_model == example_model2

        # Convert model instance back to dict and verify no loss of data
        example_model_json2 = example_model.to_dict()
        assert example_model_json2 == example_model_json

class TestModel_ExampleCollection():
    """
    Test Class for ExampleCollection
    """

    def test_example_collection_serialization(self):
        """
        Test serialization/deserialization for ExampleCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a ExampleCollection model
        example_collection_model_json = {}
        example_collection_model_json['examples'] = [example_model]
        example_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of ExampleCollection by calling from_dict on the json representation
        example_collection_model = ExampleCollection.from_dict(example_collection_model_json)
        assert example_collection_model != False

        # Construct a model instance of ExampleCollection by calling from_dict on the json representation
        example_collection_model_dict = ExampleCollection.from_dict(example_collection_model_json).__dict__
        example_collection_model2 = ExampleCollection(**example_collection_model_dict)

        # Verify the model instances are equivalent
        assert example_collection_model == example_collection_model2

        # Convert model instance back to dict and verify no loss of data
        example_collection_model_json2 = example_collection_model.to_dict()
        assert example_collection_model_json2 == example_collection_model_json

class TestModel_Intent():
    """
    Test Class for Intent
    """

    def test_intent_serialization(self):
        """
        Test serialization/deserialization for Intent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a Intent model
        intent_model_json = {}
        intent_model_json['intent'] = 'testString'
        intent_model_json['description'] = 'testString'
        intent_model_json['created'] = "2019-01-01T12:00:00Z"
        intent_model_json['updated'] = "2019-01-01T12:00:00Z"
        intent_model_json['examples'] = [example_model]

        # Construct a model instance of Intent by calling from_dict on the json representation
        intent_model = Intent.from_dict(intent_model_json)
        assert intent_model != False

        # Construct a model instance of Intent by calling from_dict on the json representation
        intent_model_dict = Intent.from_dict(intent_model_json).__dict__
        intent_model2 = Intent(**intent_model_dict)

        # Verify the model instances are equivalent
        assert intent_model == intent_model2

        # Convert model instance back to dict and verify no loss of data
        intent_model_json2 = intent_model.to_dict()
        assert intent_model_json2 == intent_model_json

class TestModel_IntentCollection():
    """
    Test Class for IntentCollection
    """

    def test_intent_collection_serialization(self):
        """
        Test serialization/deserialization for IntentCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        intent_model = {} # Intent
        intent_model['intent'] = 'testString'
        intent_model['description'] = 'testString'
        intent_model['created'] = "2019-01-01T12:00:00Z"
        intent_model['updated'] = "2019-01-01T12:00:00Z"
        intent_model['examples'] = [example_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a IntentCollection model
        intent_collection_model_json = {}
        intent_collection_model_json['intents'] = [intent_model]
        intent_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of IntentCollection by calling from_dict on the json representation
        intent_collection_model = IntentCollection.from_dict(intent_collection_model_json)
        assert intent_collection_model != False

        # Construct a model instance of IntentCollection by calling from_dict on the json representation
        intent_collection_model_dict = IntentCollection.from_dict(intent_collection_model_json).__dict__
        intent_collection_model2 = IntentCollection(**intent_collection_model_dict)

        # Verify the model instances are equivalent
        assert intent_collection_model == intent_collection_model2

        # Convert model instance back to dict and verify no loss of data
        intent_collection_model_json2 = intent_collection_model.to_dict()
        assert intent_collection_model_json2 == intent_collection_model_json

class TestModel_Log():
    """
    Test Class for Log
    """

    def test_log_serialization(self):
        """
        Test serialization/deserialization for Log
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        message_context_metadata_model = {} # MessageContextMetadata
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        context_model = {} # Context
        context_model['conversation_id'] = 'testString'
        context_model['system'] = {}
        context_model['metadata'] = message_context_metadata_model
        context_model['foo'] = 'testString'

        dialog_node_visited_details_model = {} # DialogNodeVisitedDetails
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        log_message_model = {} # LogMessage
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        output_data_model = {} # OutputData
        output_data_model['nodes_visited'] = ['testString']
        output_data_model['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model['log_messages'] = [log_message_model]
        output_data_model['text'] = ['testString']
        output_data_model['generic'] = [runtime_response_generic_model]
        output_data_model['foo'] = 'testString'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        message_request_model = {} # MessageRequest
        message_request_model['input'] = message_input_model
        message_request_model['intents'] = [runtime_intent_model]
        message_request_model['entities'] = [runtime_entity_model]
        message_request_model['alternate_intents'] = False
        message_request_model['context'] = context_model
        message_request_model['output'] = output_data_model
        message_request_model['actions'] = [dialog_node_action_model]
        message_request_model['user_id'] = 'testString'

        message_response_model = {} # MessageResponse
        message_response_model['input'] = message_input_model
        message_response_model['intents'] = [runtime_intent_model]
        message_response_model['entities'] = [runtime_entity_model]
        message_response_model['alternate_intents'] = False
        message_response_model['context'] = context_model
        message_response_model['output'] = output_data_model
        message_response_model['actions'] = [dialog_node_action_model]
        message_response_model['user_id'] = 'testString'

        # Construct a json representation of a Log model
        log_model_json = {}
        log_model_json['request'] = message_request_model
        log_model_json['response'] = message_response_model
        log_model_json['log_id'] = 'testString'
        log_model_json['request_timestamp'] = 'testString'
        log_model_json['response_timestamp'] = 'testString'
        log_model_json['workspace_id'] = 'testString'
        log_model_json['language'] = 'testString'

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

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        message_context_metadata_model = {} # MessageContextMetadata
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        context_model = {} # Context
        context_model['conversation_id'] = 'testString'
        context_model['system'] = {}
        context_model['metadata'] = message_context_metadata_model
        context_model['foo'] = 'testString'

        dialog_node_visited_details_model = {} # DialogNodeVisitedDetails
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        log_message_model = {} # LogMessage
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        output_data_model = {} # OutputData
        output_data_model['nodes_visited'] = ['testString']
        output_data_model['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model['log_messages'] = [log_message_model]
        output_data_model['text'] = ['testString']
        output_data_model['generic'] = [runtime_response_generic_model]
        output_data_model['foo'] = 'testString'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        message_request_model = {} # MessageRequest
        message_request_model['input'] = message_input_model
        message_request_model['intents'] = [runtime_intent_model]
        message_request_model['entities'] = [runtime_entity_model]
        message_request_model['alternate_intents'] = False
        message_request_model['context'] = context_model
        message_request_model['output'] = output_data_model
        message_request_model['actions'] = [dialog_node_action_model]
        message_request_model['user_id'] = 'testString'

        message_response_model = {} # MessageResponse
        message_response_model['input'] = message_input_model
        message_response_model['intents'] = [runtime_intent_model]
        message_response_model['entities'] = [runtime_entity_model]
        message_response_model['alternate_intents'] = False
        message_response_model['context'] = context_model
        message_response_model['output'] = output_data_model
        message_response_model['actions'] = [dialog_node_action_model]
        message_response_model['user_id'] = 'testString'

        log_model = {} # Log
        log_model['request'] = message_request_model
        log_model['response'] = message_response_model
        log_model['log_id'] = 'testString'
        log_model['request_timestamp'] = 'testString'
        log_model['response_timestamp'] = 'testString'
        log_model['workspace_id'] = 'testString'
        log_model['language'] = 'testString'

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

class TestModel_LogMessage():
    """
    Test Class for LogMessage
    """

    def test_log_message_serialization(self):
        """
        Test serialization/deserialization for LogMessage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        # Construct a json representation of a LogMessage model
        log_message_model_json = {}
        log_message_model_json['level'] = 'info'
        log_message_model_json['msg'] = 'testString'
        log_message_model_json['code'] = 'testString'
        log_message_model_json['source'] = log_message_source_model

        # Construct a model instance of LogMessage by calling from_dict on the json representation
        log_message_model = LogMessage.from_dict(log_message_model_json)
        assert log_message_model != False

        # Construct a model instance of LogMessage by calling from_dict on the json representation
        log_message_model_dict = LogMessage.from_dict(log_message_model_json).__dict__
        log_message_model2 = LogMessage(**log_message_model_dict)

        # Verify the model instances are equivalent
        assert log_message_model == log_message_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_model_json2 = log_message_model.to_dict()
        assert log_message_model_json2 == log_message_model_json

class TestModel_LogMessageSource():
    """
    Test Class for LogMessageSource
    """

    def test_log_message_source_serialization(self):
        """
        Test serialization/deserialization for LogMessageSource
        """

        # Construct a json representation of a LogMessageSource model
        log_message_source_model_json = {}
        log_message_source_model_json['type'] = 'dialog_node'
        log_message_source_model_json['dialog_node'] = 'testString'

        # Construct a model instance of LogMessageSource by calling from_dict on the json representation
        log_message_source_model = LogMessageSource.from_dict(log_message_source_model_json)
        assert log_message_source_model != False

        # Construct a model instance of LogMessageSource by calling from_dict on the json representation
        log_message_source_model_dict = LogMessageSource.from_dict(log_message_source_model_json).__dict__
        log_message_source_model2 = LogMessageSource(**log_message_source_model_dict)

        # Verify the model instances are equivalent
        assert log_message_source_model == log_message_source_model2

        # Convert model instance back to dict and verify no loss of data
        log_message_source_model_json2 = log_message_source_model.to_dict()
        assert log_message_source_model_json2 == log_message_source_model_json

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

class TestModel_Mention():
    """
    Test Class for Mention
    """

    def test_mention_serialization(self):
        """
        Test serialization/deserialization for Mention
        """

        # Construct a json representation of a Mention model
        mention_model_json = {}
        mention_model_json['entity'] = 'testString'
        mention_model_json['location'] = [38]

        # Construct a model instance of Mention by calling from_dict on the json representation
        mention_model = Mention.from_dict(mention_model_json)
        assert mention_model != False

        # Construct a model instance of Mention by calling from_dict on the json representation
        mention_model_dict = Mention.from_dict(mention_model_json).__dict__
        mention_model2 = Mention(**mention_model_dict)

        # Verify the model instances are equivalent
        assert mention_model == mention_model2

        # Convert model instance back to dict and verify no loss of data
        mention_model_json2 = mention_model.to_dict()
        assert mention_model_json2 == mention_model_json

class TestModel_MessageContextMetadata():
    """
    Test Class for MessageContextMetadata
    """

    def test_message_context_metadata_serialization(self):
        """
        Test serialization/deserialization for MessageContextMetadata
        """

        # Construct a json representation of a MessageContextMetadata model
        message_context_metadata_model_json = {}
        message_context_metadata_model_json['deployment'] = 'testString'
        message_context_metadata_model_json['user_id'] = 'testString'

        # Construct a model instance of MessageContextMetadata by calling from_dict on the json representation
        message_context_metadata_model = MessageContextMetadata.from_dict(message_context_metadata_model_json)
        assert message_context_metadata_model != False

        # Construct a model instance of MessageContextMetadata by calling from_dict on the json representation
        message_context_metadata_model_dict = MessageContextMetadata.from_dict(message_context_metadata_model_json).__dict__
        message_context_metadata_model2 = MessageContextMetadata(**message_context_metadata_model_dict)

        # Verify the model instances are equivalent
        assert message_context_metadata_model == message_context_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        message_context_metadata_model_json2 = message_context_metadata_model.to_dict()
        assert message_context_metadata_model_json2 == message_context_metadata_model_json

class TestModel_MessageInput():
    """
    Test Class for MessageInput
    """

    def test_message_input_serialization(self):
        """
        Test serialization/deserialization for MessageInput
        """

        # Construct a json representation of a MessageInput model
        message_input_model_json = {}
        message_input_model_json['text'] = 'testString'
        message_input_model_json['spelling_suggestions'] = False
        message_input_model_json['spelling_auto_correct'] = False
        message_input_model_json['suggested_text'] = 'testString'
        message_input_model_json['original_text'] = 'testString'
        message_input_model_json['foo'] = 'testString'

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

        # Test get_properties and set_properties methods.
        message_input_model.set_properties({})
        actual_dict = message_input_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        message_input_model.set_properties(expected_dict)
        actual_dict = message_input_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_MessageRequest():
    """
    Test Class for MessageRequest
    """

    def test_message_request_serialization(self):
        """
        Test serialization/deserialization for MessageRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        message_context_metadata_model = {} # MessageContextMetadata
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        context_model = {} # Context
        context_model['conversation_id'] = 'testString'
        context_model['system'] = {}
        context_model['metadata'] = message_context_metadata_model
        context_model['foo'] = 'testString'

        dialog_node_visited_details_model = {} # DialogNodeVisitedDetails
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        log_message_model = {} # LogMessage
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        output_data_model = {} # OutputData
        output_data_model['nodes_visited'] = ['testString']
        output_data_model['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model['log_messages'] = [log_message_model]
        output_data_model['text'] = ['testString']
        output_data_model['generic'] = [runtime_response_generic_model]
        output_data_model['foo'] = 'testString'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Construct a json representation of a MessageRequest model
        message_request_model_json = {}
        message_request_model_json['input'] = message_input_model
        message_request_model_json['intents'] = [runtime_intent_model]
        message_request_model_json['entities'] = [runtime_entity_model]
        message_request_model_json['alternate_intents'] = False
        message_request_model_json['context'] = context_model
        message_request_model_json['output'] = output_data_model
        message_request_model_json['actions'] = [dialog_node_action_model]
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

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        message_context_metadata_model = {} # MessageContextMetadata
        message_context_metadata_model['deployment'] = 'testString'
        message_context_metadata_model['user_id'] = 'testString'

        context_model = {} # Context
        context_model['conversation_id'] = 'testString'
        context_model['system'] = {}
        context_model['metadata'] = message_context_metadata_model
        context_model['foo'] = 'testString'

        dialog_node_visited_details_model = {} # DialogNodeVisitedDetails
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        log_message_model = {} # LogMessage
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        output_data_model = {} # OutputData
        output_data_model['nodes_visited'] = ['testString']
        output_data_model['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model['log_messages'] = [log_message_model]
        output_data_model['text'] = ['testString']
        output_data_model['generic'] = [runtime_response_generic_model]
        output_data_model['foo'] = 'testString'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        # Construct a json representation of a MessageResponse model
        message_response_model_json = {}
        message_response_model_json['input'] = message_input_model
        message_response_model_json['intents'] = [runtime_intent_model]
        message_response_model_json['entities'] = [runtime_entity_model]
        message_response_model_json['alternate_intents'] = False
        message_response_model_json['context'] = context_model
        message_response_model_json['output'] = output_data_model
        message_response_model_json['actions'] = [dialog_node_action_model]
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

class TestModel_OutputData():
    """
    Test Class for OutputData
    """

    def test_output_data_serialization(self):
        """
        Test serialization/deserialization for OutputData
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dialog_node_visited_details_model = {} # DialogNodeVisitedDetails
        dialog_node_visited_details_model['dialog_node'] = 'testString'
        dialog_node_visited_details_model['title'] = 'testString'
        dialog_node_visited_details_model['conditions'] = 'testString'

        log_message_source_model = {} # LogMessageSource
        log_message_source_model['type'] = 'dialog_node'
        log_message_source_model['dialog_node'] = 'testString'

        log_message_model = {} # LogMessage
        log_message_model['level'] = 'info'
        log_message_model['msg'] = 'testString'
        log_message_model['code'] = 'testString'
        log_message_model['source'] = log_message_source_model

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        runtime_response_generic_model = {} # RuntimeResponseGenericRuntimeResponseTypeOption
        runtime_response_generic_model['response_type'] = 'option'
        runtime_response_generic_model['title'] = 'testString'
        runtime_response_generic_model['description'] = 'testString'
        runtime_response_generic_model['preference'] = 'dropdown'
        runtime_response_generic_model['options'] = [dialog_node_output_options_element_model]
        runtime_response_generic_model['channels'] = [response_generic_channel_model]

        # Construct a json representation of a OutputData model
        output_data_model_json = {}
        output_data_model_json['nodes_visited'] = ['testString']
        output_data_model_json['nodes_visited_details'] = [dialog_node_visited_details_model]
        output_data_model_json['log_messages'] = [log_message_model]
        output_data_model_json['text'] = ['testString']
        output_data_model_json['generic'] = [runtime_response_generic_model]
        output_data_model_json['foo'] = 'testString'

        # Construct a model instance of OutputData by calling from_dict on the json representation
        output_data_model = OutputData.from_dict(output_data_model_json)
        assert output_data_model != False

        # Construct a model instance of OutputData by calling from_dict on the json representation
        output_data_model_dict = OutputData.from_dict(output_data_model_json).__dict__
        output_data_model2 = OutputData(**output_data_model_dict)

        # Verify the model instances are equivalent
        assert output_data_model == output_data_model2

        # Convert model instance back to dict and verify no loss of data
        output_data_model_json2 = output_data_model.to_dict()
        assert output_data_model_json2 == output_data_model_json

        # Test get_properties and set_properties methods.
        output_data_model.set_properties({})
        actual_dict = output_data_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': 'testString'}
        output_data_model.set_properties(expected_dict)
        actual_dict = output_data_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_Pagination():
    """
    Test Class for Pagination
    """

    def test_pagination_serialization(self):
        """
        Test serialization/deserialization for Pagination
        """

        # Construct a json representation of a Pagination model
        pagination_model_json = {}
        pagination_model_json['refresh_url'] = 'testString'
        pagination_model_json['next_url'] = 'testString'
        pagination_model_json['total'] = 38
        pagination_model_json['matched'] = 38
        pagination_model_json['refresh_cursor'] = 'testString'
        pagination_model_json['next_cursor'] = 'testString'

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model = Pagination.from_dict(pagination_model_json)
        assert pagination_model != False

        # Construct a model instance of Pagination by calling from_dict on the json representation
        pagination_model_dict = Pagination.from_dict(pagination_model_json).__dict__
        pagination_model2 = Pagination(**pagination_model_dict)

        # Verify the model instances are equivalent
        assert pagination_model == pagination_model2

        # Convert model instance back to dict and verify no loss of data
        pagination_model_json2 = pagination_model.to_dict()
        assert pagination_model_json2 == pagination_model_json

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
        response_generic_channel_model_json['channel'] = 'chat'

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

class TestModel_Synonym():
    """
    Test Class for Synonym
    """

    def test_synonym_serialization(self):
        """
        Test serialization/deserialization for Synonym
        """

        # Construct a json representation of a Synonym model
        synonym_model_json = {}
        synonym_model_json['synonym'] = 'testString'
        synonym_model_json['created'] = "2019-01-01T12:00:00Z"
        synonym_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Synonym by calling from_dict on the json representation
        synonym_model = Synonym.from_dict(synonym_model_json)
        assert synonym_model != False

        # Construct a model instance of Synonym by calling from_dict on the json representation
        synonym_model_dict = Synonym.from_dict(synonym_model_json).__dict__
        synonym_model2 = Synonym(**synonym_model_dict)

        # Verify the model instances are equivalent
        assert synonym_model == synonym_model2

        # Convert model instance back to dict and verify no loss of data
        synonym_model_json2 = synonym_model.to_dict()
        assert synonym_model_json2 == synonym_model_json

class TestModel_SynonymCollection():
    """
    Test Class for SynonymCollection
    """

    def test_synonym_collection_serialization(self):
        """
        Test serialization/deserialization for SynonymCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        synonym_model = {} # Synonym
        synonym_model['synonym'] = 'testString'
        synonym_model['created'] = "2019-01-01T12:00:00Z"
        synonym_model['updated'] = "2019-01-01T12:00:00Z"

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a SynonymCollection model
        synonym_collection_model_json = {}
        synonym_collection_model_json['synonyms'] = [synonym_model]
        synonym_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of SynonymCollection by calling from_dict on the json representation
        synonym_collection_model = SynonymCollection.from_dict(synonym_collection_model_json)
        assert synonym_collection_model != False

        # Construct a model instance of SynonymCollection by calling from_dict on the json representation
        synonym_collection_model_dict = SynonymCollection.from_dict(synonym_collection_model_json).__dict__
        synonym_collection_model2 = SynonymCollection(**synonym_collection_model_dict)

        # Verify the model instances are equivalent
        assert synonym_collection_model == synonym_collection_model2

        # Convert model instance back to dict and verify no loss of data
        synonym_collection_model_json2 = synonym_collection_model.to_dict()
        assert synonym_collection_model_json2 == synonym_collection_model_json

class TestModel_Value():
    """
    Test Class for Value
    """

    def test_value_serialization(self):
        """
        Test serialization/deserialization for Value
        """

        # Construct a json representation of a Value model
        value_model_json = {}
        value_model_json['value'] = 'testString'
        value_model_json['metadata'] = {}
        value_model_json['type'] = 'synonyms'
        value_model_json['synonyms'] = ['testString']
        value_model_json['patterns'] = ['testString']
        value_model_json['created'] = "2019-01-01T12:00:00Z"
        value_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of Value by calling from_dict on the json representation
        value_model = Value.from_dict(value_model_json)
        assert value_model != False

        # Construct a model instance of Value by calling from_dict on the json representation
        value_model_dict = Value.from_dict(value_model_json).__dict__
        value_model2 = Value(**value_model_dict)

        # Verify the model instances are equivalent
        assert value_model == value_model2

        # Convert model instance back to dict and verify no loss of data
        value_model_json2 = value_model.to_dict()
        assert value_model_json2 == value_model_json

class TestModel_ValueCollection():
    """
    Test Class for ValueCollection
    """

    def test_value_collection_serialization(self):
        """
        Test serialization/deserialization for ValueCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        value_model = {} # Value
        value_model['value'] = 'testString'
        value_model['metadata'] = {}
        value_model['type'] = 'synonyms'
        value_model['synonyms'] = ['testString']
        value_model['patterns'] = ['testString']
        value_model['created'] = "2019-01-01T12:00:00Z"
        value_model['updated'] = "2019-01-01T12:00:00Z"

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a ValueCollection model
        value_collection_model_json = {}
        value_collection_model_json['values'] = [value_model]
        value_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of ValueCollection by calling from_dict on the json representation
        value_collection_model = ValueCollection.from_dict(value_collection_model_json)
        assert value_collection_model != False

        # Construct a model instance of ValueCollection by calling from_dict on the json representation
        value_collection_model_dict = ValueCollection.from_dict(value_collection_model_json).__dict__
        value_collection_model2 = ValueCollection(**value_collection_model_dict)

        # Verify the model instances are equivalent
        assert value_collection_model == value_collection_model2

        # Convert model instance back to dict and verify no loss of data
        value_collection_model_json2 = value_collection_model.to_dict()
        assert value_collection_model_json2 == value_collection_model_json

class TestModel_Webhook():
    """
    Test Class for Webhook
    """

    def test_webhook_serialization(self):
        """
        Test serialization/deserialization for Webhook
        """

        # Construct dict forms of any model objects needed in order to build this model.

        webhook_header_model = {} # WebhookHeader
        webhook_header_model['name'] = 'testString'
        webhook_header_model['value'] = 'testString'

        # Construct a json representation of a Webhook model
        webhook_model_json = {}
        webhook_model_json['url'] = 'testString'
        webhook_model_json['name'] = 'testString'
        webhook_model_json['headers'] = [webhook_header_model]

        # Construct a model instance of Webhook by calling from_dict on the json representation
        webhook_model = Webhook.from_dict(webhook_model_json)
        assert webhook_model != False

        # Construct a model instance of Webhook by calling from_dict on the json representation
        webhook_model_dict = Webhook.from_dict(webhook_model_json).__dict__
        webhook_model2 = Webhook(**webhook_model_dict)

        # Verify the model instances are equivalent
        assert webhook_model == webhook_model2

        # Convert model instance back to dict and verify no loss of data
        webhook_model_json2 = webhook_model.to_dict()
        assert webhook_model_json2 == webhook_model_json

class TestModel_WebhookHeader():
    """
    Test Class for WebhookHeader
    """

    def test_webhook_header_serialization(self):
        """
        Test serialization/deserialization for WebhookHeader
        """

        # Construct a json representation of a WebhookHeader model
        webhook_header_model_json = {}
        webhook_header_model_json['name'] = 'testString'
        webhook_header_model_json['value'] = 'testString'

        # Construct a model instance of WebhookHeader by calling from_dict on the json representation
        webhook_header_model = WebhookHeader.from_dict(webhook_header_model_json)
        assert webhook_header_model != False

        # Construct a model instance of WebhookHeader by calling from_dict on the json representation
        webhook_header_model_dict = WebhookHeader.from_dict(webhook_header_model_json).__dict__
        webhook_header_model2 = WebhookHeader(**webhook_header_model_dict)

        # Verify the model instances are equivalent
        assert webhook_header_model == webhook_header_model2

        # Convert model instance back to dict and verify no loss of data
        webhook_header_model_json2 = webhook_header_model.to_dict()
        assert webhook_header_model_json2 == webhook_header_model_json

class TestModel_Workspace():
    """
    Test Class for Workspace
    """

    def test_workspace_serialization(self):
        """
        Test serialization/deserialization for Workspace
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        dialog_node_output_generic_model = {} # DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_output_modifiers_model = {} # DialogNodeOutputModifiers
        dialog_node_output_modifiers_model['overwrite'] = True

        dialog_node_output_model = {} # DialogNodeOutput
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        dialog_node_context_model = {} # DialogNodeContext
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        dialog_node_next_step_model = {} # DialogNodeNextStep
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_model = {} # DialogNode
        dialog_node_model['dialog_node'] = 'testString'
        dialog_node_model['description'] = 'testString'
        dialog_node_model['conditions'] = 'testString'
        dialog_node_model['parent'] = 'testString'
        dialog_node_model['previous_sibling'] = 'testString'
        dialog_node_model['output'] = dialog_node_output_model
        dialog_node_model['context'] = dialog_node_context_model
        dialog_node_model['metadata'] = {}
        dialog_node_model['next_step'] = dialog_node_next_step_model
        dialog_node_model['title'] = 'testString'
        dialog_node_model['type'] = 'standard'
        dialog_node_model['event_name'] = 'focus'
        dialog_node_model['variable'] = 'testString'
        dialog_node_model['actions'] = [dialog_node_action_model]
        dialog_node_model['digress_in'] = 'not_available'
        dialog_node_model['digress_out'] = 'allow_returning'
        dialog_node_model['digress_out_slots'] = 'not_allowed'
        dialog_node_model['user_label'] = 'testString'
        dialog_node_model['disambiguation_opt_out'] = False
        dialog_node_model['disabled'] = True
        dialog_node_model['created'] = "2019-01-01T12:00:00Z"
        dialog_node_model['updated'] = "2019-01-01T12:00:00Z"

        counterexample_model = {} # Counterexample
        counterexample_model['text'] = 'testString'
        counterexample_model['created'] = "2019-01-01T12:00:00Z"
        counterexample_model['updated'] = "2019-01-01T12:00:00Z"

        workspace_system_settings_tooling_model = {} # WorkspaceSystemSettingsTooling
        workspace_system_settings_tooling_model['store_generic_responses'] = True

        workspace_system_settings_disambiguation_model = {} # WorkspaceSystemSettingsDisambiguation
        workspace_system_settings_disambiguation_model['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['enabled'] = False
        workspace_system_settings_disambiguation_model['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model['randomize'] = True
        workspace_system_settings_disambiguation_model['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model['suggestion_text_policy'] = 'testString'

        workspace_system_settings_system_entities_model = {} # WorkspaceSystemSettingsSystemEntities
        workspace_system_settings_system_entities_model['enabled'] = False

        workspace_system_settings_off_topic_model = {} # WorkspaceSystemSettingsOffTopic
        workspace_system_settings_off_topic_model['enabled'] = False

        workspace_system_settings_model = {} # WorkspaceSystemSettings
        workspace_system_settings_model['tooling'] = workspace_system_settings_tooling_model
        workspace_system_settings_model['disambiguation'] = workspace_system_settings_disambiguation_model
        workspace_system_settings_model['human_agent_assist'] = {}
        workspace_system_settings_model['spelling_suggestions'] = False
        workspace_system_settings_model['spelling_auto_correct'] = False
        workspace_system_settings_model['system_entities'] = workspace_system_settings_system_entities_model
        workspace_system_settings_model['off_topic'] = workspace_system_settings_off_topic_model

        webhook_header_model = {} # WebhookHeader
        webhook_header_model['name'] = 'testString'
        webhook_header_model['value'] = 'testString'

        webhook_model = {} # Webhook
        webhook_model['url'] = 'testString'
        webhook_model['name'] = 'testString'
        webhook_model['headers'] = [webhook_header_model]

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        intent_model = {} # Intent
        intent_model['intent'] = 'testString'
        intent_model['description'] = 'testString'
        intent_model['created'] = "2019-01-01T12:00:00Z"
        intent_model['updated'] = "2019-01-01T12:00:00Z"
        intent_model['examples'] = [example_model]

        value_model = {} # Value
        value_model['value'] = 'testString'
        value_model['metadata'] = {}
        value_model['type'] = 'synonyms'
        value_model['synonyms'] = ['testString']
        value_model['patterns'] = ['testString']
        value_model['created'] = "2019-01-01T12:00:00Z"
        value_model['updated'] = "2019-01-01T12:00:00Z"

        entity_model = {} # Entity
        entity_model['entity'] = 'testString'
        entity_model['description'] = 'testString'
        entity_model['metadata'] = {}
        entity_model['fuzzy_match'] = True
        entity_model['created'] = "2019-01-01T12:00:00Z"
        entity_model['updated'] = "2019-01-01T12:00:00Z"
        entity_model['values'] = [value_model]

        # Construct a json representation of a Workspace model
        workspace_model_json = {}
        workspace_model_json['name'] = 'testString'
        workspace_model_json['description'] = 'testString'
        workspace_model_json['language'] = 'testString'
        workspace_model_json['workspace_id'] = 'testString'
        workspace_model_json['dialog_nodes'] = [dialog_node_model]
        workspace_model_json['counterexamples'] = [counterexample_model]
        workspace_model_json['created'] = "2019-01-01T12:00:00Z"
        workspace_model_json['updated'] = "2019-01-01T12:00:00Z"
        workspace_model_json['metadata'] = {}
        workspace_model_json['learning_opt_out'] = False
        workspace_model_json['system_settings'] = workspace_system_settings_model
        workspace_model_json['status'] = 'Non Existent'
        workspace_model_json['webhooks'] = [webhook_model]
        workspace_model_json['intents'] = [intent_model]
        workspace_model_json['entities'] = [entity_model]

        # Construct a model instance of Workspace by calling from_dict on the json representation
        workspace_model = Workspace.from_dict(workspace_model_json)
        assert workspace_model != False

        # Construct a model instance of Workspace by calling from_dict on the json representation
        workspace_model_dict = Workspace.from_dict(workspace_model_json).__dict__
        workspace_model2 = Workspace(**workspace_model_dict)

        # Verify the model instances are equivalent
        assert workspace_model == workspace_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_model_json2 = workspace_model.to_dict()
        assert workspace_model_json2 == workspace_model_json

class TestModel_WorkspaceCollection():
    """
    Test Class for WorkspaceCollection
    """

    def test_workspace_collection_serialization(self):
        """
        Test serialization/deserialization for WorkspaceCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        dialog_node_output_generic_model = {} # DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        dialog_node_output_generic_model['response_type'] = 'channel_transfer'
        dialog_node_output_generic_model['message_to_user'] = 'testString'
        dialog_node_output_generic_model['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_model['channels'] = [response_generic_channel_model]

        dialog_node_output_modifiers_model = {} # DialogNodeOutputModifiers
        dialog_node_output_modifiers_model['overwrite'] = True

        dialog_node_output_model = {} # DialogNodeOutput
        dialog_node_output_model['generic'] = [dialog_node_output_generic_model]
        dialog_node_output_model['integrations'] = {}
        dialog_node_output_model['modifiers'] = dialog_node_output_modifiers_model
        dialog_node_output_model['foo'] = 'testString'

        dialog_node_context_model = {} # DialogNodeContext
        dialog_node_context_model['integrations'] = {}
        dialog_node_context_model['foo'] = 'testString'

        dialog_node_next_step_model = {} # DialogNodeNextStep
        dialog_node_next_step_model['behavior'] = 'get_user_input'
        dialog_node_next_step_model['dialog_node'] = 'testString'
        dialog_node_next_step_model['selector'] = 'condition'

        dialog_node_action_model = {} # DialogNodeAction
        dialog_node_action_model['name'] = 'testString'
        dialog_node_action_model['type'] = 'client'
        dialog_node_action_model['parameters'] = {}
        dialog_node_action_model['result_variable'] = 'testString'
        dialog_node_action_model['credentials'] = 'testString'

        dialog_node_model = {} # DialogNode
        dialog_node_model['dialog_node'] = 'testString'
        dialog_node_model['description'] = 'testString'
        dialog_node_model['conditions'] = 'testString'
        dialog_node_model['parent'] = 'testString'
        dialog_node_model['previous_sibling'] = 'testString'
        dialog_node_model['output'] = dialog_node_output_model
        dialog_node_model['context'] = dialog_node_context_model
        dialog_node_model['metadata'] = {}
        dialog_node_model['next_step'] = dialog_node_next_step_model
        dialog_node_model['title'] = 'testString'
        dialog_node_model['type'] = 'standard'
        dialog_node_model['event_name'] = 'focus'
        dialog_node_model['variable'] = 'testString'
        dialog_node_model['actions'] = [dialog_node_action_model]
        dialog_node_model['digress_in'] = 'not_available'
        dialog_node_model['digress_out'] = 'allow_returning'
        dialog_node_model['digress_out_slots'] = 'not_allowed'
        dialog_node_model['user_label'] = 'testString'
        dialog_node_model['disambiguation_opt_out'] = False
        dialog_node_model['disabled'] = True
        dialog_node_model['created'] = "2019-01-01T12:00:00Z"
        dialog_node_model['updated'] = "2019-01-01T12:00:00Z"

        counterexample_model = {} # Counterexample
        counterexample_model['text'] = 'testString'
        counterexample_model['created'] = "2019-01-01T12:00:00Z"
        counterexample_model['updated'] = "2019-01-01T12:00:00Z"

        workspace_system_settings_tooling_model = {} # WorkspaceSystemSettingsTooling
        workspace_system_settings_tooling_model['store_generic_responses'] = True

        workspace_system_settings_disambiguation_model = {} # WorkspaceSystemSettingsDisambiguation
        workspace_system_settings_disambiguation_model['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['enabled'] = False
        workspace_system_settings_disambiguation_model['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model['randomize'] = True
        workspace_system_settings_disambiguation_model['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model['suggestion_text_policy'] = 'testString'

        workspace_system_settings_system_entities_model = {} # WorkspaceSystemSettingsSystemEntities
        workspace_system_settings_system_entities_model['enabled'] = False

        workspace_system_settings_off_topic_model = {} # WorkspaceSystemSettingsOffTopic
        workspace_system_settings_off_topic_model['enabled'] = False

        workspace_system_settings_model = {} # WorkspaceSystemSettings
        workspace_system_settings_model['tooling'] = workspace_system_settings_tooling_model
        workspace_system_settings_model['disambiguation'] = workspace_system_settings_disambiguation_model
        workspace_system_settings_model['human_agent_assist'] = {}
        workspace_system_settings_model['spelling_suggestions'] = False
        workspace_system_settings_model['spelling_auto_correct'] = False
        workspace_system_settings_model['system_entities'] = workspace_system_settings_system_entities_model
        workspace_system_settings_model['off_topic'] = workspace_system_settings_off_topic_model

        webhook_header_model = {} # WebhookHeader
        webhook_header_model['name'] = 'testString'
        webhook_header_model['value'] = 'testString'

        webhook_model = {} # Webhook
        webhook_model['url'] = 'testString'
        webhook_model['name'] = 'testString'
        webhook_model['headers'] = [webhook_header_model]

        mention_model = {} # Mention
        mention_model['entity'] = 'testString'
        mention_model['location'] = [38]

        example_model = {} # Example
        example_model['text'] = 'testString'
        example_model['mentions'] = [mention_model]
        example_model['created'] = "2019-01-01T12:00:00Z"
        example_model['updated'] = "2019-01-01T12:00:00Z"

        intent_model = {} # Intent
        intent_model['intent'] = 'testString'
        intent_model['description'] = 'testString'
        intent_model['created'] = "2019-01-01T12:00:00Z"
        intent_model['updated'] = "2019-01-01T12:00:00Z"
        intent_model['examples'] = [example_model]

        value_model = {} # Value
        value_model['value'] = 'testString'
        value_model['metadata'] = {}
        value_model['type'] = 'synonyms'
        value_model['synonyms'] = ['testString']
        value_model['patterns'] = ['testString']
        value_model['created'] = "2019-01-01T12:00:00Z"
        value_model['updated'] = "2019-01-01T12:00:00Z"

        entity_model = {} # Entity
        entity_model['entity'] = 'testString'
        entity_model['description'] = 'testString'
        entity_model['metadata'] = {}
        entity_model['fuzzy_match'] = True
        entity_model['created'] = "2019-01-01T12:00:00Z"
        entity_model['updated'] = "2019-01-01T12:00:00Z"
        entity_model['values'] = [value_model]

        workspace_model = {} # Workspace
        workspace_model['name'] = 'testString'
        workspace_model['description'] = 'testString'
        workspace_model['language'] = 'testString'
        workspace_model['workspace_id'] = 'testString'
        workspace_model['dialog_nodes'] = [dialog_node_model]
        workspace_model['counterexamples'] = [counterexample_model]
        workspace_model['created'] = "2019-01-01T12:00:00Z"
        workspace_model['updated'] = "2019-01-01T12:00:00Z"
        workspace_model['metadata'] = {}
        workspace_model['learning_opt_out'] = False
        workspace_model['system_settings'] = workspace_system_settings_model
        workspace_model['status'] = 'Non Existent'
        workspace_model['webhooks'] = [webhook_model]
        workspace_model['intents'] = [intent_model]
        workspace_model['entities'] = [entity_model]

        pagination_model = {} # Pagination
        pagination_model['refresh_url'] = 'testString'
        pagination_model['next_url'] = 'testString'
        pagination_model['total'] = 38
        pagination_model['matched'] = 38
        pagination_model['refresh_cursor'] = 'testString'
        pagination_model['next_cursor'] = 'testString'

        # Construct a json representation of a WorkspaceCollection model
        workspace_collection_model_json = {}
        workspace_collection_model_json['workspaces'] = [workspace_model]
        workspace_collection_model_json['pagination'] = pagination_model

        # Construct a model instance of WorkspaceCollection by calling from_dict on the json representation
        workspace_collection_model = WorkspaceCollection.from_dict(workspace_collection_model_json)
        assert workspace_collection_model != False

        # Construct a model instance of WorkspaceCollection by calling from_dict on the json representation
        workspace_collection_model_dict = WorkspaceCollection.from_dict(workspace_collection_model_json).__dict__
        workspace_collection_model2 = WorkspaceCollection(**workspace_collection_model_dict)

        # Verify the model instances are equivalent
        assert workspace_collection_model == workspace_collection_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_collection_model_json2 = workspace_collection_model.to_dict()
        assert workspace_collection_model_json2 == workspace_collection_model_json

class TestModel_WorkspaceSystemSettings():
    """
    Test Class for WorkspaceSystemSettings
    """

    def test_workspace_system_settings_serialization(self):
        """
        Test serialization/deserialization for WorkspaceSystemSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        workspace_system_settings_tooling_model = {} # WorkspaceSystemSettingsTooling
        workspace_system_settings_tooling_model['store_generic_responses'] = True

        workspace_system_settings_disambiguation_model = {} # WorkspaceSystemSettingsDisambiguation
        workspace_system_settings_disambiguation_model['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model['enabled'] = False
        workspace_system_settings_disambiguation_model['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model['randomize'] = True
        workspace_system_settings_disambiguation_model['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model['suggestion_text_policy'] = 'testString'

        workspace_system_settings_system_entities_model = {} # WorkspaceSystemSettingsSystemEntities
        workspace_system_settings_system_entities_model['enabled'] = False

        workspace_system_settings_off_topic_model = {} # WorkspaceSystemSettingsOffTopic
        workspace_system_settings_off_topic_model['enabled'] = False

        # Construct a json representation of a WorkspaceSystemSettings model
        workspace_system_settings_model_json = {}
        workspace_system_settings_model_json['tooling'] = workspace_system_settings_tooling_model
        workspace_system_settings_model_json['disambiguation'] = workspace_system_settings_disambiguation_model
        workspace_system_settings_model_json['human_agent_assist'] = {}
        workspace_system_settings_model_json['spelling_suggestions'] = False
        workspace_system_settings_model_json['spelling_auto_correct'] = False
        workspace_system_settings_model_json['system_entities'] = workspace_system_settings_system_entities_model
        workspace_system_settings_model_json['off_topic'] = workspace_system_settings_off_topic_model

        # Construct a model instance of WorkspaceSystemSettings by calling from_dict on the json representation
        workspace_system_settings_model = WorkspaceSystemSettings.from_dict(workspace_system_settings_model_json)
        assert workspace_system_settings_model != False

        # Construct a model instance of WorkspaceSystemSettings by calling from_dict on the json representation
        workspace_system_settings_model_dict = WorkspaceSystemSettings.from_dict(workspace_system_settings_model_json).__dict__
        workspace_system_settings_model2 = WorkspaceSystemSettings(**workspace_system_settings_model_dict)

        # Verify the model instances are equivalent
        assert workspace_system_settings_model == workspace_system_settings_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_system_settings_model_json2 = workspace_system_settings_model.to_dict()
        assert workspace_system_settings_model_json2 == workspace_system_settings_model_json

class TestModel_WorkspaceSystemSettingsDisambiguation():
    """
    Test Class for WorkspaceSystemSettingsDisambiguation
    """

    def test_workspace_system_settings_disambiguation_serialization(self):
        """
        Test serialization/deserialization for WorkspaceSystemSettingsDisambiguation
        """

        # Construct a json representation of a WorkspaceSystemSettingsDisambiguation model
        workspace_system_settings_disambiguation_model_json = {}
        workspace_system_settings_disambiguation_model_json['prompt'] = 'testString'
        workspace_system_settings_disambiguation_model_json['none_of_the_above_prompt'] = 'testString'
        workspace_system_settings_disambiguation_model_json['enabled'] = False
        workspace_system_settings_disambiguation_model_json['sensitivity'] = 'auto'
        workspace_system_settings_disambiguation_model_json['randomize'] = True
        workspace_system_settings_disambiguation_model_json['max_suggestions'] = 1
        workspace_system_settings_disambiguation_model_json['suggestion_text_policy'] = 'testString'

        # Construct a model instance of WorkspaceSystemSettingsDisambiguation by calling from_dict on the json representation
        workspace_system_settings_disambiguation_model = WorkspaceSystemSettingsDisambiguation.from_dict(workspace_system_settings_disambiguation_model_json)
        assert workspace_system_settings_disambiguation_model != False

        # Construct a model instance of WorkspaceSystemSettingsDisambiguation by calling from_dict on the json representation
        workspace_system_settings_disambiguation_model_dict = WorkspaceSystemSettingsDisambiguation.from_dict(workspace_system_settings_disambiguation_model_json).__dict__
        workspace_system_settings_disambiguation_model2 = WorkspaceSystemSettingsDisambiguation(**workspace_system_settings_disambiguation_model_dict)

        # Verify the model instances are equivalent
        assert workspace_system_settings_disambiguation_model == workspace_system_settings_disambiguation_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_system_settings_disambiguation_model_json2 = workspace_system_settings_disambiguation_model.to_dict()
        assert workspace_system_settings_disambiguation_model_json2 == workspace_system_settings_disambiguation_model_json

class TestModel_WorkspaceSystemSettingsOffTopic():
    """
    Test Class for WorkspaceSystemSettingsOffTopic
    """

    def test_workspace_system_settings_off_topic_serialization(self):
        """
        Test serialization/deserialization for WorkspaceSystemSettingsOffTopic
        """

        # Construct a json representation of a WorkspaceSystemSettingsOffTopic model
        workspace_system_settings_off_topic_model_json = {}
        workspace_system_settings_off_topic_model_json['enabled'] = False

        # Construct a model instance of WorkspaceSystemSettingsOffTopic by calling from_dict on the json representation
        workspace_system_settings_off_topic_model = WorkspaceSystemSettingsOffTopic.from_dict(workspace_system_settings_off_topic_model_json)
        assert workspace_system_settings_off_topic_model != False

        # Construct a model instance of WorkspaceSystemSettingsOffTopic by calling from_dict on the json representation
        workspace_system_settings_off_topic_model_dict = WorkspaceSystemSettingsOffTopic.from_dict(workspace_system_settings_off_topic_model_json).__dict__
        workspace_system_settings_off_topic_model2 = WorkspaceSystemSettingsOffTopic(**workspace_system_settings_off_topic_model_dict)

        # Verify the model instances are equivalent
        assert workspace_system_settings_off_topic_model == workspace_system_settings_off_topic_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_system_settings_off_topic_model_json2 = workspace_system_settings_off_topic_model.to_dict()
        assert workspace_system_settings_off_topic_model_json2 == workspace_system_settings_off_topic_model_json

class TestModel_WorkspaceSystemSettingsSystemEntities():
    """
    Test Class for WorkspaceSystemSettingsSystemEntities
    """

    def test_workspace_system_settings_system_entities_serialization(self):
        """
        Test serialization/deserialization for WorkspaceSystemSettingsSystemEntities
        """

        # Construct a json representation of a WorkspaceSystemSettingsSystemEntities model
        workspace_system_settings_system_entities_model_json = {}
        workspace_system_settings_system_entities_model_json['enabled'] = False

        # Construct a model instance of WorkspaceSystemSettingsSystemEntities by calling from_dict on the json representation
        workspace_system_settings_system_entities_model = WorkspaceSystemSettingsSystemEntities.from_dict(workspace_system_settings_system_entities_model_json)
        assert workspace_system_settings_system_entities_model != False

        # Construct a model instance of WorkspaceSystemSettingsSystemEntities by calling from_dict on the json representation
        workspace_system_settings_system_entities_model_dict = WorkspaceSystemSettingsSystemEntities.from_dict(workspace_system_settings_system_entities_model_json).__dict__
        workspace_system_settings_system_entities_model2 = WorkspaceSystemSettingsSystemEntities(**workspace_system_settings_system_entities_model_dict)

        # Verify the model instances are equivalent
        assert workspace_system_settings_system_entities_model == workspace_system_settings_system_entities_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_system_settings_system_entities_model_json2 = workspace_system_settings_system_entities_model.to_dict()
        assert workspace_system_settings_system_entities_model_json2 == workspace_system_settings_system_entities_model_json

class TestModel_WorkspaceSystemSettingsTooling():
    """
    Test Class for WorkspaceSystemSettingsTooling
    """

    def test_workspace_system_settings_tooling_serialization(self):
        """
        Test serialization/deserialization for WorkspaceSystemSettingsTooling
        """

        # Construct a json representation of a WorkspaceSystemSettingsTooling model
        workspace_system_settings_tooling_model_json = {}
        workspace_system_settings_tooling_model_json['store_generic_responses'] = True

        # Construct a model instance of WorkspaceSystemSettingsTooling by calling from_dict on the json representation
        workspace_system_settings_tooling_model = WorkspaceSystemSettingsTooling.from_dict(workspace_system_settings_tooling_model_json)
        assert workspace_system_settings_tooling_model != False

        # Construct a model instance of WorkspaceSystemSettingsTooling by calling from_dict on the json representation
        workspace_system_settings_tooling_model_dict = WorkspaceSystemSettingsTooling.from_dict(workspace_system_settings_tooling_model_json).__dict__
        workspace_system_settings_tooling_model2 = WorkspaceSystemSettingsTooling(**workspace_system_settings_tooling_model_dict)

        # Verify the model instances are equivalent
        assert workspace_system_settings_tooling_model == workspace_system_settings_tooling_model2

        # Convert model instance back to dict and verify no loss of data
        workspace_system_settings_tooling_model_json2 = workspace_system_settings_tooling_model.to_dict()
        assert workspace_system_settings_tooling_model_json2 == workspace_system_settings_tooling_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer
        """

        # Construct dict forms of any model objects needed in order to build this model.

        channel_transfer_target_chat_model = {} # ChannelTransferTargetChat
        channel_transfer_target_chat_model['url'] = 'testString'

        channel_transfer_target_model = {} # ChannelTransferTarget
        channel_transfer_target_model['chat'] = channel_transfer_target_chat_model

        channel_transfer_info_model = {} # ChannelTransferInfo
        channel_transfer_info_model['target'] = channel_transfer_target_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer model
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json['response_type'] = 'channel_transfer'
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json['message_to_user'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json['transfer_info'] = channel_transfer_info_model
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer.from_dict(dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer.from_dict(dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer(**dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model == dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_channel_transfer_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent
        """

        # Construct dict forms of any model objects needed in order to build this model.

        agent_availability_message_model = {} # AgentAvailabilityMessage
        agent_availability_message_model['message'] = 'testString'

        dialog_node_output_connect_to_agent_transfer_info_model = {} # DialogNodeOutputConnectToAgentTransferInfo
        dialog_node_output_connect_to_agent_transfer_info_model['target'] = {}

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent model
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['response_type'] = 'connect_to_agent'
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['message_to_human_agent'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['agent_available'] = agent_availability_message_model
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['agent_unavailable'] = agent_availability_message_model
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['transfer_info'] = dialog_node_output_connect_to_agent_transfer_info_model
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent.from_dict(dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent.from_dict(dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent(**dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model == dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_connect_to_agent_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeImage():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeImage
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_image_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeImage
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeImage model
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['response_type'] = 'image'
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['source'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['title'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['description'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['channels'] = [response_generic_channel_model]
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json['alt_text'] = 'testString'

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeImage by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_image_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeImage.from_dict(dialog_node_output_generic_dialog_node_output_response_type_image_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_image_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeImage by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_image_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeImage.from_dict(dialog_node_output_generic_dialog_node_output_response_type_image_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_image_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeImage(**dialog_node_output_generic_dialog_node_output_response_type_image_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_image_model == dialog_node_output_generic_dialog_node_output_response_type_image_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_image_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_image_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_image_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_image_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeOption():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeOption
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_option_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeOption
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeOption model
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['response_type'] = 'option'
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['title'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['description'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['preference'] = 'dropdown'
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['options'] = [dialog_node_output_options_element_model]
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeOption by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_option_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeOption.from_dict(dialog_node_output_generic_dialog_node_output_response_type_option_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_option_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeOption by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_option_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeOption.from_dict(dialog_node_output_generic_dialog_node_output_response_type_option_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_option_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeOption(**dialog_node_output_generic_dialog_node_output_response_type_option_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_option_model == dialog_node_output_generic_dialog_node_output_response_type_option_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_option_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_option_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_option_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_option_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypePause():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypePause
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_pause_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypePause
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypePause model
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json['response_type'] = 'pause'
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json['time'] = 38
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json['typing'] = True
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypePause by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_pause_model = DialogNodeOutputGenericDialogNodeOutputResponseTypePause.from_dict(dialog_node_output_generic_dialog_node_output_response_type_pause_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_pause_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypePause by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypePause.from_dict(dialog_node_output_generic_dialog_node_output_response_type_pause_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_pause_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypePause(**dialog_node_output_generic_dialog_node_output_response_type_pause_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_pause_model == dialog_node_output_generic_dialog_node_output_response_type_pause_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_pause_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_pause_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_pause_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_pause_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_search_skill_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill model
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['response_type'] = 'search_skill'
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['query'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['query_type'] = 'natural_language'
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['filter'] = 'testString'
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['discovery_version'] = '2018-12-03'
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill.from_dict(dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_search_skill_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill.from_dict(dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill(**dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_search_skill_model == dialog_node_output_generic_dialog_node_output_response_type_search_skill_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_search_skill_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_search_skill_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeText():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeText
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_text_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeText
        """

        # Construct dict forms of any model objects needed in order to build this model.

        dialog_node_output_text_values_element_model = {} # DialogNodeOutputTextValuesElement
        dialog_node_output_text_values_element_model['text'] = 'testString'

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeText model
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json['response_type'] = 'text'
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json['values'] = [dialog_node_output_text_values_element_model]
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json['selection_policy'] = 'sequential'
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json['delimiter'] = '\n'
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeText by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_text_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeText.from_dict(dialog_node_output_generic_dialog_node_output_response_type_text_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_text_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeText by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_text_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeText.from_dict(dialog_node_output_generic_dialog_node_output_response_type_text_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_text_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeText(**dialog_node_output_generic_dialog_node_output_response_type_text_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_text_model == dialog_node_output_generic_dialog_node_output_response_type_text_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_text_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_text_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_text_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_text_model_json

class TestModel_DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined():
    """
    Test Class for DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined
    """

    def test_dialog_node_output_generic_dialog_node_output_response_type_user_defined_serialization(self):
        """
        Test serialization/deserialization for DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined
        """

        # Construct dict forms of any model objects needed in order to build this model.

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined model
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json = {}
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json['response_type'] = 'user_defined'
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json['user_defined'] = {}
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json['channels'] = [response_generic_channel_model]

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model = DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined.from_dict(dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json)
        assert dialog_node_output_generic_dialog_node_output_response_type_user_defined_model != False

        # Construct a model instance of DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined by calling from_dict on the json representation
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_dict = DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined.from_dict(dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json).__dict__
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model2 = DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined(**dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_dict)

        # Verify the model instances are equivalent
        assert dialog_node_output_generic_dialog_node_output_response_type_user_defined_model == dialog_node_output_generic_dialog_node_output_response_type_user_defined_model2

        # Convert model instance back to dict and verify no loss of data
        dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json2 = dialog_node_output_generic_dialog_node_output_response_type_user_defined_model.to_dict()
        assert dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json2 == dialog_node_output_generic_dialog_node_output_response_type_user_defined_model_json

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
        response_generic_channel_model['channel'] = 'chat'

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
        response_generic_channel_model['channel'] = 'chat'

        # Construct a json representation of a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json = {}
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['response_type'] = 'connect_to_agent'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['message_to_human_agent'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_available'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['agent_unavailable'] = agent_availability_message_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['transfer_info'] = dialog_node_output_connect_to_agent_transfer_info_model
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['topic'] = 'testString'
        runtime_response_generic_runtime_response_type_connect_to_agent_model_json['dialog_node'] = 'testString'
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
        response_generic_channel_model['channel'] = 'chat'

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

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_node_output_options_element_value_model = {} # DialogNodeOutputOptionsElementValue
        dialog_node_output_options_element_value_model['input'] = message_input_model
        dialog_node_output_options_element_value_model['intents'] = [runtime_intent_model]
        dialog_node_output_options_element_value_model['entities'] = [runtime_entity_model]

        dialog_node_output_options_element_model = {} # DialogNodeOutputOptionsElement
        dialog_node_output_options_element_model['label'] = 'testString'
        dialog_node_output_options_element_model['value'] = dialog_node_output_options_element_value_model

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

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
        response_generic_channel_model['channel'] = 'chat'

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

class TestModel_RuntimeResponseGenericRuntimeResponseTypeSuggestion():
    """
    Test Class for RuntimeResponseGenericRuntimeResponseTypeSuggestion
    """

    def test_runtime_response_generic_runtime_response_type_suggestion_serialization(self):
        """
        Test serialization/deserialization for RuntimeResponseGenericRuntimeResponseTypeSuggestion
        """

        # Construct dict forms of any model objects needed in order to build this model.

        message_input_model = {} # MessageInput
        message_input_model['text'] = 'testString'
        message_input_model['spelling_suggestions'] = False
        message_input_model['spelling_auto_correct'] = False
        message_input_model['suggested_text'] = 'testString'
        message_input_model['original_text'] = 'testString'
        message_input_model['foo'] = 'testString'

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

        dialog_suggestion_value_model = {} # DialogSuggestionValue
        dialog_suggestion_value_model['input'] = message_input_model
        dialog_suggestion_value_model['intents'] = [runtime_intent_model]
        dialog_suggestion_value_model['entities'] = [runtime_entity_model]

        dialog_suggestion_model = {} # DialogSuggestion
        dialog_suggestion_model['label'] = 'testString'
        dialog_suggestion_model['value'] = dialog_suggestion_value_model
        dialog_suggestion_model['output'] = {}
        dialog_suggestion_model['dialog_node'] = 'testString'

        response_generic_channel_model = {} # ResponseGenericChannel
        response_generic_channel_model['channel'] = 'chat'

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
        response_generic_channel_model['channel'] = 'chat'

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
        response_generic_channel_model['channel'] = 'chat'

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
