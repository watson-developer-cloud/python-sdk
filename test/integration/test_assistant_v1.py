# coding: utf-8
from unittest import TestCase
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator, BearerTokenAuthenticator
from os.path import abspath
import os
import ibm_watson
import pytest
import json

@pytest.mark.skipif(os.getenv('ASSISTANT_APIKEY') is None,
                    reason='requires ASSISTANT_APIKEY')
class TestAssistantV1(TestCase):

    @classmethod
    def setup_class(cls):

        create_workspace_data = {
            "name":
            "test_workspace",
            "description":
            "integration tests",
            "language":
            "en",
            "intents": [{
                "intent": "hello",
                "description": "string",
                "examples": [{
                    "text": "good morning"
                }]
            }],
            "entities": [{
                "entity": "pizza_toppings",
                "description": "Tasty pizza toppings",
                "metadata": {
                    "property": "value"
                }
            }],
            "counterexamples": [{
                "text": "string"
            }],
            "metadata": {},
        }

        authenticator = IAMAuthenticator(os.getenv('ASSISTANT_APIKEY'))
        cls.assistant = ibm_watson.AssistantV1(
            version='2018-07-10',
            authenticator=authenticator
        )
        cls.assistant.set_default_headers({
            'X-Watson-Learning-Opt-Out': '1',
            'X-Watson-Test': '1'
        })

        response = cls.assistant.create_workspace(
            name=create_workspace_data['name'],
            description=create_workspace_data['description'],
            language='en',
            intents=create_workspace_data['intents'],
            entities=create_workspace_data['entities'],
            counterexamples=create_workspace_data['counterexamples'],
            metadata=create_workspace_data['metadata']).get_result()

        cls.workspace_id = response['workspace_id']

        examples = [{"text": "good morning"}]
        response = cls.assistant.create_intent(
            workspace_id=cls.workspace_id,
            intent='test_intent',
            description='Test intent.',
            examples=examples).get_result()

    @classmethod
    def teardown_class(cls):
        response = cls.assistant.delete_intent(workspace_id=cls.workspace_id, intent='updated_test_intent').get_result()
        assert response is not None

        response = cls.assistant.delete_workspace(cls.workspace_id).get_result()
        assert response is not None

    def test_workspace(self):
        response = self.assistant.get_workspace(self.workspace_id, export=True).get_result()
        assert response is not None

        response = self.assistant.list_workspaces().get_result()
        assert response is not None
        print(json.dumps(response, indent=2))

        response = self.assistant.message(self.workspace_id,
            input={
                'text': 'What\'s the weather like?'
            },
            context={
                'metadata': {
                    'deployment': 'myDeployment'
                }
            }).get_result()
        assert response is not None

        response = self.assistant.update_workspace(workspace_id=self.workspace_id, description='Updated test workspace.').get_result()
        assert response is not None

    def test_intent(self):
        response = self.assistant.get_intent(
            workspace_id=self.workspace_id, intent='test_intent', export=True).get_result()
        assert response is not None

        response = self.assistant.update_intent(
            workspace_id=self.workspace_id,
            intent='test_intent',
            new_intent='updated_test_intent',
            new_description='Updated test intent.').get_result()
        assert response is not None

        response = self.assistant.list_intents(
            workspace_id=self.workspace_id, export=True).get_result()
        assert response is not None
        print(json.dumps(response, indent=2))
