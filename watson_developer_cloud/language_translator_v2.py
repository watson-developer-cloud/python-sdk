# coding: utf-8

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
"""
Language Translator translates text from one language to another. The service offers
multiple domain-specific models that you can customize based on your unique terminology
and language. Use Language Translator to take news from across the globe and present it in
your language, communicate with your customers in their own language, and more.
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class LanguageTranslatorV2(WatsonService):
    """The Language Translator V2 service."""

    default_url = 'https://gateway.watsonplatform.net/language-translator/api'

    def __init__(self, url=default_url, username=None, password=None):
        """
        Construct a new client for the Language Translator service.

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

        """

        WatsonService.__init__(
            self,
            vcap_services_name='language_translator',
            url=url,
            username=username,
            password=password,
            use_vcap_services=True)

    #########################
    # translate
    #########################

    def translate(self, text, model_id=None, source=None, target=None):
        """
        Translates the input text from the source language to the target language.

        :param list[str] text: Input text in UTF-8 encoding. It is a list so that multiple paragraphs can be submitted. Also accept a single string, instead of an array, as valid input.
        :param str model_id: The unique model_id of the translation model being used to translate text. The model_id inherently specifies source language, target language, and domain. If the model_id is specified, there is no need for the source and target parameters and the values are ignored.
        :param str source: Used in combination with target as an alternative way to select the model for translation. When target and source are set, and model_id is not set, the system chooses a default model with the right language pair to translate (usually the model based on the news domain).
        :param str target: Used in combination with source as an alternative way to select the model for translation. When target and source are set, and model_id is not set, the system chooses a default model with the right language pair to translate (usually the model based on the news domain).
        :return: A `dict` containing the `TranslationResult` response.
        :rtype: dict
        """
        if text is None:
            raise ValueError('text must be provided')
        data = {
            'text': text,
            'model_id': model_id,
            'source': source,
            'target': target
        }
        url = '/v2/translate'
        response = self.request(
            method='POST', url=url, json=data, accept_json=True)
        return response

    #########################
    # identify
    #########################

    def identify(self, text):
        """
        Identifies the language of the input text.

        :param str text: Input text in UTF-8 format.
        :return: A `dict` containing the `IdentifiedLanguages` response.
        :rtype: dict
        """
        if text is None:
            raise ValueError('text must be provided')
        data = text
        headers = {'content-type': 'text/plain'}
        url = '/v2/identify'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            data=data,
            accept_json=True)
        return response

    def list_identifiable_languages(self):
        """
        Lists all languages that can be identified by the API.

        Lists all languages that the service can identify. Returns the two-letter code
        (for example, `en` for English or `es` for Spanish) and name of each language.

        :return: A `dict` containing the `IdentifiableLanguages` response.
        :rtype: dict
        """
        url = '/v2/identifiable_languages'
        response = self.request(method='GET', url=url, accept_json=True)
        return response

    #########################
    # models
    #########################

    def create_model(self,
                     base_model_id,
                     name=None,
                     forced_glossary=None,
                     parallel_corpus=None,
                     monolingual_corpus=None,
                     forced_glossary_filename=None,
                     parallel_corpus_filename=None,
                     monolingual_corpus_filename=None):
        """
        Uploads a TMX glossary file on top of a domain to customize a translation model.

        :param str base_model_id: Specifies the domain model that is used as the base for the training. To see current supported domain models, use the GET /v2/models parameter.
        :param str name: The model name. Valid characters are letters, numbers, -, and _. No spaces.
        :param file forced_glossary: A TMX file with your customizations. The customizations in the file completely overwrite the domain data translation, including high frequency or high confidence phrase translations. You can upload only one glossary with a file size less than 10 MB per call.
        :param file parallel_corpus: A TMX file that contains entries that are treated as a parallel corpus instead of a glossary.
        :param file monolingual_corpus: A UTF-8 encoded plain text file that is used to customize the target language model.
        :param str forced_glossary_filename: The filename for forced_glossary.
        :param str parallel_corpus_filename: The filename for parallel_corpus.
        :param str monolingual_corpus_filename: The filename for monolingual_corpus.
        :return: A `dict` containing the `TranslationModel` response.
        :rtype: dict
        """
        if base_model_id is None:
            raise ValueError('base_model_id must be provided')
        params = {'base_model_id': base_model_id, 'name': name}
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
        monolingual_corpus_tuple = None
        if monolingual_corpus:
            if not monolingual_corpus_filename and hasattr(
                    monolingual_corpus, 'name'):
                monolingual_corpus_filename = monolingual_corpus.name
            mime_type = 'text/plain'
            monolingual_corpus_tuple = (monolingual_corpus_filename,
                                        monolingual_corpus, mime_type)
        url = '/v2/models'
        response = self.request(
            method='POST',
            url=url,
            params=params,
            files={
                'forced_glossary': forced_glossary_tuple,
                'parallel_corpus': parallel_corpus_tuple,
                'monolingual_corpus': monolingual_corpus_tuple
            },
            accept_json=True)
        return response

    def delete_model(self, model_id):
        """
        Deletes a custom translation model.

        :param str model_id: The model identifier.
        :return: A `dict` containing the `DeleteModelResult` response.
        :rtype: dict
        """
        if model_id is None:
            raise ValueError('model_id must be provided')
        url = '/v2/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(method='DELETE', url=url, accept_json=True)
        return response

    def get_model(self, model_id):
        """
        Get information about the given translation model, including training status.

        :param str model_id: Model ID to use.
        :return: A `dict` containing the `TranslationModel` response.
        :rtype: dict
        """
        if model_id is None:
            raise ValueError('model_id must be provided')
        url = '/v2/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(method='GET', url=url, accept_json=True)
        return response

    def list_models(self, source=None, target=None, default_models=None):
        """
        Lists available standard and custom models by source or target language.

        :param str source: Filter models by source language.
        :param str target: Filter models by target language.
        :param bool default_models: Valid values are leaving it unset, `true`, and `false`. When `true`, it filters models to return the default_models model or models. When `false`, it returns the non-default_models model or models. If not set, it returns all models, default_models and non-default_models.
        :return: A `dict` containing the `TranslationModels` response.
        :rtype: dict
        """
        params = {'source': source, 'target': target, 'default': default_models}
        url = '/v2/models'
        response = self.request(
            method='GET', url=url, params=params, accept_json=True)
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
            args['status'] = _dict['status']
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

    :attr str language: The code for an identifiable language.
    :attr str name: The name of the identifiable language.
    """

    def __init__(self, language, name):
        """
        Initialize a IdentifiableLanguage object.

        :param str language: The code for an identifiable language.
        :param str name: The name of the identifiable language.
        """
        self.language = language
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiableLanguage object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict['language']
        else:
            raise ValueError(
                'Required property \'language\' not present in IdentifiableLanguage JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict['name']
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

    :attr list[IdentifiableLanguage] languages: A list of all languages that the service can identify.
    """

    def __init__(self, languages):
        """
        Initialize a IdentifiableLanguages object.

        :param list[IdentifiableLanguage] languages: A list of all languages that the service can identify.
        """
        self.languages = languages

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiableLanguages object from a json dictionary."""
        args = {}
        if 'languages' in _dict:
            args['languages'] = [
                IdentifiableLanguage._from_dict(x) for x in _dict['languages']
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

    :attr str language: The code for an identified language.
    :attr float confidence: The confidence score for the identified language.
    """

    def __init__(self, language, confidence):
        """
        Initialize a IdentifiedLanguage object.

        :param str language: The code for an identified language.
        :param float confidence: The confidence score for the identified language.
        """
        self.language = language
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiedLanguage object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict['language']
        else:
            raise ValueError(
                'Required property \'language\' not present in IdentifiedLanguage JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict['confidence']
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

    :attr list[IdentifiedLanguage] languages: A ranking of identified languages with confidence scores.
    """

    def __init__(self, languages):
        """
        Initialize a IdentifiedLanguages object.

        :param list[IdentifiedLanguage] languages: A ranking of identified languages with confidence scores.
        """
        self.languages = languages

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IdentifiedLanguages object from a json dictionary."""
        args = {}
        if 'languages' in _dict:
            args['languages'] = [
                IdentifiedLanguage._from_dict(x) for x in _dict['languages']
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
        if 'translation' in _dict:
            args['translation_output'] = _dict['translation']
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

    :attr str model_id: A globally unique string that identifies the underlying model that is used for translation. This string contains all the information about source language, target language, domain, and various other related configurations.
    :attr str name: (optional) If a model is trained by a user, there might be an optional “name” parameter attached during training to help the user identify the model.
    :attr str source: (optional) Source language in two letter language code. Use the five letter code when clarifying between multiple supported languages. When model_id is used directly, it will override the source-target language combination. Also, when a two letter language code is used, but no suitable default is found, it returns an error.
    :attr str target: (optional) Target language in two letter language code.
    :attr str base_model_id: (optional) If this model is a custom model, this returns the base model that it is trained on. For a base model, this response value is empty.
    :attr str domain: (optional) The domain of the translation model.
    :attr bool customizable: (optional) Whether this model can be used as a base for customization. Customized models are not further customizable, and we don't allow the customization of certain base models.
    :attr bool default_model: (optional) Whether this model is considered a default model and is used when the source and target languages are specified without the model_id.
    :attr str owner: (optional) Returns the Bluemix ID of the instance that created the model, or an empty string if it is a model that is trained by IBM.
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

        :param str model_id: A globally unique string that identifies the underlying model that is used for translation. This string contains all the information about source language, target language, domain, and various other related configurations.
        :param str name: (optional) If a model is trained by a user, there might be an optional “name” parameter attached during training to help the user identify the model.
        :param str source: (optional) Source language in two letter language code. Use the five letter code when clarifying between multiple supported languages. When model_id is used directly, it will override the source-target language combination. Also, when a two letter language code is used, but no suitable default is found, it returns an error.
        :param str target: (optional) Target language in two letter language code.
        :param str base_model_id: (optional) If this model is a custom model, this returns the base model that it is trained on. For a base model, this response value is empty.
        :param str domain: (optional) The domain of the translation model.
        :param bool customizable: (optional) Whether this model can be used as a base for customization. Customized models are not further customizable, and we don't allow the customization of certain base models.
        :param bool default_model: (optional) Whether this model is considered a default model and is used when the source and target languages are specified without the model_id.
        :param str owner: (optional) Returns the Bluemix ID of the instance that created the model, or an empty string if it is a model that is trained by IBM.
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
            args['model_id'] = _dict['model_id']
        else:
            raise ValueError(
                'Required property \'model_id\' not present in TranslationModel JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict['name']
        if 'source' in _dict:
            args['source'] = _dict['source']
        if 'target' in _dict:
            args['target'] = _dict['target']
        if 'base_model_id' in _dict:
            args['base_model_id'] = _dict['base_model_id']
        if 'domain' in _dict:
            args['domain'] = _dict['domain']
        if 'customizable' in _dict:
            args['customizable'] = _dict['customizable']
        if 'default_model' in _dict:
            args['default_model'] = _dict['default_model']
        if 'owner' in _dict:
            args['owner'] = _dict['owner']
        if 'status' in _dict:
            args['status'] = _dict['status']
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
                TranslationModel._from_dict(x) for x in _dict['models']
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

    :attr int word_count: Number of words of the complete input text.
    :attr int character_count: Number of characters of the complete input text.
    :attr list[Translation] translations: List of translation output in UTF-8, corresponding to the list of input text.
    """

    def __init__(self, word_count, character_count, translations):
        """
        Initialize a TranslationResult object.

        :param int word_count: Number of words of the complete input text.
        :param int character_count: Number of characters of the complete input text.
        :param list[Translation] translations: List of translation output in UTF-8, corresponding to the list of input text.
        """
        self.word_count = word_count
        self.character_count = character_count
        self.translations = translations

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TranslationResult object from a json dictionary."""
        args = {}
        if 'word_count' in _dict:
            args['word_count'] = _dict['word_count']
        else:
            raise ValueError(
                'Required property \'word_count\' not present in TranslationResult JSON'
            )
        if 'character_count' in _dict:
            args['character_count'] = _dict['character_count']
        else:
            raise ValueError(
                'Required property \'character_count\' not present in TranslationResult JSON'
            )
        if 'translations' in _dict:
            args['translations'] = [
                Translation._from_dict(x) for x in _dict['translations']
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
