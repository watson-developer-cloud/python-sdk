# coding: utf-8

# Copyright 2019, 2024 IBM All Rights Reserved.
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

from unittest import TestCase
import ibm_watson
from ibm_watson.assistant_v2 import MessageInput
from ibm_watson.common import parse_sse_stream_data
import pytest
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

class TestAssistantV2(TestCase):

    def setUp(self):
        
        with open('./auth.json') as f:
            data = json.load(f)
            assistant_auth = data.get("assistantv2")
            self.assistant_id = assistant_auth.get("assistantId")
            self.environment_id = assistant_auth.get("environmentId")

            self.authenticator = IAMAuthenticator(apikey=assistant_auth.get("apikey"))
            self.assistant = ibm_watson.AssistantV2(version='2024-08-25', authenticator=self.authenticator)
            self.assistant.set_service_url(assistant_auth.get("serviceUrl"))
            self.assistant.set_default_headers({
                'X-Watson-Learning-Opt-Out': '1',
                'X-Watson-Test': '1'
            })

    def test_list_assistants(self):
        response = self.assistant.list_assistants().get_result()
        assert response is not None

    def test_message_stream_stateless(self):
        input = MessageInput(message_type="text", text="can you list the steps to create a custom extension?")
        user_id = "Angelo"

        response = self.assistant.message_stream_stateless(self.assistant_id, self.environment_id, input=input, user_id=user_id).get_result()

        for data in parse_sse_stream_data(response):
            # One of these items must exist
            # assert "partial_item" in data_json or "complete_item" in data_json or "final_item" in data_json

            if "partial_item" in data:
                assert data["partial_item"]["text"] is not None
            elif "complete_item" in data:
                assert data["complete_item"]["text"] is not None
            elif "final_response" in data:
                assert data["final_response"] is not None
            else:
                pytest.fail("Should be impossible to get here")

