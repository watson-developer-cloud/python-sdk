import responses,os
import watson_developer_cloud
try:
    from urllib.parse import urlparse, urljoin
except ImportError:
    from urlparse import urlparse, urljoin

base_discovery_url = 'https://gateway.watsonplatform.net/discovery/api/v1/'

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
    discovery.list_collections('envid')

    called_url = urlparse(responses.calls[0].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path
    assert len(responses.calls) == 1


@responses.activate
def test_collection():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/collections/collid')

    discovery_fields = urljoin(base_discovery_url, 'environments/envid/collections/collid/fields')
    config_url = urljoin(base_discovery_url, 'environments/envid/configurations')

    responses.add(responses.GET, config_url,
                  body="{\"configurations\": [{ \"name\": \"Default Configuration\", \"configuration_id\": \"confid\"}]}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, discovery_fields,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')

    responses.add(responses.GET, discovery_url,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')

    responses.add(responses.DELETE, discovery_url,
                  body="{\"body\": \"hello\"}", status=200,
                  content_type='application/json')

    responses.add(responses.POST,
                 urljoin(base_discovery_url, 'environments/envid/collections'),
                 body="{\"body\": \"create\"}",
                 status=200,
                 content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.create_collection(environment_id='envid',
                                name="name",
                                description="",
                                configuration_id='confid')

    discovery.create_collection(environment_id='envid',
                                name="name",
                                description="")

    discovery.get_collection('envid', 'collid')

    called_url = urlparse(responses.calls[3].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path

    discovery.delete_collection(environment_id='envid',collection_id='collid')
    discovery.list_collection_fields(environment_id='envid', collection_id='collid')
    assert len(responses.calls) == 6

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

@responses.activate
def test_configs():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/configurations')
    discovery_config_id = urljoin(base_discovery_url, 'environments/envid/configurations/confid')

    responses.add(responses.GET, discovery_url,
                  body="{\"configurations\": [{ \"name\": \"Default Configuration\", \"configuration_id\": \"confid\"}]}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, discovery_config_id,
                  body="{\"configurations\": [{ \"name\": \"Default Configuration\", \"configuration_id\": \"confid\"}]}",
                  status=200,
                  content_type='application/json')


    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.list_configurations(environment_id='envid')
    conf_id = discovery.get_default_configuration_id(environment_id='envid')
    assert conf_id == 'confid'

    discovery.get_configuration(environment_id='envid', configuration_id='confid')

    assert len(responses.calls) == 3


@responses.activate
def test_empty_configs():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/configurations')
    responses.add(responses.GET, discovery_url,
                  body="{}",
                  status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')

    conf_id = discovery.get_default_configuration_id(environment_id='envid')
    assert conf_id == None
    assert len(responses.calls) == 1

@responses.activate
def test_no_configs():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/configurations')
    responses.add(responses.GET, discovery_url,
                  body="{\"configurations\": []}",
                  status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')

    conf_id = discovery.get_default_configuration_id(environment_id='envid')
    assert conf_id == None
    assert len(responses.calls) == 1


@responses.activate
def test_document():
    discovery_url = urljoin(base_discovery_url, 'environments/envid/preview')
    config_url = urljoin(base_discovery_url, 'environments/envid/configurations')
    responses.add(responses.POST, discovery_url,
                  body="{\"configurations\": []}",
                  status=200,
                  content_type='application/json')
    responses.add(responses.GET, config_url,
                  body="{\"configurations\": [{ \"name\": \"Default Configuration\", \"configuration_id\": \"confid\"}]}",
                  status=200,
                  content_type='application/json')


    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')

    with open(os.path.join(os.getcwd(), 'resources', 'simple.html')) as fileinfo:
        conf_id = discovery.test_document(environment_id='envid', configuration_id='bogus', fileinfo=fileinfo)
        assert conf_id != None
        conf_id = discovery.test_document(environment_id='envid', fileinfo=fileinfo)
        assert conf_id != None

    assert len(responses.calls) == 3

    add_doc_url = urljoin(base_discovery_url, 'environments/envid/collections/collid/documents')
    del_doc_url = urljoin(base_discovery_url, 'environments/envid/collections/collid/documents/docid')
    responses.add(responses.POST, add_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.DELETE, del_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    with open(os.path.join(os.getcwd(), 'resources', 'simple.html')) as fileinfo:
        conf_id = discovery.add_document(environment_id='envid',
                                         collection_id='collid',
                                         fileinfo=fileinfo)
        assert conf_id != None

    assert len(responses.calls) == 4

    discovery.delete_document(environment_id='envid',
                              collection_id='collid',
                              document_id='docid')

    assert len(responses.calls) == 5