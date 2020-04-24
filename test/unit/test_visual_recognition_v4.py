# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
import ibm_watson.visual_recognition_v4
from ibm_watson.visual_recognition_v4 import *

base_url = 'https://gateway.watsonplatform.net/visual-recognition/api'

##############################################################################
# Start of Service: Analysis
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for analyze
#-----------------------------------------------------------------------------
class TestAnalyze():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_response(self):
        body = self.construct_full_body()
        response = fake_response_AnalyzeResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AnalyzeResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_analyze_empty(self):
        check_empty_required_params(self, fake_response_AnalyzeResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/analyze'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.analyze(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_ids'] = []
        body['features'] = []
        body['images_file'] = []
        body['image_url'] = []
        body['threshold'] = 12345.0
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_ids'] = []
        body['features'] = []
        return body


# endregion
##############################################################################
# End of Service: Analysis
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
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.create_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "description": "string1", })
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
        response = fake_response_CollectionsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collections_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CollectionsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_collections_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.list_collections(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
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
        endpoint = '/v4/collections/{0}'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.get_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
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
        endpoint = '/v4/collections/{0}'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.update_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body.update({"name": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
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
        endpoint = '/v4/collections/{0}'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.delete_collection(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Collections
##############################################################################

##############################################################################
# Start of Service: Images
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for add_images
#-----------------------------------------------------------------------------
class TestAddImages():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_images_response(self):
        body = self.construct_full_body()
        response = fake_response_ImageDetailsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_images_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ImageDetailsList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_images_empty(self):
        check_empty_required_params(self, fake_response_ImageDetailsList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.add_images(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['images_file'] = []
        body['image_url'] = []
        body['training_data'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_images
#-----------------------------------------------------------------------------
class TestListImages():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_images_response(self):
        body = self.construct_full_body()
        response = fake_response_ImageSummaryList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_images_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ImageSummaryList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_images_empty(self):
        check_empty_required_params(self, fake_response_ImageSummaryList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.list_images(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_image_details
#-----------------------------------------------------------------------------
class TestGetImageDetails():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_details_response(self):
        body = self.construct_full_body()
        response = fake_response_ImageDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_details_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ImageDetails_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_image_details_empty(self):
        check_empty_required_params(self, fake_response_ImageDetails_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images/{1}'.format(body['collection_id'], body['image_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.get_image_details(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_image
#-----------------------------------------------------------------------------
class TestDeleteImage():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_image_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_image_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_image_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images/{1}'.format(body['collection_id'], body['image_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.delete_image(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_jpeg_image
#-----------------------------------------------------------------------------
class TestGetJpegImage():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_jpeg_image_response(self):
        body = self.construct_full_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_jpeg_image_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_jpeg_image_empty(self):
        check_empty_required_params(self, fake_response_BinaryIO_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images/{1}/jpeg'.format(body['collection_id'], body['image_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.get_jpeg_image(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        body['size'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Images
##############################################################################

##############################################################################
# Start of Service: Objects
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_object_metadata
#-----------------------------------------------------------------------------
class TestListObjectMetadata():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_object_metadata_response(self):
        body = self.construct_full_body()
        response = fake_response_ObjectMetadataList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_object_metadata_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ObjectMetadataList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_object_metadata_empty(self):
        check_empty_required_params(self, fake_response_ObjectMetadataList_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/objects'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.list_object_metadata(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_object_metadata
#-----------------------------------------------------------------------------
class TestUpdateObjectMetadata():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_object_metadata_response(self):
        body = self.construct_full_body()
        response = fake_response_UpdateObjectMetadata_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_object_metadata_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_UpdateObjectMetadata_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_object_metadata_empty(self):
        check_empty_required_params(self, fake_response_UpdateObjectMetadata_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/objects/{1}'.format(body['collection_id'], body['object'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.update_object_metadata(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        body.update({"new_object": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        body.update({"new_object": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_object_metadata
#-----------------------------------------------------------------------------
class TestGetObjectMetadata():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_object_metadata_response(self):
        body = self.construct_full_body()
        response = fake_response_ObjectMetadata_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_object_metadata_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ObjectMetadata_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_object_metadata_empty(self):
        check_empty_required_params(self, fake_response_ObjectMetadata_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/objects/{1}'.format(body['collection_id'], body['object'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.get_object_metadata(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_object
#-----------------------------------------------------------------------------
class TestDeleteObject():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_object_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_object_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_object_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/objects/{1}'.format(body['collection_id'], body['object'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.delete_object(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['object'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Objects
##############################################################################

##############################################################################
# Start of Service: Training
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for train
#-----------------------------------------------------------------------------
class TestTrain():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_response(self):
        body = self.construct_full_body()
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Collection_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_empty(self):
        check_empty_required_params(self, fake_response_Collection_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/train'.format(body['collection_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.train(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for add_image_training_data
#-----------------------------------------------------------------------------
class TestAddImageTrainingData():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_image_training_data_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingDataObjects_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_image_training_data_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingDataObjects_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_image_training_data_empty(self):
        check_empty_required_params(self, fake_response_TrainingDataObjects_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/collections/{0}/images/{1}/training_data'.format(body['collection_id'], body['image_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.add_image_training_data(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        body.update({"objects": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['collection_id'] = "string1"
        body['image_id'] = "string1"
        body.update({"objects": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_training_usage
#-----------------------------------------------------------------------------
class TestGetTrainingUsage():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_usage_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingEvents_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_usage_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingEvents_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_training_usage_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v4/training_usage'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
            )
        service.set_service_url(base_url)
        output = service.get_training_usage(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['start_time'] = "string1"
        body['end_time'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


# endregion
##############################################################################
# End of Service: Training
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
        endpoint = '/v4/user_data'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='')
    
    def call_service(self, body):
        service = VisualRecognitionV4(
            authenticator=NoAuthAuthenticator(),
            version='2019-02-11',
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
fake_response_AnalyzeResponse_json = """{"images": [], "warnings": [], "trace": "fake_trace"}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "description": "fake_description"}}}"""
fake_response_CollectionsList_json = """{"collections": []}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "description": "fake_description"}}}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "description": "fake_description"}}}"""
fake_response_ImageDetailsList_json = """{"images": [], "warnings": [], "trace": "fake_trace"}"""
fake_response_ImageSummaryList_json = """{"images": []}"""
fake_response_ImageDetails_json = """{"image_id": "fake_image_id", "updated": "2017-05-16T13:56:54.957Z", "created": "2017-05-16T13:56:54.957Z", "source": {"type": "fake_type", "filename": "fake_filename", "archive_filename": "fake_archive_filename", "source_url": "fake_source_url", "resolved_url": "fake_resolved_url"}, "dimensions": {"height": 6, "width": 5}, "errors": [], "training_data": {"objects": []}}"""
fake_response_BinaryIO_json = """Contents of response byte-stream..."""
fake_response_ObjectMetadataList_json = """{"object_count": 12, "objects": []}"""
fake_response_UpdateObjectMetadata_json = """{"object": "fake_object", "count": 5}"""
fake_response_ObjectMetadata_json = """{"object": "fake_object", "count": 5}"""
fake_response_Collection_json = """{"collection_id": "fake_collection_id", "name": "fake_name", "description": "fake_description", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z", "image_count": 11, "training_status": {"objects": {"ready": false, "in_progress": false, "data_changed": true, "latest_failed": false, "description": "fake_description"}}}"""
fake_response_TrainingDataObjects_json = """{"objects": []}"""
fake_response_TrainingEvents_json = """{"start_time": "2017-05-16T13:56:54.957Z", "end_time": "2017-05-16T13:56:54.957Z", "completed_events": 16, "trained_images": 14, "events": []}"""
