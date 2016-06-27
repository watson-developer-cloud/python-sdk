import responses
import watson_developer_cloud
import os


@responses.activate
## Simple test, just calling tone() with some text
def test_success():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    tone_args = '?version=2016-05-19'
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone_response.json')) as response_json:
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
## Invoking tone() with some modifiers given in 'params': specific tones requested, and sentences skipped
def test_with_args():
    tone_url = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone'
    tone_args = { 'version': '2016-05-19', 'tones': 'social', 'sentences': 'false' }
    tone_response = None
    with open(os.path.join(os.path.dirname(__file__), '../resources/tone_response.json')) as response_json:
        tone_response = response_json.read()

    responses.add(responses.POST, tone_url,
                  body=tone_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality.txt')) as tone_text:
        tone_analyzer = watson_developer_cloud.ToneAnalyzerV3("2016-05-19",
            username="username", password="password")
        tone_analyzer.tone(tone_text.read(), tones="social", sentences=False)


    assert responses.calls[0].request.url.split('?')[0] == tone_url 
    # Compare args. Order is not deterministic!
    actualArgs = {}
    for arg in responses.calls[0].request.url.split('?')[1].split('&'):
        actualArgs[arg.split('=')[0]] = arg.split('=')[1]
    assert actualArgs == tone_args
    assert responses.calls[0].response.text == tone_response
    assert len(responses.calls) == 1
