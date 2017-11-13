# coding=utf-8
import json

from watson_developer_cloud import WatsonService

import responses

##############################################################################
# Service
##############################################################################

class AnyServiceV1(WatsonService):
    default_url = 'https://gateway.watsonplatform.net/test/api'

    def __init__(self, version, url=default_url, username=None, password=None):
        WatsonService.__init__(
            self,
            vcap_services_name='test',
            url=url,
            username=username,
            password=password,
            use_vcap_services=True)
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
