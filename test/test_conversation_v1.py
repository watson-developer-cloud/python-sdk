import json
import responses
import watson_developer_cloud

platform_url = "https://gateway.watsonplatform.net"
conversation_path = "/conversation/api/v1"
base_url = "{0}{1}".format(platform_url, conversation_path)


@responses.activate
def test_list_worksapces():
    workspace_url = "{0}{1}".format(base_url, "/workspaces")
    message_response = {"workspaces": [],
                        "pagination": {
                            "refresh_url":
                                "/v1/workspaces?version=2016-09-20"}}
    responses.add(responses.GET, workspace_url,
                  body=json.dumps(message_response), status=200,
                  content_type='application/json')
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')
    workspaces = conversation.list_workspaces()
    assert 'workspaces' in workspaces
    assert len(workspaces['workspaces']) == 0


@responses.activate
def test_get_workspace():
    workspace_url = "{0}{1}/boguswid".format(base_url, "/workspaces")
    message_response = {
                        "name": "development",
                        "created": "2017-02-09T18:41:19.890Z",
                        "updated": "2017-02-09T18:41:19.890Z",
                        "language": "en",
                        "metadata": None,
                        "description": "this is a workspace",
                        "workspace_id": "boguswid",
                        "status": 'Training',
                        }
    responses.add(responses.GET, workspace_url,
                  body=json.dumps(message_response), status=200,
                  content_type='application/json')
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')
    workspace = conversation.get_workspace(workspace_id='boguswid')
    assert workspace['name'] == 'development'
    assert workspace['workspace_id'] == 'boguswid'
    assert workspace['status'] == 'Training'

    workspace = conversation.get_workspace(workspace_id='boguswid',
                                           export=True)
    assert workspace['status'] == 'Training'


@responses.activate
def test_delete_workspace():
    workspace_url = "{0}{1}/boguswid".format(base_url, "/workspaces")
    message_response = {}
    responses.add(responses.DELETE, workspace_url,
                  body=json.dumps(message_response), status=200,
                  content_type='application/json')
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')
    workspace = conversation.delete_workspace(workspace_id='boguswid')
    assert len(responses.calls) == 1
    assert workspace == {}


@responses.activate
def test_create_workspace():
    workspace_data = {
                      "name": "development",
                      "intents": [
                                  {
                                   "intent": "orderpizza",
                                   "examples": [
                                                {
                                                 "text": "can I order a pizza?"
                                                }, {
                                                 "text": "want order a pizza"
                                                }, {
                                                 "text": "pizza order"
                                                }, {
                                                 "text": "pizza to go"
                                                }],
                                   "description": None
                                  }],
                      "entities": [{'entity': 'just for testing'}],
                      "language": "en",
                      "metadata": {'thing': 'something'},
                      "description": "this is a development workspace",
                      "dialog_nodes": [{'conditions': '#orderpizza',
                                        'context': None,
                                        'description': None,
                                        'dialog_node': 'YesYouCan',
                                        'go_to': None,
                                        'metadata': None,
                                        'output':  {'text': {'selection_policy': 'random',
                                                             'values': ['Yes You can!', 'Of course!']}},
                                                             'parent': None,
                                                             'previous_sibling': None}],
                      "counterexamples": [{'counter': 'counterexamples for test'}]
                      }

    workspace_url = "{0}{1}".format(base_url, "/workspaces")
    message_response = workspace_data
    message_response["workspace_id"] = 'bogusid'
    responses.add(responses.POST, workspace_url,
                  body=json.dumps(message_response), status=200,
                  content_type='application/json')
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')
    workspace = conversation.create_workspace(name=workspace_data['name'],
                                              description=workspace_data['description'],
                                              language=workspace_data['language'],
                                              intents=workspace_data['intents'],
                                              metadata=workspace_data['metadata'],
                                              counterexamples=workspace_data['counterexamples'],
                                              dialog_nodes=workspace_data['dialog_nodes'],
                                              entities=workspace_data['entities'])
    assert workspace == message_response
    assert len(responses.calls) == 1


@responses.activate
def test_update_workspace():
    workspace_data = {
                      "name": "development",
                      "intents": [
                                  {
                                   "intent": "orderpizza",
                                   "examples": [
                                                {
                                                 "text": "can I order a pizza?"
                                                }, {
                                                 "text": "want order a pizza"
                                                }, {
                                                 "text": "pizza order"
                                                }, {
                                                 "text": "pizza to go"
                                                }],
                                   "description": None
                                  }],
                      "entities": [],
                      "language": "en",
                      "metadata": {},
                      "description": "this is a development workspace",
                      "dialog_nodes": [],
                      "counterexamples": [],
                      "workspace_id": 'boguswid'
                      }

    workspace_url = "{0}{1}".format(base_url, "/workspaces/boguswid")
    message_response = workspace_data
    responses.add(responses.POST, workspace_url,
                  body=json.dumps(message_response), status=200,
                  content_type='application/json')
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')
    workspace = conversation.update_workspace('boguswid',
                                              name=workspace_data['name'],
                                              description=workspace_data['description'],
                                              language=workspace_data['language'],
                                              intents=workspace_data['intents'],
                                              metadata=workspace_data['metadata'],
                                              counterexamples=workspace_data['counterexamples'],
                                              dialog_nodes=workspace_data['dialog_nodes'],
                                              entities=workspace_data['entities'])
    assert len(responses.calls) == 1
    assert workspace == message_response


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
