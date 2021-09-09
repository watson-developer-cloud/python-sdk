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
Unit Tests for ToneAnalyzerV3
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_watson.tone_analyzer_v3 import *

version = 'testString'

_service = ToneAnalyzerV3(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.tone-analyzer.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Methods
##############################################################################
# region

class TestTone():
    """
    Test Class for tone
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
    def test_tone_all_params(self):
        """
        tone()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone')
        mock_response = '{"document_tone": {"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "warning": "warning"}, "sentences_tone": [{"sentence_id": 11, "text": "text", "tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "input_from": 10, "input_to": 8}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToneInput model
        tone_input_model = {}
        tone_input_model['text'] = 'testString'

        # Set up parameter values
        tone_input = tone_input_model
        content_type = 'application/json'
        sentences = True
        tones = ['emotion']
        content_language = 'en'
        accept_language = 'en'

        # Invoke method
        response = _service.tone(
            tone_input,
            content_type=content_type,
            sentences=sentences,
            tones=tones,
            content_language=content_language,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'sentences={}'.format('true' if sentences else 'false') in query_string
        assert 'tones={}'.format(','.join(tones)) in query_string
        # Validate body params


    @responses.activate
    def test_tone_required_params(self):
        """
        test_tone_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone')
        mock_response = '{"document_tone": {"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "warning": "warning"}, "sentences_tone": [{"sentence_id": 11, "text": "text", "tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "input_from": 10, "input_to": 8}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToneInput model
        tone_input_model = {}
        tone_input_model['text'] = 'testString'

        # Set up parameter values
        tone_input = tone_input_model

        # Invoke method
        response = _service.tone(
            tone_input,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params


    @responses.activate
    def test_tone_value_error(self):
        """
        test_tone_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone')
        mock_response = '{"document_tone": {"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "warning": "warning"}, "sentences_tone": [{"sentence_id": 11, "text": "text", "tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "tone_categories": [{"tones": [{"score": 5, "tone_id": "tone_id", "tone_name": "tone_name"}], "category_id": "category_id", "category_name": "category_name"}], "input_from": 10, "input_to": 8}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ToneInput model
        tone_input_model = {}
        tone_input_model['text'] = 'testString'

        # Set up parameter values
        tone_input = tone_input_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "tone_input": tone_input,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.tone(**req_copy)



class TestToneChat():
    """
    Test Class for tone_chat
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
    def test_tone_chat_all_params(self):
        """
        tone_chat()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone_chat')
        mock_response = '{"utterances_tone": [{"utterance_id": 12, "utterance_text": "utterance_text", "tones": [{"score": 5, "tone_id": "excited", "tone_name": "tone_name"}], "error": "error"}], "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Utterance model
        utterance_model = {}
        utterance_model['text'] = 'testString'
        utterance_model['user'] = 'testString'

        # Set up parameter values
        utterances = [utterance_model]
        content_language = 'en'
        accept_language = 'en'

        # Invoke method
        response = _service.tone_chat(
            utterances,
            content_language=content_language,
            accept_language=accept_language,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['utterances'] == [utterance_model]


    @responses.activate
    def test_tone_chat_required_params(self):
        """
        test_tone_chat_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone_chat')
        mock_response = '{"utterances_tone": [{"utterance_id": 12, "utterance_text": "utterance_text", "tones": [{"score": 5, "tone_id": "excited", "tone_name": "tone_name"}], "error": "error"}], "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Utterance model
        utterance_model = {}
        utterance_model['text'] = 'testString'
        utterance_model['user'] = 'testString'

        # Set up parameter values
        utterances = [utterance_model]

        # Invoke method
        response = _service.tone_chat(
            utterances,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['utterances'] == [utterance_model]


    @responses.activate
    def test_tone_chat_value_error(self):
        """
        test_tone_chat_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/tone_chat')
        mock_response = '{"utterances_tone": [{"utterance_id": 12, "utterance_text": "utterance_text", "tones": [{"score": 5, "tone_id": "excited", "tone_name": "tone_name"}], "error": "error"}], "warning": "warning"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a Utterance model
        utterance_model = {}
        utterance_model['text'] = 'testString'
        utterance_model['user'] = 'testString'

        # Set up parameter values
        utterances = [utterance_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "utterances": utterances,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.tone_chat(**req_copy)



# endregion
##############################################################################
# End of Service: Methods
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_DocumentAnalysis():
    """
    Test Class for DocumentAnalysis
    """

    def test_document_analysis_serialization(self):
        """
        Test serialization/deserialization for DocumentAnalysis
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_score_model = {} # ToneScore
        tone_score_model['score'] = 72.5
        tone_score_model['tone_id'] = 'testString'
        tone_score_model['tone_name'] = 'testString'

        tone_category_model = {} # ToneCategory
        tone_category_model['tones'] = [tone_score_model]
        tone_category_model['category_id'] = 'testString'
        tone_category_model['category_name'] = 'testString'

        # Construct a json representation of a DocumentAnalysis model
        document_analysis_model_json = {}
        document_analysis_model_json['tones'] = [tone_score_model]
        document_analysis_model_json['tone_categories'] = [tone_category_model]
        document_analysis_model_json['warning'] = 'testString'

        # Construct a model instance of DocumentAnalysis by calling from_dict on the json representation
        document_analysis_model = DocumentAnalysis.from_dict(document_analysis_model_json)
        assert document_analysis_model != False

        # Construct a model instance of DocumentAnalysis by calling from_dict on the json representation
        document_analysis_model_dict = DocumentAnalysis.from_dict(document_analysis_model_json).__dict__
        document_analysis_model2 = DocumentAnalysis(**document_analysis_model_dict)

        # Verify the model instances are equivalent
        assert document_analysis_model == document_analysis_model2

        # Convert model instance back to dict and verify no loss of data
        document_analysis_model_json2 = document_analysis_model.to_dict()
        assert document_analysis_model_json2 == document_analysis_model_json

class TestModel_SentenceAnalysis():
    """
    Test Class for SentenceAnalysis
    """

    def test_sentence_analysis_serialization(self):
        """
        Test serialization/deserialization for SentenceAnalysis
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_score_model = {} # ToneScore
        tone_score_model['score'] = 72.5
        tone_score_model['tone_id'] = 'testString'
        tone_score_model['tone_name'] = 'testString'

        tone_category_model = {} # ToneCategory
        tone_category_model['tones'] = [tone_score_model]
        tone_category_model['category_id'] = 'testString'
        tone_category_model['category_name'] = 'testString'

        # Construct a json representation of a SentenceAnalysis model
        sentence_analysis_model_json = {}
        sentence_analysis_model_json['sentence_id'] = 38
        sentence_analysis_model_json['text'] = 'testString'
        sentence_analysis_model_json['tones'] = [tone_score_model]
        sentence_analysis_model_json['tone_categories'] = [tone_category_model]
        sentence_analysis_model_json['input_from'] = 38
        sentence_analysis_model_json['input_to'] = 38

        # Construct a model instance of SentenceAnalysis by calling from_dict on the json representation
        sentence_analysis_model = SentenceAnalysis.from_dict(sentence_analysis_model_json)
        assert sentence_analysis_model != False

        # Construct a model instance of SentenceAnalysis by calling from_dict on the json representation
        sentence_analysis_model_dict = SentenceAnalysis.from_dict(sentence_analysis_model_json).__dict__
        sentence_analysis_model2 = SentenceAnalysis(**sentence_analysis_model_dict)

        # Verify the model instances are equivalent
        assert sentence_analysis_model == sentence_analysis_model2

        # Convert model instance back to dict and verify no loss of data
        sentence_analysis_model_json2 = sentence_analysis_model.to_dict()
        assert sentence_analysis_model_json2 == sentence_analysis_model_json

class TestModel_ToneAnalysis():
    """
    Test Class for ToneAnalysis
    """

    def test_tone_analysis_serialization(self):
        """
        Test serialization/deserialization for ToneAnalysis
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_score_model = {} # ToneScore
        tone_score_model['score'] = 72.5
        tone_score_model['tone_id'] = 'testString'
        tone_score_model['tone_name'] = 'testString'

        tone_category_model = {} # ToneCategory
        tone_category_model['tones'] = [tone_score_model]
        tone_category_model['category_id'] = 'testString'
        tone_category_model['category_name'] = 'testString'

        document_analysis_model = {} # DocumentAnalysis
        document_analysis_model['tones'] = [tone_score_model]
        document_analysis_model['tone_categories'] = [tone_category_model]
        document_analysis_model['warning'] = 'testString'

        sentence_analysis_model = {} # SentenceAnalysis
        sentence_analysis_model['sentence_id'] = 38
        sentence_analysis_model['text'] = 'testString'
        sentence_analysis_model['tones'] = [tone_score_model]
        sentence_analysis_model['tone_categories'] = [tone_category_model]
        sentence_analysis_model['input_from'] = 38
        sentence_analysis_model['input_to'] = 38

        # Construct a json representation of a ToneAnalysis model
        tone_analysis_model_json = {}
        tone_analysis_model_json['document_tone'] = document_analysis_model
        tone_analysis_model_json['sentences_tone'] = [sentence_analysis_model]

        # Construct a model instance of ToneAnalysis by calling from_dict on the json representation
        tone_analysis_model = ToneAnalysis.from_dict(tone_analysis_model_json)
        assert tone_analysis_model != False

        # Construct a model instance of ToneAnalysis by calling from_dict on the json representation
        tone_analysis_model_dict = ToneAnalysis.from_dict(tone_analysis_model_json).__dict__
        tone_analysis_model2 = ToneAnalysis(**tone_analysis_model_dict)

        # Verify the model instances are equivalent
        assert tone_analysis_model == tone_analysis_model2

        # Convert model instance back to dict and verify no loss of data
        tone_analysis_model_json2 = tone_analysis_model.to_dict()
        assert tone_analysis_model_json2 == tone_analysis_model_json

class TestModel_ToneCategory():
    """
    Test Class for ToneCategory
    """

    def test_tone_category_serialization(self):
        """
        Test serialization/deserialization for ToneCategory
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_score_model = {} # ToneScore
        tone_score_model['score'] = 72.5
        tone_score_model['tone_id'] = 'testString'
        tone_score_model['tone_name'] = 'testString'

        # Construct a json representation of a ToneCategory model
        tone_category_model_json = {}
        tone_category_model_json['tones'] = [tone_score_model]
        tone_category_model_json['category_id'] = 'testString'
        tone_category_model_json['category_name'] = 'testString'

        # Construct a model instance of ToneCategory by calling from_dict on the json representation
        tone_category_model = ToneCategory.from_dict(tone_category_model_json)
        assert tone_category_model != False

        # Construct a model instance of ToneCategory by calling from_dict on the json representation
        tone_category_model_dict = ToneCategory.from_dict(tone_category_model_json).__dict__
        tone_category_model2 = ToneCategory(**tone_category_model_dict)

        # Verify the model instances are equivalent
        assert tone_category_model == tone_category_model2

        # Convert model instance back to dict and verify no loss of data
        tone_category_model_json2 = tone_category_model.to_dict()
        assert tone_category_model_json2 == tone_category_model_json

class TestModel_ToneChatScore():
    """
    Test Class for ToneChatScore
    """

    def test_tone_chat_score_serialization(self):
        """
        Test serialization/deserialization for ToneChatScore
        """

        # Construct a json representation of a ToneChatScore model
        tone_chat_score_model_json = {}
        tone_chat_score_model_json['score'] = 72.5
        tone_chat_score_model_json['tone_id'] = 'excited'
        tone_chat_score_model_json['tone_name'] = 'testString'

        # Construct a model instance of ToneChatScore by calling from_dict on the json representation
        tone_chat_score_model = ToneChatScore.from_dict(tone_chat_score_model_json)
        assert tone_chat_score_model != False

        # Construct a model instance of ToneChatScore by calling from_dict on the json representation
        tone_chat_score_model_dict = ToneChatScore.from_dict(tone_chat_score_model_json).__dict__
        tone_chat_score_model2 = ToneChatScore(**tone_chat_score_model_dict)

        # Verify the model instances are equivalent
        assert tone_chat_score_model == tone_chat_score_model2

        # Convert model instance back to dict and verify no loss of data
        tone_chat_score_model_json2 = tone_chat_score_model.to_dict()
        assert tone_chat_score_model_json2 == tone_chat_score_model_json

class TestModel_ToneInput():
    """
    Test Class for ToneInput
    """

    def test_tone_input_serialization(self):
        """
        Test serialization/deserialization for ToneInput
        """

        # Construct a json representation of a ToneInput model
        tone_input_model_json = {}
        tone_input_model_json['text'] = 'testString'

        # Construct a model instance of ToneInput by calling from_dict on the json representation
        tone_input_model = ToneInput.from_dict(tone_input_model_json)
        assert tone_input_model != False

        # Construct a model instance of ToneInput by calling from_dict on the json representation
        tone_input_model_dict = ToneInput.from_dict(tone_input_model_json).__dict__
        tone_input_model2 = ToneInput(**tone_input_model_dict)

        # Verify the model instances are equivalent
        assert tone_input_model == tone_input_model2

        # Convert model instance back to dict and verify no loss of data
        tone_input_model_json2 = tone_input_model.to_dict()
        assert tone_input_model_json2 == tone_input_model_json

class TestModel_ToneScore():
    """
    Test Class for ToneScore
    """

    def test_tone_score_serialization(self):
        """
        Test serialization/deserialization for ToneScore
        """

        # Construct a json representation of a ToneScore model
        tone_score_model_json = {}
        tone_score_model_json['score'] = 72.5
        tone_score_model_json['tone_id'] = 'testString'
        tone_score_model_json['tone_name'] = 'testString'

        # Construct a model instance of ToneScore by calling from_dict on the json representation
        tone_score_model = ToneScore.from_dict(tone_score_model_json)
        assert tone_score_model != False

        # Construct a model instance of ToneScore by calling from_dict on the json representation
        tone_score_model_dict = ToneScore.from_dict(tone_score_model_json).__dict__
        tone_score_model2 = ToneScore(**tone_score_model_dict)

        # Verify the model instances are equivalent
        assert tone_score_model == tone_score_model2

        # Convert model instance back to dict and verify no loss of data
        tone_score_model_json2 = tone_score_model.to_dict()
        assert tone_score_model_json2 == tone_score_model_json

class TestModel_Utterance():
    """
    Test Class for Utterance
    """

    def test_utterance_serialization(self):
        """
        Test serialization/deserialization for Utterance
        """

        # Construct a json representation of a Utterance model
        utterance_model_json = {}
        utterance_model_json['text'] = 'testString'
        utterance_model_json['user'] = 'testString'

        # Construct a model instance of Utterance by calling from_dict on the json representation
        utterance_model = Utterance.from_dict(utterance_model_json)
        assert utterance_model != False

        # Construct a model instance of Utterance by calling from_dict on the json representation
        utterance_model_dict = Utterance.from_dict(utterance_model_json).__dict__
        utterance_model2 = Utterance(**utterance_model_dict)

        # Verify the model instances are equivalent
        assert utterance_model == utterance_model2

        # Convert model instance back to dict and verify no loss of data
        utterance_model_json2 = utterance_model.to_dict()
        assert utterance_model_json2 == utterance_model_json

class TestModel_UtteranceAnalyses():
    """
    Test Class for UtteranceAnalyses
    """

    def test_utterance_analyses_serialization(self):
        """
        Test serialization/deserialization for UtteranceAnalyses
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_chat_score_model = {} # ToneChatScore
        tone_chat_score_model['score'] = 72.5
        tone_chat_score_model['tone_id'] = 'excited'
        tone_chat_score_model['tone_name'] = 'testString'

        utterance_analysis_model = {} # UtteranceAnalysis
        utterance_analysis_model['utterance_id'] = 38
        utterance_analysis_model['utterance_text'] = 'testString'
        utterance_analysis_model['tones'] = [tone_chat_score_model]
        utterance_analysis_model['error'] = 'testString'

        # Construct a json representation of a UtteranceAnalyses model
        utterance_analyses_model_json = {}
        utterance_analyses_model_json['utterances_tone'] = [utterance_analysis_model]
        utterance_analyses_model_json['warning'] = 'testString'

        # Construct a model instance of UtteranceAnalyses by calling from_dict on the json representation
        utterance_analyses_model = UtteranceAnalyses.from_dict(utterance_analyses_model_json)
        assert utterance_analyses_model != False

        # Construct a model instance of UtteranceAnalyses by calling from_dict on the json representation
        utterance_analyses_model_dict = UtteranceAnalyses.from_dict(utterance_analyses_model_json).__dict__
        utterance_analyses_model2 = UtteranceAnalyses(**utterance_analyses_model_dict)

        # Verify the model instances are equivalent
        assert utterance_analyses_model == utterance_analyses_model2

        # Convert model instance back to dict and verify no loss of data
        utterance_analyses_model_json2 = utterance_analyses_model.to_dict()
        assert utterance_analyses_model_json2 == utterance_analyses_model_json

class TestModel_UtteranceAnalysis():
    """
    Test Class for UtteranceAnalysis
    """

    def test_utterance_analysis_serialization(self):
        """
        Test serialization/deserialization for UtteranceAnalysis
        """

        # Construct dict forms of any model objects needed in order to build this model.

        tone_chat_score_model = {} # ToneChatScore
        tone_chat_score_model['score'] = 72.5
        tone_chat_score_model['tone_id'] = 'excited'
        tone_chat_score_model['tone_name'] = 'testString'

        # Construct a json representation of a UtteranceAnalysis model
        utterance_analysis_model_json = {}
        utterance_analysis_model_json['utterance_id'] = 38
        utterance_analysis_model_json['utterance_text'] = 'testString'
        utterance_analysis_model_json['tones'] = [tone_chat_score_model]
        utterance_analysis_model_json['error'] = 'testString'

        # Construct a model instance of UtteranceAnalysis by calling from_dict on the json representation
        utterance_analysis_model = UtteranceAnalysis.from_dict(utterance_analysis_model_json)
        assert utterance_analysis_model != False

        # Construct a model instance of UtteranceAnalysis by calling from_dict on the json representation
        utterance_analysis_model_dict = UtteranceAnalysis.from_dict(utterance_analysis_model_json).__dict__
        utterance_analysis_model2 = UtteranceAnalysis(**utterance_analysis_model_dict)

        # Verify the model instances are equivalent
        assert utterance_analysis_model == utterance_analysis_model2

        # Convert model instance back to dict and verify no loss of data
        utterance_analysis_model_json2 = utterance_analysis_model.to_dict()
        assert utterance_analysis_model_json2 == utterance_analysis_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
