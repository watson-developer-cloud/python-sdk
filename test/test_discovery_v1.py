import responses
import watson_developer_cloud
try:
    from urllib.parse import urlparse, urljoin
except ImportError:
    from urlparse import urlparse, urljoin

base_discovery_url = 'https://gateway.watsonplatform.net/discovery-experimental/api/v1/'

@responses.activate
def test_environments():
    discovery_url = urljoin(base_discovery_url, 'environments')
    discovery_response_body = """{
  "environments": [
    {
      "environment_id": "string",
      "name": "envname",
      "description": "",
      "created": "2016-11-20T01:03:17.645Z",
      "updated": "2016-11-20T01:03:17.645Z",
      "status": "status",
      "index_capacity": {
        "disk_usage": {
          "used_bytes": 0,
          "total_bytes": 0,
          "used": "string",
          "total": "string",
          "percent_used": 0
        },
        "memory_usage": {
          "used_bytes": 0,
          "total_bytes": 0,
          "used": "string",
          "total": "string",
          "percent_used": 0
        }
      }
    }
  ]
}"""

    responses.add(responses.GET, discovery_url,
                  body=discovery_response_body, status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.get_environments()

    assert responses.calls[0].request.url == "{0}?version=2016-11-07".format(discovery_url)
    assert responses.calls[0].response.text == discovery_response_body
    assert len(responses.calls) == 1

@responses.activate
def test_get_environment():
    discovery_url = urljoin(base_discovery_url, 'environments/envid')
    responses.add(responses.GET, discovery_url,
                  body="{\"resulting_key\": true}", status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.get_environment(environment_id='envid')
    assert responses.calls[0].request.url == "{0}?version=2016-11-07".format(discovery_url)
    assert len(responses.calls) == 1

@responses.activate
def test_create_environment():

    discovery_url = urljoin(base_discovery_url, 'environments')
    responses.add(responses.POST, discovery_url,
                  body="{\"resulting_key\": true}", status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')

    discovery.create_environment()
    discovery.create_environment(name="my name", description="my description")
    thrown = False
    try:
        badname = "-".join([str(x) for x in range(0, 255)])
        discovery.create_environment(name=badname)
    except ValueError as ve:
        thrown = True
        assert str(ve) == "name must be a string having length between 0 and 255 characters"

    assert thrown

    thrown = False
    try:
        baddescription = "-".join([str(x) for x in range(0, 255)])
        discovery.create_environment(description=baddescription)
    except ValueError as ve:
        thrown = True
        assert str(ve) == "description must be a string having length between 0 and 255 characters"

    assert thrown

    try:
        discovery.create_environment(size=14)
    except ValueError as ve:
        thrown = True
        assert str(ve) == "Size can be 1, 2, or 3"

    assert thrown
    assert len(responses.calls) == 2

@responses.activate
def test_update_environment():
    discovery_url = urljoin(base_discovery_url, 'environments/envid')
    responses.add(responses.PUT, discovery_url,
                  body="{\"resulting_key\": true}", status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.update_environment('envid', name="hello", description="new")
    assert len(responses.calls) == 1

@responses.activate
def test_delete_environment():
    discovery_url = urljoin(base_discovery_url, 'environments/envid')
    responses.add(responses.DELETE, discovery_url,
                  body="{\"resulting_key\": true}", status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.delete_environment('envid')
    assert len(responses.calls) == 1

@responses.activate
def test_collections():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/collections')

    responses.add(responses.GET, discovery_url,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')


    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.get_collections('envid')

    called_url = urlparse(responses.calls[0].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path
    assert len(responses.calls) == 1


@responses.activate
def test_get_collection():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/collections/collid')

    responses.add(responses.GET, discovery_url,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.get_collection('envid', 'collid')

    called_url = urlparse(responses.calls[0].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path
    assert len(responses.calls) == 1

@responses.activate
def test_query():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/collections/collid/query')

    responses.add(responses.GET, discovery_url,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')
    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.query('envid', 'collid', {'count': 10})

    called_url = urlparse(responses.calls[0].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path
    assert len(responses.calls) == 1
