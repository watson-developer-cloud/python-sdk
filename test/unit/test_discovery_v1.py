# coding: utf-8
import responses
import os
import json
import io
import time
import jwt
from unittest import TestCase
import ibm_watson
from ibm_watson.discovery_v1 import TrainingDataSet, TrainingQuery, TrainingExample
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator, IAMAuthenticator

from urllib.parse import urlparse, urljoin

base_discovery_url = 'https://gateway.watsonplatform.net/discovery/api/v1/'

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/discovery/api'
base_url = '{0}{1}'.format(platform_url, service_path)

version = '2016-12-01'
environment_id = 'envid'
collection_id = 'collid'

def get_access_token():
    access_token_layout = {
        "username": "dummy",
        "role": "Admin",
        "permissions": [
            "administrator",
            "manage_catalog"
        ],
        "sub": "admin",
        "iss": "sss",
        "aud": "sss",
        "uid": "sss",
        "iat": 3600,
        "exp": int(time.time())
    }

    access_token = jwt.encode(access_token_layout, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
    return access_token.decode('utf-8')

class TestDiscoveryV1(TestCase):
    @classmethod
    def setUp(cls):
        iam_url = "https://iam.cloud.ibm.com/identity/token"
        iam_token_response = {
            "access_token": get_access_token(),
            "token_type": "Bearer",
            "expires_in": 3600,
            "expiration": 1524167011,
            "refresh_token": "jy4gl91BQ"
        }
        responses.add(
            responses.POST, url=iam_url, body=json.dumps(iam_token_response), status=200)

    @classmethod
    @responses.activate
    def test_environments(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        discovery.list_environments()

        url_str = "{0}?version=2018-08-13".format(discovery_url)
        assert responses.calls[0].request.url == url_str

        assert responses.calls[0].response.text == discovery_response_body
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_get_environment(cls):
        discovery_url = urljoin(base_discovery_url, 'environments/envid')
        responses.add(responses.GET, discovery_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.get_environment(environment_id='envid')
        url_str = "{0}?version=2018-08-13".format(discovery_url)
        assert responses.calls[0].request.url == url_str
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_create_environment(cls):

        discovery_url = urljoin(base_discovery_url, 'environments')
        responses.add(responses.POST, discovery_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.create_environment(name="my name", description="my description")
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_update_environment(cls):
        discovery_url = urljoin(base_discovery_url, 'environments/envid')
        responses.add(responses.PUT, discovery_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.update_environment('envid', name="hello", description="new")
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_delete_environment(cls):
        discovery_url = urljoin(base_discovery_url, 'environments/envid')
        responses.add(responses.DELETE, discovery_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.delete_environment('envid')
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_collections(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/collections')

        responses.add(responses.GET, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.list_collections('envid')

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_collection(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.create_collection(environment_id='envid',
                                    name="name",
                                    description="",
                                    language="",
                                    configuration_id='confid')

        discovery.create_collection(environment_id='envid',
                                    name="name",
                                    language="es",
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

    @classmethod
    @responses.activate
    def test_federated_query(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/query')

        responses.add(responses.POST, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.federated_query('envid', filter='colls.sha1::9181d244*', collection_ids=['collid1', 'collid2'])

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_federated_query_2(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/query')

        responses.add(responses.POST, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.federated_query('envid', collection_ids="'collid1', 'collid2'",
                                  filter='colls.sha1::9181d244*',
                                  bias='1',
                                  logging_opt_out=True)

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_federated_query_notices(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/notices')

        responses.add(responses.GET, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')
        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        discovery.federated_query_notices('envid', collection_ids=['collid1', 'collid2'], filter='notices.sha1::9181d244*')

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_query(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/collections/collid/query')

        responses.add(responses.POST, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')
        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        discovery.query('envid', 'collid',
                        filter='extracted_metadata.sha1::9181d244*',
                        count=1,
                        passages=True,
                        passages_fields=['x', 'y'],
                        logging_opt_out='True',
                        passages_count=2)

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_query_2(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/collections/collid/query')

        responses.add(responses.POST, discovery_url,
                      body="{\"body\": \"hello\"}", status=200,
                      content_type='application/json')
        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        discovery.query('envid', 'collid',
                        filter='extracted_metadata.sha1::9181d244*',
                        count=1,
                        passages=True,
                        passages_fields=['x', 'y'],
                        logging_opt_out='True',
                        passages_count=2,
                        bias='1',
                        collection_ids='1,2')

        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)

        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_query_notices(cls):
        discovery_url = urljoin(
            base_discovery_url,
            'environments/envid/collections/collid/notices')

        responses.add(
            responses.GET,
            discovery_url,
            body="{\"body\": \"hello\"}",
            status=200,
            content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.query_notices('envid', 'collid', filter='notices.sha1::*')
        called_url = urlparse(responses.calls[0].request.url)
        test_url = urlparse(discovery_url)
        assert called_url.netloc == test_url.netloc
        assert called_url.path == test_url.path
        assert len(responses.calls) == 1


    @classmethod
    @responses.activate
    def test_configs(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/configurations')
        discovery_config_id = urljoin(base_discovery_url,
                                      'environments/envid/configurations/confid')

        results = {"configurations":[{"name": "Default Configuration", "configuration_id": "confid"}]}

        responses.add(responses.GET, discovery_url,
                      body=json.dumps(results),
                      status=200,
                      content_type='application/json')

        responses.add(responses.GET, discovery_config_id,
                      body=json.dumps(results['configurations'][0]),
                      status=200,
                      content_type='application/json')
        responses.add(responses.POST, discovery_url,
                      body=json.dumps(results['configurations'][0]),
                      status=200,
                      content_type='application/json')
        responses.add(responses.PUT, discovery_config_id,
                      body=json.dumps(results['configurations'][0]),
                      status=200,
                      content_type='application/json')
        responses.add(responses.DELETE, discovery_config_id,
                      body=json.dumps({'deleted': 'bogus -- ok'}),
                      status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        discovery.list_configurations(environment_id='envid')

        discovery.get_configuration(environment_id='envid',
                                    configuration_id='confid')

        assert len(responses.calls) == 2

        discovery.create_configuration(environment_id='envid',
                                       name='my name')
        discovery.create_configuration(environment_id='envid',
                                       name='my name',
                                       source={'type': 'salesforce', 'credential_id': 'xxx'})
        discovery.update_configuration(environment_id='envid',
                                       configuration_id='confid',
                                       name='my new name')
        discovery.update_configuration(environment_id='envid',
                                       configuration_id='confid',
                                       name='my new name',
                                       source={'type': 'salesforce', 'credential_id': 'xxx'})
        discovery.delete_configuration(environment_id='envid',
                                       configuration_id='confid')

        assert len(responses.calls) == 7


    @classmethod
    @responses.activate
    def test_document(cls):
        discovery_url = urljoin(base_discovery_url,
                                'environments/envid/preview')
        config_url = urljoin(base_discovery_url,
                             'environments/envid/configurations')
        responses.add(responses.POST, discovery_url,
                      body="{\"configurations\": []}",
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, config_url,
                      body=json.dumps({"configurations": [{"name": "Default Configuration", "configuration_id": "confid"}]}),
                      status=200,
                      content_type='application/json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

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

        doc_status = {
            "document_id": "45556e23-f2b1-449d-8f27-489b514000ff",
            "configuration_id": "2e079259-7dd2-40a9-998f-3e716f5a7b88",
            "created" : "2016-06-16T10:56:54.957Z",
            "updated" : "2017-05-16T13:56:54.957Z",
            "status": "available",
            "status_description": "Document is successfully ingested and indexed with no warnings",
            "notices": []
            }

        responses.add(responses.GET, del_doc_url,
                      body=json.dumps(doc_status),
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
                                             file=fileinfo)
            assert conf_id is not None

        assert len(responses.calls) == 1

        discovery.get_document_status(environment_id='envid',
                                      collection_id='collid',
                                      document_id='docid')

        assert len(responses.calls) == 2

        discovery.update_document(environment_id='envid',
                                  collection_id='collid',
                                  document_id='docid')

        assert len(responses.calls) == 3

        discovery.update_document(environment_id='envid',
                                  collection_id='collid',
                                  document_id='docid')

        assert len(responses.calls) == 4

        discovery.delete_document(environment_id='envid',
                                  collection_id='collid',
                                  document_id='docid')

        assert len(responses.calls) == 5

        conf_id = discovery.add_document(environment_id='envid',
                                         collection_id='collid',
                                         file=io.StringIO(u'my string of file'),
                                         filename='file.txt')

        assert len(responses.calls) == 6

        conf_id = discovery.add_document(environment_id='envid',
                                         collection_id='collid',
                                         file=io.StringIO(u'<h1>my string of file</h1>'),
                                         filename='file.html',
                                         file_content_type='application/html')

        assert len(responses.calls) == 7

        conf_id = discovery.add_document(environment_id='envid',
                                         collection_id='collid',
                                         file=io.StringIO(u'<h1>my string of file</h1>'),
                                         filename='file.html',
                                         file_content_type='application/html',
                                         metadata=io.StringIO(u'{"stuff": "woot!"}'))

        assert len(responses.calls) == 8


    @classmethod
    @responses.activate
    def test_delete_all_training_data(cls):
        training_endpoint = '/v1/environments/{0}/collections/{1}/training_data'
        endpoint = training_endpoint.format(environment_id, collection_id)
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.DELETE, url, status=204)

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.delete_all_training_data(environment_id=environment_id,
                                                      collection_id=collection_id).get_result()

        assert response is None


    @classmethod
    @responses.activate
    def test_list_training_data(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.list_training_data(environment_id=environment_id,
                                                collection_id=collection_id).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingDataSet
        TrainingDataSet._from_dict(response)


    @classmethod
    @responses.activate
    def test_add_training_data(cls):
        training_endpoint = '/v1/environments/{0}/collections/{1}/training_data'
        endpoint = training_endpoint.format(environment_id, collection_id)
        url = '{0}{1}'.format(base_url, endpoint)
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.add_training_data(
            environment_id=environment_id,
            collection_id=collection_id,
            natural_language_query=natural_language_query,
            filter=filter,
            examples=examples).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingQuery
        TrainingQuery._from_dict(response)


    @classmethod
    @responses.activate
    def test_delete_training_data(cls):
        training_endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'
        query_id = 'queryid'
        endpoint = training_endpoint.format(
            environment_id, collection_id, query_id)
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(responses.DELETE, url, status=204)

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.delete_training_data(environment_id=environment_id,
                                                  collection_id=collection_id,
                                                  query_id=query_id).get_result()

        assert response is None


    @classmethod
    @responses.activate
    def test_get_training_data(cls):
        training_endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'
        query_id = 'queryid'
        endpoint = training_endpoint.format(
            environment_id, collection_id, query_id)
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        response = discovery.get_training_data(environment_id=environment_id,
                                               collection_id=collection_id,
                                               query_id=query_id).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingQuery
        TrainingQuery._from_dict(response)


    @classmethod
    @responses.activate
    def test_create_training_example(cls):
        examples_endpoint = '/v1/environments/{0}/collections/{1}/training_data' + \
            '/{2}/examples'
        query_id = 'queryid'
        endpoint = examples_endpoint.format(
            environment_id, collection_id, query_id)
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.create_training_example(
            environment_id=environment_id,
            collection_id=collection_id,
            query_id=query_id,
            document_id=document_id,
            relevance=relevance,
            cross_reference=cross_reference).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingExample
        TrainingExample._from_dict(response)


    @classmethod
    @responses.activate
    def test_delete_training_example(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)
        response = discovery.delete_training_example(
            environment_id=environment_id,
            collection_id=collection_id,
            query_id=query_id,
            example_id=example_id).get_result()

        assert response is None


    @classmethod
    @responses.activate
    def test_get_training_example(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.get_training_example(
            environment_id=environment_id,
            collection_id=collection_id,
            query_id=query_id,
            example_id=example_id).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingExample
        TrainingExample._from_dict(response)


    @classmethod
    @responses.activate
    def test_update_training_example(cls):
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

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.update_training_example(
            environment_id=environment_id,
            collection_id=collection_id,
            query_id=query_id,
            example_id=example_id,
            relevance=relevance,
            cross_reference=cross_reference).get_result()

        assert response == mock_response
        # Verify that response can be converted to a TrainingExample
        TrainingExample._from_dict(response)

    @classmethod
    @responses.activate
    def test_expansions(cls):
        url = 'https://gateway.watsonplatform.net/discovery/api/v1/environments/envid/collections/colid/expansions'
        responses.add(
            responses.GET,
            url,
            body='{"expansions": "results"}',
            status=200,
            content_type='application_json')
        responses.add(
            responses.DELETE,
            url,
            body='{"description": "success" }',
            status=200,
            content_type='application_json')
        responses.add(
            responses.POST,
            url,
            body='{"expansions": "success" }',
            status=200,
            content_type='application_json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.list_expansions('envid', 'colid')
        assert responses.calls[0].response.json() == {"expansions": "results"}

        discovery.create_expansions('envid', 'colid', [{"input_terms": "dumb", "expanded_terms": "dumb2"}])
        assert responses.calls[1].response.json() == {"expansions": "success"}

        discovery.delete_expansions('envid', 'colid')
        assert responses.calls[2].response.json() == {"description": "success"}

        assert len(responses.calls) == 3

    @classmethod
    @responses.activate
    def test_delete_user_data(cls):
        url = 'https://gateway.watsonplatform.net/discovery/api/v1/user_data'
        responses.add(
            responses.DELETE,
            url,
            body='{"description": "success" }',
            status=204,
            content_type='application_json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        response = discovery.delete_user_data('id').get_result()
        assert response is None
        assert len(responses.calls) == 1

    @classmethod
    @responses.activate
    def test_credentials(cls):
        discovery_credentials_url = urljoin(base_discovery_url, 'environments/envid/credentials')

        results = {'credential_id': 'e68305ce-29f3-48ea-b829-06653ca0fdef',
                   'source_type': 'salesforce',
                   'credential_details': {
                       'url': 'https://login.salesforce.com',
                       'credential_type': 'username_password',
                       'username':'user@email.com'}
                  }
        authenticator = IAMAuthenticator('iam_apikey')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        responses.add(responses.GET, "{0}/{1}?version=2018-08-13".format(discovery_credentials_url, 'credential_id'),
                      body=json.dumps(results),
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, "{0}?version=2018-08-13".format(discovery_credentials_url),
                      body=json.dumps([results]),
                      status=200,
                      content_type='application/json')

        responses.add(responses.POST, "{0}?version=2018-08-13".format(discovery_credentials_url),
                      body=json.dumps(results),
                      status=200,
                      content_type='application/json')
        results['source_type'] = 'ibm'
        responses.add(responses.PUT, "{0}/{1}?version=2018-08-13".format(discovery_credentials_url, 'credential_id'),
                      body=json.dumps(results),
                      status=200,
                      content_type='application/json')
        responses.add(responses.DELETE, "{0}/{1}?version=2018-08-13".format(discovery_credentials_url, 'credential_id'),
                      body=json.dumps({'deleted': 'bogus -- ok'}),
                      status=200,
                      content_type='application/json')

        discovery.create_credentials('envid', source_type='salesforce', credential_details={
            'url': 'https://login.salesforce.com',
            'credential_type': 'username_password',
            'username':'user@email.com'
            })

        discovery.get_credentials('envid', 'credential_id')

        discovery.update_credentials(environment_id='envid',
                                     credential_id='credential_id',
                                     source_type='salesforce',
                                     credential_details=results['credential_details'])
        discovery.list_credentials('envid')
        discovery.delete_credentials(environment_id='envid', credential_id='credential_id')
        assert len(responses.calls) == 10

    @classmethod
    @responses.activate
    def test_events_and_feedback(cls):
        discovery_event_url = urljoin(base_discovery_url, 'events')
        discovery_metrics_event_rate_url = urljoin(base_discovery_url, 'metrics/event_rate')
        discovery_metrics_query_url = urljoin(base_discovery_url, 'metrics/number_of_queries')
        discovery_metrics_query_event_url = urljoin(base_discovery_url, 'metrics/number_of_queries_with_event')
        discovery_metrics_query_no_results_url = urljoin(base_discovery_url, 'metrics/number_of_queries_with_no_search_results')
        discovery_metrics_query_token_event_url = urljoin(base_discovery_url, 'metrics/top_query_tokens_with_event_rate')
        discovery_query_log_url = urljoin(base_discovery_url, 'logs')

        event_data = {
            "environment_id": "xxx",
            "session_token": "yyy",
            "client_timestamp": "2018-08-14T14:39:59.268Z",
            "display_rank": 0,
            "collection_id": "abc",
            "document_id": "xyz",
            "query_id": "cde"
        }

        create_event_response = {
            "type": "click",
            "data": event_data
        }

        metric_response = {
            "aggregations": [
                {
                    "interval": "1d",
                    "event_type": "click",
                    "results": [
                        {
                            "key_as_string": "2018-08-14T14:39:59.309Z",
                            "key": 1533513600000,
                            "matching_results": 2,
                            "event_rate": 0.0
                        }
                    ]
                }
            ]
        }

        metric_token_response = {
            "aggregations": [
                {
                    "event_type": "click",
                    "results": [
                        {
                            "key": "content",
                            "matching_results": 5,
                            "event_rate": 0.6
                        },
                        {
                            "key": "first",
                            "matching_results": 5,
                            "event_rate": 0.6
                        },
                        {
                            "key": "of",
                            "matching_results": 5,
                            "event_rate": 0.6
                        }
                    ]
                }
            ]
        }

        log_query_response = {
            "matching_results": 20,
            "results": [
                {
                    "customer_id": "",
                    "environment_id": "xxx",
                    "natural_language_query": "The content of the first chapter",
                    "query_id": "1ICUdh3Pab",
                    "document_results": {
                        "count": 1,
                        "results": [
                            {
                                "collection_id": "b67a82f3-6507-4c25-9757-3485ff4f2a32",
                                "score": 0.025773458,
                                "position": 10,
                                "document_id": "af0be20e-e130-4712-9a2e-37d9c8b9c52f"
                            }
                        ]
                    },
                    "event_type": "query",
                    "session_token": "1_nbEfQtKVcg9qx3t41ICUdh3Pab",
                    "created_timestamp": "2018-08-14T18:20:30.460Z"
                }
            ]
        }

        responses.add(responses.POST, "{0}?version=2018-08-13".format(discovery_event_url),
                      body=json.dumps(create_event_response),
                      status=200,
                      content_type='application/json')

        responses.add(responses.GET, "{0}?version=2018-08-13&start_time=2018-08-13T14%3A39%3A59.309Z&end_time=2018-08-14T14%3A39%3A59.309Z&result_type=document".format(discovery_metrics_event_rate_url),
                      body=json.dumps(metric_response),
                      status=200,
                      content_type='application/json')

        responses.add(responses.GET, "{0}?version=2018-08-13&start_time=2018-08-13T14%3A39%3A59.309Z&end_time=2018-08-14T14%3A39%3A59.309Z&result_type=document".format(discovery_metrics_query_url),
                      body=json.dumps(metric_response),
                      status=200,
                      content_type='application/json')

        responses.add(responses.GET, "{0}?version=2018-08-13&start_time=2018-08-13T14%3A39%3A59.309Z&end_time=2018-08-14T14%3A39%3A59.309Z&result_type=document".format(discovery_metrics_query_event_url),
                      body=json.dumps(metric_response),
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, "{0}?version=2018-08-13&start_time=2018-08-13T14%3A39%3A59.309Z&end_time=2018-08-14T14%3A39%3A59.309Z&result_type=document".format(discovery_metrics_query_no_results_url),
                      body=json.dumps(metric_response),
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, "{0}?version=2018-08-13&count=2".format(discovery_metrics_query_token_event_url),
                      body=json.dumps(metric_token_response),
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, "{0}?version=2018-08-13".format(discovery_query_log_url),
                      body=json.dumps(log_query_response),
                      status=200,
                      content_type='application/json')


        authenticator = IAMAuthenticator('iam_apikey')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.create_event('click', event_data)
        assert responses.calls[1].response.json()["data"] == event_data

        discovery.get_metrics_event_rate(start_time='2018-08-13T14:39:59.309Z',
                                         end_time='2018-08-14T14:39:59.309Z',
                                         result_type='document')
        assert responses.calls[3].response.json() == metric_response

        discovery.get_metrics_query(start_time='2018-08-13T14:39:59.309Z',
                                    end_time='2018-08-14T14:39:59.309Z',
                                    result_type='document')
        assert responses.calls[5].response.json() == metric_response

        discovery.get_metrics_query_event(
            start_time='2018-08-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document')
        assert responses.calls[7].response.json() == metric_response

        discovery.get_metrics_query_no_results(
            start_time='2018-08-13T14:39:59.309Z',
            end_time='2018-08-14T14:39:59.309Z',
            result_type='document')
        assert responses.calls[9].response.json() == metric_response

        discovery.get_metrics_query_token_event(count=2)
        assert responses.calls[11].response.json() == metric_token_response

        discovery.query_log()
        assert responses.calls[13].response.json() == log_query_response

        assert len(responses.calls) == 14

    @classmethod
    @responses.activate
    def test_tokenization_dictionary(cls):
        url = 'https://gateway.watsonplatform.net/discovery/api/v1/environments/envid/collections/colid/word_lists/tokenization_dictionary?version=2018-08-13'
        responses.add(
            responses.POST,
            url,
            body='{"status": "pending"}',
            status=200,
            content_type='application_json')
        responses.add(
            responses.DELETE,
            url,
            body='{"status": "pending"}',
            status=200)
        responses.add(
            responses.GET,
            url,
            body='{"status": "pending", "type":"tokenization_dictionary"}',
            status=200,
            content_type='application_json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        tokenization_rules = [
            {
                'text': 'token',
                'tokens': ['token 1', 'token 2'],
                'readings': ['reading 1', 'reading 2'],
                'part_of_speech': 'noun',
            }
        ]

        discovery.create_tokenization_dictionary('envid', 'colid', tokenization_rules=tokenization_rules)
        assert responses.calls[0].response.json() == {"status": "pending"}

        discovery.get_tokenization_dictionary_status('envid', 'colid')
        assert responses.calls[1].response.json() == {"status": "pending", "type":"tokenization_dictionary"}

        discovery.delete_tokenization_dictionary('envid', 'colid')
        assert responses.calls[2].response.status_code == 200

        assert len(responses.calls) == 3

    @classmethod
    @responses.activate
    def test_stopword_operations(cls):
        url = 'https://gateway.watsonplatform.net/discovery/api/v1/environments/envid/collections/colid/word_lists/stopwords?version=2018-08-13'
        responses.add(
            responses.POST,
            url,
            body='{"status": "pending", "type": "stopwords"}',
            status=200,
            content_type='application_json')
        responses.add(
            responses.DELETE,
            url,
            status=200)
        responses.add(
            responses.GET,
            url,
            body='{"status": "ready", "type": "stopwords"}',
            status=200,
            content_type='application_json')

        authenticator = BasicAuthenticator('username', 'password')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        stopwords_file_path = os.path.join(os.getcwd(), 'resources', 'stopwords.txt')
        with open(stopwords_file_path) as file:
            discovery.create_stopword_list('envid', 'colid', file)
            assert responses.calls[0].response.json() == {"status": "pending", "type": "stopwords"}

        discovery.get_stopword_list_status('envid', 'colid')
        assert responses.calls[1].response.json() == {"status": "ready", "type": "stopwords"}

        discovery.delete_stopword_list('envid', 'colid')
        assert responses.calls[2].response.status_code == 200

        assert len(responses.calls) == 3


    @classmethod
    @responses.activate
    def test_gateway_configuration(cls):
        discovery_gateway_url = urljoin(base_discovery_url, 'environments/envid/gateways')

        gateway_details = {
            "status": "idle",
            "token_id": "9GnaCreixek_prod_ng",
            "token": "4FByv9Mmd79x6c",
            "name": "test-gateway-configuration-python",
            "gateway_id": "gateway_id"
        }

        responses.add(responses.GET, "{0}/{1}?version=2018-08-13".format(discovery_gateway_url, 'gateway_id'),
                      body=json.dumps(gateway_details),
                      status=200,
                      content_type='application/json')
        responses.add(responses.POST, "{0}?version=2018-08-13".format(discovery_gateway_url),
                      body=json.dumps(gateway_details),
                      status=200,
                      content_type='application/json')
        responses.add(responses.GET, "{0}?version=2018-08-13".format(discovery_gateway_url),
                      body=json.dumps({'gateways': [gateway_details]}),
                      status=200,
                      content_type='application/json')
        responses.add(responses.DELETE, "{0}/{1}?version=2018-08-13".format(discovery_gateway_url, 'gateway_id'),
                      body=json.dumps({'gateway_id': 'gateway_id', 'status': 'deleted'}),
                      status=200,
                      content_type='application/json')

        authenticator = IAMAuthenticator('iam_apikey')
        discovery = ibm_watson.DiscoveryV1('2018-08-13', authenticator=authenticator)

        discovery.create_gateway('envid', name='gateway_id')
        discovery.list_gateways('envid')
        discovery.get_gateway('envid', 'gateway_id')
        discovery.delete_gateway(environment_id='envid', gateway_id='gateway_id')
        assert len(responses.calls) == 8
