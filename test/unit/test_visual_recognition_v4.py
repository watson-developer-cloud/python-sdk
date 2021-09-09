# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2019, 2021.
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
Unit Tests for VisualRecognitionV4
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
from ibm_watson.visual_recognition_v4 import *

version = 'testString'

_service = VisualRecognitionV4(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.visual-recognition.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Analysis
##############################################################################
# region

class TestAnalyze():
    """
    Test Class for analyze
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
    def test_analyze_all_params(self):
        """
        analyze()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/analyze')
        mock_response = '{"images": [{"source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "objects": {"collections": [{"collection_id": "collection_id", "objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}, "score": 5}]}]}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}]}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FileWithMetadata model
        file_with_metadata_model = {}
        file_with_metadata_model['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model['filename'] = 'testString'
        file_with_metadata_model['content_type'] = 'testString'

        # Set up parameter values
        collection_ids = ['testString']
        features = ['objects']
        images_file = [file_with_metadata_model]
        image_url = ['testString']
        threshold = 0.15

        # Invoke method
        response = _service.analyze(
            collection_ids,
            features,
            images_file=images_file,
            image_url=image_url,
            threshold=threshold,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_analyze_required_params(self):
        """
        test_analyze_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/analyze')
        mock_response = '{"images": [{"source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "objects": {"collections": [{"collection_id": "collection_id", "objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}, "score": 5}]}]}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}]}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_ids = ['testString']
        features = ['objects']

        # Invoke method
        response = _service.analyze(
            collection_ids,
            features,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_analyze_value_error(self):
        """
        test_analyze_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/analyze')
        mock_response = '{"images": [{"source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "objects": {"collections": [{"collection_id": "collection_id", "objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}, "score": 5}]}]}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}]}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_ids = ['testString']
        features = ['objects']

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_ids": collection_ids,
            "features": features,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.analyze(**req_copy)



# endregion
##############################################################################
# End of Service: Analysis
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
        url = self.preprocess_url(_base_url + '/v4/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ObjectTrainingStatus model
        object_training_status_model = {}
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        # Construct a dict representation of a TrainingStatus model
        training_status_model = {}
        training_status_model['objects'] = object_training_status_model

        # Set up parameter values
        name = 'testString'
        description = 'testString'
        training_status = training_status_model

        # Invoke method
        response = _service.create_collection(
            name=name,
            description=description,
            training_status=training_status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['training_status'] == training_status_model


    @responses.activate
    def test_create_collection_value_error(self):
        """
        test_create_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ObjectTrainingStatus model
        object_training_status_model = {}
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        # Construct a dict representation of a TrainingStatus model
        training_status_model = {}
        training_status_model['objects'] = object_training_status_model

        # Set up parameter values
        name = 'testString'
        description = 'testString'
        training_status = training_status_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = self.preprocess_url(_base_url + '/v4/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_collections()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_collections_value_error(self):
        """
        test_list_collections_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections')
        mock_response = '{"collections": [{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}]}'
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
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.get_collection(
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
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
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
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ObjectTrainingStatus model
        object_training_status_model = {}
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        # Construct a dict representation of a TrainingStatus model
        training_status_model = {}
        training_status_model['objects'] = object_training_status_model

        # Set up parameter values
        collection_id = 'testString'
        name = 'testString'
        description = 'testString'
        training_status = training_status_model

        # Invoke method
        response = _service.update_collection(
            collection_id,
            name=name,
            description=description,
            training_status=training_status,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['training_status'] == training_status_model


    @responses.activate
    def test_update_collection_required_params(self):
        """
        test_update_collection_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.update_collection(
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_update_collection_value_error(self):
        """
        test_update_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
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
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.delete_collection(
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
        url = self.preprocess_url(_base_url + '/v4/collections/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_collection(**req_copy)



class TestGetModelFile():
    """
    Test Class for get_model_file
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
    def test_get_model_file_all_params(self):
        """
        get_model_file()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/model')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        feature = 'objects'
        model_format = 'rscnn'

        # Invoke method
        response = _service.get_model_file(
            collection_id,
            feature,
            model_format,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'feature={}'.format(feature) in query_string
        assert 'model_format={}'.format(model_format) in query_string


    @responses.activate
    def test_get_model_file_value_error(self):
        """
        test_get_model_file_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/model')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/octet-stream',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        feature = 'objects'
        model_format = 'rscnn'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "feature": feature,
            "model_format": model_format,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_model_file(**req_copy)



# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: Images
##############################################################################
# region

class TestAddImages():
    """
    Test Class for add_images
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
    def test_add_images_all_params(self):
        """
        add_images()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images')
        mock_response = '{"images": [{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}], "training_data": {"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a FileWithMetadata model
        file_with_metadata_model = {}
        file_with_metadata_model['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model['filename'] = 'testString'
        file_with_metadata_model['content_type'] = 'testString'

        # Set up parameter values
        collection_id = 'testString'
        images_file = [file_with_metadata_model]
        image_url = ['testString']
        training_data = '{"objects":[{"object":"2018-Fit","location":{"left":33,"top":8,"width":760,"height":419}}]}'

        # Invoke method
        response = _service.add_images(
            collection_id,
            images_file=images_file,
            image_url=image_url,
            training_data=training_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_add_images_required_params(self):
        """
        test_add_images_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images')
        mock_response = '{"images": [{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}], "training_data": {"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.add_images(
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_add_images_value_error(self):
        """
        test_add_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images')
        mock_response = '{"images": [{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}], "training_data": {"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}}], "warnings": [{"code": "invalid_field", "message": "message", "more_info": "more_info"}], "trace": "trace"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_images(**req_copy)



class TestListImages():
    """
    Test Class for list_images
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
    def test_list_images_all_params(self):
        """
        list_images()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images')
        mock_response = '{"images": [{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.list_images(
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_images_value_error(self):
        """
        test_list_images_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images')
        mock_response = '{"images": [{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_images(**req_copy)



class TestGetImageDetails():
    """
    Test Class for get_image_details
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
    def test_get_image_details_all_params(self):
        """
        get_image_details()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString')
        mock_response = '{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}], "training_data": {"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Invoke method
        response = _service.get_image_details(
            collection_id,
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_image_details_value_error(self):
        """
        test_get_image_details_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString')
        mock_response = '{"image_id": "image_id", "updated": "2019-01-01T12:00:00.000Z", "created": "2019-01-01T12:00:00.000Z", "source": {"type": "file", "filename": "filename", "archive_filename": "archive_filename", "source_url": "source_url", "resolved_url": "resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [{"code": "invalid_field", "message": "message", "more_info": "more_info", "target": {"type": "field", "name": "name"}}], "training_data": {"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_image_details(**req_copy)



class TestDeleteImage():
    """
    Test Class for delete_image
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
    def test_delete_image_all_params(self):
        """
        delete_image()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Invoke method
        response = _service.delete_image(
            collection_id,
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_image_value_error(self):
        """
        test_delete_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_image(**req_copy)



class TestGetJpegImage():
    """
    Test Class for get_jpeg_image
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
    def test_get_jpeg_image_all_params(self):
        """
        get_jpeg_image()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString/jpeg')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='image/jpeg',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'
        size = 'full'

        # Invoke method
        response = _service.get_jpeg_image(
            collection_id,
            image_id,
            size=size,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'size={}'.format(size) in query_string


    @responses.activate
    def test_get_jpeg_image_required_params(self):
        """
        test_get_jpeg_image_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString/jpeg')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='image/jpeg',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Invoke method
        response = _service.get_jpeg_image(
            collection_id,
            image_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_jpeg_image_value_error(self):
        """
        test_get_jpeg_image_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString/jpeg')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='image/jpeg',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_jpeg_image(**req_copy)



# endregion
##############################################################################
# End of Service: Images
##############################################################################

##############################################################################
# Start of Service: Objects
##############################################################################
# region

class TestListObjectMetadata():
    """
    Test Class for list_object_metadata
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
    def test_list_object_metadata_all_params(self):
        """
        list_object_metadata()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects')
        mock_response = '{"object_count": 12, "objects": [{"object": "object", "count": 5}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.list_object_metadata(
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_object_metadata_value_error(self):
        """
        test_list_object_metadata_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects')
        mock_response = '{"object_count": 12, "objects": [{"object": "object", "count": 5}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_object_metadata(**req_copy)



class TestUpdateObjectMetadata():
    """
    Test Class for update_object_metadata
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
    def test_update_object_metadata_all_params(self):
        """
        update_object_metadata()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        mock_response = '{"object": "object", "count": 5}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'
        new_object = 'testString'

        # Invoke method
        response = _service.update_object_metadata(
            collection_id,
            object,
            new_object,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['object'] == 'testString'


    @responses.activate
    def test_update_object_metadata_value_error(self):
        """
        test_update_object_metadata_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        mock_response = '{"object": "object", "count": 5}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'
        new_object = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "object": object,
            "new_object": new_object,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_object_metadata(**req_copy)



class TestGetObjectMetadata():
    """
    Test Class for get_object_metadata
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
    def test_get_object_metadata_all_params(self):
        """
        get_object_metadata()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        mock_response = '{"object": "object", "count": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'

        # Invoke method
        response = _service.get_object_metadata(
            collection_id,
            object,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_object_metadata_value_error(self):
        """
        test_get_object_metadata_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        mock_response = '{"object": "object", "count": 5}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "object": object,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_object_metadata(**req_copy)



class TestDeleteObject():
    """
    Test Class for delete_object
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
    def test_delete_object_all_params(self):
        """
        delete_object()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'

        # Invoke method
        response = _service.delete_object(
            collection_id,
            object,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_object_value_error(self):
        """
        test_delete_object_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/objects/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        collection_id = 'testString'
        object = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "object": object,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_object(**req_copy)



# endregion
##############################################################################
# End of Service: Objects
##############################################################################

##############################################################################
# Start of Service: Training
##############################################################################
# region

class TestTrain():
    """
    Test Class for train
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
    def test_train_all_params(self):
        """
        train()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/train')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        collection_id = 'testString'

        # Invoke method
        response = _service.train(
            collection_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_train_value_error(self):
        """
        test_train_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/train')
        mock_response = '{"collection_id": "collection_id", "name": "name", "description": "description", "created": "2019-01-01T12:00:00.000Z", "updated": "2019-01-01T12:00:00.000Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "rscnn_ready": false, "description": "description"}}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        collection_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.train(**req_copy)



class TestAddImageTrainingData():
    """
    Test Class for add_image_training_data
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
    def test_add_image_training_data_all_params(self):
        """
        add_image_training_data()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString/training_data')
        mock_response = '{"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Location model
        location_model = {}
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        # Construct a dict representation of a TrainingDataObject model
        training_data_object_model = {}
        training_data_object_model['object'] = 'testString'
        training_data_object_model['location'] = location_model

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'
        objects = [training_data_object_model]

        # Invoke method
        response = _service.add_image_training_data(
            collection_id,
            image_id,
            objects=objects,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['objects'] == [training_data_object_model]


    @responses.activate
    def test_add_image_training_data_value_error(self):
        """
        test_add_image_training_data_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/collections/testString/images/testString/training_data')
        mock_response = '{"objects": [{"object": "object", "location": {"top": 3, "left": 4, "width": 5, "height": 6}}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Location model
        location_model = {}
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        # Construct a dict representation of a TrainingDataObject model
        training_data_object_model = {}
        training_data_object_model['object'] = 'testString'
        training_data_object_model['location'] = location_model

        # Set up parameter values
        collection_id = 'testString'
        image_id = 'testString'
        objects = [training_data_object_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "collection_id": collection_id,
            "image_id": image_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_image_training_data(**req_copy)



class TestGetTrainingUsage():
    """
    Test Class for get_training_usage
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
    def test_get_training_usage_all_params(self):
        """
        get_training_usage()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/training_usage')
        mock_response = '{"start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "completed_events": 16, "trained_images": 14, "events": [{"type": "objects", "collection_id": "collection_id", "completion_time": "2019-01-01T12:00:00.000Z", "status": "failed", "image_count": 11}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        start_time = string_to_date('2019-01-01')
        end_time = string_to_date('2019-01-01')

        # Invoke method
        response = _service.get_training_usage(
            start_time=start_time,
            end_time=end_time,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'start_time={}'.format(date_to_string(start_time)) in query_string
        assert 'end_time={}'.format(date_to_string(end_time)) in query_string


    @responses.activate
    def test_get_training_usage_required_params(self):
        """
        test_get_training_usage_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/training_usage')
        mock_response = '{"start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "completed_events": 16, "trained_images": 14, "events": [{"type": "objects", "collection_id": "collection_id", "completion_time": "2019-01-01T12:00:00.000Z", "status": "failed", "image_count": 11}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.get_training_usage()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_training_usage_value_error(self):
        """
        test_get_training_usage_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v4/training_usage')
        mock_response = '{"start_time": "2019-01-01T12:00:00.000Z", "end_time": "2019-01-01T12:00:00.000Z", "completed_events": 16, "trained_images": 14, "events": [{"type": "objects", "collection_id": "collection_id", "completion_time": "2019-01-01T12:00:00.000Z", "status": "failed", "image_count": 11}]}'
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
                _service.get_training_usage(**req_copy)



# endregion
##############################################################################
# End of Service: Training
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
        url = self.preprocess_url(_base_url + '/v4/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        customer_id = 'testString'

        # Invoke method
        response = _service.delete_user_data(
            customer_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
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
        url = self.preprocess_url(_base_url + '/v4/user_data')
        responses.add(responses.DELETE,
                      url,
                      status=202)

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
# Start of Model Tests
##############################################################################
# region
class TestModel_AnalyzeResponse():
    """
    Test Class for AnalyzeResponse
    """

    def test_analyze_response_serialization(self):
        """
        Test serialization/deserialization for AnalyzeResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_source_model = {} # ImageSource
        image_source_model['type'] = 'file'
        image_source_model['filename'] = 'testString'
        image_source_model['archive_filename'] = 'testString'
        image_source_model['source_url'] = 'testString'
        image_source_model['resolved_url'] = 'testString'

        image_dimensions_model = {} # ImageDimensions
        image_dimensions_model['height'] = 38
        image_dimensions_model['width'] = 38

        object_detail_location_model = {} # ObjectDetailLocation
        object_detail_location_model['top'] = 38
        object_detail_location_model['left'] = 38
        object_detail_location_model['width'] = 38
        object_detail_location_model['height'] = 38

        object_detail_model = {} # ObjectDetail
        object_detail_model['object'] = 'testString'
        object_detail_model['location'] = object_detail_location_model
        object_detail_model['score'] = 72.5

        collection_objects_model = {} # CollectionObjects
        collection_objects_model['collection_id'] = 'testString'
        collection_objects_model['objects'] = [object_detail_model]

        detected_objects_model = {} # DetectedObjects
        detected_objects_model['collections'] = [collection_objects_model]

        error_target_model = {} # ErrorTarget
        error_target_model['type'] = 'field'
        error_target_model['name'] = 'testString'

        error_model = {} # Error
        error_model['code'] = 'invalid_field'
        error_model['message'] = 'testString'
        error_model['more_info'] = 'testString'
        error_model['target'] = error_target_model

        image_model = {} # Image
        image_model['source'] = image_source_model
        image_model['dimensions'] = image_dimensions_model
        image_model['objects'] = detected_objects_model
        image_model['errors'] = [error_model]

        warning_model = {} # Warning
        warning_model['code'] = 'invalid_field'
        warning_model['message'] = 'testString'
        warning_model['more_info'] = 'testString'

        # Construct a json representation of a AnalyzeResponse model
        analyze_response_model_json = {}
        analyze_response_model_json['images'] = [image_model]
        analyze_response_model_json['warnings'] = [warning_model]
        analyze_response_model_json['trace'] = 'testString'

        # Construct a model instance of AnalyzeResponse by calling from_dict on the json representation
        analyze_response_model = AnalyzeResponse.from_dict(analyze_response_model_json)
        assert analyze_response_model != False

        # Construct a model instance of AnalyzeResponse by calling from_dict on the json representation
        analyze_response_model_dict = AnalyzeResponse.from_dict(analyze_response_model_json).__dict__
        analyze_response_model2 = AnalyzeResponse(**analyze_response_model_dict)

        # Verify the model instances are equivalent
        assert analyze_response_model == analyze_response_model2

        # Convert model instance back to dict and verify no loss of data
        analyze_response_model_json2 = analyze_response_model.to_dict()
        assert analyze_response_model_json2 == analyze_response_model_json

class TestModel_Collection():
    """
    Test Class for Collection
    """

    def test_collection_serialization(self):
        """
        Test serialization/deserialization for Collection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_training_status_model = {} # ObjectTrainingStatus
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        collection_training_status_model = {} # CollectionTrainingStatus
        collection_training_status_model['objects'] = object_training_status_model

        # Construct a json representation of a Collection model
        collection_model_json = {}
        collection_model_json['collection_id'] = 'testString'
        collection_model_json['name'] = 'testString'
        collection_model_json['description'] = 'testString'
        collection_model_json['created'] = "2019-01-01T12:00:00Z"
        collection_model_json['updated'] = "2019-01-01T12:00:00Z"
        collection_model_json['image_count'] = 38
        collection_model_json['training_status'] = collection_training_status_model

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

class TestModel_CollectionObjects():
    """
    Test Class for CollectionObjects
    """

    def test_collection_objects_serialization(self):
        """
        Test serialization/deserialization for CollectionObjects
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_detail_location_model = {} # ObjectDetailLocation
        object_detail_location_model['top'] = 38
        object_detail_location_model['left'] = 38
        object_detail_location_model['width'] = 38
        object_detail_location_model['height'] = 38

        object_detail_model = {} # ObjectDetail
        object_detail_model['object'] = 'testString'
        object_detail_model['location'] = object_detail_location_model
        object_detail_model['score'] = 72.5

        # Construct a json representation of a CollectionObjects model
        collection_objects_model_json = {}
        collection_objects_model_json['collection_id'] = 'testString'
        collection_objects_model_json['objects'] = [object_detail_model]

        # Construct a model instance of CollectionObjects by calling from_dict on the json representation
        collection_objects_model = CollectionObjects.from_dict(collection_objects_model_json)
        assert collection_objects_model != False

        # Construct a model instance of CollectionObjects by calling from_dict on the json representation
        collection_objects_model_dict = CollectionObjects.from_dict(collection_objects_model_json).__dict__
        collection_objects_model2 = CollectionObjects(**collection_objects_model_dict)

        # Verify the model instances are equivalent
        assert collection_objects_model == collection_objects_model2

        # Convert model instance back to dict and verify no loss of data
        collection_objects_model_json2 = collection_objects_model.to_dict()
        assert collection_objects_model_json2 == collection_objects_model_json

class TestModel_CollectionTrainingStatus():
    """
    Test Class for CollectionTrainingStatus
    """

    def test_collection_training_status_serialization(self):
        """
        Test serialization/deserialization for CollectionTrainingStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_training_status_model = {} # ObjectTrainingStatus
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        # Construct a json representation of a CollectionTrainingStatus model
        collection_training_status_model_json = {}
        collection_training_status_model_json['objects'] = object_training_status_model

        # Construct a model instance of CollectionTrainingStatus by calling from_dict on the json representation
        collection_training_status_model = CollectionTrainingStatus.from_dict(collection_training_status_model_json)
        assert collection_training_status_model != False

        # Construct a model instance of CollectionTrainingStatus by calling from_dict on the json representation
        collection_training_status_model_dict = CollectionTrainingStatus.from_dict(collection_training_status_model_json).__dict__
        collection_training_status_model2 = CollectionTrainingStatus(**collection_training_status_model_dict)

        # Verify the model instances are equivalent
        assert collection_training_status_model == collection_training_status_model2

        # Convert model instance back to dict and verify no loss of data
        collection_training_status_model_json2 = collection_training_status_model.to_dict()
        assert collection_training_status_model_json2 == collection_training_status_model_json

class TestModel_CollectionsList():
    """
    Test Class for CollectionsList
    """

    def test_collections_list_serialization(self):
        """
        Test serialization/deserialization for CollectionsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_training_status_model = {} # ObjectTrainingStatus
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        collection_training_status_model = {} # CollectionTrainingStatus
        collection_training_status_model['objects'] = object_training_status_model

        collection_model = {} # Collection
        collection_model['collection_id'] = 'testString'
        collection_model['name'] = 'testString'
        collection_model['description'] = 'testString'
        collection_model['created'] = "2019-01-01T12:00:00Z"
        collection_model['updated'] = "2019-01-01T12:00:00Z"
        collection_model['image_count'] = 38
        collection_model['training_status'] = collection_training_status_model

        # Construct a json representation of a CollectionsList model
        collections_list_model_json = {}
        collections_list_model_json['collections'] = [collection_model]

        # Construct a model instance of CollectionsList by calling from_dict on the json representation
        collections_list_model = CollectionsList.from_dict(collections_list_model_json)
        assert collections_list_model != False

        # Construct a model instance of CollectionsList by calling from_dict on the json representation
        collections_list_model_dict = CollectionsList.from_dict(collections_list_model_json).__dict__
        collections_list_model2 = CollectionsList(**collections_list_model_dict)

        # Verify the model instances are equivalent
        assert collections_list_model == collections_list_model2

        # Convert model instance back to dict and verify no loss of data
        collections_list_model_json2 = collections_list_model.to_dict()
        assert collections_list_model_json2 == collections_list_model_json

class TestModel_DetectedObjects():
    """
    Test Class for DetectedObjects
    """

    def test_detected_objects_serialization(self):
        """
        Test serialization/deserialization for DetectedObjects
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_detail_location_model = {} # ObjectDetailLocation
        object_detail_location_model['top'] = 38
        object_detail_location_model['left'] = 38
        object_detail_location_model['width'] = 38
        object_detail_location_model['height'] = 38

        object_detail_model = {} # ObjectDetail
        object_detail_model['object'] = 'testString'
        object_detail_model['location'] = object_detail_location_model
        object_detail_model['score'] = 72.5

        collection_objects_model = {} # CollectionObjects
        collection_objects_model['collection_id'] = 'testString'
        collection_objects_model['objects'] = [object_detail_model]

        # Construct a json representation of a DetectedObjects model
        detected_objects_model_json = {}
        detected_objects_model_json['collections'] = [collection_objects_model]

        # Construct a model instance of DetectedObjects by calling from_dict on the json representation
        detected_objects_model = DetectedObjects.from_dict(detected_objects_model_json)
        assert detected_objects_model != False

        # Construct a model instance of DetectedObjects by calling from_dict on the json representation
        detected_objects_model_dict = DetectedObjects.from_dict(detected_objects_model_json).__dict__
        detected_objects_model2 = DetectedObjects(**detected_objects_model_dict)

        # Verify the model instances are equivalent
        assert detected_objects_model == detected_objects_model2

        # Convert model instance back to dict and verify no loss of data
        detected_objects_model_json2 = detected_objects_model.to_dict()
        assert detected_objects_model_json2 == detected_objects_model_json

class TestModel_Error():
    """
    Test Class for Error
    """

    def test_error_serialization(self):
        """
        Test serialization/deserialization for Error
        """

        # Construct dict forms of any model objects needed in order to build this model.

        error_target_model = {} # ErrorTarget
        error_target_model['type'] = 'parameter'
        error_target_model['name'] = 'version'

        # Construct a json representation of a Error model
        error_model_json = {}
        error_model_json['code'] = 'invalid_field'
        error_model_json['message'] = 'testString'
        error_model_json['more_info'] = 'testString'
        error_model_json['target'] = error_target_model

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model = Error.from_dict(error_model_json)
        assert error_model != False

        # Construct a model instance of Error by calling from_dict on the json representation
        error_model_dict = Error.from_dict(error_model_json).__dict__
        error_model2 = Error(**error_model_dict)

        # Verify the model instances are equivalent
        assert error_model == error_model2

        # Convert model instance back to dict and verify no loss of data
        error_model_json2 = error_model.to_dict()
        assert error_model_json2 == error_model_json

class TestModel_ErrorTarget():
    """
    Test Class for ErrorTarget
    """

    def test_error_target_serialization(self):
        """
        Test serialization/deserialization for ErrorTarget
        """

        # Construct a json representation of a ErrorTarget model
        error_target_model_json = {}
        error_target_model_json['type'] = 'field'
        error_target_model_json['name'] = 'testString'

        # Construct a model instance of ErrorTarget by calling from_dict on the json representation
        error_target_model = ErrorTarget.from_dict(error_target_model_json)
        assert error_target_model != False

        # Construct a model instance of ErrorTarget by calling from_dict on the json representation
        error_target_model_dict = ErrorTarget.from_dict(error_target_model_json).__dict__
        error_target_model2 = ErrorTarget(**error_target_model_dict)

        # Verify the model instances are equivalent
        assert error_target_model == error_target_model2

        # Convert model instance back to dict and verify no loss of data
        error_target_model_json2 = error_target_model.to_dict()
        assert error_target_model_json2 == error_target_model_json

class TestModel_Image():
    """
    Test Class for Image
    """

    def test_image_serialization(self):
        """
        Test serialization/deserialization for Image
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_source_model = {} # ImageSource
        image_source_model['type'] = 'file'
        image_source_model['filename'] = 'testString'
        image_source_model['archive_filename'] = 'testString'
        image_source_model['source_url'] = 'testString'
        image_source_model['resolved_url'] = 'testString'

        image_dimensions_model = {} # ImageDimensions
        image_dimensions_model['height'] = 38
        image_dimensions_model['width'] = 38

        object_detail_location_model = {} # ObjectDetailLocation
        object_detail_location_model['top'] = 38
        object_detail_location_model['left'] = 38
        object_detail_location_model['width'] = 38
        object_detail_location_model['height'] = 38

        object_detail_model = {} # ObjectDetail
        object_detail_model['object'] = 'testString'
        object_detail_model['location'] = object_detail_location_model
        object_detail_model['score'] = 72.5

        collection_objects_model = {} # CollectionObjects
        collection_objects_model['collection_id'] = 'testString'
        collection_objects_model['objects'] = [object_detail_model]

        detected_objects_model = {} # DetectedObjects
        detected_objects_model['collections'] = [collection_objects_model]

        error_target_model = {} # ErrorTarget
        error_target_model['type'] = 'field'
        error_target_model['name'] = 'testString'

        error_model = {} # Error
        error_model['code'] = 'invalid_field'
        error_model['message'] = 'testString'
        error_model['more_info'] = 'testString'
        error_model['target'] = error_target_model

        # Construct a json representation of a Image model
        image_model_json = {}
        image_model_json['source'] = image_source_model
        image_model_json['dimensions'] = image_dimensions_model
        image_model_json['objects'] = detected_objects_model
        image_model_json['errors'] = [error_model]

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model = Image.from_dict(image_model_json)
        assert image_model != False

        # Construct a model instance of Image by calling from_dict on the json representation
        image_model_dict = Image.from_dict(image_model_json).__dict__
        image_model2 = Image(**image_model_dict)

        # Verify the model instances are equivalent
        assert image_model == image_model2

        # Convert model instance back to dict and verify no loss of data
        image_model_json2 = image_model.to_dict()
        assert image_model_json2 == image_model_json

class TestModel_ImageDetails():
    """
    Test Class for ImageDetails
    """

    def test_image_details_serialization(self):
        """
        Test serialization/deserialization for ImageDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_source_model = {} # ImageSource
        image_source_model['type'] = 'file'
        image_source_model['filename'] = 'testString'
        image_source_model['archive_filename'] = 'testString'
        image_source_model['source_url'] = 'testString'
        image_source_model['resolved_url'] = 'testString'

        image_dimensions_model = {} # ImageDimensions
        image_dimensions_model['height'] = 38
        image_dimensions_model['width'] = 38

        error_target_model = {} # ErrorTarget
        error_target_model['type'] = 'field'
        error_target_model['name'] = 'testString'

        error_model = {} # Error
        error_model['code'] = 'invalid_field'
        error_model['message'] = 'testString'
        error_model['more_info'] = 'testString'
        error_model['target'] = error_target_model

        location_model = {} # Location
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        training_data_object_model = {} # TrainingDataObject
        training_data_object_model['object'] = 'testString'
        training_data_object_model['location'] = location_model

        training_data_objects_model = {} # TrainingDataObjects
        training_data_objects_model['objects'] = [training_data_object_model]

        # Construct a json representation of a ImageDetails model
        image_details_model_json = {}
        image_details_model_json['image_id'] = 'testString'
        image_details_model_json['updated'] = "2019-01-01T12:00:00Z"
        image_details_model_json['created'] = "2019-01-01T12:00:00Z"
        image_details_model_json['source'] = image_source_model
        image_details_model_json['dimensions'] = image_dimensions_model
        image_details_model_json['errors'] = [error_model]
        image_details_model_json['training_data'] = training_data_objects_model

        # Construct a model instance of ImageDetails by calling from_dict on the json representation
        image_details_model = ImageDetails.from_dict(image_details_model_json)
        assert image_details_model != False

        # Construct a model instance of ImageDetails by calling from_dict on the json representation
        image_details_model_dict = ImageDetails.from_dict(image_details_model_json).__dict__
        image_details_model2 = ImageDetails(**image_details_model_dict)

        # Verify the model instances are equivalent
        assert image_details_model == image_details_model2

        # Convert model instance back to dict and verify no loss of data
        image_details_model_json2 = image_details_model.to_dict()
        assert image_details_model_json2 == image_details_model_json

class TestModel_ImageDetailsList():
    """
    Test Class for ImageDetailsList
    """

    def test_image_details_list_serialization(self):
        """
        Test serialization/deserialization for ImageDetailsList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_source_model = {} # ImageSource
        image_source_model['type'] = 'file'
        image_source_model['filename'] = 'testString'
        image_source_model['archive_filename'] = 'testString'
        image_source_model['source_url'] = 'testString'
        image_source_model['resolved_url'] = 'testString'

        image_dimensions_model = {} # ImageDimensions
        image_dimensions_model['height'] = 38
        image_dimensions_model['width'] = 38

        error_target_model = {} # ErrorTarget
        error_target_model['type'] = 'field'
        error_target_model['name'] = 'testString'

        error_model = {} # Error
        error_model['code'] = 'invalid_field'
        error_model['message'] = 'testString'
        error_model['more_info'] = 'testString'
        error_model['target'] = error_target_model

        location_model = {} # Location
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        training_data_object_model = {} # TrainingDataObject
        training_data_object_model['object'] = 'testString'
        training_data_object_model['location'] = location_model

        training_data_objects_model = {} # TrainingDataObjects
        training_data_objects_model['objects'] = [training_data_object_model]

        image_details_model = {} # ImageDetails
        image_details_model['image_id'] = 'testString'
        image_details_model['updated'] = "2019-01-01T12:00:00Z"
        image_details_model['created'] = "2019-01-01T12:00:00Z"
        image_details_model['source'] = image_source_model
        image_details_model['dimensions'] = image_dimensions_model
        image_details_model['errors'] = [error_model]
        image_details_model['training_data'] = training_data_objects_model

        warning_model = {} # Warning
        warning_model['code'] = 'invalid_field'
        warning_model['message'] = 'testString'
        warning_model['more_info'] = 'testString'

        # Construct a json representation of a ImageDetailsList model
        image_details_list_model_json = {}
        image_details_list_model_json['images'] = [image_details_model]
        image_details_list_model_json['warnings'] = [warning_model]
        image_details_list_model_json['trace'] = 'testString'

        # Construct a model instance of ImageDetailsList by calling from_dict on the json representation
        image_details_list_model = ImageDetailsList.from_dict(image_details_list_model_json)
        assert image_details_list_model != False

        # Construct a model instance of ImageDetailsList by calling from_dict on the json representation
        image_details_list_model_dict = ImageDetailsList.from_dict(image_details_list_model_json).__dict__
        image_details_list_model2 = ImageDetailsList(**image_details_list_model_dict)

        # Verify the model instances are equivalent
        assert image_details_list_model == image_details_list_model2

        # Convert model instance back to dict and verify no loss of data
        image_details_list_model_json2 = image_details_list_model.to_dict()
        assert image_details_list_model_json2 == image_details_list_model_json

class TestModel_ImageDimensions():
    """
    Test Class for ImageDimensions
    """

    def test_image_dimensions_serialization(self):
        """
        Test serialization/deserialization for ImageDimensions
        """

        # Construct a json representation of a ImageDimensions model
        image_dimensions_model_json = {}
        image_dimensions_model_json['height'] = 38
        image_dimensions_model_json['width'] = 38

        # Construct a model instance of ImageDimensions by calling from_dict on the json representation
        image_dimensions_model = ImageDimensions.from_dict(image_dimensions_model_json)
        assert image_dimensions_model != False

        # Construct a model instance of ImageDimensions by calling from_dict on the json representation
        image_dimensions_model_dict = ImageDimensions.from_dict(image_dimensions_model_json).__dict__
        image_dimensions_model2 = ImageDimensions(**image_dimensions_model_dict)

        # Verify the model instances are equivalent
        assert image_dimensions_model == image_dimensions_model2

        # Convert model instance back to dict and verify no loss of data
        image_dimensions_model_json2 = image_dimensions_model.to_dict()
        assert image_dimensions_model_json2 == image_dimensions_model_json

class TestModel_ImageSource():
    """
    Test Class for ImageSource
    """

    def test_image_source_serialization(self):
        """
        Test serialization/deserialization for ImageSource
        """

        # Construct a json representation of a ImageSource model
        image_source_model_json = {}
        image_source_model_json['type'] = 'file'
        image_source_model_json['filename'] = 'testString'
        image_source_model_json['archive_filename'] = 'testString'
        image_source_model_json['source_url'] = 'testString'
        image_source_model_json['resolved_url'] = 'testString'

        # Construct a model instance of ImageSource by calling from_dict on the json representation
        image_source_model = ImageSource.from_dict(image_source_model_json)
        assert image_source_model != False

        # Construct a model instance of ImageSource by calling from_dict on the json representation
        image_source_model_dict = ImageSource.from_dict(image_source_model_json).__dict__
        image_source_model2 = ImageSource(**image_source_model_dict)

        # Verify the model instances are equivalent
        assert image_source_model == image_source_model2

        # Convert model instance back to dict and verify no loss of data
        image_source_model_json2 = image_source_model.to_dict()
        assert image_source_model_json2 == image_source_model_json

class TestModel_ImageSummary():
    """
    Test Class for ImageSummary
    """

    def test_image_summary_serialization(self):
        """
        Test serialization/deserialization for ImageSummary
        """

        # Construct a json representation of a ImageSummary model
        image_summary_model_json = {}
        image_summary_model_json['image_id'] = 'testString'
        image_summary_model_json['updated'] = "2019-01-01T12:00:00Z"

        # Construct a model instance of ImageSummary by calling from_dict on the json representation
        image_summary_model = ImageSummary.from_dict(image_summary_model_json)
        assert image_summary_model != False

        # Construct a model instance of ImageSummary by calling from_dict on the json representation
        image_summary_model_dict = ImageSummary.from_dict(image_summary_model_json).__dict__
        image_summary_model2 = ImageSummary(**image_summary_model_dict)

        # Verify the model instances are equivalent
        assert image_summary_model == image_summary_model2

        # Convert model instance back to dict and verify no loss of data
        image_summary_model_json2 = image_summary_model.to_dict()
        assert image_summary_model_json2 == image_summary_model_json

class TestModel_ImageSummaryList():
    """
    Test Class for ImageSummaryList
    """

    def test_image_summary_list_serialization(self):
        """
        Test serialization/deserialization for ImageSummaryList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        image_summary_model = {} # ImageSummary
        image_summary_model['image_id'] = 'testString'
        image_summary_model['updated'] = "2019-01-01T12:00:00Z"

        # Construct a json representation of a ImageSummaryList model
        image_summary_list_model_json = {}
        image_summary_list_model_json['images'] = [image_summary_model]

        # Construct a model instance of ImageSummaryList by calling from_dict on the json representation
        image_summary_list_model = ImageSummaryList.from_dict(image_summary_list_model_json)
        assert image_summary_list_model != False

        # Construct a model instance of ImageSummaryList by calling from_dict on the json representation
        image_summary_list_model_dict = ImageSummaryList.from_dict(image_summary_list_model_json).__dict__
        image_summary_list_model2 = ImageSummaryList(**image_summary_list_model_dict)

        # Verify the model instances are equivalent
        assert image_summary_list_model == image_summary_list_model2

        # Convert model instance back to dict and verify no loss of data
        image_summary_list_model_json2 = image_summary_list_model.to_dict()
        assert image_summary_list_model_json2 == image_summary_list_model_json

class TestModel_Location():
    """
    Test Class for Location
    """

    def test_location_serialization(self):
        """
        Test serialization/deserialization for Location
        """

        # Construct a json representation of a Location model
        location_model_json = {}
        location_model_json['top'] = 38
        location_model_json['left'] = 38
        location_model_json['width'] = 38
        location_model_json['height'] = 38

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model = Location.from_dict(location_model_json)
        assert location_model != False

        # Construct a model instance of Location by calling from_dict on the json representation
        location_model_dict = Location.from_dict(location_model_json).__dict__
        location_model2 = Location(**location_model_dict)

        # Verify the model instances are equivalent
        assert location_model == location_model2

        # Convert model instance back to dict and verify no loss of data
        location_model_json2 = location_model.to_dict()
        assert location_model_json2 == location_model_json

class TestModel_ObjectDetail():
    """
    Test Class for ObjectDetail
    """

    def test_object_detail_serialization(self):
        """
        Test serialization/deserialization for ObjectDetail
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_detail_location_model = {} # ObjectDetailLocation
        object_detail_location_model['top'] = 38
        object_detail_location_model['left'] = 38
        object_detail_location_model['width'] = 38
        object_detail_location_model['height'] = 38

        # Construct a json representation of a ObjectDetail model
        object_detail_model_json = {}
        object_detail_model_json['object'] = 'testString'
        object_detail_model_json['location'] = object_detail_location_model
        object_detail_model_json['score'] = 72.5

        # Construct a model instance of ObjectDetail by calling from_dict on the json representation
        object_detail_model = ObjectDetail.from_dict(object_detail_model_json)
        assert object_detail_model != False

        # Construct a model instance of ObjectDetail by calling from_dict on the json representation
        object_detail_model_dict = ObjectDetail.from_dict(object_detail_model_json).__dict__
        object_detail_model2 = ObjectDetail(**object_detail_model_dict)

        # Verify the model instances are equivalent
        assert object_detail_model == object_detail_model2

        # Convert model instance back to dict and verify no loss of data
        object_detail_model_json2 = object_detail_model.to_dict()
        assert object_detail_model_json2 == object_detail_model_json

class TestModel_ObjectDetailLocation():
    """
    Test Class for ObjectDetailLocation
    """

    def test_object_detail_location_serialization(self):
        """
        Test serialization/deserialization for ObjectDetailLocation
        """

        # Construct a json representation of a ObjectDetailLocation model
        object_detail_location_model_json = {}
        object_detail_location_model_json['top'] = 38
        object_detail_location_model_json['left'] = 38
        object_detail_location_model_json['width'] = 38
        object_detail_location_model_json['height'] = 38

        # Construct a model instance of ObjectDetailLocation by calling from_dict on the json representation
        object_detail_location_model = ObjectDetailLocation.from_dict(object_detail_location_model_json)
        assert object_detail_location_model != False

        # Construct a model instance of ObjectDetailLocation by calling from_dict on the json representation
        object_detail_location_model_dict = ObjectDetailLocation.from_dict(object_detail_location_model_json).__dict__
        object_detail_location_model2 = ObjectDetailLocation(**object_detail_location_model_dict)

        # Verify the model instances are equivalent
        assert object_detail_location_model == object_detail_location_model2

        # Convert model instance back to dict and verify no loss of data
        object_detail_location_model_json2 = object_detail_location_model.to_dict()
        assert object_detail_location_model_json2 == object_detail_location_model_json

class TestModel_ObjectMetadata():
    """
    Test Class for ObjectMetadata
    """

    def test_object_metadata_serialization(self):
        """
        Test serialization/deserialization for ObjectMetadata
        """

        # Construct a json representation of a ObjectMetadata model
        object_metadata_model_json = {}
        object_metadata_model_json['object'] = 'testString'
        object_metadata_model_json['count'] = 38

        # Construct a model instance of ObjectMetadata by calling from_dict on the json representation
        object_metadata_model = ObjectMetadata.from_dict(object_metadata_model_json)
        assert object_metadata_model != False

        # Construct a model instance of ObjectMetadata by calling from_dict on the json representation
        object_metadata_model_dict = ObjectMetadata.from_dict(object_metadata_model_json).__dict__
        object_metadata_model2 = ObjectMetadata(**object_metadata_model_dict)

        # Verify the model instances are equivalent
        assert object_metadata_model == object_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        object_metadata_model_json2 = object_metadata_model.to_dict()
        assert object_metadata_model_json2 == object_metadata_model_json

class TestModel_ObjectMetadataList():
    """
    Test Class for ObjectMetadataList
    """

    def test_object_metadata_list_serialization(self):
        """
        Test serialization/deserialization for ObjectMetadataList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_metadata_model = {} # ObjectMetadata
        object_metadata_model['object'] = 'testString'
        object_metadata_model['count'] = 38

        # Construct a json representation of a ObjectMetadataList model
        object_metadata_list_model_json = {}
        object_metadata_list_model_json['object_count'] = 38
        object_metadata_list_model_json['objects'] = [object_metadata_model]

        # Construct a model instance of ObjectMetadataList by calling from_dict on the json representation
        object_metadata_list_model = ObjectMetadataList.from_dict(object_metadata_list_model_json)
        assert object_metadata_list_model != False

        # Construct a model instance of ObjectMetadataList by calling from_dict on the json representation
        object_metadata_list_model_dict = ObjectMetadataList.from_dict(object_metadata_list_model_json).__dict__
        object_metadata_list_model2 = ObjectMetadataList(**object_metadata_list_model_dict)

        # Verify the model instances are equivalent
        assert object_metadata_list_model == object_metadata_list_model2

        # Convert model instance back to dict and verify no loss of data
        object_metadata_list_model_json2 = object_metadata_list_model.to_dict()
        assert object_metadata_list_model_json2 == object_metadata_list_model_json

class TestModel_ObjectTrainingStatus():
    """
    Test Class for ObjectTrainingStatus
    """

    def test_object_training_status_serialization(self):
        """
        Test serialization/deserialization for ObjectTrainingStatus
        """

        # Construct a json representation of a ObjectTrainingStatus model
        object_training_status_model_json = {}
        object_training_status_model_json['ready'] = True
        object_training_status_model_json['in_progress'] = True
        object_training_status_model_json['data_changed'] = True
        object_training_status_model_json['latest_failed'] = True
        object_training_status_model_json['rscnn_ready'] = True
        object_training_status_model_json['description'] = 'testString'

        # Construct a model instance of ObjectTrainingStatus by calling from_dict on the json representation
        object_training_status_model = ObjectTrainingStatus.from_dict(object_training_status_model_json)
        assert object_training_status_model != False

        # Construct a model instance of ObjectTrainingStatus by calling from_dict on the json representation
        object_training_status_model_dict = ObjectTrainingStatus.from_dict(object_training_status_model_json).__dict__
        object_training_status_model2 = ObjectTrainingStatus(**object_training_status_model_dict)

        # Verify the model instances are equivalent
        assert object_training_status_model == object_training_status_model2

        # Convert model instance back to dict and verify no loss of data
        object_training_status_model_json2 = object_training_status_model.to_dict()
        assert object_training_status_model_json2 == object_training_status_model_json

class TestModel_TrainingDataObject():
    """
    Test Class for TrainingDataObject
    """

    def test_training_data_object_serialization(self):
        """
        Test serialization/deserialization for TrainingDataObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        # Construct a json representation of a TrainingDataObject model
        training_data_object_model_json = {}
        training_data_object_model_json['object'] = 'testString'
        training_data_object_model_json['location'] = location_model

        # Construct a model instance of TrainingDataObject by calling from_dict on the json representation
        training_data_object_model = TrainingDataObject.from_dict(training_data_object_model_json)
        assert training_data_object_model != False

        # Construct a model instance of TrainingDataObject by calling from_dict on the json representation
        training_data_object_model_dict = TrainingDataObject.from_dict(training_data_object_model_json).__dict__
        training_data_object_model2 = TrainingDataObject(**training_data_object_model_dict)

        # Verify the model instances are equivalent
        assert training_data_object_model == training_data_object_model2

        # Convert model instance back to dict and verify no loss of data
        training_data_object_model_json2 = training_data_object_model.to_dict()
        assert training_data_object_model_json2 == training_data_object_model_json

class TestModel_TrainingDataObjects():
    """
    Test Class for TrainingDataObjects
    """

    def test_training_data_objects_serialization(self):
        """
        Test serialization/deserialization for TrainingDataObjects
        """

        # Construct dict forms of any model objects needed in order to build this model.

        location_model = {} # Location
        location_model['top'] = 38
        location_model['left'] = 38
        location_model['width'] = 38
        location_model['height'] = 38

        training_data_object_model = {} # TrainingDataObject
        training_data_object_model['object'] = 'testString'
        training_data_object_model['location'] = location_model

        # Construct a json representation of a TrainingDataObjects model
        training_data_objects_model_json = {}
        training_data_objects_model_json['objects'] = [training_data_object_model]

        # Construct a model instance of TrainingDataObjects by calling from_dict on the json representation
        training_data_objects_model = TrainingDataObjects.from_dict(training_data_objects_model_json)
        assert training_data_objects_model != False

        # Construct a model instance of TrainingDataObjects by calling from_dict on the json representation
        training_data_objects_model_dict = TrainingDataObjects.from_dict(training_data_objects_model_json).__dict__
        training_data_objects_model2 = TrainingDataObjects(**training_data_objects_model_dict)

        # Verify the model instances are equivalent
        assert training_data_objects_model == training_data_objects_model2

        # Convert model instance back to dict and verify no loss of data
        training_data_objects_model_json2 = training_data_objects_model.to_dict()
        assert training_data_objects_model_json2 == training_data_objects_model_json

class TestModel_TrainingEvent():
    """
    Test Class for TrainingEvent
    """

    def test_training_event_serialization(self):
        """
        Test serialization/deserialization for TrainingEvent
        """

        # Construct a json representation of a TrainingEvent model
        training_event_model_json = {}
        training_event_model_json['type'] = 'objects'
        training_event_model_json['collection_id'] = 'testString'
        training_event_model_json['completion_time'] = "2019-01-01T12:00:00Z"
        training_event_model_json['status'] = 'failed'
        training_event_model_json['image_count'] = 38

        # Construct a model instance of TrainingEvent by calling from_dict on the json representation
        training_event_model = TrainingEvent.from_dict(training_event_model_json)
        assert training_event_model != False

        # Construct a model instance of TrainingEvent by calling from_dict on the json representation
        training_event_model_dict = TrainingEvent.from_dict(training_event_model_json).__dict__
        training_event_model2 = TrainingEvent(**training_event_model_dict)

        # Verify the model instances are equivalent
        assert training_event_model == training_event_model2

        # Convert model instance back to dict and verify no loss of data
        training_event_model_json2 = training_event_model.to_dict()
        assert training_event_model_json2 == training_event_model_json

class TestModel_TrainingEvents():
    """
    Test Class for TrainingEvents
    """

    def test_training_events_serialization(self):
        """
        Test serialization/deserialization for TrainingEvents
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_event_model = {} # TrainingEvent
        training_event_model['type'] = 'objects'
        training_event_model['collection_id'] = 'testString'
        training_event_model['completion_time'] = "2019-01-01T12:00:00Z"
        training_event_model['status'] = 'failed'
        training_event_model['image_count'] = 38

        # Construct a json representation of a TrainingEvents model
        training_events_model_json = {}
        training_events_model_json['start_time'] = "2019-01-01T12:00:00Z"
        training_events_model_json['end_time'] = "2019-01-01T12:00:00Z"
        training_events_model_json['completed_events'] = 38
        training_events_model_json['trained_images'] = 38
        training_events_model_json['events'] = [training_event_model]

        # Construct a model instance of TrainingEvents by calling from_dict on the json representation
        training_events_model = TrainingEvents.from_dict(training_events_model_json)
        assert training_events_model != False

        # Construct a model instance of TrainingEvents by calling from_dict on the json representation
        training_events_model_dict = TrainingEvents.from_dict(training_events_model_json).__dict__
        training_events_model2 = TrainingEvents(**training_events_model_dict)

        # Verify the model instances are equivalent
        assert training_events_model == training_events_model2

        # Convert model instance back to dict and verify no loss of data
        training_events_model_json2 = training_events_model.to_dict()
        assert training_events_model_json2 == training_events_model_json

class TestModel_TrainingStatus():
    """
    Test Class for TrainingStatus
    """

    def test_training_status_serialization(self):
        """
        Test serialization/deserialization for TrainingStatus
        """

        # Construct dict forms of any model objects needed in order to build this model.

        object_training_status_model = {} # ObjectTrainingStatus
        object_training_status_model['ready'] = True
        object_training_status_model['in_progress'] = True
        object_training_status_model['data_changed'] = True
        object_training_status_model['latest_failed'] = True
        object_training_status_model['rscnn_ready'] = True
        object_training_status_model['description'] = 'testString'

        # Construct a json representation of a TrainingStatus model
        training_status_model_json = {}
        training_status_model_json['objects'] = object_training_status_model

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

class TestModel_UpdateObjectMetadata():
    """
    Test Class for UpdateObjectMetadata
    """

    def test_update_object_metadata_serialization(self):
        """
        Test serialization/deserialization for UpdateObjectMetadata
        """

        # Construct a json representation of a UpdateObjectMetadata model
        update_object_metadata_model_json = {}
        update_object_metadata_model_json['object'] = 'testString'
        update_object_metadata_model_json['count'] = 38

        # Construct a model instance of UpdateObjectMetadata by calling from_dict on the json representation
        update_object_metadata_model = UpdateObjectMetadata.from_dict(update_object_metadata_model_json)
        assert update_object_metadata_model != False

        # Construct a model instance of UpdateObjectMetadata by calling from_dict on the json representation
        update_object_metadata_model_dict = UpdateObjectMetadata.from_dict(update_object_metadata_model_json).__dict__
        update_object_metadata_model2 = UpdateObjectMetadata(**update_object_metadata_model_dict)

        # Verify the model instances are equivalent
        assert update_object_metadata_model == update_object_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        update_object_metadata_model_json2 = update_object_metadata_model.to_dict()
        assert update_object_metadata_model_json2 == update_object_metadata_model_json

class TestModel_Warning():
    """
    Test Class for Warning
    """

    def test_warning_serialization(self):
        """
        Test serialization/deserialization for Warning
        """

        # Construct a json representation of a Warning model
        warning_model_json = {}
        warning_model_json['code'] = 'invalid_field'
        warning_model_json['message'] = 'testString'
        warning_model_json['more_info'] = 'testString'

        # Construct a model instance of Warning by calling from_dict on the json representation
        warning_model = Warning.from_dict(warning_model_json)
        assert warning_model != False

        # Construct a model instance of Warning by calling from_dict on the json representation
        warning_model_dict = Warning.from_dict(warning_model_json).__dict__
        warning_model2 = Warning(**warning_model_dict)

        # Verify the model instances are equivalent
        assert warning_model == warning_model2

        # Convert model instance back to dict and verify no loss of data
        warning_model_json2 = warning_model.to_dict()
        assert warning_model_json2 == warning_model_json

class TestModel_FileWithMetadata():
    """
    Test Class for FileWithMetadata
    """

    def test_file_with_metadata_serialization(self):
        """
        Test serialization/deserialization for FileWithMetadata
        """

        # Construct a json representation of a FileWithMetadata model
        file_with_metadata_model_json = {}
        file_with_metadata_model_json['data'] = io.BytesIO(b'This is a mock file.').getvalue()
        file_with_metadata_model_json['filename'] = 'testString'
        file_with_metadata_model_json['content_type'] = 'testString'

        # Construct a model instance of FileWithMetadata by calling from_dict on the json representation
        file_with_metadata_model = FileWithMetadata.from_dict(file_with_metadata_model_json)
        assert file_with_metadata_model != False

        # Construct a model instance of FileWithMetadata by calling from_dict on the json representation
        file_with_metadata_model_dict = FileWithMetadata.from_dict(file_with_metadata_model_json).__dict__
        file_with_metadata_model2 = FileWithMetadata(**file_with_metadata_model_dict)

        # Verify the model instances are equivalent
        assert file_with_metadata_model == file_with_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        file_with_metadata_model_json2 = file_with_metadata_model.to_dict()
        assert file_with_metadata_model_json2 == file_with_metadata_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
