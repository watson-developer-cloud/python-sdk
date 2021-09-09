# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Unit Tests for TextToSpeechV1
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import io
import json
import pytest
import re
import requests
import responses
import tempfile
import urllib
from ibm_watson.text_to_speech_v1 import *


_service = TextToSpeechV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Voices
##############################################################################
# region

class TestListVoices():
    """
    Test Class for list_voices
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
    def test_list_voices_all_params(self):
        """
        list_voices()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/voices')
        mock_response = '{"voices": [{"url": "url", "gender": "gender", "name": "name", "language": "language", "description": "description", "customizable": true, "supported_features": {"custom_pronunciation": true, "voice_transformation": true}, "customization": {"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_voices()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetVoice():
    """
    Test Class for get_voice
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
    def test_get_voice_all_params(self):
        """
        get_voice()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/voices/ar-AR_OmarVoice')
        mock_response = '{"url": "url", "gender": "gender", "name": "name", "language": "language", "description": "description", "customizable": true, "supported_features": {"custom_pronunciation": true, "voice_transformation": true}, "customization": {"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        voice = 'ar-AR_OmarVoice'
        customization_id = 'testString'

        # Invoke method
        response = _service.get_voice(
            voice,
            customization_id=customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'customization_id={}'.format(customization_id) in query_string


    @responses.activate
    def test_get_voice_required_params(self):
        """
        test_get_voice_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/voices/ar-AR_OmarVoice')
        mock_response = '{"url": "url", "gender": "gender", "name": "name", "language": "language", "description": "description", "customizable": true, "supported_features": {"custom_pronunciation": true, "voice_transformation": true}, "customization": {"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        voice = 'ar-AR_OmarVoice'

        # Invoke method
        response = _service.get_voice(
            voice,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_voice_value_error(self):
        """
        test_get_voice_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/voices/ar-AR_OmarVoice')
        mock_response = '{"url": "url", "gender": "gender", "name": "name", "language": "language", "description": "description", "customizable": true, "supported_features": {"custom_pronunciation": true, "voice_transformation": true}, "customization": {"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        voice = 'ar-AR_OmarVoice'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "voice": voice,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_voice(**req_copy)



# endregion
##############################################################################
# End of Service: Voices
##############################################################################

##############################################################################
# Start of Service: Synthesis
##############################################################################
# region

class TestSynthesize():
    """
    Test Class for synthesize
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
    def test_synthesize_all_params(self):
        """
        synthesize()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/synthesize')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='audio/basic',
                      status=200)

        # Set up parameter values
        text = 'testString'
        accept = 'audio/ogg;codecs=opus'
        voice = 'en-US_MichaelV3Voice'
        customization_id = 'testString'

        # Invoke method
        response = _service.synthesize(
            text,
            accept=accept,
            voice=voice,
            customization_id=customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'voice={}'.format(voice) in query_string
        assert 'customization_id={}'.format(customization_id) in query_string
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_synthesize_required_params(self):
        """
        test_synthesize_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/synthesize')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='audio/basic',
                      status=200)

        # Set up parameter values
        text = 'testString'

        # Invoke method
        response = _service.synthesize(
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_synthesize_value_error(self):
        """
        test_synthesize_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/synthesize')
        mock_response = 'This is a mock binary response.'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='audio/basic',
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
                _service.synthesize(**req_copy)



# endregion
##############################################################################
# End of Service: Synthesis
##############################################################################

##############################################################################
# Start of Service: Pronunciation
##############################################################################
# region

class TestGetPronunciation():
    """
    Test Class for get_pronunciation
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
    def test_get_pronunciation_all_params(self):
        """
        get_pronunciation()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/pronunciation')
        mock_response = '{"pronunciation": "pronunciation"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = 'testString'
        voice = 'en-US_MichaelV3Voice'
        format = 'ipa'
        customization_id = 'testString'

        # Invoke method
        response = _service.get_pronunciation(
            text,
            voice=voice,
            format=format,
            customization_id=customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'text={}'.format(text) in query_string
        assert 'voice={}'.format(voice) in query_string
        assert 'format={}'.format(format) in query_string
        assert 'customization_id={}'.format(customization_id) in query_string


    @responses.activate
    def test_get_pronunciation_required_params(self):
        """
        test_get_pronunciation_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/pronunciation')
        mock_response = '{"pronunciation": "pronunciation"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        text = 'testString'

        # Invoke method
        response = _service.get_pronunciation(
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'text={}'.format(text) in query_string


    @responses.activate
    def test_get_pronunciation_value_error(self):
        """
        test_get_pronunciation_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/pronunciation')
        mock_response = '{"pronunciation": "pronunciation"}'
        responses.add(responses.GET,
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
                _service.get_pronunciation(**req_copy)



# endregion
##############################################################################
# End of Service: Pronunciation
##############################################################################

##############################################################################
# Start of Service: CustomModels
##############################################################################
# region

class TestCreateCustomModel():
    """
    Test Class for create_custom_model
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
    def test_create_custom_model_all_params(self):
        """
        create_custom_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        language = 'en-US'
        description = 'testString'

        # Invoke method
        response = _service.create_custom_model(
            name,
            language=language,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['language'] == 'en-US'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_create_custom_model_value_error(self):
        """
        test_create_custom_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        language = 'en-US'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_custom_model(**req_copy)



class TestListCustomModels():
    """
    Test Class for list_custom_models
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
    def test_list_custom_models_all_params(self):
        """
        list_custom_models()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        language = 'ar-MS'

        # Invoke method
        response = _service.list_custom_models(
            language=language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'language={}'.format(language) in query_string


    @responses.activate
    def test_list_custom_models_required_params(self):
        """
        test_list_custom_models_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_custom_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestUpdateCustomModel():
    """
    Test Class for update_custom_model
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
    def test_update_custom_model_all_params(self):
        """
        update_custom_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Word model
        word_model = {}
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        # Set up parameter values
        customization_id = 'testString'
        name = 'testString'
        description = 'testString'
        words = [word_model]

        # Invoke method
        response = _service.update_custom_model(
            customization_id,
            name=name,
            description=description,
            words=words,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['description'] == 'testString'
        assert req_body['words'] == [word_model]


    @responses.activate
    def test_update_custom_model_value_error(self):
        """
        test_update_custom_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Word model
        word_model = {}
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        # Set up parameter values
        customization_id = 'testString'
        name = 'testString'
        description = 'testString'
        words = [word_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_custom_model(**req_copy)



class TestGetCustomModel():
    """
    Test Class for get_custom_model
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
    def test_get_custom_model_all_params(self):
        """
        get_custom_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        mock_response = '{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.get_custom_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_custom_model_value_error(self):
        """
        test_get_custom_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        mock_response = '{"customization_id": "customization_id", "name": "name", "language": "language", "owner": "owner", "created": "created", "last_modified": "last_modified", "description": "description", "words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}], "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_custom_model(**req_copy)



class TestDeleteCustomModel():
    """
    Test Class for delete_custom_model
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
    def test_delete_custom_model_all_params(self):
        """
        delete_custom_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.delete_custom_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_custom_model_value_error(self):
        """
        test_delete_custom_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_model(**req_copy)



# endregion
##############################################################################
# End of Service: CustomModels
##############################################################################

##############################################################################
# Start of Service: CustomWords
##############################################################################
# region

class TestAddWords():
    """
    Test Class for add_words
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
    def test_add_words_all_params(self):
        """
        add_words()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Word model
        word_model = {}
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        # Set up parameter values
        customization_id = 'testString'
        words = [word_model]

        # Invoke method
        response = _service.add_words(
            customization_id,
            words,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['words'] == [word_model]


    @responses.activate
    def test_add_words_value_error(self):
        """
        test_add_words_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Construct a dict representation of a Word model
        word_model = {}
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        # Set up parameter values
        customization_id = 'testString'
        words = [word_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "words": words,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_words(**req_copy)



class TestListWords():
    """
    Test Class for list_words
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
    def test_list_words_all_params(self):
        """
        list_words()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        mock_response = '{"words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.list_words(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_words_value_error(self):
        """
        test_list_words_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        mock_response = '{"words": [{"word": "word", "translation": "translation", "part_of_speech": "Dosi"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_words(**req_copy)



class TestAddWord():
    """
    Test Class for add_word
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
    def test_add_word_all_params(self):
        """
        add_word()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'
        translation = 'testString'
        part_of_speech = 'Dosi'

        # Invoke method
        response = _service.add_word(
            customization_id,
            word,
            translation,
            part_of_speech=part_of_speech,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['translation'] == 'testString'
        assert req_body['part_of_speech'] == 'Dosi'


    @responses.activate
    def test_add_word_value_error(self):
        """
        test_add_word_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.PUT,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'
        translation = 'testString'
        part_of_speech = 'Dosi'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word": word,
            "translation": translation,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_word(**req_copy)



class TestGetWord():
    """
    Test Class for get_word
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
    def test_get_word_all_params(self):
        """
        get_word()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        mock_response = '{"translation": "translation", "part_of_speech": "Dosi"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'

        # Invoke method
        response = _service.get_word(
            customization_id,
            word,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_word_value_error(self):
        """
        test_get_word_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        mock_response = '{"translation": "translation", "part_of_speech": "Dosi"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word": word,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_word(**req_copy)



class TestDeleteWord():
    """
    Test Class for delete_word
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
    def test_delete_word_all_params(self):
        """
        delete_word()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'

        # Invoke method
        response = _service.delete_word(
            customization_id,
            word,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_word_value_error(self):
        """
        test_delete_word_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'
        word = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word": word,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_word(**req_copy)



# endregion
##############################################################################
# End of Service: CustomWords
##############################################################################

##############################################################################
# Start of Service: CustomPrompts
##############################################################################
# region

class TestListCustomPrompts():
    """
    Test Class for list_custom_prompts
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
    def test_list_custom_prompts_all_params(self):
        """
        list_custom_prompts()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts')
        mock_response = '{"prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.list_custom_prompts(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_custom_prompts_value_error(self):
        """
        test_list_custom_prompts_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts')
        mock_response = '{"prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_custom_prompts(**req_copy)



class TestAddCustomPrompt():
    """
    Test Class for add_custom_prompt
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
    def test_add_custom_prompt_all_params(self):
        """
        add_custom_prompt()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        mock_response = '{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PromptMetadata model
        prompt_metadata_model = {}
        prompt_metadata_model['prompt_text'] = 'testString'
        prompt_metadata_model['speaker_id'] = 'testString'

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'
        metadata = prompt_metadata_model
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.add_custom_prompt(
            customization_id,
            prompt_id,
            metadata,
            file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_add_custom_prompt_value_error(self):
        """
        test_add_custom_prompt_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        mock_response = '{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a PromptMetadata model
        prompt_metadata_model = {}
        prompt_metadata_model['prompt_text'] = 'testString'
        prompt_metadata_model['speaker_id'] = 'testString'

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'
        metadata = prompt_metadata_model
        file = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "prompt_id": prompt_id,
            "metadata": metadata,
            "file": file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_custom_prompt(**req_copy)



class TestGetCustomPrompt():
    """
    Test Class for get_custom_prompt
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
    def test_get_custom_prompt_all_params(self):
        """
        get_custom_prompt()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        mock_response = '{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'

        # Invoke method
        response = _service.get_custom_prompt(
            customization_id,
            prompt_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_custom_prompt_value_error(self):
        """
        test_get_custom_prompt_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        mock_response = '{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error", "speaker_id": "speaker_id"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "prompt_id": prompt_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_custom_prompt(**req_copy)



class TestDeleteCustomPrompt():
    """
    Test Class for delete_custom_prompt
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
    def test_delete_custom_prompt_all_params(self):
        """
        delete_custom_prompt()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'

        # Invoke method
        response = _service.delete_custom_prompt(
            customization_id,
            prompt_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_custom_prompt_value_error(self):
        """
        test_delete_custom_prompt_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/prompts/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        customization_id = 'testString'
        prompt_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "prompt_id": prompt_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_custom_prompt(**req_copy)



# endregion
##############################################################################
# End of Service: CustomPrompts
##############################################################################

##############################################################################
# Start of Service: SpeakerModels
##############################################################################
# region

class TestListSpeakerModels():
    """
    Test Class for list_speaker_models
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
    def test_list_speaker_models_all_params(self):
        """
        list_speaker_models()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers')
        mock_response = '{"speakers": [{"speaker_id": "speaker_id", "name": "name"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_speaker_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCreateSpeakerModel():
    """
    Test Class for create_speaker_model
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
    def test_create_speaker_model_all_params(self):
        """
        create_speaker_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers')
        mock_response = '{"speaker_id": "speaker_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        speaker_name = 'testString'
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_speaker_model(
            speaker_name,
            audio,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'speaker_name={}'.format(speaker_name) in query_string
        # Validate body params
        assert responses.calls[0].request.body == audio


    @responses.activate
    def test_create_speaker_model_value_error(self):
        """
        test_create_speaker_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers')
        mock_response = '{"speaker_id": "speaker_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        speaker_name = 'testString'
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "speaker_name": speaker_name,
            "audio": audio,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_speaker_model(**req_copy)



class TestGetSpeakerModel():
    """
    Test Class for get_speaker_model
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
    def test_get_speaker_model_all_params(self):
        """
        get_speaker_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers/testString')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        speaker_id = 'testString'

        # Invoke method
        response = _service.get_speaker_model(
            speaker_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_speaker_model_value_error(self):
        """
        test_get_speaker_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers/testString')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "prompts": [{"prompt": "prompt", "prompt_id": "prompt_id", "status": "status", "error": "error"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        speaker_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "speaker_id": speaker_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_speaker_model(**req_copy)



class TestDeleteSpeakerModel():
    """
    Test Class for delete_speaker_model
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
    def test_delete_speaker_model_all_params(self):
        """
        delete_speaker_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        speaker_id = 'testString'

        # Invoke method
        response = _service.delete_speaker_model(
            speaker_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_speaker_model_value_error(self):
        """
        test_delete_speaker_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/speakers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        speaker_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "speaker_id": speaker_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_speaker_model(**req_copy)



# endregion
##############################################################################
# End of Service: SpeakerModels
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
# Start of Model Tests
##############################################################################
# region
class TestModel_CustomModel():
    """
    Test Class for CustomModel
    """

    def test_custom_model_serialization(self):
        """
        Test serialization/deserialization for CustomModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        prompt_model = {} # Prompt
        prompt_model['prompt'] = 'testString'
        prompt_model['prompt_id'] = 'testString'
        prompt_model['status'] = 'testString'
        prompt_model['error'] = 'testString'
        prompt_model['speaker_id'] = 'testString'

        # Construct a json representation of a CustomModel model
        custom_model_model_json = {}
        custom_model_model_json['customization_id'] = 'testString'
        custom_model_model_json['name'] = 'testString'
        custom_model_model_json['language'] = 'testString'
        custom_model_model_json['owner'] = 'testString'
        custom_model_model_json['created'] = 'testString'
        custom_model_model_json['last_modified'] = 'testString'
        custom_model_model_json['description'] = 'testString'
        custom_model_model_json['words'] = [word_model]
        custom_model_model_json['prompts'] = [prompt_model]

        # Construct a model instance of CustomModel by calling from_dict on the json representation
        custom_model_model = CustomModel.from_dict(custom_model_model_json)
        assert custom_model_model != False

        # Construct a model instance of CustomModel by calling from_dict on the json representation
        custom_model_model_dict = CustomModel.from_dict(custom_model_model_json).__dict__
        custom_model_model2 = CustomModel(**custom_model_model_dict)

        # Verify the model instances are equivalent
        assert custom_model_model == custom_model_model2

        # Convert model instance back to dict and verify no loss of data
        custom_model_model_json2 = custom_model_model.to_dict()
        assert custom_model_model_json2 == custom_model_model_json

class TestModel_CustomModels():
    """
    Test Class for CustomModels
    """

    def test_custom_models_serialization(self):
        """
        Test serialization/deserialization for CustomModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        prompt_model = {} # Prompt
        prompt_model['prompt'] = 'testString'
        prompt_model['prompt_id'] = 'testString'
        prompt_model['status'] = 'testString'
        prompt_model['error'] = 'testString'
        prompt_model['speaker_id'] = 'testString'

        custom_model_model = {} # CustomModel
        custom_model_model['customization_id'] = 'testString'
        custom_model_model['name'] = 'testString'
        custom_model_model['language'] = 'testString'
        custom_model_model['owner'] = 'testString'
        custom_model_model['created'] = 'testString'
        custom_model_model['last_modified'] = 'testString'
        custom_model_model['description'] = 'testString'
        custom_model_model['words'] = [word_model]
        custom_model_model['prompts'] = [prompt_model]

        # Construct a json representation of a CustomModels model
        custom_models_model_json = {}
        custom_models_model_json['customizations'] = [custom_model_model]

        # Construct a model instance of CustomModels by calling from_dict on the json representation
        custom_models_model = CustomModels.from_dict(custom_models_model_json)
        assert custom_models_model != False

        # Construct a model instance of CustomModels by calling from_dict on the json representation
        custom_models_model_dict = CustomModels.from_dict(custom_models_model_json).__dict__
        custom_models_model2 = CustomModels(**custom_models_model_dict)

        # Verify the model instances are equivalent
        assert custom_models_model == custom_models_model2

        # Convert model instance back to dict and verify no loss of data
        custom_models_model_json2 = custom_models_model.to_dict()
        assert custom_models_model_json2 == custom_models_model_json

class TestModel_Prompt():
    """
    Test Class for Prompt
    """

    def test_prompt_serialization(self):
        """
        Test serialization/deserialization for Prompt
        """

        # Construct a json representation of a Prompt model
        prompt_model_json = {}
        prompt_model_json['prompt'] = 'testString'
        prompt_model_json['prompt_id'] = 'testString'
        prompt_model_json['status'] = 'testString'
        prompt_model_json['error'] = 'testString'
        prompt_model_json['speaker_id'] = 'testString'

        # Construct a model instance of Prompt by calling from_dict on the json representation
        prompt_model = Prompt.from_dict(prompt_model_json)
        assert prompt_model != False

        # Construct a model instance of Prompt by calling from_dict on the json representation
        prompt_model_dict = Prompt.from_dict(prompt_model_json).__dict__
        prompt_model2 = Prompt(**prompt_model_dict)

        # Verify the model instances are equivalent
        assert prompt_model == prompt_model2

        # Convert model instance back to dict and verify no loss of data
        prompt_model_json2 = prompt_model.to_dict()
        assert prompt_model_json2 == prompt_model_json

class TestModel_PromptMetadata():
    """
    Test Class for PromptMetadata
    """

    def test_prompt_metadata_serialization(self):
        """
        Test serialization/deserialization for PromptMetadata
        """

        # Construct a json representation of a PromptMetadata model
        prompt_metadata_model_json = {}
        prompt_metadata_model_json['prompt_text'] = 'testString'
        prompt_metadata_model_json['speaker_id'] = 'testString'

        # Construct a model instance of PromptMetadata by calling from_dict on the json representation
        prompt_metadata_model = PromptMetadata.from_dict(prompt_metadata_model_json)
        assert prompt_metadata_model != False

        # Construct a model instance of PromptMetadata by calling from_dict on the json representation
        prompt_metadata_model_dict = PromptMetadata.from_dict(prompt_metadata_model_json).__dict__
        prompt_metadata_model2 = PromptMetadata(**prompt_metadata_model_dict)

        # Verify the model instances are equivalent
        assert prompt_metadata_model == prompt_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        prompt_metadata_model_json2 = prompt_metadata_model.to_dict()
        assert prompt_metadata_model_json2 == prompt_metadata_model_json

class TestModel_Prompts():
    """
    Test Class for Prompts
    """

    def test_prompts_serialization(self):
        """
        Test serialization/deserialization for Prompts
        """

        # Construct dict forms of any model objects needed in order to build this model.

        prompt_model = {} # Prompt
        prompt_model['prompt'] = 'testString'
        prompt_model['prompt_id'] = 'testString'
        prompt_model['status'] = 'testString'
        prompt_model['error'] = 'testString'
        prompt_model['speaker_id'] = 'testString'

        # Construct a json representation of a Prompts model
        prompts_model_json = {}
        prompts_model_json['prompts'] = [prompt_model]

        # Construct a model instance of Prompts by calling from_dict on the json representation
        prompts_model = Prompts.from_dict(prompts_model_json)
        assert prompts_model != False

        # Construct a model instance of Prompts by calling from_dict on the json representation
        prompts_model_dict = Prompts.from_dict(prompts_model_json).__dict__
        prompts_model2 = Prompts(**prompts_model_dict)

        # Verify the model instances are equivalent
        assert prompts_model == prompts_model2

        # Convert model instance back to dict and verify no loss of data
        prompts_model_json2 = prompts_model.to_dict()
        assert prompts_model_json2 == prompts_model_json

class TestModel_Pronunciation():
    """
    Test Class for Pronunciation
    """

    def test_pronunciation_serialization(self):
        """
        Test serialization/deserialization for Pronunciation
        """

        # Construct a json representation of a Pronunciation model
        pronunciation_model_json = {}
        pronunciation_model_json['pronunciation'] = 'testString'

        # Construct a model instance of Pronunciation by calling from_dict on the json representation
        pronunciation_model = Pronunciation.from_dict(pronunciation_model_json)
        assert pronunciation_model != False

        # Construct a model instance of Pronunciation by calling from_dict on the json representation
        pronunciation_model_dict = Pronunciation.from_dict(pronunciation_model_json).__dict__
        pronunciation_model2 = Pronunciation(**pronunciation_model_dict)

        # Verify the model instances are equivalent
        assert pronunciation_model == pronunciation_model2

        # Convert model instance back to dict and verify no loss of data
        pronunciation_model_json2 = pronunciation_model.to_dict()
        assert pronunciation_model_json2 == pronunciation_model_json

class TestModel_Speaker():
    """
    Test Class for Speaker
    """

    def test_speaker_serialization(self):
        """
        Test serialization/deserialization for Speaker
        """

        # Construct a json representation of a Speaker model
        speaker_model_json = {}
        speaker_model_json['speaker_id'] = 'testString'
        speaker_model_json['name'] = 'testString'

        # Construct a model instance of Speaker by calling from_dict on the json representation
        speaker_model = Speaker.from_dict(speaker_model_json)
        assert speaker_model != False

        # Construct a model instance of Speaker by calling from_dict on the json representation
        speaker_model_dict = Speaker.from_dict(speaker_model_json).__dict__
        speaker_model2 = Speaker(**speaker_model_dict)

        # Verify the model instances are equivalent
        assert speaker_model == speaker_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_model_json2 = speaker_model.to_dict()
        assert speaker_model_json2 == speaker_model_json

class TestModel_SpeakerCustomModel():
    """
    Test Class for SpeakerCustomModel
    """

    def test_speaker_custom_model_serialization(self):
        """
        Test serialization/deserialization for SpeakerCustomModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speaker_prompt_model = {} # SpeakerPrompt
        speaker_prompt_model['prompt'] = 'testString'
        speaker_prompt_model['prompt_id'] = 'testString'
        speaker_prompt_model['status'] = 'testString'
        speaker_prompt_model['error'] = 'testString'

        # Construct a json representation of a SpeakerCustomModel model
        speaker_custom_model_model_json = {}
        speaker_custom_model_model_json['customization_id'] = 'testString'
        speaker_custom_model_model_json['prompts'] = [speaker_prompt_model]

        # Construct a model instance of SpeakerCustomModel by calling from_dict on the json representation
        speaker_custom_model_model = SpeakerCustomModel.from_dict(speaker_custom_model_model_json)
        assert speaker_custom_model_model != False

        # Construct a model instance of SpeakerCustomModel by calling from_dict on the json representation
        speaker_custom_model_model_dict = SpeakerCustomModel.from_dict(speaker_custom_model_model_json).__dict__
        speaker_custom_model_model2 = SpeakerCustomModel(**speaker_custom_model_model_dict)

        # Verify the model instances are equivalent
        assert speaker_custom_model_model == speaker_custom_model_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_custom_model_model_json2 = speaker_custom_model_model.to_dict()
        assert speaker_custom_model_model_json2 == speaker_custom_model_model_json

class TestModel_SpeakerCustomModels():
    """
    Test Class for SpeakerCustomModels
    """

    def test_speaker_custom_models_serialization(self):
        """
        Test serialization/deserialization for SpeakerCustomModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speaker_prompt_model = {} # SpeakerPrompt
        speaker_prompt_model['prompt'] = 'testString'
        speaker_prompt_model['prompt_id'] = 'testString'
        speaker_prompt_model['status'] = 'testString'
        speaker_prompt_model['error'] = 'testString'

        speaker_custom_model_model = {} # SpeakerCustomModel
        speaker_custom_model_model['customization_id'] = 'testString'
        speaker_custom_model_model['prompts'] = [speaker_prompt_model]

        # Construct a json representation of a SpeakerCustomModels model
        speaker_custom_models_model_json = {}
        speaker_custom_models_model_json['customizations'] = [speaker_custom_model_model]

        # Construct a model instance of SpeakerCustomModels by calling from_dict on the json representation
        speaker_custom_models_model = SpeakerCustomModels.from_dict(speaker_custom_models_model_json)
        assert speaker_custom_models_model != False

        # Construct a model instance of SpeakerCustomModels by calling from_dict on the json representation
        speaker_custom_models_model_dict = SpeakerCustomModels.from_dict(speaker_custom_models_model_json).__dict__
        speaker_custom_models_model2 = SpeakerCustomModels(**speaker_custom_models_model_dict)

        # Verify the model instances are equivalent
        assert speaker_custom_models_model == speaker_custom_models_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_custom_models_model_json2 = speaker_custom_models_model.to_dict()
        assert speaker_custom_models_model_json2 == speaker_custom_models_model_json

class TestModel_SpeakerModel():
    """
    Test Class for SpeakerModel
    """

    def test_speaker_model_serialization(self):
        """
        Test serialization/deserialization for SpeakerModel
        """

        # Construct a json representation of a SpeakerModel model
        speaker_model_model_json = {}
        speaker_model_model_json['speaker_id'] = 'testString'

        # Construct a model instance of SpeakerModel by calling from_dict on the json representation
        speaker_model_model = SpeakerModel.from_dict(speaker_model_model_json)
        assert speaker_model_model != False

        # Construct a model instance of SpeakerModel by calling from_dict on the json representation
        speaker_model_model_dict = SpeakerModel.from_dict(speaker_model_model_json).__dict__
        speaker_model_model2 = SpeakerModel(**speaker_model_model_dict)

        # Verify the model instances are equivalent
        assert speaker_model_model == speaker_model_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_model_model_json2 = speaker_model_model.to_dict()
        assert speaker_model_model_json2 == speaker_model_model_json

class TestModel_SpeakerPrompt():
    """
    Test Class for SpeakerPrompt
    """

    def test_speaker_prompt_serialization(self):
        """
        Test serialization/deserialization for SpeakerPrompt
        """

        # Construct a json representation of a SpeakerPrompt model
        speaker_prompt_model_json = {}
        speaker_prompt_model_json['prompt'] = 'testString'
        speaker_prompt_model_json['prompt_id'] = 'testString'
        speaker_prompt_model_json['status'] = 'testString'
        speaker_prompt_model_json['error'] = 'testString'

        # Construct a model instance of SpeakerPrompt by calling from_dict on the json representation
        speaker_prompt_model = SpeakerPrompt.from_dict(speaker_prompt_model_json)
        assert speaker_prompt_model != False

        # Construct a model instance of SpeakerPrompt by calling from_dict on the json representation
        speaker_prompt_model_dict = SpeakerPrompt.from_dict(speaker_prompt_model_json).__dict__
        speaker_prompt_model2 = SpeakerPrompt(**speaker_prompt_model_dict)

        # Verify the model instances are equivalent
        assert speaker_prompt_model == speaker_prompt_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_prompt_model_json2 = speaker_prompt_model.to_dict()
        assert speaker_prompt_model_json2 == speaker_prompt_model_json

class TestModel_Speakers():
    """
    Test Class for Speakers
    """

    def test_speakers_serialization(self):
        """
        Test serialization/deserialization for Speakers
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speaker_model = {} # Speaker
        speaker_model['speaker_id'] = 'testString'
        speaker_model['name'] = 'testString'

        # Construct a json representation of a Speakers model
        speakers_model_json = {}
        speakers_model_json['speakers'] = [speaker_model]

        # Construct a model instance of Speakers by calling from_dict on the json representation
        speakers_model = Speakers.from_dict(speakers_model_json)
        assert speakers_model != False

        # Construct a model instance of Speakers by calling from_dict on the json representation
        speakers_model_dict = Speakers.from_dict(speakers_model_json).__dict__
        speakers_model2 = Speakers(**speakers_model_dict)

        # Verify the model instances are equivalent
        assert speakers_model == speakers_model2

        # Convert model instance back to dict and verify no loss of data
        speakers_model_json2 = speakers_model.to_dict()
        assert speakers_model_json2 == speakers_model_json

class TestModel_SupportedFeatures():
    """
    Test Class for SupportedFeatures
    """

    def test_supported_features_serialization(self):
        """
        Test serialization/deserialization for SupportedFeatures
        """

        # Construct a json representation of a SupportedFeatures model
        supported_features_model_json = {}
        supported_features_model_json['custom_pronunciation'] = True
        supported_features_model_json['voice_transformation'] = True

        # Construct a model instance of SupportedFeatures by calling from_dict on the json representation
        supported_features_model = SupportedFeatures.from_dict(supported_features_model_json)
        assert supported_features_model != False

        # Construct a model instance of SupportedFeatures by calling from_dict on the json representation
        supported_features_model_dict = SupportedFeatures.from_dict(supported_features_model_json).__dict__
        supported_features_model2 = SupportedFeatures(**supported_features_model_dict)

        # Verify the model instances are equivalent
        assert supported_features_model == supported_features_model2

        # Convert model instance back to dict and verify no loss of data
        supported_features_model_json2 = supported_features_model.to_dict()
        assert supported_features_model_json2 == supported_features_model_json

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
        translation_model_json['part_of_speech'] = 'Dosi'

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

class TestModel_Voice():
    """
    Test Class for Voice
    """

    def test_voice_serialization(self):
        """
        Test serialization/deserialization for Voice
        """

        # Construct dict forms of any model objects needed in order to build this model.

        supported_features_model = {} # SupportedFeatures
        supported_features_model['custom_pronunciation'] = True
        supported_features_model['voice_transformation'] = True

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        prompt_model = {} # Prompt
        prompt_model['prompt'] = 'testString'
        prompt_model['prompt_id'] = 'testString'
        prompt_model['status'] = 'testString'
        prompt_model['error'] = 'testString'
        prompt_model['speaker_id'] = 'testString'

        custom_model_model = {} # CustomModel
        custom_model_model['customization_id'] = 'testString'
        custom_model_model['name'] = 'testString'
        custom_model_model['language'] = 'testString'
        custom_model_model['owner'] = 'testString'
        custom_model_model['created'] = 'testString'
        custom_model_model['last_modified'] = 'testString'
        custom_model_model['description'] = 'testString'
        custom_model_model['words'] = [word_model]
        custom_model_model['prompts'] = [prompt_model]

        # Construct a json representation of a Voice model
        voice_model_json = {}
        voice_model_json['url'] = 'testString'
        voice_model_json['gender'] = 'testString'
        voice_model_json['name'] = 'testString'
        voice_model_json['language'] = 'testString'
        voice_model_json['description'] = 'testString'
        voice_model_json['customizable'] = True
        voice_model_json['supported_features'] = supported_features_model
        voice_model_json['customization'] = custom_model_model

        # Construct a model instance of Voice by calling from_dict on the json representation
        voice_model = Voice.from_dict(voice_model_json)
        assert voice_model != False

        # Construct a model instance of Voice by calling from_dict on the json representation
        voice_model_dict = Voice.from_dict(voice_model_json).__dict__
        voice_model2 = Voice(**voice_model_dict)

        # Verify the model instances are equivalent
        assert voice_model == voice_model2

        # Convert model instance back to dict and verify no loss of data
        voice_model_json2 = voice_model.to_dict()
        assert voice_model_json2 == voice_model_json

class TestModel_Voices():
    """
    Test Class for Voices
    """

    def test_voices_serialization(self):
        """
        Test serialization/deserialization for Voices
        """

        # Construct dict forms of any model objects needed in order to build this model.

        supported_features_model = {} # SupportedFeatures
        supported_features_model['custom_pronunciation'] = True
        supported_features_model['voice_transformation'] = True

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        prompt_model = {} # Prompt
        prompt_model['prompt'] = 'testString'
        prompt_model['prompt_id'] = 'testString'
        prompt_model['status'] = 'testString'
        prompt_model['error'] = 'testString'
        prompt_model['speaker_id'] = 'testString'

        custom_model_model = {} # CustomModel
        custom_model_model['customization_id'] = 'testString'
        custom_model_model['name'] = 'testString'
        custom_model_model['language'] = 'testString'
        custom_model_model['owner'] = 'testString'
        custom_model_model['created'] = 'testString'
        custom_model_model['last_modified'] = 'testString'
        custom_model_model['description'] = 'testString'
        custom_model_model['words'] = [word_model]
        custom_model_model['prompts'] = [prompt_model]

        voice_model = {} # Voice
        voice_model['url'] = 'testString'
        voice_model['gender'] = 'testString'
        voice_model['name'] = 'testString'
        voice_model['language'] = 'testString'
        voice_model['description'] = 'testString'
        voice_model['customizable'] = True
        voice_model['supported_features'] = supported_features_model
        voice_model['customization'] = custom_model_model

        # Construct a json representation of a Voices model
        voices_model_json = {}
        voices_model_json['voices'] = [voice_model]

        # Construct a model instance of Voices by calling from_dict on the json representation
        voices_model = Voices.from_dict(voices_model_json)
        assert voices_model != False

        # Construct a model instance of Voices by calling from_dict on the json representation
        voices_model_dict = Voices.from_dict(voices_model_json).__dict__
        voices_model2 = Voices(**voices_model_dict)

        # Verify the model instances are equivalent
        assert voices_model == voices_model2

        # Convert model instance back to dict and verify no loss of data
        voices_model_json2 = voices_model.to_dict()
        assert voices_model_json2 == voices_model_json

class TestModel_Word():
    """
    Test Class for Word
    """

    def test_word_serialization(self):
        """
        Test serialization/deserialization for Word
        """

        # Construct a json representation of a Word model
        word_model_json = {}
        word_model_json['word'] = 'testString'
        word_model_json['translation'] = 'testString'
        word_model_json['part_of_speech'] = 'Dosi'

        # Construct a model instance of Word by calling from_dict on the json representation
        word_model = Word.from_dict(word_model_json)
        assert word_model != False

        # Construct a model instance of Word by calling from_dict on the json representation
        word_model_dict = Word.from_dict(word_model_json).__dict__
        word_model2 = Word(**word_model_dict)

        # Verify the model instances are equivalent
        assert word_model == word_model2

        # Convert model instance back to dict and verify no loss of data
        word_model_json2 = word_model.to_dict()
        assert word_model_json2 == word_model_json

class TestModel_Words():
    """
    Test Class for Words
    """

    def test_words_serialization(self):
        """
        Test serialization/deserialization for Words
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['translation'] = 'testString'
        word_model['part_of_speech'] = 'Dosi'

        # Construct a json representation of a Words model
        words_model_json = {}
        words_model_json['words'] = [word_model]

        # Construct a model instance of Words by calling from_dict on the json representation
        words_model = Words.from_dict(words_model_json)
        assert words_model != False

        # Construct a model instance of Words by calling from_dict on the json representation
        words_model_dict = Words.from_dict(words_model_json).__dict__
        words_model2 = Words(**words_model_dict)

        # Verify the model instances are equivalent
        assert words_model == words_model2

        # Convert model instance back to dict and verify no loss of data
        words_model_json2 = words_model.to_dict()
        assert words_model_json2 == words_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
