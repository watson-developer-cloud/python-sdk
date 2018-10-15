# coding: utf-8
import responses
import watson_developer_cloud


@responses.activate
def test_request_token():
    url = 'https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/speech-to-text/api'
    responses.add(responses.GET,
                  url=url,
                  body=b'mocked token',
                  status=200)
    authorization = watson_developer_cloud.AuthorizationV1(username='xxx',
                                                           password='yyy')
    authorization.get_token(url=watson_developer_cloud.SpeechToTextV1.default_url)
    assert responses.calls[0].request.url == url
    assert responses.calls[0].response.content.decode('utf-8') == 'mocked token'
