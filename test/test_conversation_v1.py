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
import responses
import watson_developer_cloud

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
    assert counterexample == response


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
        workspace_id='boguswid', text='What are you wearing%3F')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample == response


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
    counterexamples = service.list_counterexamples(
        workspace_id='boguswid')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexamples == response


@responses.activate
def test_update_counterexample():
    endpoint = '/v1/workspaces/{0}/counterexamples/{1}'.format('boguswid', 'What%20are%20you%20wearing%3F')
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
        workspace_id='boguswid', text='What are you wearing%3F', new_text='What are you wearing%3F')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert counterexample == response

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
    assert example == response


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
        workspace_id='boguswid', intent='pizza_order', text='Gimme a pizza with pepperoni', new_text='Gimme a pizza with pepperoni')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert example == response

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
    assert intent == response


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


@responses.activate
def test_update_intent():
    endpoint = '/v1/workspaces/{0}/intents/{1}'.format('boguswid', 'pizza_order')
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
        workspace_id='boguswid', intent='pizza_order', new_intent='pizza_order', new_description='User wants to start a new pizza order')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert intent == response

#########################
# message
#########################


@responses.activate
def test_message():

    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')

    workspace_id = 'f8fdbc65-e0bd-4e43-b9f8-2975a366d4ec'
    message_url = '%s/workspaces/%s/message' % (base_url, workspace_id)
    url1_str = '%s/workspaces/%s/message?version=2016-09-20'
    message_url1 = url1_str % (base_url, workspace_id)
    message_response = {"context": {
                        "conversation_id":
                            "1b7b67c0-90ed-45dc-8508-9488bc483d5b",
                        "system": {"dialog_stack":
                                   ["root"],
                                   "dialog_turn_counter": 1,
                                   "dialog_request_counter": 1}},
                        "intents": [],
                        "entities": [],
                        "input": {}}

    responses.add(responses.POST, message_url,
                  body=json.dumps(message_response),
                  status=200,
                  content_type='application/json')

    message = conversation.message(workspace_id=workspace_id,
                                   message_input={'text':
                                                  'Turn on the lights'},
                                   context=None)

    assert message is not None
    assert responses.calls[0].request.url == message_url1
    assert responses.calls[0].response.text == json.dumps(message_response)


# test context
    responses.add(responses.POST, message_url,
                  body=message_response, status=200,
                  content_type='application/json')

    message_ctx = {'context':
                   {'conversation_id': '1b7b67c0-90ed-45dc-8508-9488bc483d5b',
                    'system': {
                        'dialog_stack': ['root'],
                        'dialog_turn_counter': 2,
                        'dialog_request_counter': 1}}}
    message = conversation.message(workspace_id=workspace_id,
                                   message_input={'text':
                                                  'Turn on the lights'},
                                   context=json.dumps(message_ctx))

    assert message is not None
    assert responses.calls[1].request.url == message_url1
    assert responses.calls[1].response.text == json.dumps(message_response)

    assert len(responses.calls) == 2

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
    assert workspace == response


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
    workspace = service.get_workspace(
        workspace_id='boguswid', export=False)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert workspace == response


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
