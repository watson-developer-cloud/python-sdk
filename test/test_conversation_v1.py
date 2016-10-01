import responses
import watson_developer_cloud

@responses.activate
def test_message():

# Ranker endpoints
    conversation = watson_developer_cloud.ConversationV1(username="username",
                                                         password="password",
                                                         version='2016-09-20')

    workspace_id = 'f8fdbc65-e0bd-4e43-b9f8-2975a366d4ec'
    message_url = 'https://gateway.watsonplatform.net/conversation/api/v1/workspaces/%s/message' % workspace_id
    message_url1 = 'https://gateway.watsonplatform.net/conversation/api/v1/workspaces/%s/message?version=2016-09-20' % workspace_id
    message_response = '{"context":{"conversation_id":"1b7b67c0-90ed-45dc-8508-9488bc483d5b","system":{"dialog_stack":["root"],"dialog_turn_counter":1,"dialog_request_counter":1}},"intents":[],"entities":[],"input":{}}'

    responses.add(responses.POST, message_url,
              body=message_response, status=200,
              content_type='application/json')

    message = conversation.message(workspace_id=workspace_id, message_input={'text': 'Turn on the lights'}, context=None)

    assert message is not None
    assert responses.calls[0].request.url == message_url1
    assert responses.calls[0].response.text == message_response


    # test context
    responses.add(responses.POST, message_url,
              body=message_response, status=200,
              content_type='application/json')

    message = conversation.message(workspace_id=workspace_id, message_input={'text': 'Turn on the lights'}, context={'context': {'conversation_id':'1b7b67c0-90ed-45dc-8508-9488bc483d5b', 'system': {'dialog_stack':['root'], 'dialog_turn_counter':2, 'dialog_request_counter':1}}})

    assert message is not None
    assert responses.calls[1].request.url == message_url1
    assert responses.calls[1].response.text == message_response

    assert len(responses.calls) == 2
