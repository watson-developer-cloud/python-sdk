# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2021.
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
Unit Tests for LanguageTranslatorV3
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
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
from ibm_watson.language_translator_v3 import *

version = '2018-05-01'

_service = LanguageTranslatorV3(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.language-translator.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Languages
##############################################################################
# region

class TestListLanguages():
    """
    Test Class for list_languages
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
    def test_list_languages_all_params(self):
        """
        list_languages()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/languages')
        mock_response = '{"languages": [{"language": "language", "language_name": "language_name", "native_language_name": "native_language_name", "country_code": "country_code", "words_separated": false, "direction": "direction", "supported_as_source": false, "supported_as_target": false, "identifiable": true}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_languages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_languages_value_error(self):
        """
        test_list_languages_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/languages')
        mock_response = '{"languages": [{"language": "language", "language_name": "language_name", "native_language_name": "native_language_name", "country_code": "country_code", "words_separated": false, "direction": "direction", "supported_as_source": false, "supported_as_target": false, "identifiable": true}]}'
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
                _service.list_languages(**req_copy)



# endregion
##############################################################################
# End of Service: Languages
##############################################################################

##############################################################################
# Start of Service: Translation
##############################################################################
# region

class TestTranslate():
    """
    Test Class for translate
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
    def test_translate_all_params(self):
        """
        translate()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/translate')
        mock_response = '{"word_count": 10, "character_count": 15, "detected_language": "detected_language", "detected_language_confidence": 0, "translations": [{"translation": "translation"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = ['testString']
        model_id = 'testString'
        source = 'testString'
        target = 'testString'

        # Invoke method
        response = _service.translate(
            text,
            model_id=model_id,
            source=source,
            target=target,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == ['testString']
        assert req_body['model_id'] == 'testString'
        assert req_body['source'] == 'testString'
        assert req_body['target'] == 'testString'


    @responses.activate
    def test_translate_value_error(self):
        """
        test_translate_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/translate')
        mock_response = '{"word_count": 10, "character_count": 15, "detected_language": "detected_language", "detected_language_confidence": 0, "translations": [{"translation": "translation"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = ['testString']
        model_id = 'testString'
        source = 'testString'
        target = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.translate(**req_copy)



# endregion
##############################################################################
# End of Service: Translation
##############################################################################

##############################################################################
# Start of Service: Identification
##############################################################################
# region

class TestListIdentifiableLanguages():
    """
    Test Class for list_identifiable_languages
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
    def test_list_identifiable_languages_all_params(self):
        """
        list_identifiable_languages()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/identifiable_languages')
        mock_response = '{"languages": [{"language": "language", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_identifiable_languages()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_identifiable_languages_value_error(self):
        """
        test_list_identifiable_languages_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/identifiable_languages')
        mock_response = '{"languages": [{"language": "language", "name": "name"}]}'
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
                _service.list_identifiable_languages(**req_copy)



class TestIdentify():
    """
    Test Class for identify
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
    def test_identify_all_params(self):
        """
        identify()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/identify')
        mock_response = '{"languages": [{"language": "language", "confidence": 0}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = 'testString'

        # Invoke method
        response = _service.identify(
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        assert str(responses.calls[0].request.body, 'utf-8') == text


    @responses.activate
    def test_identify_value_error(self):
        """
        test_identify_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/identify')
        mock_response = '{"languages": [{"language": "language", "confidence": 0}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.identify(**req_copy)



# endregion
##############################################################################
# End of Service: Identification
##############################################################################

##############################################################################
# Start of Service: Models
##############################################################################
# region

class TestListModels():
    """
    Test Class for list_models
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
    def test_list_models_all_params(self):
        """
        list_models()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"models": [{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        source = 'testString'
        target = 'testString'
        default = True

        # Invoke method
        response = _service.list_models(
            source=source,
            target=target,
            default=default,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'source={}'.format(source) in query_string
        assert 'target={}'.format(target) in query_string
        assert 'default={}'.format('true' if default else 'false') in query_string


    @responses.activate
    def test_list_models_required_params(self):
        """
        test_list_models_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"models": [{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_models_value_error(self):
        """
        test_list_models_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"models": [{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}]}'
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
                _service.list_models(**req_copy)



class TestCreateModel():
    """
    Test Class for create_model
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
    def test_create_model_all_params(self):
        """
        create_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        base_model_id = 'testString'
        forced_glossary = io.BytesIO(b'This is a mock file.').getvalue()
        parallel_corpus = io.BytesIO(b'This is a mock file.').getvalue()
        name = 'testString'

        # Invoke method
        response = _service.create_model(
            base_model_id,
            forced_glossary=forced_glossary,
            parallel_corpus=parallel_corpus,
            name=name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'base_model_id={}'.format(base_model_id) in query_string
        assert 'name={}'.format(name) in query_string


    @responses.activate
    def test_create_model_required_params(self):
        """
        test_create_model_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        base_model_id = 'testString'

        # Invoke method
        response = _service.create_model(
            base_model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'base_model_id={}'.format(base_model_id) in query_string


    @responses.activate
    def test_create_model_value_error(self):
        """
        test_create_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models')
        mock_response = '{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        base_model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "base_model_id": base_model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_model(**req_copy)



class TestDeleteModel():
    """
    Test Class for delete_model
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
    def test_delete_model_all_params(self):
        """
        delete_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models/testString')
        mock_response = '{"status": "status"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Invoke method
        response = _service.delete_model(
            model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_model_value_error(self):
        """
        test_delete_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models/testString')
        mock_response = '{"status": "status"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_model(**req_copy)



class TestGetModel():
    """
    Test Class for get_model
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
    def test_get_model_all_params(self):
        """
        get_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Invoke method
        response = _service.get_model(
            model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_model_value_error(self):
        """
        test_get_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/models/testString')
        mock_response = '{"model_id": "model_id", "name": "name", "source": "source", "target": "target", "base_model_id": "base_model_id", "domain": "domain", "customizable": true, "default_model": false, "owner": "owner", "status": "uploading"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_model(**req_copy)



# endregion
##############################################################################
# End of Service: Models
##############################################################################

##############################################################################
# Start of Service: DocumentTranslation
##############################################################################
# region

class TestListDocuments():
    """
    Test Class for list_documents
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
    def test_list_documents_all_params(self):
        """
        list_documents()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents')
        mock_response = '{"documents": [{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_documents()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_documents_value_error(self):
        """
        test_list_documents_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents')
        mock_response = '{"documents": [{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}]}'
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
                _service.list_documents(**req_copy)



class TestTranslateDocument():
    """
    Test Class for translate_document
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
    def test_translate_document_all_params(self):
        """
        translate_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents')
        mock_response = '{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'
        file_content_type = 'application/powerpoint'
        model_id = 'testString'
        source = 'testString'
        target = 'testString'
        document_id = 'testString'

        # Invoke method
        response = _service.translate_document(
            file,
            filename=filename,
            file_content_type=file_content_type,
            model_id=model_id,
            source=source,
            target=target,
            document_id=document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_translate_document_required_params(self):
        """
        test_translate_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents')
        mock_response = '{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'

        # Invoke method
        response = _service.translate_document(
            file,
            filename=filename,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    @responses.activate
    def test_translate_document_value_error(self):
        """
        test_translate_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents')
        mock_response = '{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Set up parameter values
        file = io.BytesIO(b'This is a mock file.').getvalue()
        filename = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.translate_document(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v3/documents/testString')
        mock_response = '{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        document_id = 'testString'

        # Invoke method
        response = _service.get_document_status(
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
        url = self.preprocess_url(_base_url + '/v3/documents/testString')
        mock_response = '{"document_id": "document_id", "filename": "filename", "status": "processing", "model_id": "model_id", "base_model_id": "base_model_id", "source": "source", "detected_language_confidence": 0, "target": "target", "created": "2019-01-01T12:00:00.000Z", "completed": "2019-01-01T12:00:00.000Z", "word_count": 10, "character_count": 15}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_document_status(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v3/documents/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        document_id = 'testString'

        # Invoke method
        response = _service.delete_document(
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_document_value_error(self):
        """
        test_delete_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_document(**req_copy)



class TestGetTranslatedDocument():
    """
    Test Class for get_translated_document
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
    def test_get_translated_document_all_params(self):
        """
        get_translated_document()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents/testString/translated_document')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/powerpoint',
                      status=200)

        # Set up parameter values
        document_id = 'testString'
        accept = 'application/powerpoint'

        # Invoke method
        response = _service.get_translated_document(
            document_id,
            accept=accept,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_translated_document_required_params(self):
        """
        test_get_translated_document_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents/testString/translated_document')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/powerpoint',
                      status=200)

        # Set up parameter values
        document_id = 'testString'

        # Invoke method
        response = _service.get_translated_document(
            document_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_translated_document_value_error(self):
        """
        test_get_translated_document_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/documents/testString/translated_document')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/powerpoint',
                      status=200)

        # Set up parameter values
        document_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "document_id": document_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_translated_document(**req_copy)



# endregion
##############################################################################
# End of Service: DocumentTranslation
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_DeleteModelResult():
    """
    Test Class for DeleteModelResult
    """

    def test_delete_model_result_serialization(self):
        """
        Test serialization/deserialization for DeleteModelResult
        """

        # Construct a json representation of a DeleteModelResult model
        delete_model_result_model_json = {}
        delete_model_result_model_json['status'] = 'testString'

        # Construct a model instance of DeleteModelResult by calling from_dict on the json representation
        delete_model_result_model = DeleteModelResult.from_dict(delete_model_result_model_json)
        assert delete_model_result_model != False

        # Construct a model instance of DeleteModelResult by calling from_dict on the json representation
        delete_model_result_model_dict = DeleteModelResult.from_dict(delete_model_result_model_json).__dict__
        delete_model_result_model2 = DeleteModelResult(**delete_model_result_model_dict)

        # Verify the model instances are equivalent
        assert delete_model_result_model == delete_model_result_model2

        # Convert model instance back to dict and verify no loss of data
        delete_model_result_model_json2 = delete_model_result_model.to_dict()
        assert delete_model_result_model_json2 == delete_model_result_model_json

class TestModel_DocumentList():
    """
    Test Class for DocumentList
    """

    def test_document_list_serialization(self):
        """
        Test serialization/deserialization for DocumentList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_status_model = {} # DocumentStatus
        document_status_model['document_id'] = 'testString'
        document_status_model['filename'] = 'testString'
        document_status_model['status'] = 'processing'
        document_status_model['model_id'] = 'testString'
        document_status_model['base_model_id'] = 'testString'
        document_status_model['source'] = 'testString'
        document_status_model['detected_language_confidence'] = 0
        document_status_model['target'] = 'testString'
        document_status_model['created'] = "2019-01-01T12:00:00Z"
        document_status_model['completed'] = "2019-01-01T12:00:00Z"
        document_status_model['word_count'] = 38
        document_status_model['character_count'] = 38

        # Construct a json representation of a DocumentList model
        document_list_model_json = {}
        document_list_model_json['documents'] = [document_status_model]

        # Construct a model instance of DocumentList by calling from_dict on the json representation
        document_list_model = DocumentList.from_dict(document_list_model_json)
        assert document_list_model != False

        # Construct a model instance of DocumentList by calling from_dict on the json representation
        document_list_model_dict = DocumentList.from_dict(document_list_model_json).__dict__
        document_list_model2 = DocumentList(**document_list_model_dict)

        # Verify the model instances are equivalent
        assert document_list_model == document_list_model2

        # Convert model instance back to dict and verify no loss of data
        document_list_model_json2 = document_list_model.to_dict()
        assert document_list_model_json2 == document_list_model_json

class TestModel_DocumentStatus():
    """
    Test Class for DocumentStatus
    """

    def test_document_status_serialization(self):
        """
        Test serialization/deserialization for DocumentStatus
        """

        # Construct a json representation of a DocumentStatus model
        document_status_model_json = {}
        document_status_model_json['document_id'] = 'testString'
        document_status_model_json['filename'] = 'testString'
        document_status_model_json['status'] = 'processing'
        document_status_model_json['model_id'] = 'testString'
        document_status_model_json['base_model_id'] = 'testString'
        document_status_model_json['source'] = 'testString'
        document_status_model_json['detected_language_confidence'] = 0
        document_status_model_json['target'] = 'testString'
        document_status_model_json['created'] = "2019-01-01T12:00:00Z"
        document_status_model_json['completed'] = "2019-01-01T12:00:00Z"
        document_status_model_json['word_count'] = 38
        document_status_model_json['character_count'] = 38

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

class TestModel_IdentifiableLanguage():
    """
    Test Class for IdentifiableLanguage
    """

    def test_identifiable_language_serialization(self):
        """
        Test serialization/deserialization for IdentifiableLanguage
        """

        # Construct a json representation of a IdentifiableLanguage model
        identifiable_language_model_json = {}
        identifiable_language_model_json['language'] = 'testString'
        identifiable_language_model_json['name'] = 'testString'

        # Construct a model instance of IdentifiableLanguage by calling from_dict on the json representation
        identifiable_language_model = IdentifiableLanguage.from_dict(identifiable_language_model_json)
        assert identifiable_language_model != False

        # Construct a model instance of IdentifiableLanguage by calling from_dict on the json representation
        identifiable_language_model_dict = IdentifiableLanguage.from_dict(identifiable_language_model_json).__dict__
        identifiable_language_model2 = IdentifiableLanguage(**identifiable_language_model_dict)

        # Verify the model instances are equivalent
        assert identifiable_language_model == identifiable_language_model2

        # Convert model instance back to dict and verify no loss of data
        identifiable_language_model_json2 = identifiable_language_model.to_dict()
        assert identifiable_language_model_json2 == identifiable_language_model_json

class TestModel_IdentifiableLanguages():
    """
    Test Class for IdentifiableLanguages
    """

    def test_identifiable_languages_serialization(self):
        """
        Test serialization/deserialization for IdentifiableLanguages
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identifiable_language_model = {} # IdentifiableLanguage
        identifiable_language_model['language'] = 'testString'
        identifiable_language_model['name'] = 'testString'

        # Construct a json representation of a IdentifiableLanguages model
        identifiable_languages_model_json = {}
        identifiable_languages_model_json['languages'] = [identifiable_language_model]

        # Construct a model instance of IdentifiableLanguages by calling from_dict on the json representation
        identifiable_languages_model = IdentifiableLanguages.from_dict(identifiable_languages_model_json)
        assert identifiable_languages_model != False

        # Construct a model instance of IdentifiableLanguages by calling from_dict on the json representation
        identifiable_languages_model_dict = IdentifiableLanguages.from_dict(identifiable_languages_model_json).__dict__
        identifiable_languages_model2 = IdentifiableLanguages(**identifiable_languages_model_dict)

        # Verify the model instances are equivalent
        assert identifiable_languages_model == identifiable_languages_model2

        # Convert model instance back to dict and verify no loss of data
        identifiable_languages_model_json2 = identifiable_languages_model.to_dict()
        assert identifiable_languages_model_json2 == identifiable_languages_model_json

class TestModel_IdentifiedLanguage():
    """
    Test Class for IdentifiedLanguage
    """

    def test_identified_language_serialization(self):
        """
        Test serialization/deserialization for IdentifiedLanguage
        """

        # Construct a json representation of a IdentifiedLanguage model
        identified_language_model_json = {}
        identified_language_model_json['language'] = 'testString'
        identified_language_model_json['confidence'] = 0

        # Construct a model instance of IdentifiedLanguage by calling from_dict on the json representation
        identified_language_model = IdentifiedLanguage.from_dict(identified_language_model_json)
        assert identified_language_model != False

        # Construct a model instance of IdentifiedLanguage by calling from_dict on the json representation
        identified_language_model_dict = IdentifiedLanguage.from_dict(identified_language_model_json).__dict__
        identified_language_model2 = IdentifiedLanguage(**identified_language_model_dict)

        # Verify the model instances are equivalent
        assert identified_language_model == identified_language_model2

        # Convert model instance back to dict and verify no loss of data
        identified_language_model_json2 = identified_language_model.to_dict()
        assert identified_language_model_json2 == identified_language_model_json

class TestModel_IdentifiedLanguages():
    """
    Test Class for IdentifiedLanguages
    """

    def test_identified_languages_serialization(self):
        """
        Test serialization/deserialization for IdentifiedLanguages
        """

        # Construct dict forms of any model objects needed in order to build this model.

        identified_language_model = {} # IdentifiedLanguage
        identified_language_model['language'] = 'testString'
        identified_language_model['confidence'] = 0

        # Construct a json representation of a IdentifiedLanguages model
        identified_languages_model_json = {}
        identified_languages_model_json['languages'] = [identified_language_model]

        # Construct a model instance of IdentifiedLanguages by calling from_dict on the json representation
        identified_languages_model = IdentifiedLanguages.from_dict(identified_languages_model_json)
        assert identified_languages_model != False

        # Construct a model instance of IdentifiedLanguages by calling from_dict on the json representation
        identified_languages_model_dict = IdentifiedLanguages.from_dict(identified_languages_model_json).__dict__
        identified_languages_model2 = IdentifiedLanguages(**identified_languages_model_dict)

        # Verify the model instances are equivalent
        assert identified_languages_model == identified_languages_model2

        # Convert model instance back to dict and verify no loss of data
        identified_languages_model_json2 = identified_languages_model.to_dict()
        assert identified_languages_model_json2 == identified_languages_model_json

class TestModel_Language():
    """
    Test Class for Language
    """

    def test_language_serialization(self):
        """
        Test serialization/deserialization for Language
        """

        # Construct a json representation of a Language model
        language_model_json = {}
        language_model_json['language'] = 'testString'
        language_model_json['language_name'] = 'testString'
        language_model_json['native_language_name'] = 'testString'
        language_model_json['country_code'] = 'testString'
        language_model_json['words_separated'] = True
        language_model_json['direction'] = 'testString'
        language_model_json['supported_as_source'] = True
        language_model_json['supported_as_target'] = True
        language_model_json['identifiable'] = True

        # Construct a model instance of Language by calling from_dict on the json representation
        language_model = Language.from_dict(language_model_json)
        assert language_model != False

        # Construct a model instance of Language by calling from_dict on the json representation
        language_model_dict = Language.from_dict(language_model_json).__dict__
        language_model2 = Language(**language_model_dict)

        # Verify the model instances are equivalent
        assert language_model == language_model2

        # Convert model instance back to dict and verify no loss of data
        language_model_json2 = language_model.to_dict()
        assert language_model_json2 == language_model_json

class TestModel_Languages():
    """
    Test Class for Languages
    """

    def test_languages_serialization(self):
        """
        Test serialization/deserialization for Languages
        """

        # Construct dict forms of any model objects needed in order to build this model.

        language_model = {} # Language
        language_model['language'] = 'testString'
        language_model['language_name'] = 'testString'
        language_model['native_language_name'] = 'testString'
        language_model['country_code'] = 'testString'
        language_model['words_separated'] = True
        language_model['direction'] = 'testString'
        language_model['supported_as_source'] = True
        language_model['supported_as_target'] = True
        language_model['identifiable'] = True

        # Construct a json representation of a Languages model
        languages_model_json = {}
        languages_model_json['languages'] = [language_model]

        # Construct a model instance of Languages by calling from_dict on the json representation
        languages_model = Languages.from_dict(languages_model_json)
        assert languages_model != False

        # Construct a model instance of Languages by calling from_dict on the json representation
        languages_model_dict = Languages.from_dict(languages_model_json).__dict__
        languages_model2 = Languages(**languages_model_dict)

        # Verify the model instances are equivalent
        assert languages_model == languages_model2

        # Convert model instance back to dict and verify no loss of data
        languages_model_json2 = languages_model.to_dict()
        assert languages_model_json2 == languages_model_json

class TestModel_Translation():
    """
    Test Class for Translation
    """

    def test_translation_serialization(self):
        """
        Test serialization/deserialization for Translation
        """

        # Construct a json representation of a Translation model
        translation_model_json = {}
        translation_model_json['translation'] = 'testString'

        # Construct a model instance of Translation by calling from_dict on the json representation
        translation_model = Translation.from_dict(translation_model_json)
        assert translation_model != False

        # Construct a model instance of Translation by calling from_dict on the json representation
        translation_model_dict = Translation.from_dict(translation_model_json).__dict__
        translation_model2 = Translation(**translation_model_dict)

        # Verify the model instances are equivalent
        assert translation_model == translation_model2

        # Convert model instance back to dict and verify no loss of data
        translation_model_json2 = translation_model.to_dict()
        assert translation_model_json2 == translation_model_json

class TestModel_TranslationModel():
    """
    Test Class for TranslationModel
    """

    def test_translation_model_serialization(self):
        """
        Test serialization/deserialization for TranslationModel
        """

        # Construct a json representation of a TranslationModel model
        translation_model_model_json = {}
        translation_model_model_json['model_id'] = 'testString'
        translation_model_model_json['name'] = 'testString'
        translation_model_model_json['source'] = 'testString'
        translation_model_model_json['target'] = 'testString'
        translation_model_model_json['base_model_id'] = 'testString'
        translation_model_model_json['domain'] = 'testString'
        translation_model_model_json['customizable'] = True
        translation_model_model_json['default_model'] = True
        translation_model_model_json['owner'] = 'testString'
        translation_model_model_json['status'] = 'uploading'

        # Construct a model instance of TranslationModel by calling from_dict on the json representation
        translation_model_model = TranslationModel.from_dict(translation_model_model_json)
        assert translation_model_model != False

        # Construct a model instance of TranslationModel by calling from_dict on the json representation
        translation_model_model_dict = TranslationModel.from_dict(translation_model_model_json).__dict__
        translation_model_model2 = TranslationModel(**translation_model_model_dict)

        # Verify the model instances are equivalent
        assert translation_model_model == translation_model_model2

        # Convert model instance back to dict and verify no loss of data
        translation_model_model_json2 = translation_model_model.to_dict()
        assert translation_model_model_json2 == translation_model_model_json

class TestModel_TranslationModels():
    """
    Test Class for TranslationModels
    """

    def test_translation_models_serialization(self):
        """
        Test serialization/deserialization for TranslationModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        translation_model_model = {} # TranslationModel
        translation_model_model['model_id'] = 'testString'
        translation_model_model['name'] = 'testString'
        translation_model_model['source'] = 'testString'
        translation_model_model['target'] = 'testString'
        translation_model_model['base_model_id'] = 'testString'
        translation_model_model['domain'] = 'testString'
        translation_model_model['customizable'] = True
        translation_model_model['default_model'] = True
        translation_model_model['owner'] = 'testString'
        translation_model_model['status'] = 'uploading'

        # Construct a json representation of a TranslationModels model
        translation_models_model_json = {}
        translation_models_model_json['models'] = [translation_model_model]

        # Construct a model instance of TranslationModels by calling from_dict on the json representation
        translation_models_model = TranslationModels.from_dict(translation_models_model_json)
        assert translation_models_model != False

        # Construct a model instance of TranslationModels by calling from_dict on the json representation
        translation_models_model_dict = TranslationModels.from_dict(translation_models_model_json).__dict__
        translation_models_model2 = TranslationModels(**translation_models_model_dict)

        # Verify the model instances are equivalent
        assert translation_models_model == translation_models_model2

        # Convert model instance back to dict and verify no loss of data
        translation_models_model_json2 = translation_models_model.to_dict()
        assert translation_models_model_json2 == translation_models_model_json

class TestModel_TranslationResult():
    """
    Test Class for TranslationResult
    """

    def test_translation_result_serialization(self):
        """
        Test serialization/deserialization for TranslationResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        translation_model = {} # Translation
        translation_model['translation'] = 'testString'

        # Construct a json representation of a TranslationResult model
        translation_result_model_json = {}
        translation_result_model_json['word_count'] = 38
        translation_result_model_json['character_count'] = 38
        translation_result_model_json['detected_language'] = 'testString'
        translation_result_model_json['detected_language_confidence'] = 0
        translation_result_model_json['translations'] = [translation_model]

        # Construct a model instance of TranslationResult by calling from_dict on the json representation
        translation_result_model = TranslationResult.from_dict(translation_result_model_json)
        assert translation_result_model != False

        # Construct a model instance of TranslationResult by calling from_dict on the json representation
        translation_result_model_dict = TranslationResult.from_dict(translation_result_model_json).__dict__
        translation_result_model2 = TranslationResult(**translation_result_model_dict)

        # Verify the model instances are equivalent
        assert translation_result_model == translation_result_model2

        # Convert model instance back to dict and verify no loss of data
        translation_result_model_json2 = translation_result_model.to_dict()
        assert translation_result_model_json2 == translation_result_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
