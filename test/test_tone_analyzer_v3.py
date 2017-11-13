import responses
import watson_developer_cloud
from watson_developer_cloud import WatsonException
from watson_developer_cloud import WatsonApiException
import os
import json


@responses.activate
# Simple test, just calling tone() with some text
def test_tone():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    tone_args = '?version=2016-05-19'
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone-v3-expect1.json')) as response_json:
        tone_response = response_json.read()

    responses.add(responses.POST, tone_url,
                  body=tone_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality.txt')) as tone_text:
        tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
                                                              username="username", password="password")
        tone_analyzer.tone(tone_text.read())

    assert responses.calls[0].request.url == tone_url + tone_args
    assert responses.calls[0].response.text == tone_response

    assert len(responses.calls) == 1


@responses.activate
# Invoking tone() with some modifiers given in 'params': sentences skipped
def test_tone_with_args():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    tone_args = {'version': '2016-05-19', 'sentences': 'false'}
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone-v3-expect1.json')) as response_json:
        tone_response = response_json.read()

    responses.add(responses.POST, tone_url,
                  body=tone_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality.txt')) as tone_text:
        tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
                                                              username="username", password="password")
        tone_analyzer.tone(tone_text.read(), sentences=False)

    assert responses.calls[0].request.url.split('?')[0] == tone_url
    # Compare args. Order is not deterministic!
    actualArgs = {}
    for arg in responses.calls[0].request.url.split('?')[1].split('&'):
        actualArgs[arg.split('=')[0]] = arg.split('=')[1]
    assert actualArgs == tone_args
    assert responses.calls[0].response.text == tone_response
    assert len(responses.calls) == 1


@responses.activate
# Invoking tone() with some modifiers specified as positional parameters: sentences is false
def test_tone_with_positional_args():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    tone_args = {'version': '2016-05-19', 'sentences': 'false'}
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone-v3-expect1.json')) as response_json:
        tone_response = response_json.read()

    responses.add(responses.POST, tone_url,
                  body=tone_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality.txt')) as tone_text:
        tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
                                                              username="username", password="password")
        tone_analyzer.tone(tone_text.read(), 'application/json', False)

    assert responses.calls[0].request.url.split('?')[0] == tone_url
    # Compare args. Order is not deterministic!
    actualArgs = {}
    for arg in responses.calls[0].request.url.split('?')[1].split('&'):
        actualArgs[arg.split('=')[0]] = arg.split('=')[1]
    assert actualArgs == tone_args
    assert responses.calls[0].response.text == tone_response
    assert len(responses.calls) == 1


@responses.activate
# Invoking tone_chat()
def test_tone_chat():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone_chat'
    tone_args = '?version=2016-05-19'
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone-v3-expect2.json')) as response_json:
        tone_response = response_json.read()

    responses.add(responses.POST, tone_url,
                  body=tone_response, status=200,
                  content_type='application/json')

    tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
                                                          username="username", password="password")
    utterances = [{'text': 'I am very happy', 'user': 'glenn'}]
    tone_analyzer.tone_chat(utterances)

    assert responses.calls[0].request.url == tone_url + tone_args
    assert responses.calls[0].response.text == tone_response
    assert len(responses.calls) == 1


#########################
# error response
#########################


@responses.activate
def test_error():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    error_code = 400
    error_message = "Invalid JSON input at line 2, column 12"
    tone_response = {
        "code": error_code,
        "sub_code": "C00012",
        "error": error_message
    }
    responses.add(responses.POST,
                  tone_url,
                  body=json.dumps(tone_response),
                  status=error_code,
                  content_type='application/json')

    tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
                                                          username="username", password="password")
    text = "Team, I know that times are tough!"
    try:
        tone_analyzer.tone(text)
    except WatsonException as ex:
        assert len(responses.calls) == 1
        assert isinstance(ex, WatsonApiException)
        assert ex.code == error_code
        assert ex.message == error_message
        assert len(ex.info) == 1
        assert ex.info['sub_code'] == 'C00012'
