# coding=utf-8

import json
import os
import responses
import watson_developer_cloud
from watson_developer_cloud.language_translator_v3 import TranslationResult, TranslationModels, TranslationModel, IdentifiedLanguages, IdentifiableLanguages, DeleteModelResult

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/language-translator/api'
base_url = '{0}{1}'.format(platform_url, service_path)

iam_url = "https://iam.bluemix.net/identity/token"
iam_token_response = """{
    "access_token": "oAeisG8yqPY7sFR_x66Z15",
    "token_type": "Bearer",
    "expires_in": 3600,
    "expiration": 1524167011,
    "refresh_token": "jy4gl91BQ"
}"""

#########################
# counterexamples
#########################

@responses.activate
def test_translate_source_target():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    endpoint = '/v3/translate'
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)

    response = service.translate('Hola, cómo estás? €', source='es', target='en')
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    TranslationResult._from_dict(response)

@responses.activate
def test_translate_model_id():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    endpoint = '/v3/translate'
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.translate('Messi is the best ever',
                                 model_id='en-es-conversational')

    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    TranslationResult._from_dict(response)

@responses.activate
def test_identify():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    endpoint = '/v3/identify'
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.identify('祝你有美好的一天')
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    IdentifiedLanguages._from_dict(response)

@responses.activate
def test_list_identifiable_languages():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    endpoint = '/v3/identifiable_languages'
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.list_identifiable_languages()
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    IdentifiableLanguages._from_dict(response)

@responses.activate
def test_create_model():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        username='xxx',
        password='yyy'
    )
    endpoint = '/v3/models'
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "status": "available",
        "model_id": "en-es-conversational",
        "domain": "conversational",
        "target": "es",
        "customizable": False,
        "source": "en",
        "base_model_id": "en-es-conversational",
        "owner": "",
        "default_model": False,
        "name": "test_glossary"
    }
    responses.add(
        responses.POST,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    with open(os.path.join(os.path.dirname(__file__), '../../resources/language_translator_model.tmx'), 'rb') as custom_model:
        response = service.create_model('en-fr',
                                        name='test_glossary',
                                        forced_glossary=custom_model)
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url.startswith(url)
    assert response == expected
    TranslationModel._from_dict(response)

@responses.activate
def test_delete_model():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    model_id = 'en-es-conversational'
    endpoint = '/v3/models/' + model_id
    url = '{0}{1}'.format(base_url, endpoint)
    expected = {
        "status": "OK",
    }
    responses.add(
        responses.DELETE,
        url,
        body=json.dumps(expected),
        status=200,
        content_type='application/json')
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.delete_model(model_id)
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    DeleteModelResult._from_dict(response)

@responses.activate
def test_get_model():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    model_id = 'en-es-conversational'
    endpoint = '/v3/models/' + model_id
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.get_model(model_id)
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    TranslationModel._from_dict(response)

@responses.activate
def test_list_models():
    service = watson_developer_cloud.LanguageTranslatorV3(
        version='2018-05-01',
        iam_api_key='iam_api_key')
    endpoint = '/v3/models'
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
    responses.add(responses.POST, url=iam_url, body=iam_token_response, status=200)
    response = service.list_models()
    assert len(responses.calls) == 2
    assert responses.calls[1].request.url.startswith(url)
    assert response == expected
    TranslationModels._from_dict(response)
