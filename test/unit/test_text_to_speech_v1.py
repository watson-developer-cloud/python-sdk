# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2015, 2020.
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

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
import ibm_watson.text_to_speech_v1
from ibm_watson.text_to_speech_v1 import *

base_url = 'https://stream.watsonplatform.net/text-to-speech/api'

##############################################################################
# Start of Service: Voices
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_voices
#-----------------------------------------------------------------------------
class TestListVoices():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voices_response(self):
        body = self.construct_full_body()
        response = fake_response_Voices_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voices_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Voices_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voices_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/voices'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_voices(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_voice
#-----------------------------------------------------------------------------
class TestGetVoice():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_response(self):
        body = self.construct_full_body()
        response = fake_response_Voice_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Voice_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_empty(self):
        check_empty_required_params(self, fake_response_Voice_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/voices/{0}'.format(body['voice'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_voice(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['voice'] = "string1"
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['voice'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Voices
##############################################################################

##############################################################################
# Start of Service: Synthesis
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for synthesize
#-----------------------------------------------------------------------------
class TestSynthesize():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_synthesize_response(self):
        body = self.construct_full_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_synthesize_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_BinaryIO_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_synthesize_empty(self):
        check_empty_required_params(self, fake_response_BinaryIO_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/synthesize'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.synthesize(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"text": "string1", })
        body['accept'] = "string1"
        body['voice'] = "string1"
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"text": "string1", })
        return body


# endregion
##############################################################################
# End of Service: Synthesis
##############################################################################

##############################################################################
# Start of Service: Pronunciation
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for get_pronunciation
#-----------------------------------------------------------------------------
class TestGetPronunciation():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_pronunciation_response(self):
        body = self.construct_full_body()
        response = fake_response_Pronunciation_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_pronunciation_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Pronunciation_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_pronunciation_empty(self):
        check_empty_required_params(self, fake_response_Pronunciation_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/pronunciation'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_pronunciation(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['text'] = "string1"
        body['voice'] = "string1"
        body['format'] = "string1"
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['text'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Pronunciation
##############################################################################

##############################################################################
# Start of Service: CustomModels
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_voice_model
#-----------------------------------------------------------------------------
class TestCreateVoiceModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_voice_model_response(self):
        body = self.construct_full_body()
        response = fake_response_VoiceModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_voice_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_VoiceModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_voice_model_empty(self):
        check_empty_required_params(self, fake_response_VoiceModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.create_voice_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "language": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "language": "string1", "description": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_voice_models
#-----------------------------------------------------------------------------
class TestListVoiceModels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voice_models_response(self):
        body = self.construct_full_body()
        response = fake_response_VoiceModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voice_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_VoiceModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_voice_models_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_voice_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for update_voice_model
#-----------------------------------------------------------------------------
class TestUpdateVoiceModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_voice_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_voice_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_update_voice_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.update_voice_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "words": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body.update({"name": "string1", "description": "string1", "words": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_voice_model
#-----------------------------------------------------------------------------
class TestGetVoiceModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_model_response(self):
        body = self.construct_full_body()
        response = fake_response_VoiceModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_VoiceModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_voice_model_empty(self):
        check_empty_required_params(self, fake_response_VoiceModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_voice_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_voice_model
#-----------------------------------------------------------------------------
class TestDeleteVoiceModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_voice_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_voice_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_voice_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_voice_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomModels
##############################################################################

##############################################################################
# Start of Service: CustomWords
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for add_words
#-----------------------------------------------------------------------------
class TestAddWords():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_words_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_words_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_words_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_words(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body.update({"words": [], })
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body.update({"words": [], })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_words
#-----------------------------------------------------------------------------
class TestListWords():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_words_response(self):
        body = self.construct_full_body()
        response = fake_response_Words_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_words_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Words_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_words_empty(self):
        check_empty_required_params(self, fake_response_Words_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_words(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for add_word
#-----------------------------------------------------------------------------
class TestAddWord():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_word_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_word_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_word_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        body.update({"translation": "string1", "part_of_speech": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        body.update({"translation": "string1", "part_of_speech": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for get_word
#-----------------------------------------------------------------------------
class TestGetWord():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_word_response(self):
        body = self.construct_full_body()
        response = fake_response_Translation_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_word_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Translation_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_word_empty(self):
        check_empty_required_params(self, fake_response_Translation_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_word
#-----------------------------------------------------------------------------
class TestDeleteWord():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_word_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_word_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_word_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomWords
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
        service = TextToSpeechV1(
            authenticator=NoAuthAuthenticator(),
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
fake_response_Voices_json = """{"voices": []}"""
fake_response_Voice_json = """{"url": "fake_url", "gender": "fake_gender", "name": "fake_name", "language": "fake_language", "description": "fake_description", "customizable": true, "supported_features": {"custom_pronunciation": true, "voice_transformation": true}, "customization": {"customization_id": "fake_customization_id", "name": "fake_name", "language": "fake_language", "owner": "fake_owner", "created": "fake_created", "last_modified": "fake_last_modified", "description": "fake_description", "words": []}}"""
fake_response_BinaryIO_json = """Contents of response byte-stream..."""
fake_response_Pronunciation_json = """{"pronunciation": "fake_pronunciation"}"""
fake_response_VoiceModel_json = """{"customization_id": "fake_customization_id", "name": "fake_name", "language": "fake_language", "owner": "fake_owner", "created": "fake_created", "last_modified": "fake_last_modified", "description": "fake_description", "words": []}"""
fake_response_VoiceModels_json = """{"customizations": []}"""
fake_response_VoiceModel_json = """{"customization_id": "fake_customization_id", "name": "fake_name", "language": "fake_language", "owner": "fake_owner", "created": "fake_created", "last_modified": "fake_last_modified", "description": "fake_description", "words": []}"""
fake_response_Words_json = """{"words": []}"""
fake_response_Translation_json = """{"translation": "fake_translation", "part_of_speech": "fake_part_of_speech"}"""
