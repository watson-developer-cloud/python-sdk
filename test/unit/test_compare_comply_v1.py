# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2020.
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
import ibm_watson.compare_comply_v1
from ibm_watson.compare_comply_v1 import *

base_url = 'https://gateway.watsonplatform.net/compare-comply/api'

##############################################################################
# Start of Service: HTMLConversion
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for convert_to_html
#-----------------------------------------------------------------------------
class TestConvertToHtml():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_convert_to_html_response(self):
        body = self.construct_full_body()
        response = fake_response_HTMLReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_convert_to_html_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_HTMLReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_convert_to_html_empty(self):
        check_empty_required_params(self, fake_response_HTMLReturn_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/html_conversion'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.convert_to_html(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        body['file_content_type'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        return body


# endregion
##############################################################################
# End of Service: HTMLConversion
##############################################################################

##############################################################################
# Start of Service: ElementClassification
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for classify_elements
#-----------------------------------------------------------------------------
class TestClassifyElements():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_elements_response(self):
        body = self.construct_full_body()
        response = fake_response_ClassifyReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_elements_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_ClassifyReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_classify_elements_empty(self):
        check_empty_required_params(self, fake_response_ClassifyReturn_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/element_classification'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.classify_elements(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        body['file_content_type'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        return body


# endregion
##############################################################################
# End of Service: ElementClassification
##############################################################################

##############################################################################
# Start of Service: Tables
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for extract_tables
#-----------------------------------------------------------------------------
class TestExtractTables():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_extract_tables_response(self):
        body = self.construct_full_body()
        response = fake_response_TableReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_extract_tables_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TableReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_extract_tables_empty(self):
        check_empty_required_params(self, fake_response_TableReturn_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/tables'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.extract_tables(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        body['file_content_type'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        return body


# endregion
##############################################################################
# End of Service: Tables
##############################################################################

##############################################################################
# Start of Service: Comparison
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for compare_documents
#-----------------------------------------------------------------------------
class TestCompareDocuments():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_compare_documents_response(self):
        body = self.construct_full_body()
        response = fake_response_CompareReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_compare_documents_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_CompareReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_compare_documents_empty(self):
        check_empty_required_params(self, fake_response_CompareReturn_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/comparison'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.compare_documents(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['file_1'] = tempfile.NamedTemporaryFile()
        body['file_2'] = tempfile.NamedTemporaryFile()
        body['file_1_content_type'] = "string1"
        body['file_2_content_type'] = "string1"
        body['file_1_label'] = "string1"
        body['file_2_label'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['file_1'] = tempfile.NamedTemporaryFile()
        body['file_2'] = tempfile.NamedTemporaryFile()
        return body


# endregion
##############################################################################
# End of Service: Comparison
##############################################################################

##############################################################################
# Start of Service: Feedback
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for add_feedback
#-----------------------------------------------------------------------------
class TestAddFeedback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_feedback_response(self):
        body = self.construct_full_body()
        response = fake_response_FeedbackReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_feedback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_FeedbackReturn_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_feedback_empty(self):
        check_empty_required_params(self, fake_response_FeedbackReturn_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/feedback'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.add_feedback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"feedback_data": FeedbackDataInput._from_dict(json.loads("""{"feedback_type": "fake_feedback_type", "document": {"title": "fake_title", "hash": "fake_hash"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "location": {"begin": 5, "end": 3}, "text": "fake_text", "original_labels": {"types": [], "categories": []}, "updated_labels": {"types": [], "categories": []}}""")), "user_id": "string1", "comment": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"feedback_data": FeedbackDataInput._from_dict(json.loads("""{"feedback_type": "fake_feedback_type", "document": {"title": "fake_title", "hash": "fake_hash"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "location": {"begin": 5, "end": 3}, "text": "fake_text", "original_labels": {"types": [], "categories": []}, "updated_labels": {"types": [], "categories": []}}""")), "user_id": "string1", "comment": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_feedback
#-----------------------------------------------------------------------------
class TestListFeedback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_feedback_response(self):
        body = self.construct_full_body()
        response = fake_response_FeedbackList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_feedback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_FeedbackList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_feedback_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/feedback'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.list_feedback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['feedback_type'] = "string1"
        body['before'] = datetime.now().date()
        body['after'] = datetime.now().date()
        body['document_title'] = "string1"
        body['model_id'] = "string1"
        body['model_version'] = "string1"
        body['category_removed'] = "string1"
        body['category_added'] = "string1"
        body['category_not_changed'] = "string1"
        body['type_removed'] = "string1"
        body['type_added'] = "string1"
        body['type_not_changed'] = "string1"
        body['page_limit'] = 12345
        body['cursor'] = "string1"
        body['sort'] = "string1"
        body['include_total'] = True
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_feedback
#-----------------------------------------------------------------------------
class TestGetFeedback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_feedback_response(self):
        body = self.construct_full_body()
        response = fake_response_GetFeedback_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_feedback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_GetFeedback_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_feedback_empty(self):
        check_empty_required_params(self, fake_response_GetFeedback_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/feedback/{0}'.format(body['feedback_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.get_feedback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['feedback_id'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['feedback_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_feedback
#-----------------------------------------------------------------------------
class TestDeleteFeedback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_feedback_response(self):
        body = self.construct_full_body()
        response = fake_response_FeedbackDeleted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_feedback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_FeedbackDeleted_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_feedback_empty(self):
        check_empty_required_params(self, fake_response_FeedbackDeleted_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/feedback/{0}'.format(body['feedback_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.delete_feedback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['feedback_id'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['feedback_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Feedback
##############################################################################

##############################################################################
# Start of Service: Batches
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_batch
#-----------------------------------------------------------------------------
class TestCreateBatch():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_batch_response(self):
        body = self.construct_full_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_batch_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_batch_empty(self):
        check_empty_required_params(self, fake_response_BatchStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/batches'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.create_batch(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['function'] = "string1"
        body['input_credentials_file'] = tempfile.NamedTemporaryFile()
        body['input_bucket_location'] = "string1"
        body['input_bucket_name'] = "string1"
        body['output_credentials_file'] = tempfile.NamedTemporaryFile()
        body['output_bucket_location'] = "string1"
        body['output_bucket_name'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['function'] = "string1"
        body['input_credentials_file'] = tempfile.NamedTemporaryFile()
        body['input_bucket_location'] = "string1"
        body['input_bucket_name'] = "string1"
        body['output_credentials_file'] = tempfile.NamedTemporaryFile()
        body['output_bucket_location'] = "string1"
        body['output_bucket_name'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for list_batches
#-----------------------------------------------------------------------------
class TestListBatches():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_batches_response(self):
        body = self.construct_full_body()
        response = fake_response_Batches_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_batches_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Batches_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_batches_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/batches'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.list_batches(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_batch
#-----------------------------------------------------------------------------
class TestGetBatch():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_batch_response(self):
        body = self.construct_full_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_batch_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_batch_empty(self):
        check_empty_required_params(self, fake_response_BatchStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/batches/{0}'.format(body['batch_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.get_batch(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['batch_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['batch_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for update_batch
#-----------------------------------------------------------------------------
class TestUpdateBatch():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_batch_response(self):
        body = self.construct_full_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_batch_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BatchStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_batch_empty(self):
        check_empty_required_params(self, fake_response_BatchStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/batches/{0}'.format(body['batch_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = CompareComplyV1(
            authenticator=NoAuthAuthenticator(),
            version='2018-10-15',
            )
        service.set_service_url(base_url)
        output = service.update_batch(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['batch_id'] = "string1"
        body['action'] = "string1"
        body['model'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['batch_id'] = "string1"
        body['action'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Batches
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
fake_response_HTMLReturn_json = """{"num_pages": "fake_num_pages", "author": "fake_author", "publication_date": "fake_publication_date", "title": "fake_title", "html": "fake_html"}"""
fake_response_ClassifyReturn_json = """{"document": {"title": "fake_title", "html": "fake_html", "hash": "fake_hash", "label": "fake_label"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "elements": [], "effective_dates": [], "contract_amounts": [], "termination_dates": [], "contract_types": [], "contract_terms": [], "payment_terms": [], "contract_currencies": [], "tables": [], "document_structure": {"section_titles": [], "leading_sentences": [], "paragraphs": []}, "parties": []}"""
fake_response_TableReturn_json = """{"document": {"html": "fake_html", "title": "fake_title", "hash": "fake_hash"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "tables": []}"""
fake_response_CompareReturn_json = """{"model_id": "fake_model_id", "model_version": "fake_model_version", "documents": [], "aligned_elements": [], "unaligned_elements": []}"""
fake_response_FeedbackReturn_json = """{"feedback_id": "fake_feedback_id", "user_id": "fake_user_id", "comment": "fake_comment", "created": "2017-05-16T13:56:54.957Z", "feedback_data": {"feedback_type": "fake_feedback_type", "document": {"title": "fake_title", "hash": "fake_hash"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "location": {"begin": 5, "end": 3}, "text": "fake_text", "original_labels": {"types": [], "categories": [], "modification": "fake_modification"}, "updated_labels": {"types": [], "categories": [], "modification": "fake_modification"}, "pagination": {"refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor", "refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5}}}"""
fake_response_FeedbackList_json = """{"feedback": []}"""
fake_response_GetFeedback_json = """{"feedback_id": "fake_feedback_id", "created": "2017-05-16T13:56:54.957Z", "comment": "fake_comment", "feedback_data": {"feedback_type": "fake_feedback_type", "document": {"title": "fake_title", "hash": "fake_hash"}, "model_id": "fake_model_id", "model_version": "fake_model_version", "location": {"begin": 5, "end": 3}, "text": "fake_text", "original_labels": {"types": [], "categories": [], "modification": "fake_modification"}, "updated_labels": {"types": [], "categories": [], "modification": "fake_modification"}, "pagination": {"refresh_cursor": "fake_refresh_cursor", "next_cursor": "fake_next_cursor", "refresh_url": "fake_refresh_url", "next_url": "fake_next_url", "total": 5}}}"""
fake_response_FeedbackDeleted_json = """{"status": 6, "message": "fake_message"}"""
fake_response_BatchStatus_json = """{"function": "fake_function", "input_bucket_location": "fake_input_bucket_location", "input_bucket_name": "fake_input_bucket_name", "output_bucket_location": "fake_output_bucket_location", "output_bucket_name": "fake_output_bucket_name", "batch_id": "fake_batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_Batches_json = """{"batches": []}"""
fake_response_BatchStatus_json = """{"function": "fake_function", "input_bucket_location": "fake_input_bucket_location", "input_bucket_name": "fake_input_bucket_name", "output_bucket_location": "fake_output_bucket_location", "output_bucket_name": "fake_output_bucket_name", "batch_id": "fake_batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
fake_response_BatchStatus_json = """{"function": "fake_function", "input_bucket_location": "fake_input_bucket_location", "input_bucket_name": "fake_input_bucket_name", "output_bucket_location": "fake_output_bucket_location", "output_bucket_name": "fake_output_bucket_name", "batch_id": "fake_batch_id", "document_counts": {"total": 5, "pending": 7, "successful": 10, "failed": 6}, "status": "fake_status", "created": "2017-05-16T13:56:54.957Z", "updated": "2017-05-16T13:56:54.957Z"}"""
