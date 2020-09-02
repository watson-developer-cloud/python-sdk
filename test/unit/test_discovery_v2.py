# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2019, 2020.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from datetime import datetime
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
import tempfile
import ibm_watson.discovery_v2
from ibm_watson.discovery_v2 import *

base_url = 'https://api.us-south.discovery.watson.cloud.ibm.com'

##############################################################################
# Start of Service: Collections
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_collections
#-----------------------------------------------------------------------------
class TestListCollections():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collections_response(self):
        body = self.construct_full_body()
        response = fake_response_ListCollectionsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collections_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListCollectionsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collections_empty(self):
        check_empty_required_params(self, fake_response_ListCollectionsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.list_collections(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_collection
#-----------------------------------------------------------------------------
class TestCreateCollection():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_collection_response(self):
        body = self.construct_full_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_collection_empty(self):
        check_empty_required_params(self, fake_response_CollectionDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.create_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "language": "string1", "enrichments": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "language": "string1", "enrichments": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_collection
#-----------------------------------------------------------------------------
class TestGetCollection():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_collection_response(self):
        body = self.construct_full_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_collection_empty(self):
        check_empty_required_params(self, fake_response_CollectionDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}'.format(body['project_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_collection
#-----------------------------------------------------------------------------
class TestUpdateCollection():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_collection_response(self):
        body = self.construct_full_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CollectionDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_collection_empty(self):
        check_empty_required_params(self, fake_response_CollectionDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}'.format(body['project_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.update_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "enrichments": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "enrichments": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_collection
#-----------------------------------------------------------------------------
class TestDeleteCollection():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_collection_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_collection_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}'.format(body['project_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: Queries
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for query
#-----------------------------------------------------------------------------
class TestQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_response(self):
        body = self.construct_full_body()
        response = fake_response_QueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_QueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_empty(self):
        check_empty_required_params(self, fake_response_QueryResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/query'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"collection_ids": [], "filter": "string1", "query": "string1", "natural_language_query": "string1", "aggregation": "string1", "count": 12345, "return_": [], "offset": 12345, "sort": "string1", "highlight": True, "spelling_suggestions": True, "table_results": QueryLargeTableResults._from_dict(json.loads("""{"enabled": false, "count": 5}""")), "suggested_refinements": QueryLargeSuggestedRefinements._from_dict(json.loads("""{"enabled": false, "count": 5}""")), "passages": QueryLargePassages._from_dict(json.loads("""{"enabled": false, "per_document": true, "max_per_document": 16, "fields": [], "count": 5, "characters": 10}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_autocompletion
#-----------------------------------------------------------------------------
class TestGetAutocompletion():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_autocompletion_response(self):
        body = self.construct_full_body()
        response = fake_response_Completions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_autocompletion_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Completions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_autocompletion_empty(self):
        check_empty_required_params(self, fake_response_Completions_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/autocompletion'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_autocompletion(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['prefix'] = "string1"
        body['collection_ids'] = []
        body['field'] = "string1"
        body['count'] = 12345
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['prefix'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for query_notices
#-----------------------------------------------------------------------------
class TestQueryNotices():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_notices_response(self):
        body = self.construct_full_body()
        response = fake_response_QueryNoticesResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_notices_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_QueryNoticesResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_notices_empty(self):
        check_empty_required_params(self, fake_response_QueryNoticesResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/notices'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.query_notices(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['filter'] = "string1"
        body['query'] = "string1"
        body['natural_language_query'] = "string1"
        body['count'] = 12345
        body['offset'] = 12345
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_fields
#-----------------------------------------------------------------------------
class TestListFields():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_fields_response(self):
        body = self.construct_full_body()
        response = fake_response_ListFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_fields_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_fields_empty(self):
        check_empty_required_params(self, fake_response_ListFieldsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/fields'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.list_fields(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_ids'] = []
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: ComponentSettings
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_component_settings
#-----------------------------------------------------------------------------
class TestGetComponentSettings():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_component_settings_response(self):
        body = self.construct_full_body()
        response = fake_response_ComponentSettingsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_component_settings_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ComponentSettingsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_component_settings_empty(self):
        check_empty_required_params(self, fake_response_ComponentSettingsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/component_settings'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_component_settings(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: ComponentSettings
##############################################################################

##############################################################################
# Start of Service: Documents
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for add_document
#-----------------------------------------------------------------------------
class TestAddDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_document_response(self):
        body = self.construct_full_body()
        response = fake_response_DocumentAccepted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DocumentAccepted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_document_empty(self):
        check_empty_required_params(self, fake_response_DocumentAccepted_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}/documents'.format(body['project_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.add_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['metadata'] = "string1"
        body['x_watson_discovery_force'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_document
#-----------------------------------------------------------------------------
class TestUpdateDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_document_response(self):
        body = self.construct_full_body()
        response = fake_response_DocumentAccepted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DocumentAccepted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_document_empty(self):
        check_empty_required_params(self, fake_response_DocumentAccepted_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}/documents/{2}'.format(body['project_id'], body['collection_id'], body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.update_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['metadata'] = "string1"
        body['x_watson_discovery_force'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_document
#-----------------------------------------------------------------------------
class TestDeleteDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_document_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteDocumentResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteDocumentResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_document_empty(self):
        check_empty_required_params(self, fake_response_DeleteDocumentResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}/documents/{2}'.format(body['project_id'], body['collection_id'], body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        body['x_watson_discovery_force'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: TrainingData
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_training_queries
#-----------------------------------------------------------------------------
class TestListTrainingQueries():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_queries_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuerySet_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_queries_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuerySet_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_queries_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuerySet_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/training_data/queries'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.list_training_queries(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_training_queries
#-----------------------------------------------------------------------------
class TestDeleteTrainingQueries():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_queries_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_queries_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_queries_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/training_data/queries'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_training_queries(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_training_query
#-----------------------------------------------------------------------------
class TestCreateTrainingQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_query_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_query_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuery_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/training_data/queries'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.create_training_query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"natural_language_query": "string1", "examples": [], "filter": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"natural_language_query": "string1", "examples": [], "filter": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_training_query
#-----------------------------------------------------------------------------
class TestGetTrainingQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_query_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_query_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuery_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/training_data/queries/{1}'.format(body['project_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_training_query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['query_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['query_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_training_query
#-----------------------------------------------------------------------------
class TestUpdateTrainingQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_query_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_query_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuery_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/training_data/queries/{1}'.format(body['project_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.update_training_query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['query_id'] = "string1"
        body.update({"natural_language_query": "string1", "examples": [], "filter": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['query_id'] = "string1"
        body.update({"natural_language_query": "string1", "examples": [], "filter": "string1", })
        return body


# endregion
##############################################################################
# End of Service: TrainingData
##############################################################################

##############################################################################
# Start of Service: Analyze
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for analyze_document
#-----------------------------------------------------------------------------
class TestAnalyzeDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_document_response(self):
        body = self.construct_full_body()
        response = fake_response_AnalyzedDocument_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AnalyzedDocument_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_document_empty(self):
        check_empty_required_params(self, fake_response_AnalyzedDocument_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/collections/{1}/analyze'.format(body['project_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.analyze_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['metadata'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['collection_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Analyze
##############################################################################

##############################################################################
# Start of Service: Enrichments
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_enrichments
#-----------------------------------------------------------------------------
class TestListEnrichments():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_enrichments_response(self):
        body = self.construct_full_body()
        response = fake_response_Enrichments_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_enrichments_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Enrichments_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_enrichments_empty(self):
        check_empty_required_params(self, fake_response_Enrichments_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/enrichments'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.list_enrichments(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_enrichment
#-----------------------------------------------------------------------------
class TestCreateEnrichment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_enrichment_response(self):
        body = self.construct_full_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_enrichment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_enrichment_empty(self):
        check_empty_required_params(self, fake_response_Enrichment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/enrichments'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.create_enrichment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment'] = {"enrichment": {"mock": "data"}}
        body['file'] = tempfile.NamedTemporaryFile()
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment'] = {"enrichment": {"mock": "data"}}
        return body


#-----------------------------------------------------------------------------
# Test Class for get_enrichment
#-----------------------------------------------------------------------------
class TestGetEnrichment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_enrichment_response(self):
        body = self.construct_full_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_enrichment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_enrichment_empty(self):
        check_empty_required_params(self, fake_response_Enrichment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/enrichments/{1}'.format(body['project_id'], body['enrichment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_enrichment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_enrichment
#-----------------------------------------------------------------------------
class TestUpdateEnrichment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_enrichment_response(self):
        body = self.construct_full_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_enrichment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Enrichment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_enrichment_empty(self):
        check_empty_required_params(self, fake_response_Enrichment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/enrichments/{1}'.format(body['project_id'], body['enrichment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.update_enrichment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_enrichment
#-----------------------------------------------------------------------------
class TestDeleteEnrichment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_enrichment_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_enrichment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_enrichment_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}/enrichments/{1}'.format(body['project_id'], body['enrichment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_enrichment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        body['enrichment_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Enrichments
##############################################################################

##############################################################################
# Start of Service: Projects
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_projects
#-----------------------------------------------------------------------------
class TestListProjects():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_projects_response(self):
        body = self.construct_full_body()
        response = fake_response_ListProjectsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_projects_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListProjectsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_projects_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.list_projects(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for create_project
#-----------------------------------------------------------------------------
class TestCreateProject():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_project_response(self):
        body = self.construct_full_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_project_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_project_empty(self):
        check_empty_required_params(self, fake_response_ProjectDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.create_project(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "type": "string1", "default_query_parameters": DefaultQueryParams._from_dict(json.loads("""{"collection_ids": [], "passages": {"enabled": false, "count": 5, "fields": [], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "fake_aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "fake_sort", "return": []}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "type": "string1", "default_query_parameters": DefaultQueryParams._from_dict(json.loads("""{"collection_ids": [], "passages": {"enabled": false, "count": 5, "fields": [], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "fake_aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "fake_sort", "return": []}""")), })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_project
#-----------------------------------------------------------------------------
class TestGetProject():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_project_response(self):
        body = self.construct_full_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_project_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_project_empty(self):
        check_empty_required_params(self, fake_response_ProjectDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.get_project(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_project
#-----------------------------------------------------------------------------
class TestUpdateProject():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_project_response(self):
        body = self.construct_full_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_project_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ProjectDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_project_empty(self):
        check_empty_required_params(self, fake_response_ProjectDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.update_project(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        body.update({"name": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_project
#-----------------------------------------------------------------------------
class TestDeleteProject():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_project_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_project_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_project_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/projects/{0}'.format(body['project_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_project(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['project_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Projects
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for delete_user_data
#-----------------------------------------------------------------------------
class TestDeleteUserData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_user_data_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v2/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV2(
            authenticator=NoAuthAuthenticator(),
            version='2019-11-22',
            )
        service.set_service_url(base_url)
        output = service.delete_user_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customer_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customer_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: UserData
##############################################################################


def check_empty_required_params(obj, response):
    """Test function to assert that the operation will throw an error when given empty required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    body = {k: None for k in body.keys()}
    error = False
    try:
        send_request(obj, body, response)
    except ValueError as e:
        error = True
    assert error

def check_missing_required_params(obj):
    """Test function to assert that the operation will throw an error when missing required data

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    error = False
    try:
        send_request(obj, {}, {}, url=url)
    except TypeError as e:
        error = True
    assert error

def check_empty_response(obj):
    """Test function to assert that the operation will return an empty response when given an empty request

    Args:
        obj: The generated test function

    """
    body = obj.construct_full_body()
    url = obj.make_url(body)
    send_request(obj, {}, {}, url=url)

def send_request(obj, body, response, url=None):
    """Test function to create a request, send it, and assert its accuracy to the mock response

    Args:
        obj: The generated test function
        body: Dict filled with fake data for calling the service
        response_str: Mock response string

    """
    if not url:
        url = obj.make_url(body)
    obj.add_mock_response(url, response)
    output = obj.call_service(body)
    assert responses.calls[0].request.url.startswith(url)
    assert output.get_result() == response

####################
## Mock Responses ##
####################

fake_response__json = None
fake_response_ListCollectionsResponse_json = """{"collections": []}"""
fake_response_CollectionDetails_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "language": "fake_language", "enrichments": []}"""
fake_response_CollectionDetails_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "language": "fake_language", "enrichments": []}"""
fake_response_CollectionDetails_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "language": "fake_language", "enrichments": []}"""
fake_response_QueryResponse_json = """{"matching_results": 16, "results": [], "aggregations": [], "retrieval_details": {"document_retrieval_strategy": "fake_document_retrieval_strategy"}, "suggested_query": "fake_suggested_query", "suggested_refinements": [], "table_results": []}"""
fake_response_Completions_json = """{"completions": []}"""
fake_response_QueryNoticesResponse_json = """{"matching_results": 16, "notices": []}"""
fake_response_ListFieldsResponse_json = """{"fields": []}"""
fake_response_ComponentSettingsResponse_json = """{"fields_shown": {"body": {"use_passage": false, "field": "fake_field"}, "title": {"field": "fake_field"}}, "autocomplete": true, "structured_search": false, "results_per_page": 16, "aggregations": []}"""
fake_response_DocumentAccepted_json = """{"document_id": "fake_document_id", "status": "fake_status"}"""
fake_response_DocumentAccepted_json = """{"document_id": "fake_document_id", "status": "fake_status"}"""
fake_response_DeleteDocumentResponse_json = """{"document_id": "fake_document_id", "status": "fake_status"}"""
fake_response_TrainingQuerySet_json = """{"queries": []}"""
fake_response_TrainingQuery_json = """{"query_id": "fake_query_id", "natural_language_query": "fake_natural_language_query", "filter": "fake_filter", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_TrainingQuery_json = """{"query_id": "fake_query_id", "natural_language_query": "fake_natural_language_query", "filter": "fake_filter", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_TrainingQuery_json = """{"query_id": "fake_query_id", "natural_language_query": "fake_natural_language_query", "filter": "fake_filter", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "examples": []}"""
fake_response_AnalyzedDocument_json = """{"notices": [], "result": {}}"""
fake_response_Enrichments_json = """{"enrichments": []}"""
fake_response_Enrichment_json = """{"enrichment_id": "fake_enrichment_id", "name": "fake_name", "description": "fake_description", "type": "fake_type", "options": {"languages": [], "entity_type": "fake_entity_type", "regular_expression": "fake_regular_expression", "result_field": "fake_result_field"}}"""
fake_response_Enrichment_json = """{"enrichment_id": "fake_enrichment_id", "name": "fake_name", "description": "fake_description", "type": "fake_type", "options": {"languages": [], "entity_type": "fake_entity_type", "regular_expression": "fake_regular_expression", "result_field": "fake_result_field"}}"""
fake_response_Enrichment_json = """{"enrichment_id": "fake_enrichment_id", "name": "fake_name", "description": "fake_description", "type": "fake_type", "options": {"languages": [], "entity_type": "fake_entity_type", "regular_expression": "fake_regular_expression", "result_field": "fake_result_field"}}"""
fake_response_ListProjectsResponse_json = """{"projects": []}"""
fake_response_ProjectDetails_json = """{"project_id": "fake_project_id", "name": "fake_name", "type": "fake_type", "relevancy_training_status": {"data_updated": "fake_data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "fake_successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": [], "passages": {"enabled": false, "count": 5, "fields": [], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "fake_aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "fake_sort", "return": []}}"""
fake_response_ProjectDetails_json = """{"project_id": "fake_project_id", "name": "fake_name", "type": "fake_type", "relevancy_training_status": {"data_updated": "fake_data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "fake_successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": [], "passages": {"enabled": false, "count": 5, "fields": [], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "fake_aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "fake_sort", "return": []}}"""
fake_response_ProjectDetails_json = """{"project_id": "fake_project_id", "name": "fake_name", "type": "fake_type", "relevancy_training_status": {"data_updated": "fake_data_updated", "total_examples": 14, "sufficient_label_diversity": true, "processing": true, "minimum_examples_added": true, "successfully_trained": "fake_successfully_trained", "available": false, "notices": 7, "minimum_queries_added": false}, "collection_count": 16, "default_query_parameters": {"collection_ids": [], "passages": {"enabled": false, "count": 5, "fields": [], "characters": 10, "per_document": true, "max_per_document": 16}, "table_results": {"enabled": false, "count": 5, "per_document": 12}, "aggregation": "fake_aggregation", "suggested_refinements": {"enabled": false, "count": 5}, "spelling_suggestions": true, "highlight": false, "count": 5, "sort": "fake_sort", "return": []}}"""
