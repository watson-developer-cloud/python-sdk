import responses
import os
import json
import watson_developer_cloud
import pytest
try:
    from urllib.parse import urlparse, urljoin
except ImportError:
    from urlparse import urlparse, urljoin

base_discovery_url = 'https://gateway.watsonplatform.net/discovery/api/v1/'

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/discovery/api'
base_url = '{0}{1}'.format(platform_url, service_path)

version = '2016-12-01'
environment_id = 'envid'
collection_id = 'collid'

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

    url_str = "{0}?version=2016-11-07".format(discovery_url)
    assert responses.calls[0].request.url == url_str

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
    url_str = "{0}?version=2016-11-07".format(discovery_url)
    assert responses.calls[0].request.url == url_str
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
        errorstr_first = "name must be a string having length between"
        errorstr = "{0} 0 and 255 characters".format(errorstr_first)
        assert str(ve) == errorstr

    assert thrown

    thrown = False
    try:
        baddescription = "-".join([str(x) for x in range(0, 255)])
        discovery.create_environment(description=baddescription)
    except ValueError as ve:
        thrown = True
        errorstr_first = "description must be a string having length between"
        errorstr = "{0} 0 and 255 characters".format(errorstr_first)
        assert str(ve) == errorstr

    assert thrown

    with pytest.raises(ValueError):
        discovery.create_environment(size=14)

    discovery.create_environment(size=0)

    assert len(responses.calls) == 3


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
    discovery_url = urljoin(base_discovery_url,
                            'environments/envid/collections')

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
    discovery_url = urljoin(base_discovery_url,
                            'environments/envid/collections/collid')

    discovery_fields = urljoin(base_discovery_url,
                               'environments/envid/collections/collid/fields')
    config_url = urljoin(base_discovery_url,
                         'environments/envid/configurations')

    responses.add(responses.GET, config_url,
                  body="{\"body\": \"hello\"}",
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
                  urljoin(base_discovery_url,
                          'environments/envid/collections'),
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

    called_url = urlparse(responses.calls[2].request.url)
    test_url = urlparse(discovery_url)

    assert called_url.netloc == test_url.netloc
    assert called_url.path == test_url.path

    discovery.delete_collection(environment_id='envid',
                                collection_id='collid')
    discovery.list_collection_fields(environment_id='envid',
                                     collection_id='collid')
    assert len(responses.calls) == 5


@responses.activate
def test_query():
    discovery_url = urljoin(base_discovery_url,
                            'environments/envid/collections/collid/query')

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
    discovery_url = urljoin(base_discovery_url,
                            'environments/envid/configurations')
    discovery_config_id = urljoin(base_discovery_url,
                                  'environments/envid/configurations/confid')

    results = {"configurations":
               [{"name": "Default Configuration",
                 "configuration_id": "confid"}]}
    json_result = json.dumps(results)
    responses.add(responses.GET, discovery_url,
                  body=json_result,
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, discovery_config_id,
                  body=json_result,
                  status=200,
                  content_type='application/json')
    responses.add(responses.POST, discovery_url,
                  body=json_result,
                  status=200,
                  content_type='application/json')
    responses.add(responses.DELETE, discovery_config_id,
                  body=json.dumps({'deleted': 'bogus -- ok'}),
                  status=200,
                  content_type='application/json')
    responses.add(responses.PUT, discovery_config_id,
                  body=json.dumps({'updated': 'bogus -- ok'}),
                  status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    discovery.list_configurations(environment_id='envid')

    discovery.get_configuration(environment_id='envid',
                                configuration_id='confid')

    assert len(responses.calls) == 2

    discovery.create_configuration(environment_id='envid',
                                   config_data={'name': 'my name'})
    discovery.update_configuration(environment_id='envid',
                                   configuration_id='confid',
                                   config_data={'name': 'my new name'})
    discovery.delete_configuration(environment_id='envid',
                                   configuration_id='confid')

    assert len(responses.calls) == 5


@responses.activate
def test_document():
    discovery_url = urljoin(base_discovery_url,
                            'environments/envid/preview')
    config_url = urljoin(base_discovery_url,
                         'environments/envid/configurations')
    responses.add(responses.POST, discovery_url,
                  body="{\"configurations\": []}",
                  status=200,
                  content_type='application/json')
    responses.add(responses.GET, config_url,
                  body=json.dumps({"configurations":
                                  [{"name": "Default Configuration",
                                    "configuration_id": "confid"}]}),
                  status=200,
                  content_type='application/json')

    discovery = watson_developer_cloud.DiscoveryV1('2016-11-07',
                                                   username='username',
                                                   password='password')
    html_path = os.path.join(os.getcwd(), 'resources', 'simple.html')
    with open(html_path) as fileinfo:
        conf_id = discovery.test_document(environment_id='envid',
                                          configuration_id='bogus',
                                          fileinfo=fileinfo)
        assert conf_id is not None
        conf_id = discovery.test_document(environment_id='envid',
                                          fileinfo=fileinfo)
        assert conf_id is not None

    assert len(responses.calls) == 2

    add_doc_url = urljoin(base_discovery_url,
                          'environments/envid/collections/collid/documents')

    doc_id_path = 'environments/envid/collections/collid/documents/docid'

    update_doc_url = urljoin(base_discovery_url, doc_id_path)
    del_doc_url = urljoin(base_discovery_url,
                          doc_id_path)
    responses.add(responses.POST, add_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.GET, del_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.POST, update_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    responses.add(responses.DELETE, del_doc_url,
                  body="{\"body\": []}",
                  status=200,
                  content_type='application/json')

    html_path = os.path.join(os.getcwd(), 'resources', 'simple.html')
    with open(html_path) as fileinfo:
        conf_id = discovery.add_document(environment_id='envid',
                                         collection_id='collid',
                                         file_info=fileinfo)
        assert conf_id is not None

    assert len(responses.calls) == 3

    discovery.get_document(environment_id='envid',
                           collection_id='collid',
                           document_id='docid')

    assert len(responses.calls) == 4

    discovery.update_document(environment_id='envid',
                              collection_id='collid',
                              document_id='docid')

    assert len(responses.calls) == 5

    discovery.delete_document(environment_id='envid',
                              collection_id='collid',
                              document_id='docid')

    assert len(responses.calls) == 6

    conf_id = discovery.add_document(environment_id='envid',
                                     collection_id='collid',
                                     file_data='my string of file')

    assert len(responses.calls) == 7

    conf_id = discovery.add_document(environment_id='envid',
                                     collection_id='collid',
                                     file_data='my string of file',
                                     mime_type='application/html')

    assert len(responses.calls) == 8

    conf_id = discovery.add_document(environment_id='envid',
                                     collection_id='collid',
                                     file_data='my string of file',
                                     mime_type='application/html',
                                     metadata={'stuff': 'woot!'})

    assert len(responses.calls) == 9


@responses.activate
def test_delete_training_data():
    training_endpoint = '/v1/environments/{0}/collections/{1}/training_data'
    endpoint = training_endpoint.format(environment_id, collection_id)
    url = '{0}{1}'.format(base_url, endpoint)
    responses.add(responses.DELETE, url, status=204)

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.delete_training_data(environment_id=environment_id,
                                            collection_id=collection_id)

    assert response.status_code == 204


@responses.activate
def test_list_training_data():
    training_endpoint = '/v1/environments/{0}/collections/{1}/training_data'
    endpoint = training_endpoint.format(environment_id, collection_id)
    url = '{0}{1}'.format(base_url, endpoint)
    mock_response = {
        "environment_id": "string",
        "collection_id": "string",
        "queries": [
            {
                "query_id": "string",
                "natural_language_query": "string",
                "filter": "string",
                "examples": [
                    {
                        "document_id": "string",
                        "cross_reference": "string",
                        "relevance": 0
                    }
                ]
            }
        ]
    }
    responses.add(responses.GET,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.list_training_data(environment_id=environment_id,
                                          collection_id=collection_id)

    assert response == mock_response


@responses.activate
def test_add_training_data_query():
    training_endpoint = '/v1/environments/{0}/collections/{1}/training_data'
    endpoint = training_endpoint.format(environment_id, collection_id)
    url = '{0}{1}'.format(base_url, endpoint)
    query_id = "some_unique_id"
    natural_language_query = "why is the sky blue"
    filter = "text:meteorology"
    examples = [
        {
            "document_id": "54f95ac0-3e4f-4756-bea6-7a67b2713c81",
            "relevance": 1
        },
        {
            "document_id": "01bcca32-7300-4c9f-8d32-33ed7ea643da",
            "cross_reference": "my_id_field:1463",
            "relevance": 5
        }
    ]
    mock_response = {
        "query_id": "string",
        "natural_language_query": "string",
        "filter": "string",
        "examples": [
            {
                "document_id": "string",
                "cross_reference": "string",
                "relevance": 0
            }
        ]
    }
    responses.add(responses.POST,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.add_training_data_query(
        environment_id=environment_id,
        collection_id=collection_id,
        natural_language_query=natural_language_query,
        query_id=query_id,
        filter=filter,
        examples=examples)

    assert response == mock_response


@responses.activate
def test_delete_training_data_query():
    training_endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'
    query_id = 'queryid'
    endpoint = training_endpoint.format(environment_id, collection_id, query_id)
    url = '{0}{1}'.format(base_url, endpoint)
    responses.add(responses.DELETE, url, status=204)

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.delete_training_data_query(environment_id=environment_id,
                                                  collection_id=collection_id,
                                                  query_id=query_id)

    assert response.status_code == 204


@responses.activate
def test_get_training_data_query():
    training_endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'
    query_id = 'queryid'
    endpoint = training_endpoint.format(environment_id, collection_id, query_id)
    url = '{0}{1}'.format(base_url, endpoint)
    mock_response = {
        "query_id": "string",
        "natural_language_query": "string",
        "filter": "string",
        "examples": [
            {
                "document_id": "string",
                "cross_reference": "string",
                "relevance": 0
            }
        ]
    }
    responses.add(responses.GET,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.get_training_data_query(environment_id=environment_id,
                                               collection_id=collection_id,
                                               query_id=query_id)

    assert response == mock_response


@responses.activate
def test_list_training_data_query_examples():
    examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
        '/{2}/examples'
    query_id = 'queryid'
    endpoint = examples_endpoint.format(environment_id, collection_id, query_id)
    url = '{0}{1}'.format(base_url, endpoint)
    mock_response = [
        {
            "document_id": "string",
            "cross_reference": "string",
            "relevance": 0
        }
    ]
    responses.add(responses.GET,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.list_training_data_query_examples(
        environment_id=environment_id,
        collection_id=collection_id,
        query_id=query_id)

    assert response == mock_response


@responses.activate
def test_add_training_data_query_example():
    examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
        '/{2}/examples'
    query_id = 'queryid'
    endpoint = examples_endpoint.format(environment_id, collection_id, query_id)
    url = '{0}{1}'.format(base_url, endpoint)
    document_id = "string"
    relevance = 0
    cross_reference = "string"
    mock_response = {
        "document_id": "string",
        "cross_reference": "string",
        "relevance": 0
    }
    responses.add(responses.POST,
                  url,
                  body=json.dumps(mock_response),
                  status=201,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.add_training_data_query_example(
        environment_id=environment_id,
        collection_id=collection_id,
        query_id=query_id,
        document_id=document_id,
        relevance=relevance,
        cross_reference=cross_reference)

    assert response == mock_response


@responses.activate
def test_delete_training_data_query_example():
    examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
        '/{2}/examples/{3}'
    query_id = 'queryid'
    example_id = 'exampleid'
    endpoint = examples_endpoint.format(environment_id,
                                        collection_id,
                                        query_id,
                                        example_id)
    url = '{0}{1}'.format(base_url, endpoint)
    responses.add(responses.DELETE, url, status=204)

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.delete_training_data_query_example(
        environment_id=environment_id,
        collection_id=collection_id,
        query_id=query_id,
        example_id=example_id)

    assert response.status_code == 204


@responses.activate
def test_get_training_data_query_example():
    examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
        '/{2}/examples/{3}'
    query_id = 'queryid'
    example_id = 'exampleid'
    endpoint = examples_endpoint.format(environment_id,
                                        collection_id,
                                        query_id,
                                        example_id)
    url = '{0}{1}'.format(base_url, endpoint)
    mock_response = {
        "document_id": "string",
        "cross_reference": "string",
        "relevance": 0
    }
    responses.add(responses.GET,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.get_training_data_query_example(
        environment_id=environment_id,
        collection_id=collection_id,
        query_id=query_id,
        example_id=example_id)

    assert response == mock_response


@responses.activate
def test_update_training_data_query_example():
    examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
        '/{2}/examples/{3}'
    query_id = 'queryid'
    example_id = 'exampleid'
    endpoint = examples_endpoint.format(environment_id,
                                        collection_id,
                                        query_id,
                                        example_id)
    url = '{0}{1}'.format(base_url, endpoint)
    relevance = 0
    cross_reference = "string"
    mock_response = {
        "document_id": "string",
        "cross_reference": "string",
        "relevance": 0
    }
    responses.add(responses.PUT,
                  url,
                  body=json.dumps(mock_response),
                  status=200,
                  content_type='application/json')

    service = watson_developer_cloud.DiscoveryV1(version,
                                                 username='username',
                                                 password='password')
    response = service.update_training_data_query_example(
        environment_id=environment_id,
        collection_id=collection_id,
        query_id=query_id,
        example_id=example_id,
        relevance=relevance,
        cross_reference=cross_reference)

    assert response == mock_response
