# coding: utf-8
import responses
import ibm_watson


@responses.activate
def test_request_token():
    url = 'https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/speech-to-text/api'
    responses.add(responses.GET,
                  url=url,
                  body=b'mocked token',
                  status=200)
    authorization = ibm_watson.AuthorizationV1(username='xxx', password='yyy')
    authorization.get_token(url=ibm_watson.SpeechToTextV1.default_url)
    assert responses.calls[0].request.url == url
    assert responses.calls[0].response.content.decode('utf-8') == 'mocked token'
