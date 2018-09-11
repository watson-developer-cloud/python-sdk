# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
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
IBM Watson&trade; Language Translator translates text from one language to another. The
service offers multiple IBM provided translation models that you can customize based on
your unique terminology and language. Use Language Translator to take news from across the
globe and present it in your language, communicate with your customers in their own
language, and more.
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class LanguageTranslatorV3(WatsonService):
    """The Language Translator V3 service."""

    default_url = 'https://gateway.watsonplatform.net/language-translator/api'

    def __init__(
            self,
            version,
            url=default_url,
            username=None,
            password=None,
            iam_apikey=None,
            iam_access_token=None,
            iam_url=None,
    ):
        """
        Construct a new client for the Language Translator service.

        :param str version: The API version date to use with the service, in
               "YYYY-MM-DD" format. Whenever the API is changed in a backwards
               incompatible way, a new minor version of the API is released.
               The service uses the API version for the date you specify, or
               the most recent version before that date. Note that you should
               not programmatically specify the current date at runtime, in
               case the API has been updated since your application's release.
               Instead, specify a version date that is compatible with your
               application, and don't change it until your application is
               ready for a later version.

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/language-translator/api").
               The base url may differ between Bluemix regions.

        :param str username: The username used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str password: The password used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str iam_apikey: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.bluemix.net/identity/token'.
        """

        WatsonService.__init__(
            self,
            vcap_services_name='language_translator',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # Translation
    #########################

    def translate(self, text, model_id=None, source=None, target=None,
                  **kwargs):
        """
        Translate.

        Translates the input text from the source language to the target language.

        :param list[str] text: Input text in UTF-8 encoding. Multiple entries will result
        in multiple translations in the response.
        :param str model_id: Model ID of the translation model to use. If this is
        specified, the **source** and **target** parameters will be ignored. The method
        requires either a model ID or both the **source** and **target** parameters.
        :param str source: Language code of the source text language. Use with `target` as
        an alternative way to select a translation model. When `source` and `target` are
        set, and a model ID is not set, the system chooses a default model for the
        language pair (usually the model based on the news domain).
        :param str target: Language code of the translation target language. Use with
        source as an alternative way to select a translation model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {
            'text': text,
            'model_id': model_id,
            'source': source,
            'target': target
        }
        url = '/v3/translate'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Identification
    #########################

    def identify(self, text, **kwargs):
        """
        Identify language.

        Identifies the language of the input text.

        :param str text: Input text in UTF-8 format.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = text
        headers['content-type'] = 'text/plain'
        url = '/v3/identify'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            accept_json=True)
        return response

    def list_identifiable_languages(self, **kwargs):
        """
        List identifiable languages.

        Lists the languages that the service can identify. Returns the language code (for
        example, `en` for English or `es` for Spanish) and name of each language.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/identifiable_languages'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    #########################
    # Models
    #########################

    def create_model(self,
                     base_model_id,
                     name=None,
                     forced_glossary=None,
                     parallel_corpus=None,
                     forced_glossary_filename=None,
                     parallel_corpus_filename=None,
                     **kwargs):
        """
        Create model.

        Uploads Translation Memory eXchange (TMX) files to customize a translation model.
        You can either customize a model with a forced glossary or with a corpus that
        contains parallel sentences. To create a model that is customized with a parallel
        corpus <b>and</b> a forced glossary, proceed in two steps: customize with a
        parallel corpus first and then customize the resulting model with a glossary.
        Depending on the type of customization and the size of the uploaded corpora,
        training can range from minutes for a glossary to several hours for a large
        parallel corpus. You can upload a single forced glossary file and this file must
        be less than <b>10 MB</b>. You can upload multiple parallel corpora tmx files. The
        cumulative file size of all uploaded files is limited to <b>250 MB</b>. To
        successfully train with a parallel corpus you must have at least <b>5,000 parallel
        sentences</b> in your corpus.
        You can have a <b>maxium of 10 custom models per language pair</b>.

        :param str base_model_id: The model ID of the model to use as the base for
        customization. To see available models, use the `List models` method. Usually all
        IBM provided models are customizable. In addition, all your models that have been
        created via parallel corpus customization, can be further customized with a forced
        glossary.
        :param str name: An optional model name that you can use to identify the model.
        Valid characters are letters, numbers, dashes, underscores, spaces and
        apostrophes. The maximum length is 32 characters.
        :param file forced_glossary: A TMX file with your customizations. The
        customizations in the file completely overwrite the domain translaton data,
        including high frequency or high confidence phrase translations. You can upload
        only one glossary with a file size less than 10 MB per call. A forced glossary
        should contain single words or short phrases.
        :param file parallel_corpus: A TMX file with parallel sentences for source and
        target language. You can upload multiple parallel_corpus files in one request. All
        uploaded parallel_corpus files combined, your parallel corpus must contain at
        least 5,000 parallel sentences to train successfully.
        :param str forced_glossary_filename: The filename for forced_glossary.
        :param str parallel_corpus_filename: The filename for parallel_corpus.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if base_model_id is None:
            raise ValueError('base_model_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'base_model_id': base_model_id,
            'name': name
        }
        forced_glossary_tuple = None
        if forced_glossary:
            if not forced_glossary_filename and hasattr(forced_glossary,
                                                        'name'):
                forced_glossary_filename = forced_glossary.name
            mime_type = 'application/octet-stream'
            forced_glossary_tuple = (forced_glossary_filename, forced_glossary,
                                     mime_type)
        parallel_corpus_tuple = None
        if parallel_corpus:
            if not parallel_corpus_filename and hasattr(parallel_corpus,
                                                        'name'):
                parallel_corpus_filename = parallel_corpus.name
            mime_type = 'application/octet-stream'
            parallel_corpus_tuple = (parallel_corpus_filename, parallel_corpus,
                                     mime_type)
        url = '/v3/models'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={
                'forced_glossary': forced_glossary_tuple,
                'parallel_corpus': parallel_corpus_tuple
            },
            accept_json=True)
        return response

    def delete_model(self, model_id, **kwargs):
        """
        Delete model.

        Deletes a custom translation model.

        :param str model_id: Model ID of the model to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if model_id is None:
            raise ValueError('model_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def get_model(self, model_id, **kwargs):
        """
        Get model details.

        Gets information about a translation model, including training status for custom
        models. Use this API call to poll the status of your customization request. A
        successfully completed training will have a status of `available`.

        :param str model_id: Model ID of the model to get.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        if model_id is None:
            raise ValueError('model_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_models(self,
                    source=None,
                    target=None,
                    default_models=None,
                    **kwargs):
        """
        List models.

        Lists available translation models.

        :param str source: Specify a language code to filter results by source language.
        :param str target: Specify a language code to filter results by target language.
        :param bool default_models: If the default parameter isn't specified, the service
        will return all models (default and non-default) for each language pair. To return
        only default models, set this to `true`. To return only non-default models, set
        this to `false`. There is exactly one default model per language pair, the IBM
        provided base model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {
            'version': self.version,
            'source': source,
            'target': target,
            'default': default_models
        }
        url = '/v3/models'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class DeleteModelResult(object):
    """
    DeleteModelResult.

    :attr str status: "OK" indicates that the model was successfully deleted.
    """

    def __init__(self, status):
        """
        Initialize a DeleteModelResult object.

        :param str status: "OK" indicates that the model was successfully deleted.
        """
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteModelResult object from a json dictionary."""
        args = {}
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError(
                'Required property \'status\' not present in DeleteModelResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this DeleteModelResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IdentifiableLanguage(object):
    """
    IdentifiableLanguage.

    :attr str language: The language code for an identifiable language.
    :attr str name: The name of the identifiable language.
    """

    def __init__(self, language, name):
        """
        Initialize a IdentifiableLanguage object.

        :param str language: The language code for an identifiable language.
        :param str name: The name of the identifiable language.
        """
        self.language = language
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiableLanguage object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in IdentifiableLanguage JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in IdentifiableLanguage JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def __str__(self):
        """Return a `str` version of this IdentifiableLanguage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IdentifiableLanguages(object):
    """
    IdentifiableLanguages.

    :attr list[IdentifiableLanguage] languages: A list of all languages that the service
    can identify.
    """

    def __init__(self, languages):
        """
        Initialize a IdentifiableLanguages object.

        :param list[IdentifiableLanguage] languages: A list of all languages that the
        service can identify.
        """
        self.languages = languages

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiableLanguages object from a json dictionary."""
        args = {}
        if 'languages' in _dict:
            args['languages'] = [
                IdentifiableLanguage._from_dict(x)
                for x in (_dict.get('languages'))
            ]
        else:
            raise ValueError(
                'Required property \'languages\' not present in IdentifiableLanguages JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'languages') and self.languages is not None:
            _dict['languages'] = [x._to_dict() for x in self.languages]
        return _dict

    def __str__(self):
        """Return a `str` version of this IdentifiableLanguages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IdentifiedLanguage(object):
    """
    IdentifiedLanguage.

    :attr str language: The language code for an identified language.
    :attr float confidence: The confidence score for the identified language.
    """

    def __init__(self, language, confidence):
        """
        Initialize a IdentifiedLanguage object.

        :param str language: The language code for an identified language.
        :param float confidence: The confidence score for the identified language.
        """
        self.language = language
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiedLanguage object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in IdentifiedLanguage JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        else:
            raise ValueError(
                'Required property \'confidence\' not present in IdentifiedLanguage JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def __str__(self):
        """Return a `str` version of this IdentifiedLanguage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IdentifiedLanguages(object):
    """
    IdentifiedLanguages.

    :attr list[IdentifiedLanguage] languages: A ranking of identified languages with
    confidence scores.
    """

    def __init__(self, languages):
        """
        Initialize a IdentifiedLanguages object.

        :param list[IdentifiedLanguage] languages: A ranking of identified languages with
        confidence scores.
        """
        self.languages = languages

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiedLanguages object from a json dictionary."""
        args = {}
        if 'languages' in _dict:
            args['languages'] = [
                IdentifiedLanguage._from_dict(x)
                for x in (_dict.get('languages'))
            ]
        else:
            raise ValueError(
                'Required property \'languages\' not present in IdentifiedLanguages JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'languages') and self.languages is not None:
            _dict['languages'] = [x._to_dict() for x in self.languages]
        return _dict

    def __str__(self):
        """Return a `str` version of this IdentifiedLanguages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Translation(object):
    """
    Translation.

    :attr str translation_output: Translation output in UTF-8.
    """

    def __init__(self, translation_output):
        """
        Initialize a Translation object.

        :param str translation_output: Translation output in UTF-8.
        """
        self.translation_output = translation_output

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Translation object from a json dictionary."""
        args = {}
        if 'translation' in _dict or 'translation_output' in _dict:
            args['translation_output'] = _dict.get('translation') or _dict.get(
                'translation_output')
        else:
            raise ValueError(
                'Required property \'translation\' not present in Translation JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(
                self,
                'translation_output') and self.translation_output is not None:
            _dict['translation'] = self.translation_output
        return _dict

    def __str__(self):
        """Return a `str` version of this Translation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TranslationModel(object):
    """
    Response payload for models.

    :attr str model_id: A globally unique string that identifies the underlying model that
    is used for translation.
    :attr str name: (optional) Optional name that can be specified when the model is
    created.
    :attr str source: (optional) Translation source language code.
    :attr str target: (optional) Translation target language code.
    :attr str base_model_id: (optional) Model ID of the base model that was used to
    customize the model. If the model is not a custom model, this will be an empty string.
    :attr str domain: (optional) The domain of the translation model.
    :attr bool customizable: (optional) Whether this model can be used as a base for
    customization. Customized models are not further customizable, and some base models
    are not customizable.
    :attr bool default_model: (optional) Whether or not the model is a default model. A
    default model is the model for a given language pair that will be used when that
    language pair is specified in the source and target parameters.
    :attr str owner: (optional) Either an empty string, indicating the model is not a
    custom model, or the ID of the service instance that created the model.
    :attr str status: (optional) Availability of a model.
    """

    def __init__(self,
                 model_id,
                 name=None,
                 source=None,
                 target=None,
                 base_model_id=None,
                 domain=None,
                 customizable=None,
                 default_model=None,
                 owner=None,
                 status=None):
        """
        Initialize a TranslationModel object.

        :param str model_id: A globally unique string that identifies the underlying model
        that is used for translation.
        :param str name: (optional) Optional name that can be specified when the model is
        created.
        :param str source: (optional) Translation source language code.
        :param str target: (optional) Translation target language code.
        :param str base_model_id: (optional) Model ID of the base model that was used to
        customize the model. If the model is not a custom model, this will be an empty
        string.
        :param str domain: (optional) The domain of the translation model.
        :param bool customizable: (optional) Whether this model can be used as a base for
        customization. Customized models are not further customizable, and some base
        models are not customizable.
        :param bool default_model: (optional) Whether or not the model is a default model.
        A default model is the model for a given language pair that will be used when that
        language pair is specified in the source and target parameters.
        :param str owner: (optional) Either an empty string, indicating the model is not a
        custom model, or the ID of the service instance that created the model.
        :param str status: (optional) Availability of a model.
        """
        self.model_id = model_id
        self.name = name
        self.source = source
        self.target = target
        self.base_model_id = base_model_id
        self.domain = domain
        self.customizable = customizable
        self.default_model = default_model
        self.owner = owner
        self.status = status

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TranslationModel object from a json dictionary."""
        args = {}
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        else:
            raise ValueError(
                'Required property \'model_id\' not present in TranslationModel JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'target' in _dict:
            args['target'] = _dict.get('target')
        if 'base_model_id' in _dict:
            args['base_model_id'] = _dict.get('base_model_id')
        if 'domain' in _dict:
            args['domain'] = _dict.get('domain')
        if 'customizable' in _dict:
            args['customizable'] = _dict.get('customizable')
        if 'default_model' in _dict:
            args['default_model'] = _dict.get('default_model')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        if hasattr(self, 'base_model_id') and self.base_model_id is not None:
            _dict['base_model_id'] = self.base_model_id
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'customizable') and self.customizable is not None:
            _dict['customizable'] = self.customizable
        if hasattr(self, 'default_model') and self.default_model is not None:
            _dict['default_model'] = self.default_model
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def __str__(self):
        """Return a `str` version of this TranslationModel object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TranslationModels(object):
    """
    The response type for listing existing translation models.

    :attr list[TranslationModel] models: An array of available models.
    """

    def __init__(self, models):
        """
        Initialize a TranslationModels object.

        :param list[TranslationModel] models: An array of available models.
        """
        self.models = models

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TranslationModels object from a json dictionary."""
        args = {}
        if 'models' in _dict:
            args['models'] = [
                TranslationModel._from_dict(x) for x in (_dict.get('models'))
            ]
        else:
            raise ValueError(
                'Required property \'models\' not present in TranslationModels JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            _dict['models'] = [x._to_dict() for x in self.models]
        return _dict

    def __str__(self):
        """Return a `str` version of this TranslationModels object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TranslationResult(object):
    """
    TranslationResult.

    :attr int word_count: Number of words in the input text.
    :attr int character_count: Number of characters in the input text.
    :attr list[Translation] translations: List of translation output in UTF-8,
    corresponding to the input text entries.
    """

    def __init__(self, word_count, character_count, translations):
        """
        Initialize a TranslationResult object.

        :param int word_count: Number of words in the input text.
        :param int character_count: Number of characters in the input text.
        :param list[Translation] translations: List of translation output in UTF-8,
        corresponding to the input text entries.
        """
        self.word_count = word_count
        self.character_count = character_count
        self.translations = translations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TranslationResult object from a json dictionary."""
        args = {}
        if 'word_count' in _dict:
            args['word_count'] = _dict.get('word_count')
        else:
            raise ValueError(
                'Required property \'word_count\' not present in TranslationResult JSON'
            )
        if 'character_count' in _dict:
            args['character_count'] = _dict.get('character_count')
        else:
            raise ValueError(
                'Required property \'character_count\' not present in TranslationResult JSON'
            )
        if 'translations' in _dict:
            args['translations'] = [
                Translation._from_dict(x) for x in (_dict.get('translations'))
            ]
        else:
            raise ValueError(
                'Required property \'translations\' not present in TranslationResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'word_count') and self.word_count is not None:
            _dict['word_count'] = self.word_count
        if hasattr(self,
                   'character_count') and self.character_count is not None:
            _dict['character_count'] = self.character_count
        if hasattr(self, 'translations') and self.translations is not None:
            _dict['translations'] = [x._to_dict() for x in self.translations]
        return _dict

    def __str__(self):
        """Return a `str` version of this TranslationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
