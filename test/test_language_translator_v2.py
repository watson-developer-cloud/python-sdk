# coding=utf-8

# Copyright 2017 IBM All Rights Reserved.
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

import json
import responses
import watson_developer_cloud
from watson_developer_cloud.language_translator_v2 import TranslationResult, TranslationModels, TranslationModel, IdentifiedLanguages, IdentifiableLanguages

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/language-translator/api'
base_url = '{0}{1}'.format(platform_url, service_path)

#########################
# counterexamples
#########################

@responses.activate
def test_translate_source_target():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    endpoint = '/v2/translate'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "character_count": 19,
        "translations": [{"translation": u"Hello, how are you ? \u20ac"}],
        "word_count": 4
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.translate('Hola, cómo estás? €', source='es', target='en')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a TranslationResult
    TranslationResult._from_dict(response)

@responses.activate
def test_translate_model_id():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    endpoint = '/v2/translate'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "character_count": 22,
        "translations": [
            {
                "translation": "Messi es el mejor"
            }
        ],
        "word_count": 5
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.translate('Messi is the best ever',
                                 model_id='en-es-conversational')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a TranslationResult
    TranslationResult._from_dict(response)

@responses.activate
def test_list_models():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    endpoint = '/v2/models'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "models": [
            {
                "status": "available",
                "model_id": "en-es-conversational",
                "domain": "conversational",
                "target": "es",
                "customizable": False,
                "source": "en",
                "base_model_id": "",
                "owner": "",
                "default_model": False,
                "name": "en-es-conversational"
            },
            {
                "status": "available",
                "model_id": "es-en",
                "domain": "news",
                "target": "en",
                "customizable": True,
                "source": "es",
                "base_model_id": "",
                "owner": "",
                "default_model": True,
                "name": "es-en"
            }
        ]
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.list_models()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a TranslationModels
    TranslationModels._from_dict(response)

@responses.activate
def test_get_model():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    model_id = 'en-es-conversational'
    endpoint = '/v2/models/' + model_id
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "status": "available",
        "model_id": "en-es-conversational",
        "domain": "conversational",
        "target": "es",
        "customizable": False,
        "source": "en",
        "base_model_id": "",
        "owner": "",
        "default_model": False,
        "name": "en-es-conversational"
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.get_model(model_id)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a TranslationModel
    TranslationModel._from_dict(response)

# print(json.dumps(language_translator.identify('你好'), indent=2))

@responses.activate
def test_identify():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    endpoint = '/v2/identify'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "languages": [
            {
                "confidence": 0.477673,
                "language": "zh"
            },
            {
                "confidence": 0.262053,
                "language": "zh-TW"
            },
            {
                "confidence": 0.00958378,
                "language": "en"
            }
        ]
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.identify('祝你有美好的一天')
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a IdentifiedLanguages
    IdentifiedLanguages._from_dict(response)

# print(json.dumps(language_translator.get_identifiable_languages(), indent=2))

@responses.activate
def test_list_identifiable_languages():
    service = watson_developer_cloud.LanguageTranslatorV2(
        username='username', password='password')
    endpoint = '/v2/identifiable_languages'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "languages": [
            {
                "name": "German",
                "language": "de"
            },
            {
                "name": "Greek",
                "language": "el"
            },
            {
                "name": "English",
                "language": "en"
            },
            {
                "name": "Esperanto",
                "language": "eo"
            },
            {
                "name": "Spanish",
                "language": "es"
            },
            {
                "name": "Chinese",
                "language": "zh"
            }
            ]
    }
    responses.add(
        responses.GET,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    response = service.list_identifiable_languages()
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    # Verify that response can be converted to a IdentifiableLanguages
    IdentifiableLanguages._from_dict(response)
