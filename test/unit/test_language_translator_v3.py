# coding=utf-8

import json
import responses
import time
import jwt
from unittest import TestCase
from os.path import join, dirname
import ibm_watson
from ibm_watson.language_translator_v3 import TranslationResult, TranslationModels, TranslationModel, IdentifiedLanguages, IdentifiableLanguages, DeleteModelResult

platform_url = 'https://gateway.watsonplatform.net'
service_path = '/language-translator/api'
base_url = '{0}{1}'.format(platform_url, service_path)

def get_access_token():
    access_token_layout = {
        "username": "dummy",
        "role": "Admin",
        "permissions": [
            "administrator",
            "manage_catalog"
        ],
        "sub": "admin",
        "iss": "sss",
        "aud": "sss",
        "uid": "sss",
        "iat": 3600,
        "exp": int(time.time())
    }

    access_token = jwt.encode(access_token_layout, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})
    return access_token.decode('utf-8')

class TestLanguageTranslatorV3(TestCase):
    @classmethod
    def setUp(cls):
        iam_url = "https://iam.cloud.ibm.com/identity/token"
        iam_token_response = {
            "access_token": get_access_token(),
            "token_type": "Bearer",
            "expires_in": 3600,
            "expiration": 1524167011,
            "refresh_token": "jy4gl91BQ"
        }
        responses.add(
            responses.POST, url=iam_url, body=json.dumps(iam_token_response), status=200)

    @classmethod
    @responses.activate
    def test_translate_source_target(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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

        response = service.translate('Hola, cómo estás? €', source='es', target='en').get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        TranslationResult._from_dict(response)

    @classmethod
    @responses.activate
    def test_translate_model_id(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.translate('Messi is the best ever',
                                     model_id='en-es-conversational').get_result()

        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        TranslationResult._from_dict(response)

    @classmethod
    @responses.activate
    def test_identify(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.identify('祝你有美好的一天').get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        IdentifiedLanguages._from_dict(response)

    @classmethod
    @responses.activate
    def test_list_identifiable_languages(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.list_identifiable_languages().get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        IdentifiableLanguages._from_dict(response)

    @classmethod
    @responses.activate
    def test_create_model(cls):
        service = ibm_watson.LanguageTranslatorV3(
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
        with open(join(dirname(__file__), '../../resources/language_translator_model.tmx'), 'rb') as custom_model:
            response = service.create_model('en-fr',
                                            name='test_glossary',
                                            forced_glossary=custom_model).get_result()
        assert len(responses.calls) == 1
        assert responses.calls[0].request.url.startswith(url)
        assert response == expected
        TranslationModel._from_dict(response)

    @classmethod
    @responses.activate
    def test_delete_model(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.delete_model(model_id).get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        DeleteModelResult._from_dict(response)

    @classmethod
    @responses.activate
    def test_get_model(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.get_model(model_id).get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        TranslationModel._from_dict(response)

    @classmethod
    @responses.activate
    def test_list_models(cls):
        service = ibm_watson.LanguageTranslatorV3(
            version='2018-05-01',
            iam_apikey='iam_apikey')
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
        response = service.list_models().get_result()
        assert len(responses.calls) == 2
        assert responses.calls[1].request.url.startswith(url)
        assert response == expected
        TranslationModels._from_dict(response)

    @classmethod
    @responses.activate
    def test_document_translation(cls):
        document_status = {
            'status': 'processing',
            'model_id': 'en-es',
            'target': 'es',
            'created': '2019-06-05T20:59:37',
            'filename': 'hello_world.txt',
            'source': 'en',
            'document_id': '2a683723'}
        endpoint = '/v3/documents'
        url = '{0}{1}'.format(base_url, endpoint)
        responses.add(
            responses.POST,
            url,
            body=json.dumps(document_status),
            status=200,
            content_type='application_json')
        responses.add(
            responses.DELETE,
            url + '/2a683723',
            status=200)
        responses.add(
            responses.GET,
            url,
            body=json.dumps({'documents': [document_status]}),
            status=200,
            content_type='application_json')
        responses.add(
            responses.GET,
            url + '/2a683723/translated_document?version=2017-11-07',
            body='binary response',
            status=200)
        responses.add(
            responses.GET,
            url + '/2a683723?version=2017-11-07',
            body=json.dumps(document_status),
            status=200,
            content_type='application_json')
        language_translator = ibm_watson.LanguageTranslatorV3('2017-11-07', username="username", password="password")

        with open(join(dirname(__file__), '../../resources/hello_world.txt'), 'r') as fileinfo:
            translation = language_translator.translate_document(
                file=fileinfo,
                file_content_type='text/plain',
                model_id='en-es').get_result()
            assert translation == document_status

        status = language_translator.list_documents().get_result()
        assert status['documents'][0]['document_id'] == '2a683723'

        delete_result = language_translator.delete_document('2a683723').get_result()
        assert delete_result.url == 'https://gateway.watsonplatform.net/language-translator/api/v3/documents/2a683723?version=2017-11-07'

        response = language_translator.get_translated_document('2a683723', 'text/plain').get_result()
        assert response.content is not None

        doc_status = language_translator.get_document_status('2a683723').get_result()
        assert doc_status['document_id'] == '2a683723'

        assert len(responses.calls) == 5
