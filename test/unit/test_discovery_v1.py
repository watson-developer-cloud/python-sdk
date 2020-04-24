# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2016, 2020.
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
import ibm_watson.discovery_v1
from ibm_watson.discovery_v1 import *

base_url = 'https://gateway.watsonplatform.net/discovery/api'

##############################################################################
# Start of Service: Environments
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_environment
#-----------------------------------------------------------------------------
class TestCreateEnvironment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_environment_response(self):
        body = self.construct_full_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_environment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_environment_empty(self):
        check_empty_required_params(self, fake_response_Environment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_environment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "description": "string1", "size": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "description": "string1", "size": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_environments
#-----------------------------------------------------------------------------
class TestListEnvironments():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_environments_response(self):
        body = self.construct_full_body()
        response = fake_response_ListEnvironmentsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_environments_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListEnvironmentsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_environments_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_environments(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_environment
#-----------------------------------------------------------------------------
class TestGetEnvironment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_environment_response(self):
        body = self.construct_full_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_environment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_environment_empty(self):
        check_empty_required_params(self, fake_response_Environment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_environment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_environment
#-----------------------------------------------------------------------------
class TestUpdateEnvironment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_environment_response(self):
        body = self.construct_full_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_environment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Environment_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_environment_empty(self):
        check_empty_required_params(self, fake_response_Environment_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_environment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "size": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "size": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_environment
#-----------------------------------------------------------------------------
class TestDeleteEnvironment():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_environment_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteEnvironmentResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_environment_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteEnvironmentResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_environment_empty(self):
        check_empty_required_params(self, fake_response_DeleteEnvironmentResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_environment(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
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
        response = fake_response_ListCollectionFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_fields_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListCollectionFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_fields_empty(self):
        check_empty_required_params(self, fake_response_ListCollectionFieldsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/fields'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_fields(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_ids'] = []
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_ids'] = []
        return body


# endregion
##############################################################################
# End of Service: Environments
##############################################################################

##############################################################################
# Start of Service: Configurations
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_configuration
#-----------------------------------------------------------------------------
class TestCreateConfiguration():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_configuration_response(self):
        body = self.construct_full_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_configuration_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_configuration_empty(self):
        check_empty_required_params(self, fake_response_Configuration_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/configurations'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_configuration(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "conversions": Conversions._from_dict(json.loads("""{"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}""")), "enrichments": [], "normalizations": [], "source": Source._from_dict(json.loads("""{"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "conversions": Conversions._from_dict(json.loads("""{"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}""")), "enrichments": [], "normalizations": [], "source": Source._from_dict(json.loads("""{"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}""")), })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_configurations
#-----------------------------------------------------------------------------
class TestListConfigurations():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_configurations_response(self):
        body = self.construct_full_body()
        response = fake_response_ListConfigurationsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_configurations_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListConfigurationsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_configurations_empty(self):
        check_empty_required_params(self, fake_response_ListConfigurationsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/configurations'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_configurations(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_configuration
#-----------------------------------------------------------------------------
class TestGetConfiguration():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_configuration_response(self):
        body = self.construct_full_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_configuration_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_configuration_empty(self):
        check_empty_required_params(self, fake_response_Configuration_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/configurations/{1}'.format(body['environment_id'], body['configuration_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_configuration(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_configuration
#-----------------------------------------------------------------------------
class TestUpdateConfiguration():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_configuration_response(self):
        body = self.construct_full_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_configuration_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Configuration_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_configuration_empty(self):
        check_empty_required_params(self, fake_response_Configuration_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/configurations/{1}'.format(body['environment_id'], body['configuration_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_configuration(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "conversions": Conversions._from_dict(json.loads("""{"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}""")), "enrichments": [], "normalizations": [], "source": Source._from_dict(json.loads("""{"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "conversions": Conversions._from_dict(json.loads("""{"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}""")), "enrichments": [], "normalizations": [], "source": Source._from_dict(json.loads("""{"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}""")), })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_configuration
#-----------------------------------------------------------------------------
class TestDeleteConfiguration():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_configuration_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteConfigurationResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_configuration_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteConfigurationResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_configuration_empty(self):
        check_empty_required_params(self, fake_response_DeleteConfigurationResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/configurations/{1}'.format(body['environment_id'], body['configuration_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_configuration(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['configuration_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Configurations
##############################################################################

##############################################################################
# Start of Service: Collections
##############################################################################
# region

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
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_collection_empty(self):
        check_empty_required_params(self, fake_response_Collection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "configuration_id": "string1", "language": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "configuration_id": "string1", "language": "string1", })
        return body


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
        endpoint = '/v1/environments/{0}/collections'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_collections(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
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
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_collection_empty(self):
        check_empty_required_params(self, fake_response_Collection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
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
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_collection_empty(self):
        check_empty_required_params(self, fake_response_Collection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "configuration_id": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "configuration_id": "string1", })
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
        response = fake_response_DeleteCollectionResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_collection_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteCollectionResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_collection_empty(self):
        check_empty_required_params(self, fake_response_DeleteCollectionResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_collection_fields
#-----------------------------------------------------------------------------
class TestListCollectionFields():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collection_fields_response(self):
        body = self.construct_full_body()
        response = fake_response_ListCollectionFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collection_fields_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ListCollectionFieldsResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collection_fields_empty(self):
        check_empty_required_params(self, fake_response_ListCollectionFieldsResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/fields'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_collection_fields(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: QueryModifications
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_expansions
#-----------------------------------------------------------------------------
class TestListExpansions():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_expansions_response(self):
        body = self.construct_full_body()
        response = fake_response_Expansions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_expansions_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Expansions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_expansions_empty(self):
        check_empty_required_params(self, fake_response_Expansions_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/expansions'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_expansions(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_expansions
#-----------------------------------------------------------------------------
class TestCreateExpansions():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_expansions_response(self):
        body = self.construct_full_body()
        response = fake_response_Expansions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_expansions_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Expansions_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_expansions_empty(self):
        check_empty_required_params(self, fake_response_Expansions_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/expansions'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_expansions(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"expansions": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"expansions": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_expansions
#-----------------------------------------------------------------------------
class TestDeleteExpansions():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_expansions_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_expansions_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_expansions_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/expansions'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_expansions(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_tokenization_dictionary_status
#-----------------------------------------------------------------------------
class TestGetTokenizationDictionaryStatus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_tokenization_dictionary_status_response(self):
        body = self.construct_full_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_tokenization_dictionary_status_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_tokenization_dictionary_status_empty(self):
        check_empty_required_params(self, fake_response_TokenDictStatusResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_tokenization_dictionary_status(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_tokenization_dictionary
#-----------------------------------------------------------------------------
class TestCreateTokenizationDictionary():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_tokenization_dictionary_response(self):
        body = self.construct_full_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_tokenization_dictionary_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_tokenization_dictionary_empty(self):
        check_empty_required_params(self, fake_response_TokenDictStatusResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_tokenization_dictionary(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"tokenization_rules": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_tokenization_dictionary
#-----------------------------------------------------------------------------
class TestDeleteTokenizationDictionary():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tokenization_dictionary_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tokenization_dictionary_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_tokenization_dictionary_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/tokenization_dictionary'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_tokenization_dictionary(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_stopword_list_status
#-----------------------------------------------------------------------------
class TestGetStopwordListStatus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_stopword_list_status_response(self):
        body = self.construct_full_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_stopword_list_status_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_stopword_list_status_empty(self):
        check_empty_required_params(self, fake_response_TokenDictStatusResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_stopword_list_status(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_stopword_list
#-----------------------------------------------------------------------------
class TestCreateStopwordList():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_stopword_list_response(self):
        body = self.construct_full_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_stopword_list_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TokenDictStatusResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_stopword_list_empty(self):
        check_empty_required_params(self, fake_response_TokenDictStatusResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_stopword_list(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['stopword_file'] = tempfile.NamedTemporaryFile()
        body['stopword_filename'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['stopword_file'] = tempfile.NamedTemporaryFile()
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_stopword_list
#-----------------------------------------------------------------------------
class TestDeleteStopwordList():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_stopword_list_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_stopword_list_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_stopword_list_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/word_lists/stopwords'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_stopword_list(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: QueryModifications
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
        endpoint = '/v1/environments/{0}/collections/{1}/documents'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.add_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['metadata'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_document_status
#-----------------------------------------------------------------------------
class TestGetDocumentStatus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_status_response(self):
        body = self.construct_full_body()
        response = fake_response_DocumentStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_status_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DocumentStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_document_status_empty(self):
        check_empty_required_params(self, fake_response_DocumentStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(body['environment_id'], body['collection_id'], body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_document_status(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
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
        endpoint = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(body['environment_id'], body['collection_id'], body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['metadata'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
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
        endpoint = '/v1/environments/{0}/collections/{1}/documents/{2}'.format(body['environment_id'], body['collection_id'], body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['document_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Documents
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
        endpoint = '/v1/environments/{0}/collections/{1}/query'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"filter": "string1", "query": "string1", "natural_language_query": "string1", "passages": True, "aggregation": "string1", "count": 12345, "return_": "string1", "offset": 12345, "sort": "string1", "highlight": True, "passages_fields": "string1", "passages_count": 12345, "passages_characters": 12345, "deduplicate": True, "deduplicate_field": "string1", "similar": True, "similar_document_ids": "string1", "similar_fields": "string1", "bias": "string1", "spelling_suggestions": True, })
        body['x_watson_logging_opt_out'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
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
        endpoint = '/v1/environments/{0}/collections/{1}/notices'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.query_notices(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['filter'] = "string1"
        body['query'] = "string1"
        body['natural_language_query'] = "string1"
        body['passages'] = True
        body['aggregation'] = "string1"
        body['count'] = 12345
        body['return_'] = []
        body['offset'] = 12345
        body['sort'] = []
        body['highlight'] = True
        body['passages_fields'] = []
        body['passages_count'] = 12345
        body['passages_characters'] = 12345
        body['deduplicate_field'] = "string1"
        body['similar'] = True
        body['similar_document_ids'] = []
        body['similar_fields'] = []
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for federated_query
#-----------------------------------------------------------------------------
class TestFederatedQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_response(self):
        body = self.construct_full_body()
        response = fake_response_QueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_QueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_empty(self):
        check_empty_required_params(self, fake_response_QueryResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/query'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.federated_query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"collection_ids": "string1", "filter": "string1", "query": "string1", "natural_language_query": "string1", "passages": True, "aggregation": "string1", "count": 12345, "return_": "string1", "offset": 12345, "sort": "string1", "highlight": True, "passages_fields": "string1", "passages_count": 12345, "passages_characters": 12345, "deduplicate": True, "deduplicate_field": "string1", "similar": True, "similar_document_ids": "string1", "similar_fields": "string1", "bias": "string1", })
        body['x_watson_logging_opt_out'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"collection_ids": "string1", "filter": "string1", "query": "string1", "natural_language_query": "string1", "passages": True, "aggregation": "string1", "count": 12345, "return_": "string1", "offset": 12345, "sort": "string1", "highlight": True, "passages_fields": "string1", "passages_count": 12345, "passages_characters": 12345, "deduplicate": True, "deduplicate_field": "string1", "similar": True, "similar_document_ids": "string1", "similar_fields": "string1", "bias": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for federated_query_notices
#-----------------------------------------------------------------------------
class TestFederatedQueryNotices():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_notices_response(self):
        body = self.construct_full_body()
        response = fake_response_QueryNoticesResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_notices_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_QueryNoticesResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_federated_query_notices_empty(self):
        check_empty_required_params(self, fake_response_QueryNoticesResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/notices'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.federated_query_notices(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_ids'] = []
        body['filter'] = "string1"
        body['query'] = "string1"
        body['natural_language_query'] = "string1"
        body['aggregation'] = "string1"
        body['count'] = 12345
        body['return_'] = []
        body['offset'] = 12345
        body['sort'] = []
        body['highlight'] = True
        body['deduplicate_field'] = "string1"
        body['similar'] = True
        body['similar_document_ids'] = []
        body['similar_fields'] = []
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_ids'] = []
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
        endpoint = '/v1/environments/{0}/collections/{1}/autocompletion'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_autocompletion(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['prefix'] = "string1"
        body['field'] = "string1"
        body['count'] = 12345
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['prefix'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: TrainingData
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_training_data
#-----------------------------------------------------------------------------
class TestListTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingDataSet_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingDataSet_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_data_empty(self):
        check_empty_required_params(self, fake_response_TrainingDataSet_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for add_training_data
#-----------------------------------------------------------------------------
class TestAddTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_training_data_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuery_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.add_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"natural_language_query": "string1", "filter": "string1", "examples": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body.update({"natural_language_query": "string1", "filter": "string1", "examples": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_all_training_data
#-----------------------------------------------------------------------------
class TestDeleteAllTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_all_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_all_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_all_training_data_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data'.format(body['environment_id'], body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_all_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_training_data
#-----------------------------------------------------------------------------
class TestGetTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingQuery_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_data_empty(self):
        check_empty_required_params(self, fake_response_TrainingQuery_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(body['environment_id'], body['collection_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_training_data
#-----------------------------------------------------------------------------
class TestDeleteTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_data_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}'.format(body['environment_id'], body['collection_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_training_examples
#-----------------------------------------------------------------------------
class TestListTrainingExamples():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_examples_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingExampleList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_examples_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingExampleList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_training_examples_empty(self):
        check_empty_required_params(self, fake_response_TrainingExampleList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(body['environment_id'], body['collection_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_training_examples(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_training_example
#-----------------------------------------------------------------------------
class TestCreateTrainingExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_example_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_training_example_empty(self):
        check_empty_required_params(self, fake_response_TrainingExample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples'.format(body['environment_id'], body['collection_id'], body['query_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_training_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body.update({"document_id": "string1", "cross_reference": "string1", "relevance": 12345, })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body.update({"document_id": "string1", "cross_reference": "string1", "relevance": 12345, })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_training_example
#-----------------------------------------------------------------------------
class TestDeleteTrainingExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_example_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_training_example_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(body['environment_id'], body['collection_id'], body['query_id'], body['example_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_training_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_training_example
#-----------------------------------------------------------------------------
class TestUpdateTrainingExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_example_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_training_example_empty(self):
        check_empty_required_params(self, fake_response_TrainingExample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(body['environment_id'], body['collection_id'], body['query_id'], body['example_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_training_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        body.update({"cross_reference": "string1", "relevance": 12345, })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        body.update({"cross_reference": "string1", "relevance": 12345, })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_training_example
#-----------------------------------------------------------------------------
class TestGetTrainingExample():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_example_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_example_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingExample_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_example_empty(self):
        check_empty_required_params(self, fake_response_TrainingExample_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/collections/{1}/training_data/{2}/examples/{3}'.format(body['environment_id'], body['collection_id'], body['query_id'], body['example_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_training_example(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['collection_id'] = "string1"
        body['query_id'] = "string1"
        body['example_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: TrainingData
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
        endpoint = '/v1/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
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

##############################################################################
# Start of Service: EventsAndFeedback
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_event
#-----------------------------------------------------------------------------
class TestCreateEvent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_event_response(self):
        body = self.construct_full_body()
        response = fake_response_CreateEventResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_event_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CreateEventResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_event_empty(self):
        check_empty_required_params(self, fake_response_CreateEventResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/events'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_event(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"type": "string1", "data": EventData._from_dict(json.loads("""{"environment_id": "fake_environment_id", "session_token": "fake_session_token", "client_timestamp": "2017-05-16T13:56:54.957Z", "display_rank": 12, "collection_id": "fake_collection_id", "document_id": "fake_document_id", "query_id": "fake_query_id"}""")), })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"type": "string1", "data": EventData._from_dict(json.loads("""{"environment_id": "fake_environment_id", "session_token": "fake_session_token", "client_timestamp": "2017-05-16T13:56:54.957Z", "display_rank": 12, "collection_id": "fake_collection_id", "document_id": "fake_document_id", "query_id": "fake_query_id"}""")), })
        return body


#-----------------------------------------------------------------------------
# Test Class for query_log
#-----------------------------------------------------------------------------
class TestQueryLog():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_log_response(self):
        body = self.construct_full_body()
        response = fake_response_LogQueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_log_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LogQueryResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_query_log_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/logs'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.query_log(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['filter'] = "string1"
        body['query'] = "string1"
        body['count'] = 12345
        body['offset'] = 12345
        body['sort'] = []
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_metrics_query
#-----------------------------------------------------------------------------
class TestGetMetricsQuery():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_response(self):
        body = self.construct_full_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/metrics/number_of_queries'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_metrics_query(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['start_time'] = datetime.now()
        body['end_time'] = datetime.now()
        body['result_type'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_metrics_query_event
#-----------------------------------------------------------------------------
class TestGetMetricsQueryEvent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_event_response(self):
        body = self.construct_full_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_event_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_event_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/metrics/number_of_queries_with_event'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_metrics_query_event(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['start_time'] = datetime.now()
        body['end_time'] = datetime.now()
        body['result_type'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_metrics_query_no_results
#-----------------------------------------------------------------------------
class TestGetMetricsQueryNoResults():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_no_results_response(self):
        body = self.construct_full_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_no_results_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_no_results_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/metrics/number_of_queries_with_no_search_results'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_metrics_query_no_results(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['start_time'] = datetime.now()
        body['end_time'] = datetime.now()
        body['result_type'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_metrics_event_rate
#-----------------------------------------------------------------------------
class TestGetMetricsEventRate():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_event_rate_response(self):
        body = self.construct_full_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_event_rate_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MetricResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_event_rate_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/metrics/event_rate'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_metrics_event_rate(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['start_time'] = datetime.now()
        body['end_time'] = datetime.now()
        body['result_type'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_metrics_query_token_event
#-----------------------------------------------------------------------------
class TestGetMetricsQueryTokenEvent():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_token_event_response(self):
        body = self.construct_full_body()
        response = fake_response_MetricTokenResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_token_event_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_MetricTokenResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_metrics_query_token_event_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/metrics/top_query_tokens_with_event_rate'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_metrics_query_token_event(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['count'] = 12345
        return body

    def construct_required_body(self):
        body = dict()
        return body


# endregion
##############################################################################
# End of Service: EventsAndFeedback
##############################################################################

##############################################################################
# Start of Service: Credentials
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_credentials
#-----------------------------------------------------------------------------
class TestListCredentials():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_credentials_response(self):
        body = self.construct_full_body()
        response = fake_response_CredentialsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_credentials_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CredentialsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_credentials_empty(self):
        check_empty_required_params(self, fake_response_CredentialsList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/credentials'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_credentials(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_credentials
#-----------------------------------------------------------------------------
class TestCreateCredentials():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_credentials_response(self):
        body = self.construct_full_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_credentials_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_credentials_empty(self):
        check_empty_required_params(self, fake_response_Credentials_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/credentials'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_credentials(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"source_type": "string1", "credential_details": CredentialDetails._from_dict(json.loads("""{"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}""")), "status": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"source_type": "string1", "credential_details": CredentialDetails._from_dict(json.loads("""{"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}""")), "status": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_credentials
#-----------------------------------------------------------------------------
class TestGetCredentials():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_credentials_response(self):
        body = self.construct_full_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_credentials_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_credentials_empty(self):
        check_empty_required_params(self, fake_response_Credentials_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/credentials/{1}'.format(body['environment_id'], body['credential_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_credentials(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_credentials
#-----------------------------------------------------------------------------
class TestUpdateCredentials():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_credentials_response(self):
        body = self.construct_full_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_credentials_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Credentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_credentials_empty(self):
        check_empty_required_params(self, fake_response_Credentials_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/credentials/{1}'.format(body['environment_id'], body['credential_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.update_credentials(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        body.update({"source_type": "string1", "credential_details": CredentialDetails._from_dict(json.loads("""{"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}""")), "status": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        body.update({"source_type": "string1", "credential_details": CredentialDetails._from_dict(json.loads("""{"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}""")), "status": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_credentials
#-----------------------------------------------------------------------------
class TestDeleteCredentials():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_credentials_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteCredentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_credentials_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteCredentials_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_credentials_empty(self):
        check_empty_required_params(self, fake_response_DeleteCredentials_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/credentials/{1}'.format(body['environment_id'], body['credential_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_credentials(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['credential_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Credentials
##############################################################################

##############################################################################
# Start of Service: GatewayConfiguration
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_gateways
#-----------------------------------------------------------------------------
class TestListGateways():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateways_response(self):
        body = self.construct_full_body()
        response = fake_response_GatewayList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateways_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_GatewayList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_gateways_empty(self):
        check_empty_required_params(self, fake_response_GatewayList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/gateways'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.list_gateways(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_gateway
#-----------------------------------------------------------------------------
class TestCreateGateway():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_response(self):
        body = self.construct_full_body()
        response = fake_response_Gateway_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Gateway_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_gateway_empty(self):
        check_empty_required_params(self, fake_response_Gateway_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/gateways'.format(body['environment_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.create_gateway(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body.update({"name": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_gateway
#-----------------------------------------------------------------------------
class TestGetGateway():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_response(self):
        body = self.construct_full_body()
        response = fake_response_Gateway_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Gateway_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_gateway_empty(self):
        check_empty_required_params(self, fake_response_Gateway_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/gateways/{1}'.format(body['environment_id'], body['gateway_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.get_gateway(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['gateway_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['gateway_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_gateway
#-----------------------------------------------------------------------------
class TestDeleteGateway():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_response(self):
        body = self.construct_full_body()
        response = fake_response_GatewayDelete_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_GatewayDelete_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_gateway_empty(self):
        check_empty_required_params(self, fake_response_GatewayDelete_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/environments/{0}/gateways/{1}'.format(body['environment_id'], body['gateway_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = DiscoveryV1(
            authenticator=NoAuthAuthenticator(),
            version='2019-04-30',
            )
        service.set_service_url(base_url)
        output = service.delete_gateway(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['gateway_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['environment_id'] = "string1"
        body['gateway_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: GatewayConfiguration
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
fake_response_Environment_json = """{"environment_id": "fake_environment_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "read_only": false, "size": "fake_size", "requested_size": "fake_requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "fake_scope", "status": "fake_status", "status_description": "fake_status_description"}}"""
fake_response_ListEnvironmentsResponse_json = """{"environments": []}"""
fake_response_Environment_json = """{"environment_id": "fake_environment_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "read_only": false, "size": "fake_size", "requested_size": "fake_requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "fake_scope", "status": "fake_status", "status_description": "fake_status_description"}}"""
fake_response_Environment_json = """{"environment_id": "fake_environment_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "read_only": false, "size": "fake_size", "requested_size": "fake_requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "fake_scope", "status": "fake_status", "status_description": "fake_status_description"}}"""
fake_response_DeleteEnvironmentResponse_json = """{"environment_id": "fake_environment_id", "status": "fake_status"}"""
fake_response_ListCollectionFieldsResponse_json = """{"fields": []}"""
fake_response_Configuration_json = """{"configuration_id": "fake_configuration_id", "name": "fake_name", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "description": "fake_description", "conversions": {"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}, "enrichments": [], "normalizations": [], "source": {"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}}"""
fake_response_ListConfigurationsResponse_json = """{"configurations": []}"""
fake_response_Configuration_json = """{"configuration_id": "fake_configuration_id", "name": "fake_name", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "description": "fake_description", "conversions": {"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}, "enrichments": [], "normalizations": [], "source": {"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}}"""
fake_response_Configuration_json = """{"configuration_id": "fake_configuration_id", "name": "fake_name", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "description": "fake_description", "conversions": {"pdf": {"heading": {"fonts": []}}, "word": {"heading": {"fonts": [], "styles": []}}, "html": {"exclude_tags_completely": [], "exclude_tags_keep_content": [], "keep_content": {"xpaths": []}, "exclude_content": {"xpaths": []}, "keep_tag_attributes": [], "exclude_tag_attributes": []}, "segment": {"enabled": false, "selector_tags": [], "annotated_fields": []}, "json_normalizations": [], "image_text_recognition": true}, "enrichments": [], "normalizations": [], "source": {"type": "fake_type", "credential_id": "fake_credential_id", "schedule": {"enabled": false, "time_zone": "fake_time_zone", "frequency": "fake_frequency"}, "options": {"folders": [], "objects": [], "site_collections": [], "urls": [], "buckets": [], "crawl_all_buckets": false}}}"""
fake_response_DeleteConfigurationResponse_json = """{"configuration_id": "fake_configuration_id", "status": "fake_status", "notices": []}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "configuration_id": "fake_configuration_id", "language": "fake_language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2017-05-16T13:56:54.957Z", "data_updated": "2017-05-16T13:56:54.957Z"}, "crawl_status": {"source_crawl": {"status": "fake_status", "next_crawl": "2017-05-16T13:56:54.957Z"}}, "smart_document_understanding": {"enabled": false, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}"""
fake_response_ListCollectionsResponse_json = """{"collections": []}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "configuration_id": "fake_configuration_id", "language": "fake_language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2017-05-16T13:56:54.957Z", "data_updated": "2017-05-16T13:56:54.957Z"}, "crawl_status": {"source_crawl": {"status": "fake_status", "next_crawl": "2017-05-16T13:56:54.957Z"}}, "smart_document_understanding": {"enabled": false, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "status": "fake_status", "configuration_id": "fake_configuration_id", "language": "fake_language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2017-05-16T13:56:54.957Z", "data_updated": "2017-05-16T13:56:54.957Z"}, "crawl_status": {"source_crawl": {"status": "fake_status", "next_crawl": "2017-05-16T13:56:54.957Z"}}, "smart_document_understanding": {"enabled": false, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}"""
fake_response_DeleteCollectionResponse_json = """{"collection_id": "fake_collection_id", "status": "fake_status"}"""
fake_response_ListCollectionFieldsResponse_json = """{"fields": []}"""
fake_response_Expansions_json = """{"expansions": []}"""
fake_response_Expansions_json = """{"expansions": []}"""
fake_response_TokenDictStatusResponse_json = """{"status": "fake_status", "type": "fake_type"}"""
fake_response_TokenDictStatusResponse_json = """{"status": "fake_status", "type": "fake_type"}"""
fake_response_TokenDictStatusResponse_json = """{"status": "fake_status", "type": "fake_type"}"""
fake_response_TokenDictStatusResponse_json = """{"status": "fake_status", "type": "fake_type"}"""
fake_response_DocumentAccepted_json = """{"document_id": "fake_document_id", "status": "fake_status", "notices": []}"""
fake_response_DocumentStatus_json = """{"document_id": "fake_document_id", "configuration_id": "fake_configuration_id", "status": "fake_status", "status_description": "fake_status_description", "filename": "fake_filename", "file_type": "fake_file_type", "sha1": "fake_sha1", "notices": []}"""
fake_response_DocumentAccepted_json = """{"document_id": "fake_document_id", "status": "fake_status", "notices": []}"""
fake_response_DeleteDocumentResponse_json = """{"document_id": "fake_document_id", "status": "fake_status"}"""
fake_response_QueryResponse_json = """{"matching_results": 16, "results": [], "aggregations": [], "passages": [], "duplicates_removed": 18, "session_token": "fake_session_token", "retrieval_details": {"document_retrieval_strategy": "fake_document_retrieval_strategy"}, "suggested_query": "fake_suggested_query"}"""
fake_response_QueryNoticesResponse_json = """{"matching_results": 16, "results": [], "aggregations": [], "passages": [], "duplicates_removed": 18}"""
fake_response_QueryResponse_json = """{"matching_results": 16, "results": [], "aggregations": [], "passages": [], "duplicates_removed": 18, "session_token": "fake_session_token", "retrieval_details": {"document_retrieval_strategy": "fake_document_retrieval_strategy"}, "suggested_query": "fake_suggested_query"}"""
fake_response_QueryNoticesResponse_json = """{"matching_results": 16, "results": [], "aggregations": [], "passages": [], "duplicates_removed": 18}"""
fake_response_Completions_json = """{"completions": []}"""
fake_response_TrainingDataSet_json = """{"environment_id": "fake_environment_id", "collection_id": "fake_collection_id", "queries": []}"""
fake_response_TrainingQuery_json = """{"query_id": "fake_query_id", "natural_language_query": "fake_natural_language_query", "filter": "fake_filter", "examples": []}"""
fake_response_TrainingQuery_json = """{"query_id": "fake_query_id", "natural_language_query": "fake_natural_language_query", "filter": "fake_filter", "examples": []}"""
fake_response_TrainingExampleList_json = """{"examples": []}"""
fake_response_TrainingExample_json = """{"document_id": "fake_document_id", "cross_reference": "fake_cross_reference", "relevance": 9}"""
fake_response_TrainingExample_json = """{"document_id": "fake_document_id", "cross_reference": "fake_cross_reference", "relevance": 9}"""
fake_response_TrainingExample_json = """{"document_id": "fake_document_id", "cross_reference": "fake_cross_reference", "relevance": 9}"""
fake_response_CreateEventResponse_json = """{"type": "fake_type", "data": {"environment_id": "fake_environment_id", "session_token": "fake_session_token", "client_timestamp": "2017-05-16T13:56:54.957Z", "display_rank": 12, "collection_id": "fake_collection_id", "document_id": "fake_document_id", "query_id": "fake_query_id"}}"""
fake_response_LogQueryResponse_json = """{"matching_results": 16, "results": []}"""
fake_response_MetricResponse_json = """{"aggregations": []}"""
fake_response_MetricResponse_json = """{"aggregations": []}"""
fake_response_MetricResponse_json = """{"aggregations": []}"""
fake_response_MetricResponse_json = """{"aggregations": []}"""
fake_response_MetricTokenResponse_json = """{"aggregations": []}"""
fake_response_CredentialsList_json = """{"credentials": []}"""
fake_response_Credentials_json = """{"credential_id": "fake_credential_id", "source_type": "fake_source_type", "credential_details": {"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}, "status": "fake_status"}"""
fake_response_Credentials_json = """{"credential_id": "fake_credential_id", "source_type": "fake_source_type", "credential_details": {"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}, "status": "fake_status"}"""
fake_response_Credentials_json = """{"credential_id": "fake_credential_id", "source_type": "fake_source_type", "credential_details": {"credential_type": "fake_credential_type", "client_id": "fake_client_id", "enterprise_id": "fake_enterprise_id", "url": "fake_url", "username": "fake_username", "organization_url": "fake_organization_url", "site_collection.path": "fake_site_collection_path", "client_secret": "fake_client_secret", "public_key_id": "fake_public_key_id", "private_key": "fake_private_key", "passphrase": "fake_passphrase", "password": "fake_password", "gateway_id": "fake_gateway_id", "source_version": "fake_source_version", "web_application_url": "fake_web_application_url", "domain": "fake_domain", "endpoint": "fake_endpoint", "access_key_id": "fake_access_key_id", "secret_access_key": "fake_secret_access_key"}, "status": "fake_status"}"""
fake_response_DeleteCredentials_json = """{"credential_id": "fake_credential_id", "status": "fake_status"}"""
fake_response_GatewayList_json = """{"gateways": []}"""
fake_response_Gateway_json = """{"gateway_id": "fake_gateway_id", "name": "fake_name", "status": "fake_status", "token": "fake_token", "token_id": "fake_token_id"}"""
fake_response_Gateway_json = """{"gateway_id": "fake_gateway_id", "name": "fake_name", "status": "fake_status", "token": "fake_token", "token_id": "fake_token_id"}"""
fake_response_GatewayDelete_json = """{"gateway_id": "fake_gateway_id", "status": "fake_status"}"""
