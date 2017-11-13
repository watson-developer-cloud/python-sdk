# Copyright 2017 IBM All Rights Reserved.
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

import json
import datetime
from dateutil.tz import tzutc
import responses
import watson_developer_cloud
from watson_developer_cloud import WatsonException
from watson_developer_cloud import WatsonApiException
from watson_developer_cloud.conversation_v1 import Context, Counterexample, \
    CounterexampleCollection, Entity, EntityCollection, Example, \
    ExampleCollection, InputData, Intent, IntentCollection, Synonym, \
    SynonymCollection, Value, ValueCollection, Workspace, WorkspaceCollection

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/conversation/api'
base_url = '{0}{1}'.format(platform_url, service_path)

#########################
# counterexamples
#########################


@responses.activate
def test_create_counterexample():
    endpoint = '/v1/workspaces/{0}/counterexamples'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "I want financial advice today.",
        "created": "2016-07-11T16:39:01.774Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    counterexample = service.create_counterexample(
        workspace_id='boguswid', text='I want financial advice today.')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample == response
    # Verify that response can be converted to a Counterexample
    Counterexample._from_dict(counterexample)

@responses.activate
def test_rate_limit_exceeded():
    endpoint = '/v1/workspaces/{0}/counterexamples'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    error_code = 429
    error_msg = 'Rate limit exceeded'
    responses.add(
        responses.POST,
        url,
        body='Rate limit exceeded',
        status=429,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    try:
        service.create_counterexample(
            workspace_id='boguswid', text='I want financial advice today.')
    except WatsonException as ex:
        assert len(responses.calls) == 1
        assert isinstance(ex, WatsonApiException)
        assert error_code == ex.code
        assert error_msg in str(ex)

@responses.activate
def test_unknown_error():
    endpoint = '/v1/workspaces/{0}/counterexamples'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    error_msg = 'Unknown error'
    responses.add(
        responses.POST,
        url,
        status=407,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    try:
        service.create_counterexample(
            workspace_id='boguswid', text='I want financial advice today.')
    except WatsonException as ex:
        assert len(responses.calls) == 1
        assert error_msg in str(ex)

@responses.activate
def test_delete_counterexample():
    endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(
        'boguswid', 'I%20want%20financial%20advice%20today')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {}
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    counterexample = service.delete_counterexample(
        workspace_id='boguswid', text='I want financial advice today')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample is None


@responses.activate
def test_get_counterexample():
    endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(
        'boguswid', 'What%20are%20you%20wearing%3F')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "What are you wearing?",
        "created": "2016-07-11T23:53:59.153Z",
        "updated": "2016-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    counterexample = service.get_counterexample(
        workspace_id='boguswid', text='What are you wearing?')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample == response
    # Verify that response can be converted to a Counterexample
    Counterexample._from_dict(counterexample)

@responses.activate
def test_list_counterexamples():
    endpoint = '/v1/workspaces/{0}/counterexamples'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "counterexamples": [{
            "text": "I want financial advice today.",
            "created": "2016-07-11T16:39:01.774Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }, {
            "text": "What are you wearing today",
            "created": "2016-07-11T16:39:01.774Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/counterexamples?version=2017-12-18&page_limit=2",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/counterexamples?cursor=base64=&version=2017-12-18&page_limit=2"
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    counterexamples = service.list_counterexamples(workspace_id='boguswid')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexamples == response
    # Verify that response can be converted to a CounterexampleCollection
    CounterexampleCollection._from_dict(counterexamples)

@responses.activate
def test_update_counterexample():
    endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format(
        'boguswid', 'What%20are%20you%20wearing%3F')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "What are you wearing?",
        "created": "2016-07-11T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    counterexample = service.update_counterexample(
        workspace_id='boguswid',
        text='What are you wearing?',
        new_text='What are you wearing?')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample == response
    # Verify that response can be converted to a Counterexample
    Counterexample._from_dict(counterexample)

#########################
# entities
#########################


@responses.activate
def test_create_entity():
    endpoint = '/v1/workspaces/{0}/entities'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "created": "2015-12-06T04:32:20.000Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "metadata": {
            "property": "value"
        }
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    entity = service.create_entity(
        workspace_id='boguswid',
        entity='pizza_toppings',
        description='Tasty pizza toppings',
        metadata={"property": "value"},
        values=None,
        fuzzy_match=None)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert entity == response
    # Verify that response can be converted to an Entity
    Entity._from_dict(entity)

@responses.activate
def test_delete_entity():
    endpoint = '/v1/workspaces/{0}/entities/{1}'.format('boguswid', 'pizza_toppings')
    url = '{0}{1}'.format(base_url, endpoint)
    response = ""
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    entity = service.delete_entity(workspace_id='boguswid', entity='pizza_toppings')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert entity is None


@responses.activate
def test_get_entity():
    endpoint = '/v1/workspaces/{0}/entities/{1}'.format('boguswid', 'pizza_toppings')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "created": "2015-12-06T04:32:20.000Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "metadata": {
            "property": "value"
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    entity = service.get_entity(workspace_id='boguswid', entity='pizza_toppings', export=True)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert entity == response
    # Verify that response can be converted to an Entity
    Entity._from_dict(entity)


@responses.activate
def test_list_entities():
    endpoint = '/v1/workspaces/{0}/entities'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "entities": [{
            "entity": "pizza_toppings",
            "description": "Tasty pizza toppings",
            "created": "2015-12-06T04:32:20.000Z",
            "updated": "2015-12-07T18:53:59.153Z",
            "metadata": {
                "property": "value"
            }
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/entities?version=2017-12-18&filter=name:pizza&include_count=true&page_limit=1",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/entities?cursor=base64=&version=2017-12-18&filter=name:pizza&page_limit=1",
            "total":
            1,
            "matched":
            1
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    entities = service.list_entities(
        workspace_id='boguswid',
        export=True)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert entities == response
    # Verify that response can be converted to an EntityCollection
    EntityCollection._from_dict(entities)


@responses.activate
def test_update_entity():
    endpoint = '/v1/workspaces/{0}/entities/{1}'.format('boguswid', 'pizza_toppings')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "created": "2015-12-06T04:32:20.000Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "metadata": {
            "property": "value"
        }
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    entity = service.update_entity(
        workspace_id='boguswid',
        entity='pizza_toppings',
        new_entity='pizza_toppings')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert entity == response
    # Verify that response can be converted to an Entity
    Entity._from_dict(entity)


#########################
# examples
#########################


@responses.activate
def test_create_example():
    endpoint = '/v1/workspaces/{0}/intents/{1}/examples'.format(
        'boguswid', 'pizza_order')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "Gimme a pizza with pepperoni",
        "created": "2016-07-11T16:39:01.774Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    example = service.create_example(
        workspace_id='boguswid',
        intent='pizza_order',
        text='Gimme a pizza with pepperoni')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert example == response
    # Verify that response can be converted to an Example
    Example._from_dict(example)


@responses.activate
def test_delete_example():
    endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
        'boguswid', 'pizza_order', 'Gimme%20a%20pizza%20with%20pepperoni')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {}
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    example = service.delete_example(
        workspace_id='boguswid',
        intent='pizza_order',
        text='Gimme a pizza with pepperoni')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert example is None


@responses.activate
def test_get_example():
    endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
        'boguswid', 'pizza_order', 'Gimme%20a%20pizza%20with%20pepperoni')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "Gimme a pizza with pepperoni",
        "created": "2016-07-11T23:53:59.153Z",
        "updated": "2016-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    example = service.get_example(
        workspace_id='boguswid',
        intent='pizza_order',
        text='Gimme a pizza with pepperoni')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert example == response
    # Verify that response can be converted to an Example
    Example._from_dict(example)


@responses.activate
def test_list_examples():
    endpoint = '/v1/workspaces/{0}/intents/{1}/examples'.format(
        'boguswid', 'pizza_order')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "examples": [{
            "text": "Can I order a pizza?",
            "created": "2016-07-11T16:39:01.774Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }, {
            "text": "Gimme a pizza with pepperoni",
            "created": "2016-07-11T16:39:01.774Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/intents/order/examples?version=2017-12-18&page_limit=2",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/intents/order/examples?cursor=base64=&version=2017-12-18&page_limit=2"
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    examples = service.list_examples(
        workspace_id='boguswid', intent='pizza_order')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert examples == response
    # Verify that response can be converted to an ExampleCollection
    ExampleCollection._from_dict(examples)


@responses.activate
def test_update_example():
    endpoint = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
        'boguswid', 'pizza_order', 'Gimme%20a%20pizza%20with%20pepperoni')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "text": "Gimme a pizza with pepperoni",
        "created": "2016-07-11T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    example = service.update_example(
        workspace_id='boguswid',
        intent='pizza_order',
        text='Gimme a pizza with pepperoni',
        new_text='Gimme a pizza with pepperoni')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert example == response
    # Verify that response can be converted to an Example
    Example._from_dict(example)


#########################
# intents
#########################


@responses.activate
def test_create_intent():
    endpoint = '/v1/workspaces/{0}/intents'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "intent": "pizza_order",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "description": "User wants to start a new pizza order"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    intent = service.create_intent(
        workspace_id='boguswid',
        intent='pizza_order',
        description='User wants to start a new pizza order')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intent == response
    # Verify that response can be converted to an Intent
    Intent._from_dict(intent)


@responses.activate
def test_delete_intent():
    endpoint = '/v1/workspaces/{0}/intents/{1}'.format('boguswid',
                                                       'pizza_order')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {}
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    intent = service.delete_intent(
        workspace_id='boguswid', intent='pizza_order')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intent is None


@responses.activate
def test_get_intent():
    endpoint = '/v1/workspaces/{0}/intents/{1}'.format('boguswid',
                                                       'pizza_order')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "intent": "pizza_order",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "description": "User wants to start a new pizza order"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    intent = service.get_intent(
        workspace_id='boguswid', intent='pizza_order', export=False)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intent == response
    # Verify that response can be converted to an Intent
    Intent._from_dict(intent)

@responses.activate
def test_list_intents():
    endpoint = '/v1/workspaces/{0}/intents'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "intents": [{
            "intent": "pizza_order",
            "created": "2015-12-06T23:53:59.153Z",
            "updated": "2015-12-07T18:53:59.153Z",
            "description": "User wants to start a new pizza order"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/intents?version=2017-12-18&page_limit=1",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/intents?cursor=base64=&version=2017-12-18&page_limit=1"
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    intents = service.list_intents(workspace_id='boguswid', export=False)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intents == response
    # Verify that response can be converted to an IntentCollection
    IntentCollection._from_dict(intents)

@responses.activate
def test_update_intent():
    endpoint = '/v1/workspaces/{0}/intents/{1}'.format('boguswid',
                                                       'pizza_order')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "intent": "pizza_order",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z",
        "description": "User wants to start a new pizza order"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    intent = service.update_intent(
        workspace_id='boguswid',
        intent='pizza_order',
        new_intent='pizza_order',
        new_description='User wants to start a new pizza order')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intent == response
    # Verify that response can be converted to an Intent
    Intent._from_dict(intent)

def test_intent_models():
    intent = Intent(intent_name="pizza_order",
                    created=datetime.datetime(2015, 12, 6, 23, 53, 59, 15300, tzinfo=tzutc()),
                    updated=datetime.datetime(2015, 12, 7, 18, 53, 59, 15300, tzinfo=tzutc()),
                    description="User wants to start a new pizza order")
    intentDict = intent._to_dict()
    check = Intent._from_dict(intentDict)
    assert intent == check


#########################
# logs
#########################


@responses.activate
def test_list_logs():
    endpoint = '/v1/workspaces/{0}/logs'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "logs": [{
            "request": {
                "input": {
                    "text": "Can you turn off the AC"
                },
                "context": {
                    "conversation_id": "f2c7e362-4cc8-4761-8b0f-9ccd70c63bca",
                    "system": {}
                }
            },
            "response": {
                "input": {
                    "text": "Can you turn off the AC"
                },
                "context": {
                    "conversation_id": "f2c7e362-4cc8-4761-8b0f-9ccd70c63bca",
                    "system": {
                        "dialog_stack": ["root"],
                        "dialog_turn_counter": 1,
                        "dialog_request_counter": 1
                    },
                    "defaultCounter": 0
                },
                "entities": [],
                "intents": [{
                    "intent": "turn_off",
                    "confidence": 0.9332477126694649
                }],
                "output": {
                    "log_messages": [],
                    "text": [
                        "Hi. It looks like a nice drive today. What would you like me to do?"
                    ],
                    "nodes_visited": ["node_1_1467221909631"]
                }
            },
            "request_timestamp": "2016-07-16T09:22:38.960Z",
            "response_timestamp": "2016-07-16T09:22:39.011Z",
            "log_id": "e70d6c12-582d-47a8-a6a2-845120a1f232"
        }],
        "pagination": {
            "next_url":
            "/v1/workspaces/15fb0e8a-463d-4fec-86aa-a737d9c38a32/logs?cursor=dOfVSuh6fBpDuOxEL9m1S7JKDV7KLuBmRR+lQG1s1i/rVnBZ0ZBVCuy53ruHgPImC31gQv5prUsJ77e0Mj+6sGu/yfusHYF5&version=2016-07-11&filter=response.top_intent:turn_off&page_limit=1",
            "matched":
            215
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    logs = service.list_logs(
        workspace_id='boguswid')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert logs == response


#########################
# message
#########################


@responses.activate
def test_message():

    conversation = watson_developer_cloud.ConversationV1(
        username="username", password="password", version='2016-09-20')
    conversation.set_default_headers({'x-watson-learning-opt-out': "true"})

    workspace_id = 'f8fdbc65-e0bd-4e43-b9f8-2975a366d4ec'
    message_url = '%s/v1/workspaces/%s/message' % (base_url, workspace_id)
    url1_str = '%s/v1/workspaces/%s/message?version=2016-09-20'
    message_url1 = url1_str % (base_url, workspace_id)
    message_response = {
        "context": {
            "conversation_id": "1b7b67c0-90ed-45dc-8508-9488bc483d5b",
            "system": {
                "dialog_stack": ["root"],
                "dialog_turn_counter": 1,
                "dialog_request_counter": 1
            }
        },
        "intents": [],
        "entities": [],
        "input": {},
        "output": {
            "text": "okay",
            "log_messages": []
        }
    }

    responses.add(
        responses.POST,
        message_url,
        body=json.dumps(message_response),
        status=200,
        content_type='application/json')

    message = conversation.message(
        workspace_id=workspace_id,
        input={'text': 'Turn on the lights'},
        context=None)

    assert message is not None
    assert responses.calls[0].request.url == message_url1
    assert 'x-watson-learning-opt-out' in responses.calls[0].request.headers
    assert responses.calls[0].request.headers['x-watson-learning-opt-out'] == 'true'
    assert responses.calls[0].response.text == json.dumps(message_response)

    # test context
    responses.add(
        responses.POST,
        message_url,
        body=message_response,
        status=200,
        content_type='application/json')

    message_ctx = {
        'context': {
            'conversation_id': '1b7b67c0-90ed-45dc-8508-9488bc483d5b',
            'system': {
                'dialog_stack': ['root'],
                'dialog_turn_counter': 2,
                'dialog_request_counter': 1
            }
        }
    }
    message = conversation.message(
        workspace_id=workspace_id,
        input={'text': 'Turn on the lights'},
        context=json.dumps(message_ctx))

    assert message is not None
    assert responses.calls[1].request.url == message_url1
    assert responses.calls[1].response.text == json.dumps(message_response)

    assert len(responses.calls) == 2

@responses.activate
def test_message_with_models():

    conversation = watson_developer_cloud.ConversationV1(
        username="username", password="password", version='2016-09-20')
    conversation.set_default_headers({'x-watson-learning-opt-out': "true"})

    workspace_id = 'f8fdbc65-e0bd-4e43-b9f8-2975a366d4ec'
    message_url = '%s/v1/workspaces/%s/message' % (base_url, workspace_id)
    url1_str = '%s/v1/workspaces/%s/message?version=2016-09-20'
    message_url1 = url1_str % (base_url, workspace_id)
    message_response = {
        "context": {
            "conversation_id": "1b7b67c0-90ed-45dc-8508-9488bc483d5b",
            "system": {
                "dialog_stack": ["root"],
                "dialog_turn_counter": 1,
                "dialog_request_counter": 1
            }
        },
        "intents": [],
        "entities": [],
        "input": {},
        "output": {
            "text": "okay",
            "log_messages": []
        }
    }

    responses.add(
        responses.POST,
        message_url,
        body=json.dumps(message_response),
        status=200,
        content_type='application/json')

    message = conversation.message(
        workspace_id=workspace_id,
        input=InputData(text='Turn on the lights'),
        context=None)

    assert message is not None
    assert responses.calls[0].request.url == message_url1
    assert 'x-watson-learning-opt-out' in responses.calls[0].request.headers
    assert responses.calls[0].request.headers['x-watson-learning-opt-out'] == 'true'
    assert responses.calls[0].response.text == json.dumps(message_response)

    # test context
    responses.add(
        responses.POST,
        message_url,
        body=message_response,
        status=200,
        content_type='application/json')

    message_ctx = Context._from_dict(message_response['context'])
    message = conversation.message(
        workspace_id=workspace_id,
        input=InputData(text='Turn on the lights'),
        context=message_ctx)

    assert message is not None
    assert responses.calls[1].request.url == message_url1
    assert responses.calls[1].response.text == json.dumps(message_response)

    assert len(responses.calls) == 2


#########################
# synonyms
#########################


@responses.activate
def test_create_synonym():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
        'boguswid', 'aeiou', 'vowel')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "synonym": "aeiou",
        "created": "2000-01-23T04:56:07.000+00:00",
        "updated": "2000-01-23T04:56:07.000+00:00"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    synonym = service.create_synonym(
        workspace_id='boguswid', entity='aeiou', value='vowel', synonym='a')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert synonym == response
    # Verify that response can be converted to a Synonym
    Synonym._from_dict(synonym)

@responses.activate
def test_delete_synonym():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
        'boguswid', 'aeiou', 'vowel', 'a')
    url = '{0}{1}'.format(base_url, endpoint)
    response = ""
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    synonym = service.delete_synonym(
        workspace_id='boguswid', entity='aeiou', value='vowel', synonym='a')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert synonym is None


@responses.activate
def test_get_synonym():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
        'boguswid', 'grilling', 'bbq', 'barbecue')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "synonym": "barbecue",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    synonym = service.get_synonym(
        workspace_id='boguswid', entity='grilling', value='bbq', synonym='barbecue')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert synonym == response
    # Verify that response can be converted to a Synonym
    Synonym._from_dict(synonym)


@responses.activate
def test_list_synonyms():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
        'boguswid', 'grilling', 'bbq')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "synonyms": [{
            "synonym": "BBQ sauce",
            "created": "2015-12-06T23:53:59.153Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }, {
            "synonym": "barbecue",
            "created": "2015-12-06T23:53:59.153Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/entities/sauce/values/types/synonyms?version=2017-12-18&filter=name:b&include_count=true&page_limit=2",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/entities/sauce/values/types/synonyms?cursor=base64=&version=2017-12-18&filter=name:b&page_limit=2",
            "total":
            8,
            "matched":
            2
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    synonyms = service.list_synonyms(
        workspace_id='boguswid',
        entity='grilling',
        value='bbq')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert synonyms == response
    # Verify that response can be converted to a SynonymCollection
    SynonymCollection._from_dict(synonyms)


@responses.activate
def test_update_synonym():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
        'boguswid', 'grilling', 'bbq', 'barbecue')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "synonym": "barbecue",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    synonym = service.update_synonym(
        workspace_id='boguswid', entity='grilling', value='bbq', synonym='barbecue', new_synonym='barbecue')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert synonym == response
    # Verify that response can be converted to a Synonym
    Synonym._from_dict(synonym)


#########################
# values
#########################


@responses.activate
def test_create_value():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values'.format('boguswid', 'grilling')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "metadata": "{}",
        "created": "2000-01-23T04:56:07.000+00:00",
        "value": "aeiou",
        "type": "synonyms",
        "updated": "2000-01-23T04:56:07.000+00:00"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    value = service.create_value(
        workspace_id='boguswid',
        entity='grilling',
        value='aeiou')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert value == response
    # Verify that response can be converted to a Value
    Value._from_dict(value)


@responses.activate
def test_delete_value():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
        'boguswid', 'grilling', 'bbq')
    url = '{0}{1}'.format(base_url, endpoint)
    response = ""
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    value = service.delete_value(
        workspace_id='boguswid', entity='grilling', value='bbq')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert value is None


@responses.activate
def test_get_value():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
        'boguswid', 'grilling', 'bbq')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "value": "BBQ sauce",
        "metadata": {
            "code": 1422
        },
        "type": "synonyms",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-07T18:53:59.153Z"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    value = service.get_value(
        workspace_id='boguswid', entity='grilling', value='bbq', export=True)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert value == response
    # Verify that response can be converted to a Value
    Value._from_dict(value)


@responses.activate
def test_list_values():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values'.format('boguswid', 'grilling')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "values": [{
            "value": "BBQ sauce",
            "metadata": {
                "code": 1422
            },
            "type": "synonyms",
            "created": "2015-12-06T23:53:59.153Z",
            "updated": "2015-12-07T18:53:59.153Z"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces/pizza_app-e0f3/entities/sauce/values?version=2017-12-18&filter=name:pizza&include_count=true&page_limit=1",
            "next_url":
            "/v1/workspaces/pizza_app-e0f3/sauce/values?cursor=base64=&version=2017-12-18&filter=name:pizza&page_limit=1",
            "total":
            1,
            "matched":
            1
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    values = service.list_values(
        workspace_id='boguswid',
        entity='grilling',
        export=True)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert values == response
    # Verify that response can be converted to a ValueCollection
    ValueCollection._from_dict(values)


@responses.activate
def test_update_value():
    endpoint = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
        'boguswid', 'grilling', 'bbq')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "value": "BBQ sauce",
        "metadata": {
            "code": 1422
        },
        "type": "synonyms",
        "created": "2015-12-06T23:53:59.153Z",
        "updated": "2015-12-06T23:53:59.153Z"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-04-21')
    value = service.update_value(
        workspace_id='boguswid',
        entity='grilling',
        value='bbq',
        new_value='BBQ sauce',
        new_metadata={"code": 1422},
        new_synonyms=None)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert value == response
    # Verify that response can be converted to a Value
    Value._from_dict(value)


#########################
# workspaces
#########################


@responses.activate
def test_create_workspace():
    endpoint = '/v1/workspaces'
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "name": "Pizza app",
        "created": "2015-12-06T23:53:59.153Z",
        "language": "en",
        "metadata": {},
        "updated": "2015-12-06T23:53:59.153Z",
        "description": "Pizza app",
        "workspace_id": "pizza_app-e0f3"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=201,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    workspace = service.create_workspace(
        name='Pizza app', description='Pizza app', language='en', metadata={})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspace == response
    # Verify that response can be converted to a Workspace
    Workspace._from_dict(workspace)

@responses.activate
def test_delete_workspace():
    endpoint = '/v1/workspaces/{0}'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {}
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    workspace = service.delete_workspace(workspace_id='boguswid')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspace is None


@responses.activate
def test_get_workspace():
    endpoint = '/v1/workspaces/{0}'.format('boguswid')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "name": "Pizza app",
        "created": "2015-12-06T23:53:59.153Z",
        "language": "en",
        "metadata": {},
        "updated": "2015-12-06T23:53:59.153Z",
        "description": "Pizza app",
        "status": "Available",
        "learning_opt_out": False,
        "workspace_id": "pizza_app-e0f3"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    workspace = service.get_workspace(workspace_id='boguswid', export=False)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspace == response
    # Verify that response can be converted to a Workspace
    Workspace._from_dict(workspace)


@responses.activate
def test_list_workspaces():
    endpoint = '/v1/workspaces'
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "workspaces": [{
            "name": "Pizza app",
            "created": "2015-12-06T23:53:59.153Z",
            "language": "en",
            "metadata": {},
            "updated": "2015-12-06T23:53:59.153Z",
            "description": "Pizza app",
            "workspace_id": "pizza_app-e0f3"
        }],
        "pagination": {
            "refresh_url":
            "/v1/workspaces?version=2016-01-24&page_limit=1",
            "next_url":
            "/v1/workspaces?cursor=base64=&version=2016-01-24&page_limit=1"
        }
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    workspaces = service.list_workspaces()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspaces == response
    # Verify that response can be converted to a WorkspaceCollection
    WorkspaceCollection._from_dict(workspaces)


@responses.activate
def test_update_workspace():
    endpoint = '/v1/workspaces/{0}'.format('pizza_app-e0f3')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        "name": "Pizza app",
        "created": "2015-12-06T23:53:59.153Z",
        "language": "en",
        "metadata": {},
        "updated": "2015-12-06T23:53:59.153Z",
        "description": "Pizza app",
        "workspace_id": "pizza_app-e0f3"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = watson_developer_cloud.ConversationV1(
        username='username', password='password', version='2017-02-03')
    workspace = service.update_workspace(
        workspace_id='pizza_app-e0f3',
        name='Pizza app',
        description='Pizza app',
        language='en',
        metadata={})
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspace == response
    # Verify that response can be converted to a Workspace
    Workspace._from_dict(workspace)
