# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2020.
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
Analyze various features of text content at scale. Provide text, raw HTML, or a public URL
and IBM Watson Natural Language Understanding will give you results for the features you
request. The service cleans HTML content before analysis by default, so the results can
ignore most advertisements and other unwanted content.
You can create [custom
models](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
with Watson Knowledge Studio to detect custom entities and relations in Natural Language
Understanding.
"""

import json
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from .common import get_sdk_headers
from datetime import datetime
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import DetailedResponse
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from typing import Dict
from typing import List

##############################################################################
# Service
##############################################################################


class NaturalLanguageUnderstandingV1(BaseService):
    """The Natural Language Understanding V1 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/natural-language-understanding/api'
    DEFAULT_SERVICE_NAME = 'natural-language-understanding'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Natural Language Understanding service.

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

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator,
                             disable_ssl_verification=False)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Analyze
    #########################

    def analyze(self,
                features: 'Features',
                *,
                text: str = None,
                html: str = None,
                url: str = None,
                clean: bool = None,
                xpath: str = None,
                fallback_to_raw: bool = None,
                return_analyzed_text: bool = None,
                language: str = None,
                limit_text_characters: int = None,
                **kwargs) -> 'DetailedResponse':
        """
        Analyze text.

        Analyzes text, HTML, or a public webpage for the following features:
        - Categories
        - Concepts
        - Emotion
        - Entities
        - Keywords
        - Metadata
        - Relations
        - Semantic roles
        - Sentiment
        - Syntax (Experimental).
        If a language for the input text is not specified with the `language` parameter,
        the service [automatically detects the
        language](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-detectable-languages).

        :param Features features: Specific features to analyze the document for.
        :param str text: (optional) The plain text to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param str html: (optional) The HTML file to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param str url: (optional) The webpage to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param bool clean: (optional) Set this to `false` to disable webpage
               cleaning. To learn more about webpage cleaning, see the [Analyzing
               webpages](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-analyzing-webpages)
               documentation.
        :param str xpath: (optional) An [XPath
               query](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-analyzing-webpages#xpath)
               to perform on `html` or `url` input. Results of the query will be appended
               to the cleaned webpage text before it is analyzed. To analyze only the
               results of the XPath query, set the `clean` parameter to `false`.
        :param bool fallback_to_raw: (optional) Whether to use raw HTML content if
               text cleaning fails.
        :param bool return_analyzed_text: (optional) Whether or not to return the
               analyzed text.
        :param str language: (optional) ISO 639-1 code that specifies the language
               of your text. This overrides automatic language detection. Language support
               differs depending on the features you include in your analysis. See
               [Language
               support](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-language-support)
               for more information.
        :param int limit_text_characters: (optional) Sets the maximum number of
               characters that are processed by the service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if features is None:
            raise ValueError('features must be provided')
        features = self._convert_model(features)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='analyze')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'features': features,
            'text': text,
            'html': html,
            'url': url,
            'clean': clean,
            'xpath': xpath,
            'fallback_to_raw': fallback_to_raw,
            'return_analyzed_text': return_analyzed_text,
            'language': language,
            'limit_text_characters': limit_text_characters
        }

        url = '/v1/analyze'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Manage models
    #########################

    def list_models(self, **kwargs) -> 'DetailedResponse':
        """
        List models.

        Lists Watson Knowledge Studio [custom entities and relations
        models](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
        that are deployed to your Natural Language Understanding service.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_models')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/models'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_model(self, model_id: str, **kwargs) -> 'DetailedResponse':
        """
        Delete model.

        Deletes a custom model.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='delete_model')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/models/{0}'.format(*self._encode_path_vars(model_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class AnalysisResults():
    """
    Results of the analysis, organized by feature.

    :attr str language: (optional) Language used to analyze the text.
    :attr str analyzed_text: (optional) Text that was used in the analysis.
    :attr str retrieved_url: (optional) URL of the webpage that was analyzed.
    :attr AnalysisResultsUsage usage: (optional) API usage information for the
          request.
    :attr List[ConceptsResult] concepts: (optional) The general concepts referenced
          or alluded to in the analyzed text.
    :attr List[EntitiesResult] entities: (optional) The entities detected in the
          analyzed text.
    :attr List[KeywordsResult] keywords: (optional) The keywords from the analyzed
          text.
    :attr List[CategoriesResult] categories: (optional) The categories that the
          service assigned to the analyzed text.
    :attr EmotionResult emotion: (optional) The anger, disgust, fear, joy, or
          sadness conveyed by the content.
    :attr AnalysisResultsMetadata metadata: (optional) Webpage metadata, such as the
          author and the title of the page.
    :attr List[RelationsResult] relations: (optional) The relationships between
          entities in the content.
    :attr List[SemanticRolesResult] semantic_roles: (optional) Sentences parsed into
          `subject`, `action`, and `object` form.
    :attr SentimentResult sentiment: (optional) The sentiment of the content.
    :attr SyntaxResult syntax: (optional) Tokens and sentences returned from syntax
          analysis.
    """

    def __init__(self,
                 *,
                 language: str = None,
                 analyzed_text: str = None,
                 retrieved_url: str = None,
                 usage: 'AnalysisResultsUsage' = None,
                 concepts: List['ConceptsResult'] = None,
                 entities: List['EntitiesResult'] = None,
                 keywords: List['KeywordsResult'] = None,
                 categories: List['CategoriesResult'] = None,
                 emotion: 'EmotionResult' = None,
                 metadata: 'AnalysisResultsMetadata' = None,
                 relations: List['RelationsResult'] = None,
                 semantic_roles: List['SemanticRolesResult'] = None,
                 sentiment: 'SentimentResult' = None,
                 syntax: 'SyntaxResult' = None) -> None:
        """
        Initialize a AnalysisResults object.

        :param str language: (optional) Language used to analyze the text.
        :param str analyzed_text: (optional) Text that was used in the analysis.
        :param str retrieved_url: (optional) URL of the webpage that was analyzed.
        :param AnalysisResultsUsage usage: (optional) API usage information for the
               request.
        :param List[ConceptsResult] concepts: (optional) The general concepts
               referenced or alluded to in the analyzed text.
        :param List[EntitiesResult] entities: (optional) The entities detected in
               the analyzed text.
        :param List[KeywordsResult] keywords: (optional) The keywords from the
               analyzed text.
        :param List[CategoriesResult] categories: (optional) The categories that
               the service assigned to the analyzed text.
        :param EmotionResult emotion: (optional) The anger, disgust, fear, joy, or
               sadness conveyed by the content.
        :param AnalysisResultsMetadata metadata: (optional) Webpage metadata, such
               as the author and the title of the page.
        :param List[RelationsResult] relations: (optional) The relationships
               between entities in the content.
        :param List[SemanticRolesResult] semantic_roles: (optional) Sentences
               parsed into `subject`, `action`, and `object` form.
        :param SentimentResult sentiment: (optional) The sentiment of the content.
        :param SyntaxResult syntax: (optional) Tokens and sentences returned from
               syntax analysis.
        """
        self.language = language
        self.analyzed_text = analyzed_text
        self.retrieved_url = retrieved_url
        self.usage = usage
        self.concepts = concepts
        self.entities = entities
        self.keywords = keywords
        self.categories = categories
        self.emotion = emotion
        self.metadata = metadata
        self.relations = relations
        self.semantic_roles = semantic_roles
        self.sentiment = sentiment
        self.syntax = syntax

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalysisResults':
        """Initialize a AnalysisResults object from a json dictionary."""
        args = {}
        valid_keys = [
            'language', 'analyzed_text', 'retrieved_url', 'usage', 'concepts',
            'entities', 'keywords', 'categories', 'emotion', 'metadata',
            'relations', 'semantic_roles', 'sentiment', 'syntax'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AnalysisResults: '
                + ', '.join(bad_keys))
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'analyzed_text' in _dict:
            args['analyzed_text'] = _dict.get('analyzed_text')
        if 'retrieved_url' in _dict:
            args['retrieved_url'] = _dict.get('retrieved_url')
        if 'usage' in _dict:
            args['usage'] = AnalysisResultsUsage._from_dict(_dict.get('usage'))
        if 'concepts' in _dict:
            args['concepts'] = [
                ConceptsResult._from_dict(x) for x in (_dict.get('concepts'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                EntitiesResult._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'keywords' in _dict:
            args['keywords'] = [
                KeywordsResult._from_dict(x) for x in (_dict.get('keywords'))
            ]
        if 'categories' in _dict:
            args['categories'] = [
                CategoriesResult._from_dict(x)
                for x in (_dict.get('categories'))
            ]
        if 'emotion' in _dict:
            args['emotion'] = EmotionResult._from_dict(_dict.get('emotion'))
        if 'metadata' in _dict:
            args['metadata'] = AnalysisResultsMetadata._from_dict(
                _dict.get('metadata'))
        if 'relations' in _dict:
            args['relations'] = [
                RelationsResult._from_dict(x) for x in (_dict.get('relations'))
            ]
        if 'semantic_roles' in _dict:
            args['semantic_roles'] = [
                SemanticRolesResult._from_dict(x)
                for x in (_dict.get('semantic_roles'))
            ]
        if 'sentiment' in _dict:
            args['sentiment'] = SentimentResult._from_dict(
                _dict.get('sentiment'))
        if 'syntax' in _dict:
            args['syntax'] = SyntaxResult._from_dict(_dict.get('syntax'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'analyzed_text') and self.analyzed_text is not None:
            _dict['analyzed_text'] = self.analyzed_text
        if hasattr(self, 'retrieved_url') and self.retrieved_url is not None:
            _dict['retrieved_url'] = self.retrieved_url
        if hasattr(self, 'usage') and self.usage is not None:
            _dict['usage'] = self.usage._to_dict()
        if hasattr(self, 'concepts') and self.concepts is not None:
            _dict['concepts'] = [x._to_dict() for x in self.concepts]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = [x._to_dict() for x in self.keywords]
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = [x._to_dict() for x in self.categories]
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata._to_dict()
        if hasattr(self, 'relations') and self.relations is not None:
            _dict['relations'] = [x._to_dict() for x in self.relations]
        if hasattr(self, 'semantic_roles') and self.semantic_roles is not None:
            _dict['semantic_roles'] = [
                x._to_dict() for x in self.semantic_roles
            ]
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment._to_dict()
        if hasattr(self, 'syntax') and self.syntax is not None:
            _dict['syntax'] = self.syntax._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalysisResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AnalysisResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalysisResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalysisResultsMetadata():
    """
    Webpage metadata, such as the author and the title of the page.

    :attr List[Author] authors: (optional) The authors of the document.
    :attr str publication_date: (optional) The publication date in the format ISO
          8601.
    :attr str title: (optional) The title of the document.
    :attr str image: (optional) URL of a prominent image on the webpage.
    :attr List[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
    """

    def __init__(self,
                 *,
                 authors: List['Author'] = None,
                 publication_date: str = None,
                 title: str = None,
                 image: str = None,
                 feeds: List['Feed'] = None) -> None:
        """
        Initialize a AnalysisResultsMetadata object.

        :param List[Author] authors: (optional) The authors of the document.
        :param str publication_date: (optional) The publication date in the format
               ISO 8601.
        :param str title: (optional) The title of the document.
        :param str image: (optional) URL of a prominent image on the webpage.
        :param List[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
        """
        self.authors = authors
        self.publication_date = publication_date
        self.title = title
        self.image = image
        self.feeds = feeds

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalysisResultsMetadata':
        """Initialize a AnalysisResultsMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['authors', 'publication_date', 'title', 'image', 'feeds']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AnalysisResultsMetadata: '
                + ', '.join(bad_keys))
        if 'authors' in _dict:
            args['authors'] = [
                Author._from_dict(x) for x in (_dict.get('authors'))
            ]
        if 'publication_date' in _dict:
            args['publication_date'] = _dict.get('publication_date')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        if 'feeds' in _dict:
            args['feeds'] = [Feed._from_dict(x) for x in (_dict.get('feeds'))]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResultsMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authors') and self.authors is not None:
            _dict['authors'] = [x._to_dict() for x in self.authors]
        if hasattr(self,
                   'publication_date') and self.publication_date is not None:
            _dict['publication_date'] = self.publication_date
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        if hasattr(self, 'feeds') and self.feeds is not None:
            _dict['feeds'] = [x._to_dict() for x in self.feeds]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalysisResultsMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AnalysisResultsMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalysisResultsMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalysisResultsUsage():
    """
    API usage information for the request.

    :attr int features: (optional) Number of features used in the API call.
    :attr int text_characters: (optional) Number of text characters processed.
    :attr int text_units: (optional) Number of 10,000-character units processed.
    """

    def __init__(self,
                 *,
                 features: int = None,
                 text_characters: int = None,
                 text_units: int = None) -> None:
        """
        Initialize a AnalysisResultsUsage object.

        :param int features: (optional) Number of features used in the API call.
        :param int text_characters: (optional) Number of text characters processed.
        :param int text_units: (optional) Number of 10,000-character units
               processed.
        """
        self.features = features
        self.text_characters = text_characters
        self.text_units = text_units

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalysisResultsUsage':
        """Initialize a AnalysisResultsUsage object from a json dictionary."""
        args = {}
        valid_keys = ['features', 'text_characters', 'text_units']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AnalysisResultsUsage: '
                + ', '.join(bad_keys))
        if 'features' in _dict:
            args['features'] = _dict.get('features')
        if 'text_characters' in _dict:
            args['text_characters'] = _dict.get('text_characters')
        if 'text_units' in _dict:
            args['text_units'] = _dict.get('text_units')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResultsUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features
        if hasattr(self,
                   'text_characters') and self.text_characters is not None:
            _dict['text_characters'] = self.text_characters
        if hasattr(self, 'text_units') and self.text_units is not None:
            _dict['text_units'] = self.text_units
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalysisResultsUsage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AnalysisResultsUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalysisResultsUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Author():
    """
    The author of the analyzed content.

    :attr str name: (optional) Name of the author.
    """

    def __init__(self, *, name: str = None) -> None:
        """
        Initialize a Author object.

        :param str name: (optional) Name of the author.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Author':
        """Initialize a Author object from a json dictionary."""
        args = {}
        valid_keys = ['name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Author: ' +
                ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Author object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Author object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Author') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Author') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesOptions():
    """
    Returns a five-level taxonomy of the content. The top three categories are returned.
    Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Spanish.

    :attr bool explanation: (optional) Set this to `true` to return explanations for
          each categorization. **This is available only for English categories.**.
    :attr int limit: (optional) Maximum number of categories to return.
    :attr str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the standard categories model.
          The custom categories experimental feature will be retired on 19 December 2019.
          On that date, deployed custom categories models will no longer be accessible in
          Natural Language Understanding. The feature will be removed from Knowledge
          Studio on an earlier date. Custom categories models will no longer be accessible
          in Knowledge Studio on 17 December 2019.
    """

    def __init__(self,
                 *,
                 explanation: bool = None,
                 limit: int = None,
                 model: str = None) -> None:
        """
        Initialize a CategoriesOptions object.

        :param bool explanation: (optional) Set this to `true` to return
               explanations for each categorization. **This is available only for English
               categories.**.
        :param int limit: (optional) Maximum number of categories to return.
        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the standard categories model.
               The custom categories experimental feature will be retired on 19 December
               2019. On that date, deployed custom categories models will no longer be
               accessible in Natural Language Understanding. The feature will be removed
               from Knowledge Studio on an earlier date. Custom categories models will no
               longer be accessible in Knowledge Studio on 17 December 2019.
        """
        self.explanation = explanation
        self.limit = limit
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesOptions':
        """Initialize a CategoriesOptions object from a json dictionary."""
        args = {}
        valid_keys = ['explanation', 'limit', 'model']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoriesOptions: '
                + ', '.join(bad_keys))
        if 'explanation' in _dict:
            args['explanation'] = _dict.get('explanation')
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'explanation') and self.explanation is not None:
            _dict['explanation'] = self.explanation
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesRelevantText():
    """
    Relevant text that contributed to the categorization.

    :attr str text: (optional) Text from the analyzed source that supports the
          categorization.
    """

    def __init__(self, *, text: str = None) -> None:
        """
        Initialize a CategoriesRelevantText object.

        :param str text: (optional) Text from the analyzed source that supports the
               categorization.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesRelevantText':
        """Initialize a CategoriesRelevantText object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoriesRelevantText: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesRelevantText object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesRelevantText object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesRelevantText') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesRelevantText') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesResult():
    """
    A categorization of the analyzed text.

    :attr str label: (optional) The path to the category through the 5-level
          taxonomy hierarchy. For the complete list of categories, see the [Categories
          hierarchy](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories#categories-hierarchy)
          documentation.
    :attr float score: (optional) Confidence score for the category classification.
          Higher values indicate greater confidence.
    :attr CategoriesResultExplanation explanation: (optional) Information that helps
          to explain what contributed to the categories result.
    """

    def __init__(self,
                 *,
                 label: str = None,
                 score: float = None,
                 explanation: 'CategoriesResultExplanation' = None) -> None:
        """
        Initialize a CategoriesResult object.

        :param str label: (optional) The path to the category through the 5-level
               taxonomy hierarchy. For the complete list of categories, see the
               [Categories
               hierarchy](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories#categories-hierarchy)
               documentation.
        :param float score: (optional) Confidence score for the category
               classification. Higher values indicate greater confidence.
        :param CategoriesResultExplanation explanation: (optional) Information that
               helps to explain what contributed to the categories result.
        """
        self.label = label
        self.score = score
        self.explanation = explanation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesResult':
        """Initialize a CategoriesResult object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'score', 'explanation']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoriesResult: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        if 'explanation' in _dict:
            args['explanation'] = CategoriesResultExplanation._from_dict(
                _dict.get('explanation'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'explanation') and self.explanation is not None:
            _dict['explanation'] = self.explanation._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesResultExplanation():
    """
    Information that helps to explain what contributed to the categories result.

    :attr List[CategoriesRelevantText] relevant_text: (optional) An array of
          relevant text from the source that contributed to the categorization. The sorted
          array begins with the phrase that contributed most significantly to the result,
          followed by phrases that were less and less impactful.
    """

    def __init__(self,
                 *,
                 relevant_text: List['CategoriesRelevantText'] = None) -> None:
        """
        Initialize a CategoriesResultExplanation object.

        :param List[CategoriesRelevantText] relevant_text: (optional) An array of
               relevant text from the source that contributed to the categorization. The
               sorted array begins with the phrase that contributed most significantly to
               the result, followed by phrases that were less and less impactful.
        """
        self.relevant_text = relevant_text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesResultExplanation':
        """Initialize a CategoriesResultExplanation object from a json dictionary."""
        args = {}
        valid_keys = ['relevant_text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CategoriesResultExplanation: '
                + ', '.join(bad_keys))
        if 'relevant_text' in _dict:
            args['relevant_text'] = [
                CategoriesRelevantText._from_dict(x)
                for x in (_dict.get('relevant_text'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesResultExplanation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'relevant_text') and self.relevant_text is not None:
            _dict['relevant_text'] = [x._to_dict() for x in self.relevant_text]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesResultExplanation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesResultExplanation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesResultExplanation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConceptsOptions():
    """
    Returns high-level concepts in the content. For example, a research paper about deep
    learning might return the concept, "Artificial Intelligence" although the term is not
    mentioned.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Spanish.

    :attr int limit: (optional) Maximum number of concepts to return.
    """

    def __init__(self, *, limit: int = None) -> None:
        """
        Initialize a ConceptsOptions object.

        :param int limit: (optional) Maximum number of concepts to return.
        """
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConceptsOptions':
        """Initialize a ConceptsOptions object from a json dictionary."""
        args = {}
        valid_keys = ['limit']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ConceptsOptions: '
                + ', '.join(bad_keys))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConceptsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ConceptsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConceptsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConceptsResult():
    """
    The general concepts referenced or alluded to in the analyzed text.

    :attr str text: (optional) Name of the concept.
    :attr float relevance: (optional) Relevance score between 0 and 1. Higher scores
          indicate greater relevance.
    :attr str dbpedia_resource: (optional) Link to the corresponding DBpedia
          resource.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 relevance: float = None,
                 dbpedia_resource: str = None) -> None:
        """
        Initialize a ConceptsResult object.

        :param str text: (optional) Name of the concept.
        :param float relevance: (optional) Relevance score between 0 and 1. Higher
               scores indicate greater relevance.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
               resource.
        """
        self.text = text
        self.relevance = relevance
        self.dbpedia_resource = dbpedia_resource

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConceptsResult':
        """Initialize a ConceptsResult object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'relevance', 'dbpedia_resource']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ConceptsResult: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        if 'dbpedia_resource' in _dict:
            args['dbpedia_resource'] = _dict.get('dbpedia_resource')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self,
                   'dbpedia_resource') and self.dbpedia_resource is not None:
            _dict['dbpedia_resource'] = self.dbpedia_resource
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConceptsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ConceptsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConceptsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteModelResults():
    """
    Delete model results.

    :attr str deleted: (optional) model_id of the deleted model.
    """

    def __init__(self, *, deleted: str = None) -> None:
        """
        Initialize a DeleteModelResults object.

        :param str deleted: (optional) model_id of the deleted model.
        """
        self.deleted = deleted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteModelResults':
        """Initialize a DeleteModelResults object from a json dictionary."""
        args = {}
        valid_keys = ['deleted']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DeleteModelResults: '
                + ', '.join(bad_keys))
        if 'deleted' in _dict:
            args['deleted'] = _dict.get('deleted')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteModelResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteModelResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DeleteModelResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteModelResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DisambiguationResult():
    """
    Disambiguation information for the entity.

    :attr str name: (optional) Common entity name.
    :attr str dbpedia_resource: (optional) Link to the corresponding DBpedia
          resource.
    :attr List[str] subtype: (optional) Entity subtype information.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 dbpedia_resource: str = None,
                 subtype: List[str] = None) -> None:
        """
        Initialize a DisambiguationResult object.

        :param str name: (optional) Common entity name.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
               resource.
        :param List[str] subtype: (optional) Entity subtype information.
        """
        self.name = name
        self.dbpedia_resource = dbpedia_resource
        self.subtype = subtype

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DisambiguationResult':
        """Initialize a DisambiguationResult object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'dbpedia_resource', 'subtype']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DisambiguationResult: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'dbpedia_resource' in _dict:
            args['dbpedia_resource'] = _dict.get('dbpedia_resource')
        if 'subtype' in _dict:
            args['subtype'] = _dict.get('subtype')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DisambiguationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self,
                   'dbpedia_resource') and self.dbpedia_resource is not None:
            _dict['dbpedia_resource'] = self.dbpedia_resource
        if hasattr(self, 'subtype') and self.subtype is not None:
            _dict['subtype'] = self.subtype
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DisambiguationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DisambiguationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DisambiguationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentEmotionResults():
    """
    Emotion results for the document as a whole.

    :attr EmotionScores emotion: (optional) Emotion results for the document as a
          whole.
    """

    def __init__(self, *, emotion: 'EmotionScores' = None) -> None:
        """
        Initialize a DocumentEmotionResults object.

        :param EmotionScores emotion: (optional) Emotion results for the document
               as a whole.
        """
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentEmotionResults':
        """Initialize a DocumentEmotionResults object from a json dictionary."""
        args = {}
        valid_keys = ['emotion']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentEmotionResults: '
                + ', '.join(bad_keys))
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentEmotionResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentEmotionResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentEmotionResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentEmotionResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentSentimentResults():
    """
    DocumentSentimentResults.

    :attr str label: (optional) Indicates whether the sentiment is positive,
          neutral, or negative.
    :attr float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(self, *, label: str = None, score: float = None) -> None:
        """
        Initialize a DocumentSentimentResults object.

        :param str label: (optional) Indicates whether the sentiment is positive,
               neutral, or negative.
        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.label = label
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentSentimentResults':
        """Initialize a DocumentSentimentResults object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'score']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DocumentSentimentResults: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DocumentSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionOptions():
    """
    Detects anger, disgust, fear, joy, or sadness that is conveyed in the content or by
    the context around target phrases specified in the targets parameter. You can analyze
    emotion for detected entities with `entities.emotion` and for keywords with
    `keywords.emotion`.
    Supported languages: English.

    :attr bool document: (optional) Set this to `false` to hide document-level
          emotion results.
    :attr List[str] targets: (optional) Emotion results will be returned for each
          target string that is found in the document.
    """

    def __init__(self,
                 *,
                 document: bool = None,
                 targets: List[str] = None) -> None:
        """
        Initialize a EmotionOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
               emotion results.
        :param List[str] targets: (optional) Emotion results will be returned for
               each target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionOptions':
        """Initialize a EmotionOptions object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EmotionOptions: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EmotionOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionResult():
    """
    The detected anger, disgust, fear, joy, or sadness that is conveyed by the content.
    Emotion information can be returned for detected entities, keywords, or user-specified
    target phrases found in the text.

    :attr DocumentEmotionResults document: (optional) Emotion results for the
          document as a whole.
    :attr List[TargetedEmotionResults] targets: (optional) Emotion results for
          specified targets.
    """

    def __init__(self,
                 *,
                 document: 'DocumentEmotionResults' = None,
                 targets: List['TargetedEmotionResults'] = None) -> None:
        """
        Initialize a EmotionResult object.

        :param DocumentEmotionResults document: (optional) Emotion results for the
               document as a whole.
        :param List[TargetedEmotionResults] targets: (optional) Emotion results for
               specified targets.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionResult':
        """Initialize a EmotionResult object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EmotionResult: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = DocumentEmotionResults._from_dict(
                _dict.get('document'))
        if 'targets' in _dict:
            args['targets'] = [
                TargetedEmotionResults._from_dict(x)
                for x in (_dict.get('targets'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x._to_dict() for x in self.targets]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EmotionResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionScores():
    """
    EmotionScores.

    :attr float anger: (optional) Anger score from 0 to 1. A higher score means that
          the text is more likely to convey anger.
    :attr float disgust: (optional) Disgust score from 0 to 1. A higher score means
          that the text is more likely to convey disgust.
    :attr float fear: (optional) Fear score from 0 to 1. A higher score means that
          the text is more likely to convey fear.
    :attr float joy: (optional) Joy score from 0 to 1. A higher score means that the
          text is more likely to convey joy.
    :attr float sadness: (optional) Sadness score from 0 to 1. A higher score means
          that the text is more likely to convey sadness.
    """

    def __init__(self,
                 *,
                 anger: float = None,
                 disgust: float = None,
                 fear: float = None,
                 joy: float = None,
                 sadness: float = None) -> None:
        """
        Initialize a EmotionScores object.

        :param float anger: (optional) Anger score from 0 to 1. A higher score
               means that the text is more likely to convey anger.
        :param float disgust: (optional) Disgust score from 0 to 1. A higher score
               means that the text is more likely to convey disgust.
        :param float fear: (optional) Fear score from 0 to 1. A higher score means
               that the text is more likely to convey fear.
        :param float joy: (optional) Joy score from 0 to 1. A higher score means
               that the text is more likely to convey joy.
        :param float sadness: (optional) Sadness score from 0 to 1. A higher score
               means that the text is more likely to convey sadness.
        """
        self.anger = anger
        self.disgust = disgust
        self.fear = fear
        self.joy = joy
        self.sadness = sadness

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionScores':
        """Initialize a EmotionScores object from a json dictionary."""
        args = {}
        valid_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EmotionScores: '
                + ', '.join(bad_keys))
        if 'anger' in _dict:
            args['anger'] = _dict.get('anger')
        if 'disgust' in _dict:
            args['disgust'] = _dict.get('disgust')
        if 'fear' in _dict:
            args['fear'] = _dict.get('fear')
        if 'joy' in _dict:
            args['joy'] = _dict.get('joy')
        if 'sadness' in _dict:
            args['sadness'] = _dict.get('sadness')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionScores object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'anger') and self.anger is not None:
            _dict['anger'] = self.anger
        if hasattr(self, 'disgust') and self.disgust is not None:
            _dict['disgust'] = self.disgust
        if hasattr(self, 'fear') and self.fear is not None:
            _dict['fear'] = self.fear
        if hasattr(self, 'joy') and self.joy is not None:
            _dict['joy'] = self.joy
        if hasattr(self, 'sadness') and self.sadness is not None:
            _dict['sadness'] = self.sadness
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionScores object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EmotionScores') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionScores') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesOptions():
    """
    Identifies people, cities, organizations, and other entities in the content. See
    [Entity types and
    subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-types).
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are supported only through
    custom models.

    :attr int limit: (optional) Maximum number of entities to return.
    :attr bool mentions: (optional) Set this to `true` to return locations of entity
          mentions.
    :attr str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the standard entity detection model.
    :attr bool sentiment: (optional) Set this to `true` to return sentiment
          information for detected entities.
    :attr bool emotion: (optional) Set this to `true` to analyze emotion for
          detected keywords.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 mentions: bool = None,
                 model: str = None,
                 sentiment: bool = None,
                 emotion: bool = None) -> None:
        """
        Initialize a EntitiesOptions object.

        :param int limit: (optional) Maximum number of entities to return.
        :param bool mentions: (optional) Set this to `true` to return locations of
               entity mentions.
        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the standard entity detection model.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
               information for detected entities.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for
               detected keywords.
        """
        self.limit = limit
        self.mentions = mentions
        self.model = model
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntitiesOptions':
        """Initialize a EntitiesOptions object from a json dictionary."""
        args = {}
        valid_keys = ['limit', 'mentions', 'model', 'sentiment', 'emotion']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntitiesOptions: '
                + ', '.join(bad_keys))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'mentions' in _dict:
            args['mentions'] = _dict.get('mentions')
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = self.mentions
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntitiesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EntitiesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntitiesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesResult():
    """
    The important people, places, geopolitical entities and other types of entities in
    your content.

    :attr str type: (optional) Entity type.
    :attr str text: (optional) The name of the entity.
    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values
          indicate greater relevance.
    :attr float confidence: (optional) Confidence in the entity identification from
          0 to 1. Higher values indicate higher confidence. In standard entities requests,
          confidence is returned only for English text. All entities requests that use
          custom models return the confidence score.
    :attr List[EntityMention] mentions: (optional) Entity mentions and locations.
    :attr int count: (optional) How many times the entity was mentioned in the text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the entity,
          enabled with the `emotion` option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results
          for the entity, enabled with the `sentiment` option.
    :attr DisambiguationResult disambiguation: (optional) Disambiguation information
          for the entity.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 text: str = None,
                 relevance: float = None,
                 confidence: float = None,
                 mentions: List['EntityMention'] = None,
                 count: int = None,
                 emotion: 'EmotionScores' = None,
                 sentiment: 'FeatureSentimentResults' = None,
                 disambiguation: 'DisambiguationResult' = None) -> None:
        """
        Initialize a EntitiesResult object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The name of the entity.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher
               values indicate greater relevance.
        :param float confidence: (optional) Confidence in the entity identification
               from 0 to 1. Higher values indicate higher confidence. In standard entities
               requests, confidence is returned only for English text. All entities
               requests that use custom models return the confidence score.
        :param List[EntityMention] mentions: (optional) Entity mentions and
               locations.
        :param int count: (optional) How many times the entity was mentioned in the
               text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the
               entity, enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis
               results for the entity, enabled with the `sentiment` option.
        :param DisambiguationResult disambiguation: (optional) Disambiguation
               information for the entity.
        """
        self.type = type
        self.text = text
        self.relevance = relevance
        self.confidence = confidence
        self.mentions = mentions
        self.count = count
        self.emotion = emotion
        self.sentiment = sentiment
        self.disambiguation = disambiguation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntitiesResult':
        """Initialize a EntitiesResult object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'text', 'relevance', 'confidence', 'mentions', 'count',
            'emotion', 'sentiment', 'disambiguation'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntitiesResult: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'mentions' in _dict:
            args['mentions'] = [
                EntityMention._from_dict(x) for x in (_dict.get('mentions'))
            ]
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        if 'sentiment' in _dict:
            args['sentiment'] = FeatureSentimentResults._from_dict(
                _dict.get('sentiment'))
        if 'disambiguation' in _dict:
            args['disambiguation'] = DisambiguationResult._from_dict(
                _dict.get('disambiguation'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = [x._to_dict() for x in self.mentions]
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment._to_dict()
        if hasattr(self, 'disambiguation') and self.disambiguation is not None:
            _dict['disambiguation'] = self.disambiguation._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntitiesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EntitiesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntitiesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMention():
    """
    EntityMention.

    :attr str text: (optional) Entity mention text.
    :attr List[int] location: (optional) Character offsets indicating the beginning
          and end of the mention in the analyzed text.
    :attr float confidence: (optional) Confidence in the entity identification from
          0 to 1. Higher values indicate higher confidence. In standard entities requests,
          confidence is returned only for English text. All entities requests that use
          custom models return the confidence score.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 location: List[int] = None,
                 confidence: float = None) -> None:
        """
        Initialize a EntityMention object.

        :param str text: (optional) Entity mention text.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the mention in the analyzed text.
        :param float confidence: (optional) Confidence in the entity identification
               from 0 to 1. Higher values indicate higher confidence. In standard entities
               requests, confidence is returned only for English text. All entities
               requests that use custom models return the confidence score.
        """
        self.text = text
        self.location = location
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityMention':
        """Initialize a EntityMention object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location', 'confidence']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntityMention: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMention object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntityMention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'EntityMention') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityMention') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeatureSentimentResults():
    """
    FeatureSentimentResults.

    :attr float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(self, *, score: float = None) -> None:
        """
        Initialize a FeatureSentimentResults object.

        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeatureSentimentResults':
        """Initialize a FeatureSentimentResults object from a json dictionary."""
        args = {}
        valid_keys = ['score']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FeatureSentimentResults: '
                + ', '.join(bad_keys))
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeatureSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeatureSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FeatureSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeatureSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Features():
    """
    Analysis features and options.

    :attr ConceptsOptions concepts: (optional) Returns high-level concepts in the
          content. For example, a research paper about deep learning might return the
          concept, "Artificial Intelligence" although the term is not mentioned.
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Spanish.
    :attr EmotionOptions emotion: (optional) Detects anger, disgust, fear, joy, or
          sadness that is conveyed in the content or by the context around target phrases
          specified in the targets parameter. You can analyze emotion for detected
          entities with `entities.emotion` and for keywords with `keywords.emotion`.
          Supported languages: English.
    :attr EntitiesOptions entities: (optional) Identifies people, cities,
          organizations, and other entities in the content. See [Entity types and
          subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-types).
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are supported
          only through custom models.
    :attr KeywordsOptions keywords: (optional) Returns important keywords in the
          content.
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Russian, Spanish, Swedish.
    :attr MetadataOptions metadata: (optional) Returns information from the
          document, including author name, title, RSS/ATOM feeds, prominent page image,
          and publication date. Supports URL and HTML input types only.
    :attr RelationsOptions relations: (optional) Recognizes when two entities are
          related and identifies the type of relation. For example, an `awardedTo`
          relation might connect the entities "Nobel Prize" and "Albert Einstein". See
          [Relation
          types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
          Supported languages: Arabic, English, German, Japanese, Korean, Spanish.
          Chinese, Dutch, French, Italian, and Portuguese custom models are also
          supported.
    :attr SemanticRolesOptions semantic_roles: (optional) Parses sentences into
          subject, action, and object form.
          Supported languages: English, German, Japanese, Korean, Spanish.
    :attr SentimentOptions sentiment: (optional) Analyzes the general sentiment of
          your content or the sentiment toward specific target phrases. You can analyze
          sentiment for detected entities with `entities.sentiment` and for keywords with
          `keywords.sentiment`.
           Supported languages: Arabic, English, French, German, Italian, Japanese,
          Korean, Portuguese, Russian, Spanish.
    :attr CategoriesOptions categories: (optional) Returns a five-level taxonomy of
          the content. The top three categories are returned.
          Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
          Portuguese, Spanish.
    :attr SyntaxOptions syntax: (optional) Returns tokens and sentences from the
          input text.
    """

    def __init__(self,
                 *,
                 concepts: 'ConceptsOptions' = None,
                 emotion: 'EmotionOptions' = None,
                 entities: 'EntitiesOptions' = None,
                 keywords: 'KeywordsOptions' = None,
                 metadata: 'MetadataOptions' = None,
                 relations: 'RelationsOptions' = None,
                 semantic_roles: 'SemanticRolesOptions' = None,
                 sentiment: 'SentimentOptions' = None,
                 categories: 'CategoriesOptions' = None,
                 syntax: 'SyntaxOptions' = None) -> None:
        """
        Initialize a Features object.

        :param ConceptsOptions concepts: (optional) Returns high-level concepts in
               the content. For example, a research paper about deep learning might return
               the concept, "Artificial Intelligence" although the term is not mentioned.
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Spanish.
        :param EmotionOptions emotion: (optional) Detects anger, disgust, fear,
               joy, or sadness that is conveyed in the content or by the context around
               target phrases specified in the targets parameter. You can analyze emotion
               for detected entities with `entities.emotion` and for keywords with
               `keywords.emotion`.
               Supported languages: English.
        :param EntitiesOptions entities: (optional) Identifies people, cities,
               organizations, and other entities in the content. See [Entity types and
               subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-types).
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are
               supported only through custom models.
        :param KeywordsOptions keywords: (optional) Returns important keywords in
               the content.
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Russian, Spanish, Swedish.
        :param MetadataOptions metadata: (optional) Returns information from the
               document, including author name, title, RSS/ATOM feeds, prominent page
               image, and publication date. Supports URL and HTML input types only.
        :param RelationsOptions relations: (optional) Recognizes when two entities
               are related and identifies the type of relation. For example, an
               `awardedTo` relation might connect the entities "Nobel Prize" and "Albert
               Einstein". See [Relation
               types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
               Supported languages: Arabic, English, German, Japanese, Korean, Spanish.
               Chinese, Dutch, French, Italian, and Portuguese custom models are also
               supported.
        :param SemanticRolesOptions semantic_roles: (optional) Parses sentences
               into subject, action, and object form.
               Supported languages: English, German, Japanese, Korean, Spanish.
        :param SentimentOptions sentiment: (optional) Analyzes the general
               sentiment of your content or the sentiment toward specific target phrases.
               You can analyze sentiment for detected entities with `entities.sentiment`
               and for keywords with `keywords.sentiment`.
                Supported languages: Arabic, English, French, German, Italian, Japanese,
               Korean, Portuguese, Russian, Spanish.
        :param CategoriesOptions categories: (optional) Returns a five-level
               taxonomy of the content. The top three categories are returned.
               Supported languages: Arabic, English, French, German, Italian, Japanese,
               Korean, Portuguese, Spanish.
        :param SyntaxOptions syntax: (optional) Returns tokens and sentences from
               the input text.
        """
        self.concepts = concepts
        self.emotion = emotion
        self.entities = entities
        self.keywords = keywords
        self.metadata = metadata
        self.relations = relations
        self.semantic_roles = semantic_roles
        self.sentiment = sentiment
        self.categories = categories
        self.syntax = syntax

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Features':
        """Initialize a Features object from a json dictionary."""
        args = {}
        valid_keys = [
            'concepts', 'emotion', 'entities', 'keywords', 'metadata',
            'relations', 'semantic_roles', 'sentiment', 'categories', 'syntax'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Features: '
                + ', '.join(bad_keys))
        if 'concepts' in _dict:
            args['concepts'] = ConceptsOptions._from_dict(_dict.get('concepts'))
        if 'emotion' in _dict:
            args['emotion'] = EmotionOptions._from_dict(_dict.get('emotion'))
        if 'entities' in _dict:
            args['entities'] = EntitiesOptions._from_dict(_dict.get('entities'))
        if 'keywords' in _dict:
            args['keywords'] = KeywordsOptions._from_dict(_dict.get('keywords'))
        if 'metadata' in _dict:
            args['metadata'] = MetadataOptions._from_dict(_dict.get('metadata'))
        if 'relations' in _dict:
            args['relations'] = RelationsOptions._from_dict(
                _dict.get('relations'))
        if 'semantic_roles' in _dict:
            args['semantic_roles'] = SemanticRolesOptions._from_dict(
                _dict.get('semantic_roles'))
        if 'sentiment' in _dict:
            args['sentiment'] = SentimentOptions._from_dict(
                _dict.get('sentiment'))
        if 'categories' in _dict:
            args['categories'] = CategoriesOptions._from_dict(
                _dict.get('categories'))
        if 'syntax' in _dict:
            args['syntax'] = SyntaxOptions._from_dict(_dict.get('syntax'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Features object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'concepts') and self.concepts is not None:
            _dict['concepts'] = self.concepts._to_dict()
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities._to_dict()
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords._to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata._to_dict()
        if hasattr(self, 'relations') and self.relations is not None:
            _dict['relations'] = self.relations._to_dict()
        if hasattr(self, 'semantic_roles') and self.semantic_roles is not None:
            _dict['semantic_roles'] = self.semantic_roles._to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment._to_dict()
        if hasattr(self, 'categories') and self.categories is not None:
            _dict['categories'] = self.categories._to_dict()
        if hasattr(self, 'syntax') and self.syntax is not None:
            _dict['syntax'] = self.syntax._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Features object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Features') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Features') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Feed():
    """
    RSS or ATOM feed found on the webpage.

    :attr str link: (optional) URL of the RSS or ATOM feed.
    """

    def __init__(self, *, link: str = None) -> None:
        """
        Initialize a Feed object.

        :param str link: (optional) URL of the RSS or ATOM feed.
        """
        self.link = link

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Feed':
        """Initialize a Feed object from a json dictionary."""
        args = {}
        valid_keys = ['link']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Feed: ' +
                ', '.join(bad_keys))
        if 'link' in _dict:
            args['link'] = _dict.get('link')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Feed object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'link') and self.link is not None:
            _dict['link'] = self.link
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Feed object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Feed') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Feed') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsOptions():
    """
    Returns important keywords in the content.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish.

    :attr int limit: (optional) Maximum number of keywords to return.
    :attr bool sentiment: (optional) Set this to `true` to return sentiment
          information for detected keywords.
    :attr bool emotion: (optional) Set this to `true` to analyze emotion for
          detected keywords.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 sentiment: bool = None,
                 emotion: bool = None) -> None:
        """
        Initialize a KeywordsOptions object.

        :param int limit: (optional) Maximum number of keywords to return.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
               information for detected keywords.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for
               detected keywords.
        """
        self.limit = limit
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeywordsOptions':
        """Initialize a KeywordsOptions object from a json dictionary."""
        args = {}
        valid_keys = ['limit', 'sentiment', 'emotion']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class KeywordsOptions: '
                + ', '.join(bad_keys))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeywordsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'KeywordsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeywordsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsResult():
    """
    The important keywords in the content, organized by relevance.

    :attr int count: (optional) Number of times the keyword appears in the analyzed
          text.
    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values
          indicate greater relevance.
    :attr str text: (optional) The keyword text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the
          keyword, enabled with the `emotion` option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results
          for the keyword, enabled with the `sentiment` option.
    """

    def __init__(self,
                 *,
                 count: int = None,
                 relevance: float = None,
                 text: str = None,
                 emotion: 'EmotionScores' = None,
                 sentiment: 'FeatureSentimentResults' = None) -> None:
        """
        Initialize a KeywordsResult object.

        :param int count: (optional) Number of times the keyword appears in the
               analyzed text.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher
               values indicate greater relevance.
        :param str text: (optional) The keyword text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the
               keyword, enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis
               results for the keyword, enabled with the `sentiment` option.
        """
        self.count = count
        self.relevance = relevance
        self.text = text
        self.emotion = emotion
        self.sentiment = sentiment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeywordsResult':
        """Initialize a KeywordsResult object from a json dictionary."""
        args = {}
        valid_keys = ['count', 'relevance', 'text', 'emotion', 'sentiment']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class KeywordsResult: '
                + ', '.join(bad_keys))
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        if 'sentiment' in _dict:
            args['sentiment'] = FeatureSentimentResults._from_dict(
                _dict.get('sentiment'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeywordsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'KeywordsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeywordsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListModelsResults():
    """
    Custom models that are available for entities and relations.

    :attr List[Model] models: (optional) An array of available models.
    """

    def __init__(self, *, models: List['Model'] = None) -> None:
        """
        Initialize a ListModelsResults object.

        :param List[Model] models: (optional) An array of available models.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListModelsResults':
        """Initialize a ListModelsResults object from a json dictionary."""
        args = {}
        valid_keys = ['models']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ListModelsResults: '
                + ', '.join(bad_keys))
        if 'models' in _dict:
            args['models'] = [
                Model._from_dict(x) for x in (_dict.get('models'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListModelsResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            _dict['models'] = [x._to_dict() for x in self.models]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListModelsResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ListModelsResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListModelsResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetadataOptions():
    """
    Returns information from the document, including author name, title, RSS/ATOM feeds,
    prominent page image, and publication date. Supports URL and HTML input types only.

    """

    def __init__(self) -> None:
        """
        Initialize a MetadataOptions object.

        """

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MetadataOptions':
        """Initialize a MetadataOptions object from a json dictionary."""
        args = {}
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetadataOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MetadataOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'MetadataOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MetadataOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Model():
    """
    Model.

    :attr str status: (optional) When the status is `available`, the model is ready
          to use.
    :attr str model_id: (optional) Unique model ID.
    :attr str language: (optional) ISO 639-1 code indicating the language of the
          model.
    :attr str description: (optional) Model description.
    :attr str workspace_id: (optional) ID of the Watson Knowledge Studio workspace
          that deployed this model to Natural Language Understanding.
    :attr str version: (optional) The model version, if it was manually provided in
          Watson Knowledge Studio.
    :attr str version_description: (optional) The description of the version, if it
          was manually provided in Watson Knowledge Studio.
    :attr datetime created: (optional) A dateTime indicating when the model was
          created.
    """

    def __init__(self,
                 *,
                 status: str = None,
                 model_id: str = None,
                 language: str = None,
                 description: str = None,
                 workspace_id: str = None,
                 version: str = None,
                 version_description: str = None,
                 created: datetime = None) -> None:
        """
        Initialize a Model object.

        :param str status: (optional) When the status is `available`, the model is
               ready to use.
        :param str model_id: (optional) Unique model ID.
        :param str language: (optional) ISO 639-1 code indicating the language of
               the model.
        :param str description: (optional) Model description.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version: (optional) The model version, if it was manually
               provided in Watson Knowledge Studio.
        :param str version_description: (optional) The description of the version,
               if it was manually provided in Watson Knowledge Studio.
        :param datetime created: (optional) A dateTime indicating when the model
               was created.
        """
        self.status = status
        self.model_id = model_id
        self.language = language
        self.description = description
        self.workspace_id = workspace_id
        self.version = version
        self.version_description = version_description
        self.created = created

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Model':
        """Initialize a Model object from a json dictionary."""
        args = {}
        valid_keys = [
            'status', 'model_id', 'language', 'description', 'workspace_id',
            'version', 'version_description', 'created'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Model: ' +
                ', '.join(bad_keys))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'model_id' in _dict:
            args['model_id'] = _dict.get('model_id')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        if 'version' in _dict:
            args['version'] = _dict.get('version')
        if 'version_description' in _dict:
            args['version_description'] = _dict.get('version_description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Model object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(
                self,
                'version_description') and self.version_description is not None:
            _dict['version_description'] = self.version_description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Model object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Model') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Model') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationArgument():
    """
    RelationArgument.

    :attr List[RelationEntity] entities: (optional) An array of extracted entities.
    :attr List[int] location: (optional) Character offsets indicating the beginning
          and end of the mention in the analyzed text.
    :attr str text: (optional) Text that corresponds to the argument.
    """

    def __init__(self,
                 *,
                 entities: List['RelationEntity'] = None,
                 location: List[int] = None,
                 text: str = None) -> None:
        """
        Initialize a RelationArgument object.

        :param List[RelationEntity] entities: (optional) An array of extracted
               entities.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the mention in the analyzed text.
        :param str text: (optional) Text that corresponds to the argument.
        """
        self.entities = entities
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationArgument':
        """Initialize a RelationArgument object from a json dictionary."""
        args = {}
        valid_keys = ['entities', 'location', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RelationArgument: '
                + ', '.join(bad_keys))
        if 'entities' in _dict:
            args['entities'] = [
                RelationEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationArgument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationArgument object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RelationArgument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationArgument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationEntity():
    """
    An entity that corresponds with an argument in a relation.

    :attr str text: (optional) Text that corresponds to the entity.
    :attr str type: (optional) Entity type.
    """

    def __init__(self, *, text: str = None, type: str = None) -> None:
        """
        Initialize a RelationEntity object.

        :param str text: (optional) Text that corresponds to the entity.
        :param str type: (optional) Entity type.
        """
        self.text = text
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationEntity':
        """Initialize a RelationEntity object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RelationEntity: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RelationEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsOptions():
    """
    Recognizes when two entities are related and identifies the type of relation. For
    example, an `awardedTo` relation might connect the entities "Nobel Prize" and "Albert
    Einstein". See [Relation
    types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
    Supported languages: Arabic, English, German, Japanese, Korean, Spanish. Chinese,
    Dutch, French, Italian, and Portuguese custom models are also supported.

    :attr str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the default model.
    """

    def __init__(self, *, model: str = None) -> None:
        """
        Initialize a RelationsOptions object.

        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the default model.
        """
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationsOptions':
        """Initialize a RelationsOptions object from a json dictionary."""
        args = {}
        valid_keys = ['model']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RelationsOptions: '
                + ', '.join(bad_keys))
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RelationsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsResult():
    """
    The relations between entities found in the content.

    :attr float score: (optional) Confidence score for the relation. Higher values
          indicate greater confidence.
    :attr str sentence: (optional) The sentence that contains the relation.
    :attr str type: (optional) The type of the relation.
    :attr List[RelationArgument] arguments: (optional) Entity mentions that are
          involved in the relation.
    """

    def __init__(self,
                 *,
                 score: float = None,
                 sentence: str = None,
                 type: str = None,
                 arguments: List['RelationArgument'] = None) -> None:
        """
        Initialize a RelationsResult object.

        :param float score: (optional) Confidence score for the relation. Higher
               values indicate greater confidence.
        :param str sentence: (optional) The sentence that contains the relation.
        :param str type: (optional) The type of the relation.
        :param List[RelationArgument] arguments: (optional) Entity mentions that
               are involved in the relation.
        """
        self.score = score
        self.sentence = sentence
        self.type = type
        self.arguments = arguments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationsResult':
        """Initialize a RelationsResult object from a json dictionary."""
        args = {}
        valid_keys = ['score', 'sentence', 'type', 'arguments']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RelationsResult: '
                + ', '.join(bad_keys))
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        if 'sentence' in _dict:
            args['sentence'] = _dict.get('sentence')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'arguments' in _dict:
            args['arguments'] = [
                RelationArgument._from_dict(x) for x in (_dict.get('arguments'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'sentence') and self.sentence is not None:
            _dict['sentence'] = self.sentence
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'arguments') and self.arguments is not None:
            _dict['arguments'] = [x._to_dict() for x in self.arguments]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'RelationsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesEntity():
    """
    SemanticRolesEntity.

    :attr str type: (optional) Entity type.
    :attr str text: (optional) The entity text.
    """

    def __init__(self, *, type: str = None, text: str = None) -> None:
        """
        Initialize a SemanticRolesEntity object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The entity text.
        """
        self.type = type
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesEntity':
        """Initialize a SemanticRolesEntity object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesEntity: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesKeyword():
    """
    SemanticRolesKeyword.

    :attr str text: (optional) The keyword text.
    """

    def __init__(self, *, text: str = None) -> None:
        """
        Initialize a SemanticRolesKeyword object.

        :param str text: (optional) The keyword text.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesKeyword':
        """Initialize a SemanticRolesKeyword object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesKeyword: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesKeyword object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesKeyword object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesKeyword') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesKeyword') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesOptions():
    """
    Parses sentences into subject, action, and object form.
    Supported languages: English, German, Japanese, Korean, Spanish.

    :attr int limit: (optional) Maximum number of semantic_roles results to return.
    :attr bool keywords: (optional) Set this to `true` to return keyword information
          for subjects and objects.
    :attr bool entities: (optional) Set this to `true` to return entity information
          for subjects and objects.
    """

    def __init__(self,
                 *,
                 limit: int = None,
                 keywords: bool = None,
                 entities: bool = None) -> None:
        """
        Initialize a SemanticRolesOptions object.

        :param int limit: (optional) Maximum number of semantic_roles results to
               return.
        :param bool keywords: (optional) Set this to `true` to return keyword
               information for subjects and objects.
        :param bool entities: (optional) Set this to `true` to return entity
               information for subjects and objects.
        """
        self.limit = limit
        self.keywords = keywords
        self.entities = entities

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesOptions':
        """Initialize a SemanticRolesOptions object from a json dictionary."""
        args = {}
        valid_keys = ['limit', 'keywords', 'entities']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesOptions: '
                + ', '.join(bad_keys))
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'keywords' in _dict:
            args['keywords'] = _dict.get('keywords')
        if 'entities' in _dict:
            args['entities'] = _dict.get('entities')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResult():
    """
    The object containing the actions and the objects the actions act upon.

    :attr str sentence: (optional) Sentence from the source that contains the
          subject, action, and object.
    :attr SemanticRolesResultSubject subject: (optional) The extracted subject from
          the sentence.
    :attr SemanticRolesResultAction action: (optional) The extracted action from the
          sentence.
    :attr SemanticRolesResultObject object: (optional) The extracted object from the
          sentence.
    """

    def __init__(self,
                 *,
                 sentence: str = None,
                 subject: 'SemanticRolesResultSubject' = None,
                 action: 'SemanticRolesResultAction' = None,
                 object: 'SemanticRolesResultObject' = None) -> None:
        """
        Initialize a SemanticRolesResult object.

        :param str sentence: (optional) Sentence from the source that contains the
               subject, action, and object.
        :param SemanticRolesResultSubject subject: (optional) The extracted subject
               from the sentence.
        :param SemanticRolesResultAction action: (optional) The extracted action
               from the sentence.
        :param SemanticRolesResultObject object: (optional) The extracted object
               from the sentence.
        """
        self.sentence = sentence
        self.subject = subject
        self.action = action
        self.object = object

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResult':
        """Initialize a SemanticRolesResult object from a json dictionary."""
        args = {}
        valid_keys = ['sentence', 'subject', 'action', 'object']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesResult: '
                + ', '.join(bad_keys))
        if 'sentence' in _dict:
            args['sentence'] = _dict.get('sentence')
        if 'subject' in _dict:
            args['subject'] = SemanticRolesResultSubject._from_dict(
                _dict.get('subject'))
        if 'action' in _dict:
            args['action'] = SemanticRolesResultAction._from_dict(
                _dict.get('action'))
        if 'object' in _dict:
            args['object'] = SemanticRolesResultObject._from_dict(
                _dict.get('object'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentence') and self.sentence is not None:
            _dict['sentence'] = self.sentence
        if hasattr(self, 'subject') and self.subject is not None:
            _dict['subject'] = self.subject._to_dict()
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action._to_dict()
        if hasattr(self, 'object') and self.object is not None:
            _dict['object'] = self.object._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultAction():
    """
    The extracted action from the sentence.

    :attr str text: (optional) Analyzed text that corresponds to the action.
    :attr str normalized: (optional) normalized version of the action.
    :attr SemanticRolesVerb verb: (optional)
    """

    def __init__(self,
                 *,
                 text: str = None,
                 normalized: str = None,
                 verb: 'SemanticRolesVerb' = None) -> None:
        """
        Initialize a SemanticRolesResultAction object.

        :param str text: (optional) Analyzed text that corresponds to the action.
        :param str normalized: (optional) normalized version of the action.
        :param SemanticRolesVerb verb: (optional)
        """
        self.text = text
        self.normalized = normalized
        self.verb = verb

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultAction':
        """Initialize a SemanticRolesResultAction object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'normalized', 'verb']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesResultAction: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'normalized' in _dict:
            args['normalized'] = _dict.get('normalized')
        if 'verb' in _dict:
            args['verb'] = SemanticRolesVerb._from_dict(_dict.get('verb'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'normalized') and self.normalized is not None:
            _dict['normalized'] = self.normalized
        if hasattr(self, 'verb') and self.verb is not None:
            _dict['verb'] = self.verb._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultAction object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultObject():
    """
    The extracted object from the sentence.

    :attr str text: (optional) Object text.
    :attr List[SemanticRolesKeyword] keywords: (optional) An array of extracted
          keywords.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 keywords: List['SemanticRolesKeyword'] = None) -> None:
        """
        Initialize a SemanticRolesResultObject object.

        :param str text: (optional) Object text.
        :param List[SemanticRolesKeyword] keywords: (optional) An array of
               extracted keywords.
        """
        self.text = text
        self.keywords = keywords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultObject':
        """Initialize a SemanticRolesResultObject object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'keywords']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesResultObject: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'keywords' in _dict:
            args['keywords'] = [
                SemanticRolesKeyword._from_dict(x)
                for x in (_dict.get('keywords'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = [x._to_dict() for x in self.keywords]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultObject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultSubject():
    """
    The extracted subject from the sentence.

    :attr str text: (optional) Text that corresponds to the subject role.
    :attr List[SemanticRolesEntity] entities: (optional) An array of extracted
          entities.
    :attr List[SemanticRolesKeyword] keywords: (optional) An array of extracted
          keywords.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 entities: List['SemanticRolesEntity'] = None,
                 keywords: List['SemanticRolesKeyword'] = None) -> None:
        """
        Initialize a SemanticRolesResultSubject object.

        :param str text: (optional) Text that corresponds to the subject role.
        :param List[SemanticRolesEntity] entities: (optional) An array of extracted
               entities.
        :param List[SemanticRolesKeyword] keywords: (optional) An array of
               extracted keywords.
        """
        self.text = text
        self.entities = entities
        self.keywords = keywords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultSubject':
        """Initialize a SemanticRolesResultSubject object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'entities', 'keywords']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesResultSubject: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'entities' in _dict:
            args['entities'] = [
                SemanticRolesEntity._from_dict(x)
                for x in (_dict.get('entities'))
            ]
        if 'keywords' in _dict:
            args['keywords'] = [
                SemanticRolesKeyword._from_dict(x)
                for x in (_dict.get('keywords'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultSubject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = [x._to_dict() for x in self.keywords]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultSubject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultSubject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultSubject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesVerb():
    """
    SemanticRolesVerb.

    :attr str text: (optional) The keyword text.
    :attr str tense: (optional) Verb tense.
    """

    def __init__(self, *, text: str = None, tense: str = None) -> None:
        """
        Initialize a SemanticRolesVerb object.

        :param str text: (optional) The keyword text.
        :param str tense: (optional) Verb tense.
        """
        self.text = text
        self.tense = tense

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesVerb':
        """Initialize a SemanticRolesVerb object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'tense']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SemanticRolesVerb: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'tense' in _dict:
            args['tense'] = _dict.get('tense')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesVerb object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tense') and self.tense is not None:
            _dict['tense'] = self.tense
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesVerb object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesVerb') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesVerb') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentenceResult():
    """
    SentenceResult.

    :attr str text: (optional) The sentence.
    :attr List[int] location: (optional) Character offsets indicating the beginning
          and end of the sentence in the analyzed text.
    """

    def __init__(self, *, text: str = None, location: List[int] = None) -> None:
        """
        Initialize a SentenceResult object.

        :param str text: (optional) The sentence.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the sentence in the analyzed text.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentenceResult':
        """Initialize a SentenceResult object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SentenceResult: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentenceResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentenceResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SentenceResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentenceResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentOptions():
    """
    Analyzes the general sentiment of your content or the sentiment toward specific target
    phrases. You can analyze sentiment for detected entities with `entities.sentiment` and
    for keywords with `keywords.sentiment`.
     Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Russian, Spanish.

    :attr bool document: (optional) Set this to `false` to hide document-level
          sentiment results.
    :attr List[str] targets: (optional) Sentiment results will be returned for each
          target string that is found in the document.
    """

    def __init__(self,
                 *,
                 document: bool = None,
                 targets: List[str] = None) -> None:
        """
        Initialize a SentimentOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
               sentiment results.
        :param List[str] targets: (optional) Sentiment results will be returned for
               each target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentimentOptions':
        """Initialize a SentimentOptions object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SentimentOptions: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentimentOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SentimentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentimentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentResult():
    """
    The sentiment of the content.

    :attr DocumentSentimentResults document: (optional) The document level
          sentiment.
    :attr List[TargetedSentimentResults] targets: (optional) The targeted sentiment
          to analyze.
    """

    def __init__(self,
                 *,
                 document: 'DocumentSentimentResults' = None,
                 targets: List['TargetedSentimentResults'] = None) -> None:
        """
        Initialize a SentimentResult object.

        :param DocumentSentimentResults document: (optional) The document level
               sentiment.
        :param List[TargetedSentimentResults] targets: (optional) The targeted
               sentiment to analyze.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentimentResult':
        """Initialize a SentimentResult object from a json dictionary."""
        args = {}
        valid_keys = ['document', 'targets']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SentimentResult: '
                + ', '.join(bad_keys))
        if 'document' in _dict:
            args['document'] = DocumentSentimentResults._from_dict(
                _dict.get('document'))
        if 'targets' in _dict:
            args['targets'] = [
                TargetedSentimentResults._from_dict(x)
                for x in (_dict.get('targets'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x._to_dict() for x in self.targets]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentimentResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SentimentResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentimentResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxOptions():
    """
    Returns tokens and sentences from the input text.

    :attr SyntaxOptionsTokens tokens: (optional) Tokenization options.
    :attr bool sentences: (optional) Set this to `true` to return sentence
          information.
    """

    def __init__(self,
                 *,
                 tokens: 'SyntaxOptionsTokens' = None,
                 sentences: bool = None) -> None:
        """
        Initialize a SyntaxOptions object.

        :param SyntaxOptionsTokens tokens: (optional) Tokenization options.
        :param bool sentences: (optional) Set this to `true` to return sentence
               information.
        """
        self.tokens = tokens
        self.sentences = sentences

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxOptions':
        """Initialize a SyntaxOptions object from a json dictionary."""
        args = {}
        valid_keys = ['tokens', 'sentences']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SyntaxOptions: '
                + ', '.join(bad_keys))
        if 'tokens' in _dict:
            args['tokens'] = SyntaxOptionsTokens._from_dict(_dict.get('tokens'))
        if 'sentences' in _dict:
            args['sentences'] = _dict.get('sentences')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tokens') and self.tokens is not None:
            _dict['tokens'] = self.tokens._to_dict()
        if hasattr(self, 'sentences') and self.sentences is not None:
            _dict['sentences'] = self.sentences
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxOptionsTokens():
    """
    Tokenization options.

    :attr bool lemma: (optional) Set this to `true` to return the lemma for each
          token.
    :attr bool part_of_speech: (optional) Set this to `true` to return the part of
          speech for each token.
    """

    def __init__(self,
                 *,
                 lemma: bool = None,
                 part_of_speech: bool = None) -> None:
        """
        Initialize a SyntaxOptionsTokens object.

        :param bool lemma: (optional) Set this to `true` to return the lemma for
               each token.
        :param bool part_of_speech: (optional) Set this to `true` to return the
               part of speech for each token.
        """
        self.lemma = lemma
        self.part_of_speech = part_of_speech

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxOptionsTokens':
        """Initialize a SyntaxOptionsTokens object from a json dictionary."""
        args = {}
        valid_keys = ['lemma', 'part_of_speech']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SyntaxOptionsTokens: '
                + ', '.join(bad_keys))
        if 'lemma' in _dict:
            args['lemma'] = _dict.get('lemma')
        if 'part_of_speech' in _dict:
            args['part_of_speech'] = _dict.get('part_of_speech')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxOptionsTokens object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'lemma') and self.lemma is not None:
            _dict['lemma'] = self.lemma
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxOptionsTokens object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxOptionsTokens') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxOptionsTokens') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxResult():
    """
    Tokens and sentences returned from syntax analysis.

    :attr List[TokenResult] tokens: (optional)
    :attr List[SentenceResult] sentences: (optional)
    """

    def __init__(self,
                 *,
                 tokens: List['TokenResult'] = None,
                 sentences: List['SentenceResult'] = None) -> None:
        """
        Initialize a SyntaxResult object.

        :param List[TokenResult] tokens: (optional)
        :param List[SentenceResult] sentences: (optional)
        """
        self.tokens = tokens
        self.sentences = sentences

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxResult':
        """Initialize a SyntaxResult object from a json dictionary."""
        args = {}
        valid_keys = ['tokens', 'sentences']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SyntaxResult: '
                + ', '.join(bad_keys))
        if 'tokens' in _dict:
            args['tokens'] = [
                TokenResult._from_dict(x) for x in (_dict.get('tokens'))
            ]
        if 'sentences' in _dict:
            args['sentences'] = [
                SentenceResult._from_dict(x) for x in (_dict.get('sentences'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tokens') and self.tokens is not None:
            _dict['tokens'] = [x._to_dict() for x in self.tokens]
        if hasattr(self, 'sentences') and self.sentences is not None:
            _dict['sentences'] = [x._to_dict() for x in self.sentences]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedEmotionResults():
    """
    Emotion results for a specified target.

    :attr str text: (optional) Targeted text.
    :attr EmotionScores emotion: (optional) The emotion results for the target.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 emotion: 'EmotionScores' = None) -> None:
        """
        Initialize a TargetedEmotionResults object.

        :param str text: (optional) Targeted text.
        :param EmotionScores emotion: (optional) The emotion results for the
               target.
        """
        self.text = text
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetedEmotionResults':
        """Initialize a TargetedEmotionResults object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'emotion']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TargetedEmotionResults: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedEmotionResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetedEmotionResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TargetedEmotionResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetedEmotionResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedSentimentResults():
    """
    TargetedSentimentResults.

    :attr str text: (optional) Targeted text.
    :attr float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(self, *, text: str = None, score: float = None) -> None:
        """
        Initialize a TargetedSentimentResults object.

        :param str text: (optional) Targeted text.
        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.text = text
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetedSentimentResults':
        """Initialize a TargetedSentimentResults object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'score']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TargetedSentimentResults: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetedSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TargetedSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetedSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TokenResult():
    """
    TokenResult.

    :attr str text: (optional) The token as it appears in the analyzed text.
    :attr str part_of_speech: (optional) The part of speech of the token. For
          descriptions of the values, see [Universal Dependencies POS
          tags](https://universaldependencies.org/u/pos/).
    :attr List[int] location: (optional) Character offsets indicating the beginning
          and end of the token in the analyzed text.
    :attr str lemma: (optional) The
          [lemma](https://wikipedia.org/wiki/Lemma_%28morphology%29) of the token.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 part_of_speech: str = None,
                 location: List[int] = None,
                 lemma: str = None) -> None:
        """
        Initialize a TokenResult object.

        :param str text: (optional) The token as it appears in the analyzed text.
        :param str part_of_speech: (optional) The part of speech of the token. For
               descriptions of the values, see [Universal Dependencies POS
               tags](https://universaldependencies.org/u/pos/).
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the token in the analyzed text.
        :param str lemma: (optional) The
               [lemma](https://wikipedia.org/wiki/Lemma_%28morphology%29) of the token.
        """
        self.text = text
        self.part_of_speech = part_of_speech
        self.location = location
        self.lemma = lemma

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenResult':
        """Initialize a TokenResult object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'part_of_speech', 'location', 'lemma']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TokenResult: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'part_of_speech' in _dict:
            args['part_of_speech'] = _dict.get('part_of_speech')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'lemma' in _dict:
            args['lemma'] = _dict.get('lemma')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'lemma') and self.lemma is not None:
            _dict['lemma'] = self.lemma
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TokenResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PartOfSpeechEnum(Enum):
        """
        The part of speech of the token. For descriptions of the values, see [Universal
        Dependencies POS tags](https://universaldependencies.org/u/pos/).
        """
        ADJ = "ADJ"
        ADP = "ADP"
        ADV = "ADV"
        AUX = "AUX"
        CCONJ = "CCONJ"
        DET = "DET"
        INTJ = "INTJ"
        NOUN = "NOUN"
        NUM = "NUM"
        PART = "PART"
        PRON = "PRON"
        PROPN = "PROPN"
        PUNCT = "PUNCT"
        SCONJ = "SCONJ"
        SYM = "SYM"
        VERB = "VERB"
        X = "X"
