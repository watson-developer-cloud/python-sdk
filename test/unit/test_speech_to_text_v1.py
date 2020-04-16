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
import tempfile
import ibm_watson.speech_to_text_v1
from ibm_watson.speech_to_text_v1 import *

base_url = 'https://stream.watsonplatform.net/speech-to-text/api'

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
        response = fake_response_SpeechModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_SpeechModels_json
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
        endpoint = '/v1/models'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
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
        response = fake_response_SpeechModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_SpeechModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_model_empty(self):
        check_empty_required_params(self, fake_response_SpeechModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/models/{0}'.format(body['model_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
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
# Start of Service: Synchronous
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for recognize
#-----------------------------------------------------------------------------
class TestRecognize():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_recognize_response(self):
        body = self.construct_full_body()
        response = fake_response_SpeechRecognitionResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_recognize_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_SpeechRecognitionResults_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_recognize_empty(self):
        check_empty_required_params(self, fake_response_SpeechRecognitionResults_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/recognize'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.recognize(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['audio'] = tempfile.NamedTemporaryFile()
        body['content_type'] = "string1"
        body['model'] = "string1"
        body['language_customization_id'] = "string1"
        body['acoustic_customization_id'] = "string1"
        body['base_model_version'] = "string1"
        body['customization_weight'] = 12345.0
        body['inactivity_timeout'] = 12345
        body['keywords'] = []
        body['keywords_threshold'] = 12345.0
        body['max_alternatives'] = 12345
        body['word_alternatives_threshold'] = 12345.0
        body['word_confidence'] = True
        body['timestamps'] = True
        body['profanity_filter'] = True
        body['smart_formatting'] = True
        body['speaker_labels'] = True
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        body['redaction'] = True
        body['audio_metrics'] = True
        body['end_of_phrase_silence_time'] = 12345.0
        body['split_transcript_at_phrase_end'] = True
        body['speech_detector_sensitivity'] = 12345.0
        body['background_audio_suppression'] = 12345.0
        return body

    def construct_required_body(self):
        body = dict()
        body['audio'] = tempfile.NamedTemporaryFile()
        return body


# endregion
##############################################################################
# End of Service: Synchronous
##############################################################################

##############################################################################
# Start of Service: Asynchronous
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for register_callback
#-----------------------------------------------------------------------------
class TestRegisterCallback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_register_callback_response(self):
        body = self.construct_full_body()
        response = fake_response_RegisterStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_register_callback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_RegisterStatus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_register_callback_empty(self):
        check_empty_required_params(self, fake_response_RegisterStatus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/register_callback'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.register_callback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['callback_url'] = "string1"
        body['user_secret'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['callback_url'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for unregister_callback
#-----------------------------------------------------------------------------
class TestUnregisterCallback():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_unregister_callback_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_unregister_callback_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_unregister_callback_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/unregister_callback'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.unregister_callback(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['callback_url'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['callback_url'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for create_job
#-----------------------------------------------------------------------------
class TestCreateJob():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_job_response(self):
        body = self.construct_full_body()
        response = fake_response_RecognitionJob_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_job_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_RecognitionJob_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_job_empty(self):
        check_empty_required_params(self, fake_response_RecognitionJob_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/recognitions'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.create_job(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['audio'] = tempfile.NamedTemporaryFile()
        body['content_type'] = "string1"
        body['model'] = "string1"
        body['callback_url'] = "string1"
        body['events'] = "string1"
        body['user_token'] = "string1"
        body['results_ttl'] = 12345
        body['language_customization_id'] = "string1"
        body['acoustic_customization_id'] = "string1"
        body['base_model_version'] = "string1"
        body['customization_weight'] = 12345.0
        body['inactivity_timeout'] = 12345
        body['keywords'] = []
        body['keywords_threshold'] = 12345.0
        body['max_alternatives'] = 12345
        body['word_alternatives_threshold'] = 12345.0
        body['word_confidence'] = True
        body['timestamps'] = True
        body['profanity_filter'] = True
        body['smart_formatting'] = True
        body['speaker_labels'] = True
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        body['redaction'] = True
        body['processing_metrics'] = True
        body['processing_metrics_interval'] = 12345.0
        body['audio_metrics'] = True
        body['end_of_phrase_silence_time'] = 12345.0
        body['split_transcript_at_phrase_end'] = True
        body['speech_detector_sensitivity'] = 12345.0
        body['background_audio_suppression'] = 12345.0
        return body

    def construct_required_body(self):
        body = dict()
        body['audio'] = tempfile.NamedTemporaryFile()
        return body


#-----------------------------------------------------------------------------
# Test Class for check_jobs
#-----------------------------------------------------------------------------
class TestCheckJobs():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_jobs_response(self):
        body = self.construct_full_body()
        response = fake_response_RecognitionJobs_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_jobs_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_RecognitionJobs_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_jobs_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/recognitions'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.check_jobs(**body)
        return output

    def construct_full_body(self):
        body = dict()
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for check_job
#-----------------------------------------------------------------------------
class TestCheckJob():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_job_response(self):
        body = self.construct_full_body()
        response = fake_response_RecognitionJob_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_job_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_RecognitionJob_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_check_job_empty(self):
        check_empty_required_params(self, fake_response_RecognitionJob_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/recognitions/{0}'.format(body['id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.check_job(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_job
#-----------------------------------------------------------------------------
class TestDeleteJob():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_job_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_job_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_job_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/recognitions/{0}'.format(body['id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=204,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_job(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: Asynchronous
##############################################################################

##############################################################################
# Start of Service: CustomLanguageModels
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_language_model
#-----------------------------------------------------------------------------
class TestCreateLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response_LanguageModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LanguageModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_language_model_empty(self):
        check_empty_required_params(self, fake_response_LanguageModel_json)
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
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.create_language_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "base_model_name": "string1", "dialect": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "base_model_name": "string1", "dialect": "string1", "description": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_language_models
#-----------------------------------------------------------------------------
class TestListLanguageModels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_language_models_response(self):
        body = self.construct_full_body()
        response = fake_response_LanguageModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_language_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LanguageModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_language_models_empty(self):
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
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_language_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_language_model
#-----------------------------------------------------------------------------
class TestGetLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response_LanguageModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_LanguageModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_language_model_empty(self):
        check_empty_required_params(self, fake_response_LanguageModel_json)
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
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_language_model(**body)
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
# Test Class for delete_language_model
#-----------------------------------------------------------------------------
class TestDeleteLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_language_model_empty(self):
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
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_language_model(**body)
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
# Test Class for train_language_model
#-----------------------------------------------------------------------------
class TestTrainLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_language_model_empty(self):
        check_empty_required_params(self, fake_response_TrainingResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/train'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.train_language_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_type_to_add'] = "string1"
        body['customization_weight'] = 12345.0
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for reset_language_model
#-----------------------------------------------------------------------------
class TestResetLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_language_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/reset'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.reset_language_model(**body)
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
# Test Class for upgrade_language_model
#-----------------------------------------------------------------------------
class TestUpgradeLanguageModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_language_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_language_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_language_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/upgrade_model'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.upgrade_language_model(**body)
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
# End of Service: CustomLanguageModels
##############################################################################

##############################################################################
# Start of Service: CustomCorpora
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_corpora
#-----------------------------------------------------------------------------
class TestListCorpora():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_corpora_response(self):
        body = self.construct_full_body()
        response = fake_response_Corpora_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_corpora_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Corpora_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_corpora_empty(self):
        check_empty_required_params(self, fake_response_Corpora_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/corpora'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_corpora(**body)
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
# Test Class for add_corpus
#-----------------------------------------------------------------------------
class TestAddCorpus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_corpus_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_corpus_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_corpus_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/corpora/{1}'.format(body['customization_id'], body['corpus_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_corpus(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        body['corpus_file'] = tempfile.NamedTemporaryFile()
        body['allow_overwrite'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        body['corpus_file'] = tempfile.NamedTemporaryFile()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_corpus
#-----------------------------------------------------------------------------
class TestGetCorpus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_response(self):
        body = self.construct_full_body()
        response = fake_response_Corpus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Corpus_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_corpus_empty(self):
        check_empty_required_params(self, fake_response_Corpus_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/corpora/{1}'.format(body['customization_id'], body['corpus_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_corpus(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_corpus
#-----------------------------------------------------------------------------
class TestDeleteCorpus():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_corpus_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_corpus_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_corpus_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/corpora/{1}'.format(body['customization_id'], body['corpus_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_corpus(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['corpus_name'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomCorpora
##############################################################################

##############################################################################
# Start of Service: CustomWords
##############################################################################
# region

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
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_words(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_type'] = "string1"
        body['sort'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


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
                    status=201,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
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
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.PUT,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
        body.update({"word": "string1", "sounds_like": [], "display_as": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
        body.update({"word": "string1", "sounds_like": [], "display_as": "string1", })
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
        response = fake_response_Word_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_word_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Word_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_word_empty(self):
        check_empty_required_params(self, fake_response_Word_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
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
        endpoint = '/v1/customizations/{0}/words/{1}'.format(body['customization_id'], body['word_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_word(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['word_name'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomWords
##############################################################################

##############################################################################
# Start of Service: CustomGrammars
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_grammars
#-----------------------------------------------------------------------------
class TestListGrammars():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_grammars_response(self):
        body = self.construct_full_body()
        response = fake_response_Grammars_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_grammars_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Grammars_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_grammars_empty(self):
        check_empty_required_params(self, fake_response_Grammars_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/grammars'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_grammars(**body)
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
# Test Class for add_grammar
#-----------------------------------------------------------------------------
class TestAddGrammar():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_grammar_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_grammar_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_grammar_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/grammars/{1}'.format(body['customization_id'], body['grammar_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_grammar(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        body['grammar_file'] = "string1"
        body['content_type'] = "string1"
        body['allow_overwrite'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        body['grammar_file'] = "string1"
        body['content_type'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for get_grammar
#-----------------------------------------------------------------------------
class TestGetGrammar():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_grammar_response(self):
        body = self.construct_full_body()
        response = fake_response_Grammar_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_grammar_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_Grammar_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_grammar_empty(self):
        check_empty_required_params(self, fake_response_Grammar_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/grammars/{1}'.format(body['customization_id'], body['grammar_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_grammar(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_grammar
#-----------------------------------------------------------------------------
class TestDeleteGrammar():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_grammar_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_grammar_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_grammar_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/customizations/{0}/grammars/{1}'.format(body['customization_id'], body['grammar_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_grammar(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['grammar_name'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomGrammars
##############################################################################

##############################################################################
# Start of Service: CustomAcousticModels
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for create_acoustic_model
#-----------------------------------------------------------------------------
class TestCreateAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response_AcousticModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AcousticModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_create_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response_AcousticModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.create_acoustic_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body.update({"name": "string1", "base_model_name": "string1", "description": "string1", })
        return body

    def construct_required_body(self):
        body = dict()
        body.update({"name": "string1", "base_model_name": "string1", "description": "string1", })
        return body


#-----------------------------------------------------------------------------
# Test Class for list_acoustic_models
#-----------------------------------------------------------------------------
class TestListAcousticModels():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_acoustic_models_response(self):
        body = self.construct_full_body()
        response = fake_response_AcousticModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_acoustic_models_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AcousticModels_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_acoustic_models_empty(self):
        check_empty_response(self)
        assert len(responses.calls) == 1

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations'
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_acoustic_models(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['language'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_acoustic_model
#-----------------------------------------------------------------------------
class TestGetAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response_AcousticModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AcousticModel_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response_AcousticModel_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_acoustic_model(**body)
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
# Test Class for delete_acoustic_model
#-----------------------------------------------------------------------------
class TestDeleteAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_acoustic_model(**body)
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
# Test Class for train_acoustic_model
#-----------------------------------------------------------------------------
class TestTrainAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response_TrainingResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_TrainingResponse_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_train_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response_TrainingResponse_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/train'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.train_acoustic_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['custom_language_model_id'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for reset_acoustic_model
#-----------------------------------------------------------------------------
class TestResetAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_reset_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/reset'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.reset_acoustic_model(**body)
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
# Test Class for upgrade_acoustic_model
#-----------------------------------------------------------------------------
class TestUpgradeAcousticModel():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_acoustic_model_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_acoustic_model_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_upgrade_acoustic_model_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/upgrade_model'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.upgrade_acoustic_model(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['custom_language_model_id'] = "string1"
        body['force'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomAcousticModels
##############################################################################

##############################################################################
# Start of Service: CustomAudioResources
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for list_audio
#-----------------------------------------------------------------------------
class TestListAudio():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_audio_response(self):
        body = self.construct_full_body()
        response = fake_response_AudioResources_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_audio_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AudioResources_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_list_audio_empty(self):
        check_empty_required_params(self, fake_response_AudioResources_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/audio'.format(body['customization_id'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.list_audio(**body)
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
# Test Class for add_audio
#-----------------------------------------------------------------------------
class TestAddAudio():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_audio_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_audio_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_add_audio_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/audio/{1}'.format(body['customization_id'], body['audio_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.POST,
                    url,
                    body=json.dumps(response),
                    status=201,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.add_audio(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        body['audio_resource'] = tempfile.NamedTemporaryFile()
        body['content_type'] = "string1"
        body['contained_content_type'] = "string1"
        body['allow_overwrite'] = True
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        body['audio_resource'] = tempfile.NamedTemporaryFile()
        return body


#-----------------------------------------------------------------------------
# Test Class for get_audio
#-----------------------------------------------------------------------------
class TestGetAudio():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_audio_response(self):
        body = self.construct_full_body()
        response = fake_response_AudioListing_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_audio_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response_AudioListing_json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_get_audio_empty(self):
        check_empty_required_params(self, fake_response_AudioListing_json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/audio/{1}'.format(body['customization_id'], body['audio_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.GET,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='application/json')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.get_audio(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        return body


#-----------------------------------------------------------------------------
# Test Class for delete_audio
#-----------------------------------------------------------------------------
class TestDeleteAudio():

    #--------------------------------------------------------
    # Test 1: Send fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_audio_response(self):
        body = self.construct_full_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 2: Send only required fake data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_audio_required_response(self):
        # Check response with required params
        body = self.construct_required_body()
        response = fake_response__json
        send_request(self, body, response)
        assert len(responses.calls) == 1

    #--------------------------------------------------------
    # Test 3: Send empty data and check response
    #--------------------------------------------------------
    @responses.activate
    def test_delete_audio_empty(self):
        check_empty_required_params(self, fake_response__json)
        check_missing_required_params(self)
        assert len(responses.calls) == 0

    #-----------
    #- Helpers -
    #-----------
    def make_url(self, body):
        endpoint = '/v1/acoustic_customizations/{0}/audio/{1}'.format(body['customization_id'], body['audio_name'])
        url = '{0}{1}'.format(base_url, endpoint)
        return url

    def add_mock_response(self, url, response):
        responses.add(responses.DELETE,
                    url,
                    body=json.dumps(response),
                    status=200,
                    content_type='')
    
    def call_service(self, body):
        service = SpeechToTextV1(
            authenticator=NoAuthAuthenticator(),
            )
        service.set_service_url(base_url)
        output = service.delete_audio(**body)
        return output

    def construct_full_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        return body

    def construct_required_body(self):
        body = dict()
        body['customization_id'] = "string1"
        body['audio_name'] = "string1"
        return body


# endregion
##############################################################################
# End of Service: CustomAudioResources
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
        service = SpeechToTextV1(
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
fake_response_SpeechModels_json = """{"models": []}"""
fake_response_SpeechModel_json = """{"name": "fake_name", "language": "fake_language", "rate": 4, "url": "fake_url", "supported_features": {"custom_language_model": false, "speaker_labels": true}, "description": "fake_description"}"""
fake_response_SpeechRecognitionResults_json = """{"results": [], "result_index": 12, "speaker_labels": [], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [], "clipping_rate": [], "speech_level": [], "non_speech_level": []}}, "warnings": []}"""
fake_response_RegisterStatus_json = """{"status": "fake_status", "url": "fake_url"}"""
fake_response_RecognitionJob_json = """{"id": "fake_id", "status": "fake_status", "created": "fake_created", "updated": "fake_updated", "url": "fake_url", "user_token": "fake_user_token", "results": [], "warnings": []}"""
fake_response_RecognitionJobs_json = """{"recognitions": []}"""
fake_response_RecognitionJob_json = """{"id": "fake_id", "status": "fake_status", "created": "fake_created", "updated": "fake_updated", "url": "fake_url", "user_token": "fake_user_token", "results": [], "warnings": []}"""
fake_response_LanguageModel_json = """{"customization_id": "fake_customization_id", "created": "fake_created", "updated": "fake_updated", "language": "fake_language", "dialect": "fake_dialect", "versions": [], "owner": "fake_owner", "name": "fake_name", "description": "fake_description", "base_model_name": "fake_base_model_name", "status": "fake_status", "progress": 8, "error": "fake_error", "warnings": "fake_warnings"}"""
fake_response_LanguageModels_json = """{"customizations": []}"""
fake_response_LanguageModel_json = """{"customization_id": "fake_customization_id", "created": "fake_created", "updated": "fake_updated", "language": "fake_language", "dialect": "fake_dialect", "versions": [], "owner": "fake_owner", "name": "fake_name", "description": "fake_description", "base_model_name": "fake_base_model_name", "status": "fake_status", "progress": 8, "error": "fake_error", "warnings": "fake_warnings"}"""
fake_response_TrainingResponse_json = """{"warnings": []}"""
fake_response_Corpora_json = """{"corpora": []}"""
fake_response_Corpus_json = """{"name": "fake_name", "total_words": 11, "out_of_vocabulary_words": 23, "status": "fake_status", "error": "fake_error"}"""
fake_response_Words_json = """{"words": []}"""
fake_response_Word_json = """{"word": "fake_word", "sounds_like": [], "display_as": "fake_display_as", "count": 5, "source": [], "error": []}"""
fake_response_Grammars_json = """{"grammars": []}"""
fake_response_Grammar_json = """{"name": "fake_name", "out_of_vocabulary_words": 23, "status": "fake_status", "error": "fake_error"}"""
fake_response_AcousticModel_json = """{"customization_id": "fake_customization_id", "created": "fake_created", "updated": "fake_updated", "language": "fake_language", "versions": [], "owner": "fake_owner", "name": "fake_name", "description": "fake_description", "base_model_name": "fake_base_model_name", "status": "fake_status", "progress": 8, "warnings": "fake_warnings"}"""
fake_response_AcousticModels_json = """{"customizations": []}"""
fake_response_AcousticModel_json = """{"customization_id": "fake_customization_id", "created": "fake_created", "updated": "fake_updated", "language": "fake_language", "versions": [], "owner": "fake_owner", "name": "fake_name", "description": "fake_description", "base_model_name": "fake_base_model_name", "status": "fake_status", "progress": 8, "warnings": "fake_warnings"}"""
fake_response_TrainingResponse_json = """{"warnings": []}"""
fake_response_AudioResources_json = """{"total_minutes_of_audio": 22, "audio": []}"""
fake_response_AudioListing_json = """{"duration": 8, "name": "fake_name", "details": {"type": "fake_type", "codec": "fake_codec", "frequency": 9, "compression": "fake_compression"}, "status": "fake_status", "container": {"duration": 8, "name": "fake_name", "details": {"type": "fake_type", "codec": "fake_codec", "frequency": 9, "compression": "fake_compression"}, "status": "fake_status"}, "audio": []}"""
