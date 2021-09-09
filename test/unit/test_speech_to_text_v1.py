# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2015, 2021.
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
Unit Tests for SpeechToTextV1
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
from ibm_watson.speech_to_text_v1 import *


_service = SpeechToTextV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://api.us-south.speech-to-text.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

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
        url = self.preprocess_url(_base_url + '/v1/models')
        mock_response = '{"models": [{"name": "name", "language": "language", "rate": 4, "url": "url", "supported_features": {"custom_language_model": false, "speaker_labels": true, "low_latency": false}, "description": "description"}]}'
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
        url = self.preprocess_url(_base_url + '/v1/models/ar-AR_BroadbandModel')
        mock_response = '{"name": "name", "language": "language", "rate": 4, "url": "url", "supported_features": {"custom_language_model": false, "speaker_labels": true, "low_latency": false}, "description": "description"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'ar-AR_BroadbandModel'

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
        url = self.preprocess_url(_base_url + '/v1/models/ar-AR_BroadbandModel')
        mock_response = '{"name": "name", "language": "language", "rate": 4, "url": "url", "supported_features": {"custom_language_model": false, "speaker_labels": true, "low_latency": false}, "description": "description"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'ar-AR_BroadbandModel'

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
# Start of Service: Synchronous
##############################################################################
# region

class TestRecognize():
    """
    Test Class for recognize
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
    def test_recognize_all_params(self):
        """
        recognize()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognize')
        mock_response = '{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'application/octet-stream'
        model = 'en-US_BroadbandModel'
        language_customization_id = 'testString'
        acoustic_customization_id = 'testString'
        base_model_version = 'testString'
        customization_weight = 72.5
        inactivity_timeout = 38
        keywords = ['testString']
        keywords_threshold = 72.5
        max_alternatives = 38
        word_alternatives_threshold = 72.5
        word_confidence = False
        timestamps = False
        profanity_filter = True
        smart_formatting = False
        speaker_labels = False
        customization_id = 'testString'
        grammar_name = 'testString'
        redaction = False
        audio_metrics = False
        end_of_phrase_silence_time = 72.5
        split_transcript_at_phrase_end = False
        speech_detector_sensitivity = 72.5
        background_audio_suppression = 72.5
        low_latency = False

        # Invoke method
        response = _service.recognize(
            audio,
            content_type=content_type,
            model=model,
            language_customization_id=language_customization_id,
            acoustic_customization_id=acoustic_customization_id,
            base_model_version=base_model_version,
            customization_weight=customization_weight,
            inactivity_timeout=inactivity_timeout,
            keywords=keywords,
            keywords_threshold=keywords_threshold,
            max_alternatives=max_alternatives,
            word_alternatives_threshold=word_alternatives_threshold,
            word_confidence=word_confidence,
            timestamps=timestamps,
            profanity_filter=profanity_filter,
            smart_formatting=smart_formatting,
            speaker_labels=speaker_labels,
            customization_id=customization_id,
            grammar_name=grammar_name,
            redaction=redaction,
            audio_metrics=audio_metrics,
            end_of_phrase_silence_time=end_of_phrase_silence_time,
            split_transcript_at_phrase_end=split_transcript_at_phrase_end,
            speech_detector_sensitivity=speech_detector_sensitivity,
            background_audio_suppression=background_audio_suppression,
            low_latency=low_latency,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string
        assert 'language_customization_id={}'.format(language_customization_id) in query_string
        assert 'acoustic_customization_id={}'.format(acoustic_customization_id) in query_string
        assert 'base_model_version={}'.format(base_model_version) in query_string
        assert 'customization_weight={}'.format(customization_weight) in query_string
        assert 'inactivity_timeout={}'.format(inactivity_timeout) in query_string
        assert 'keywords={}'.format(','.join(keywords)) in query_string
        assert 'keywords_threshold={}'.format(keywords_threshold) in query_string
        assert 'max_alternatives={}'.format(max_alternatives) in query_string
        assert 'word_alternatives_threshold={}'.format(word_alternatives_threshold) in query_string
        assert 'word_confidence={}'.format('true' if word_confidence else 'false') in query_string
        assert 'timestamps={}'.format('true' if timestamps else 'false') in query_string
        assert 'profanity_filter={}'.format('true' if profanity_filter else 'false') in query_string
        assert 'smart_formatting={}'.format('true' if smart_formatting else 'false') in query_string
        assert 'speaker_labels={}'.format('true' if speaker_labels else 'false') in query_string
        assert 'customization_id={}'.format(customization_id) in query_string
        assert 'grammar_name={}'.format(grammar_name) in query_string
        assert 'redaction={}'.format('true' if redaction else 'false') in query_string
        assert 'audio_metrics={}'.format('true' if audio_metrics else 'false') in query_string
        assert 'end_of_phrase_silence_time={}'.format(end_of_phrase_silence_time) in query_string
        assert 'split_transcript_at_phrase_end={}'.format('true' if split_transcript_at_phrase_end else 'false') in query_string
        assert 'speech_detector_sensitivity={}'.format(speech_detector_sensitivity) in query_string
        assert 'background_audio_suppression={}'.format(background_audio_suppression) in query_string
        assert 'low_latency={}'.format('true' if low_latency else 'false') in query_string
        # Validate body params


    @responses.activate
    def test_recognize_required_params(self):
        """
        test_recognize_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognize')
        mock_response = '{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.recognize(
            audio,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params


    @responses.activate
    def test_recognize_value_error(self):
        """
        test_recognize_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognize')
        mock_response = '{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "audio": audio,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.recognize(**req_copy)



# endregion
##############################################################################
# End of Service: Synchronous
##############################################################################

##############################################################################
# Start of Service: Asynchronous
##############################################################################
# region

class TestRegisterCallback():
    """
    Test Class for register_callback
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
    def test_register_callback_all_params(self):
        """
        register_callback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/register_callback')
        mock_response = '{"status": "created", "url": "url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        callback_url = 'testString'
        user_secret = 'testString'

        # Invoke method
        response = _service.register_callback(
            callback_url,
            user_secret=user_secret,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'callback_url={}'.format(callback_url) in query_string
        assert 'user_secret={}'.format(user_secret) in query_string


    @responses.activate
    def test_register_callback_required_params(self):
        """
        test_register_callback_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/register_callback')
        mock_response = '{"status": "created", "url": "url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        callback_url = 'testString'

        # Invoke method
        response = _service.register_callback(
            callback_url,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'callback_url={}'.format(callback_url) in query_string


    @responses.activate
    def test_register_callback_value_error(self):
        """
        test_register_callback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/register_callback')
        mock_response = '{"status": "created", "url": "url"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        callback_url = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "callback_url": callback_url,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.register_callback(**req_copy)



class TestUnregisterCallback():
    """
    Test Class for unregister_callback
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
    def test_unregister_callback_all_params(self):
        """
        unregister_callback()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/unregister_callback')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        callback_url = 'testString'

        # Invoke method
        response = _service.unregister_callback(
            callback_url,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'callback_url={}'.format(callback_url) in query_string


    @responses.activate
    def test_unregister_callback_value_error(self):
        """
        test_unregister_callback_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/unregister_callback')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        callback_url = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "callback_url": callback_url,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.unregister_callback(**req_copy)



class TestCreateJob():
    """
    Test Class for create_job
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
    def test_create_job_all_params(self):
        """
        create_job()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions')
        mock_response = '{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'application/octet-stream'
        model = 'en-US_BroadbandModel'
        callback_url = 'testString'
        events = 'recognitions.started'
        user_token = 'testString'
        results_ttl = 38
        language_customization_id = 'testString'
        acoustic_customization_id = 'testString'
        base_model_version = 'testString'
        customization_weight = 72.5
        inactivity_timeout = 38
        keywords = ['testString']
        keywords_threshold = 72.5
        max_alternatives = 38
        word_alternatives_threshold = 72.5
        word_confidence = False
        timestamps = False
        profanity_filter = True
        smart_formatting = False
        speaker_labels = False
        customization_id = 'testString'
        grammar_name = 'testString'
        redaction = False
        processing_metrics = False
        processing_metrics_interval = 72.5
        audio_metrics = False
        end_of_phrase_silence_time = 72.5
        split_transcript_at_phrase_end = False
        speech_detector_sensitivity = 72.5
        background_audio_suppression = 72.5
        low_latency = False

        # Invoke method
        response = _service.create_job(
            audio,
            content_type=content_type,
            model=model,
            callback_url=callback_url,
            events=events,
            user_token=user_token,
            results_ttl=results_ttl,
            language_customization_id=language_customization_id,
            acoustic_customization_id=acoustic_customization_id,
            base_model_version=base_model_version,
            customization_weight=customization_weight,
            inactivity_timeout=inactivity_timeout,
            keywords=keywords,
            keywords_threshold=keywords_threshold,
            max_alternatives=max_alternatives,
            word_alternatives_threshold=word_alternatives_threshold,
            word_confidence=word_confidence,
            timestamps=timestamps,
            profanity_filter=profanity_filter,
            smart_formatting=smart_formatting,
            speaker_labels=speaker_labels,
            customization_id=customization_id,
            grammar_name=grammar_name,
            redaction=redaction,
            processing_metrics=processing_metrics,
            processing_metrics_interval=processing_metrics_interval,
            audio_metrics=audio_metrics,
            end_of_phrase_silence_time=end_of_phrase_silence_time,
            split_transcript_at_phrase_end=split_transcript_at_phrase_end,
            speech_detector_sensitivity=speech_detector_sensitivity,
            background_audio_suppression=background_audio_suppression,
            low_latency=low_latency,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'model={}'.format(model) in query_string
        assert 'callback_url={}'.format(callback_url) in query_string
        assert 'events={}'.format(events) in query_string
        assert 'user_token={}'.format(user_token) in query_string
        assert 'results_ttl={}'.format(results_ttl) in query_string
        assert 'language_customization_id={}'.format(language_customization_id) in query_string
        assert 'acoustic_customization_id={}'.format(acoustic_customization_id) in query_string
        assert 'base_model_version={}'.format(base_model_version) in query_string
        assert 'customization_weight={}'.format(customization_weight) in query_string
        assert 'inactivity_timeout={}'.format(inactivity_timeout) in query_string
        assert 'keywords={}'.format(','.join(keywords)) in query_string
        assert 'keywords_threshold={}'.format(keywords_threshold) in query_string
        assert 'max_alternatives={}'.format(max_alternatives) in query_string
        assert 'word_alternatives_threshold={}'.format(word_alternatives_threshold) in query_string
        assert 'word_confidence={}'.format('true' if word_confidence else 'false') in query_string
        assert 'timestamps={}'.format('true' if timestamps else 'false') in query_string
        assert 'profanity_filter={}'.format('true' if profanity_filter else 'false') in query_string
        assert 'smart_formatting={}'.format('true' if smart_formatting else 'false') in query_string
        assert 'speaker_labels={}'.format('true' if speaker_labels else 'false') in query_string
        assert 'customization_id={}'.format(customization_id) in query_string
        assert 'grammar_name={}'.format(grammar_name) in query_string
        assert 'redaction={}'.format('true' if redaction else 'false') in query_string
        assert 'processing_metrics={}'.format('true' if processing_metrics else 'false') in query_string
        assert 'processing_metrics_interval={}'.format(processing_metrics_interval) in query_string
        assert 'audio_metrics={}'.format('true' if audio_metrics else 'false') in query_string
        assert 'end_of_phrase_silence_time={}'.format(end_of_phrase_silence_time) in query_string
        assert 'split_transcript_at_phrase_end={}'.format('true' if split_transcript_at_phrase_end else 'false') in query_string
        assert 'speech_detector_sensitivity={}'.format(speech_detector_sensitivity) in query_string
        assert 'background_audio_suppression={}'.format(background_audio_suppression) in query_string
        assert 'low_latency={}'.format('true' if low_latency else 'false') in query_string
        # Validate body params


    @responses.activate
    def test_create_job_required_params(self):
        """
        test_create_job_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions')
        mock_response = '{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_job(
            audio,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params


    @responses.activate
    def test_create_job_value_error(self):
        """
        test_create_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions')
        mock_response = '{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        audio = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "audio": audio,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_job(**req_copy)



class TestCheckJobs():
    """
    Test Class for check_jobs
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
    def test_check_jobs_all_params(self):
        """
        check_jobs()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions')
        mock_response = '{"recognitions": [{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.check_jobs()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestCheckJob():
    """
    Test Class for check_job
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
    def test_check_job_all_params(self):
        """
        check_job()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions/testString')
        mock_response = '{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.check_job(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_check_job_value_error(self):
        """
        test_check_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions/testString')
        mock_response = '{"id": "id", "status": "waiting", "created": "created", "updated": "updated", "url": "url", "user_token": "user_token", "results": [{"results": [{"final": false, "alternatives": [{"transcript": "transcript", "confidence": 0, "timestamps": ["timestamps"], "word_confidence": ["word_confidence"]}], "keywords_result": {"mapKey": [{"normalized_text": "normalized_text", "start_time": 10, "end_time": 8, "confidence": 0}]}, "word_alternatives": [{"start_time": 10, "end_time": 8, "alternatives": [{"confidence": 0, "word": "word"}]}], "end_of_utterance": "end_of_data"}], "result_index": 12, "speaker_labels": [{"from": 5, "to": 2, "speaker": 7, "confidence": 10, "final": false}], "processing_metrics": {"processed_audio": {"received": 8, "seen_by_engine": 14, "transcription": 13, "speaker_labels": 14}, "wall_clock_since_first_byte_received": 36, "periodic": true}, "audio_metrics": {"sampling_interval": 17, "accumulated": {"final": false, "end_time": 8, "signal_to_noise_ratio": 21, "speech_ratio": 12, "high_frequency_loss": 19, "direct_current_offset": [{"begin": 5, "end": 3, "count": 5}], "clipping_rate": [{"begin": 5, "end": 3, "count": 5}], "speech_level": [{"begin": 5, "end": 3, "count": 5}], "non_speech_level": [{"begin": 5, "end": 3, "count": 5}]}}, "warnings": ["warnings"]}], "warnings": ["warnings"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.check_job(**req_copy)



class TestDeleteJob():
    """
    Test Class for delete_job
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
    def test_delete_job_all_params(self):
        """
        delete_job()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Invoke method
        response = _service.delete_job(
            id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_job_value_error(self):
        """
        test_delete_job_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/recognitions/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "id": id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_job(**req_copy)



# endregion
##############################################################################
# End of Service: Asynchronous
##############################################################################

##############################################################################
# Start of Service: CustomLanguageModels
##############################################################################
# region

class TestCreateLanguageModel():
    """
    Test Class for create_language_model
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
    def test_create_language_model_all_params(self):
        """
        create_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        base_model_name = 'ar-MS_Telephony'
        dialect = 'testString'
        description = 'testString'

        # Invoke method
        response = _service.create_language_model(
            name,
            base_model_name,
            dialect=dialect,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['base_model_name'] == 'ar-MS_Telephony'
        assert req_body['dialect'] == 'testString'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_create_language_model_value_error(self):
        """
        test_create_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        base_model_name = 'ar-MS_Telephony'
        dialect = 'testString'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "base_model_name": base_model_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_language_model(**req_copy)



class TestListLanguageModels():
    """
    Test Class for list_language_models
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
    def test_list_language_models_all_params(self):
        """
        list_language_models()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        language = 'ar-AR'

        # Invoke method
        response = _service.list_language_models(
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
    def test_list_language_models_required_params(self):
        """
        test_list_language_models_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_language_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetLanguageModel():
    """
    Test Class for get_language_model
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
    def test_get_language_model_all_params(self):
        """
        get_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.get_language_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_language_model_value_error(self):
        """
        test_get_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "dialect": "dialect", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "error": "error", "warnings": "warnings"}'
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
                _service.get_language_model(**req_copy)



class TestDeleteLanguageModel():
    """
    Test Class for delete_language_model
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
    def test_delete_language_model_all_params(self):
        """
        delete_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.delete_language_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_language_model_value_error(self):
        """
        test_delete_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString')
        responses.add(responses.DELETE,
                      url,
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
                _service.delete_language_model(**req_copy)



class TestTrainLanguageModel():
    """
    Test Class for train_language_model
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
    def test_train_language_model_all_params(self):
        """
        train_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_type_to_add = 'all'
        customization_weight = 72.5

        # Invoke method
        response = _service.train_language_model(
            customization_id,
            word_type_to_add=word_type_to_add,
            customization_weight=customization_weight,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'word_type_to_add={}'.format(word_type_to_add) in query_string
        assert 'customization_weight={}'.format(customization_weight) in query_string


    @responses.activate
    def test_train_language_model_required_params(self):
        """
        test_train_language_model_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.train_language_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_train_language_model_value_error(self):
        """
        test_train_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
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
                _service.train_language_model(**req_copy)



class TestResetLanguageModel():
    """
    Test Class for reset_language_model
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
    def test_reset_language_model_all_params(self):
        """
        reset_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/reset')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.reset_language_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_reset_language_model_value_error(self):
        """
        test_reset_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/reset')
        responses.add(responses.POST,
                      url,
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
                _service.reset_language_model(**req_copy)



class TestUpgradeLanguageModel():
    """
    Test Class for upgrade_language_model
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
    def test_upgrade_language_model_all_params(self):
        """
        upgrade_language_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/upgrade_model')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.upgrade_language_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_upgrade_language_model_value_error(self):
        """
        test_upgrade_language_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/upgrade_model')
        responses.add(responses.POST,
                      url,
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
                _service.upgrade_language_model(**req_copy)



# endregion
##############################################################################
# End of Service: CustomLanguageModels
##############################################################################

##############################################################################
# Start of Service: CustomCorpora
##############################################################################
# region

class TestListCorpora():
    """
    Test Class for list_corpora
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
    def test_list_corpora_all_params(self):
        """
        list_corpora()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora')
        mock_response = '{"corpora": [{"name": "name", "total_words": 11, "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.list_corpora(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_corpora_value_error(self):
        """
        test_list_corpora_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora')
        mock_response = '{"corpora": [{"name": "name", "total_words": 11, "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}]}'
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
                _service.list_corpora(**req_copy)



class TestAddCorpus():
    """
    Test Class for add_corpus
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
    def test_add_corpus_all_params(self):
        """
        add_corpus()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'
        corpus_file = io.BytesIO(b'This is a mock file.').getvalue()
        allow_overwrite = False

        # Invoke method
        response = _service.add_corpus(
            customization_id,
            corpus_name,
            corpus_file,
            allow_overwrite=allow_overwrite,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'allow_overwrite={}'.format('true' if allow_overwrite else 'false') in query_string


    @responses.activate
    def test_add_corpus_required_params(self):
        """
        test_add_corpus_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'
        corpus_file = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.add_corpus(
            customization_id,
            corpus_name,
            corpus_file,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201


    @responses.activate
    def test_add_corpus_value_error(self):
        """
        test_add_corpus_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'
        corpus_file = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "corpus_name": corpus_name,
            "corpus_file": corpus_file,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_corpus(**req_copy)



class TestGetCorpus():
    """
    Test Class for get_corpus
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
    def test_get_corpus_all_params(self):
        """
        get_corpus()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        mock_response = '{"name": "name", "total_words": 11, "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'

        # Invoke method
        response = _service.get_corpus(
            customization_id,
            corpus_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_corpus_value_error(self):
        """
        test_get_corpus_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        mock_response = '{"name": "name", "total_words": 11, "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "corpus_name": corpus_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_corpus(**req_copy)



class TestDeleteCorpus():
    """
    Test Class for delete_corpus
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
    def test_delete_corpus_all_params(self):
        """
        delete_corpus()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'

        # Invoke method
        response = _service.delete_corpus(
            customization_id,
            corpus_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_corpus_value_error(self):
        """
        test_delete_corpus_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/corpora/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        corpus_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "corpus_name": corpus_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_corpus(**req_copy)



# endregion
##############################################################################
# End of Service: CustomCorpora
##############################################################################

##############################################################################
# Start of Service: CustomWords
##############################################################################
# region

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
        mock_response = '{"words": [{"word": "word", "sounds_like": ["sounds_like"], "display_as": "display_as", "count": 5, "source": ["source"], "error": [{"element": "element"}]}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_type = 'all'
        sort = 'alphabetical'

        # Invoke method
        response = _service.list_words(
            customization_id,
            word_type=word_type,
            sort=sort,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'word_type={}'.format(word_type) in query_string
        assert 'sort={}'.format(sort) in query_string


    @responses.activate
    def test_list_words_required_params(self):
        """
        test_list_words_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        mock_response = '{"words": [{"word": "word", "sounds_like": ["sounds_like"], "display_as": "display_as", "count": 5, "source": ["source"], "error": [{"element": "element"}]}]}'
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
        mock_response = '{"words": [{"word": "word", "sounds_like": ["sounds_like"], "display_as": "display_as", "count": 5, "source": ["source"], "error": [{"element": "element"}]}]}'
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
                      status=201)

        # Construct a dict representation of a CustomWord model
        custom_word_model = {}
        custom_word_model['word'] = 'testString'
        custom_word_model['sounds_like'] = ['testString']
        custom_word_model['display_as'] = 'testString'

        # Set up parameter values
        customization_id = 'testString'
        words = [custom_word_model]

        # Invoke method
        response = _service.add_words(
            customization_id,
            words,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['words'] == [custom_word_model]


    @responses.activate
    def test_add_words_value_error(self):
        """
        test_add_words_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Construct a dict representation of a CustomWord model
        custom_word_model = {}
        custom_word_model['word'] = 'testString'
        custom_word_model['sounds_like'] = ['testString']
        custom_word_model['display_as'] = 'testString'

        # Set up parameter values
        customization_id = 'testString'
        words = [custom_word_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "words": words,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_words(**req_copy)



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
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'
        word = 'testString'
        sounds_like = ['testString']
        display_as = 'testString'

        # Invoke method
        response = _service.add_word(
            customization_id,
            word_name,
            word=word,
            sounds_like=sounds_like,
            display_as=display_as,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['word'] == 'testString'
        assert req_body['sounds_like'] == ['testString']
        assert req_body['display_as'] == 'testString'


    @responses.activate
    def test_add_word_value_error(self):
        """
        test_add_word_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.PUT,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'
        word = 'testString'
        sounds_like = ['testString']
        display_as = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word_name": word_name,
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
        mock_response = '{"word": "word", "sounds_like": ["sounds_like"], "display_as": "display_as", "count": 5, "source": ["source"], "error": [{"element": "element"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'

        # Invoke method
        response = _service.get_word(
            customization_id,
            word_name,
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
        mock_response = '{"word": "word", "sounds_like": ["sounds_like"], "display_as": "display_as", "count": 5, "source": ["source"], "error": [{"element": "element"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word_name": word_name,
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
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'

        # Invoke method
        response = _service.delete_word(
            customization_id,
            word_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_word_value_error(self):
        """
        test_delete_word_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/words/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        word_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "word_name": word_name,
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
# Start of Service: CustomGrammars
##############################################################################
# region

class TestListGrammars():
    """
    Test Class for list_grammars
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
    def test_list_grammars_all_params(self):
        """
        list_grammars()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars')
        mock_response = '{"grammars": [{"name": "name", "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.list_grammars(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_grammars_value_error(self):
        """
        test_list_grammars_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars')
        mock_response = '{"grammars": [{"name": "name", "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}]}'
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
                _service.list_grammars(**req_copy)



class TestAddGrammar():
    """
    Test Class for add_grammar
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
    def test_add_grammar_all_params(self):
        """
        add_grammar()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'
        grammar_file = 'testString'
        content_type = 'application/srgs'
        allow_overwrite = False

        # Invoke method
        response = _service.add_grammar(
            customization_id,
            grammar_name,
            grammar_file,
            content_type,
            allow_overwrite=allow_overwrite,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'allow_overwrite={}'.format('true' if allow_overwrite else 'false') in query_string
        # Validate body params


    @responses.activate
    def test_add_grammar_required_params(self):
        """
        test_add_grammar_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'
        grammar_file = 'testString'
        content_type = 'application/srgs'

        # Invoke method
        response = _service.add_grammar(
            customization_id,
            grammar_name,
            grammar_file,
            content_type,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params


    @responses.activate
    def test_add_grammar_value_error(self):
        """
        test_add_grammar_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'
        grammar_file = 'testString'
        content_type = 'application/srgs'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "grammar_name": grammar_name,
            "grammar_file": grammar_file,
            "content_type": content_type,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_grammar(**req_copy)



class TestGetGrammar():
    """
    Test Class for get_grammar
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
    def test_get_grammar_all_params(self):
        """
        get_grammar()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        mock_response = '{"name": "name", "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'

        # Invoke method
        response = _service.get_grammar(
            customization_id,
            grammar_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_grammar_value_error(self):
        """
        test_get_grammar_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        mock_response = '{"name": "name", "out_of_vocabulary_words": 23, "status": "analyzed", "error": "error"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "grammar_name": grammar_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_grammar(**req_copy)



class TestDeleteGrammar():
    """
    Test Class for delete_grammar
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
    def test_delete_grammar_all_params(self):
        """
        delete_grammar()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'

        # Invoke method
        response = _service.delete_grammar(
            customization_id,
            grammar_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_grammar_value_error(self):
        """
        test_delete_grammar_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/customizations/testString/grammars/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        grammar_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "grammar_name": grammar_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_grammar(**req_copy)



# endregion
##############################################################################
# End of Service: CustomGrammars
##############################################################################

##############################################################################
# Start of Service: CustomAcousticModels
##############################################################################
# region

class TestCreateAcousticModel():
    """
    Test Class for create_acoustic_model
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
    def test_create_acoustic_model_all_params(self):
        """
        create_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        base_model_name = 'ar-AR_BroadbandModel'
        description = 'testString'

        # Invoke method
        response = _service.create_acoustic_model(
            name,
            base_model_name,
            description=description,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['name'] == 'testString'
        assert req_body['base_model_name'] == 'ar-AR_BroadbandModel'
        assert req_body['description'] == 'testString'


    @responses.activate
    def test_create_acoustic_model_value_error(self):
        """
        test_create_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        name = 'testString'
        base_model_name = 'ar-AR_BroadbandModel'
        description = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "name": name,
            "base_model_name": base_model_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_acoustic_model(**req_copy)



class TestListAcousticModels():
    """
    Test Class for list_acoustic_models
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
    def test_list_acoustic_models_all_params(self):
        """
        list_acoustic_models()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        language = 'ar-AR'

        # Invoke method
        response = _service.list_acoustic_models(
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
    def test_list_acoustic_models_required_params(self):
        """
        test_list_acoustic_models_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations')
        mock_response = '{"customizations": [{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_acoustic_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetAcousticModel():
    """
    Test Class for get_acoustic_model
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
    def test_get_acoustic_model_all_params(self):
        """
        get_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.get_acoustic_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_acoustic_model_value_error(self):
        """
        test_get_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString')
        mock_response = '{"customization_id": "customization_id", "created": "created", "updated": "updated", "language": "language", "versions": ["versions"], "owner": "owner", "name": "name", "description": "description", "base_model_name": "base_model_name", "status": "pending", "progress": 8, "warnings": "warnings"}'
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
                _service.get_acoustic_model(**req_copy)



class TestDeleteAcousticModel():
    """
    Test Class for delete_acoustic_model
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
    def test_delete_acoustic_model_all_params(self):
        """
        delete_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.delete_acoustic_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_acoustic_model_value_error(self):
        """
        test_delete_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString')
        responses.add(responses.DELETE,
                      url,
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
                _service.delete_acoustic_model(**req_copy)



class TestTrainAcousticModel():
    """
    Test Class for train_acoustic_model
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
    def test_train_acoustic_model_all_params(self):
        """
        train_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        custom_language_model_id = 'testString'

        # Invoke method
        response = _service.train_acoustic_model(
            customization_id,
            custom_language_model_id=custom_language_model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'custom_language_model_id={}'.format(custom_language_model_id) in query_string


    @responses.activate
    def test_train_acoustic_model_required_params(self):
        """
        test_train_acoustic_model_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.train_acoustic_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_train_acoustic_model_value_error(self):
        """
        test_train_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/train')
        mock_response = '{"warnings": [{"code": "invalid_audio_files", "message": "message"}]}'
        responses.add(responses.POST,
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
                _service.train_acoustic_model(**req_copy)



class TestResetAcousticModel():
    """
    Test Class for reset_acoustic_model
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
    def test_reset_acoustic_model_all_params(self):
        """
        reset_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/reset')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.reset_acoustic_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_reset_acoustic_model_value_error(self):
        """
        test_reset_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/reset')
        responses.add(responses.POST,
                      url,
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
                _service.reset_acoustic_model(**req_copy)



class TestUpgradeAcousticModel():
    """
    Test Class for upgrade_acoustic_model
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
    def test_upgrade_acoustic_model_all_params(self):
        """
        upgrade_acoustic_model()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/upgrade_model')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        custom_language_model_id = 'testString'
        force = False

        # Invoke method
        response = _service.upgrade_acoustic_model(
            customization_id,
            custom_language_model_id=custom_language_model_id,
            force=force,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'custom_language_model_id={}'.format(custom_language_model_id) in query_string
        assert 'force={}'.format('true' if force else 'false') in query_string


    @responses.activate
    def test_upgrade_acoustic_model_required_params(self):
        """
        test_upgrade_acoustic_model_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/upgrade_model')
        responses.add(responses.POST,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.upgrade_acoustic_model(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_upgrade_acoustic_model_value_error(self):
        """
        test_upgrade_acoustic_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/upgrade_model')
        responses.add(responses.POST,
                      url,
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
                _service.upgrade_acoustic_model(**req_copy)



# endregion
##############################################################################
# End of Service: CustomAcousticModels
##############################################################################

##############################################################################
# Start of Service: CustomAudioResources
##############################################################################
# region

class TestListAudio():
    """
    Test Class for list_audio
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
    def test_list_audio_all_params(self):
        """
        list_audio()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio')
        mock_response = '{"total_minutes_of_audio": 22, "audio": [{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'

        # Invoke method
        response = _service.list_audio(
            customization_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_audio_value_error(self):
        """
        test_list_audio_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio')
        mock_response = '{"total_minutes_of_audio": 22, "audio": [{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}]}'
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
                _service.list_audio(**req_copy)



class TestAddAudio():
    """
    Test Class for add_audio
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
    def test_add_audio_all_params(self):
        """
        add_audio()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'
        audio_resource = io.BytesIO(b'This is a mock file.').getvalue()
        content_type = 'application/zip'
        contained_content_type = 'audio/alaw'
        allow_overwrite = False

        # Invoke method
        response = _service.add_audio(
            customization_id,
            audio_name,
            audio_resource,
            content_type=content_type,
            contained_content_type=contained_content_type,
            allow_overwrite=allow_overwrite,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'allow_overwrite={}'.format('true' if allow_overwrite else 'false') in query_string
        # Validate body params


    @responses.activate
    def test_add_audio_required_params(self):
        """
        test_add_audio_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'
        audio_resource = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.add_audio(
            customization_id,
            audio_name,
            audio_resource,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params


    @responses.activate
    def test_add_audio_value_error(self):
        """
        test_add_audio_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        responses.add(responses.POST,
                      url,
                      status=201)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'
        audio_resource = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "audio_name": audio_name,
            "audio_resource": audio_resource,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.add_audio(**req_copy)



class TestGetAudio():
    """
    Test Class for get_audio
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
    def test_get_audio_all_params(self):
        """
        get_audio()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        mock_response = '{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok", "container": {"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}, "audio": [{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'

        # Invoke method
        response = _service.get_audio(
            customization_id,
            audio_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_audio_value_error(self):
        """
        test_get_audio_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        mock_response = '{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok", "container": {"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}, "audio": [{"duration": 8, "name": "name", "details": {"type": "audio", "codec": "codec", "frequency": 9, "compression": "zip"}, "status": "ok"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "audio_name": audio_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_audio(**req_copy)



class TestDeleteAudio():
    """
    Test Class for delete_audio
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
    def test_delete_audio_all_params(self):
        """
        delete_audio()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'

        # Invoke method
        response = _service.delete_audio(
            customization_id,
            audio_name,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_audio_value_error(self):
        """
        test_delete_audio_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/acoustic_customizations/testString/audio/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        customization_id = 'testString'
        audio_name = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "customization_id": customization_id,
            "audio_name": audio_name,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_audio(**req_copy)



# endregion
##############################################################################
# End of Service: CustomAudioResources
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
class TestModel_AcousticModel():
    """
    Test Class for AcousticModel
    """

    def test_acoustic_model_serialization(self):
        """
        Test serialization/deserialization for AcousticModel
        """

        # Construct a json representation of a AcousticModel model
        acoustic_model_model_json = {}
        acoustic_model_model_json['customization_id'] = 'testString'
        acoustic_model_model_json['created'] = 'testString'
        acoustic_model_model_json['updated'] = 'testString'
        acoustic_model_model_json['language'] = 'testString'
        acoustic_model_model_json['versions'] = ['testString']
        acoustic_model_model_json['owner'] = 'testString'
        acoustic_model_model_json['name'] = 'testString'
        acoustic_model_model_json['description'] = 'testString'
        acoustic_model_model_json['base_model_name'] = 'testString'
        acoustic_model_model_json['status'] = 'pending'
        acoustic_model_model_json['progress'] = 38
        acoustic_model_model_json['warnings'] = 'testString'

        # Construct a model instance of AcousticModel by calling from_dict on the json representation
        acoustic_model_model = AcousticModel.from_dict(acoustic_model_model_json)
        assert acoustic_model_model != False

        # Construct a model instance of AcousticModel by calling from_dict on the json representation
        acoustic_model_model_dict = AcousticModel.from_dict(acoustic_model_model_json).__dict__
        acoustic_model_model2 = AcousticModel(**acoustic_model_model_dict)

        # Verify the model instances are equivalent
        assert acoustic_model_model == acoustic_model_model2

        # Convert model instance back to dict and verify no loss of data
        acoustic_model_model_json2 = acoustic_model_model.to_dict()
        assert acoustic_model_model_json2 == acoustic_model_model_json

class TestModel_AcousticModels():
    """
    Test Class for AcousticModels
    """

    def test_acoustic_models_serialization(self):
        """
        Test serialization/deserialization for AcousticModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        acoustic_model_model = {} # AcousticModel
        acoustic_model_model['customization_id'] = 'testString'
        acoustic_model_model['created'] = 'testString'
        acoustic_model_model['updated'] = 'testString'
        acoustic_model_model['language'] = 'testString'
        acoustic_model_model['versions'] = ['testString']
        acoustic_model_model['owner'] = 'testString'
        acoustic_model_model['name'] = 'testString'
        acoustic_model_model['description'] = 'testString'
        acoustic_model_model['base_model_name'] = 'testString'
        acoustic_model_model['status'] = 'pending'
        acoustic_model_model['progress'] = 38
        acoustic_model_model['warnings'] = 'testString'

        # Construct a json representation of a AcousticModels model
        acoustic_models_model_json = {}
        acoustic_models_model_json['customizations'] = [acoustic_model_model]

        # Construct a model instance of AcousticModels by calling from_dict on the json representation
        acoustic_models_model = AcousticModels.from_dict(acoustic_models_model_json)
        assert acoustic_models_model != False

        # Construct a model instance of AcousticModels by calling from_dict on the json representation
        acoustic_models_model_dict = AcousticModels.from_dict(acoustic_models_model_json).__dict__
        acoustic_models_model2 = AcousticModels(**acoustic_models_model_dict)

        # Verify the model instances are equivalent
        assert acoustic_models_model == acoustic_models_model2

        # Convert model instance back to dict and verify no loss of data
        acoustic_models_model_json2 = acoustic_models_model.to_dict()
        assert acoustic_models_model_json2 == acoustic_models_model_json

class TestModel_AudioDetails():
    """
    Test Class for AudioDetails
    """

    def test_audio_details_serialization(self):
        """
        Test serialization/deserialization for AudioDetails
        """

        # Construct a json representation of a AudioDetails model
        audio_details_model_json = {}
        audio_details_model_json['type'] = 'audio'
        audio_details_model_json['codec'] = 'testString'
        audio_details_model_json['frequency'] = 38
        audio_details_model_json['compression'] = 'zip'

        # Construct a model instance of AudioDetails by calling from_dict on the json representation
        audio_details_model = AudioDetails.from_dict(audio_details_model_json)
        assert audio_details_model != False

        # Construct a model instance of AudioDetails by calling from_dict on the json representation
        audio_details_model_dict = AudioDetails.from_dict(audio_details_model_json).__dict__
        audio_details_model2 = AudioDetails(**audio_details_model_dict)

        # Verify the model instances are equivalent
        assert audio_details_model == audio_details_model2

        # Convert model instance back to dict and verify no loss of data
        audio_details_model_json2 = audio_details_model.to_dict()
        assert audio_details_model_json2 == audio_details_model_json

class TestModel_AudioListing():
    """
    Test Class for AudioListing
    """

    def test_audio_listing_serialization(self):
        """
        Test serialization/deserialization for AudioListing
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audio_details_model = {} # AudioDetails
        audio_details_model['type'] = 'audio'
        audio_details_model['codec'] = 'testString'
        audio_details_model['frequency'] = 38
        audio_details_model['compression'] = 'zip'

        audio_resource_model = {} # AudioResource
        audio_resource_model['duration'] = 38
        audio_resource_model['name'] = 'testString'
        audio_resource_model['details'] = audio_details_model
        audio_resource_model['status'] = 'ok'

        # Construct a json representation of a AudioListing model
        audio_listing_model_json = {}
        audio_listing_model_json['duration'] = 38
        audio_listing_model_json['name'] = 'testString'
        audio_listing_model_json['details'] = audio_details_model
        audio_listing_model_json['status'] = 'ok'
        audio_listing_model_json['container'] = audio_resource_model
        audio_listing_model_json['audio'] = [audio_resource_model]

        # Construct a model instance of AudioListing by calling from_dict on the json representation
        audio_listing_model = AudioListing.from_dict(audio_listing_model_json)
        assert audio_listing_model != False

        # Construct a model instance of AudioListing by calling from_dict on the json representation
        audio_listing_model_dict = AudioListing.from_dict(audio_listing_model_json).__dict__
        audio_listing_model2 = AudioListing(**audio_listing_model_dict)

        # Verify the model instances are equivalent
        assert audio_listing_model == audio_listing_model2

        # Convert model instance back to dict and verify no loss of data
        audio_listing_model_json2 = audio_listing_model.to_dict()
        assert audio_listing_model_json2 == audio_listing_model_json

class TestModel_AudioMetrics():
    """
    Test Class for AudioMetrics
    """

    def test_audio_metrics_serialization(self):
        """
        Test serialization/deserialization for AudioMetrics
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audio_metrics_histogram_bin_model = {} # AudioMetricsHistogramBin
        audio_metrics_histogram_bin_model['begin'] = 72.5
        audio_metrics_histogram_bin_model['end'] = 72.5
        audio_metrics_histogram_bin_model['count'] = 38

        audio_metrics_details_model = {} # AudioMetricsDetails
        audio_metrics_details_model['final'] = True
        audio_metrics_details_model['end_time'] = 72.5
        audio_metrics_details_model['signal_to_noise_ratio'] = 72.5
        audio_metrics_details_model['speech_ratio'] = 72.5
        audio_metrics_details_model['high_frequency_loss'] = 72.5
        audio_metrics_details_model['direct_current_offset'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['clipping_rate'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['speech_level'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['non_speech_level'] = [audio_metrics_histogram_bin_model]

        # Construct a json representation of a AudioMetrics model
        audio_metrics_model_json = {}
        audio_metrics_model_json['sampling_interval'] = 72.5
        audio_metrics_model_json['accumulated'] = audio_metrics_details_model

        # Construct a model instance of AudioMetrics by calling from_dict on the json representation
        audio_metrics_model = AudioMetrics.from_dict(audio_metrics_model_json)
        assert audio_metrics_model != False

        # Construct a model instance of AudioMetrics by calling from_dict on the json representation
        audio_metrics_model_dict = AudioMetrics.from_dict(audio_metrics_model_json).__dict__
        audio_metrics_model2 = AudioMetrics(**audio_metrics_model_dict)

        # Verify the model instances are equivalent
        assert audio_metrics_model == audio_metrics_model2

        # Convert model instance back to dict and verify no loss of data
        audio_metrics_model_json2 = audio_metrics_model.to_dict()
        assert audio_metrics_model_json2 == audio_metrics_model_json

class TestModel_AudioMetricsDetails():
    """
    Test Class for AudioMetricsDetails
    """

    def test_audio_metrics_details_serialization(self):
        """
        Test serialization/deserialization for AudioMetricsDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audio_metrics_histogram_bin_model = {} # AudioMetricsHistogramBin
        audio_metrics_histogram_bin_model['begin'] = 72.5
        audio_metrics_histogram_bin_model['end'] = 72.5
        audio_metrics_histogram_bin_model['count'] = 38

        # Construct a json representation of a AudioMetricsDetails model
        audio_metrics_details_model_json = {}
        audio_metrics_details_model_json['final'] = True
        audio_metrics_details_model_json['end_time'] = 72.5
        audio_metrics_details_model_json['signal_to_noise_ratio'] = 72.5
        audio_metrics_details_model_json['speech_ratio'] = 72.5
        audio_metrics_details_model_json['high_frequency_loss'] = 72.5
        audio_metrics_details_model_json['direct_current_offset'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model_json['clipping_rate'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model_json['speech_level'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model_json['non_speech_level'] = [audio_metrics_histogram_bin_model]

        # Construct a model instance of AudioMetricsDetails by calling from_dict on the json representation
        audio_metrics_details_model = AudioMetricsDetails.from_dict(audio_metrics_details_model_json)
        assert audio_metrics_details_model != False

        # Construct a model instance of AudioMetricsDetails by calling from_dict on the json representation
        audio_metrics_details_model_dict = AudioMetricsDetails.from_dict(audio_metrics_details_model_json).__dict__
        audio_metrics_details_model2 = AudioMetricsDetails(**audio_metrics_details_model_dict)

        # Verify the model instances are equivalent
        assert audio_metrics_details_model == audio_metrics_details_model2

        # Convert model instance back to dict and verify no loss of data
        audio_metrics_details_model_json2 = audio_metrics_details_model.to_dict()
        assert audio_metrics_details_model_json2 == audio_metrics_details_model_json

class TestModel_AudioMetricsHistogramBin():
    """
    Test Class for AudioMetricsHistogramBin
    """

    def test_audio_metrics_histogram_bin_serialization(self):
        """
        Test serialization/deserialization for AudioMetricsHistogramBin
        """

        # Construct a json representation of a AudioMetricsHistogramBin model
        audio_metrics_histogram_bin_model_json = {}
        audio_metrics_histogram_bin_model_json['begin'] = 72.5
        audio_metrics_histogram_bin_model_json['end'] = 72.5
        audio_metrics_histogram_bin_model_json['count'] = 38

        # Construct a model instance of AudioMetricsHistogramBin by calling from_dict on the json representation
        audio_metrics_histogram_bin_model = AudioMetricsHistogramBin.from_dict(audio_metrics_histogram_bin_model_json)
        assert audio_metrics_histogram_bin_model != False

        # Construct a model instance of AudioMetricsHistogramBin by calling from_dict on the json representation
        audio_metrics_histogram_bin_model_dict = AudioMetricsHistogramBin.from_dict(audio_metrics_histogram_bin_model_json).__dict__
        audio_metrics_histogram_bin_model2 = AudioMetricsHistogramBin(**audio_metrics_histogram_bin_model_dict)

        # Verify the model instances are equivalent
        assert audio_metrics_histogram_bin_model == audio_metrics_histogram_bin_model2

        # Convert model instance back to dict and verify no loss of data
        audio_metrics_histogram_bin_model_json2 = audio_metrics_histogram_bin_model.to_dict()
        assert audio_metrics_histogram_bin_model_json2 == audio_metrics_histogram_bin_model_json

class TestModel_AudioResource():
    """
    Test Class for AudioResource
    """

    def test_audio_resource_serialization(self):
        """
        Test serialization/deserialization for AudioResource
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audio_details_model = {} # AudioDetails
        audio_details_model['type'] = 'audio'
        audio_details_model['codec'] = 'testString'
        audio_details_model['frequency'] = 38
        audio_details_model['compression'] = 'zip'

        # Construct a json representation of a AudioResource model
        audio_resource_model_json = {}
        audio_resource_model_json['duration'] = 38
        audio_resource_model_json['name'] = 'testString'
        audio_resource_model_json['details'] = audio_details_model
        audio_resource_model_json['status'] = 'ok'

        # Construct a model instance of AudioResource by calling from_dict on the json representation
        audio_resource_model = AudioResource.from_dict(audio_resource_model_json)
        assert audio_resource_model != False

        # Construct a model instance of AudioResource by calling from_dict on the json representation
        audio_resource_model_dict = AudioResource.from_dict(audio_resource_model_json).__dict__
        audio_resource_model2 = AudioResource(**audio_resource_model_dict)

        # Verify the model instances are equivalent
        assert audio_resource_model == audio_resource_model2

        # Convert model instance back to dict and verify no loss of data
        audio_resource_model_json2 = audio_resource_model.to_dict()
        assert audio_resource_model_json2 == audio_resource_model_json

class TestModel_AudioResources():
    """
    Test Class for AudioResources
    """

    def test_audio_resources_serialization(self):
        """
        Test serialization/deserialization for AudioResources
        """

        # Construct dict forms of any model objects needed in order to build this model.

        audio_details_model = {} # AudioDetails
        audio_details_model['type'] = 'audio'
        audio_details_model['codec'] = 'testString'
        audio_details_model['frequency'] = 38
        audio_details_model['compression'] = 'zip'

        audio_resource_model = {} # AudioResource
        audio_resource_model['duration'] = 38
        audio_resource_model['name'] = 'testString'
        audio_resource_model['details'] = audio_details_model
        audio_resource_model['status'] = 'ok'

        # Construct a json representation of a AudioResources model
        audio_resources_model_json = {}
        audio_resources_model_json['total_minutes_of_audio'] = 72.5
        audio_resources_model_json['audio'] = [audio_resource_model]

        # Construct a model instance of AudioResources by calling from_dict on the json representation
        audio_resources_model = AudioResources.from_dict(audio_resources_model_json)
        assert audio_resources_model != False

        # Construct a model instance of AudioResources by calling from_dict on the json representation
        audio_resources_model_dict = AudioResources.from_dict(audio_resources_model_json).__dict__
        audio_resources_model2 = AudioResources(**audio_resources_model_dict)

        # Verify the model instances are equivalent
        assert audio_resources_model == audio_resources_model2

        # Convert model instance back to dict and verify no loss of data
        audio_resources_model_json2 = audio_resources_model.to_dict()
        assert audio_resources_model_json2 == audio_resources_model_json

class TestModel_Corpora():
    """
    Test Class for Corpora
    """

    def test_corpora_serialization(self):
        """
        Test serialization/deserialization for Corpora
        """

        # Construct dict forms of any model objects needed in order to build this model.

        corpus_model = {} # Corpus
        corpus_model['name'] = 'testString'
        corpus_model['total_words'] = 38
        corpus_model['out_of_vocabulary_words'] = 38
        corpus_model['status'] = 'analyzed'
        corpus_model['error'] = 'testString'

        # Construct a json representation of a Corpora model
        corpora_model_json = {}
        corpora_model_json['corpora'] = [corpus_model]

        # Construct a model instance of Corpora by calling from_dict on the json representation
        corpora_model = Corpora.from_dict(corpora_model_json)
        assert corpora_model != False

        # Construct a model instance of Corpora by calling from_dict on the json representation
        corpora_model_dict = Corpora.from_dict(corpora_model_json).__dict__
        corpora_model2 = Corpora(**corpora_model_dict)

        # Verify the model instances are equivalent
        assert corpora_model == corpora_model2

        # Convert model instance back to dict and verify no loss of data
        corpora_model_json2 = corpora_model.to_dict()
        assert corpora_model_json2 == corpora_model_json

class TestModel_Corpus():
    """
    Test Class for Corpus
    """

    def test_corpus_serialization(self):
        """
        Test serialization/deserialization for Corpus
        """

        # Construct a json representation of a Corpus model
        corpus_model_json = {}
        corpus_model_json['name'] = 'testString'
        corpus_model_json['total_words'] = 38
        corpus_model_json['out_of_vocabulary_words'] = 38
        corpus_model_json['status'] = 'analyzed'
        corpus_model_json['error'] = 'testString'

        # Construct a model instance of Corpus by calling from_dict on the json representation
        corpus_model = Corpus.from_dict(corpus_model_json)
        assert corpus_model != False

        # Construct a model instance of Corpus by calling from_dict on the json representation
        corpus_model_dict = Corpus.from_dict(corpus_model_json).__dict__
        corpus_model2 = Corpus(**corpus_model_dict)

        # Verify the model instances are equivalent
        assert corpus_model == corpus_model2

        # Convert model instance back to dict and verify no loss of data
        corpus_model_json2 = corpus_model.to_dict()
        assert corpus_model_json2 == corpus_model_json

class TestModel_CustomWord():
    """
    Test Class for CustomWord
    """

    def test_custom_word_serialization(self):
        """
        Test serialization/deserialization for CustomWord
        """

        # Construct a json representation of a CustomWord model
        custom_word_model_json = {}
        custom_word_model_json['word'] = 'testString'
        custom_word_model_json['sounds_like'] = ['testString']
        custom_word_model_json['display_as'] = 'testString'

        # Construct a model instance of CustomWord by calling from_dict on the json representation
        custom_word_model = CustomWord.from_dict(custom_word_model_json)
        assert custom_word_model != False

        # Construct a model instance of CustomWord by calling from_dict on the json representation
        custom_word_model_dict = CustomWord.from_dict(custom_word_model_json).__dict__
        custom_word_model2 = CustomWord(**custom_word_model_dict)

        # Verify the model instances are equivalent
        assert custom_word_model == custom_word_model2

        # Convert model instance back to dict and verify no loss of data
        custom_word_model_json2 = custom_word_model.to_dict()
        assert custom_word_model_json2 == custom_word_model_json

class TestModel_Grammar():
    """
    Test Class for Grammar
    """

    def test_grammar_serialization(self):
        """
        Test serialization/deserialization for Grammar
        """

        # Construct a json representation of a Grammar model
        grammar_model_json = {}
        grammar_model_json['name'] = 'testString'
        grammar_model_json['out_of_vocabulary_words'] = 38
        grammar_model_json['status'] = 'analyzed'
        grammar_model_json['error'] = 'testString'

        # Construct a model instance of Grammar by calling from_dict on the json representation
        grammar_model = Grammar.from_dict(grammar_model_json)
        assert grammar_model != False

        # Construct a model instance of Grammar by calling from_dict on the json representation
        grammar_model_dict = Grammar.from_dict(grammar_model_json).__dict__
        grammar_model2 = Grammar(**grammar_model_dict)

        # Verify the model instances are equivalent
        assert grammar_model == grammar_model2

        # Convert model instance back to dict and verify no loss of data
        grammar_model_json2 = grammar_model.to_dict()
        assert grammar_model_json2 == grammar_model_json

class TestModel_Grammars():
    """
    Test Class for Grammars
    """

    def test_grammars_serialization(self):
        """
        Test serialization/deserialization for Grammars
        """

        # Construct dict forms of any model objects needed in order to build this model.

        grammar_model = {} # Grammar
        grammar_model['name'] = 'testString'
        grammar_model['out_of_vocabulary_words'] = 38
        grammar_model['status'] = 'analyzed'
        grammar_model['error'] = 'testString'

        # Construct a json representation of a Grammars model
        grammars_model_json = {}
        grammars_model_json['grammars'] = [grammar_model]

        # Construct a model instance of Grammars by calling from_dict on the json representation
        grammars_model = Grammars.from_dict(grammars_model_json)
        assert grammars_model != False

        # Construct a model instance of Grammars by calling from_dict on the json representation
        grammars_model_dict = Grammars.from_dict(grammars_model_json).__dict__
        grammars_model2 = Grammars(**grammars_model_dict)

        # Verify the model instances are equivalent
        assert grammars_model == grammars_model2

        # Convert model instance back to dict and verify no loss of data
        grammars_model_json2 = grammars_model.to_dict()
        assert grammars_model_json2 == grammars_model_json

class TestModel_KeywordResult():
    """
    Test Class for KeywordResult
    """

    def test_keyword_result_serialization(self):
        """
        Test serialization/deserialization for KeywordResult
        """

        # Construct a json representation of a KeywordResult model
        keyword_result_model_json = {}
        keyword_result_model_json['normalized_text'] = 'testString'
        keyword_result_model_json['start_time'] = 72.5
        keyword_result_model_json['end_time'] = 72.5
        keyword_result_model_json['confidence'] = 0

        # Construct a model instance of KeywordResult by calling from_dict on the json representation
        keyword_result_model = KeywordResult.from_dict(keyword_result_model_json)
        assert keyword_result_model != False

        # Construct a model instance of KeywordResult by calling from_dict on the json representation
        keyword_result_model_dict = KeywordResult.from_dict(keyword_result_model_json).__dict__
        keyword_result_model2 = KeywordResult(**keyword_result_model_dict)

        # Verify the model instances are equivalent
        assert keyword_result_model == keyword_result_model2

        # Convert model instance back to dict and verify no loss of data
        keyword_result_model_json2 = keyword_result_model.to_dict()
        assert keyword_result_model_json2 == keyword_result_model_json

class TestModel_LanguageModel():
    """
    Test Class for LanguageModel
    """

    def test_language_model_serialization(self):
        """
        Test serialization/deserialization for LanguageModel
        """

        # Construct a json representation of a LanguageModel model
        language_model_model_json = {}
        language_model_model_json['customization_id'] = 'testString'
        language_model_model_json['created'] = 'testString'
        language_model_model_json['updated'] = 'testString'
        language_model_model_json['language'] = 'testString'
        language_model_model_json['dialect'] = 'testString'
        language_model_model_json['versions'] = ['testString']
        language_model_model_json['owner'] = 'testString'
        language_model_model_json['name'] = 'testString'
        language_model_model_json['description'] = 'testString'
        language_model_model_json['base_model_name'] = 'testString'
        language_model_model_json['status'] = 'pending'
        language_model_model_json['progress'] = 38
        language_model_model_json['error'] = 'testString'
        language_model_model_json['warnings'] = 'testString'

        # Construct a model instance of LanguageModel by calling from_dict on the json representation
        language_model_model = LanguageModel.from_dict(language_model_model_json)
        assert language_model_model != False

        # Construct a model instance of LanguageModel by calling from_dict on the json representation
        language_model_model_dict = LanguageModel.from_dict(language_model_model_json).__dict__
        language_model_model2 = LanguageModel(**language_model_model_dict)

        # Verify the model instances are equivalent
        assert language_model_model == language_model_model2

        # Convert model instance back to dict and verify no loss of data
        language_model_model_json2 = language_model_model.to_dict()
        assert language_model_model_json2 == language_model_model_json

class TestModel_LanguageModels():
    """
    Test Class for LanguageModels
    """

    def test_language_models_serialization(self):
        """
        Test serialization/deserialization for LanguageModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        language_model_model = {} # LanguageModel
        language_model_model['customization_id'] = 'testString'
        language_model_model['created'] = 'testString'
        language_model_model['updated'] = 'testString'
        language_model_model['language'] = 'testString'
        language_model_model['dialect'] = 'testString'
        language_model_model['versions'] = ['testString']
        language_model_model['owner'] = 'testString'
        language_model_model['name'] = 'testString'
        language_model_model['description'] = 'testString'
        language_model_model['base_model_name'] = 'testString'
        language_model_model['status'] = 'pending'
        language_model_model['progress'] = 38
        language_model_model['error'] = 'testString'
        language_model_model['warnings'] = 'testString'

        # Construct a json representation of a LanguageModels model
        language_models_model_json = {}
        language_models_model_json['customizations'] = [language_model_model]

        # Construct a model instance of LanguageModels by calling from_dict on the json representation
        language_models_model = LanguageModels.from_dict(language_models_model_json)
        assert language_models_model != False

        # Construct a model instance of LanguageModels by calling from_dict on the json representation
        language_models_model_dict = LanguageModels.from_dict(language_models_model_json).__dict__
        language_models_model2 = LanguageModels(**language_models_model_dict)

        # Verify the model instances are equivalent
        assert language_models_model == language_models_model2

        # Convert model instance back to dict and verify no loss of data
        language_models_model_json2 = language_models_model.to_dict()
        assert language_models_model_json2 == language_models_model_json

class TestModel_ProcessedAudio():
    """
    Test Class for ProcessedAudio
    """

    def test_processed_audio_serialization(self):
        """
        Test serialization/deserialization for ProcessedAudio
        """

        # Construct a json representation of a ProcessedAudio model
        processed_audio_model_json = {}
        processed_audio_model_json['received'] = 72.5
        processed_audio_model_json['seen_by_engine'] = 72.5
        processed_audio_model_json['transcription'] = 72.5
        processed_audio_model_json['speaker_labels'] = 72.5

        # Construct a model instance of ProcessedAudio by calling from_dict on the json representation
        processed_audio_model = ProcessedAudio.from_dict(processed_audio_model_json)
        assert processed_audio_model != False

        # Construct a model instance of ProcessedAudio by calling from_dict on the json representation
        processed_audio_model_dict = ProcessedAudio.from_dict(processed_audio_model_json).__dict__
        processed_audio_model2 = ProcessedAudio(**processed_audio_model_dict)

        # Verify the model instances are equivalent
        assert processed_audio_model == processed_audio_model2

        # Convert model instance back to dict and verify no loss of data
        processed_audio_model_json2 = processed_audio_model.to_dict()
        assert processed_audio_model_json2 == processed_audio_model_json

class TestModel_ProcessingMetrics():
    """
    Test Class for ProcessingMetrics
    """

    def test_processing_metrics_serialization(self):
        """
        Test serialization/deserialization for ProcessingMetrics
        """

        # Construct dict forms of any model objects needed in order to build this model.

        processed_audio_model = {} # ProcessedAudio
        processed_audio_model['received'] = 72.5
        processed_audio_model['seen_by_engine'] = 72.5
        processed_audio_model['transcription'] = 72.5
        processed_audio_model['speaker_labels'] = 72.5

        # Construct a json representation of a ProcessingMetrics model
        processing_metrics_model_json = {}
        processing_metrics_model_json['processed_audio'] = processed_audio_model
        processing_metrics_model_json['wall_clock_since_first_byte_received'] = 72.5
        processing_metrics_model_json['periodic'] = True

        # Construct a model instance of ProcessingMetrics by calling from_dict on the json representation
        processing_metrics_model = ProcessingMetrics.from_dict(processing_metrics_model_json)
        assert processing_metrics_model != False

        # Construct a model instance of ProcessingMetrics by calling from_dict on the json representation
        processing_metrics_model_dict = ProcessingMetrics.from_dict(processing_metrics_model_json).__dict__
        processing_metrics_model2 = ProcessingMetrics(**processing_metrics_model_dict)

        # Verify the model instances are equivalent
        assert processing_metrics_model == processing_metrics_model2

        # Convert model instance back to dict and verify no loss of data
        processing_metrics_model_json2 = processing_metrics_model.to_dict()
        assert processing_metrics_model_json2 == processing_metrics_model_json

class TestModel_RecognitionJob():
    """
    Test Class for RecognitionJob
    """

    def test_recognition_job_serialization(self):
        """
        Test serialization/deserialization for RecognitionJob
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speech_recognition_alternative_model = {} # SpeechRecognitionAlternative
        speech_recognition_alternative_model['transcript'] = 'testString'
        speech_recognition_alternative_model['confidence'] = 0
        speech_recognition_alternative_model['timestamps'] = ['testString']
        speech_recognition_alternative_model['word_confidence'] = ['testString']

        keyword_result_model = {} # KeywordResult
        keyword_result_model['normalized_text'] = 'testString'
        keyword_result_model['start_time'] = 72.5
        keyword_result_model['end_time'] = 72.5
        keyword_result_model['confidence'] = 0

        word_alternative_result_model = {} # WordAlternativeResult
        word_alternative_result_model['confidence'] = 0
        word_alternative_result_model['word'] = 'testString'

        word_alternative_results_model = {} # WordAlternativeResults
        word_alternative_results_model['start_time'] = 72.5
        word_alternative_results_model['end_time'] = 72.5
        word_alternative_results_model['alternatives'] = [word_alternative_result_model]

        speech_recognition_result_model = {} # SpeechRecognitionResult
        speech_recognition_result_model['final'] = True
        speech_recognition_result_model['alternatives'] = [speech_recognition_alternative_model]
        speech_recognition_result_model['keywords_result'] = {}
        speech_recognition_result_model['word_alternatives'] = [word_alternative_results_model]
        speech_recognition_result_model['end_of_utterance'] = 'end_of_data'

        speaker_labels_result_model = {} # SpeakerLabelsResult
        speaker_labels_result_model['from'] = 72.5
        speaker_labels_result_model['to'] = 72.5
        speaker_labels_result_model['speaker'] = 38
        speaker_labels_result_model['confidence'] = 72.5
        speaker_labels_result_model['final'] = True

        processed_audio_model = {} # ProcessedAudio
        processed_audio_model['received'] = 72.5
        processed_audio_model['seen_by_engine'] = 72.5
        processed_audio_model['transcription'] = 72.5
        processed_audio_model['speaker_labels'] = 72.5

        processing_metrics_model = {} # ProcessingMetrics
        processing_metrics_model['processed_audio'] = processed_audio_model
        processing_metrics_model['wall_clock_since_first_byte_received'] = 72.5
        processing_metrics_model['periodic'] = True

        audio_metrics_histogram_bin_model = {} # AudioMetricsHistogramBin
        audio_metrics_histogram_bin_model['begin'] = 72.5
        audio_metrics_histogram_bin_model['end'] = 72.5
        audio_metrics_histogram_bin_model['count'] = 38

        audio_metrics_details_model = {} # AudioMetricsDetails
        audio_metrics_details_model['final'] = True
        audio_metrics_details_model['end_time'] = 72.5
        audio_metrics_details_model['signal_to_noise_ratio'] = 72.5
        audio_metrics_details_model['speech_ratio'] = 72.5
        audio_metrics_details_model['high_frequency_loss'] = 72.5
        audio_metrics_details_model['direct_current_offset'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['clipping_rate'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['speech_level'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['non_speech_level'] = [audio_metrics_histogram_bin_model]

        audio_metrics_model = {} # AudioMetrics
        audio_metrics_model['sampling_interval'] = 72.5
        audio_metrics_model['accumulated'] = audio_metrics_details_model

        speech_recognition_results_model = {} # SpeechRecognitionResults
        speech_recognition_results_model['results'] = [speech_recognition_result_model]
        speech_recognition_results_model['result_index'] = 38
        speech_recognition_results_model['speaker_labels'] = [speaker_labels_result_model]
        speech_recognition_results_model['processing_metrics'] = processing_metrics_model
        speech_recognition_results_model['audio_metrics'] = audio_metrics_model
        speech_recognition_results_model['warnings'] = ['testString']

        # Construct a json representation of a RecognitionJob model
        recognition_job_model_json = {}
        recognition_job_model_json['id'] = 'testString'
        recognition_job_model_json['status'] = 'waiting'
        recognition_job_model_json['created'] = 'testString'
        recognition_job_model_json['updated'] = 'testString'
        recognition_job_model_json['url'] = 'testString'
        recognition_job_model_json['user_token'] = 'testString'
        recognition_job_model_json['results'] = [speech_recognition_results_model]
        recognition_job_model_json['warnings'] = ['testString']

        # Construct a model instance of RecognitionJob by calling from_dict on the json representation
        recognition_job_model = RecognitionJob.from_dict(recognition_job_model_json)
        assert recognition_job_model != False

        # Construct a model instance of RecognitionJob by calling from_dict on the json representation
        recognition_job_model_dict = RecognitionJob.from_dict(recognition_job_model_json).__dict__
        recognition_job_model2 = RecognitionJob(**recognition_job_model_dict)

        # Verify the model instances are equivalent
        assert recognition_job_model == recognition_job_model2

        # Convert model instance back to dict and verify no loss of data
        recognition_job_model_json2 = recognition_job_model.to_dict()
        assert recognition_job_model_json2 == recognition_job_model_json

class TestModel_RecognitionJobs():
    """
    Test Class for RecognitionJobs
    """

    def test_recognition_jobs_serialization(self):
        """
        Test serialization/deserialization for RecognitionJobs
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speech_recognition_alternative_model = {} # SpeechRecognitionAlternative
        speech_recognition_alternative_model['transcript'] = 'testString'
        speech_recognition_alternative_model['confidence'] = 0
        speech_recognition_alternative_model['timestamps'] = ['testString']
        speech_recognition_alternative_model['word_confidence'] = ['testString']

        keyword_result_model = {} # KeywordResult
        keyword_result_model['normalized_text'] = 'testString'
        keyword_result_model['start_time'] = 72.5
        keyword_result_model['end_time'] = 72.5
        keyword_result_model['confidence'] = 0

        word_alternative_result_model = {} # WordAlternativeResult
        word_alternative_result_model['confidence'] = 0
        word_alternative_result_model['word'] = 'testString'

        word_alternative_results_model = {} # WordAlternativeResults
        word_alternative_results_model['start_time'] = 72.5
        word_alternative_results_model['end_time'] = 72.5
        word_alternative_results_model['alternatives'] = [word_alternative_result_model]

        speech_recognition_result_model = {} # SpeechRecognitionResult
        speech_recognition_result_model['final'] = True
        speech_recognition_result_model['alternatives'] = [speech_recognition_alternative_model]
        speech_recognition_result_model['keywords_result'] = {}
        speech_recognition_result_model['word_alternatives'] = [word_alternative_results_model]
        speech_recognition_result_model['end_of_utterance'] = 'end_of_data'

        speaker_labels_result_model = {} # SpeakerLabelsResult
        speaker_labels_result_model['from'] = 72.5
        speaker_labels_result_model['to'] = 72.5
        speaker_labels_result_model['speaker'] = 38
        speaker_labels_result_model['confidence'] = 72.5
        speaker_labels_result_model['final'] = True

        processed_audio_model = {} # ProcessedAudio
        processed_audio_model['received'] = 72.5
        processed_audio_model['seen_by_engine'] = 72.5
        processed_audio_model['transcription'] = 72.5
        processed_audio_model['speaker_labels'] = 72.5

        processing_metrics_model = {} # ProcessingMetrics
        processing_metrics_model['processed_audio'] = processed_audio_model
        processing_metrics_model['wall_clock_since_first_byte_received'] = 72.5
        processing_metrics_model['periodic'] = True

        audio_metrics_histogram_bin_model = {} # AudioMetricsHistogramBin
        audio_metrics_histogram_bin_model['begin'] = 72.5
        audio_metrics_histogram_bin_model['end'] = 72.5
        audio_metrics_histogram_bin_model['count'] = 38

        audio_metrics_details_model = {} # AudioMetricsDetails
        audio_metrics_details_model['final'] = True
        audio_metrics_details_model['end_time'] = 72.5
        audio_metrics_details_model['signal_to_noise_ratio'] = 72.5
        audio_metrics_details_model['speech_ratio'] = 72.5
        audio_metrics_details_model['high_frequency_loss'] = 72.5
        audio_metrics_details_model['direct_current_offset'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['clipping_rate'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['speech_level'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['non_speech_level'] = [audio_metrics_histogram_bin_model]

        audio_metrics_model = {} # AudioMetrics
        audio_metrics_model['sampling_interval'] = 72.5
        audio_metrics_model['accumulated'] = audio_metrics_details_model

        speech_recognition_results_model = {} # SpeechRecognitionResults
        speech_recognition_results_model['results'] = [speech_recognition_result_model]
        speech_recognition_results_model['result_index'] = 38
        speech_recognition_results_model['speaker_labels'] = [speaker_labels_result_model]
        speech_recognition_results_model['processing_metrics'] = processing_metrics_model
        speech_recognition_results_model['audio_metrics'] = audio_metrics_model
        speech_recognition_results_model['warnings'] = ['testString']

        recognition_job_model = {} # RecognitionJob
        recognition_job_model['id'] = 'testString'
        recognition_job_model['status'] = 'waiting'
        recognition_job_model['created'] = 'testString'
        recognition_job_model['updated'] = 'testString'
        recognition_job_model['url'] = 'testString'
        recognition_job_model['user_token'] = 'testString'
        recognition_job_model['results'] = [speech_recognition_results_model]
        recognition_job_model['warnings'] = ['testString']

        # Construct a json representation of a RecognitionJobs model
        recognition_jobs_model_json = {}
        recognition_jobs_model_json['recognitions'] = [recognition_job_model]

        # Construct a model instance of RecognitionJobs by calling from_dict on the json representation
        recognition_jobs_model = RecognitionJobs.from_dict(recognition_jobs_model_json)
        assert recognition_jobs_model != False

        # Construct a model instance of RecognitionJobs by calling from_dict on the json representation
        recognition_jobs_model_dict = RecognitionJobs.from_dict(recognition_jobs_model_json).__dict__
        recognition_jobs_model2 = RecognitionJobs(**recognition_jobs_model_dict)

        # Verify the model instances are equivalent
        assert recognition_jobs_model == recognition_jobs_model2

        # Convert model instance back to dict and verify no loss of data
        recognition_jobs_model_json2 = recognition_jobs_model.to_dict()
        assert recognition_jobs_model_json2 == recognition_jobs_model_json

class TestModel_RegisterStatus():
    """
    Test Class for RegisterStatus
    """

    def test_register_status_serialization(self):
        """
        Test serialization/deserialization for RegisterStatus
        """

        # Construct a json representation of a RegisterStatus model
        register_status_model_json = {}
        register_status_model_json['status'] = 'created'
        register_status_model_json['url'] = 'testString'

        # Construct a model instance of RegisterStatus by calling from_dict on the json representation
        register_status_model = RegisterStatus.from_dict(register_status_model_json)
        assert register_status_model != False

        # Construct a model instance of RegisterStatus by calling from_dict on the json representation
        register_status_model_dict = RegisterStatus.from_dict(register_status_model_json).__dict__
        register_status_model2 = RegisterStatus(**register_status_model_dict)

        # Verify the model instances are equivalent
        assert register_status_model == register_status_model2

        # Convert model instance back to dict and verify no loss of data
        register_status_model_json2 = register_status_model.to_dict()
        assert register_status_model_json2 == register_status_model_json

class TestModel_SpeakerLabelsResult():
    """
    Test Class for SpeakerLabelsResult
    """

    def test_speaker_labels_result_serialization(self):
        """
        Test serialization/deserialization for SpeakerLabelsResult
        """

        # Construct a json representation of a SpeakerLabelsResult model
        speaker_labels_result_model_json = {}
        speaker_labels_result_model_json['from'] = 72.5
        speaker_labels_result_model_json['to'] = 72.5
        speaker_labels_result_model_json['speaker'] = 38
        speaker_labels_result_model_json['confidence'] = 72.5
        speaker_labels_result_model_json['final'] = True

        # Construct a model instance of SpeakerLabelsResult by calling from_dict on the json representation
        speaker_labels_result_model = SpeakerLabelsResult.from_dict(speaker_labels_result_model_json)
        assert speaker_labels_result_model != False

        # Construct a model instance of SpeakerLabelsResult by calling from_dict on the json representation
        speaker_labels_result_model_dict = SpeakerLabelsResult.from_dict(speaker_labels_result_model_json).__dict__
        speaker_labels_result_model2 = SpeakerLabelsResult(**speaker_labels_result_model_dict)

        # Verify the model instances are equivalent
        assert speaker_labels_result_model == speaker_labels_result_model2

        # Convert model instance back to dict and verify no loss of data
        speaker_labels_result_model_json2 = speaker_labels_result_model.to_dict()
        assert speaker_labels_result_model_json2 == speaker_labels_result_model_json

class TestModel_SpeechModel():
    """
    Test Class for SpeechModel
    """

    def test_speech_model_serialization(self):
        """
        Test serialization/deserialization for SpeechModel
        """

        # Construct dict forms of any model objects needed in order to build this model.

        supported_features_model = {} # SupportedFeatures
        supported_features_model['custom_language_model'] = True
        supported_features_model['speaker_labels'] = True
        supported_features_model['low_latency'] = True

        # Construct a json representation of a SpeechModel model
        speech_model_model_json = {}
        speech_model_model_json['name'] = 'testString'
        speech_model_model_json['language'] = 'testString'
        speech_model_model_json['rate'] = 38
        speech_model_model_json['url'] = 'testString'
        speech_model_model_json['supported_features'] = supported_features_model
        speech_model_model_json['description'] = 'testString'

        # Construct a model instance of SpeechModel by calling from_dict on the json representation
        speech_model_model = SpeechModel.from_dict(speech_model_model_json)
        assert speech_model_model != False

        # Construct a model instance of SpeechModel by calling from_dict on the json representation
        speech_model_model_dict = SpeechModel.from_dict(speech_model_model_json).__dict__
        speech_model_model2 = SpeechModel(**speech_model_model_dict)

        # Verify the model instances are equivalent
        assert speech_model_model == speech_model_model2

        # Convert model instance back to dict and verify no loss of data
        speech_model_model_json2 = speech_model_model.to_dict()
        assert speech_model_model_json2 == speech_model_model_json

class TestModel_SpeechModels():
    """
    Test Class for SpeechModels
    """

    def test_speech_models_serialization(self):
        """
        Test serialization/deserialization for SpeechModels
        """

        # Construct dict forms of any model objects needed in order to build this model.

        supported_features_model = {} # SupportedFeatures
        supported_features_model['custom_language_model'] = True
        supported_features_model['speaker_labels'] = True
        supported_features_model['low_latency'] = True

        speech_model_model = {} # SpeechModel
        speech_model_model['name'] = 'testString'
        speech_model_model['language'] = 'testString'
        speech_model_model['rate'] = 38
        speech_model_model['url'] = 'testString'
        speech_model_model['supported_features'] = supported_features_model
        speech_model_model['description'] = 'testString'

        # Construct a json representation of a SpeechModels model
        speech_models_model_json = {}
        speech_models_model_json['models'] = [speech_model_model]

        # Construct a model instance of SpeechModels by calling from_dict on the json representation
        speech_models_model = SpeechModels.from_dict(speech_models_model_json)
        assert speech_models_model != False

        # Construct a model instance of SpeechModels by calling from_dict on the json representation
        speech_models_model_dict = SpeechModels.from_dict(speech_models_model_json).__dict__
        speech_models_model2 = SpeechModels(**speech_models_model_dict)

        # Verify the model instances are equivalent
        assert speech_models_model == speech_models_model2

        # Convert model instance back to dict and verify no loss of data
        speech_models_model_json2 = speech_models_model.to_dict()
        assert speech_models_model_json2 == speech_models_model_json

class TestModel_SpeechRecognitionAlternative():
    """
    Test Class for SpeechRecognitionAlternative
    """

    def test_speech_recognition_alternative_serialization(self):
        """
        Test serialization/deserialization for SpeechRecognitionAlternative
        """

        # Construct a json representation of a SpeechRecognitionAlternative model
        speech_recognition_alternative_model_json = {}
        speech_recognition_alternative_model_json['transcript'] = 'testString'
        speech_recognition_alternative_model_json['confidence'] = 0
        speech_recognition_alternative_model_json['timestamps'] = ['testString']
        speech_recognition_alternative_model_json['word_confidence'] = ['testString']

        # Construct a model instance of SpeechRecognitionAlternative by calling from_dict on the json representation
        speech_recognition_alternative_model = SpeechRecognitionAlternative.from_dict(speech_recognition_alternative_model_json)
        assert speech_recognition_alternative_model != False

        # Construct a model instance of SpeechRecognitionAlternative by calling from_dict on the json representation
        speech_recognition_alternative_model_dict = SpeechRecognitionAlternative.from_dict(speech_recognition_alternative_model_json).__dict__
        speech_recognition_alternative_model2 = SpeechRecognitionAlternative(**speech_recognition_alternative_model_dict)

        # Verify the model instances are equivalent
        assert speech_recognition_alternative_model == speech_recognition_alternative_model2

        # Convert model instance back to dict and verify no loss of data
        speech_recognition_alternative_model_json2 = speech_recognition_alternative_model.to_dict()
        assert speech_recognition_alternative_model_json2 == speech_recognition_alternative_model_json

class TestModel_SpeechRecognitionResult():
    """
    Test Class for SpeechRecognitionResult
    """

    def test_speech_recognition_result_serialization(self):
        """
        Test serialization/deserialization for SpeechRecognitionResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speech_recognition_alternative_model = {} # SpeechRecognitionAlternative
        speech_recognition_alternative_model['transcript'] = 'testString'
        speech_recognition_alternative_model['confidence'] = 0
        speech_recognition_alternative_model['timestamps'] = ['testString']
        speech_recognition_alternative_model['word_confidence'] = ['testString']

        keyword_result_model = {} # KeywordResult
        keyword_result_model['normalized_text'] = 'testString'
        keyword_result_model['start_time'] = 72.5
        keyword_result_model['end_time'] = 72.5
        keyword_result_model['confidence'] = 0

        word_alternative_result_model = {} # WordAlternativeResult
        word_alternative_result_model['confidence'] = 0
        word_alternative_result_model['word'] = 'testString'

        word_alternative_results_model = {} # WordAlternativeResults
        word_alternative_results_model['start_time'] = 72.5
        word_alternative_results_model['end_time'] = 72.5
        word_alternative_results_model['alternatives'] = [word_alternative_result_model]

        # Construct a json representation of a SpeechRecognitionResult model
        speech_recognition_result_model_json = {}
        speech_recognition_result_model_json['final'] = True
        speech_recognition_result_model_json['alternatives'] = [speech_recognition_alternative_model]
        speech_recognition_result_model_json['keywords_result'] = {}
        speech_recognition_result_model_json['word_alternatives'] = [word_alternative_results_model]
        speech_recognition_result_model_json['end_of_utterance'] = 'end_of_data'

        # Construct a model instance of SpeechRecognitionResult by calling from_dict on the json representation
        speech_recognition_result_model = SpeechRecognitionResult.from_dict(speech_recognition_result_model_json)
        assert speech_recognition_result_model != False

        # Construct a model instance of SpeechRecognitionResult by calling from_dict on the json representation
        speech_recognition_result_model_dict = SpeechRecognitionResult.from_dict(speech_recognition_result_model_json).__dict__
        speech_recognition_result_model2 = SpeechRecognitionResult(**speech_recognition_result_model_dict)

        # Verify the model instances are equivalent
        assert speech_recognition_result_model == speech_recognition_result_model2

        # Convert model instance back to dict and verify no loss of data
        speech_recognition_result_model_json2 = speech_recognition_result_model.to_dict()
        assert speech_recognition_result_model_json2 == speech_recognition_result_model_json

class TestModel_SpeechRecognitionResults():
    """
    Test Class for SpeechRecognitionResults
    """

    def test_speech_recognition_results_serialization(self):
        """
        Test serialization/deserialization for SpeechRecognitionResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        speech_recognition_alternative_model = {} # SpeechRecognitionAlternative
        speech_recognition_alternative_model['transcript'] = 'testString'
        speech_recognition_alternative_model['confidence'] = 0
        speech_recognition_alternative_model['timestamps'] = ['testString']
        speech_recognition_alternative_model['word_confidence'] = ['testString']

        keyword_result_model = {} # KeywordResult
        keyword_result_model['normalized_text'] = 'testString'
        keyword_result_model['start_time'] = 72.5
        keyword_result_model['end_time'] = 72.5
        keyword_result_model['confidence'] = 0

        word_alternative_result_model = {} # WordAlternativeResult
        word_alternative_result_model['confidence'] = 0
        word_alternative_result_model['word'] = 'testString'

        word_alternative_results_model = {} # WordAlternativeResults
        word_alternative_results_model['start_time'] = 72.5
        word_alternative_results_model['end_time'] = 72.5
        word_alternative_results_model['alternatives'] = [word_alternative_result_model]

        speech_recognition_result_model = {} # SpeechRecognitionResult
        speech_recognition_result_model['final'] = True
        speech_recognition_result_model['alternatives'] = [speech_recognition_alternative_model]
        speech_recognition_result_model['keywords_result'] = {}
        speech_recognition_result_model['word_alternatives'] = [word_alternative_results_model]
        speech_recognition_result_model['end_of_utterance'] = 'end_of_data'

        speaker_labels_result_model = {} # SpeakerLabelsResult
        speaker_labels_result_model['from'] = 72.5
        speaker_labels_result_model['to'] = 72.5
        speaker_labels_result_model['speaker'] = 38
        speaker_labels_result_model['confidence'] = 72.5
        speaker_labels_result_model['final'] = True

        processed_audio_model = {} # ProcessedAudio
        processed_audio_model['received'] = 72.5
        processed_audio_model['seen_by_engine'] = 72.5
        processed_audio_model['transcription'] = 72.5
        processed_audio_model['speaker_labels'] = 72.5

        processing_metrics_model = {} # ProcessingMetrics
        processing_metrics_model['processed_audio'] = processed_audio_model
        processing_metrics_model['wall_clock_since_first_byte_received'] = 72.5
        processing_metrics_model['periodic'] = True

        audio_metrics_histogram_bin_model = {} # AudioMetricsHistogramBin
        audio_metrics_histogram_bin_model['begin'] = 72.5
        audio_metrics_histogram_bin_model['end'] = 72.5
        audio_metrics_histogram_bin_model['count'] = 38

        audio_metrics_details_model = {} # AudioMetricsDetails
        audio_metrics_details_model['final'] = True
        audio_metrics_details_model['end_time'] = 72.5
        audio_metrics_details_model['signal_to_noise_ratio'] = 72.5
        audio_metrics_details_model['speech_ratio'] = 72.5
        audio_metrics_details_model['high_frequency_loss'] = 72.5
        audio_metrics_details_model['direct_current_offset'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['clipping_rate'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['speech_level'] = [audio_metrics_histogram_bin_model]
        audio_metrics_details_model['non_speech_level'] = [audio_metrics_histogram_bin_model]

        audio_metrics_model = {} # AudioMetrics
        audio_metrics_model['sampling_interval'] = 72.5
        audio_metrics_model['accumulated'] = audio_metrics_details_model

        # Construct a json representation of a SpeechRecognitionResults model
        speech_recognition_results_model_json = {}
        speech_recognition_results_model_json['results'] = [speech_recognition_result_model]
        speech_recognition_results_model_json['result_index'] = 38
        speech_recognition_results_model_json['speaker_labels'] = [speaker_labels_result_model]
        speech_recognition_results_model_json['processing_metrics'] = processing_metrics_model
        speech_recognition_results_model_json['audio_metrics'] = audio_metrics_model
        speech_recognition_results_model_json['warnings'] = ['testString']

        # Construct a model instance of SpeechRecognitionResults by calling from_dict on the json representation
        speech_recognition_results_model = SpeechRecognitionResults.from_dict(speech_recognition_results_model_json)
        assert speech_recognition_results_model != False

        # Construct a model instance of SpeechRecognitionResults by calling from_dict on the json representation
        speech_recognition_results_model_dict = SpeechRecognitionResults.from_dict(speech_recognition_results_model_json).__dict__
        speech_recognition_results_model2 = SpeechRecognitionResults(**speech_recognition_results_model_dict)

        # Verify the model instances are equivalent
        assert speech_recognition_results_model == speech_recognition_results_model2

        # Convert model instance back to dict and verify no loss of data
        speech_recognition_results_model_json2 = speech_recognition_results_model.to_dict()
        assert speech_recognition_results_model_json2 == speech_recognition_results_model_json

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
        supported_features_model_json['custom_language_model'] = True
        supported_features_model_json['speaker_labels'] = True
        supported_features_model_json['low_latency'] = True

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

class TestModel_TrainingResponse():
    """
    Test Class for TrainingResponse
    """

    def test_training_response_serialization(self):
        """
        Test serialization/deserialization for TrainingResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        training_warning_model = {} # TrainingWarning
        training_warning_model['code'] = 'invalid_audio_files'
        training_warning_model['message'] = 'testString'

        # Construct a json representation of a TrainingResponse model
        training_response_model_json = {}
        training_response_model_json['warnings'] = [training_warning_model]

        # Construct a model instance of TrainingResponse by calling from_dict on the json representation
        training_response_model = TrainingResponse.from_dict(training_response_model_json)
        assert training_response_model != False

        # Construct a model instance of TrainingResponse by calling from_dict on the json representation
        training_response_model_dict = TrainingResponse.from_dict(training_response_model_json).__dict__
        training_response_model2 = TrainingResponse(**training_response_model_dict)

        # Verify the model instances are equivalent
        assert training_response_model == training_response_model2

        # Convert model instance back to dict and verify no loss of data
        training_response_model_json2 = training_response_model.to_dict()
        assert training_response_model_json2 == training_response_model_json

class TestModel_TrainingWarning():
    """
    Test Class for TrainingWarning
    """

    def test_training_warning_serialization(self):
        """
        Test serialization/deserialization for TrainingWarning
        """

        # Construct a json representation of a TrainingWarning model
        training_warning_model_json = {}
        training_warning_model_json['code'] = 'invalid_audio_files'
        training_warning_model_json['message'] = 'testString'

        # Construct a model instance of TrainingWarning by calling from_dict on the json representation
        training_warning_model = TrainingWarning.from_dict(training_warning_model_json)
        assert training_warning_model != False

        # Construct a model instance of TrainingWarning by calling from_dict on the json representation
        training_warning_model_dict = TrainingWarning.from_dict(training_warning_model_json).__dict__
        training_warning_model2 = TrainingWarning(**training_warning_model_dict)

        # Verify the model instances are equivalent
        assert training_warning_model == training_warning_model2

        # Convert model instance back to dict and verify no loss of data
        training_warning_model_json2 = training_warning_model.to_dict()
        assert training_warning_model_json2 == training_warning_model_json

class TestModel_Word():
    """
    Test Class for Word
    """

    def test_word_serialization(self):
        """
        Test serialization/deserialization for Word
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_error_model = {} # WordError
        word_error_model['element'] = 'testString'

        # Construct a json representation of a Word model
        word_model_json = {}
        word_model_json['word'] = 'testString'
        word_model_json['sounds_like'] = ['testString']
        word_model_json['display_as'] = 'testString'
        word_model_json['count'] = 38
        word_model_json['source'] = ['testString']
        word_model_json['error'] = [word_error_model]

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

class TestModel_WordAlternativeResult():
    """
    Test Class for WordAlternativeResult
    """

    def test_word_alternative_result_serialization(self):
        """
        Test serialization/deserialization for WordAlternativeResult
        """

        # Construct a json representation of a WordAlternativeResult model
        word_alternative_result_model_json = {}
        word_alternative_result_model_json['confidence'] = 0
        word_alternative_result_model_json['word'] = 'testString'

        # Construct a model instance of WordAlternativeResult by calling from_dict on the json representation
        word_alternative_result_model = WordAlternativeResult.from_dict(word_alternative_result_model_json)
        assert word_alternative_result_model != False

        # Construct a model instance of WordAlternativeResult by calling from_dict on the json representation
        word_alternative_result_model_dict = WordAlternativeResult.from_dict(word_alternative_result_model_json).__dict__
        word_alternative_result_model2 = WordAlternativeResult(**word_alternative_result_model_dict)

        # Verify the model instances are equivalent
        assert word_alternative_result_model == word_alternative_result_model2

        # Convert model instance back to dict and verify no loss of data
        word_alternative_result_model_json2 = word_alternative_result_model.to_dict()
        assert word_alternative_result_model_json2 == word_alternative_result_model_json

class TestModel_WordAlternativeResults():
    """
    Test Class for WordAlternativeResults
    """

    def test_word_alternative_results_serialization(self):
        """
        Test serialization/deserialization for WordAlternativeResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_alternative_result_model = {} # WordAlternativeResult
        word_alternative_result_model['confidence'] = 0
        word_alternative_result_model['word'] = 'testString'

        # Construct a json representation of a WordAlternativeResults model
        word_alternative_results_model_json = {}
        word_alternative_results_model_json['start_time'] = 72.5
        word_alternative_results_model_json['end_time'] = 72.5
        word_alternative_results_model_json['alternatives'] = [word_alternative_result_model]

        # Construct a model instance of WordAlternativeResults by calling from_dict on the json representation
        word_alternative_results_model = WordAlternativeResults.from_dict(word_alternative_results_model_json)
        assert word_alternative_results_model != False

        # Construct a model instance of WordAlternativeResults by calling from_dict on the json representation
        word_alternative_results_model_dict = WordAlternativeResults.from_dict(word_alternative_results_model_json).__dict__
        word_alternative_results_model2 = WordAlternativeResults(**word_alternative_results_model_dict)

        # Verify the model instances are equivalent
        assert word_alternative_results_model == word_alternative_results_model2

        # Convert model instance back to dict and verify no loss of data
        word_alternative_results_model_json2 = word_alternative_results_model.to_dict()
        assert word_alternative_results_model_json2 == word_alternative_results_model_json

class TestModel_WordError():
    """
    Test Class for WordError
    """

    def test_word_error_serialization(self):
        """
        Test serialization/deserialization for WordError
        """

        # Construct a json representation of a WordError model
        word_error_model_json = {}
        word_error_model_json['element'] = 'testString'

        # Construct a model instance of WordError by calling from_dict on the json representation
        word_error_model = WordError.from_dict(word_error_model_json)
        assert word_error_model != False

        # Construct a model instance of WordError by calling from_dict on the json representation
        word_error_model_dict = WordError.from_dict(word_error_model_json).__dict__
        word_error_model2 = WordError(**word_error_model_dict)

        # Verify the model instances are equivalent
        assert word_error_model == word_error_model2

        # Convert model instance back to dict and verify no loss of data
        word_error_model_json2 = word_error_model.to_dict()
        assert word_error_model_json2 == word_error_model_json

class TestModel_Words():
    """
    Test Class for Words
    """

    def test_words_serialization(self):
        """
        Test serialization/deserialization for Words
        """

        # Construct dict forms of any model objects needed in order to build this model.

        word_error_model = {} # WordError
        word_error_model['element'] = 'testString'

        word_model = {} # Word
        word_model['word'] = 'testString'
        word_model['sounds_like'] = ['testString']
        word_model['display_as'] = 'testString'
        word_model['count'] = 38
        word_model['source'] = ['testString']
        word_model['error'] = [word_error_model]

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
