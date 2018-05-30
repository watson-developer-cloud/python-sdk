# coding=utf-8
import json
import pytest
from watson_developer_cloud import WatsonService
import time

import responses

##############################################################################
# Service
##############################################################################

class AnyServiceV1(WatsonService):
    default_url = 'https://gateway.watsonplatform.net/test/api'

    def __init__(self, version, url=default_url, username=None, password=None,
                 api_key=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
        WatsonService.__init__(
            self,
            vcap_services_name='test',
            url=url,
            api_key=api_key,
            username=username,
            password=password,
            use_vcap_services=True,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url)
        self.version = version

    def op_with_path_params(self, path0, path1):
        if path0 is None:
            raise ValueError('path0 must be provided')
        if path1 is None:
            raise ValueError('path1 must be provided')
        params = {'version': self.version}
        url = '/v1/foo/{0}/bar/{1}/baz'.format(
            *self._encode_path_vars(path0, path1))
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
        return response

    def with_http_config(self, http_config):
        self.set_http_config(http_config)
        response = self.request(method='GET', url='', accept_json=True)
        return response

    def any_service_call(self):
        response = self.request(method='GET', url='', accept_json=True)
        return response

@responses.activate
def test_url_encoding():
    service = AnyServiceV1('2017-07-07', username='username', password='password')

    # All characters in path0 _must_ be encoded in path segments
    path0 = ' \"<>^`{}|/\\?#%[]'
    path0_encoded = '%20%22%3C%3E%5E%60%7B%7D%7C%2F%5C%3F%23%25%5B%5D'
    # All non-ASCII chars _must_ be encoded in path segments
    path1 = u'比萨浇头'.encode('utf8')  # "pizza toppings"
    path1_encoded = '%E6%AF%94%E8%90%A8%E6%B5%87%E5%A4%B4'

    path_encoded = '/v1/foo/' + path0_encoded + '/bar/' + path1_encoded + '/baz'
    test_url = service.default_url + path_encoded

    responses.add(responses.GET,
                  test_url,
                  status=200,
                  body=json.dumps({"foobar": "baz"}),
                  content_type='application/json')

    response = service.op_with_path_params(path0, path1)

    assert response is not None
    assert len(responses.calls) == 1
    assert path_encoded in responses.calls[0].request.url
    assert 'version=2017-07-07' in responses.calls[0].request.url

@responses.activate
def test_http_config():
    service = AnyServiceV1('2017-07-07', username='username', password='password')
    responses.add(responses.GET,
                  service.default_url,
                  status=200,
                  body=json.dumps({"foobar": "baz"}),
                  content_type='application/json')

    response = service.with_http_config({'timeout': 100})
    assert response is not None
    assert len(responses.calls) == 1

@responses.activate
def test_fail_http_config():
    service = AnyServiceV1('2017-07-07', username='username', password='password')
    with pytest.raises(TypeError):
        service.with_http_config(None)

@responses.activate
def test_iam():
    iam_url = "https://iam.bluemix.net/identity/token"
    service = AnyServiceV1('2017-07-07', iam_api_key="iam_api_key")
    assert service.token_manager is not None

    iam_url = "https://iam.bluemix.net/identity/token"
    service = AnyServiceV1('2017-07-07', username='xxx', password='yyy')
    assert service.token_manager is None
    service.set_iam_api_key('yyy')
    assert service.token_manager is not None

    service.token_manager.token_info = {
        "access_token": "dummy",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": int(time.time()) - 4000,
        "refresh_token": "jy4gl91BQ"
    }
    response = """{
        "access_token": "hellohello",
        "token_type": "Bearer",
        "expires_in": 3600,
        "expiration": 1524167011,
        "refresh_token": "jy4gl91BQ"
    }"""
    responses.add(responses.POST, url=iam_url, body=response, status=200)
    responses.add(responses.GET,
                  service.default_url,
                  body=json.dumps({"foobar": "baz"}),
                  content_type='application/json')
    service.any_service_call()
    assert "grant_type=refresh_token" in responses.calls[0].request.body
