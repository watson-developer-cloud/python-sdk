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
import ibm_watson.language_translator_v3
from ibm_watson.language_translator_v3 import *

base_url = 'https://gateway.watsonplatform.net/language-translator/api'

##############################################################################
# Start of Service: Translation
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for translate
#-----------------------------------------------------------------------------
class TestTranslate():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_response(self):
        body = self.construct_full_body()
        response = fake_response_TranslationResult_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TranslationResult_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_empty(self):
        check_empty_required_params(self, fake_response_TranslationResult_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/translate'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.translate(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"text": [], "model_id": "string1", "source": "string1", "target": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"text": [], "model_id": "string1", "source": "string1", "target": "string1", })
        return body


# endregion
##############################################################################
# End of Service: Translation
##############################################################################

##############################################################################
# Start of Service: Identification
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_identifiable_languages
#-----------------------------------------------------------------------------
class TestListIdentifiableLanguages():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_identifiable_languages_response(self):
        body = self.construct_full_body()
        response = fake_response_IdentifiableLanguages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_identifiable_languages_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_IdentifiableLanguages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_identifiable_languages_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/identifiable_languages'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.list_identifiable_languages(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for identify
#-----------------------------------------------------------------------------
class TestIdentify():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_identify_response(self):
        body = self.construct_full_body()
        response = fake_response_IdentifiedLanguages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_identify_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_IdentifiedLanguages_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_identify_empty(self):
        check_empty_required_params(self, fake_response_IdentifiedLanguages_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/identify'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.identify(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['text'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['text'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Identification
##############################################################################

##############################################################################
# Start of Service: Models
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_models
#-----------------------------------------------------------------------------
class TestListModels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_response(self):
        body = self.construct_full_body()
        response = fake_response_TranslationModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TranslationModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/models'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.list_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['source'] = "string1"
        body['target'] = "string1"
        body['default'] = True
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for create_model
#-----------------------------------------------------------------------------
class TestCreateModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_model_response(self):
        body = self.construct_full_body()
        response = fake_response_TranslationModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TranslationModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_model_empty(self):
        check_empty_required_params(self, fake_response_TranslationModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/models'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.create_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['base_model_id'] = "string1"
        body['forced_glossary'] = tempfile.NamedTemporaryFile()
        body['parallel_corpus'] = tempfile.NamedTemporaryFile()
        body['name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['base_model_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_model
#-----------------------------------------------------------------------------
class TestDeleteModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_response(self):
        body = self.construct_full_body()
        response = fake_response_DeleteModelResult_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DeleteModelResult_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_model_empty(self):
        check_empty_required_params(self, fake_response_DeleteModelResult_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/models/{0}'.format(body['model_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.delete_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_model
#-----------------------------------------------------------------------------
class TestGetModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_model_response(self):
        body = self.construct_full_body()
        response = fake_response_TranslationModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TranslationModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_model_empty(self):
        check_empty_required_params(self, fake_response_TranslationModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/models/{0}'.format(body['model_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.get_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['model_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Models
##############################################################################

##############################################################################
# Start of Service: DocumentTranslation
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_documents
#-----------------------------------------------------------------------------
class TestListDocuments():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_documents_response(self):
        body = self.construct_full_body()
        response = fake_response_DocumentList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_documents_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DocumentList_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_documents_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/documents'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.list_documents(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for translate_document
#-----------------------------------------------------------------------------
class TestTranslateDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_document_response(self):
        body = self.construct_full_body()
        response = fake_response_DocumentStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_DocumentStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_translate_document_empty(self):
        check_empty_required_params(self, fake_response_DocumentStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/documents'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=202,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.translate_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
        body['filename'] = "string1"
        body['file_content_type'] = "string1"
        body['model_id'] = "string1"
        body['source'] = "string1"
        body['target'] = "string1"
        body['document_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['file'] = tempfile.NamedTemporaryFile()
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
        endpoint = '/v3/documents/{0}'.format(body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.get_document_status(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['document_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
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
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_document_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/documents/{0}'.format(body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.delete_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['document_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['document_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_translated_document
#-----------------------------------------------------------------------------
class TestGetTranslatedDocument():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_translated_document_response(self):
        body = self.construct_full_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_translated_document_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_translated_document_empty(self):
        check_empty_required_params(self, fake_response_BinaryIO_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v3/documents/{0}/translated_document'.format(body['document_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = LanguageTranslatorV3(
            authenticator=NoAuthAuthenticator(),
            version='2018-05-01',
            )
        service.set_service_url(base_url)
        output = service.get_translated_document(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['document_id'] = "string1"
        body['accept'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['document_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: DocumentTranslation
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
fake_response_TranslationResult_json = """{"word_count": 10, "character_count": 15, "detected_language": "fake_detected_language", "detected_language_confidence": 28, "translations": []}"""
fake_response_IdentifiableLanguages_json = """{"languages": []}"""
fake_response_IdentifiedLanguages_json = """{"languages": []}"""
fake_response_TranslationModels_json = """{"models": []}"""
fake_response_TranslationModel_json = """{"model_id": "fake_model_id", "name": "fake_name", "source": "fake_source", "target": "fake_target", "base_model_id": "fake_base_model_id", "domain": "fake_domain", "customizable": true, "default_model": false, "owner": "fake_owner", "status": "fake_status"}"""
fake_response_DeleteModelResult_json = """{"status": "fake_status"}"""
fake_response_TranslationModel_json = """{"model_id": "fake_model_id", "name": "fake_name", "source": "fake_source", "target": "fake_target", "base_model_id": "fake_base_model_id", "domain": "fake_domain", "customizable": true, "default_model": false, "owner": "fake_owner", "status": "fake_status"}"""
fake_response_DocumentList_json = """{"documents": []}"""
fake_response_DocumentStatus_json = """{"document_id": "fake_document_id", "filename": "fake_filename", "status": "fake_status", "model_id": "fake_model_id", "base_model_id": "fake_base_model_id", "source": "fake_source", "detected_language_confidence": 28, "target": "fake_target", "created": "2017-05-16T13:56:54.957Z", "completed": "2017-05-16T13:56:54.957Z", "word_count": 10, "character_count": 15}"""
fake_response_DocumentStatus_json = """{"document_id": "fake_document_id", "filename": "fake_filename", "status": "fake_status", "model_id": "fake_model_id", "base_model_id": "fake_base_model_id", "source": "fake_source", "detected_language_confidence": 28, "target": "fake_target", "created": "2017-05-16T13:56:54.957Z", "completed": "2017-05-16T13:56:54.957Z", "word_count": 10, "character_count": 15}"""
fake_response_BinaryIO_json = """Contents of response byte-stream..."""
