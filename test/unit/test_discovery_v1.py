# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2016, 2021.
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

"""
Unit Tests for DiscoveryV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import date_to_string, string_to_date
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watson.discovery_v1 import *

version = 'testString'

_service = DiscoveryV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.discovery.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Environments
##############################################################################
# region

class TestCreateEnvironment():
    """
    Test Class for create_environment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_environment_all_params(self):
        """
        create_environment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        description = 'testString'
        size = 'LT'

        # Invoke method
        response = _service.create_environment(
            name,
            description=description,
            size=size,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['size'] == 'LT'


    @responses.activate
    def test_create_environment_value_error(self):
        """
        test_create_environment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        description = 'testString'
        size = 'LT'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_environment(**req_copy)



class TestListEnvironments():
    """
    Test Class for list_environments
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_environments_all_params(self):
        """
        list_environments()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments')
        mock_response = '{"environments": [{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        name = 'testString'

        # Invoke method
        response = _service.list_environments(
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'name={}'.format(name) in query_string


    @responses.activate
    def test_list_environments_required_params(self):
        """
        test_list_environments_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments')
        mock_response = '{"environments": [{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_environments()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_environments_value_error(self):
        """
        test_list_environments_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments')
        mock_response = '{"environments": [{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_environments(**req_copy)



class TestGetEnvironment():
    """
    Test Class for get_environment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_environment_all_params(self):
        """
        get_environment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.get_environment(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_environment_value_error(self):
        """
        test_get_environment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_environment(**req_copy)



class TestUpdateEnvironment():
    """
    Test Class for update_environment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_environment_all_params(self):
        """
        update_environment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        size = 'S'

        # Invoke method
        response = _service.update_environment(
            environment_id,
            name=name,
            description=description,
            size=size,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['size'] == 'S'


    @responses.activate
    def test_update_environment_value_error(self):
        """
        test_update_environment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "read_only": false, "size": "LT", "requested_size": "requested_size", "index_capacity": {"documents": {"available": 9, "maximum_allowed": 15}, "disk_usage": {"used_bytes": 10, "maximum_allowed_bytes": 21}, "collections": {"available": 9, "maximum_allowed": 15}}, "search_status": {"scope": "scope", "status": "NO_DATA", "status_description": "status_description", "last_trained": "2019-01-01"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        size = 'S'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_environment(**req_copy)



class TestDeleteEnvironment():
    """
    Test Class for delete_environment
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_environment_all_params(self):
        """
        delete_environment()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.delete_environment(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_environment_value_error(self):
        """
        test_delete_environment_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString')
        mock_response = '{"environment_id": "environment_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_environment(**req_copy)



class TestListFields():
    """
    Test Class for list_fields
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_fields_all_params(self):
        """
        list_fields()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = ['testString']

        # Invoke method
        response = _service.list_fields(
            environment_id,
            collection_ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string


    @responses.activate
    def test_list_fields_value_error(self):
        """
        test_list_fields_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_ids": collection_ids,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_fields(**req_copy)



# endregion
##############################################################################
# End of Service: Environments
##############################################################################

##############################################################################
# Start of Service: Configurations
##############################################################################
# region

class TestCreateConfiguration():
    """
    Test Class for create_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_configuration_all_params(self):
        """
        create_configuration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a FontSetting model
        font_setting_model = {}
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        # Construct a dict representation of a PdfHeadingDetection model
        pdf_heading_detection_model = {}
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        # Construct a dict representation of a PdfSettings model
        pdf_settings_model = {}
        pdf_settings_model['heading'] = pdf_heading_detection_model

        # Construct a dict representation of a WordStyle model
        word_style_model = {}
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        # Construct a dict representation of a WordHeadingDetection model
        word_heading_detection_model = {}
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        # Construct a dict representation of a WordSettings model
        word_settings_model = {}
        word_settings_model['heading'] = word_heading_detection_model

        # Construct a dict representation of a XPathPatterns model
        x_path_patterns_model = {}
        x_path_patterns_model['xpaths'] = ['testString']

        # Construct a dict representation of a HtmlSettings model
        html_settings_model = {}
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        # Construct a dict representation of a SegmentSettings model
        segment_settings_model = {}
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        # Construct a dict representation of a NormalizationOperation model
        normalization_operation_model = {}
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        # Construct a dict representation of a Conversions model
        conversions_model = {}
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        # Construct a dict representation of a NluEnrichmentKeywords model
        nlu_enrichment_keywords_model = {}
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentEntities model
        nlu_enrichment_entities_model = {}
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentSentiment model
        nlu_enrichment_sentiment_model = {}
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentEmotion model
        nlu_enrichment_emotion_model = {}
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentSemanticRoles model
        nlu_enrichment_semantic_roles_model = {}
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentRelations model
        nlu_enrichment_relations_model = {}
        nlu_enrichment_relations_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentConcepts model
        nlu_enrichment_concepts_model = {}
        nlu_enrichment_concepts_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentFeatures model
        nlu_enrichment_features_model = {}
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        # Construct a dict representation of a Enrichment model
        enrichment_model = {}
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'testString'
        enrichment_model['source_field'] = 'testString'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'testString'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        # Construct a dict representation of a SourceSchedule model
        source_schedule_model = {}
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        # Construct a dict representation of a SourceOptionsFolder model
        source_options_folder_model = {}
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsObject model
        source_options_object_model = {}
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsSiteColl model
        source_options_site_coll_model = {}
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsWebCrawl model
        source_options_web_crawl_model = {}
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        # Construct a dict representation of a SourceOptionsBuckets model
        source_options_buckets_model = {}
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        # Construct a dict representation of a SourceOptions model
        source_options_model = {}
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        # Construct a dict representation of a Source model
        source_model = {}
        source_model['type'] = 'box'
        source_model['credential_id'] = 'testString'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        conversions = conversions_model
        enrichments = [enrichment_model]
        normalizations = [normalization_operation_model]
        source = source_model

        # Invoke method
        response = _service.create_configuration(
            environment_id,
            name,
            description=description,
            conversions=conversions,
            enrichments=enrichments,
            normalizations=normalizations,
            source=source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conversions'] == conversions_model
        assert req_body['enrichments'] == [enrichment_model]
        assert req_body['normalizations'] == [normalization_operation_model]
        assert req_body['source'] == source_model


    @responses.activate
    def test_create_configuration_value_error(self):
        """
        test_create_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a FontSetting model
        font_setting_model = {}
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        # Construct a dict representation of a PdfHeadingDetection model
        pdf_heading_detection_model = {}
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        # Construct a dict representation of a PdfSettings model
        pdf_settings_model = {}
        pdf_settings_model['heading'] = pdf_heading_detection_model

        # Construct a dict representation of a WordStyle model
        word_style_model = {}
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        # Construct a dict representation of a WordHeadingDetection model
        word_heading_detection_model = {}
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        # Construct a dict representation of a WordSettings model
        word_settings_model = {}
        word_settings_model['heading'] = word_heading_detection_model

        # Construct a dict representation of a XPathPatterns model
        x_path_patterns_model = {}
        x_path_patterns_model['xpaths'] = ['testString']

        # Construct a dict representation of a HtmlSettings model
        html_settings_model = {}
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        # Construct a dict representation of a SegmentSettings model
        segment_settings_model = {}
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        # Construct a dict representation of a NormalizationOperation model
        normalization_operation_model = {}
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        # Construct a dict representation of a Conversions model
        conversions_model = {}
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        # Construct a dict representation of a NluEnrichmentKeywords model
        nlu_enrichment_keywords_model = {}
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentEntities model
        nlu_enrichment_entities_model = {}
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentSentiment model
        nlu_enrichment_sentiment_model = {}
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentEmotion model
        nlu_enrichment_emotion_model = {}
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentSemanticRoles model
        nlu_enrichment_semantic_roles_model = {}
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentRelations model
        nlu_enrichment_relations_model = {}
        nlu_enrichment_relations_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentConcepts model
        nlu_enrichment_concepts_model = {}
        nlu_enrichment_concepts_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentFeatures model
        nlu_enrichment_features_model = {}
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        # Construct a dict representation of a Enrichment model
        enrichment_model = {}
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'testString'
        enrichment_model['source_field'] = 'testString'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'testString'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        # Construct a dict representation of a SourceSchedule model
        source_schedule_model = {}
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        # Construct a dict representation of a SourceOptionsFolder model
        source_options_folder_model = {}
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsObject model
        source_options_object_model = {}
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsSiteColl model
        source_options_site_coll_model = {}
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsWebCrawl model
        source_options_web_crawl_model = {}
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        # Construct a dict representation of a SourceOptionsBuckets model
        source_options_buckets_model = {}
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        # Construct a dict representation of a SourceOptions model
        source_options_model = {}
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        # Construct a dict representation of a Source model
        source_model = {}
        source_model['type'] = 'box'
        source_model['credential_id'] = 'testString'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        conversions = conversions_model
        enrichments = [enrichment_model]
        normalizations = [normalization_operation_model]
        source = source_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_configuration(**req_copy)



class TestListConfigurations():
    """
    Test Class for list_configurations
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_configurations_all_params(self):
        """
        list_configurations()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations')
        mock_response = '{"configurations": [{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.list_configurations(
            environment_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'name={}'.format(name) in query_string


    @responses.activate
    def test_list_configurations_required_params(self):
        """
        test_list_configurations_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations')
        mock_response = '{"configurations": [{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.list_configurations(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_configurations_value_error(self):
        """
        test_list_configurations_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations')
        mock_response = '{"configurations": [{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_configurations(**req_copy)



class TestGetConfiguration():
    """
    Test Class for get_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_configuration_all_params(self):
        """
        get_configuration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'

        # Invoke method
        response = _service.get_configuration(
            environment_id,
            configuration_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_configuration_value_error(self):
        """
        test_get_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "configuration_id": configuration_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_configuration(**req_copy)



class TestUpdateConfiguration():
    """
    Test Class for update_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_configuration_all_params(self):
        """
        update_configuration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FontSetting model
        font_setting_model = {}
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        # Construct a dict representation of a PdfHeadingDetection model
        pdf_heading_detection_model = {}
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        # Construct a dict representation of a PdfSettings model
        pdf_settings_model = {}
        pdf_settings_model['heading'] = pdf_heading_detection_model

        # Construct a dict representation of a WordStyle model
        word_style_model = {}
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        # Construct a dict representation of a WordHeadingDetection model
        word_heading_detection_model = {}
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        # Construct a dict representation of a WordSettings model
        word_settings_model = {}
        word_settings_model['heading'] = word_heading_detection_model

        # Construct a dict representation of a XPathPatterns model
        x_path_patterns_model = {}
        x_path_patterns_model['xpaths'] = ['testString']

        # Construct a dict representation of a HtmlSettings model
        html_settings_model = {}
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        # Construct a dict representation of a SegmentSettings model
        segment_settings_model = {}
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        # Construct a dict representation of a NormalizationOperation model
        normalization_operation_model = {}
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        # Construct a dict representation of a Conversions model
        conversions_model = {}
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        # Construct a dict representation of a NluEnrichmentKeywords model
        nlu_enrichment_keywords_model = {}
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentEntities model
        nlu_enrichment_entities_model = {}
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentSentiment model
        nlu_enrichment_sentiment_model = {}
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentEmotion model
        nlu_enrichment_emotion_model = {}
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentSemanticRoles model
        nlu_enrichment_semantic_roles_model = {}
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentRelations model
        nlu_enrichment_relations_model = {}
        nlu_enrichment_relations_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentConcepts model
        nlu_enrichment_concepts_model = {}
        nlu_enrichment_concepts_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentFeatures model
        nlu_enrichment_features_model = {}
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        # Construct a dict representation of a Enrichment model
        enrichment_model = {}
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'testString'
        enrichment_model['source_field'] = 'testString'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'testString'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        # Construct a dict representation of a SourceSchedule model
        source_schedule_model = {}
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        # Construct a dict representation of a SourceOptionsFolder model
        source_options_folder_model = {}
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsObject model
        source_options_object_model = {}
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsSiteColl model
        source_options_site_coll_model = {}
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsWebCrawl model
        source_options_web_crawl_model = {}
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        # Construct a dict representation of a SourceOptionsBuckets model
        source_options_buckets_model = {}
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        # Construct a dict representation of a SourceOptions model
        source_options_model = {}
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        # Construct a dict representation of a Source model
        source_model = {}
        source_model['type'] = 'box'
        source_model['credential_id'] = 'testString'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'
        name = 'testString'
        description = 'testString'
        conversions = conversions_model
        enrichments = [enrichment_model]
        normalizations = [normalization_operation_model]
        source = source_model

        # Invoke method
        response = _service.update_configuration(
            environment_id,
            configuration_id,
            name,
            description=description,
            conversions=conversions,
            enrichments=enrichments,
            normalizations=normalizations,
            source=source,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['conversions'] == conversions_model
        assert req_body['enrichments'] == [enrichment_model]
        assert req_body['normalizations'] == [normalization_operation_model]
        assert req_body['source'] == source_model


    @responses.activate
    def test_update_configuration_value_error(self):
        """
        test_update_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "name": "name", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "description": "description", "conversions": {"pdf": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}]}}, "word": {"heading": {"fonts": [{"level": 5, "min_size": 8, "max_size": 8, "bold": true, "italic": true, "name": "name"}], "styles": [{"level": 5, "names": ["names"]}]}}, "html": {"exclude_tags_completely": ["exclude_tags_completely"], "exclude_tags_keep_content": ["exclude_tags_keep_content"], "keep_content": {"xpaths": ["xpaths"]}, "exclude_content": {"xpaths": ["xpaths"]}, "keep_tag_attributes": ["keep_tag_attributes"], "exclude_tag_attributes": ["exclude_tag_attributes"]}, "segment": {"enabled": false, "selector_tags": ["selector_tags"], "annotated_fields": ["annotated_fields"]}, "json_normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "image_text_recognition": true}, "enrichments": [{"description": "description", "destination_field": "destination_field", "source_field": "source_field", "overwrite": false, "enrichment": "enrichment", "ignore_downstream_errors": false, "options": {"features": {"keywords": {"sentiment": false, "emotion": false, "limit": 5}, "entities": {"sentiment": false, "emotion": false, "limit": 5, "mentions": true, "mention_types": false, "sentence_locations": true, "model": "model"}, "sentiment": {"document": true, "targets": ["target"]}, "emotion": {"document": true, "targets": ["target"]}, "categories": {"mapKey": "anyValue"}, "semantic_roles": {"entities": true, "keywords": true, "limit": 5}, "relations": {"model": "model"}, "concepts": {"limit": 5}}, "language": "ar", "model": "model"}}], "normalizations": [{"operation": "copy", "source_field": "source_field", "destination_field": "destination_field"}], "source": {"type": "box", "credential_id": "credential_id", "schedule": {"enabled": true, "time_zone": "America/New_York", "frequency": "daily"}, "options": {"folders": [{"owner_user_id": "owner_user_id", "folder_id": "folder_id", "limit": 5}], "objects": [{"name": "name", "limit": 5}], "site_collections": [{"site_collection_path": "site_collection_path", "limit": 5}], "urls": [{"url": "url", "limit_to_starting_hosts": true, "crawl_speed": "normal", "allow_untrusted_certificate": false, "maximum_hops": 12, "request_timeout": 15, "override_robots_txt": false, "blacklist": ["blacklist"]}], "buckets": [{"name": "name", "limit": 5}], "crawl_all_buckets": false}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FontSetting model
        font_setting_model = {}
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        # Construct a dict representation of a PdfHeadingDetection model
        pdf_heading_detection_model = {}
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        # Construct a dict representation of a PdfSettings model
        pdf_settings_model = {}
        pdf_settings_model['heading'] = pdf_heading_detection_model

        # Construct a dict representation of a WordStyle model
        word_style_model = {}
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        # Construct a dict representation of a WordHeadingDetection model
        word_heading_detection_model = {}
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        # Construct a dict representation of a WordSettings model
        word_settings_model = {}
        word_settings_model['heading'] = word_heading_detection_model

        # Construct a dict representation of a XPathPatterns model
        x_path_patterns_model = {}
        x_path_patterns_model['xpaths'] = ['testString']

        # Construct a dict representation of a HtmlSettings model
        html_settings_model = {}
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        # Construct a dict representation of a SegmentSettings model
        segment_settings_model = {}
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        # Construct a dict representation of a NormalizationOperation model
        normalization_operation_model = {}
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        # Construct a dict representation of a Conversions model
        conversions_model = {}
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        # Construct a dict representation of a NluEnrichmentKeywords model
        nlu_enrichment_keywords_model = {}
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentEntities model
        nlu_enrichment_entities_model = {}
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentSentiment model
        nlu_enrichment_sentiment_model = {}
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentEmotion model
        nlu_enrichment_emotion_model = {}
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        # Construct a dict representation of a NluEnrichmentSemanticRoles model
        nlu_enrichment_semantic_roles_model = {}
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentRelations model
        nlu_enrichment_relations_model = {}
        nlu_enrichment_relations_model['model'] = 'testString'

        # Construct a dict representation of a NluEnrichmentConcepts model
        nlu_enrichment_concepts_model = {}
        nlu_enrichment_concepts_model['limit'] = 38

        # Construct a dict representation of a NluEnrichmentFeatures model
        nlu_enrichment_features_model = {}
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        # Construct a dict representation of a EnrichmentOptions model
        enrichment_options_model = {}
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        # Construct a dict representation of a Enrichment model
        enrichment_model = {}
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'testString'
        enrichment_model['source_field'] = 'testString'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'testString'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        # Construct a dict representation of a SourceSchedule model
        source_schedule_model = {}
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        # Construct a dict representation of a SourceOptionsFolder model
        source_options_folder_model = {}
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsObject model
        source_options_object_model = {}
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsSiteColl model
        source_options_site_coll_model = {}
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        # Construct a dict representation of a SourceOptionsWebCrawl model
        source_options_web_crawl_model = {}
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        # Construct a dict representation of a SourceOptionsBuckets model
        source_options_buckets_model = {}
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        # Construct a dict representation of a SourceOptions model
        source_options_model = {}
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        # Construct a dict representation of a Source model
        source_model = {}
        source_model['type'] = 'box'
        source_model['credential_id'] = 'testString'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'
        name = 'testString'
        description = 'testString'
        conversions = conversions_model
        enrichments = [enrichment_model]
        normalizations = [normalization_operation_model]
        source = source_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "configuration_id": configuration_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_configuration(**req_copy)



class TestDeleteConfiguration():
    """
    Test Class for delete_configuration
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_configuration_all_params(self):
        """
        delete_configuration()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "status": "deleted", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'

        # Invoke method
        response = _service.delete_configuration(
            environment_id,
            configuration_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_configuration_value_error(self):
        """
        test_delete_configuration_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/configurations/testString')
        mock_response = '{"configuration_id": "configuration_id", "status": "deleted", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        configuration_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "configuration_id": configuration_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_configuration(**req_copy)



# endregion
##############################################################################
# End of Service: Configurations
##############################################################################

##############################################################################
# Start of Service: Collections
##############################################################################
# region

class TestCreateCollection():
    """
    Test Class for create_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_collection_all_params(self):
        """
        create_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        configuration_id = 'testString'
        language = 'en'

        # Invoke method
        response = _service.create_collection(
            environment_id,
            name,
            description=description,
            configuration_id=configuration_id,
            language=language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['configuration_id'] == 'testString'
        assert req_body['language'] == 'en'


    @responses.activate
    def test_create_collection_value_error(self):
        """
        test_create_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'
        description = 'testString'
        configuration_id = 'testString'
        language = 'en'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_collection(**req_copy)



class TestListCollections():
    """
    Test Class for list_collections
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_collections_all_params(self):
        """
        list_collections()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.list_collections(
            environment_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'name={}'.format(name) in query_string


    @responses.activate
    def test_list_collections_required_params(self):
        """
        test_list_collections_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.list_collections(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_collections_value_error(self):
        """
        test_list_collections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_collections(**req_copy)



class TestGetCollection():
    """
    Test Class for get_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_collection_all_params(self):
        """
        get_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_collection(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_collection_value_error(self):
        """
        test_get_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_collection(**req_copy)



class TestUpdateCollection():
    """
    Test Class for update_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_collection_all_params(self):
        """
        update_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        configuration_id = 'testString'

        # Invoke method
        response = _service.update_collection(
            environment_id,
            collection_id,
            name,
            description=description,
            configuration_id=configuration_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['configuration_id'] == 'testString'


    @responses.activate
    def test_update_collection_value_error(self):
        """
        test_update_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "status": "active", "configuration_id": "configuration_id", "language": "language", "document_counts": {"available": 9, "processing": 10, "failed": 6, "pending": 7}, "disk_usage": {"used_bytes": 10}, "training_status": {"total_examples": 14, "available": false, "processing": true, "minimum_queries_added": false, "minimum_examples_added": true, "sufficient_label_diversity": true, "notices": 7, "successfully_trained": "2019-01-01T12:00:00.000Z", "data_updated": "2019-01-01T12:00:00.000Z"}, "crawl_status": {"source_crawl": {"status": "running", "next_crawl": "2019-01-01T12:00:00.000Z"}}, "smart_document_understanding": {"enabled": true, "total_annotated_pages": 21, "total_pages": 11, "total_documents": 15, "custom_fields": {"defined": 7, "maximum_allowed": 15}}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        configuration_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_collection(**req_copy)



class TestDeleteCollection():
    """
    Test Class for delete_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_collection_all_params(self):
        """
        delete_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_collection(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_collection_value_error(self):
        """
        test_delete_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString')
        mock_response = '{"collection_id": "collection_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_collection(**req_copy)



class TestListCollectionFields():
    """
    Test Class for list_collection_fields
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_collection_fields_all_params(self):
        """
        list_collection_fields()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.list_collection_fields(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_collection_fields_value_error(self):
        """
        test_list_collection_fields_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/fields')
        mock_response = '{"fields": [{"field": "field", "type": "nested"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_collection_fields(**req_copy)



# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: QueryModifications
##############################################################################
# region

class TestListExpansions():
    """
    Test Class for list_expansions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_expansions_all_params(self):
        """
        list_expansions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.list_expansions(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_expansions_value_error(self):
        """
        test_list_expansions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_expansions(**req_copy)



class TestCreateExpansions():
    """
    Test Class for create_expansions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_expansions_all_params(self):
        """
        create_expansions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Expansion model
        expansion_model = {}
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        expansions = [expansion_model]

        # Invoke method
        response = _service.create_expansions(
            environment_id,
            collection_id,
            expansions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['expansions'] == [expansion_model]


    @responses.activate
    def test_create_expansions_value_error(self):
        """
        test_create_expansions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        mock_response = '{"expansions": [{"input_terms": ["input_terms"], "expanded_terms": ["expanded_terms"]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Expansion model
        expansion_model = {}
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        expansions = [expansion_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "expansions": expansions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_expansions(**req_copy)



class TestDeleteExpansions():
    """
    Test Class for delete_expansions
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_expansions_all_params(self):
        """
        delete_expansions()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_expansions(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_expansions_value_error(self):
        """
        test_delete_expansions_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/expansions')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_expansions(**req_copy)



class TestGetTokenizationDictionaryStatus():
    """
    Test Class for get_tokenization_dictionary_status
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_tokenization_dictionary_status_all_params(self):
        """
        get_tokenization_dictionary_status()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_tokenization_dictionary_status(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_tokenization_dictionary_status_value_error(self):
        """
        test_get_tokenization_dictionary_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_tokenization_dictionary_status(**req_copy)



class TestCreateTokenizationDictionary():
    """
    Test Class for create_tokenization_dictionary
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_tokenization_dictionary_all_params(self):
        """
        create_tokenization_dictionary()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a TokenDictRule model
        token_dict_rule_model = {}
        token_dict_rule_model['text'] = 'testString'
        token_dict_rule_model['tokens'] = ['testString']
        token_dict_rule_model['readings'] = ['testString']
        token_dict_rule_model['part_of_speech'] = 'testString'

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        tokenization_rules = [token_dict_rule_model]

        # Invoke method
        response = _service.create_tokenization_dictionary(
            environment_id,
            collection_id,
            tokenization_rules=tokenization_rules,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['tokenization_rules'] == [token_dict_rule_model]


    @responses.activate
    def test_create_tokenization_dictionary_required_params(self):
        """
        test_create_tokenization_dictionary_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.create_tokenization_dictionary(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_create_tokenization_dictionary_value_error(self):
        """
        test_create_tokenization_dictionary_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_tokenization_dictionary(**req_copy)



class TestDeleteTokenizationDictionary():
    """
    Test Class for delete_tokenization_dictionary
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_tokenization_dictionary_all_params(self):
        """
        delete_tokenization_dictionary()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_tokenization_dictionary(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_tokenization_dictionary_value_error(self):
        """
        test_delete_tokenization_dictionary_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/tokenization_dictionary')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_tokenization_dictionary(**req_copy)



class TestGetStopwordListStatus():
    """
    Test Class for get_stopword_list_status
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_stopword_list_status_all_params(self):
        """
        get_stopword_list_status()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.get_stopword_list_status(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_stopword_list_status_value_error(self):
        """
        test_get_stopword_list_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_stopword_list_status(**req_copy)



class TestCreateStopwordList():
    """
    Test Class for create_stopword_list
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_stopword_list_all_params(self):
        """
        create_stopword_list()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        stopword_file = io.BytesIO(b'This is a mock file.').getvalue()
        stopword_filename = 'testString'

        # Invoke method
        response = _service.create_stopword_list(
            environment_id,
            collection_id,
            stopword_file,
            stopword_filename=stopword_filename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_stopword_list_required_params(self):
        """
        test_create_stopword_list_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        stopword_file = io.BytesIO(b'This is a mock file.').getvalue()
        stopword_filename = 'testString'

        # Invoke method
        response = _service.create_stopword_list(
            environment_id,
            collection_id,
            stopword_file,
            stopword_filename=stopword_filename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_stopword_list_value_error(self):
        """
        test_create_stopword_list_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        mock_response = '{"status": "active", "type": "type"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        stopword_file = io.BytesIO(b'This is a mock file.').getvalue()
        stopword_filename = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "stopword_file": stopword_file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_stopword_list(**req_copy)



class TestDeleteStopwordList():
    """
    Test Class for delete_stopword_list
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_stopword_list_all_params(self):
        """
        delete_stopword_list()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_stopword_list(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_stopword_list_value_error(self):
        """
        test_delete_stopword_list_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/word_lists/stopwords')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_stopword_list(**req_copy)



# endregion
##############################################################################
# End of Service: QueryModifications
##############################################################################

##############################################################################
# Start of Service: Documents
##############################################################################
# region

class TestAddDocument():
    """
    Test Class for add_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_document_all_params(self):
        """
        add_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'

        # Invoke method
        response = _service.add_document(
            environment_id,
            collection_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_add_document_required_params(self):
        """
        test_add_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.add_document(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_add_document_value_error(self):
        """
        test_add_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_document(**req_copy)



class TestGetDocumentStatus():
    """
    Test Class for get_document_status
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_document_status_all_params(self):
        """
        get_document_status()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "configuration_id": "configuration_id", "status": "available", "status_description": "status_description", "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.get_document_status(
            environment_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_document_status_value_error(self):
        """
        test_get_document_status_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "configuration_id": "configuration_id", "status": "available", "status_description": "status_description", "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_document_status(**req_copy)



class TestUpdateDocument():
    """
    Test Class for update_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_document_all_params(self):
        """
        update_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/json'
        metadata = 'testString'

        # Invoke method
        response = _service.update_document(
            environment_id,
            collection_id,
            document_id,
            file=file,
            filename=filename,
            file_content_type=file_content_type,
            metadata=metadata,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_update_document_required_params(self):
        """
        test_update_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.update_document(
            environment_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_update_document_value_error(self):
        """
        test_update_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "processing", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_document(**req_copy)



class TestDeleteDocument():
    """
    Test Class for delete_document
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_document_all_params(self):
        """
        delete_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.delete_document(
            environment_id,
            collection_id,
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_document_value_error(self):
        """
        test_delete_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/documents/testString')
        mock_response = '{"document_id": "document_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document(**req_copy)



# endregion
##############################################################################
# End of Service: Documents
##############################################################################

##############################################################################
# Start of Service: Queries
##############################################################################
# region

class TestQuery():
    """
    Test Class for query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_all_params(self):
        """
        query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        passages = True
        aggregation = 'testString'
        count = 38
        return_ = 'testString'
        offset = 38
        sort = 'testString'
        highlight = False
        passages_fields = 'testString'
        passages_count = 100
        passages_characters = 50
        deduplicate = False
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = 'testString'
        similar_fields = 'testString'
        bias = 'testString'
        spelling_suggestions = False
        x_watson_logging_opt_out = False

        # Invoke method
        response = _service.query(
            environment_id,
            collection_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            passages=passages,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            passages_fields=passages_fields,
            passages_count=passages_count,
            passages_characters=passages_characters,
            deduplicate=deduplicate,
            deduplicate_field=deduplicate_field,
            similar=similar,
            similar_document_ids=similar_document_ids,
            similar_fields=similar_fields,
            bias=bias,
            spelling_suggestions=spelling_suggestions,
            x_watson_logging_opt_out=x_watson_logging_opt_out,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['filter'] == 'testString'
        assert req_body['query'] == 'testString'
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['passages'] == True
        assert req_body['aggregation'] == 'testString'
        assert req_body['count'] == 38
        assert req_body['return'] == 'testString'
        assert req_body['offset'] == 38
        assert req_body['sort'] == 'testString'
        assert req_body['highlight'] == False
        assert req_body['passages.fields'] == 'testString'
        assert req_body['passages.count'] == 100
        assert req_body['passages.characters'] == 50
        assert req_body['deduplicate'] == False
        assert req_body['deduplicate.field'] == 'testString'
        assert req_body['similar'] == False
        assert req_body['similar.document_ids'] == 'testString'
        assert req_body['similar.fields'] == 'testString'
        assert req_body['bias'] == 'testString'
        assert req_body['spelling_suggestions'] == False


    @responses.activate
    def test_query_required_params(self):
        """
        test_query_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.query(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_value_error(self):
        """
        test_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query(**req_copy)



class TestQueryNotices():
    """
    Test Class for query_notices
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_notices_all_params(self):
        """
        query_notices()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        passages = True
        aggregation = 'testString'
        count = 38
        return_ = ['testString']
        offset = 38
        sort = ['testString']
        highlight = False
        passages_fields = ['testString']
        passages_count = 100
        passages_characters = 50
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = ['testString']
        similar_fields = ['testString']

        # Invoke method
        response = _service.query_notices(
            environment_id,
            collection_id,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            passages=passages,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            passages_fields=passages_fields,
            passages_count=passages_count,
            passages_characters=passages_characters,
            deduplicate_field=deduplicate_field,
            similar=similar,
            similar_document_ids=similar_document_ids,
            similar_fields=similar_fields,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'passages={}'.format('true' if passages else 'false') in query_string
        assert 'aggregation={}'.format(aggregation) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'return={}'.format(','.join(return_)) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        assert 'highlight={}'.format('true' if highlight else 'false') in query_string
        assert 'passages.fields={}'.format(','.join(passages_fields)) in query_string
        assert 'passages.count={}'.format(passages_count) in query_string
        assert 'passages.characters={}'.format(passages_characters) in query_string
        assert 'deduplicate.field={}'.format(deduplicate_field) in query_string
        assert 'similar={}'.format('true' if similar else 'false') in query_string
        assert 'similar.document_ids={}'.format(','.join(similar_document_ids)) in query_string
        assert 'similar.fields={}'.format(','.join(similar_fields)) in query_string


    @responses.activate
    def test_query_notices_required_params(self):
        """
        test_query_notices_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.query_notices(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_notices_value_error(self):
        """
        test_query_notices_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_notices(**req_copy)



class TestFederatedQuery():
    """
    Test Class for federated_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_federated_query_all_params(self):
        """
        federated_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        passages = True
        aggregation = 'testString'
        count = 38
        return_ = 'testString'
        offset = 38
        sort = 'testString'
        highlight = False
        passages_fields = 'testString'
        passages_count = 100
        passages_characters = 50
        deduplicate = False
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = 'testString'
        similar_fields = 'testString'
        bias = 'testString'
        x_watson_logging_opt_out = False

        # Invoke method
        response = _service.federated_query(
            environment_id,
            collection_ids,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            passages=passages,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            passages_fields=passages_fields,
            passages_count=passages_count,
            passages_characters=passages_characters,
            deduplicate=deduplicate,
            deduplicate_field=deduplicate_field,
            similar=similar,
            similar_document_ids=similar_document_ids,
            similar_fields=similar_fields,
            bias=bias,
            x_watson_logging_opt_out=x_watson_logging_opt_out,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['collection_ids'] == 'testString'
        assert req_body['filter'] == 'testString'
        assert req_body['query'] == 'testString'
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['passages'] == True
        assert req_body['aggregation'] == 'testString'
        assert req_body['count'] == 38
        assert req_body['return'] == 'testString'
        assert req_body['offset'] == 38
        assert req_body['sort'] == 'testString'
        assert req_body['highlight'] == False
        assert req_body['passages.fields'] == 'testString'
        assert req_body['passages.count'] == 100
        assert req_body['passages.characters'] == 50
        assert req_body['deduplicate'] == False
        assert req_body['deduplicate.field'] == 'testString'
        assert req_body['similar'] == False
        assert req_body['similar.document_ids'] == 'testString'
        assert req_body['similar.fields'] == 'testString'
        assert req_body['bias'] == 'testString'


    @responses.activate
    def test_federated_query_required_params(self):
        """
        test_federated_query_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        passages = True
        aggregation = 'testString'
        count = 38
        return_ = 'testString'
        offset = 38
        sort = 'testString'
        highlight = False
        passages_fields = 'testString'
        passages_count = 100
        passages_characters = 50
        deduplicate = False
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = 'testString'
        similar_fields = 'testString'
        bias = 'testString'

        # Invoke method
        response = _service.federated_query(
            environment_id,
            collection_ids,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            passages=passages,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            passages_fields=passages_fields,
            passages_count=passages_count,
            passages_characters=passages_characters,
            deduplicate=deduplicate,
            deduplicate_field=deduplicate_field,
            similar=similar,
            similar_document_ids=similar_document_ids,
            similar_fields=similar_fields,
            bias=bias,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['collection_ids'] == 'testString'
        assert req_body['filter'] == 'testString'
        assert req_body['query'] == 'testString'
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['passages'] == True
        assert req_body['aggregation'] == 'testString'
        assert req_body['count'] == 38
        assert req_body['return'] == 'testString'
        assert req_body['offset'] == 38
        assert req_body['sort'] == 'testString'
        assert req_body['highlight'] == False
        assert req_body['passages.fields'] == 'testString'
        assert req_body['passages.count'] == 100
        assert req_body['passages.characters'] == 50
        assert req_body['deduplicate'] == False
        assert req_body['deduplicate.field'] == 'testString'
        assert req_body['similar'] == False
        assert req_body['similar.document_ids'] == 'testString'
        assert req_body['similar.fields'] == 'testString'
        assert req_body['bias'] == 'testString'


    @responses.activate
    def test_federated_query_value_error(self):
        """
        test_federated_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/query')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18, "session_token": "session_token", "retrieval_details": {"document_retrieval_strategy": "untrained"}, "suggested_query": "suggested_query"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = 'testString'
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        passages = True
        aggregation = 'testString'
        count = 38
        return_ = 'testString'
        offset = 38
        sort = 'testString'
        highlight = False
        passages_fields = 'testString'
        passages_count = 100
        passages_characters = 50
        deduplicate = False
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = 'testString'
        similar_fields = 'testString'
        bias = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_ids": collection_ids,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.federated_query(**req_copy)



class TestFederatedQueryNotices():
    """
    Test Class for federated_query_notices
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_federated_query_notices_all_params(self):
        """
        federated_query_notices()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = ['testString']
        filter = 'testString'
        query = 'testString'
        natural_language_query = 'testString'
        aggregation = 'testString'
        count = 38
        return_ = ['testString']
        offset = 38
        sort = ['testString']
        highlight = False
        deduplicate_field = 'testString'
        similar = False
        similar_document_ids = ['testString']
        similar_fields = ['testString']

        # Invoke method
        response = _service.federated_query_notices(
            environment_id,
            collection_ids,
            filter=filter,
            query=query,
            natural_language_query=natural_language_query,
            aggregation=aggregation,
            count=count,
            return_=return_,
            offset=offset,
            sort=sort,
            highlight=highlight,
            deduplicate_field=deduplicate_field,
            similar=similar,
            similar_document_ids=similar_document_ids,
            similar_fields=similar_fields,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'natural_language_query={}'.format(natural_language_query) in query_string
        assert 'aggregation={}'.format(aggregation) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'return={}'.format(','.join(return_)) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string
        assert 'highlight={}'.format('true' if highlight else 'false') in query_string
        assert 'deduplicate.field={}'.format(deduplicate_field) in query_string
        assert 'similar={}'.format('true' if similar else 'false') in query_string
        assert 'similar.document_ids={}'.format(','.join(similar_document_ids)) in query_string
        assert 'similar.fields={}'.format(','.join(similar_fields)) in query_string


    @responses.activate
    def test_federated_query_notices_required_params(self):
        """
        test_federated_query_notices_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = ['testString']

        # Invoke method
        response = _service.federated_query_notices(
            environment_id,
            collection_ids,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'collection_ids={}'.format(','.join(collection_ids)) in query_string


    @responses.activate
    def test_federated_query_notices_value_error(self):
        """
        test_federated_query_notices_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/notices')
        mock_response = '{"matching_results": 16, "results": [{"id": "id", "metadata": {"mapKey": "anyValue"}, "collection_id": "collection_id", "result_metadata": {"score": 5, "confidence": 10}, "code": 4, "filename": "filename", "file_type": "pdf", "sha1": "sha1", "notices": [{"notice_id": "notice_id", "created": "2019-01-01T12:00:00.000Z", "document_id": "document_id", "query_id": "query_id", "severity": "warning", "step": "step", "description": "description"}]}], "aggregations": [{"type": "histogram", "matching_results": 16, "field": "field", "interval": 8}], "passages": [{"document_id": "document_id", "passage_score": 13, "passage_text": "passage_text", "start_offset": 12, "end_offset": 10, "field": "field"}], "duplicates_removed": 18}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_ids = ['testString']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_ids": collection_ids,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.federated_query_notices(**req_copy)



class TestGetAutocompletion():
    """
    Test Class for get_autocompletion
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_autocompletion_all_params(self):
        """
        get_autocompletion()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        prefix = 'testString'
        field = 'testString'
        count = 38

        # Invoke method
        response = _service.get_autocompletion(
            environment_id,
            collection_id,
            prefix,
            field=field,
            count=count,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string
        assert 'field={}'.format(field) in query_string
        assert 'count={}'.format(count) in query_string


    @responses.activate
    def test_get_autocompletion_required_params(self):
        """
        test_get_autocompletion_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        prefix = 'testString'

        # Invoke method
        response = _service.get_autocompletion(
            environment_id,
            collection_id,
            prefix,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'prefix={}'.format(prefix) in query_string


    @responses.activate
    def test_get_autocompletion_value_error(self):
        """
        test_get_autocompletion_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/autocompletion')
        mock_response = '{"completions": ["completions"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        prefix = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "prefix": prefix,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_autocompletion(**req_copy)



# endregion
##############################################################################
# End of Service: Queries
##############################################################################

##############################################################################
# Start of Service: TrainingData
##############################################################################
# region

class TestListTrainingData():
    """
    Test Class for list_training_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_training_data_all_params(self):
        """
        list_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        mock_response = '{"environment_id": "environment_id", "collection_id": "collection_id", "queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.list_training_data(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_training_data_value_error(self):
        """
        test_list_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        mock_response = '{"environment_id": "environment_id", "collection_id": "collection_id", "queries": [{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_training_data(**req_copy)



class TestAddTrainingData():
    """
    Test Class for add_training_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_add_training_data_all_params(self):
        """
        add_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['cross_reference'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        natural_language_query = 'testString'
        filter = 'testString'
        examples = [training_example_model]

        # Invoke method
        response = _service.add_training_data(
            environment_id,
            collection_id,
            natural_language_query=natural_language_query,
            filter=filter,
            examples=examples,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['natural_language_query'] == 'testString'
        assert req_body['filter'] == 'testString'
        assert req_body['examples'] == [training_example_model]


    @responses.activate
    def test_add_training_data_value_error(self):
        """
        test_add_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a TrainingExample model
        training_example_model = {}
        training_example_model['document_id'] = 'testString'
        training_example_model['cross_reference'] = 'testString'
        training_example_model['relevance'] = 38

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        natural_language_query = 'testString'
        filter = 'testString'
        examples = [training_example_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_training_data(**req_copy)



class TestDeleteAllTrainingData():
    """
    Test Class for delete_all_training_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_all_training_data_all_params(self):
        """
        delete_all_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_all_training_data(
            environment_id,
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_all_training_data_value_error(self):
        """
        test_delete_all_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_all_training_data(**req_copy)



class TestGetTrainingData():
    """
    Test Class for get_training_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_training_data_all_params(self):
        """
        get_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.get_training_data(
            environment_id,
            collection_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_training_data_value_error(self):
        """
        test_get_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString')
        mock_response = '{"query_id": "query_id", "natural_language_query": "natural_language_query", "filter": "filter", "examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_training_data(**req_copy)



class TestDeleteTrainingData():
    """
    Test Class for delete_training_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_training_data_all_params(self):
        """
        delete_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.delete_training_data(
            environment_id,
            collection_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_training_data_value_error(self):
        """
        test_delete_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_data(**req_copy)



class TestListTrainingExamples():
    """
    Test Class for list_training_examples
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_training_examples_all_params(self):
        """
        list_training_examples()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples')
        mock_response = '{"examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Invoke method
        response = _service.list_training_examples(
            environment_id,
            collection_id,
            query_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_training_examples_value_error(self):
        """
        test_list_training_examples_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples')
        mock_response = '{"examples": [{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_training_examples(**req_copy)



class TestCreateTrainingExample():
    """
    Test Class for create_training_example
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_training_example_all_params(self):
        """
        create_training_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        document_id = 'testString'
        cross_reference = 'testString'
        relevance = 38

        # Invoke method
        response = _service.create_training_example(
            environment_id,
            collection_id,
            query_id,
            document_id=document_id,
            cross_reference=cross_reference,
            relevance=relevance,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['document_id'] == 'testString'
        assert req_body['cross_reference'] == 'testString'
        assert req_body['relevance'] == 38


    @responses.activate
    def test_create_training_example_value_error(self):
        """
        test_create_training_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        document_id = 'testString'
        cross_reference = 'testString'
        relevance = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_training_example(**req_copy)



class TestDeleteTrainingExample():
    """
    Test Class for delete_training_example
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_training_example_all_params(self):
        """
        delete_training_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'

        # Invoke method
        response = _service.delete_training_example(
            environment_id,
            collection_id,
            query_id,
            example_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_training_example_value_error(self):
        """
        test_delete_training_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
            "example_id": example_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_training_example(**req_copy)



class TestUpdateTrainingExample():
    """
    Test Class for update_training_example
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_training_example_all_params(self):
        """
        update_training_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'
        cross_reference = 'testString'
        relevance = 38

        # Invoke method
        response = _service.update_training_example(
            environment_id,
            collection_id,
            query_id,
            example_id,
            cross_reference=cross_reference,
            relevance=relevance,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['cross_reference'] == 'testString'
        assert req_body['relevance'] == 38


    @responses.activate
    def test_update_training_example_value_error(self):
        """
        test_update_training_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'
        cross_reference = 'testString'
        relevance = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
            "example_id": example_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_training_example(**req_copy)



class TestGetTrainingExample():
    """
    Test Class for get_training_example
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_training_example_all_params(self):
        """
        get_training_example()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'

        # Invoke method
        response = _service.get_training_example(
            environment_id,
            collection_id,
            query_id,
            example_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_training_example_value_error(self):
        """
        test_get_training_example_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/collections/testString/training_data/testString/examples/testString')
        mock_response = '{"document_id": "document_id", "cross_reference": "cross_reference", "relevance": 9}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        collection_id = 'testString'
        query_id = 'testString'
        example_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "collection_id": collection_id,
            "query_id": query_id,
            "example_id": example_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_training_example(**req_copy)



# endregion
##############################################################################
# End of Service: TrainingData
##############################################################################

##############################################################################
# Start of Service: UserData
##############################################################################
# region

class TestDeleteUserData():
    """
    Test Class for delete_user_data
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_user_data_all_params(self):
        """
        delete_user_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'customer_id={}'.format(customer_id) in query_string


    @responses.activate
    def test_delete_user_data_value_error(self):
        """
        test_delete_user_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customer_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customer_id": customer_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_user_data(**req_copy)



# endregion
##############################################################################
# End of Service: UserData
##############################################################################

##############################################################################
# Start of Service: EventsAndFeedback
##############################################################################
# region

class TestCreateEvent():
    """
    Test Class for create_event
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_event_all_params(self):
        """
        create_event()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/events')
        mock_response = '{"type": "click", "data": {"environment_id": "environment_id", "session_token": "session_token", "client_timestamp": "2019-01-01T12:00:00.000Z", "display_rank": 12, "collection_id": "collection_id", "document_id": "document_id", "query_id": "query_id"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EventData model
        event_data_model = {}
        event_data_model['environment_id'] = 'testString'
        event_data_model['session_token'] = 'testString'
        event_data_model['client_timestamp'] = "2019-01-01T12:00:00Z"
        event_data_model['display_rank'] = 38
        event_data_model['collection_id'] = 'testString'
        event_data_model['document_id'] = 'testString'

        # Set up parameter values
        type = 'click'
        data = event_data_model

        # Invoke method
        response = _service.create_event(
            type,
            data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['type'] == 'click'
        assert req_body['data'] == event_data_model


    @responses.activate
    def test_create_event_value_error(self):
        """
        test_create_event_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/events')
        mock_response = '{"type": "click", "data": {"environment_id": "environment_id", "session_token": "session_token", "client_timestamp": "2019-01-01T12:00:00.000Z", "display_rank": 12, "collection_id": "collection_id", "document_id": "document_id", "query_id": "query_id"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a EventData model
        event_data_model = {}
        event_data_model['environment_id'] = 'testString'
        event_data_model['session_token'] = 'testString'
        event_data_model['client_timestamp'] = "2019-01-01T12:00:00Z"
        event_data_model['display_rank'] = 38
        event_data_model['collection_id'] = 'testString'
        event_data_model['document_id'] = 'testString'

        # Set up parameter values
        type = 'click'
        data = event_data_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "type": type,
            "data": data,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_event(**req_copy)



class TestQueryLog():
    """
    Test Class for query_log
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_query_log_all_params(self):
        """
        query_log()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"matching_results": 16, "results": [{"environment_id": "environment_id", "customer_id": "customer_id", "document_type": "query", "natural_language_query": "natural_language_query", "document_results": {"results": [{"position": 8, "document_id": "document_id", "score": 5, "confidence": 10, "collection_id": "collection_id"}], "count": 5}, "created_timestamp": "2019-01-01T12:00:00.000Z", "client_timestamp": "2019-01-01T12:00:00.000Z", "query_id": "query_id", "session_token": "session_token", "collection_id": "collection_id", "display_rank": 12, "document_id": "document_id", "event_type": "click", "result_type": "document"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        filter = 'testString'
        query = 'testString'
        count = 38
        offset = 38
        sort = ['testString']

        # Invoke method
        response = _service.query_log(
            filter=filter,
            query=query,
            count=count,
            offset=offset,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'filter={}'.format(filter) in query_string
        assert 'query={}'.format(query) in query_string
        assert 'count={}'.format(count) in query_string
        assert 'offset={}'.format(offset) in query_string
        assert 'sort={}'.format(','.join(sort)) in query_string


    @responses.activate
    def test_query_log_required_params(self):
        """
        test_query_log_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"matching_results": 16, "results": [{"environment_id": "environment_id", "customer_id": "customer_id", "document_type": "query", "natural_language_query": "natural_language_query", "document_results": {"results": [{"position": 8, "document_id": "document_id", "score": 5, "confidence": 10, "collection_id": "collection_id"}], "count": 5}, "created_timestamp": "2019-01-01T12:00:00.000Z", "client_timestamp": "2019-01-01T12:00:00.000Z", "query_id": "query_id", "session_token": "session_token", "collection_id": "collection_id", "display_rank": 12, "document_id": "document_id", "event_type": "click", "result_type": "document"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.query_log()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_query_log_value_error(self):
        """
        test_query_log_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/logs')
        mock_response = '{"matching_results": 16, "results": [{"environment_id": "environment_id", "customer_id": "customer_id", "document_type": "query", "natural_language_query": "natural_language_query", "document_results": {"results": [{"position": 8, "document_id": "document_id", "score": 5, "confidence": 10, "collection_id": "collection_id"}], "count": 5}, "created_timestamp": "2019-01-01T12:00:00.000Z", "client_timestamp": "2019-01-01T12:00:00.000Z", "query_id": "query_id", "session_token": "session_token", "collection_id": "collection_id", "display_rank": 12, "document_id": "document_id", "event_type": "click", "result_type": "document"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.query_log(**req_copy)



class TestGetMetricsQuery():
    """
    Test Class for get_metrics_query
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_metrics_query_all_params(self):
        """
        get_metrics_query()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        end_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        result_type = 'document'

        # Invoke method
        response = _service.get_metrics_query(
            start_time=start_time,
            end_time=end_time,
            result_type=result_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'result_type={}'.format(result_type) in query_string


    @responses.activate
    def test_get_metrics_query_required_params(self):
        """
        test_get_metrics_query_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_metrics_query()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_metrics_query_value_error(self):
        """
        test_get_metrics_query_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics_query(**req_copy)



class TestGetMetricsQueryEvent():
    """
    Test Class for get_metrics_query_event
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_metrics_query_event_all_params(self):
        """
        get_metrics_query_event()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_event')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        end_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        result_type = 'document'

        # Invoke method
        response = _service.get_metrics_query_event(
            start_time=start_time,
            end_time=end_time,
            result_type=result_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'result_type={}'.format(result_type) in query_string


    @responses.activate
    def test_get_metrics_query_event_required_params(self):
        """
        test_get_metrics_query_event_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_event')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_metrics_query_event()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_metrics_query_event_value_error(self):
        """
        test_get_metrics_query_event_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_event')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics_query_event(**req_copy)



class TestGetMetricsQueryNoResults():
    """
    Test Class for get_metrics_query_no_results
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_metrics_query_no_results_all_params(self):
        """
        get_metrics_query_no_results()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_no_search_results')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        end_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        result_type = 'document'

        # Invoke method
        response = _service.get_metrics_query_no_results(
            start_time=start_time,
            end_time=end_time,
            result_type=result_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'result_type={}'.format(result_type) in query_string


    @responses.activate
    def test_get_metrics_query_no_results_required_params(self):
        """
        test_get_metrics_query_no_results_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_no_search_results')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_metrics_query_no_results()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_metrics_query_no_results_value_error(self):
        """
        test_get_metrics_query_no_results_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/number_of_queries_with_no_search_results')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics_query_no_results(**req_copy)



class TestGetMetricsEventRate():
    """
    Test Class for get_metrics_event_rate
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_metrics_event_rate_all_params(self):
        """
        get_metrics_event_rate()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/event_rate')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        end_time = string_to_datetime('2019-01-01T12:00:00.000Z')
        result_type = 'document'

        # Invoke method
        response = _service.get_metrics_event_rate(
            start_time=start_time,
            end_time=end_time,
            result_type=result_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'result_type={}'.format(result_type) in query_string


    @responses.activate
    def test_get_metrics_event_rate_required_params(self):
        """
        test_get_metrics_event_rate_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/event_rate')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_metrics_event_rate()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_metrics_event_rate_value_error(self):
        """
        test_get_metrics_event_rate_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/event_rate')
        mock_response = '{"aggregations": [{"interval": "interval", "event_type": "event_type", "results": [{"key_as_string": "2019-01-01T12:00:00.000Z", "key": 3, "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics_event_rate(**req_copy)



class TestGetMetricsQueryTokenEvent():
    """
    Test Class for get_metrics_query_token_event
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_metrics_query_token_event_all_params(self):
        """
        get_metrics_query_token_event()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/top_query_tokens_with_event_rate')
        mock_response = '{"aggregations": [{"event_type": "event_type", "results": [{"key": "key", "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        count = 38

        # Invoke method
        response = _service.get_metrics_query_token_event(
            count=count,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'count={}'.format(count) in query_string


    @responses.activate
    def test_get_metrics_query_token_event_required_params(self):
        """
        test_get_metrics_query_token_event_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/top_query_tokens_with_event_rate')
        mock_response = '{"aggregations": [{"event_type": "event_type", "results": [{"key": "key", "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_metrics_query_token_event()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_metrics_query_token_event_value_error(self):
        """
        test_get_metrics_query_token_event_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/metrics/top_query_tokens_with_event_rate')
        mock_response = '{"aggregations": [{"event_type": "event_type", "results": [{"key": "key", "matching_results": 16, "event_rate": 10}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_metrics_query_token_event(**req_copy)



# endregion
##############################################################################
# End of Service: EventsAndFeedback
##############################################################################

##############################################################################
# Start of Service: Credentials
##############################################################################
# region

class TestListCredentials():
    """
    Test Class for list_credentials
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_credentials_all_params(self):
        """
        list_credentials()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials')
        mock_response = '{"credentials": [{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.list_credentials(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_credentials_value_error(self):
        """
        test_list_credentials_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials')
        mock_response = '{"credentials": [{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_credentials(**req_copy)



class TestCreateCredentials():
    """
    Test Class for create_credentials
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_credentials_all_params(self):
        """
        create_credentials()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CredentialDetails model
        credential_details_model = {}
        credential_details_model['credential_type'] = 'oauth2'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'testString'
        credential_details_model['username'] = 'testString'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        # Construct a dict representation of a StatusDetails model
        status_details_model = {}
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        # Set up parameter values
        environment_id = 'testString'
        source_type = 'box'
        credential_details = credential_details_model
        status = status_details_model

        # Invoke method
        response = _service.create_credentials(
            environment_id,
            source_type=source_type,
            credential_details=credential_details,
            status=status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_type'] == 'box'
        assert req_body['credential_details'] == credential_details_model
        assert req_body['status'] == status_details_model


    @responses.activate
    def test_create_credentials_value_error(self):
        """
        test_create_credentials_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CredentialDetails model
        credential_details_model = {}
        credential_details_model['credential_type'] = 'oauth2'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'testString'
        credential_details_model['username'] = 'testString'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        # Construct a dict representation of a StatusDetails model
        status_details_model = {}
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        # Set up parameter values
        environment_id = 'testString'
        source_type = 'box'
        credential_details = credential_details_model
        status = status_details_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_credentials(**req_copy)



class TestGetCredentials():
    """
    Test Class for get_credentials
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_credentials_all_params(self):
        """
        get_credentials()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'

        # Invoke method
        response = _service.get_credentials(
            environment_id,
            credential_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_credentials_value_error(self):
        """
        test_get_credentials_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "credential_id": credential_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_credentials(**req_copy)



class TestUpdateCredentials():
    """
    Test Class for update_credentials
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_update_credentials_all_params(self):
        """
        update_credentials()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CredentialDetails model
        credential_details_model = {}
        credential_details_model['credential_type'] = 'oauth2'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'testString'
        credential_details_model['username'] = 'testString'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        # Construct a dict representation of a StatusDetails model
        status_details_model = {}
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'
        source_type = 'box'
        credential_details = credential_details_model
        status = status_details_model

        # Invoke method
        response = _service.update_credentials(
            environment_id,
            credential_id,
            source_type=source_type,
            credential_details=credential_details,
            status=status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['source_type'] == 'box'
        assert req_body['credential_details'] == credential_details_model
        assert req_body['status'] == status_details_model


    @responses.activate
    def test_update_credentials_value_error(self):
        """
        test_update_credentials_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "source_type": "box", "credential_details": {"credential_type": "oauth2", "client_id": "client_id", "enterprise_id": "enterprise_id", "url": "url", "username": "username", "organization_url": "organization_url", "site_collection.path": "site_collection_path", "client_secret": "client_secret", "public_key_id": "public_key_id", "private_key": "private_key", "passphrase": "passphrase", "password": "password", "gateway_id": "gateway_id", "source_version": "online", "web_application_url": "web_application_url", "domain": "domain", "endpoint": "endpoint", "access_key_id": "access_key_id", "secret_access_key": "secret_access_key"}, "status": {"authenticated": false, "error_message": "error_message"}}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a CredentialDetails model
        credential_details_model = {}
        credential_details_model['credential_type'] = 'oauth2'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'testString'
        credential_details_model['username'] = 'testString'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        # Construct a dict representation of a StatusDetails model
        status_details_model = {}
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'
        source_type = 'box'
        credential_details = credential_details_model
        status = status_details_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "credential_id": credential_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_credentials(**req_copy)



class TestDeleteCredentials():
    """
    Test Class for delete_credentials
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_credentials_all_params(self):
        """
        delete_credentials()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'

        # Invoke method
        response = _service.delete_credentials(
            environment_id,
            credential_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_credentials_value_error(self):
        """
        test_delete_credentials_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/credentials/testString')
        mock_response = '{"credential_id": "credential_id", "status": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        credential_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "credential_id": credential_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_credentials(**req_copy)



# endregion
##############################################################################
# End of Service: Credentials
##############################################################################

##############################################################################
# Start of Service: GatewayConfiguration
##############################################################################
# region

class TestListGateways():
    """
    Test Class for list_gateways
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_gateways_all_params(self):
        """
        list_gateways()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways')
        mock_response = '{"gateways": [{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.list_gateways(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_gateways_value_error(self):
        """
        test_list_gateways_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways')
        mock_response = '{"gateways": [{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_gateways(**req_copy)



class TestCreateGateway():
    """
    Test Class for create_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_gateway_all_params(self):
        """
        create_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways')
        mock_response = '{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        name = 'testString'

        # Invoke method
        response = _service.create_gateway(
            environment_id,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'


    @responses.activate
    def test_create_gateway_required_params(self):
        """
        test_create_gateway_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways')
        mock_response = '{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Invoke method
        response = _service.create_gateway(
            environment_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_gateway_value_error(self):
        """
        test_create_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways')
        mock_response = '{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_gateway(**req_copy)



class TestGetGateway():
    """
    Test Class for get_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_gateway_all_params(self):
        """
        get_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways/testString')
        mock_response = '{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        gateway_id = 'testString'

        # Invoke method
        response = _service.get_gateway(
            environment_id,
            gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_gateway_value_error(self):
        """
        test_get_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways/testString')
        mock_response = '{"gateway_id": "gateway_id", "name": "name", "status": "connected", "token": "token", "token_id": "token_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_gateway(**req_copy)



class TestDeleteGateway():
    """
    Test Class for delete_gateway
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_gateway_all_params(self):
        """
        delete_gateway()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways/testString')
        mock_response = '{"gateway_id": "gateway_id", "status": "status"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        gateway_id = 'testString'

        # Invoke method
        response = _service.delete_gateway(
            environment_id,
            gateway_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_gateway_value_error(self):
        """
        test_delete_gateway_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/environments/testString/gateways/testString')
        mock_response = '{"gateway_id": "gateway_id", "status": "status"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        environment_id = 'testString'
        gateway_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "environment_id": environment_id,
            "gateway_id": gateway_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_gateway(**req_copy)



# endregion
##############################################################################
# End of Service: GatewayConfiguration
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AggregationResult():
    """
    Test Class for AggregationResult
    """

    def test_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for AggregationResult
        """

        # Construct a json representation of a AggregationResult model
        aggregation_result_model_json = {}
        aggregation_result_model_json['key'] = 'testString'
        aggregation_result_model_json['matching_results'] = 38

        # Construct a model instance of AggregationResult by calling from_dict on the json representation
        aggregation_result_model = AggregationResult.from_dict(aggregation_result_model_json)
        assert aggregation_result_model != False

        # Construct a model instance of AggregationResult by calling from_dict on the json representation
        aggregation_result_model_dict = AggregationResult.from_dict(aggregation_result_model_json).__dict__
        aggregation_result_model2 = AggregationResult(**aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert aggregation_result_model == aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        aggregation_result_model_json2 = aggregation_result_model.to_dict()
        assert aggregation_result_model_json2 == aggregation_result_model_json

class TestModel_Collection():
    """
    Test Class for Collection
    """

    def test_collection_serialization(self):
        """
        Test serialization/deserialization for Collection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_counts_model = {} # DocumentCounts
        document_counts_model['available'] = 0
        document_counts_model['processing'] = 0
        document_counts_model['failed'] = 0
        document_counts_model['pending'] = 26

        collection_disk_usage_model = {} # CollectionDiskUsage
        collection_disk_usage_model['used_bytes'] = 260

        training_status_model = {} # TrainingStatus
        training_status_model['total_examples'] = 0
        training_status_model['available'] = False
        training_status_model['processing'] = False
        training_status_model['minimum_queries_added'] = False
        training_status_model['minimum_examples_added'] = False
        training_status_model['sufficient_label_diversity'] = False
        training_status_model['notices'] = 0
        training_status_model['successfully_trained'] = "2019-01-01T12:00:00Z"
        training_status_model['data_updated'] = "2019-01-01T12:00:00Z"

        source_status_model = {} # SourceStatus
        source_status_model['status'] = 'complete'
        source_status_model['next_crawl'] = "2019-01-01T12:00:00Z"

        collection_crawl_status_model = {} # CollectionCrawlStatus
        collection_crawl_status_model['source_crawl'] = source_status_model

        sdu_status_custom_fields_model = {} # SduStatusCustomFields
        sdu_status_custom_fields_model['defined'] = 26
        sdu_status_custom_fields_model['maximum_allowed'] = 5

        sdu_status_model = {} # SduStatus
        sdu_status_model['enabled'] = True
        sdu_status_model['total_annotated_pages'] = 0
        sdu_status_model['total_pages'] = 0
        sdu_status_model['total_documents'] = 0
        sdu_status_model['custom_fields'] = sdu_status_custom_fields_model

        # Construct a json representation of a Collection model
        collection_model_json = {}
        collection_model_json['collection_id'] = 'testString'
        collection_model_json['name'] = 'testString'
        collection_model_json['description'] = 'testString'
        collection_model_json['created'] = "2019-01-01T12:00:00Z"
        collection_model_json['updated'] = "2019-01-01T12:00:00Z"
        collection_model_json['status'] = 'active'
        collection_model_json['configuration_id'] = 'testString'
        collection_model_json['language'] = 'testString'
        collection_model_json['document_counts'] = document_counts_model
        collection_model_json['disk_usage'] = collection_disk_usage_model
        collection_model_json['training_status'] = training_status_model
        collection_model_json['crawl_status'] = collection_crawl_status_model
        collection_model_json['smart_document_understanding'] = sdu_status_model

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model = Collection.from_dict(collection_model_json)
        assert collection_model != False

        # Construct a model instance of Collection by calling from_dict on the json representation
        collection_model_dict = Collection.from_dict(collection_model_json).__dict__
        collection_model2 = Collection(**collection_model_dict)

        # Verify the model instances are equivalent
        assert collection_model == collection_model2

        # Convert model instance back to dict and verify no loss of data
        collection_model_json2 = collection_model.to_dict()
        assert collection_model_json2 == collection_model_json

class TestModel_CollectionCrawlStatus():
    """
    Test Class for CollectionCrawlStatus
    """

    def test_collection_crawl_status_serialization(self):
        """
        Test serialization/deserialization for CollectionCrawlStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        source_status_model = {} # SourceStatus
        source_status_model['status'] = 'running'
        source_status_model['next_crawl'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a CollectionCrawlStatus model
        collection_crawl_status_model_json = {}
        collection_crawl_status_model_json['source_crawl'] = source_status_model

        # Construct a model instance of CollectionCrawlStatus by calling from_dict on the json representation
        collection_crawl_status_model = CollectionCrawlStatus.from_dict(collection_crawl_status_model_json)
        assert collection_crawl_status_model != False

        # Construct a model instance of CollectionCrawlStatus by calling from_dict on the json representation
        collection_crawl_status_model_dict = CollectionCrawlStatus.from_dict(collection_crawl_status_model_json).__dict__
        collection_crawl_status_model2 = CollectionCrawlStatus(**collection_crawl_status_model_dict)

        # Verify the model instances are equivalent
        assert collection_crawl_status_model == collection_crawl_status_model2

        # Convert model instance back to dict and verify no loss of data
        collection_crawl_status_model_json2 = collection_crawl_status_model.to_dict()
        assert collection_crawl_status_model_json2 == collection_crawl_status_model_json

class TestModel_CollectionDiskUsage():
    """
    Test Class for CollectionDiskUsage
    """

    def test_collection_disk_usage_serialization(self):
        """
        Test serialization/deserialization for CollectionDiskUsage
        """

        # Construct a json representation of a CollectionDiskUsage model
        collection_disk_usage_model_json = {}
        collection_disk_usage_model_json['used_bytes'] = 38

        # Construct a model instance of CollectionDiskUsage by calling from_dict on the json representation
        collection_disk_usage_model = CollectionDiskUsage.from_dict(collection_disk_usage_model_json)
        assert collection_disk_usage_model != False

        # Construct a model instance of CollectionDiskUsage by calling from_dict on the json representation
        collection_disk_usage_model_dict = CollectionDiskUsage.from_dict(collection_disk_usage_model_json).__dict__
        collection_disk_usage_model2 = CollectionDiskUsage(**collection_disk_usage_model_dict)

        # Verify the model instances are equivalent
        assert collection_disk_usage_model == collection_disk_usage_model2

        # Convert model instance back to dict and verify no loss of data
        collection_disk_usage_model_json2 = collection_disk_usage_model.to_dict()
        assert collection_disk_usage_model_json2 == collection_disk_usage_model_json

class TestModel_CollectionUsage():
    """
    Test Class for CollectionUsage
    """

    def test_collection_usage_serialization(self):
        """
        Test serialization/deserialization for CollectionUsage
        """

        # Construct a json representation of a CollectionUsage model
        collection_usage_model_json = {}
        collection_usage_model_json['available'] = 38
        collection_usage_model_json['maximum_allowed'] = 38

        # Construct a model instance of CollectionUsage by calling from_dict on the json representation
        collection_usage_model = CollectionUsage.from_dict(collection_usage_model_json)
        assert collection_usage_model != False

        # Construct a model instance of CollectionUsage by calling from_dict on the json representation
        collection_usage_model_dict = CollectionUsage.from_dict(collection_usage_model_json).__dict__
        collection_usage_model2 = CollectionUsage(**collection_usage_model_dict)

        # Verify the model instances are equivalent
        assert collection_usage_model == collection_usage_model2

        # Convert model instance back to dict and verify no loss of data
        collection_usage_model_json2 = collection_usage_model.to_dict()
        assert collection_usage_model_json2 == collection_usage_model_json

class TestModel_Completions():
    """
    Test Class for Completions
    """

    def test_completions_serialization(self):
        """
        Test serialization/deserialization for Completions
        """

        # Construct a json representation of a Completions model
        completions_model_json = {}
        completions_model_json['completions'] = ['testString']

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model = Completions.from_dict(completions_model_json)
        assert completions_model != False

        # Construct a model instance of Completions by calling from_dict on the json representation
        completions_model_dict = Completions.from_dict(completions_model_json).__dict__
        completions_model2 = Completions(**completions_model_dict)

        # Verify the model instances are equivalent
        assert completions_model == completions_model2

        # Convert model instance back to dict and verify no loss of data
        completions_model_json2 = completions_model.to_dict()
        assert completions_model_json2 == completions_model_json

class TestModel_Configuration():
    """
    Test Class for Configuration
    """

    def test_configuration_serialization(self):
        """
        Test serialization/deserialization for Configuration
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        pdf_heading_detection_model = {} # PdfHeadingDetection
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        pdf_settings_model = {} # PdfSettings
        pdf_settings_model['heading'] = pdf_heading_detection_model

        word_style_model = {} # WordStyle
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        word_heading_detection_model = {} # WordHeadingDetection
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        word_settings_model = {} # WordSettings
        word_settings_model['heading'] = word_heading_detection_model

        x_path_patterns_model = {} # XPathPatterns
        x_path_patterns_model['xpaths'] = ['testString']

        html_settings_model = {} # HtmlSettings
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['span']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        segment_settings_model = {} # SegmentSettings
        segment_settings_model['enabled'] = True
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['custom-field-1', 'custom-field-2']

        normalization_operation_model = {} # NormalizationOperation
        normalization_operation_model['operation'] = 'move'
        normalization_operation_model['source_field'] = 'extracted_metadata.title'
        normalization_operation_model['destination_field'] = 'metadata.title'

        conversions_model = {} # Conversions
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        nlu_enrichment_keywords_model = {} # NluEnrichmentKeywords
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = False
        nlu_enrichment_keywords_model['limit'] = 50

        nlu_enrichment_entities_model = {} # NluEnrichmentEntities
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = False
        nlu_enrichment_entities_model['limit'] = 50
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'WKS-model-id'

        nlu_enrichment_sentiment_model = {} # NluEnrichmentSentiment
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['IBM', 'Watson']

        nlu_enrichment_emotion_model = {} # NluEnrichmentEmotion
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['IBM', 'Watson']

        nlu_enrichment_semantic_roles_model = {} # NluEnrichmentSemanticRoles
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 50

        nlu_enrichment_relations_model = {} # NluEnrichmentRelations
        nlu_enrichment_relations_model['model'] = 'WKS-model-id'

        nlu_enrichment_concepts_model = {} # NluEnrichmentConcepts
        nlu_enrichment_concepts_model['limit'] = 8

        nlu_enrichment_features_model = {} # NluEnrichmentFeatures
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        enrichment_model = {} # Enrichment
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'enriched_title'
        enrichment_model['source_field'] = 'title'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'natural_language_understanding'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        source_schedule_model = {} # SourceSchedule
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'weekly'

        source_options_folder_model = {} # SourceOptionsFolder
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        source_options_object_model = {} # SourceOptionsObject
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        source_options_site_coll_model = {} # SourceOptionsSiteColl
        source_options_site_coll_model['site_collection_path'] = '/sites/TestSiteA'
        source_options_site_coll_model['limit'] = 10

        source_options_web_crawl_model = {} # SourceOptionsWebCrawl
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        source_options_buckets_model = {} # SourceOptionsBuckets
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        source_options_model = {} # SourceOptions
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        source_model = {} # Source
        source_model['type'] = 'salesforce'
        source_model['credential_id'] = '00ad0000-0000-11e8-ba89-0ed5f00f718b'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        # Construct a json representation of a Configuration model
        configuration_model_json = {}
        configuration_model_json['configuration_id'] = 'testString'
        configuration_model_json['name'] = 'testString'
        configuration_model_json['created'] = "2019-01-01T12:00:00Z"
        configuration_model_json['updated'] = "2019-01-01T12:00:00Z"
        configuration_model_json['description'] = 'testString'
        configuration_model_json['conversions'] = conversions_model
        configuration_model_json['enrichments'] = [enrichment_model]
        configuration_model_json['normalizations'] = [normalization_operation_model]
        configuration_model_json['source'] = source_model

        # Construct a model instance of Configuration by calling from_dict on the json representation
        configuration_model = Configuration.from_dict(configuration_model_json)
        assert configuration_model != False

        # Construct a model instance of Configuration by calling from_dict on the json representation
        configuration_model_dict = Configuration.from_dict(configuration_model_json).__dict__
        configuration_model2 = Configuration(**configuration_model_dict)

        # Verify the model instances are equivalent
        assert configuration_model == configuration_model2

        # Convert model instance back to dict and verify no loss of data
        configuration_model_json2 = configuration_model.to_dict()
        assert configuration_model_json2 == configuration_model_json

class TestModel_Conversions():
    """
    Test Class for Conversions
    """

    def test_conversions_serialization(self):
        """
        Test serialization/deserialization for Conversions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        pdf_heading_detection_model = {} # PdfHeadingDetection
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        pdf_settings_model = {} # PdfSettings
        pdf_settings_model['heading'] = pdf_heading_detection_model

        word_style_model = {} # WordStyle
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        word_heading_detection_model = {} # WordHeadingDetection
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        word_settings_model = {} # WordSettings
        word_settings_model['heading'] = word_heading_detection_model

        x_path_patterns_model = {} # XPathPatterns
        x_path_patterns_model['xpaths'] = ['testString']

        html_settings_model = {} # HtmlSettings
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        segment_settings_model = {} # SegmentSettings
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        normalization_operation_model = {} # NormalizationOperation
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        # Construct a json representation of a Conversions model
        conversions_model_json = {}
        conversions_model_json['pdf'] = pdf_settings_model
        conversions_model_json['word'] = word_settings_model
        conversions_model_json['html'] = html_settings_model
        conversions_model_json['segment'] = segment_settings_model
        conversions_model_json['json_normalizations'] = [normalization_operation_model]
        conversions_model_json['image_text_recognition'] = True

        # Construct a model instance of Conversions by calling from_dict on the json representation
        conversions_model = Conversions.from_dict(conversions_model_json)
        assert conversions_model != False

        # Construct a model instance of Conversions by calling from_dict on the json representation
        conversions_model_dict = Conversions.from_dict(conversions_model_json).__dict__
        conversions_model2 = Conversions(**conversions_model_dict)

        # Verify the model instances are equivalent
        assert conversions_model == conversions_model2

        # Convert model instance back to dict and verify no loss of data
        conversions_model_json2 = conversions_model.to_dict()
        assert conversions_model_json2 == conversions_model_json

class TestModel_CreateEventResponse():
    """
    Test Class for CreateEventResponse
    """

    def test_create_event_response_serialization(self):
        """
        Test serialization/deserialization for CreateEventResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        event_data_model = {} # EventData
        event_data_model['environment_id'] = 'testString'
        event_data_model['session_token'] = 'testString'
        event_data_model['client_timestamp'] = "2019-01-01T12:00:00Z"
        event_data_model['display_rank'] = 38
        event_data_model['collection_id'] = 'testString'
        event_data_model['document_id'] = 'testString'
        event_data_model['query_id'] = 'testString'

        # Construct a json representation of a CreateEventResponse model
        create_event_response_model_json = {}
        create_event_response_model_json['type'] = 'click'
        create_event_response_model_json['data'] = event_data_model

        # Construct a model instance of CreateEventResponse by calling from_dict on the json representation
        create_event_response_model = CreateEventResponse.from_dict(create_event_response_model_json)
        assert create_event_response_model != False

        # Construct a model instance of CreateEventResponse by calling from_dict on the json representation
        create_event_response_model_dict = CreateEventResponse.from_dict(create_event_response_model_json).__dict__
        create_event_response_model2 = CreateEventResponse(**create_event_response_model_dict)

        # Verify the model instances are equivalent
        assert create_event_response_model == create_event_response_model2

        # Convert model instance back to dict and verify no loss of data
        create_event_response_model_json2 = create_event_response_model.to_dict()
        assert create_event_response_model_json2 == create_event_response_model_json

class TestModel_CredentialDetails():
    """
    Test Class for CredentialDetails
    """

    def test_credential_details_serialization(self):
        """
        Test serialization/deserialization for CredentialDetails
        """

        # Construct a json representation of a CredentialDetails model
        credential_details_model_json = {}
        credential_details_model_json['credential_type'] = 'oauth2'
        credential_details_model_json['client_id'] = 'testString'
        credential_details_model_json['enterprise_id'] = 'testString'
        credential_details_model_json['url'] = 'testString'
        credential_details_model_json['username'] = 'testString'
        credential_details_model_json['organization_url'] = 'testString'
        credential_details_model_json['site_collection.path'] = 'testString'
        credential_details_model_json['client_secret'] = 'testString'
        credential_details_model_json['public_key_id'] = 'testString'
        credential_details_model_json['private_key'] = 'testString'
        credential_details_model_json['passphrase'] = 'testString'
        credential_details_model_json['password'] = 'testString'
        credential_details_model_json['gateway_id'] = 'testString'
        credential_details_model_json['source_version'] = 'online'
        credential_details_model_json['web_application_url'] = 'testString'
        credential_details_model_json['domain'] = 'testString'
        credential_details_model_json['endpoint'] = 'testString'
        credential_details_model_json['access_key_id'] = 'testString'
        credential_details_model_json['secret_access_key'] = 'testString'

        # Construct a model instance of CredentialDetails by calling from_dict on the json representation
        credential_details_model = CredentialDetails.from_dict(credential_details_model_json)
        assert credential_details_model != False

        # Construct a model instance of CredentialDetails by calling from_dict on the json representation
        credential_details_model_dict = CredentialDetails.from_dict(credential_details_model_json).__dict__
        credential_details_model2 = CredentialDetails(**credential_details_model_dict)

        # Verify the model instances are equivalent
        assert credential_details_model == credential_details_model2

        # Convert model instance back to dict and verify no loss of data
        credential_details_model_json2 = credential_details_model.to_dict()
        assert credential_details_model_json2 == credential_details_model_json

class TestModel_Credentials():
    """
    Test Class for Credentials
    """

    def test_credentials_serialization(self):
        """
        Test serialization/deserialization for Credentials
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credential_details_model = {} # CredentialDetails
        credential_details_model['credential_type'] = 'username_password'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'login.salesforce.com'
        credential_details_model['username'] = 'user@email.address'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        status_details_model = {} # StatusDetails
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        # Construct a json representation of a Credentials model
        credentials_model_json = {}
        credentials_model_json['credential_id'] = 'testString'
        credentials_model_json['source_type'] = 'box'
        credentials_model_json['credential_details'] = credential_details_model
        credentials_model_json['status'] = status_details_model

        # Construct a model instance of Credentials by calling from_dict on the json representation
        credentials_model = Credentials.from_dict(credentials_model_json)
        assert credentials_model != False

        # Construct a model instance of Credentials by calling from_dict on the json representation
        credentials_model_dict = Credentials.from_dict(credentials_model_json).__dict__
        credentials_model2 = Credentials(**credentials_model_dict)

        # Verify the model instances are equivalent
        assert credentials_model == credentials_model2

        # Convert model instance back to dict and verify no loss of data
        credentials_model_json2 = credentials_model.to_dict()
        assert credentials_model_json2 == credentials_model_json

class TestModel_CredentialsList():
    """
    Test Class for CredentialsList
    """

    def test_credentials_list_serialization(self):
        """
        Test serialization/deserialization for CredentialsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        credential_details_model = {} # CredentialDetails
        credential_details_model['credential_type'] = 'username_password'
        credential_details_model['client_id'] = 'testString'
        credential_details_model['enterprise_id'] = 'testString'
        credential_details_model['url'] = 'login.salesforce.com'
        credential_details_model['username'] = 'user@email.address'
        credential_details_model['organization_url'] = 'testString'
        credential_details_model['site_collection.path'] = 'testString'
        credential_details_model['client_secret'] = 'testString'
        credential_details_model['public_key_id'] = 'testString'
        credential_details_model['private_key'] = 'testString'
        credential_details_model['passphrase'] = 'testString'
        credential_details_model['password'] = 'testString'
        credential_details_model['gateway_id'] = 'testString'
        credential_details_model['source_version'] = 'online'
        credential_details_model['web_application_url'] = 'testString'
        credential_details_model['domain'] = 'testString'
        credential_details_model['endpoint'] = 'testString'
        credential_details_model['access_key_id'] = 'testString'
        credential_details_model['secret_access_key'] = 'testString'

        status_details_model = {} # StatusDetails
        status_details_model['authenticated'] = True
        status_details_model['error_message'] = 'testString'

        credentials_model = {} # Credentials
        credentials_model['credential_id'] = '00000d8c-0000-00e8-ba89-0ed5f89f718b'
        credentials_model['source_type'] = 'salesforce'
        credentials_model['credential_details'] = credential_details_model
        credentials_model['status'] = status_details_model

        # Construct a json representation of a CredentialsList model
        credentials_list_model_json = {}
        credentials_list_model_json['credentials'] = [credentials_model]

        # Construct a model instance of CredentialsList by calling from_dict on the json representation
        credentials_list_model = CredentialsList.from_dict(credentials_list_model_json)
        assert credentials_list_model != False

        # Construct a model instance of CredentialsList by calling from_dict on the json representation
        credentials_list_model_dict = CredentialsList.from_dict(credentials_list_model_json).__dict__
        credentials_list_model2 = CredentialsList(**credentials_list_model_dict)

        # Verify the model instances are equivalent
        assert credentials_list_model == credentials_list_model2

        # Convert model instance back to dict and verify no loss of data
        credentials_list_model_json2 = credentials_list_model.to_dict()
        assert credentials_list_model_json2 == credentials_list_model_json

class TestModel_DeleteCollectionResponse():
    """
    Test Class for DeleteCollectionResponse
    """

    def test_delete_collection_response_serialization(self):
        """
        Test serialization/deserialization for DeleteCollectionResponse
        """

        # Construct a json representation of a DeleteCollectionResponse model
        delete_collection_response_model_json = {}
        delete_collection_response_model_json['collection_id'] = 'testString'
        delete_collection_response_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteCollectionResponse by calling from_dict on the json representation
        delete_collection_response_model = DeleteCollectionResponse.from_dict(delete_collection_response_model_json)
        assert delete_collection_response_model != False

        # Construct a model instance of DeleteCollectionResponse by calling from_dict on the json representation
        delete_collection_response_model_dict = DeleteCollectionResponse.from_dict(delete_collection_response_model_json).__dict__
        delete_collection_response_model2 = DeleteCollectionResponse(**delete_collection_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_collection_response_model == delete_collection_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_collection_response_model_json2 = delete_collection_response_model.to_dict()
        assert delete_collection_response_model_json2 == delete_collection_response_model_json

class TestModel_DeleteConfigurationResponse():
    """
    Test Class for DeleteConfigurationResponse
    """

    def test_delete_configuration_response_serialization(self):
        """
        Test serialization/deserialization for DeleteConfigurationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice
        notice_model['notice_id'] = 'configuration_in_use'
        notice_model['created'] = "2016-09-28T12:34:00Z"
        notice_model['document_id'] = 'testString'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'testString'
        notice_model['description'] = 'The configuration was deleted, but it is referenced by one or more collections.'

        # Construct a json representation of a DeleteConfigurationResponse model
        delete_configuration_response_model_json = {}
        delete_configuration_response_model_json['configuration_id'] = 'testString'
        delete_configuration_response_model_json['status'] = 'deleted'
        delete_configuration_response_model_json['notices'] = [notice_model]

        # Construct a model instance of DeleteConfigurationResponse by calling from_dict on the json representation
        delete_configuration_response_model = DeleteConfigurationResponse.from_dict(delete_configuration_response_model_json)
        assert delete_configuration_response_model != False

        # Construct a model instance of DeleteConfigurationResponse by calling from_dict on the json representation
        delete_configuration_response_model_dict = DeleteConfigurationResponse.from_dict(delete_configuration_response_model_json).__dict__
        delete_configuration_response_model2 = DeleteConfigurationResponse(**delete_configuration_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_configuration_response_model == delete_configuration_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_configuration_response_model_json2 = delete_configuration_response_model.to_dict()
        assert delete_configuration_response_model_json2 == delete_configuration_response_model_json

class TestModel_DeleteCredentials():
    """
    Test Class for DeleteCredentials
    """

    def test_delete_credentials_serialization(self):
        """
        Test serialization/deserialization for DeleteCredentials
        """

        # Construct a json representation of a DeleteCredentials model
        delete_credentials_model_json = {}
        delete_credentials_model_json['credential_id'] = 'testString'
        delete_credentials_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteCredentials by calling from_dict on the json representation
        delete_credentials_model = DeleteCredentials.from_dict(delete_credentials_model_json)
        assert delete_credentials_model != False

        # Construct a model instance of DeleteCredentials by calling from_dict on the json representation
        delete_credentials_model_dict = DeleteCredentials.from_dict(delete_credentials_model_json).__dict__
        delete_credentials_model2 = DeleteCredentials(**delete_credentials_model_dict)

        # Verify the model instances are equivalent
        assert delete_credentials_model == delete_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        delete_credentials_model_json2 = delete_credentials_model.to_dict()
        assert delete_credentials_model_json2 == delete_credentials_model_json

class TestModel_DeleteDocumentResponse():
    """
    Test Class for DeleteDocumentResponse
    """

    def test_delete_document_response_serialization(self):
        """
        Test serialization/deserialization for DeleteDocumentResponse
        """

        # Construct a json representation of a DeleteDocumentResponse model
        delete_document_response_model_json = {}
        delete_document_response_model_json['document_id'] = 'testString'
        delete_document_response_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model = DeleteDocumentResponse.from_dict(delete_document_response_model_json)
        assert delete_document_response_model != False

        # Construct a model instance of DeleteDocumentResponse by calling from_dict on the json representation
        delete_document_response_model_dict = DeleteDocumentResponse.from_dict(delete_document_response_model_json).__dict__
        delete_document_response_model2 = DeleteDocumentResponse(**delete_document_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_document_response_model == delete_document_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_document_response_model_json2 = delete_document_response_model.to_dict()
        assert delete_document_response_model_json2 == delete_document_response_model_json

class TestModel_DeleteEnvironmentResponse():
    """
    Test Class for DeleteEnvironmentResponse
    """

    def test_delete_environment_response_serialization(self):
        """
        Test serialization/deserialization for DeleteEnvironmentResponse
        """

        # Construct a json representation of a DeleteEnvironmentResponse model
        delete_environment_response_model_json = {}
        delete_environment_response_model_json['environment_id'] = 'testString'
        delete_environment_response_model_json['status'] = 'deleted'

        # Construct a model instance of DeleteEnvironmentResponse by calling from_dict on the json representation
        delete_environment_response_model = DeleteEnvironmentResponse.from_dict(delete_environment_response_model_json)
        assert delete_environment_response_model != False

        # Construct a model instance of DeleteEnvironmentResponse by calling from_dict on the json representation
        delete_environment_response_model_dict = DeleteEnvironmentResponse.from_dict(delete_environment_response_model_json).__dict__
        delete_environment_response_model2 = DeleteEnvironmentResponse(**delete_environment_response_model_dict)

        # Verify the model instances are equivalent
        assert delete_environment_response_model == delete_environment_response_model2

        # Convert model instance back to dict and verify no loss of data
        delete_environment_response_model_json2 = delete_environment_response_model.to_dict()
        assert delete_environment_response_model_json2 == delete_environment_response_model_json

class TestModel_DiskUsage():
    """
    Test Class for DiskUsage
    """

    def test_disk_usage_serialization(self):
        """
        Test serialization/deserialization for DiskUsage
        """

        # Construct a json representation of a DiskUsage model
        disk_usage_model_json = {}
        disk_usage_model_json['used_bytes'] = 38
        disk_usage_model_json['maximum_allowed_bytes'] = 38

        # Construct a model instance of DiskUsage by calling from_dict on the json representation
        disk_usage_model = DiskUsage.from_dict(disk_usage_model_json)
        assert disk_usage_model != False

        # Construct a model instance of DiskUsage by calling from_dict on the json representation
        disk_usage_model_dict = DiskUsage.from_dict(disk_usage_model_json).__dict__
        disk_usage_model2 = DiskUsage(**disk_usage_model_dict)

        # Verify the model instances are equivalent
        assert disk_usage_model == disk_usage_model2

        # Convert model instance back to dict and verify no loss of data
        disk_usage_model_json2 = disk_usage_model.to_dict()
        assert disk_usage_model_json2 == disk_usage_model_json

class TestModel_DocumentAccepted():
    """
    Test Class for DocumentAccepted
    """

    def test_document_accepted_serialization(self):
        """
        Test serialization/deserialization for DocumentAccepted
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice
        notice_model['notice_id'] = 'testString'
        notice_model['created'] = "2019-01-01T12:00:00Z"
        notice_model['document_id'] = 'testString'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'testString'
        notice_model['description'] = 'testString'

        # Construct a json representation of a DocumentAccepted model
        document_accepted_model_json = {}
        document_accepted_model_json['document_id'] = 'testString'
        document_accepted_model_json['status'] = 'processing'
        document_accepted_model_json['notices'] = [notice_model]

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model = DocumentAccepted.from_dict(document_accepted_model_json)
        assert document_accepted_model != False

        # Construct a model instance of DocumentAccepted by calling from_dict on the json representation
        document_accepted_model_dict = DocumentAccepted.from_dict(document_accepted_model_json).__dict__
        document_accepted_model2 = DocumentAccepted(**document_accepted_model_dict)

        # Verify the model instances are equivalent
        assert document_accepted_model == document_accepted_model2

        # Convert model instance back to dict and verify no loss of data
        document_accepted_model_json2 = document_accepted_model.to_dict()
        assert document_accepted_model_json2 == document_accepted_model_json

class TestModel_DocumentCounts():
    """
    Test Class for DocumentCounts
    """

    def test_document_counts_serialization(self):
        """
        Test serialization/deserialization for DocumentCounts
        """

        # Construct a json representation of a DocumentCounts model
        document_counts_model_json = {}
        document_counts_model_json['available'] = 26
        document_counts_model_json['processing'] = 26
        document_counts_model_json['failed'] = 26
        document_counts_model_json['pending'] = 26

        # Construct a model instance of DocumentCounts by calling from_dict on the json representation
        document_counts_model = DocumentCounts.from_dict(document_counts_model_json)
        assert document_counts_model != False

        # Construct a model instance of DocumentCounts by calling from_dict on the json representation
        document_counts_model_dict = DocumentCounts.from_dict(document_counts_model_json).__dict__
        document_counts_model2 = DocumentCounts(**document_counts_model_dict)

        # Verify the model instances are equivalent
        assert document_counts_model == document_counts_model2

        # Convert model instance back to dict and verify no loss of data
        document_counts_model_json2 = document_counts_model.to_dict()
        assert document_counts_model_json2 == document_counts_model_json

class TestModel_DocumentStatus():
    """
    Test Class for DocumentStatus
    """

    def test_document_status_serialization(self):
        """
        Test serialization/deserialization for DocumentStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        notice_model = {} # Notice
        notice_model['notice_id'] = 'index_342'
        notice_model['created'] = "2019-01-01T12:00:00Z"
        notice_model['document_id'] = 'f1360220-ea2d-4271-9d62-89a910b13c37'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'indexing'
        notice_model['description'] = 'something bad happened'

        # Construct a json representation of a DocumentStatus model
        document_status_model_json = {}
        document_status_model_json['document_id'] = 'testString'
        document_status_model_json['configuration_id'] = 'testString'
        document_status_model_json['status'] = 'available'
        document_status_model_json['status_description'] = 'testString'
        document_status_model_json['filename'] = 'testString'
        document_status_model_json['file_type'] = 'pdf'
        document_status_model_json['sha1'] = 'testString'
        document_status_model_json['notices'] = [notice_model]

        # Construct a model instance of DocumentStatus by calling from_dict on the json representation
        document_status_model = DocumentStatus.from_dict(document_status_model_json)
        assert document_status_model != False

        # Construct a model instance of DocumentStatus by calling from_dict on the json representation
        document_status_model_dict = DocumentStatus.from_dict(document_status_model_json).__dict__
        document_status_model2 = DocumentStatus(**document_status_model_dict)

        # Verify the model instances are equivalent
        assert document_status_model == document_status_model2

        # Convert model instance back to dict and verify no loss of data
        document_status_model_json2 = document_status_model.to_dict()
        assert document_status_model_json2 == document_status_model_json

class TestModel_Enrichment():
    """
    Test Class for Enrichment
    """

    def test_enrichment_serialization(self):
        """
        Test serialization/deserialization for Enrichment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        nlu_enrichment_keywords_model = {} # NluEnrichmentKeywords
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        nlu_enrichment_entities_model = {} # NluEnrichmentEntities
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        nlu_enrichment_sentiment_model = {} # NluEnrichmentSentiment
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        nlu_enrichment_emotion_model = {} # NluEnrichmentEmotion
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        nlu_enrichment_semantic_roles_model = {} # NluEnrichmentSemanticRoles
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        nlu_enrichment_relations_model = {} # NluEnrichmentRelations
        nlu_enrichment_relations_model['model'] = 'testString'

        nlu_enrichment_concepts_model = {} # NluEnrichmentConcepts
        nlu_enrichment_concepts_model['limit'] = 38

        nlu_enrichment_features_model = {} # NluEnrichmentFeatures
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        # Construct a json representation of a Enrichment model
        enrichment_model_json = {}
        enrichment_model_json['description'] = 'testString'
        enrichment_model_json['destination_field'] = 'testString'
        enrichment_model_json['source_field'] = 'testString'
        enrichment_model_json['overwrite'] = False
        enrichment_model_json['enrichment'] = 'testString'
        enrichment_model_json['ignore_downstream_errors'] = False
        enrichment_model_json['options'] = enrichment_options_model

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model = Enrichment.from_dict(enrichment_model_json)
        assert enrichment_model != False

        # Construct a model instance of Enrichment by calling from_dict on the json representation
        enrichment_model_dict = Enrichment.from_dict(enrichment_model_json).__dict__
        enrichment_model2 = Enrichment(**enrichment_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_model == enrichment_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_model_json2 = enrichment_model.to_dict()
        assert enrichment_model_json2 == enrichment_model_json

class TestModel_EnrichmentOptions():
    """
    Test Class for EnrichmentOptions
    """

    def test_enrichment_options_serialization(self):
        """
        Test serialization/deserialization for EnrichmentOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        nlu_enrichment_keywords_model = {} # NluEnrichmentKeywords
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        nlu_enrichment_entities_model = {} # NluEnrichmentEntities
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        nlu_enrichment_sentiment_model = {} # NluEnrichmentSentiment
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        nlu_enrichment_emotion_model = {} # NluEnrichmentEmotion
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        nlu_enrichment_semantic_roles_model = {} # NluEnrichmentSemanticRoles
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        nlu_enrichment_relations_model = {} # NluEnrichmentRelations
        nlu_enrichment_relations_model['model'] = 'testString'

        nlu_enrichment_concepts_model = {} # NluEnrichmentConcepts
        nlu_enrichment_concepts_model['limit'] = 38

        nlu_enrichment_features_model = {} # NluEnrichmentFeatures
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        # Construct a json representation of a EnrichmentOptions model
        enrichment_options_model_json = {}
        enrichment_options_model_json['features'] = nlu_enrichment_features_model
        enrichment_options_model_json['language'] = 'ar'
        enrichment_options_model_json['model'] = 'testString'

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model = EnrichmentOptions.from_dict(enrichment_options_model_json)
        assert enrichment_options_model != False

        # Construct a model instance of EnrichmentOptions by calling from_dict on the json representation
        enrichment_options_model_dict = EnrichmentOptions.from_dict(enrichment_options_model_json).__dict__
        enrichment_options_model2 = EnrichmentOptions(**enrichment_options_model_dict)

        # Verify the model instances are equivalent
        assert enrichment_options_model == enrichment_options_model2

        # Convert model instance back to dict and verify no loss of data
        enrichment_options_model_json2 = enrichment_options_model.to_dict()
        assert enrichment_options_model_json2 == enrichment_options_model_json

class TestModel_Environment():
    """
    Test Class for Environment
    """

    def test_environment_serialization(self):
        """
        Test serialization/deserialization for Environment
        """

        # Construct dict forms of any model objects needed in order to build this model.

        environment_documents_model = {} # EnvironmentDocuments
        environment_documents_model['available'] = 38
        environment_documents_model['maximum_allowed'] = 1000000

        disk_usage_model = {} # DiskUsage
        disk_usage_model['used_bytes'] = 0
        disk_usage_model['maximum_allowed_bytes'] = 85899345920

        collection_usage_model = {} # CollectionUsage
        collection_usage_model['available'] = 1
        collection_usage_model['maximum_allowed'] = 4

        index_capacity_model = {} # IndexCapacity
        index_capacity_model['documents'] = environment_documents_model
        index_capacity_model['disk_usage'] = disk_usage_model
        index_capacity_model['collections'] = collection_usage_model

        search_status_model = {} # SearchStatus
        search_status_model['scope'] = 'testString'
        search_status_model['status'] = 'NO_DATA'
        search_status_model['status_description'] = 'testString'
        search_status_model['last_trained'] = "2019-01-01"

        # Construct a json representation of a Environment model
        environment_model_json = {}
        environment_model_json['environment_id'] = 'testString'
        environment_model_json['name'] = 'testString'
        environment_model_json['description'] = 'testString'
        environment_model_json['created'] = "2019-01-01T12:00:00Z"
        environment_model_json['updated'] = "2019-01-01T12:00:00Z"
        environment_model_json['status'] = 'active'
        environment_model_json['read_only'] = True
        environment_model_json['size'] = 'LT'
        environment_model_json['requested_size'] = 'testString'
        environment_model_json['index_capacity'] = index_capacity_model
        environment_model_json['search_status'] = search_status_model

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model = Environment.from_dict(environment_model_json)
        assert environment_model != False

        # Construct a model instance of Environment by calling from_dict on the json representation
        environment_model_dict = Environment.from_dict(environment_model_json).__dict__
        environment_model2 = Environment(**environment_model_dict)

        # Verify the model instances are equivalent
        assert environment_model == environment_model2

        # Convert model instance back to dict and verify no loss of data
        environment_model_json2 = environment_model.to_dict()
        assert environment_model_json2 == environment_model_json

class TestModel_EnvironmentDocuments():
    """
    Test Class for EnvironmentDocuments
    """

    def test_environment_documents_serialization(self):
        """
        Test serialization/deserialization for EnvironmentDocuments
        """

        # Construct a json representation of a EnvironmentDocuments model
        environment_documents_model_json = {}
        environment_documents_model_json['available'] = 38
        environment_documents_model_json['maximum_allowed'] = 38

        # Construct a model instance of EnvironmentDocuments by calling from_dict on the json representation
        environment_documents_model = EnvironmentDocuments.from_dict(environment_documents_model_json)
        assert environment_documents_model != False

        # Construct a model instance of EnvironmentDocuments by calling from_dict on the json representation
        environment_documents_model_dict = EnvironmentDocuments.from_dict(environment_documents_model_json).__dict__
        environment_documents_model2 = EnvironmentDocuments(**environment_documents_model_dict)

        # Verify the model instances are equivalent
        assert environment_documents_model == environment_documents_model2

        # Convert model instance back to dict and verify no loss of data
        environment_documents_model_json2 = environment_documents_model.to_dict()
        assert environment_documents_model_json2 == environment_documents_model_json

class TestModel_EventData():
    """
    Test Class for EventData
    """

    def test_event_data_serialization(self):
        """
        Test serialization/deserialization for EventData
        """

        # Construct a json representation of a EventData model
        event_data_model_json = {}
        event_data_model_json['environment_id'] = 'testString'
        event_data_model_json['session_token'] = 'testString'
        event_data_model_json['client_timestamp'] = "2019-01-01T12:00:00Z"
        event_data_model_json['display_rank'] = 38
        event_data_model_json['collection_id'] = 'testString'
        event_data_model_json['document_id'] = 'testString'
        event_data_model_json['query_id'] = 'testString'

        # Construct a model instance of EventData by calling from_dict on the json representation
        event_data_model = EventData.from_dict(event_data_model_json)
        assert event_data_model != False

        # Construct a model instance of EventData by calling from_dict on the json representation
        event_data_model_dict = EventData.from_dict(event_data_model_json).__dict__
        event_data_model2 = EventData(**event_data_model_dict)

        # Verify the model instances are equivalent
        assert event_data_model == event_data_model2

        # Convert model instance back to dict and verify no loss of data
        event_data_model_json2 = event_data_model.to_dict()
        assert event_data_model_json2 == event_data_model_json

class TestModel_Expansion():
    """
    Test Class for Expansion
    """

    def test_expansion_serialization(self):
        """
        Test serialization/deserialization for Expansion
        """

        # Construct a json representation of a Expansion model
        expansion_model_json = {}
        expansion_model_json['input_terms'] = ['testString']
        expansion_model_json['expanded_terms'] = ['testString']

        # Construct a model instance of Expansion by calling from_dict on the json representation
        expansion_model = Expansion.from_dict(expansion_model_json)
        assert expansion_model != False

        # Construct a model instance of Expansion by calling from_dict on the json representation
        expansion_model_dict = Expansion.from_dict(expansion_model_json).__dict__
        expansion_model2 = Expansion(**expansion_model_dict)

        # Verify the model instances are equivalent
        assert expansion_model == expansion_model2

        # Convert model instance back to dict and verify no loss of data
        expansion_model_json2 = expansion_model.to_dict()
        assert expansion_model_json2 == expansion_model_json

class TestModel_Expansions():
    """
    Test Class for Expansions
    """

    def test_expansions_serialization(self):
        """
        Test serialization/deserialization for Expansions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        expansion_model = {} # Expansion
        expansion_model['input_terms'] = ['testString']
        expansion_model['expanded_terms'] = ['testString']

        # Construct a json representation of a Expansions model
        expansions_model_json = {}
        expansions_model_json['expansions'] = [expansion_model]

        # Construct a model instance of Expansions by calling from_dict on the json representation
        expansions_model = Expansions.from_dict(expansions_model_json)
        assert expansions_model != False

        # Construct a model instance of Expansions by calling from_dict on the json representation
        expansions_model_dict = Expansions.from_dict(expansions_model_json).__dict__
        expansions_model2 = Expansions(**expansions_model_dict)

        # Verify the model instances are equivalent
        assert expansions_model == expansions_model2

        # Convert model instance back to dict and verify no loss of data
        expansions_model_json2 = expansions_model.to_dict()
        assert expansions_model_json2 == expansions_model_json

class TestModel_Field():
    """
    Test Class for Field
    """

    def test_field_serialization(self):
        """
        Test serialization/deserialization for Field
        """

        # Construct a json representation of a Field model
        field_model_json = {}
        field_model_json['field'] = 'testString'
        field_model_json['type'] = 'nested'

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model = Field.from_dict(field_model_json)
        assert field_model != False

        # Construct a model instance of Field by calling from_dict on the json representation
        field_model_dict = Field.from_dict(field_model_json).__dict__
        field_model2 = Field(**field_model_dict)

        # Verify the model instances are equivalent
        assert field_model == field_model2

        # Convert model instance back to dict and verify no loss of data
        field_model_json2 = field_model.to_dict()
        assert field_model_json2 == field_model_json

class TestModel_FontSetting():
    """
    Test Class for FontSetting
    """

    def test_font_setting_serialization(self):
        """
        Test serialization/deserialization for FontSetting
        """

        # Construct a json representation of a FontSetting model
        font_setting_model_json = {}
        font_setting_model_json['level'] = 38
        font_setting_model_json['min_size'] = 38
        font_setting_model_json['max_size'] = 38
        font_setting_model_json['bold'] = True
        font_setting_model_json['italic'] = True
        font_setting_model_json['name'] = 'testString'

        # Construct a model instance of FontSetting by calling from_dict on the json representation
        font_setting_model = FontSetting.from_dict(font_setting_model_json)
        assert font_setting_model != False

        # Construct a model instance of FontSetting by calling from_dict on the json representation
        font_setting_model_dict = FontSetting.from_dict(font_setting_model_json).__dict__
        font_setting_model2 = FontSetting(**font_setting_model_dict)

        # Verify the model instances are equivalent
        assert font_setting_model == font_setting_model2

        # Convert model instance back to dict and verify no loss of data
        font_setting_model_json2 = font_setting_model.to_dict()
        assert font_setting_model_json2 == font_setting_model_json

class TestModel_Gateway():
    """
    Test Class for Gateway
    """

    def test_gateway_serialization(self):
        """
        Test serialization/deserialization for Gateway
        """

        # Construct a json representation of a Gateway model
        gateway_model_json = {}
        gateway_model_json['gateway_id'] = 'testString'
        gateway_model_json['name'] = 'testString'
        gateway_model_json['status'] = 'connected'
        gateway_model_json['token'] = 'testString'
        gateway_model_json['token_id'] = 'testString'

        # Construct a model instance of Gateway by calling from_dict on the json representation
        gateway_model = Gateway.from_dict(gateway_model_json)
        assert gateway_model != False

        # Construct a model instance of Gateway by calling from_dict on the json representation
        gateway_model_dict = Gateway.from_dict(gateway_model_json).__dict__
        gateway_model2 = Gateway(**gateway_model_dict)

        # Verify the model instances are equivalent
        assert gateway_model == gateway_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_model_json2 = gateway_model.to_dict()
        assert gateway_model_json2 == gateway_model_json

class TestModel_GatewayDelete():
    """
    Test Class for GatewayDelete
    """

    def test_gateway_delete_serialization(self):
        """
        Test serialization/deserialization for GatewayDelete
        """

        # Construct a json representation of a GatewayDelete model
        gateway_delete_model_json = {}
        gateway_delete_model_json['gateway_id'] = 'testString'
        gateway_delete_model_json['status'] = 'testString'

        # Construct a model instance of GatewayDelete by calling from_dict on the json representation
        gateway_delete_model = GatewayDelete.from_dict(gateway_delete_model_json)
        assert gateway_delete_model != False

        # Construct a model instance of GatewayDelete by calling from_dict on the json representation
        gateway_delete_model_dict = GatewayDelete.from_dict(gateway_delete_model_json).__dict__
        gateway_delete_model2 = GatewayDelete(**gateway_delete_model_dict)

        # Verify the model instances are equivalent
        assert gateway_delete_model == gateway_delete_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_delete_model_json2 = gateway_delete_model.to_dict()
        assert gateway_delete_model_json2 == gateway_delete_model_json

class TestModel_GatewayList():
    """
    Test Class for GatewayList
    """

    def test_gateway_list_serialization(self):
        """
        Test serialization/deserialization for GatewayList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        gateway_model = {} # Gateway
        gateway_model['gateway_id'] = 'testString'
        gateway_model['name'] = 'testString'
        gateway_model['status'] = 'connected'
        gateway_model['token'] = 'testString'
        gateway_model['token_id'] = 'testString'

        # Construct a json representation of a GatewayList model
        gateway_list_model_json = {}
        gateway_list_model_json['gateways'] = [gateway_model]

        # Construct a model instance of GatewayList by calling from_dict on the json representation
        gateway_list_model = GatewayList.from_dict(gateway_list_model_json)
        assert gateway_list_model != False

        # Construct a model instance of GatewayList by calling from_dict on the json representation
        gateway_list_model_dict = GatewayList.from_dict(gateway_list_model_json).__dict__
        gateway_list_model2 = GatewayList(**gateway_list_model_dict)

        # Verify the model instances are equivalent
        assert gateway_list_model == gateway_list_model2

        # Convert model instance back to dict and verify no loss of data
        gateway_list_model_json2 = gateway_list_model.to_dict()
        assert gateway_list_model_json2 == gateway_list_model_json

class TestModel_HtmlSettings():
    """
    Test Class for HtmlSettings
    """

    def test_html_settings_serialization(self):
        """
        Test serialization/deserialization for HtmlSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        x_path_patterns_model = {} # XPathPatterns
        x_path_patterns_model['xpaths'] = ['testString']

        # Construct a json representation of a HtmlSettings model
        html_settings_model_json = {}
        html_settings_model_json['exclude_tags_completely'] = ['testString']
        html_settings_model_json['exclude_tags_keep_content'] = ['testString']
        html_settings_model_json['keep_content'] = x_path_patterns_model
        html_settings_model_json['exclude_content'] = x_path_patterns_model
        html_settings_model_json['keep_tag_attributes'] = ['testString']
        html_settings_model_json['exclude_tag_attributes'] = ['testString']

        # Construct a model instance of HtmlSettings by calling from_dict on the json representation
        html_settings_model = HtmlSettings.from_dict(html_settings_model_json)
        assert html_settings_model != False

        # Construct a model instance of HtmlSettings by calling from_dict on the json representation
        html_settings_model_dict = HtmlSettings.from_dict(html_settings_model_json).__dict__
        html_settings_model2 = HtmlSettings(**html_settings_model_dict)

        # Verify the model instances are equivalent
        assert html_settings_model == html_settings_model2

        # Convert model instance back to dict and verify no loss of data
        html_settings_model_json2 = html_settings_model.to_dict()
        assert html_settings_model_json2 == html_settings_model_json

class TestModel_IndexCapacity():
    """
    Test Class for IndexCapacity
    """

    def test_index_capacity_serialization(self):
        """
        Test serialization/deserialization for IndexCapacity
        """

        # Construct dict forms of any model objects needed in order to build this model.

        environment_documents_model = {} # EnvironmentDocuments
        environment_documents_model['available'] = 38
        environment_documents_model['maximum_allowed'] = 38

        disk_usage_model = {} # DiskUsage
        disk_usage_model['used_bytes'] = 38
        disk_usage_model['maximum_allowed_bytes'] = 38

        collection_usage_model = {} # CollectionUsage
        collection_usage_model['available'] = 38
        collection_usage_model['maximum_allowed'] = 38

        # Construct a json representation of a IndexCapacity model
        index_capacity_model_json = {}
        index_capacity_model_json['documents'] = environment_documents_model
        index_capacity_model_json['disk_usage'] = disk_usage_model
        index_capacity_model_json['collections'] = collection_usage_model

        # Construct a model instance of IndexCapacity by calling from_dict on the json representation
        index_capacity_model = IndexCapacity.from_dict(index_capacity_model_json)
        assert index_capacity_model != False

        # Construct a model instance of IndexCapacity by calling from_dict on the json representation
        index_capacity_model_dict = IndexCapacity.from_dict(index_capacity_model_json).__dict__
        index_capacity_model2 = IndexCapacity(**index_capacity_model_dict)

        # Verify the model instances are equivalent
        assert index_capacity_model == index_capacity_model2

        # Convert model instance back to dict and verify no loss of data
        index_capacity_model_json2 = index_capacity_model.to_dict()
        assert index_capacity_model_json2 == index_capacity_model_json

class TestModel_ListCollectionFieldsResponse():
    """
    Test Class for ListCollectionFieldsResponse
    """

    def test_list_collection_fields_response_serialization(self):
        """
        Test serialization/deserialization for ListCollectionFieldsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        field_model = {} # Field
        field_model['field'] = 'warnings'
        field_model['type'] = 'nested'

        # Construct a json representation of a ListCollectionFieldsResponse model
        list_collection_fields_response_model_json = {}
        list_collection_fields_response_model_json['fields'] = [field_model]

        # Construct a model instance of ListCollectionFieldsResponse by calling from_dict on the json representation
        list_collection_fields_response_model = ListCollectionFieldsResponse.from_dict(list_collection_fields_response_model_json)
        assert list_collection_fields_response_model != False

        # Construct a model instance of ListCollectionFieldsResponse by calling from_dict on the json representation
        list_collection_fields_response_model_dict = ListCollectionFieldsResponse.from_dict(list_collection_fields_response_model_json).__dict__
        list_collection_fields_response_model2 = ListCollectionFieldsResponse(**list_collection_fields_response_model_dict)

        # Verify the model instances are equivalent
        assert list_collection_fields_response_model == list_collection_fields_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_collection_fields_response_model_json2 = list_collection_fields_response_model.to_dict()
        assert list_collection_fields_response_model_json2 == list_collection_fields_response_model_json

class TestModel_ListCollectionsResponse():
    """
    Test Class for ListCollectionsResponse
    """

    def test_list_collections_response_serialization(self):
        """
        Test serialization/deserialization for ListCollectionsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_counts_model = {} # DocumentCounts
        document_counts_model['available'] = 26
        document_counts_model['processing'] = 26
        document_counts_model['failed'] = 26
        document_counts_model['pending'] = 26

        collection_disk_usage_model = {} # CollectionDiskUsage
        collection_disk_usage_model['used_bytes'] = 38

        training_status_model = {} # TrainingStatus
        training_status_model['total_examples'] = 38
        training_status_model['available'] = True
        training_status_model['processing'] = True
        training_status_model['minimum_queries_added'] = True
        training_status_model['minimum_examples_added'] = True
        training_status_model['sufficient_label_diversity'] = True
        training_status_model['notices'] = 38
        training_status_model['successfully_trained'] = "2019-01-01T12:00:00Z"
        training_status_model['data_updated'] = "2019-01-01T12:00:00Z"

        source_status_model = {} # SourceStatus
        source_status_model['status'] = 'running'
        source_status_model['next_crawl'] = "2019-01-01T12:00:00Z"

        collection_crawl_status_model = {} # CollectionCrawlStatus
        collection_crawl_status_model['source_crawl'] = source_status_model

        sdu_status_custom_fields_model = {} # SduStatusCustomFields
        sdu_status_custom_fields_model['defined'] = 26
        sdu_status_custom_fields_model['maximum_allowed'] = 26

        sdu_status_model = {} # SduStatus
        sdu_status_model['enabled'] = True
        sdu_status_model['total_annotated_pages'] = 26
        sdu_status_model['total_pages'] = 26
        sdu_status_model['total_documents'] = 26
        sdu_status_model['custom_fields'] = sdu_status_custom_fields_model

        collection_model = {} # Collection
        collection_model['collection_id'] = 'f1360220-ea2d-4271-9d62-89a910b13c37'
        collection_model['name'] = 'example'
        collection_model['description'] = 'this is a demo collection'
        collection_model['created'] = "2015-08-24T18:42:25.324000Z"
        collection_model['updated'] = "2015-08-24T18:42:25.324000Z"
        collection_model['status'] = 'active'
        collection_model['configuration_id'] = '6963be41-2dea-4f79-8f52-127c63c479b0'
        collection_model['language'] = 'en'
        collection_model['document_counts'] = document_counts_model
        collection_model['disk_usage'] = collection_disk_usage_model
        collection_model['training_status'] = training_status_model
        collection_model['crawl_status'] = collection_crawl_status_model
        collection_model['smart_document_understanding'] = sdu_status_model

        # Construct a json representation of a ListCollectionsResponse model
        list_collections_response_model_json = {}
        list_collections_response_model_json['collections'] = [collection_model]

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model = ListCollectionsResponse.from_dict(list_collections_response_model_json)
        assert list_collections_response_model != False

        # Construct a model instance of ListCollectionsResponse by calling from_dict on the json representation
        list_collections_response_model_dict = ListCollectionsResponse.from_dict(list_collections_response_model_json).__dict__
        list_collections_response_model2 = ListCollectionsResponse(**list_collections_response_model_dict)

        # Verify the model instances are equivalent
        assert list_collections_response_model == list_collections_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_collections_response_model_json2 = list_collections_response_model.to_dict()
        assert list_collections_response_model_json2 == list_collections_response_model_json

class TestModel_ListConfigurationsResponse():
    """
    Test Class for ListConfigurationsResponse
    """

    def test_list_configurations_response_serialization(self):
        """
        Test serialization/deserialization for ListConfigurationsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        pdf_heading_detection_model = {} # PdfHeadingDetection
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        pdf_settings_model = {} # PdfSettings
        pdf_settings_model['heading'] = pdf_heading_detection_model

        word_style_model = {} # WordStyle
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        word_heading_detection_model = {} # WordHeadingDetection
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        word_settings_model = {} # WordSettings
        word_settings_model['heading'] = word_heading_detection_model

        x_path_patterns_model = {} # XPathPatterns
        x_path_patterns_model['xpaths'] = ['testString']

        html_settings_model = {} # HtmlSettings
        html_settings_model['exclude_tags_completely'] = ['testString']
        html_settings_model['exclude_tags_keep_content'] = ['testString']
        html_settings_model['keep_content'] = x_path_patterns_model
        html_settings_model['exclude_content'] = x_path_patterns_model
        html_settings_model['keep_tag_attributes'] = ['testString']
        html_settings_model['exclude_tag_attributes'] = ['testString']

        segment_settings_model = {} # SegmentSettings
        segment_settings_model['enabled'] = False
        segment_settings_model['selector_tags'] = ['h1', 'h2']
        segment_settings_model['annotated_fields'] = ['testString']

        normalization_operation_model = {} # NormalizationOperation
        normalization_operation_model['operation'] = 'copy'
        normalization_operation_model['source_field'] = 'testString'
        normalization_operation_model['destination_field'] = 'testString'

        conversions_model = {} # Conversions
        conversions_model['pdf'] = pdf_settings_model
        conversions_model['word'] = word_settings_model
        conversions_model['html'] = html_settings_model
        conversions_model['segment'] = segment_settings_model
        conversions_model['json_normalizations'] = [normalization_operation_model]
        conversions_model['image_text_recognition'] = True

        nlu_enrichment_keywords_model = {} # NluEnrichmentKeywords
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        nlu_enrichment_entities_model = {} # NluEnrichmentEntities
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        nlu_enrichment_sentiment_model = {} # NluEnrichmentSentiment
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        nlu_enrichment_emotion_model = {} # NluEnrichmentEmotion
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        nlu_enrichment_semantic_roles_model = {} # NluEnrichmentSemanticRoles
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        nlu_enrichment_relations_model = {} # NluEnrichmentRelations
        nlu_enrichment_relations_model['model'] = 'testString'

        nlu_enrichment_concepts_model = {} # NluEnrichmentConcepts
        nlu_enrichment_concepts_model['limit'] = 38

        nlu_enrichment_features_model = {} # NluEnrichmentFeatures
        nlu_enrichment_features_model['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model['categories'] = {}
        nlu_enrichment_features_model['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model['concepts'] = nlu_enrichment_concepts_model

        enrichment_options_model = {} # EnrichmentOptions
        enrichment_options_model['features'] = nlu_enrichment_features_model
        enrichment_options_model['language'] = 'ar'
        enrichment_options_model['model'] = 'testString'

        enrichment_model = {} # Enrichment
        enrichment_model['description'] = 'testString'
        enrichment_model['destination_field'] = 'testString'
        enrichment_model['source_field'] = 'testString'
        enrichment_model['overwrite'] = False
        enrichment_model['enrichment'] = 'testString'
        enrichment_model['ignore_downstream_errors'] = False
        enrichment_model['options'] = enrichment_options_model

        source_schedule_model = {} # SourceSchedule
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        source_options_folder_model = {} # SourceOptionsFolder
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        source_options_object_model = {} # SourceOptionsObject
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        source_options_site_coll_model = {} # SourceOptionsSiteColl
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        source_options_web_crawl_model = {} # SourceOptionsWebCrawl
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        source_options_buckets_model = {} # SourceOptionsBuckets
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        source_options_model = {} # SourceOptions
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        source_model = {} # Source
        source_model['type'] = 'box'
        source_model['credential_id'] = 'testString'
        source_model['schedule'] = source_schedule_model
        source_model['options'] = source_options_model

        configuration_model = {} # Configuration
        configuration_model['configuration_id'] = 'testString'
        configuration_model['name'] = 'testString'
        configuration_model['created'] = "2019-01-01T12:00:00Z"
        configuration_model['updated'] = "2019-01-01T12:00:00Z"
        configuration_model['description'] = 'testString'
        configuration_model['conversions'] = conversions_model
        configuration_model['enrichments'] = [enrichment_model]
        configuration_model['normalizations'] = [normalization_operation_model]
        configuration_model['source'] = source_model

        # Construct a json representation of a ListConfigurationsResponse model
        list_configurations_response_model_json = {}
        list_configurations_response_model_json['configurations'] = [configuration_model]

        # Construct a model instance of ListConfigurationsResponse by calling from_dict on the json representation
        list_configurations_response_model = ListConfigurationsResponse.from_dict(list_configurations_response_model_json)
        assert list_configurations_response_model != False

        # Construct a model instance of ListConfigurationsResponse by calling from_dict on the json representation
        list_configurations_response_model_dict = ListConfigurationsResponse.from_dict(list_configurations_response_model_json).__dict__
        list_configurations_response_model2 = ListConfigurationsResponse(**list_configurations_response_model_dict)

        # Verify the model instances are equivalent
        assert list_configurations_response_model == list_configurations_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_configurations_response_model_json2 = list_configurations_response_model.to_dict()
        assert list_configurations_response_model_json2 == list_configurations_response_model_json

class TestModel_ListEnvironmentsResponse():
    """
    Test Class for ListEnvironmentsResponse
    """

    def test_list_environments_response_serialization(self):
        """
        Test serialization/deserialization for ListEnvironmentsResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        environment_documents_model = {} # EnvironmentDocuments
        environment_documents_model['available'] = 38
        environment_documents_model['maximum_allowed'] = 38

        disk_usage_model = {} # DiskUsage
        disk_usage_model['used_bytes'] = 38
        disk_usage_model['maximum_allowed_bytes'] = 38

        collection_usage_model = {} # CollectionUsage
        collection_usage_model['available'] = 38
        collection_usage_model['maximum_allowed'] = 38

        index_capacity_model = {} # IndexCapacity
        index_capacity_model['documents'] = environment_documents_model
        index_capacity_model['disk_usage'] = disk_usage_model
        index_capacity_model['collections'] = collection_usage_model

        search_status_model = {} # SearchStatus
        search_status_model['scope'] = 'testString'
        search_status_model['status'] = 'NO_DATA'
        search_status_model['status_description'] = 'testString'
        search_status_model['last_trained'] = "2019-01-01"

        environment_model = {} # Environment
        environment_model['environment_id'] = 'ecbda78e-fb06-40b1-a43f-a039fac0adc6'
        environment_model['name'] = 'byod_environment'
        environment_model['description'] = 'Private Data Environment'
        environment_model['created'] = "2017-07-14T12:54:40.985000Z"
        environment_model['updated'] = "2017-07-14T12:54:40.985000Z"
        environment_model['status'] = 'active'
        environment_model['read_only'] = False
        environment_model['size'] = 'LT'
        environment_model['requested_size'] = 'testString'
        environment_model['index_capacity'] = index_capacity_model
        environment_model['search_status'] = search_status_model

        # Construct a json representation of a ListEnvironmentsResponse model
        list_environments_response_model_json = {}
        list_environments_response_model_json['environments'] = [environment_model]

        # Construct a model instance of ListEnvironmentsResponse by calling from_dict on the json representation
        list_environments_response_model = ListEnvironmentsResponse.from_dict(list_environments_response_model_json)
        assert list_environments_response_model != False

        # Construct a model instance of ListEnvironmentsResponse by calling from_dict on the json representation
        list_environments_response_model_dict = ListEnvironmentsResponse.from_dict(list_environments_response_model_json).__dict__
        list_environments_response_model2 = ListEnvironmentsResponse(**list_environments_response_model_dict)

        # Verify the model instances are equivalent
        assert list_environments_response_model == list_environments_response_model2

        # Convert model instance back to dict and verify no loss of data
        list_environments_response_model_json2 = list_environments_response_model.to_dict()
        assert list_environments_response_model_json2 == list_environments_response_model_json

class TestModel_LogQueryResponse():
    """
    Test Class for LogQueryResponse
    """

    def test_log_query_response_serialization(self):
        """
        Test serialization/deserialization for LogQueryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_query_response_result_documents_result_model = {} # LogQueryResponseResultDocumentsResult
        log_query_response_result_documents_result_model['position'] = 38
        log_query_response_result_documents_result_model['document_id'] = 'testString'
        log_query_response_result_documents_result_model['score'] = 72.5
        log_query_response_result_documents_result_model['confidence'] = 72.5
        log_query_response_result_documents_result_model['collection_id'] = 'testString'

        log_query_response_result_documents_model = {} # LogQueryResponseResultDocuments
        log_query_response_result_documents_model['results'] = [log_query_response_result_documents_result_model]
        log_query_response_result_documents_model['count'] = 38

        log_query_response_result_model = {} # LogQueryResponseResult
        log_query_response_result_model['environment_id'] = 'testString'
        log_query_response_result_model['customer_id'] = 'testString'
        log_query_response_result_model['document_type'] = 'query'
        log_query_response_result_model['natural_language_query'] = 'testString'
        log_query_response_result_model['document_results'] = log_query_response_result_documents_model
        log_query_response_result_model['created_timestamp'] = "2019-01-01T12:00:00Z"
        log_query_response_result_model['client_timestamp'] = "2019-01-01T12:00:00Z"
        log_query_response_result_model['query_id'] = 'testString'
        log_query_response_result_model['session_token'] = 'testString'
        log_query_response_result_model['collection_id'] = 'testString'
        log_query_response_result_model['display_rank'] = 38
        log_query_response_result_model['document_id'] = 'testString'
        log_query_response_result_model['event_type'] = 'click'
        log_query_response_result_model['result_type'] = 'document'

        # Construct a json representation of a LogQueryResponse model
        log_query_response_model_json = {}
        log_query_response_model_json['matching_results'] = 38
        log_query_response_model_json['results'] = [log_query_response_result_model]

        # Construct a model instance of LogQueryResponse by calling from_dict on the json representation
        log_query_response_model = LogQueryResponse.from_dict(log_query_response_model_json)
        assert log_query_response_model != False

        # Construct a model instance of LogQueryResponse by calling from_dict on the json representation
        log_query_response_model_dict = LogQueryResponse.from_dict(log_query_response_model_json).__dict__
        log_query_response_model2 = LogQueryResponse(**log_query_response_model_dict)

        # Verify the model instances are equivalent
        assert log_query_response_model == log_query_response_model2

        # Convert model instance back to dict and verify no loss of data
        log_query_response_model_json2 = log_query_response_model.to_dict()
        assert log_query_response_model_json2 == log_query_response_model_json

class TestModel_LogQueryResponseResult():
    """
    Test Class for LogQueryResponseResult
    """

    def test_log_query_response_result_serialization(self):
        """
        Test serialization/deserialization for LogQueryResponseResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_query_response_result_documents_result_model = {} # LogQueryResponseResultDocumentsResult
        log_query_response_result_documents_result_model['position'] = 38
        log_query_response_result_documents_result_model['document_id'] = 'testString'
        log_query_response_result_documents_result_model['score'] = 72.5
        log_query_response_result_documents_result_model['confidence'] = 72.5
        log_query_response_result_documents_result_model['collection_id'] = 'testString'

        log_query_response_result_documents_model = {} # LogQueryResponseResultDocuments
        log_query_response_result_documents_model['results'] = [log_query_response_result_documents_result_model]
        log_query_response_result_documents_model['count'] = 38

        # Construct a json representation of a LogQueryResponseResult model
        log_query_response_result_model_json = {}
        log_query_response_result_model_json['environment_id'] = 'testString'
        log_query_response_result_model_json['customer_id'] = 'testString'
        log_query_response_result_model_json['document_type'] = 'query'
        log_query_response_result_model_json['natural_language_query'] = 'testString'
        log_query_response_result_model_json['document_results'] = log_query_response_result_documents_model
        log_query_response_result_model_json['created_timestamp'] = "2019-01-01T12:00:00Z"
        log_query_response_result_model_json['client_timestamp'] = "2019-01-01T12:00:00Z"
        log_query_response_result_model_json['query_id'] = 'testString'
        log_query_response_result_model_json['session_token'] = 'testString'
        log_query_response_result_model_json['collection_id'] = 'testString'
        log_query_response_result_model_json['display_rank'] = 38
        log_query_response_result_model_json['document_id'] = 'testString'
        log_query_response_result_model_json['event_type'] = 'click'
        log_query_response_result_model_json['result_type'] = 'document'

        # Construct a model instance of LogQueryResponseResult by calling from_dict on the json representation
        log_query_response_result_model = LogQueryResponseResult.from_dict(log_query_response_result_model_json)
        assert log_query_response_result_model != False

        # Construct a model instance of LogQueryResponseResult by calling from_dict on the json representation
        log_query_response_result_model_dict = LogQueryResponseResult.from_dict(log_query_response_result_model_json).__dict__
        log_query_response_result_model2 = LogQueryResponseResult(**log_query_response_result_model_dict)

        # Verify the model instances are equivalent
        assert log_query_response_result_model == log_query_response_result_model2

        # Convert model instance back to dict and verify no loss of data
        log_query_response_result_model_json2 = log_query_response_result_model.to_dict()
        assert log_query_response_result_model_json2 == log_query_response_result_model_json

class TestModel_LogQueryResponseResultDocuments():
    """
    Test Class for LogQueryResponseResultDocuments
    """

    def test_log_query_response_result_documents_serialization(self):
        """
        Test serialization/deserialization for LogQueryResponseResultDocuments
        """

        # Construct dict forms of any model objects needed in order to build this model.

        log_query_response_result_documents_result_model = {} # LogQueryResponseResultDocumentsResult
        log_query_response_result_documents_result_model['position'] = 38
        log_query_response_result_documents_result_model['document_id'] = 'testString'
        log_query_response_result_documents_result_model['score'] = 72.5
        log_query_response_result_documents_result_model['confidence'] = 72.5
        log_query_response_result_documents_result_model['collection_id'] = 'testString'

        # Construct a json representation of a LogQueryResponseResultDocuments model
        log_query_response_result_documents_model_json = {}
        log_query_response_result_documents_model_json['results'] = [log_query_response_result_documents_result_model]
        log_query_response_result_documents_model_json['count'] = 38

        # Construct a model instance of LogQueryResponseResultDocuments by calling from_dict on the json representation
        log_query_response_result_documents_model = LogQueryResponseResultDocuments.from_dict(log_query_response_result_documents_model_json)
        assert log_query_response_result_documents_model != False

        # Construct a model instance of LogQueryResponseResultDocuments by calling from_dict on the json representation
        log_query_response_result_documents_model_dict = LogQueryResponseResultDocuments.from_dict(log_query_response_result_documents_model_json).__dict__
        log_query_response_result_documents_model2 = LogQueryResponseResultDocuments(**log_query_response_result_documents_model_dict)

        # Verify the model instances are equivalent
        assert log_query_response_result_documents_model == log_query_response_result_documents_model2

        # Convert model instance back to dict and verify no loss of data
        log_query_response_result_documents_model_json2 = log_query_response_result_documents_model.to_dict()
        assert log_query_response_result_documents_model_json2 == log_query_response_result_documents_model_json

class TestModel_LogQueryResponseResultDocumentsResult():
    """
    Test Class for LogQueryResponseResultDocumentsResult
    """

    def test_log_query_response_result_documents_result_serialization(self):
        """
        Test serialization/deserialization for LogQueryResponseResultDocumentsResult
        """

        # Construct a json representation of a LogQueryResponseResultDocumentsResult model
        log_query_response_result_documents_result_model_json = {}
        log_query_response_result_documents_result_model_json['position'] = 38
        log_query_response_result_documents_result_model_json['document_id'] = 'testString'
        log_query_response_result_documents_result_model_json['score'] = 72.5
        log_query_response_result_documents_result_model_json['confidence'] = 72.5
        log_query_response_result_documents_result_model_json['collection_id'] = 'testString'

        # Construct a model instance of LogQueryResponseResultDocumentsResult by calling from_dict on the json representation
        log_query_response_result_documents_result_model = LogQueryResponseResultDocumentsResult.from_dict(log_query_response_result_documents_result_model_json)
        assert log_query_response_result_documents_result_model != False

        # Construct a model instance of LogQueryResponseResultDocumentsResult by calling from_dict on the json representation
        log_query_response_result_documents_result_model_dict = LogQueryResponseResultDocumentsResult.from_dict(log_query_response_result_documents_result_model_json).__dict__
        log_query_response_result_documents_result_model2 = LogQueryResponseResultDocumentsResult(**log_query_response_result_documents_result_model_dict)

        # Verify the model instances are equivalent
        assert log_query_response_result_documents_result_model == log_query_response_result_documents_result_model2

        # Convert model instance back to dict and verify no loss of data
        log_query_response_result_documents_result_model_json2 = log_query_response_result_documents_result_model.to_dict()
        assert log_query_response_result_documents_result_model_json2 == log_query_response_result_documents_result_model_json

class TestModel_MetricAggregation():
    """
    Test Class for MetricAggregation
    """

    def test_metric_aggregation_serialization(self):
        """
        Test serialization/deserialization for MetricAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_aggregation_result_model = {} # MetricAggregationResult
        metric_aggregation_result_model['key_as_string'] = "2019-01-01T12:00:00Z"
        metric_aggregation_result_model['key'] = 26
        metric_aggregation_result_model['matching_results'] = 38
        metric_aggregation_result_model['event_rate'] = 72.5

        # Construct a json representation of a MetricAggregation model
        metric_aggregation_model_json = {}
        metric_aggregation_model_json['interval'] = 'testString'
        metric_aggregation_model_json['event_type'] = 'testString'
        metric_aggregation_model_json['results'] = [metric_aggregation_result_model]

        # Construct a model instance of MetricAggregation by calling from_dict on the json representation
        metric_aggregation_model = MetricAggregation.from_dict(metric_aggregation_model_json)
        assert metric_aggregation_model != False

        # Construct a model instance of MetricAggregation by calling from_dict on the json representation
        metric_aggregation_model_dict = MetricAggregation.from_dict(metric_aggregation_model_json).__dict__
        metric_aggregation_model2 = MetricAggregation(**metric_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert metric_aggregation_model == metric_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        metric_aggregation_model_json2 = metric_aggregation_model.to_dict()
        assert metric_aggregation_model_json2 == metric_aggregation_model_json

class TestModel_MetricAggregationResult():
    """
    Test Class for MetricAggregationResult
    """

    def test_metric_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for MetricAggregationResult
        """

        # Construct a json representation of a MetricAggregationResult model
        metric_aggregation_result_model_json = {}
        metric_aggregation_result_model_json['key_as_string'] = "2019-01-01T12:00:00Z"
        metric_aggregation_result_model_json['key'] = 26
        metric_aggregation_result_model_json['matching_results'] = 38
        metric_aggregation_result_model_json['event_rate'] = 72.5

        # Construct a model instance of MetricAggregationResult by calling from_dict on the json representation
        metric_aggregation_result_model = MetricAggregationResult.from_dict(metric_aggregation_result_model_json)
        assert metric_aggregation_result_model != False

        # Construct a model instance of MetricAggregationResult by calling from_dict on the json representation
        metric_aggregation_result_model_dict = MetricAggregationResult.from_dict(metric_aggregation_result_model_json).__dict__
        metric_aggregation_result_model2 = MetricAggregationResult(**metric_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert metric_aggregation_result_model == metric_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        metric_aggregation_result_model_json2 = metric_aggregation_result_model.to_dict()
        assert metric_aggregation_result_model_json2 == metric_aggregation_result_model_json

class TestModel_MetricResponse():
    """
    Test Class for MetricResponse
    """

    def test_metric_response_serialization(self):
        """
        Test serialization/deserialization for MetricResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_aggregation_result_model = {} # MetricAggregationResult
        metric_aggregation_result_model['key_as_string'] = "2019-01-01T12:00:00Z"
        metric_aggregation_result_model['key'] = 26
        metric_aggregation_result_model['matching_results'] = 38
        metric_aggregation_result_model['event_rate'] = 72.5

        metric_aggregation_model = {} # MetricAggregation
        metric_aggregation_model['interval'] = 'testString'
        metric_aggregation_model['event_type'] = 'testString'
        metric_aggregation_model['results'] = [metric_aggregation_result_model]

        # Construct a json representation of a MetricResponse model
        metric_response_model_json = {}
        metric_response_model_json['aggregations'] = [metric_aggregation_model]

        # Construct a model instance of MetricResponse by calling from_dict on the json representation
        metric_response_model = MetricResponse.from_dict(metric_response_model_json)
        assert metric_response_model != False

        # Construct a model instance of MetricResponse by calling from_dict on the json representation
        metric_response_model_dict = MetricResponse.from_dict(metric_response_model_json).__dict__
        metric_response_model2 = MetricResponse(**metric_response_model_dict)

        # Verify the model instances are equivalent
        assert metric_response_model == metric_response_model2

        # Convert model instance back to dict and verify no loss of data
        metric_response_model_json2 = metric_response_model.to_dict()
        assert metric_response_model_json2 == metric_response_model_json

class TestModel_MetricTokenAggregation():
    """
    Test Class for MetricTokenAggregation
    """

    def test_metric_token_aggregation_serialization(self):
        """
        Test serialization/deserialization for MetricTokenAggregation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_token_aggregation_result_model = {} # MetricTokenAggregationResult
        metric_token_aggregation_result_model['key'] = 'testString'
        metric_token_aggregation_result_model['matching_results'] = 38
        metric_token_aggregation_result_model['event_rate'] = 72.5

        # Construct a json representation of a MetricTokenAggregation model
        metric_token_aggregation_model_json = {}
        metric_token_aggregation_model_json['event_type'] = 'testString'
        metric_token_aggregation_model_json['results'] = [metric_token_aggregation_result_model]

        # Construct a model instance of MetricTokenAggregation by calling from_dict on the json representation
        metric_token_aggregation_model = MetricTokenAggregation.from_dict(metric_token_aggregation_model_json)
        assert metric_token_aggregation_model != False

        # Construct a model instance of MetricTokenAggregation by calling from_dict on the json representation
        metric_token_aggregation_model_dict = MetricTokenAggregation.from_dict(metric_token_aggregation_model_json).__dict__
        metric_token_aggregation_model2 = MetricTokenAggregation(**metric_token_aggregation_model_dict)

        # Verify the model instances are equivalent
        assert metric_token_aggregation_model == metric_token_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        metric_token_aggregation_model_json2 = metric_token_aggregation_model.to_dict()
        assert metric_token_aggregation_model_json2 == metric_token_aggregation_model_json

class TestModel_MetricTokenAggregationResult():
    """
    Test Class for MetricTokenAggregationResult
    """

    def test_metric_token_aggregation_result_serialization(self):
        """
        Test serialization/deserialization for MetricTokenAggregationResult
        """

        # Construct a json representation of a MetricTokenAggregationResult model
        metric_token_aggregation_result_model_json = {}
        metric_token_aggregation_result_model_json['key'] = 'testString'
        metric_token_aggregation_result_model_json['matching_results'] = 38
        metric_token_aggregation_result_model_json['event_rate'] = 72.5

        # Construct a model instance of MetricTokenAggregationResult by calling from_dict on the json representation
        metric_token_aggregation_result_model = MetricTokenAggregationResult.from_dict(metric_token_aggregation_result_model_json)
        assert metric_token_aggregation_result_model != False

        # Construct a model instance of MetricTokenAggregationResult by calling from_dict on the json representation
        metric_token_aggregation_result_model_dict = MetricTokenAggregationResult.from_dict(metric_token_aggregation_result_model_json).__dict__
        metric_token_aggregation_result_model2 = MetricTokenAggregationResult(**metric_token_aggregation_result_model_dict)

        # Verify the model instances are equivalent
        assert metric_token_aggregation_result_model == metric_token_aggregation_result_model2

        # Convert model instance back to dict and verify no loss of data
        metric_token_aggregation_result_model_json2 = metric_token_aggregation_result_model.to_dict()
        assert metric_token_aggregation_result_model_json2 == metric_token_aggregation_result_model_json

class TestModel_MetricTokenResponse():
    """
    Test Class for MetricTokenResponse
    """

    def test_metric_token_response_serialization(self):
        """
        Test serialization/deserialization for MetricTokenResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        metric_token_aggregation_result_model = {} # MetricTokenAggregationResult
        metric_token_aggregation_result_model['key'] = 'testString'
        metric_token_aggregation_result_model['matching_results'] = 38
        metric_token_aggregation_result_model['event_rate'] = 72.5

        metric_token_aggregation_model = {} # MetricTokenAggregation
        metric_token_aggregation_model['event_type'] = 'testString'
        metric_token_aggregation_model['results'] = [metric_token_aggregation_result_model]

        # Construct a json representation of a MetricTokenResponse model
        metric_token_response_model_json = {}
        metric_token_response_model_json['aggregations'] = [metric_token_aggregation_model]

        # Construct a model instance of MetricTokenResponse by calling from_dict on the json representation
        metric_token_response_model = MetricTokenResponse.from_dict(metric_token_response_model_json)
        assert metric_token_response_model != False

        # Construct a model instance of MetricTokenResponse by calling from_dict on the json representation
        metric_token_response_model_dict = MetricTokenResponse.from_dict(metric_token_response_model_json).__dict__
        metric_token_response_model2 = MetricTokenResponse(**metric_token_response_model_dict)

        # Verify the model instances are equivalent
        assert metric_token_response_model == metric_token_response_model2

        # Convert model instance back to dict and verify no loss of data
        metric_token_response_model_json2 = metric_token_response_model.to_dict()
        assert metric_token_response_model_json2 == metric_token_response_model_json

class TestModel_NluEnrichmentConcepts():
    """
    Test Class for NluEnrichmentConcepts
    """

    def test_nlu_enrichment_concepts_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentConcepts
        """

        # Construct a json representation of a NluEnrichmentConcepts model
        nlu_enrichment_concepts_model_json = {}
        nlu_enrichment_concepts_model_json['limit'] = 38

        # Construct a model instance of NluEnrichmentConcepts by calling from_dict on the json representation
        nlu_enrichment_concepts_model = NluEnrichmentConcepts.from_dict(nlu_enrichment_concepts_model_json)
        assert nlu_enrichment_concepts_model != False

        # Construct a model instance of NluEnrichmentConcepts by calling from_dict on the json representation
        nlu_enrichment_concepts_model_dict = NluEnrichmentConcepts.from_dict(nlu_enrichment_concepts_model_json).__dict__
        nlu_enrichment_concepts_model2 = NluEnrichmentConcepts(**nlu_enrichment_concepts_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_concepts_model == nlu_enrichment_concepts_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_concepts_model_json2 = nlu_enrichment_concepts_model.to_dict()
        assert nlu_enrichment_concepts_model_json2 == nlu_enrichment_concepts_model_json

class TestModel_NluEnrichmentEmotion():
    """
    Test Class for NluEnrichmentEmotion
    """

    def test_nlu_enrichment_emotion_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentEmotion
        """

        # Construct a json representation of a NluEnrichmentEmotion model
        nlu_enrichment_emotion_model_json = {}
        nlu_enrichment_emotion_model_json['document'] = True
        nlu_enrichment_emotion_model_json['targets'] = ['testString']

        # Construct a model instance of NluEnrichmentEmotion by calling from_dict on the json representation
        nlu_enrichment_emotion_model = NluEnrichmentEmotion.from_dict(nlu_enrichment_emotion_model_json)
        assert nlu_enrichment_emotion_model != False

        # Construct a model instance of NluEnrichmentEmotion by calling from_dict on the json representation
        nlu_enrichment_emotion_model_dict = NluEnrichmentEmotion.from_dict(nlu_enrichment_emotion_model_json).__dict__
        nlu_enrichment_emotion_model2 = NluEnrichmentEmotion(**nlu_enrichment_emotion_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_emotion_model == nlu_enrichment_emotion_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_emotion_model_json2 = nlu_enrichment_emotion_model.to_dict()
        assert nlu_enrichment_emotion_model_json2 == nlu_enrichment_emotion_model_json

class TestModel_NluEnrichmentEntities():
    """
    Test Class for NluEnrichmentEntities
    """

    def test_nlu_enrichment_entities_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentEntities
        """

        # Construct a json representation of a NluEnrichmentEntities model
        nlu_enrichment_entities_model_json = {}
        nlu_enrichment_entities_model_json['sentiment'] = True
        nlu_enrichment_entities_model_json['emotion'] = True
        nlu_enrichment_entities_model_json['limit'] = 38
        nlu_enrichment_entities_model_json['mentions'] = True
        nlu_enrichment_entities_model_json['mention_types'] = True
        nlu_enrichment_entities_model_json['sentence_locations'] = True
        nlu_enrichment_entities_model_json['model'] = 'testString'

        # Construct a model instance of NluEnrichmentEntities by calling from_dict on the json representation
        nlu_enrichment_entities_model = NluEnrichmentEntities.from_dict(nlu_enrichment_entities_model_json)
        assert nlu_enrichment_entities_model != False

        # Construct a model instance of NluEnrichmentEntities by calling from_dict on the json representation
        nlu_enrichment_entities_model_dict = NluEnrichmentEntities.from_dict(nlu_enrichment_entities_model_json).__dict__
        nlu_enrichment_entities_model2 = NluEnrichmentEntities(**nlu_enrichment_entities_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_entities_model == nlu_enrichment_entities_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_entities_model_json2 = nlu_enrichment_entities_model.to_dict()
        assert nlu_enrichment_entities_model_json2 == nlu_enrichment_entities_model_json

class TestModel_NluEnrichmentFeatures():
    """
    Test Class for NluEnrichmentFeatures
    """

    def test_nlu_enrichment_features_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentFeatures
        """

        # Construct dict forms of any model objects needed in order to build this model.

        nlu_enrichment_keywords_model = {} # NluEnrichmentKeywords
        nlu_enrichment_keywords_model['sentiment'] = True
        nlu_enrichment_keywords_model['emotion'] = True
        nlu_enrichment_keywords_model['limit'] = 38

        nlu_enrichment_entities_model = {} # NluEnrichmentEntities
        nlu_enrichment_entities_model['sentiment'] = True
        nlu_enrichment_entities_model['emotion'] = True
        nlu_enrichment_entities_model['limit'] = 38
        nlu_enrichment_entities_model['mentions'] = True
        nlu_enrichment_entities_model['mention_types'] = True
        nlu_enrichment_entities_model['sentence_locations'] = True
        nlu_enrichment_entities_model['model'] = 'testString'

        nlu_enrichment_sentiment_model = {} # NluEnrichmentSentiment
        nlu_enrichment_sentiment_model['document'] = True
        nlu_enrichment_sentiment_model['targets'] = ['testString']

        nlu_enrichment_emotion_model = {} # NluEnrichmentEmotion
        nlu_enrichment_emotion_model['document'] = True
        nlu_enrichment_emotion_model['targets'] = ['testString']

        nlu_enrichment_semantic_roles_model = {} # NluEnrichmentSemanticRoles
        nlu_enrichment_semantic_roles_model['entities'] = True
        nlu_enrichment_semantic_roles_model['keywords'] = True
        nlu_enrichment_semantic_roles_model['limit'] = 38

        nlu_enrichment_relations_model = {} # NluEnrichmentRelations
        nlu_enrichment_relations_model['model'] = 'testString'

        nlu_enrichment_concepts_model = {} # NluEnrichmentConcepts
        nlu_enrichment_concepts_model['limit'] = 38

        # Construct a json representation of a NluEnrichmentFeatures model
        nlu_enrichment_features_model_json = {}
        nlu_enrichment_features_model_json['keywords'] = nlu_enrichment_keywords_model
        nlu_enrichment_features_model_json['entities'] = nlu_enrichment_entities_model
        nlu_enrichment_features_model_json['sentiment'] = nlu_enrichment_sentiment_model
        nlu_enrichment_features_model_json['emotion'] = nlu_enrichment_emotion_model
        nlu_enrichment_features_model_json['categories'] = {}
        nlu_enrichment_features_model_json['semantic_roles'] = nlu_enrichment_semantic_roles_model
        nlu_enrichment_features_model_json['relations'] = nlu_enrichment_relations_model
        nlu_enrichment_features_model_json['concepts'] = nlu_enrichment_concepts_model

        # Construct a model instance of NluEnrichmentFeatures by calling from_dict on the json representation
        nlu_enrichment_features_model = NluEnrichmentFeatures.from_dict(nlu_enrichment_features_model_json)
        assert nlu_enrichment_features_model != False

        # Construct a model instance of NluEnrichmentFeatures by calling from_dict on the json representation
        nlu_enrichment_features_model_dict = NluEnrichmentFeatures.from_dict(nlu_enrichment_features_model_json).__dict__
        nlu_enrichment_features_model2 = NluEnrichmentFeatures(**nlu_enrichment_features_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_features_model == nlu_enrichment_features_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_features_model_json2 = nlu_enrichment_features_model.to_dict()
        assert nlu_enrichment_features_model_json2 == nlu_enrichment_features_model_json

class TestModel_NluEnrichmentKeywords():
    """
    Test Class for NluEnrichmentKeywords
    """

    def test_nlu_enrichment_keywords_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentKeywords
        """

        # Construct a json representation of a NluEnrichmentKeywords model
        nlu_enrichment_keywords_model_json = {}
        nlu_enrichment_keywords_model_json['sentiment'] = True
        nlu_enrichment_keywords_model_json['emotion'] = True
        nlu_enrichment_keywords_model_json['limit'] = 38

        # Construct a model instance of NluEnrichmentKeywords by calling from_dict on the json representation
        nlu_enrichment_keywords_model = NluEnrichmentKeywords.from_dict(nlu_enrichment_keywords_model_json)
        assert nlu_enrichment_keywords_model != False

        # Construct a model instance of NluEnrichmentKeywords by calling from_dict on the json representation
        nlu_enrichment_keywords_model_dict = NluEnrichmentKeywords.from_dict(nlu_enrichment_keywords_model_json).__dict__
        nlu_enrichment_keywords_model2 = NluEnrichmentKeywords(**nlu_enrichment_keywords_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_keywords_model == nlu_enrichment_keywords_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_keywords_model_json2 = nlu_enrichment_keywords_model.to_dict()
        assert nlu_enrichment_keywords_model_json2 == nlu_enrichment_keywords_model_json

class TestModel_NluEnrichmentRelations():
    """
    Test Class for NluEnrichmentRelations
    """

    def test_nlu_enrichment_relations_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentRelations
        """

        # Construct a json representation of a NluEnrichmentRelations model
        nlu_enrichment_relations_model_json = {}
        nlu_enrichment_relations_model_json['model'] = 'testString'

        # Construct a model instance of NluEnrichmentRelations by calling from_dict on the json representation
        nlu_enrichment_relations_model = NluEnrichmentRelations.from_dict(nlu_enrichment_relations_model_json)
        assert nlu_enrichment_relations_model != False

        # Construct a model instance of NluEnrichmentRelations by calling from_dict on the json representation
        nlu_enrichment_relations_model_dict = NluEnrichmentRelations.from_dict(nlu_enrichment_relations_model_json).__dict__
        nlu_enrichment_relations_model2 = NluEnrichmentRelations(**nlu_enrichment_relations_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_relations_model == nlu_enrichment_relations_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_relations_model_json2 = nlu_enrichment_relations_model.to_dict()
        assert nlu_enrichment_relations_model_json2 == nlu_enrichment_relations_model_json

class TestModel_NluEnrichmentSemanticRoles():
    """
    Test Class for NluEnrichmentSemanticRoles
    """

    def test_nlu_enrichment_semantic_roles_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentSemanticRoles
        """

        # Construct a json representation of a NluEnrichmentSemanticRoles model
        nlu_enrichment_semantic_roles_model_json = {}
        nlu_enrichment_semantic_roles_model_json['entities'] = True
        nlu_enrichment_semantic_roles_model_json['keywords'] = True
        nlu_enrichment_semantic_roles_model_json['limit'] = 38

        # Construct a model instance of NluEnrichmentSemanticRoles by calling from_dict on the json representation
        nlu_enrichment_semantic_roles_model = NluEnrichmentSemanticRoles.from_dict(nlu_enrichment_semantic_roles_model_json)
        assert nlu_enrichment_semantic_roles_model != False

        # Construct a model instance of NluEnrichmentSemanticRoles by calling from_dict on the json representation
        nlu_enrichment_semantic_roles_model_dict = NluEnrichmentSemanticRoles.from_dict(nlu_enrichment_semantic_roles_model_json).__dict__
        nlu_enrichment_semantic_roles_model2 = NluEnrichmentSemanticRoles(**nlu_enrichment_semantic_roles_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_semantic_roles_model == nlu_enrichment_semantic_roles_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_semantic_roles_model_json2 = nlu_enrichment_semantic_roles_model.to_dict()
        assert nlu_enrichment_semantic_roles_model_json2 == nlu_enrichment_semantic_roles_model_json

class TestModel_NluEnrichmentSentiment():
    """
    Test Class for NluEnrichmentSentiment
    """

    def test_nlu_enrichment_sentiment_serialization(self):
        """
        Test serialization/deserialization for NluEnrichmentSentiment
        """

        # Construct a json representation of a NluEnrichmentSentiment model
        nlu_enrichment_sentiment_model_json = {}
        nlu_enrichment_sentiment_model_json['document'] = True
        nlu_enrichment_sentiment_model_json['targets'] = ['testString']

        # Construct a model instance of NluEnrichmentSentiment by calling from_dict on the json representation
        nlu_enrichment_sentiment_model = NluEnrichmentSentiment.from_dict(nlu_enrichment_sentiment_model_json)
        assert nlu_enrichment_sentiment_model != False

        # Construct a model instance of NluEnrichmentSentiment by calling from_dict on the json representation
        nlu_enrichment_sentiment_model_dict = NluEnrichmentSentiment.from_dict(nlu_enrichment_sentiment_model_json).__dict__
        nlu_enrichment_sentiment_model2 = NluEnrichmentSentiment(**nlu_enrichment_sentiment_model_dict)

        # Verify the model instances are equivalent
        assert nlu_enrichment_sentiment_model == nlu_enrichment_sentiment_model2

        # Convert model instance back to dict and verify no loss of data
        nlu_enrichment_sentiment_model_json2 = nlu_enrichment_sentiment_model.to_dict()
        assert nlu_enrichment_sentiment_model_json2 == nlu_enrichment_sentiment_model_json

class TestModel_NormalizationOperation():
    """
    Test Class for NormalizationOperation
    """

    def test_normalization_operation_serialization(self):
        """
        Test serialization/deserialization for NormalizationOperation
        """

        # Construct a json representation of a NormalizationOperation model
        normalization_operation_model_json = {}
        normalization_operation_model_json['operation'] = 'copy'
        normalization_operation_model_json['source_field'] = 'testString'
        normalization_operation_model_json['destination_field'] = 'testString'

        # Construct a model instance of NormalizationOperation by calling from_dict on the json representation
        normalization_operation_model = NormalizationOperation.from_dict(normalization_operation_model_json)
        assert normalization_operation_model != False

        # Construct a model instance of NormalizationOperation by calling from_dict on the json representation
        normalization_operation_model_dict = NormalizationOperation.from_dict(normalization_operation_model_json).__dict__
        normalization_operation_model2 = NormalizationOperation(**normalization_operation_model_dict)

        # Verify the model instances are equivalent
        assert normalization_operation_model == normalization_operation_model2

        # Convert model instance back to dict and verify no loss of data
        normalization_operation_model_json2 = normalization_operation_model.to_dict()
        assert normalization_operation_model_json2 == normalization_operation_model_json

class TestModel_Notice():
    """
    Test Class for Notice
    """

    def test_notice_serialization(self):
        """
        Test serialization/deserialization for Notice
        """

        # Construct a json representation of a Notice model
        notice_model_json = {}
        notice_model_json['notice_id'] = 'testString'
        notice_model_json['created'] = "2019-01-01T12:00:00Z"
        notice_model_json['document_id'] = 'testString'
        notice_model_json['query_id'] = 'testString'
        notice_model_json['severity'] = 'warning'
        notice_model_json['step'] = 'testString'
        notice_model_json['description'] = 'testString'

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model = Notice.from_dict(notice_model_json)
        assert notice_model != False

        # Construct a model instance of Notice by calling from_dict on the json representation
        notice_model_dict = Notice.from_dict(notice_model_json).__dict__
        notice_model2 = Notice(**notice_model_dict)

        # Verify the model instances are equivalent
        assert notice_model == notice_model2

        # Convert model instance back to dict and verify no loss of data
        notice_model_json2 = notice_model.to_dict()
        assert notice_model_json2 == notice_model_json

class TestModel_PdfHeadingDetection():
    """
    Test Class for PdfHeadingDetection
    """

    def test_pdf_heading_detection_serialization(self):
        """
        Test serialization/deserialization for PdfHeadingDetection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        # Construct a json representation of a PdfHeadingDetection model
        pdf_heading_detection_model_json = {}
        pdf_heading_detection_model_json['fonts'] = [font_setting_model]

        # Construct a model instance of PdfHeadingDetection by calling from_dict on the json representation
        pdf_heading_detection_model = PdfHeadingDetection.from_dict(pdf_heading_detection_model_json)
        assert pdf_heading_detection_model != False

        # Construct a model instance of PdfHeadingDetection by calling from_dict on the json representation
        pdf_heading_detection_model_dict = PdfHeadingDetection.from_dict(pdf_heading_detection_model_json).__dict__
        pdf_heading_detection_model2 = PdfHeadingDetection(**pdf_heading_detection_model_dict)

        # Verify the model instances are equivalent
        assert pdf_heading_detection_model == pdf_heading_detection_model2

        # Convert model instance back to dict and verify no loss of data
        pdf_heading_detection_model_json2 = pdf_heading_detection_model.to_dict()
        assert pdf_heading_detection_model_json2 == pdf_heading_detection_model_json

class TestModel_PdfSettings():
    """
    Test Class for PdfSettings
    """

    def test_pdf_settings_serialization(self):
        """
        Test serialization/deserialization for PdfSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        pdf_heading_detection_model = {} # PdfHeadingDetection
        pdf_heading_detection_model['fonts'] = [font_setting_model]

        # Construct a json representation of a PdfSettings model
        pdf_settings_model_json = {}
        pdf_settings_model_json['heading'] = pdf_heading_detection_model

        # Construct a model instance of PdfSettings by calling from_dict on the json representation
        pdf_settings_model = PdfSettings.from_dict(pdf_settings_model_json)
        assert pdf_settings_model != False

        # Construct a model instance of PdfSettings by calling from_dict on the json representation
        pdf_settings_model_dict = PdfSettings.from_dict(pdf_settings_model_json).__dict__
        pdf_settings_model2 = PdfSettings(**pdf_settings_model_dict)

        # Verify the model instances are equivalent
        assert pdf_settings_model == pdf_settings_model2

        # Convert model instance back to dict and verify no loss of data
        pdf_settings_model_json2 = pdf_settings_model.to_dict()
        assert pdf_settings_model_json2 == pdf_settings_model_json

class TestModel_QueryAggregation():
    """
    Test Class for QueryAggregation
    """

    def test_query_aggregation_serialization(self):
        """
        Test serialization/deserialization for QueryAggregation
        """

        # Construct a json representation of a QueryAggregation model
        query_aggregation_model_json = {}
        query_aggregation_model_json['type'] = 'testString'
        query_aggregation_model_json['matching_results'] = 38

        # Construct a model instance of QueryAggregation by calling from_dict on the json representation
        query_aggregation_model = QueryAggregation.from_dict(query_aggregation_model_json)
        assert query_aggregation_model != False

        # Construct a copy of the model instance by calling from_dict on the output of to_dict
        query_aggregation_model_json2 = query_aggregation_model.to_dict()
        query_aggregation_model2 = QueryAggregation.from_dict(query_aggregation_model_json2)

        # Verify the model instances are equivalent
        assert query_aggregation_model == query_aggregation_model2

        # Convert model instance back to dict and verify no loss of data
        query_aggregation_model_json2 = query_aggregation_model.to_dict()
        assert query_aggregation_model_json2 == query_aggregation_model_json

class TestModel_QueryNoticesResponse():
    """
    Test Class for QueryNoticesResponse
    """

    def test_query_notices_response_serialization(self):
        """
        Test serialization/deserialization for QueryNoticesResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        notice_model = {} # Notice
        notice_model['notice_id'] = 'xpath_not_found'
        notice_model['created'] = "2016-09-20T17:26:17Z"
        notice_model['document_id'] = '030ba125-29db-43f2-8552-f941ae30a7a8'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'html-to-html'
        notice_model['description'] = 'The xpath expression "boom" was not found.'

        query_notices_result_model = {} # QueryNoticesResult
        query_notices_result_model['id'] = '030ba125-29db-43f2-8552-f941ae30a7a8'
        query_notices_result_model['metadata'] = {}
        query_notices_result_model['collection_id'] = 'f1360220-ea2d-4271-9d62-89a910b13c37'
        query_notices_result_model['result_metadata'] = query_result_metadata_model
        query_notices_result_model['code'] = 200
        query_notices_result_model['filename'] = 'instructions.html'
        query_notices_result_model['file_type'] = 'html'
        query_notices_result_model['sha1'] = 'de9f2c7fd25e1b3afad3e85a0bd17d9b100db4b3'
        query_notices_result_model['notices'] = [notice_model]
        query_notices_result_model['score'] = { 'foo': 'bar' }

        query_aggregation_model = {} # Histogram
        query_aggregation_model['type'] = 'histogram'
        query_aggregation_model['matching_results'] = 38
        query_aggregation_model['field'] = 'testString'
        query_aggregation_model['interval'] = 38

        query_passages_model = {} # QueryPassages
        query_passages_model['document_id'] = 'testString'
        query_passages_model['passage_score'] = 72.5
        query_passages_model['passage_text'] = 'testString'
        query_passages_model['start_offset'] = 38
        query_passages_model['end_offset'] = 38
        query_passages_model['field'] = 'testString'

        # Construct a json representation of a QueryNoticesResponse model
        query_notices_response_model_json = {}
        query_notices_response_model_json['matching_results'] = 38
        query_notices_response_model_json['results'] = [query_notices_result_model]
        query_notices_response_model_json['aggregations'] = [query_aggregation_model]
        query_notices_response_model_json['passages'] = [query_passages_model]
        query_notices_response_model_json['duplicates_removed'] = 38

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model = QueryNoticesResponse.from_dict(query_notices_response_model_json)
        assert query_notices_response_model != False

        # Construct a model instance of QueryNoticesResponse by calling from_dict on the json representation
        query_notices_response_model_dict = QueryNoticesResponse.from_dict(query_notices_response_model_json).__dict__
        query_notices_response_model2 = QueryNoticesResponse(**query_notices_response_model_dict)

        # Verify the model instances are equivalent
        assert query_notices_response_model == query_notices_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_notices_response_model_json2 = query_notices_response_model.to_dict()
        assert query_notices_response_model_json2 == query_notices_response_model_json

class TestModel_QueryNoticesResult():
    """
    Test Class for QueryNoticesResult
    """

    def test_query_notices_result_serialization(self):
        """
        Test serialization/deserialization for QueryNoticesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        notice_model = {} # Notice
        notice_model['notice_id'] = 'testString'
        notice_model['created'] = "2019-01-01T12:00:00Z"
        notice_model['document_id'] = 'testString'
        notice_model['query_id'] = 'testString'
        notice_model['severity'] = 'warning'
        notice_model['step'] = 'testString'
        notice_model['description'] = 'testString'

        # Construct a json representation of a QueryNoticesResult model
        query_notices_result_model_json = {}
        query_notices_result_model_json['id'] = 'testString'
        query_notices_result_model_json['metadata'] = {}
        query_notices_result_model_json['collection_id'] = 'testString'
        query_notices_result_model_json['result_metadata'] = query_result_metadata_model
        query_notices_result_model_json['code'] = 38
        query_notices_result_model_json['filename'] = 'testString'
        query_notices_result_model_json['file_type'] = 'pdf'
        query_notices_result_model_json['sha1'] = 'testString'
        query_notices_result_model_json['notices'] = [notice_model]
        query_notices_result_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of QueryNoticesResult by calling from_dict on the json representation
        query_notices_result_model = QueryNoticesResult.from_dict(query_notices_result_model_json)
        assert query_notices_result_model != False

        # Construct a model instance of QueryNoticesResult by calling from_dict on the json representation
        query_notices_result_model_dict = QueryNoticesResult.from_dict(query_notices_result_model_json).__dict__
        query_notices_result_model2 = QueryNoticesResult(**query_notices_result_model_dict)

        # Verify the model instances are equivalent
        assert query_notices_result_model == query_notices_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_notices_result_model_json2 = query_notices_result_model.to_dict()
        assert query_notices_result_model_json2 == query_notices_result_model_json

        # Test get_properties and set_properties methods.
        query_notices_result_model.set_properties({})
        actual_dict = query_notices_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': { 'foo': 'bar' }}
        query_notices_result_model.set_properties(expected_dict)
        actual_dict = query_notices_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_QueryPassages():
    """
    Test Class for QueryPassages
    """

    def test_query_passages_serialization(self):
        """
        Test serialization/deserialization for QueryPassages
        """

        # Construct a json representation of a QueryPassages model
        query_passages_model_json = {}
        query_passages_model_json['document_id'] = 'testString'
        query_passages_model_json['passage_score'] = 72.5
        query_passages_model_json['passage_text'] = 'testString'
        query_passages_model_json['start_offset'] = 38
        query_passages_model_json['end_offset'] = 38
        query_passages_model_json['field'] = 'testString'

        # Construct a model instance of QueryPassages by calling from_dict on the json representation
        query_passages_model = QueryPassages.from_dict(query_passages_model_json)
        assert query_passages_model != False

        # Construct a model instance of QueryPassages by calling from_dict on the json representation
        query_passages_model_dict = QueryPassages.from_dict(query_passages_model_json).__dict__
        query_passages_model2 = QueryPassages(**query_passages_model_dict)

        # Verify the model instances are equivalent
        assert query_passages_model == query_passages_model2

        # Convert model instance back to dict and verify no loss of data
        query_passages_model_json2 = query_passages_model.to_dict()
        assert query_passages_model_json2 == query_passages_model_json

class TestModel_QueryResponse():
    """
    Test Class for QueryResponse
    """

    def test_query_response_serialization(self):
        """
        Test serialization/deserialization for QueryResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        query_result_model = {} # QueryResult
        query_result_model['id'] = 'watson-generated ID'
        query_result_model['metadata'] = {}
        query_result_model['collection_id'] = 'testString'
        query_result_model['result_metadata'] = query_result_metadata_model
        query_result_model['score'] = { 'foo': 'bar' }

        query_aggregation_model = {} # Histogram
        query_aggregation_model['type'] = 'histogram'
        query_aggregation_model['matching_results'] = 38
        query_aggregation_model['field'] = 'testString'
        query_aggregation_model['interval'] = 38

        query_passages_model = {} # QueryPassages
        query_passages_model['document_id'] = 'testString'
        query_passages_model['passage_score'] = 72.5
        query_passages_model['passage_text'] = 'testString'
        query_passages_model['start_offset'] = 38
        query_passages_model['end_offset'] = 38
        query_passages_model['field'] = 'testString'

        retrieval_details_model = {} # RetrievalDetails
        retrieval_details_model['document_retrieval_strategy'] = 'untrained'

        # Construct a json representation of a QueryResponse model
        query_response_model_json = {}
        query_response_model_json['matching_results'] = 38
        query_response_model_json['results'] = [query_result_model]
        query_response_model_json['aggregations'] = [query_aggregation_model]
        query_response_model_json['passages'] = [query_passages_model]
        query_response_model_json['duplicates_removed'] = 38
        query_response_model_json['session_token'] = 'testString'
        query_response_model_json['retrieval_details'] = retrieval_details_model
        query_response_model_json['suggested_query'] = 'testString'

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model = QueryResponse.from_dict(query_response_model_json)
        assert query_response_model != False

        # Construct a model instance of QueryResponse by calling from_dict on the json representation
        query_response_model_dict = QueryResponse.from_dict(query_response_model_json).__dict__
        query_response_model2 = QueryResponse(**query_response_model_dict)

        # Verify the model instances are equivalent
        assert query_response_model == query_response_model2

        # Convert model instance back to dict and verify no loss of data
        query_response_model_json2 = query_response_model.to_dict()
        assert query_response_model_json2 == query_response_model_json

class TestModel_QueryResult():
    """
    Test Class for QueryResult
    """

    def test_query_result_serialization(self):
        """
        Test serialization/deserialization for QueryResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        # Construct a json representation of a QueryResult model
        query_result_model_json = {}
        query_result_model_json['id'] = 'testString'
        query_result_model_json['metadata'] = {}
        query_result_model_json['collection_id'] = 'testString'
        query_result_model_json['result_metadata'] = query_result_metadata_model
        query_result_model_json['foo'] = { 'foo': 'bar' }

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model = QueryResult.from_dict(query_result_model_json)
        assert query_result_model != False

        # Construct a model instance of QueryResult by calling from_dict on the json representation
        query_result_model_dict = QueryResult.from_dict(query_result_model_json).__dict__
        query_result_model2 = QueryResult(**query_result_model_dict)

        # Verify the model instances are equivalent
        assert query_result_model == query_result_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_model_json2 = query_result_model.to_dict()
        assert query_result_model_json2 == query_result_model_json

        # Test get_properties and set_properties methods.
        query_result_model.set_properties({})
        actual_dict = query_result_model.get_properties()
        assert actual_dict == {}

        expected_dict = {'foo': { 'foo': 'bar' }}
        query_result_model.set_properties(expected_dict)
        actual_dict = query_result_model.get_properties()
        assert actual_dict == expected_dict

class TestModel_QueryResultMetadata():
    """
    Test Class for QueryResultMetadata
    """

    def test_query_result_metadata_serialization(self):
        """
        Test serialization/deserialization for QueryResultMetadata
        """

        # Construct a json representation of a QueryResultMetadata model
        query_result_metadata_model_json = {}
        query_result_metadata_model_json['score'] = 72.5
        query_result_metadata_model_json['confidence'] = 72.5

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model = QueryResultMetadata.from_dict(query_result_metadata_model_json)
        assert query_result_metadata_model != False

        # Construct a model instance of QueryResultMetadata by calling from_dict on the json representation
        query_result_metadata_model_dict = QueryResultMetadata.from_dict(query_result_metadata_model_json).__dict__
        query_result_metadata_model2 = QueryResultMetadata(**query_result_metadata_model_dict)

        # Verify the model instances are equivalent
        assert query_result_metadata_model == query_result_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        query_result_metadata_model_json2 = query_result_metadata_model.to_dict()
        assert query_result_metadata_model_json2 == query_result_metadata_model_json

class TestModel_RetrievalDetails():
    """
    Test Class for RetrievalDetails
    """

    def test_retrieval_details_serialization(self):
        """
        Test serialization/deserialization for RetrievalDetails
        """

        # Construct a json representation of a RetrievalDetails model
        retrieval_details_model_json = {}
        retrieval_details_model_json['document_retrieval_strategy'] = 'untrained'

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model = RetrievalDetails.from_dict(retrieval_details_model_json)
        assert retrieval_details_model != False

        # Construct a model instance of RetrievalDetails by calling from_dict on the json representation
        retrieval_details_model_dict = RetrievalDetails.from_dict(retrieval_details_model_json).__dict__
        retrieval_details_model2 = RetrievalDetails(**retrieval_details_model_dict)

        # Verify the model instances are equivalent
        assert retrieval_details_model == retrieval_details_model2

        # Convert model instance back to dict and verify no loss of data
        retrieval_details_model_json2 = retrieval_details_model.to_dict()
        assert retrieval_details_model_json2 == retrieval_details_model_json

class TestModel_SduStatus():
    """
    Test Class for SduStatus
    """

    def test_sdu_status_serialization(self):
        """
        Test serialization/deserialization for SduStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        sdu_status_custom_fields_model = {} # SduStatusCustomFields
        sdu_status_custom_fields_model['defined'] = 26
        sdu_status_custom_fields_model['maximum_allowed'] = 26

        # Construct a json representation of a SduStatus model
        sdu_status_model_json = {}
        sdu_status_model_json['enabled'] = True
        sdu_status_model_json['total_annotated_pages'] = 26
        sdu_status_model_json['total_pages'] = 26
        sdu_status_model_json['total_documents'] = 26
        sdu_status_model_json['custom_fields'] = sdu_status_custom_fields_model

        # Construct a model instance of SduStatus by calling from_dict on the json representation
        sdu_status_model = SduStatus.from_dict(sdu_status_model_json)
        assert sdu_status_model != False

        # Construct a model instance of SduStatus by calling from_dict on the json representation
        sdu_status_model_dict = SduStatus.from_dict(sdu_status_model_json).__dict__
        sdu_status_model2 = SduStatus(**sdu_status_model_dict)

        # Verify the model instances are equivalent
        assert sdu_status_model == sdu_status_model2

        # Convert model instance back to dict and verify no loss of data
        sdu_status_model_json2 = sdu_status_model.to_dict()
        assert sdu_status_model_json2 == sdu_status_model_json

class TestModel_SduStatusCustomFields():
    """
    Test Class for SduStatusCustomFields
    """

    def test_sdu_status_custom_fields_serialization(self):
        """
        Test serialization/deserialization for SduStatusCustomFields
        """

        # Construct a json representation of a SduStatusCustomFields model
        sdu_status_custom_fields_model_json = {}
        sdu_status_custom_fields_model_json['defined'] = 26
        sdu_status_custom_fields_model_json['maximum_allowed'] = 26

        # Construct a model instance of SduStatusCustomFields by calling from_dict on the json representation
        sdu_status_custom_fields_model = SduStatusCustomFields.from_dict(sdu_status_custom_fields_model_json)
        assert sdu_status_custom_fields_model != False

        # Construct a model instance of SduStatusCustomFields by calling from_dict on the json representation
        sdu_status_custom_fields_model_dict = SduStatusCustomFields.from_dict(sdu_status_custom_fields_model_json).__dict__
        sdu_status_custom_fields_model2 = SduStatusCustomFields(**sdu_status_custom_fields_model_dict)

        # Verify the model instances are equivalent
        assert sdu_status_custom_fields_model == sdu_status_custom_fields_model2

        # Convert model instance back to dict and verify no loss of data
        sdu_status_custom_fields_model_json2 = sdu_status_custom_fields_model.to_dict()
        assert sdu_status_custom_fields_model_json2 == sdu_status_custom_fields_model_json

class TestModel_SearchStatus():
    """
    Test Class for SearchStatus
    """

    def test_search_status_serialization(self):
        """
        Test serialization/deserialization for SearchStatus
        """

        # Construct a json representation of a SearchStatus model
        search_status_model_json = {}
        search_status_model_json['scope'] = 'testString'
        search_status_model_json['status'] = 'NO_DATA'
        search_status_model_json['status_description'] = 'testString'
        search_status_model_json['last_trained'] = "2019-01-01"

        # Construct a model instance of SearchStatus by calling from_dict on the json representation
        search_status_model = SearchStatus.from_dict(search_status_model_json)
        assert search_status_model != False

        # Construct a model instance of SearchStatus by calling from_dict on the json representation
        search_status_model_dict = SearchStatus.from_dict(search_status_model_json).__dict__
        search_status_model2 = SearchStatus(**search_status_model_dict)

        # Verify the model instances are equivalent
        assert search_status_model == search_status_model2

        # Convert model instance back to dict and verify no loss of data
        search_status_model_json2 = search_status_model.to_dict()
        assert search_status_model_json2 == search_status_model_json

class TestModel_SegmentSettings():
    """
    Test Class for SegmentSettings
    """

    def test_segment_settings_serialization(self):
        """
        Test serialization/deserialization for SegmentSettings
        """

        # Construct a json representation of a SegmentSettings model
        segment_settings_model_json = {}
        segment_settings_model_json['enabled'] = False
        segment_settings_model_json['selector_tags'] = ['h1', 'h2']
        segment_settings_model_json['annotated_fields'] = ['testString']

        # Construct a model instance of SegmentSettings by calling from_dict on the json representation
        segment_settings_model = SegmentSettings.from_dict(segment_settings_model_json)
        assert segment_settings_model != False

        # Construct a model instance of SegmentSettings by calling from_dict on the json representation
        segment_settings_model_dict = SegmentSettings.from_dict(segment_settings_model_json).__dict__
        segment_settings_model2 = SegmentSettings(**segment_settings_model_dict)

        # Verify the model instances are equivalent
        assert segment_settings_model == segment_settings_model2

        # Convert model instance back to dict and verify no loss of data
        segment_settings_model_json2 = segment_settings_model.to_dict()
        assert segment_settings_model_json2 == segment_settings_model_json

class TestModel_Source():
    """
    Test Class for Source
    """

    def test_source_serialization(self):
        """
        Test serialization/deserialization for Source
        """

        # Construct dict forms of any model objects needed in order to build this model.

        source_schedule_model = {} # SourceSchedule
        source_schedule_model['enabled'] = True
        source_schedule_model['time_zone'] = 'America/New_York'
        source_schedule_model['frequency'] = 'daily'

        source_options_folder_model = {} # SourceOptionsFolder
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        source_options_object_model = {} # SourceOptionsObject
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        source_options_site_coll_model = {} # SourceOptionsSiteColl
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        source_options_web_crawl_model = {} # SourceOptionsWebCrawl
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        source_options_buckets_model = {} # SourceOptionsBuckets
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        source_options_model = {} # SourceOptions
        source_options_model['folders'] = [source_options_folder_model]
        source_options_model['objects'] = [source_options_object_model]
        source_options_model['site_collections'] = [source_options_site_coll_model]
        source_options_model['urls'] = [source_options_web_crawl_model]
        source_options_model['buckets'] = [source_options_buckets_model]
        source_options_model['crawl_all_buckets'] = True

        # Construct a json representation of a Source model
        source_model_json = {}
        source_model_json['type'] = 'box'
        source_model_json['credential_id'] = 'testString'
        source_model_json['schedule'] = source_schedule_model
        source_model_json['options'] = source_options_model

        # Construct a model instance of Source by calling from_dict on the json representation
        source_model = Source.from_dict(source_model_json)
        assert source_model != False

        # Construct a model instance of Source by calling from_dict on the json representation
        source_model_dict = Source.from_dict(source_model_json).__dict__
        source_model2 = Source(**source_model_dict)

        # Verify the model instances are equivalent
        assert source_model == source_model2

        # Convert model instance back to dict and verify no loss of data
        source_model_json2 = source_model.to_dict()
        assert source_model_json2 == source_model_json

class TestModel_SourceOptions():
    """
    Test Class for SourceOptions
    """

    def test_source_options_serialization(self):
        """
        Test serialization/deserialization for SourceOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        source_options_folder_model = {} # SourceOptionsFolder
        source_options_folder_model['owner_user_id'] = 'testString'
        source_options_folder_model['folder_id'] = 'testString'
        source_options_folder_model['limit'] = 38

        source_options_object_model = {} # SourceOptionsObject
        source_options_object_model['name'] = 'testString'
        source_options_object_model['limit'] = 38

        source_options_site_coll_model = {} # SourceOptionsSiteColl
        source_options_site_coll_model['site_collection_path'] = 'testString'
        source_options_site_coll_model['limit'] = 38

        source_options_web_crawl_model = {} # SourceOptionsWebCrawl
        source_options_web_crawl_model['url'] = 'testString'
        source_options_web_crawl_model['limit_to_starting_hosts'] = True
        source_options_web_crawl_model['crawl_speed'] = 'normal'
        source_options_web_crawl_model['allow_untrusted_certificate'] = False
        source_options_web_crawl_model['maximum_hops'] = 38
        source_options_web_crawl_model['request_timeout'] = 38
        source_options_web_crawl_model['override_robots_txt'] = False
        source_options_web_crawl_model['blacklist'] = ['testString']

        source_options_buckets_model = {} # SourceOptionsBuckets
        source_options_buckets_model['name'] = 'testString'
        source_options_buckets_model['limit'] = 38

        # Construct a json representation of a SourceOptions model
        source_options_model_json = {}
        source_options_model_json['folders'] = [source_options_folder_model]
        source_options_model_json['objects'] = [source_options_object_model]
        source_options_model_json['site_collections'] = [source_options_site_coll_model]
        source_options_model_json['urls'] = [source_options_web_crawl_model]
        source_options_model_json['buckets'] = [source_options_buckets_model]
        source_options_model_json['crawl_all_buckets'] = True

        # Construct a model instance of SourceOptions by calling from_dict on the json representation
        source_options_model = SourceOptions.from_dict(source_options_model_json)
        assert source_options_model != False

        # Construct a model instance of SourceOptions by calling from_dict on the json representation
        source_options_model_dict = SourceOptions.from_dict(source_options_model_json).__dict__
        source_options_model2 = SourceOptions(**source_options_model_dict)

        # Verify the model instances are equivalent
        assert source_options_model == source_options_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_model_json2 = source_options_model.to_dict()
        assert source_options_model_json2 == source_options_model_json

class TestModel_SourceOptionsBuckets():
    """
    Test Class for SourceOptionsBuckets
    """

    def test_source_options_buckets_serialization(self):
        """
        Test serialization/deserialization for SourceOptionsBuckets
        """

        # Construct a json representation of a SourceOptionsBuckets model
        source_options_buckets_model_json = {}
        source_options_buckets_model_json['name'] = 'testString'
        source_options_buckets_model_json['limit'] = 38

        # Construct a model instance of SourceOptionsBuckets by calling from_dict on the json representation
        source_options_buckets_model = SourceOptionsBuckets.from_dict(source_options_buckets_model_json)
        assert source_options_buckets_model != False

        # Construct a model instance of SourceOptionsBuckets by calling from_dict on the json representation
        source_options_buckets_model_dict = SourceOptionsBuckets.from_dict(source_options_buckets_model_json).__dict__
        source_options_buckets_model2 = SourceOptionsBuckets(**source_options_buckets_model_dict)

        # Verify the model instances are equivalent
        assert source_options_buckets_model == source_options_buckets_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_buckets_model_json2 = source_options_buckets_model.to_dict()
        assert source_options_buckets_model_json2 == source_options_buckets_model_json

class TestModel_SourceOptionsFolder():
    """
    Test Class for SourceOptionsFolder
    """

    def test_source_options_folder_serialization(self):
        """
        Test serialization/deserialization for SourceOptionsFolder
        """

        # Construct a json representation of a SourceOptionsFolder model
        source_options_folder_model_json = {}
        source_options_folder_model_json['owner_user_id'] = 'testString'
        source_options_folder_model_json['folder_id'] = 'testString'
        source_options_folder_model_json['limit'] = 38

        # Construct a model instance of SourceOptionsFolder by calling from_dict on the json representation
        source_options_folder_model = SourceOptionsFolder.from_dict(source_options_folder_model_json)
        assert source_options_folder_model != False

        # Construct a model instance of SourceOptionsFolder by calling from_dict on the json representation
        source_options_folder_model_dict = SourceOptionsFolder.from_dict(source_options_folder_model_json).__dict__
        source_options_folder_model2 = SourceOptionsFolder(**source_options_folder_model_dict)

        # Verify the model instances are equivalent
        assert source_options_folder_model == source_options_folder_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_folder_model_json2 = source_options_folder_model.to_dict()
        assert source_options_folder_model_json2 == source_options_folder_model_json

class TestModel_SourceOptionsObject():
    """
    Test Class for SourceOptionsObject
    """

    def test_source_options_object_serialization(self):
        """
        Test serialization/deserialization for SourceOptionsObject
        """

        # Construct a json representation of a SourceOptionsObject model
        source_options_object_model_json = {}
        source_options_object_model_json['name'] = 'testString'
        source_options_object_model_json['limit'] = 38

        # Construct a model instance of SourceOptionsObject by calling from_dict on the json representation
        source_options_object_model = SourceOptionsObject.from_dict(source_options_object_model_json)
        assert source_options_object_model != False

        # Construct a model instance of SourceOptionsObject by calling from_dict on the json representation
        source_options_object_model_dict = SourceOptionsObject.from_dict(source_options_object_model_json).__dict__
        source_options_object_model2 = SourceOptionsObject(**source_options_object_model_dict)

        # Verify the model instances are equivalent
        assert source_options_object_model == source_options_object_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_object_model_json2 = source_options_object_model.to_dict()
        assert source_options_object_model_json2 == source_options_object_model_json

class TestModel_SourceOptionsSiteColl():
    """
    Test Class for SourceOptionsSiteColl
    """

    def test_source_options_site_coll_serialization(self):
        """
        Test serialization/deserialization for SourceOptionsSiteColl
        """

        # Construct a json representation of a SourceOptionsSiteColl model
        source_options_site_coll_model_json = {}
        source_options_site_coll_model_json['site_collection_path'] = 'testString'
        source_options_site_coll_model_json['limit'] = 38

        # Construct a model instance of SourceOptionsSiteColl by calling from_dict on the json representation
        source_options_site_coll_model = SourceOptionsSiteColl.from_dict(source_options_site_coll_model_json)
        assert source_options_site_coll_model != False

        # Construct a model instance of SourceOptionsSiteColl by calling from_dict on the json representation
        source_options_site_coll_model_dict = SourceOptionsSiteColl.from_dict(source_options_site_coll_model_json).__dict__
        source_options_site_coll_model2 = SourceOptionsSiteColl(**source_options_site_coll_model_dict)

        # Verify the model instances are equivalent
        assert source_options_site_coll_model == source_options_site_coll_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_site_coll_model_json2 = source_options_site_coll_model.to_dict()
        assert source_options_site_coll_model_json2 == source_options_site_coll_model_json

class TestModel_SourceOptionsWebCrawl():
    """
    Test Class for SourceOptionsWebCrawl
    """

    def test_source_options_web_crawl_serialization(self):
        """
        Test serialization/deserialization for SourceOptionsWebCrawl
        """

        # Construct a json representation of a SourceOptionsWebCrawl model
        source_options_web_crawl_model_json = {}
        source_options_web_crawl_model_json['url'] = 'testString'
        source_options_web_crawl_model_json['limit_to_starting_hosts'] = True
        source_options_web_crawl_model_json['crawl_speed'] = 'normal'
        source_options_web_crawl_model_json['allow_untrusted_certificate'] = False
        source_options_web_crawl_model_json['maximum_hops'] = 38
        source_options_web_crawl_model_json['request_timeout'] = 38
        source_options_web_crawl_model_json['override_robots_txt'] = False
        source_options_web_crawl_model_json['blacklist'] = ['testString']

        # Construct a model instance of SourceOptionsWebCrawl by calling from_dict on the json representation
        source_options_web_crawl_model = SourceOptionsWebCrawl.from_dict(source_options_web_crawl_model_json)
        assert source_options_web_crawl_model != False

        # Construct a model instance of SourceOptionsWebCrawl by calling from_dict on the json representation
        source_options_web_crawl_model_dict = SourceOptionsWebCrawl.from_dict(source_options_web_crawl_model_json).__dict__
        source_options_web_crawl_model2 = SourceOptionsWebCrawl(**source_options_web_crawl_model_dict)

        # Verify the model instances are equivalent
        assert source_options_web_crawl_model == source_options_web_crawl_model2

        # Convert model instance back to dict and verify no loss of data
        source_options_web_crawl_model_json2 = source_options_web_crawl_model.to_dict()
        assert source_options_web_crawl_model_json2 == source_options_web_crawl_model_json

class TestModel_SourceSchedule():
    """
    Test Class for SourceSchedule
    """

    def test_source_schedule_serialization(self):
        """
        Test serialization/deserialization for SourceSchedule
        """

        # Construct a json representation of a SourceSchedule model
        source_schedule_model_json = {}
        source_schedule_model_json['enabled'] = True
        source_schedule_model_json['time_zone'] = 'America/New_York'
        source_schedule_model_json['frequency'] = 'daily'

        # Construct a model instance of SourceSchedule by calling from_dict on the json representation
        source_schedule_model = SourceSchedule.from_dict(source_schedule_model_json)
        assert source_schedule_model != False

        # Construct a model instance of SourceSchedule by calling from_dict on the json representation
        source_schedule_model_dict = SourceSchedule.from_dict(source_schedule_model_json).__dict__
        source_schedule_model2 = SourceSchedule(**source_schedule_model_dict)

        # Verify the model instances are equivalent
        assert source_schedule_model == source_schedule_model2

        # Convert model instance back to dict and verify no loss of data
        source_schedule_model_json2 = source_schedule_model.to_dict()
        assert source_schedule_model_json2 == source_schedule_model_json

class TestModel_SourceStatus():
    """
    Test Class for SourceStatus
    """

    def test_source_status_serialization(self):
        """
        Test serialization/deserialization for SourceStatus
        """

        # Construct a json representation of a SourceStatus model
        source_status_model_json = {}
        source_status_model_json['status'] = 'running'
        source_status_model_json['next_crawl'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of SourceStatus by calling from_dict on the json representation
        source_status_model = SourceStatus.from_dict(source_status_model_json)
        assert source_status_model != False

        # Construct a model instance of SourceStatus by calling from_dict on the json representation
        source_status_model_dict = SourceStatus.from_dict(source_status_model_json).__dict__
        source_status_model2 = SourceStatus(**source_status_model_dict)

        # Verify the model instances are equivalent
        assert source_status_model == source_status_model2

        # Convert model instance back to dict and verify no loss of data
        source_status_model_json2 = source_status_model.to_dict()
        assert source_status_model_json2 == source_status_model_json

class TestModel_StatusDetails():
    """
    Test Class for StatusDetails
    """

    def test_status_details_serialization(self):
        """
        Test serialization/deserialization for StatusDetails
        """

        # Construct a json representation of a StatusDetails model
        status_details_model_json = {}
        status_details_model_json['authenticated'] = True
        status_details_model_json['error_message'] = 'testString'

        # Construct a model instance of StatusDetails by calling from_dict on the json representation
        status_details_model = StatusDetails.from_dict(status_details_model_json)
        assert status_details_model != False

        # Construct a model instance of StatusDetails by calling from_dict on the json representation
        status_details_model_dict = StatusDetails.from_dict(status_details_model_json).__dict__
        status_details_model2 = StatusDetails(**status_details_model_dict)

        # Verify the model instances are equivalent
        assert status_details_model == status_details_model2

        # Convert model instance back to dict and verify no loss of data
        status_details_model_json2 = status_details_model.to_dict()
        assert status_details_model_json2 == status_details_model_json

class TestModel_TokenDictRule():
    """
    Test Class for TokenDictRule
    """

    def test_token_dict_rule_serialization(self):
        """
        Test serialization/deserialization for TokenDictRule
        """

        # Construct a json representation of a TokenDictRule model
        token_dict_rule_model_json = {}
        token_dict_rule_model_json['text'] = 'testString'
        token_dict_rule_model_json['tokens'] = ['testString']
        token_dict_rule_model_json['readings'] = ['testString']
        token_dict_rule_model_json['part_of_speech'] = 'testString'

        # Construct a model instance of TokenDictRule by calling from_dict on the json representation
        token_dict_rule_model = TokenDictRule.from_dict(token_dict_rule_model_json)
        assert token_dict_rule_model != False

        # Construct a model instance of TokenDictRule by calling from_dict on the json representation
        token_dict_rule_model_dict = TokenDictRule.from_dict(token_dict_rule_model_json).__dict__
        token_dict_rule_model2 = TokenDictRule(**token_dict_rule_model_dict)

        # Verify the model instances are equivalent
        assert token_dict_rule_model == token_dict_rule_model2

        # Convert model instance back to dict and verify no loss of data
        token_dict_rule_model_json2 = token_dict_rule_model.to_dict()
        assert token_dict_rule_model_json2 == token_dict_rule_model_json

class TestModel_TokenDictStatusResponse():
    """
    Test Class for TokenDictStatusResponse
    """

    def test_token_dict_status_response_serialization(self):
        """
        Test serialization/deserialization for TokenDictStatusResponse
        """

        # Construct a json representation of a TokenDictStatusResponse model
        token_dict_status_response_model_json = {}
        token_dict_status_response_model_json['status'] = 'active'
        token_dict_status_response_model_json['type'] = 'testString'

        # Construct a model instance of TokenDictStatusResponse by calling from_dict on the json representation
        token_dict_status_response_model = TokenDictStatusResponse.from_dict(token_dict_status_response_model_json)
        assert token_dict_status_response_model != False

        # Construct a model instance of TokenDictStatusResponse by calling from_dict on the json representation
        token_dict_status_response_model_dict = TokenDictStatusResponse.from_dict(token_dict_status_response_model_json).__dict__
        token_dict_status_response_model2 = TokenDictStatusResponse(**token_dict_status_response_model_dict)

        # Verify the model instances are equivalent
        assert token_dict_status_response_model == token_dict_status_response_model2

        # Convert model instance back to dict and verify no loss of data
        token_dict_status_response_model_json2 = token_dict_status_response_model.to_dict()
        assert token_dict_status_response_model_json2 == token_dict_status_response_model_json

class TestModel_TopHitsResults():
    """
    Test Class for TopHitsResults
    """

    def test_top_hits_results_serialization(self):
        """
        Test serialization/deserialization for TopHitsResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        query_result_model = {} # QueryResult
        query_result_model['id'] = 'testString'
        query_result_model['metadata'] = {}
        query_result_model['collection_id'] = 'testString'
        query_result_model['result_metadata'] = query_result_metadata_model
        query_result_model['foo'] = { 'foo': 'bar' }

        # Construct a json representation of a TopHitsResults model
        top_hits_results_model_json = {}
        top_hits_results_model_json['matching_results'] = 38
        top_hits_results_model_json['hits'] = [query_result_model]

        # Construct a model instance of TopHitsResults by calling from_dict on the json representation
        top_hits_results_model = TopHitsResults.from_dict(top_hits_results_model_json)
        assert top_hits_results_model != False

        # Construct a model instance of TopHitsResults by calling from_dict on the json representation
        top_hits_results_model_dict = TopHitsResults.from_dict(top_hits_results_model_json).__dict__
        top_hits_results_model2 = TopHitsResults(**top_hits_results_model_dict)

        # Verify the model instances are equivalent
        assert top_hits_results_model == top_hits_results_model2

        # Convert model instance back to dict and verify no loss of data
        top_hits_results_model_json2 = top_hits_results_model.to_dict()
        assert top_hits_results_model_json2 == top_hits_results_model_json

class TestModel_TrainingDataSet():
    """
    Test Class for TrainingDataSet
    """

    def test_training_data_set_serialization(self):
        """
        Test serialization/deserialization for TrainingDataSet
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['cross_reference'] = 'testString'
        training_example_model['relevance'] = 38

        training_query_model = {} # TrainingQuery
        training_query_model['query_id'] = 'testString'
        training_query_model['natural_language_query'] = 'testString'
        training_query_model['filter'] = 'testString'
        training_query_model['examples'] = [training_example_model]

        # Construct a json representation of a TrainingDataSet model
        training_data_set_model_json = {}
        training_data_set_model_json['environment_id'] = 'testString'
        training_data_set_model_json['collection_id'] = 'testString'
        training_data_set_model_json['queries'] = [training_query_model]

        # Construct a model instance of TrainingDataSet by calling from_dict on the json representation
        training_data_set_model = TrainingDataSet.from_dict(training_data_set_model_json)
        assert training_data_set_model != False

        # Construct a model instance of TrainingDataSet by calling from_dict on the json representation
        training_data_set_model_dict = TrainingDataSet.from_dict(training_data_set_model_json).__dict__
        training_data_set_model2 = TrainingDataSet(**training_data_set_model_dict)

        # Verify the model instances are equivalent
        assert training_data_set_model == training_data_set_model2

        # Convert model instance back to dict and verify no loss of data
        training_data_set_model_json2 = training_data_set_model.to_dict()
        assert training_data_set_model_json2 == training_data_set_model_json

class TestModel_TrainingExample():
    """
    Test Class for TrainingExample
    """

    def test_training_example_serialization(self):
        """
        Test serialization/deserialization for TrainingExample
        """

        # Construct a json representation of a TrainingExample model
        training_example_model_json = {}
        training_example_model_json['document_id'] = 'testString'
        training_example_model_json['cross_reference'] = 'testString'
        training_example_model_json['relevance'] = 38

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model = TrainingExample.from_dict(training_example_model_json)
        assert training_example_model != False

        # Construct a model instance of TrainingExample by calling from_dict on the json representation
        training_example_model_dict = TrainingExample.from_dict(training_example_model_json).__dict__
        training_example_model2 = TrainingExample(**training_example_model_dict)

        # Verify the model instances are equivalent
        assert training_example_model == training_example_model2

        # Convert model instance back to dict and verify no loss of data
        training_example_model_json2 = training_example_model.to_dict()
        assert training_example_model_json2 == training_example_model_json

class TestModel_TrainingExampleList():
    """
    Test Class for TrainingExampleList
    """

    def test_training_example_list_serialization(self):
        """
        Test serialization/deserialization for TrainingExampleList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['cross_reference'] = 'testString'
        training_example_model['relevance'] = 38

        # Construct a json representation of a TrainingExampleList model
        training_example_list_model_json = {}
        training_example_list_model_json['examples'] = [training_example_model]

        # Construct a model instance of TrainingExampleList by calling from_dict on the json representation
        training_example_list_model = TrainingExampleList.from_dict(training_example_list_model_json)
        assert training_example_list_model != False

        # Construct a model instance of TrainingExampleList by calling from_dict on the json representation
        training_example_list_model_dict = TrainingExampleList.from_dict(training_example_list_model_json).__dict__
        training_example_list_model2 = TrainingExampleList(**training_example_list_model_dict)

        # Verify the model instances are equivalent
        assert training_example_list_model == training_example_list_model2

        # Convert model instance back to dict and verify no loss of data
        training_example_list_model_json2 = training_example_list_model.to_dict()
        assert training_example_list_model_json2 == training_example_list_model_json

class TestModel_TrainingQuery():
    """
    Test Class for TrainingQuery
    """

    def test_training_query_serialization(self):
        """
        Test serialization/deserialization for TrainingQuery
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_example_model = {} # TrainingExample
        training_example_model['document_id'] = 'testString'
        training_example_model['cross_reference'] = 'testString'
        training_example_model['relevance'] = 38

        # Construct a json representation of a TrainingQuery model
        training_query_model_json = {}
        training_query_model_json['query_id'] = 'testString'
        training_query_model_json['natural_language_query'] = 'testString'
        training_query_model_json['filter'] = 'testString'
        training_query_model_json['examples'] = [training_example_model]

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model = TrainingQuery.from_dict(training_query_model_json)
        assert training_query_model != False

        # Construct a model instance of TrainingQuery by calling from_dict on the json representation
        training_query_model_dict = TrainingQuery.from_dict(training_query_model_json).__dict__
        training_query_model2 = TrainingQuery(**training_query_model_dict)

        # Verify the model instances are equivalent
        assert training_query_model == training_query_model2

        # Convert model instance back to dict and verify no loss of data
        training_query_model_json2 = training_query_model.to_dict()
        assert training_query_model_json2 == training_query_model_json

class TestModel_TrainingStatus():
    """
    Test Class for TrainingStatus
    """

    def test_training_status_serialization(self):
        """
        Test serialization/deserialization for TrainingStatus
        """

        # Construct a json representation of a TrainingStatus model
        training_status_model_json = {}
        training_status_model_json['total_examples'] = 38
        training_status_model_json['available'] = True
        training_status_model_json['processing'] = True
        training_status_model_json['minimum_queries_added'] = True
        training_status_model_json['minimum_examples_added'] = True
        training_status_model_json['sufficient_label_diversity'] = True
        training_status_model_json['notices'] = 38
        training_status_model_json['successfully_trained'] = "2019-01-01T12:00:00Z"
        training_status_model_json['data_updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of TrainingStatus by calling from_dict on the json representation
        training_status_model = TrainingStatus.from_dict(training_status_model_json)
        assert training_status_model != False

        # Construct a model instance of TrainingStatus by calling from_dict on the json representation
        training_status_model_dict = TrainingStatus.from_dict(training_status_model_json).__dict__
        training_status_model2 = TrainingStatus(**training_status_model_dict)

        # Verify the model instances are equivalent
        assert training_status_model == training_status_model2

        # Convert model instance back to dict and verify no loss of data
        training_status_model_json2 = training_status_model.to_dict()
        assert training_status_model_json2 == training_status_model_json

class TestModel_WordHeadingDetection():
    """
    Test Class for WordHeadingDetection
    """

    def test_word_heading_detection_serialization(self):
        """
        Test serialization/deserialization for WordHeadingDetection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        word_style_model = {} # WordStyle
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        # Construct a json representation of a WordHeadingDetection model
        word_heading_detection_model_json = {}
        word_heading_detection_model_json['fonts'] = [font_setting_model]
        word_heading_detection_model_json['styles'] = [word_style_model]

        # Construct a model instance of WordHeadingDetection by calling from_dict on the json representation
        word_heading_detection_model = WordHeadingDetection.from_dict(word_heading_detection_model_json)
        assert word_heading_detection_model != False

        # Construct a model instance of WordHeadingDetection by calling from_dict on the json representation
        word_heading_detection_model_dict = WordHeadingDetection.from_dict(word_heading_detection_model_json).__dict__
        word_heading_detection_model2 = WordHeadingDetection(**word_heading_detection_model_dict)

        # Verify the model instances are equivalent
        assert word_heading_detection_model == word_heading_detection_model2

        # Convert model instance back to dict and verify no loss of data
        word_heading_detection_model_json2 = word_heading_detection_model.to_dict()
        assert word_heading_detection_model_json2 == word_heading_detection_model_json

class TestModel_WordSettings():
    """
    Test Class for WordSettings
    """

    def test_word_settings_serialization(self):
        """
        Test serialization/deserialization for WordSettings
        """

        # Construct dict forms of any model objects needed in order to build this model.

        font_setting_model = {} # FontSetting
        font_setting_model['level'] = 38
        font_setting_model['min_size'] = 38
        font_setting_model['max_size'] = 38
        font_setting_model['bold'] = True
        font_setting_model['italic'] = True
        font_setting_model['name'] = 'testString'

        word_style_model = {} # WordStyle
        word_style_model['level'] = 38
        word_style_model['names'] = ['testString']

        word_heading_detection_model = {} # WordHeadingDetection
        word_heading_detection_model['fonts'] = [font_setting_model]
        word_heading_detection_model['styles'] = [word_style_model]

        # Construct a json representation of a WordSettings model
        word_settings_model_json = {}
        word_settings_model_json['heading'] = word_heading_detection_model

        # Construct a model instance of WordSettings by calling from_dict on the json representation
        word_settings_model = WordSettings.from_dict(word_settings_model_json)
        assert word_settings_model != False

        # Construct a model instance of WordSettings by calling from_dict on the json representation
        word_settings_model_dict = WordSettings.from_dict(word_settings_model_json).__dict__
        word_settings_model2 = WordSettings(**word_settings_model_dict)

        # Verify the model instances are equivalent
        assert word_settings_model == word_settings_model2

        # Convert model instance back to dict and verify no loss of data
        word_settings_model_json2 = word_settings_model.to_dict()
        assert word_settings_model_json2 == word_settings_model_json

class TestModel_WordStyle():
    """
    Test Class for WordStyle
    """

    def test_word_style_serialization(self):
        """
        Test serialization/deserialization for WordStyle
        """

        # Construct a json representation of a WordStyle model
        word_style_model_json = {}
        word_style_model_json['level'] = 38
        word_style_model_json['names'] = ['testString']

        # Construct a model instance of WordStyle by calling from_dict on the json representation
        word_style_model = WordStyle.from_dict(word_style_model_json)
        assert word_style_model != False

        # Construct a model instance of WordStyle by calling from_dict on the json representation
        word_style_model_dict = WordStyle.from_dict(word_style_model_json).__dict__
        word_style_model2 = WordStyle(**word_style_model_dict)

        # Verify the model instances are equivalent
        assert word_style_model == word_style_model2

        # Convert model instance back to dict and verify no loss of data
        word_style_model_json2 = word_style_model.to_dict()
        assert word_style_model_json2 == word_style_model_json

class TestModel_XPathPatterns():
    """
    Test Class for XPathPatterns
    """

    def test_x_path_patterns_serialization(self):
        """
        Test serialization/deserialization for XPathPatterns
        """

        # Construct a json representation of a XPathPatterns model
        x_path_patterns_model_json = {}
        x_path_patterns_model_json['xpaths'] = ['testString']

        # Construct a model instance of XPathPatterns by calling from_dict on the json representation
        x_path_patterns_model = XPathPatterns.from_dict(x_path_patterns_model_json)
        assert x_path_patterns_model != False

        # Construct a model instance of XPathPatterns by calling from_dict on the json representation
        x_path_patterns_model_dict = XPathPatterns.from_dict(x_path_patterns_model_json).__dict__
        x_path_patterns_model2 = XPathPatterns(**x_path_patterns_model_dict)

        # Verify the model instances are equivalent
        assert x_path_patterns_model == x_path_patterns_model2

        # Convert model instance back to dict and verify no loss of data
        x_path_patterns_model_json2 = x_path_patterns_model.to_dict()
        assert x_path_patterns_model_json2 == x_path_patterns_model_json

class TestModel_Calculation():
    """
    Test Class for Calculation
    """

    def test_calculation_serialization(self):
        """
        Test serialization/deserialization for Calculation
        """

        # Construct a json representation of a Calculation model
        calculation_model_json = {}
        calculation_model_json['type'] = 'unique_count'
        calculation_model_json['matching_results'] = 38
        calculation_model_json['field'] = 'testString'
        calculation_model_json['value'] = 72.5

        # Construct a model instance of Calculation by calling from_dict on the json representation
        calculation_model = Calculation.from_dict(calculation_model_json)
        assert calculation_model != False

        # Construct a model instance of Calculation by calling from_dict on the json representation
        calculation_model_dict = Calculation.from_dict(calculation_model_json).__dict__
        calculation_model2 = Calculation(**calculation_model_dict)

        # Verify the model instances are equivalent
        assert calculation_model == calculation_model2

        # Convert model instance back to dict and verify no loss of data
        calculation_model_json2 = calculation_model.to_dict()
        assert calculation_model_json2 == calculation_model_json

class TestModel_Filter():
    """
    Test Class for Filter
    """

    def test_filter_serialization(self):
        """
        Test serialization/deserialization for Filter
        """

        # Construct a json representation of a Filter model
        filter_model_json = {}
        filter_model_json['type'] = 'filter'
        filter_model_json['matching_results'] = 38
        filter_model_json['match'] = 'testString'

        # Construct a model instance of Filter by calling from_dict on the json representation
        filter_model = Filter.from_dict(filter_model_json)
        assert filter_model != False

        # Construct a model instance of Filter by calling from_dict on the json representation
        filter_model_dict = Filter.from_dict(filter_model_json).__dict__
        filter_model2 = Filter(**filter_model_dict)

        # Verify the model instances are equivalent
        assert filter_model == filter_model2

        # Convert model instance back to dict and verify no loss of data
        filter_model_json2 = filter_model.to_dict()
        assert filter_model_json2 == filter_model_json

class TestModel_Histogram():
    """
    Test Class for Histogram
    """

    def test_histogram_serialization(self):
        """
        Test serialization/deserialization for Histogram
        """

        # Construct a json representation of a Histogram model
        histogram_model_json = {}
        histogram_model_json['type'] = 'histogram'
        histogram_model_json['matching_results'] = 38
        histogram_model_json['field'] = 'testString'
        histogram_model_json['interval'] = 38

        # Construct a model instance of Histogram by calling from_dict on the json representation
        histogram_model = Histogram.from_dict(histogram_model_json)
        assert histogram_model != False

        # Construct a model instance of Histogram by calling from_dict on the json representation
        histogram_model_dict = Histogram.from_dict(histogram_model_json).__dict__
        histogram_model2 = Histogram(**histogram_model_dict)

        # Verify the model instances are equivalent
        assert histogram_model == histogram_model2

        # Convert model instance back to dict and verify no loss of data
        histogram_model_json2 = histogram_model.to_dict()
        assert histogram_model_json2 == histogram_model_json

class TestModel_Nested():
    """
    Test Class for Nested
    """

    def test_nested_serialization(self):
        """
        Test serialization/deserialization for Nested
        """

        # Construct a json representation of a Nested model
        nested_model_json = {}
        nested_model_json['type'] = 'nested'
        nested_model_json['matching_results'] = 38
        nested_model_json['path'] = 'testString'

        # Construct a model instance of Nested by calling from_dict on the json representation
        nested_model = Nested.from_dict(nested_model_json)
        assert nested_model != False

        # Construct a model instance of Nested by calling from_dict on the json representation
        nested_model_dict = Nested.from_dict(nested_model_json).__dict__
        nested_model2 = Nested(**nested_model_dict)

        # Verify the model instances are equivalent
        assert nested_model == nested_model2

        # Convert model instance back to dict and verify no loss of data
        nested_model_json2 = nested_model.to_dict()
        assert nested_model_json2 == nested_model_json

class TestModel_Term():
    """
    Test Class for Term
    """

    def test_term_serialization(self):
        """
        Test serialization/deserialization for Term
        """

        # Construct a json representation of a Term model
        term_model_json = {}
        term_model_json['type'] = 'term'
        term_model_json['matching_results'] = 38
        term_model_json['field'] = 'testString'
        term_model_json['count'] = 38

        # Construct a model instance of Term by calling from_dict on the json representation
        term_model = Term.from_dict(term_model_json)
        assert term_model != False

        # Construct a model instance of Term by calling from_dict on the json representation
        term_model_dict = Term.from_dict(term_model_json).__dict__
        term_model2 = Term(**term_model_dict)

        # Verify the model instances are equivalent
        assert term_model == term_model2

        # Convert model instance back to dict and verify no loss of data
        term_model_json2 = term_model.to_dict()
        assert term_model_json2 == term_model_json

class TestModel_Timeslice():
    """
    Test Class for Timeslice
    """

    def test_timeslice_serialization(self):
        """
        Test serialization/deserialization for Timeslice
        """

        # Construct a json representation of a Timeslice model
        timeslice_model_json = {}
        timeslice_model_json['type'] = 'timeslice'
        timeslice_model_json['matching_results'] = 38
        timeslice_model_json['field'] = 'testString'
        timeslice_model_json['interval'] = 'testString'
        timeslice_model_json['anomaly'] = True

        # Construct a model instance of Timeslice by calling from_dict on the json representation
        timeslice_model = Timeslice.from_dict(timeslice_model_json)
        assert timeslice_model != False

        # Construct a model instance of Timeslice by calling from_dict on the json representation
        timeslice_model_dict = Timeslice.from_dict(timeslice_model_json).__dict__
        timeslice_model2 = Timeslice(**timeslice_model_dict)

        # Verify the model instances are equivalent
        assert timeslice_model == timeslice_model2

        # Convert model instance back to dict and verify no loss of data
        timeslice_model_json2 = timeslice_model.to_dict()
        assert timeslice_model_json2 == timeslice_model_json

class TestModel_TopHits():
    """
    Test Class for TopHits
    """

    def test_top_hits_serialization(self):
        """
        Test serialization/deserialization for TopHits
        """

        # Construct dict forms of any model objects needed in order to build this model.

        query_result_metadata_model = {} # QueryResultMetadata
        query_result_metadata_model['score'] = 72.5
        query_result_metadata_model['confidence'] = 72.5

        query_result_model = {} # QueryResult
        query_result_model['id'] = 'testString'
        query_result_model['metadata'] = {}
        query_result_model['collection_id'] = 'testString'
        query_result_model['result_metadata'] = query_result_metadata_model
        query_result_model['foo'] = { 'foo': 'bar' }

        top_hits_results_model = {} # TopHitsResults
        top_hits_results_model['matching_results'] = 38
        top_hits_results_model['hits'] = [query_result_model]

        # Construct a json representation of a TopHits model
        top_hits_model_json = {}
        top_hits_model_json['type'] = 'top_hits'
        top_hits_model_json['matching_results'] = 38
        top_hits_model_json['size'] = 38
        top_hits_model_json['hits'] = top_hits_results_model

        # Construct a model instance of TopHits by calling from_dict on the json representation
        top_hits_model = TopHits.from_dict(top_hits_model_json)
        assert top_hits_model != False

        # Construct a model instance of TopHits by calling from_dict on the json representation
        top_hits_model_dict = TopHits.from_dict(top_hits_model_json).__dict__
        top_hits_model2 = TopHits(**top_hits_model_dict)

        # Verify the model instances are equivalent
        assert top_hits_model == top_hits_model2

        # Convert model instance back to dict and verify no loss of data
        top_hits_model_json2 = top_hits_model.to_dict()
        assert top_hits_model_json2 == top_hits_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
