# coding: utf-8
import json
import responses
import ibm_watson

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/assistant/api'
base_url = '{0}{1}'.format(platform_url, service_path)

@responses.activate
def test_create_session():
    endpoint = '/v2/assistants/{0}/sessions'.format('bogus_id')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {'session_id': 'session_id'}
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = ibm_watson.AssistantV2(
        username='username', password='password', version='2017-02-03')
    session = service.create_session('bogus_id').get_result()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert session == response


@responses.activate
def test_delete_session():
    endpoint = '/v2/assistants/{0}/sessions/{1}'.format('bogus_id',
                                                        'session_id')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {}
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = ibm_watson.AssistantV2(
        username='username', password='password', version='2017-02-03')
    delete_session = service.delete_session('bogus_id',
                                            'session_id').get_result()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert delete_session == response


@responses.activate
def test_message():
    endpoint = '/v2/assistants/{0}/sessions/{1}/message'.format(
        'bogus_id', 'session_id')
    url = '{0}{1}'.format(base_url, endpoint)
    response = {
        'output': {
            'generic': [{
                'text':
                'I did not understand that. I can help you get pizza, tell a joke or find a movie.',
                'response_type':
                'text'
            }],
            'entities': [],
            'intents': [{
                'confidence': 0.8521236419677736,
                'intent': 'Weather'
            }]
        }
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(response),
        status=200,
        content_type='application/json')
    service = ibm_watson.AssistantV2(
        username='username', password='password', version='2017-02-03')
    message = service.message(
        'bogus_id', 'session_id', input={
            'text': 'What\'s the weather like?'
        }).get_result()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert message == response
