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
Analyze various features of text content at scale. Provide text, raw HTML, or a public URL
and IBM Watson Natural Language Understanding will give you results for the features you
request. The service cleans HTML content before analysis by default, so the results can
ignore most advertisements and other unwanted content.
You can create [custom
models](/docs/services/natural-language-understanding/customizing.html) with Watson
Knowledge Studio to detect custom entities and relations in Natural Language
Understanding.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class NaturalLanguageUnderstandingV1(WatsonService):
    """The Natural Language Understanding V1 service."""

    default_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api'

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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/natural-language-understanding/api").
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
            vcap_services_name='natural-language-understanding',
            url=url,
            username=username,
            password=password,
            iam_apikey=iam_apikey,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # Analyze
    #########################

    def analyze(self,
                features,
                text=None,
                html=None,
                url=None,
                clean=None,
                xpath=None,
                fallback_to_raw=None,
                return_analyzed_text=None,
                language=None,
                limit_text_characters=None,
                **kwargs):
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
        - Sentiment.

        :param Features features: Analysis features and options.
        :param str text: The plain text to analyze. One of the `text`, `html`, or `url`
        parameters is required.
        :param str html: The HTML file to analyze. One of the `text`, `html`, or `url`
        parameters is required.
        :param str url: The webpage to analyze. One of the `text`, `html`, or `url`
        parameters is required.
        :param bool clean: Set this to `false` to disable webpage cleaning. To learn more
        about webpage cleaning, see the [Analyzing
        webpages](/docs/services/natural-language-understanding/analyzing-webpages.html)
        documentation.
        :param str xpath: An [XPath
        query](/docs/services/natural-language-understanding/analyzing-webpages.html#xpath)
        to perform on `html` or `url` input. Results of the query will be appended to the
        cleaned webpage text before it is analyzed. To analyze only the results of the
        XPath query, set the `clean` parameter to `false`.
        :param bool fallback_to_raw: Whether to use raw HTML content if text cleaning
        fails.
        :param bool return_analyzed_text: Whether or not to return the analyzed text.
        :param str language: ISO 639-1 code that specifies the language of your text. This
        overrides automatic language detection. Language support differs depending on the
        features you include in your analysis. See [Language
        support](https://www.bluemix.net/docs/services/natural-language-understanding/language-support.html)
        for more information.
        :param int limit_text_characters: Sets the maximum number of characters that are
        processed by the service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if features is None:
            raise ValueError('features must be provided')
        features = self._convert_model(features, Features)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

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
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            json=data,
            accept_json=True)
        return response

    #########################
    # Manage models
    #########################

    def delete_model(self, model_id, **kwargs):
        """
        Delete model.

        Deletes a custom model.

        :param str model_id: model_id of the model to delete.
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

        url = '/v1/models/{0}'.format(*self._encode_path_vars(model_id))
        response = self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_models(self, **kwargs):
        """
        List models.

        Lists Watson Knowledge Studio [custom
        models](/docs/services/natural-language-understanding/customizing.html) that are
        deployed to your Natural Language Understanding service.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        params = {'version': self.version}

        url = '/v1/models'
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


class AnalysisResults(object):
    """
    Results of the analysis, organized by feature.

    :attr str language: (optional) Language used to analyze the text.
    :attr str analyzed_text: (optional) Text that was used in the analysis.
    :attr str retrieved_url: (optional) URL of the webpage that was analyzed.
    :attr Usage usage: (optional) Usage information.
    :attr list[ConceptsResult] concepts: (optional) The general concepts referenced or
    alluded to in the analyzed text.
    :attr list[EntitiesResult] entities: (optional) The entities detected in the analyzed
    text.
    :attr list[KeywordsResult] keywords: (optional) The keywords from the analyzed text.
    :attr list[CategoriesResult] categories: (optional) The categories that the service
    assigned to the analyzed text.
    :attr EmotionResult emotion: (optional) The detected anger, disgust, fear, joy, or
    sadness that is conveyed by the content. Emotion information can be returned for
    detected entities, keywords, or user-specified target phrases found in the text.
    :attr MetadataResult metadata: (optional) The authors, publication date, title,
    prominent page image, and RSS/ATOM feeds of the webpage. Supports URL and HTML input
    types.
    :attr list[RelationsResult] relations: (optional) The relationships between entities
    in the content.
    :attr list[SemanticRolesResult] semantic_roles: (optional) Sentences parsed into
    `subject`, `action`, and `object` form.
    :attr SentimentResult sentiment: (optional) The sentiment of the content.
    """

    def __init__(self,
                 language=None,
                 analyzed_text=None,
                 retrieved_url=None,
                 usage=None,
                 concepts=None,
                 entities=None,
                 keywords=None,
                 categories=None,
                 emotion=None,
                 metadata=None,
                 relations=None,
                 semantic_roles=None,
                 sentiment=None):
        """
        Initialize a AnalysisResults object.

        :param str language: (optional) Language used to analyze the text.
        :param str analyzed_text: (optional) Text that was used in the analysis.
        :param str retrieved_url: (optional) URL of the webpage that was analyzed.
        :param Usage usage: (optional) Usage information.
        :param list[ConceptsResult] concepts: (optional) The general concepts referenced
        or alluded to in the analyzed text.
        :param list[EntitiesResult] entities: (optional) The entities detected in the
        analyzed text.
        :param list[KeywordsResult] keywords: (optional) The keywords from the analyzed
        text.
        :param list[CategoriesResult] categories: (optional) The categories that the
        service assigned to the analyzed text.
        :param EmotionResult emotion: (optional) The detected anger, disgust, fear, joy,
        or sadness that is conveyed by the content. Emotion information can be returned
        for detected entities, keywords, or user-specified target phrases found in the
        text.
        :param MetadataResult metadata: (optional) The authors, publication date, title,
        prominent page image, and RSS/ATOM feeds of the webpage. Supports URL and HTML
        input types.
        :param list[RelationsResult] relations: (optional) The relationships between
        entities in the content.
        :param list[SemanticRolesResult] semantic_roles: (optional) Sentences parsed into
        `subject`, `action`, and `object` form.
        :param SentimentResult sentiment: (optional) The sentiment of the content.
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResults object from a json dictionary."""
        args = {}
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        if 'analyzed_text' in _dict:
            args['analyzed_text'] = _dict.get('analyzed_text')
        if 'retrieved_url' in _dict:
            args['retrieved_url'] = _dict.get('retrieved_url')
        if 'usage' in _dict:
            args['usage'] = Usage._from_dict(_dict.get('usage'))
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
            args['metadata'] = MetadataResult._from_dict(_dict.get('metadata'))
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this AnalysisResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Author(object):
    """
    The author of the analyzed content.

    :attr str name: (optional) Name of the author.
    """

    def __init__(self, name=None):
        """
        Initialize a Author object.

        :param str name: (optional) Name of the author.
        """
        self.name = name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Author object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def __str__(self):
        """Return a `str` version of this Author object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesOptions(object):
    """
    Returns a five-level taxonomy of the content. The top three categories are returned.
    Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Spanish.

    :attr int limit: (optional) Maximum number of categories to return.
    Maximum value: **10**.
    """

    def __init__(self, limit=None):
        """
        Initialize a CategoriesOptions object.

        :param int limit: (optional) Maximum number of categories to return.
        Maximum value: **10**.
        """
        self.limit = limit

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesOptions object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def __str__(self):
        """Return a `str` version of this CategoriesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesResult(object):
    """
    A categorization of the analyzed text.

    :attr str label: (optional) The path to the category through the 5-level taxonomy
    hierarchy. For the complete list of categories, see the [Categories
    hierarchy](/docs/services/natural-language-understanding/categories.html#categories-hierarchy)
    documentation.
    :attr float score: (optional) Confidence score for the category classification. Higher
    values indicate greater confidence.
    """

    def __init__(self, label=None, score=None):
        """
        Initialize a CategoriesResult object.

        :param str label: (optional) The path to the category through the 5-level taxonomy
        hierarchy. For the complete list of categories, see the [Categories
        hierarchy](/docs/services/natural-language-understanding/categories.html#categories-hierarchy)
        documentation.
        :param float score: (optional) Confidence score for the category classification.
        Higher values indicate greater confidence.
        """
        self.label = label
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesResult object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this CategoriesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConceptsOptions(object):
    """
    Returns high-level concepts in the content. For example, a research paper about deep
    learning might return the concept, "Artificial Intelligence" although the term is not
    mentioned.
    Supported languages: English, French, German, Japanese, Korean, Portuguese, Spanish.

    :attr int limit: (optional) Maximum number of concepts to return.
    """

    def __init__(self, limit=None):
        """
        Initialize a ConceptsOptions object.

        :param int limit: (optional) Maximum number of concepts to return.
        """
        self.limit = limit

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsOptions object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def __str__(self):
        """Return a `str` version of this ConceptsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConceptsResult(object):
    """
    The general concepts referenced or alluded to in the analyzed text.

    :attr str text: (optional) Name of the concept.
    :attr float relevance: (optional) Relevance score between 0 and 1. Higher scores
    indicate greater relevance.
    :attr str dbpedia_resource: (optional) Link to the corresponding DBpedia resource.
    """

    def __init__(self, text=None, relevance=None, dbpedia_resource=None):
        """
        Initialize a ConceptsResult object.

        :param str text: (optional) Name of the concept.
        :param float relevance: (optional) Relevance score between 0 and 1. Higher scores
        indicate greater relevance.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
        resource.
        """
        self.text = text
        self.relevance = relevance
        self.dbpedia_resource = dbpedia_resource

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsResult object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
        if 'dbpedia_resource' in _dict:
            args['dbpedia_resource'] = _dict.get('dbpedia_resource')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this ConceptsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteModelResults(object):
    """
    Delete model results.

    :attr str deleted: (optional) model_id of the deleted model.
    """

    def __init__(self, deleted=None):
        """
        Initialize a DeleteModelResults object.

        :param str deleted: (optional) model_id of the deleted model.
        """
        self.deleted = deleted

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteModelResults object from a json dictionary."""
        args = {}
        if 'deleted' in _dict:
            args['deleted'] = _dict.get('deleted')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        return _dict

    def __str__(self):
        """Return a `str` version of this DeleteModelResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DisambiguationResult(object):
    """
    Disambiguation information for the entity.

    :attr str name: (optional) Common entity name.
    :attr str dbpedia_resource: (optional) Link to the corresponding DBpedia resource.
    :attr list[str] subtype: (optional) Entity subtype information.
    """

    def __init__(self, name=None, dbpedia_resource=None, subtype=None):
        """
        Initialize a DisambiguationResult object.

        :param str name: (optional) Common entity name.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
        resource.
        :param list[str] subtype: (optional) Entity subtype information.
        """
        self.name = name
        self.dbpedia_resource = dbpedia_resource
        self.subtype = subtype

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DisambiguationResult object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'dbpedia_resource' in _dict:
            args['dbpedia_resource'] = _dict.get('dbpedia_resource')
        if 'subtype' in _dict:
            args['subtype'] = _dict.get('subtype')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DisambiguationResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentEmotionResults(object):
    """
    Emotion results for the document as a whole.

    :attr EmotionScores emotion: (optional) Emotion results for the document as a whole.
    """

    def __init__(self, emotion=None):
        """
        Initialize a DocumentEmotionResults object.

        :param EmotionScores emotion: (optional) Emotion results for the document as a
        whole.
        """
        self.emotion = emotion

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentEmotionResults object from a json dictionary."""
        args = {}
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentEmotionResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentSentimentResults(object):
    """
    DocumentSentimentResults.

    :attr str label: (optional) Indicates whether the sentiment is positive, neutral, or
    negative.
    :attr float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
    """

    def __init__(self, label=None, score=None):
        """
        Initialize a DocumentSentimentResults object.

        :param str label: (optional) Indicates whether the sentiment is positive, neutral,
        or negative.
        :param float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
        """
        self.label = label
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentSentimentResults object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this DocumentSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionOptions(object):
    """
    Detects anger, disgust, fear, joy, or sadness that is conveyed in the content or by
    the context around target phrases specified in the targets parameter. You can analyze
    emotion for detected entities with `entities.emotion` and for keywords with
    `keywords.emotion`.
    Supported languages: English.

    :attr bool document: (optional) Set this to `false` to hide document-level emotion
    results.
    :attr list[str] targets: (optional) Emotion results will be returned for each target
    string that is found in the document.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a EmotionOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
        emotion results.
        :param list[str] targets: (optional) Emotion results will be returned for each
        target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionOptions object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def __str__(self):
        """Return a `str` version of this EmotionOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionResult(object):
    """
    The detected anger, disgust, fear, joy, or sadness that is conveyed by the content.
    Emotion information can be returned for detected entities, keywords, or user-specified
    target phrases found in the text.

    :attr DocumentEmotionResults document: (optional) Emotion results for the document as
    a whole.
    :attr list[TargetedEmotionResults] targets: (optional) Emotion results for specified
    targets.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a EmotionResult object.

        :param DocumentEmotionResults document: (optional) Emotion results for the
        document as a whole.
        :param list[TargetedEmotionResults] targets: (optional) Emotion results for
        specified targets.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionResult object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = DocumentEmotionResults._from_dict(
                _dict.get('document'))
        if 'targets' in _dict:
            args['targets'] = [
                TargetedEmotionResults._from_dict(x)
                for x in (_dict.get('targets'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x._to_dict() for x in self.targets]
        return _dict

    def __str__(self):
        """Return a `str` version of this EmotionResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionScores(object):
    """
    EmotionScores.

    :attr float anger: (optional) Anger score from 0 to 1. A higher score means that the
    text is more likely to convey anger.
    :attr float disgust: (optional) Disgust score from 0 to 1. A higher score means that
    the text is more likely to convey disgust.
    :attr float fear: (optional) Fear score from 0 to 1. A higher score means that the
    text is more likely to convey fear.
    :attr float joy: (optional) Joy score from 0 to 1. A higher score means that the text
    is more likely to convey joy.
    :attr float sadness: (optional) Sadness score from 0 to 1. A higher score means that
    the text is more likely to convey sadness.
    """

    def __init__(self,
                 anger=None,
                 disgust=None,
                 fear=None,
                 joy=None,
                 sadness=None):
        """
        Initialize a EmotionScores object.

        :param float anger: (optional) Anger score from 0 to 1. A higher score means that
        the text is more likely to convey anger.
        :param float disgust: (optional) Disgust score from 0 to 1. A higher score means
        that the text is more likely to convey disgust.
        :param float fear: (optional) Fear score from 0 to 1. A higher score means that
        the text is more likely to convey fear.
        :param float joy: (optional) Joy score from 0 to 1. A higher score means that the
        text is more likely to convey joy.
        :param float sadness: (optional) Sadness score from 0 to 1. A higher score means
        that the text is more likely to convey sadness.
        """
        self.anger = anger
        self.disgust = disgust
        self.fear = fear
        self.joy = joy
        self.sadness = sadness

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionScores object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this EmotionScores object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesOptions(object):
    """
    Identifies people, cities, organizations, and other entities in the content. See
    [Entity types and
    subtypes](/docs/services/natural-language-understanding/entity-types.html).
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish. Arabic, Chinese, and Dutch custom models are also
    supported.

    :attr int limit: (optional) Maximum number of entities to return.
    :attr bool mentions: (optional) Set this to `true` to return locations of entity
    mentions.
    :attr str model: (optional) Enter a [custom
    model](https://www.bluemix.net/docs/services/natural-language-understanding/customizing.html)
    ID to override the standard entity detection model.
    :attr bool sentiment: (optional) Set this to `true` to return sentiment information
    for detected entities.
    :attr bool emotion: (optional) Set this to `true` to analyze emotion for detected
    keywords.
    """

    def __init__(self,
                 limit=None,
                 mentions=None,
                 model=None,
                 sentiment=None,
                 emotion=None):
        """
        Initialize a EntitiesOptions object.

        :param int limit: (optional) Maximum number of entities to return.
        :param bool mentions: (optional) Set this to `true` to return locations of entity
        mentions.
        :param str model: (optional) Enter a [custom
        model](https://www.bluemix.net/docs/services/natural-language-understanding/customizing.html)
        ID to override the standard entity detection model.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
        information for detected entities.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for detected
        keywords.
        """
        self.limit = limit
        self.mentions = mentions
        self.model = model
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesOptions object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this EntitiesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesResult(object):
    """
    The important people, places, geopolitical entities and other types of entities in
    your content.

    :attr str type: (optional) Entity type.
    :attr str text: (optional) The name of the entity.
    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values indicate
    greater relevance.
    :attr list[EntityMention] mentions: (optional) Entity mentions and locations.
    :attr int count: (optional) How many times the entity was mentioned in the text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the entity,
    enabled with the `emotion` option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the
    entity, enabled with the `sentiment` option.
    :attr DisambiguationResult disambiguation: (optional) Disambiguation information for
    the entity.
    """

    def __init__(self,
                 type=None,
                 text=None,
                 relevance=None,
                 mentions=None,
                 count=None,
                 emotion=None,
                 sentiment=None,
                 disambiguation=None):
        """
        Initialize a EntitiesResult object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The name of the entity.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher values
        indicate greater relevance.
        :param list[EntityMention] mentions: (optional) Entity mentions and locations.
        :param int count: (optional) How many times the entity was mentioned in the text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the entity,
        enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results
        for the entity, enabled with the `sentiment` option.
        :param DisambiguationResult disambiguation: (optional) Disambiguation information
        for the entity.
        """
        self.type = type
        self.text = text
        self.relevance = relevance
        self.mentions = mentions
        self.count = count
        self.emotion = emotion
        self.sentiment = sentiment
        self.disambiguation = disambiguation

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesResult object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'relevance' in _dict:
            args['relevance'] = _dict.get('relevance')
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
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

    def __str__(self):
        """Return a `str` version of this EntitiesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMention(object):
    """
    EntityMention.

    :attr str text: (optional) Entity mention text.
    :attr list[int] location: (optional) Character offsets indicating the beginning and
    end of the mention in the analyzed text.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a EntityMention object.

        :param str text: (optional) Entity mention text.
        :param list[int] location: (optional) Character offsets indicating the beginning
        and end of the mention in the analyzed text.
        """
        self.text = text
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMention object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def __str__(self):
        """Return a `str` version of this EntityMention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeatureSentimentResults(object):
    """
    FeatureSentimentResults.

    :attr float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
    """

    def __init__(self, score=None):
        """
        Initialize a FeatureSentimentResults object.

        :param float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
        """
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeatureSentimentResults object from a json dictionary."""
        args = {}
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this FeatureSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Features(object):
    """
    Analysis features and options.

    :attr ConceptsOptions concepts: (optional) Returns high-level concepts in the content.
    For example, a research paper about deep learning might return the concept,
    "Artificial Intelligence" although the term is not mentioned.
    Supported languages: English, French, German, Japanese, Korean, Portuguese, Spanish.
    :attr EmotionOptions emotion: (optional) Detects anger, disgust, fear, joy, or sadness
    that is conveyed in the content or by the context around target phrases specified in
    the targets parameter. You can analyze emotion for detected entities with
    `entities.emotion` and for keywords with `keywords.emotion`.
    Supported languages: English.
    :attr EntitiesOptions entities: (optional) Identifies people, cities, organizations,
    and other entities in the content. See [Entity types and
    subtypes](/docs/services/natural-language-understanding/entity-types.html).
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish. Arabic, Chinese, and Dutch custom models are also
    supported.
    :attr KeywordsOptions keywords: (optional) Returns important keywords in the content.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish.
    :attr MetadataOptions metadata: (optional) Returns information from the document,
    including author name, title, RSS/ATOM feeds, prominent page image, and publication
    date. Supports URL and HTML input types only.
    :attr RelationsOptions relations: (optional) Recognizes when two entities are related
    and identifies the type of relation. For example, an `awardedTo` relation might
    connect the entities "Nobel Prize" and "Albert Einstein". See [Relation
    types](/docs/services/natural-language-understanding/relations.html).
    Supported languages: Arabic, English, German, Japanese, Korean, Spanish. Chinese,
    Dutch, French, Italian, and Portuguese custom models are also supported.
    :attr SemanticRolesOptions semantic_roles: (optional) Parses sentences into subject,
    action, and object form.
    Supported languages: English, German, Japanese, Korean, Spanish.
    :attr SentimentOptions sentiment: (optional) Analyzes the general sentiment of your
    content or the sentiment toward specific target phrases. You can analyze sentiment for
    detected entities with `entities.sentiment` and for keywords with
    `keywords.sentiment`.
     Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Russian, Spanish.
    :attr CategoriesOptions categories: (optional) Returns a five-level taxonomy of the
    content. The top three categories are returned.
    Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Spanish.
    """

    def __init__(self,
                 concepts=None,
                 emotion=None,
                 entities=None,
                 keywords=None,
                 metadata=None,
                 relations=None,
                 semantic_roles=None,
                 sentiment=None,
                 categories=None):
        """
        Initialize a Features object.

        :param ConceptsOptions concepts: (optional) Returns high-level concepts in the
        content. For example, a research paper about deep learning might return the
        concept, "Artificial Intelligence" although the term is not mentioned.
        Supported languages: English, French, German, Japanese, Korean, Portuguese,
        Spanish.
        :param EmotionOptions emotion: (optional) Detects anger, disgust, fear, joy, or
        sadness that is conveyed in the content or by the context around target phrases
        specified in the targets parameter. You can analyze emotion for detected entities
        with `entities.emotion` and for keywords with `keywords.emotion`.
        Supported languages: English.
        :param EntitiesOptions entities: (optional) Identifies people, cities,
        organizations, and other entities in the content. See [Entity types and
        subtypes](/docs/services/natural-language-understanding/entity-types.html).
        Supported languages: English, French, German, Italian, Japanese, Korean,
        Portuguese, Russian, Spanish, Swedish. Arabic, Chinese, and Dutch custom models
        are also supported.
        :param KeywordsOptions keywords: (optional) Returns important keywords in the
        content.
        Supported languages: English, French, German, Italian, Japanese, Korean,
        Portuguese, Russian, Spanish, Swedish.
        :param MetadataOptions metadata: (optional) Returns information from the document,
        including author name, title, RSS/ATOM feeds, prominent page image, and
        publication date. Supports URL and HTML input types only.
        :param RelationsOptions relations: (optional) Recognizes when two entities are
        related and identifies the type of relation. For example, an `awardedTo` relation
        might connect the entities "Nobel Prize" and "Albert Einstein". See [Relation
        types](/docs/services/natural-language-understanding/relations.html).
        Supported languages: Arabic, English, German, Japanese, Korean, Spanish. Chinese,
        Dutch, French, Italian, and Portuguese custom models are also supported.
        :param SemanticRolesOptions semantic_roles: (optional) Parses sentences into
        subject, action, and object form.
        Supported languages: English, German, Japanese, Korean, Spanish.
        :param SentimentOptions sentiment: (optional) Analyzes the general sentiment of
        your content or the sentiment toward specific target phrases. You can analyze
        sentiment for detected entities with `entities.sentiment` and for keywords with
        `keywords.sentiment`.
         Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
        Portuguese, Russian, Spanish.
        :param CategoriesOptions categories: (optional) Returns a five-level taxonomy of
        the content. The top three categories are returned.
        Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
        Portuguese, Spanish.
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Features object from a json dictionary."""
        args = {}
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
        return cls(**args)

    def _to_dict(self):
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
        return _dict

    def __str__(self):
        """Return a `str` version of this Features object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Feed(object):
    """
    RSS or ATOM feed found on the webpage.

    :attr str link: (optional) URL of the RSS or ATOM feed.
    """

    def __init__(self, link=None):
        """
        Initialize a Feed object.

        :param str link: (optional) URL of the RSS or ATOM feed.
        """
        self.link = link

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Feed object from a json dictionary."""
        args = {}
        if 'link' in _dict:
            args['link'] = _dict.get('link')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'link') and self.link is not None:
            _dict['link'] = self.link
        return _dict

    def __str__(self):
        """Return a `str` version of this Feed object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsOptions(object):
    """
    Returns important keywords in the content.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish.

    :attr int limit: (optional) Maximum number of keywords to return.
    :attr bool sentiment: (optional) Set this to `true` to return sentiment information
    for detected keywords.
    :attr bool emotion: (optional) Set this to `true` to analyze emotion for detected
    keywords.
    """

    def __init__(self, limit=None, sentiment=None, emotion=None):
        """
        Initialize a KeywordsOptions object.

        :param int limit: (optional) Maximum number of keywords to return.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
        information for detected keywords.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for detected
        keywords.
        """
        self.limit = limit
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsOptions object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'sentiment' in _dict:
            args['sentiment'] = _dict.get('sentiment')
        if 'emotion' in _dict:
            args['emotion'] = _dict.get('emotion')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        return _dict

    def __str__(self):
        """Return a `str` version of this KeywordsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsResult(object):
    """
    The important keywords in the content, organized by relevance.

    :attr int count: (optional) Number of times the keyword appears in the analyzed text.
    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values indicate
    greater relevance.
    :attr str text: (optional) The keyword text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the keyword,
    enabled with the `emotion` option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the
    keyword, enabled with the `sentiment` option.
    """

    def __init__(self,
                 count=None,
                 relevance=None,
                 text=None,
                 emotion=None,
                 sentiment=None):
        """
        Initialize a KeywordsResult object.

        :param int count: (optional) Number of times the keyword appears in the analyzed
        text.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher values
        indicate greater relevance.
        :param str text: (optional) The keyword text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the keyword,
        enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results
        for the keyword, enabled with the `sentiment` option.
        """
        self.count = count
        self.relevance = relevance
        self.text = text
        self.emotion = emotion
        self.sentiment = sentiment

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsResult object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this KeywordsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListModelsResults(object):
    """
    Models available for Relations and Entities features.

    :attr list[Model] models: (optional) An array of available models.
    """

    def __init__(self, models=None):
        """
        Initialize a ListModelsResults object.

        :param list[Model] models: (optional) An array of available models.
        """
        self.models = models

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListModelsResults object from a json dictionary."""
        args = {}
        if 'models' in _dict:
            args['models'] = [
                Model._from_dict(x) for x in (_dict.get('models'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            _dict['models'] = [x._to_dict() for x in self.models]
        return _dict

    def __str__(self):
        """Return a `str` version of this ListModelsResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetadataOptions(object):
    """
    Returns information from the document, including author name, title, RSS/ATOM feeds,
    prominent page image, and publication date. Supports URL and HTML input types only.

    """

    def __init__(self, **kwargs):
        """
        Initialize a MetadataOptions object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetadataOptions object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {}
        if not hasattr(self, '_additionalProperties'):
            super(MetadataOptions, self).__setattr__('_additionalProperties',
                                                     set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(MetadataOptions, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this MetadataOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MetadataResult(object):
    """
    The authors, publication date, title, prominent page image, and RSS/ATOM feeds of the
    webpage. Supports URL and HTML input types.

    :attr list[Author] authors: (optional) The authors of the document.
    :attr str publication_date: (optional) The publication date in the format ISO 8601.
    :attr str title: (optional) The title of the document.
    :attr str image: (optional) URL of a prominent image on the webpage.
    :attr list[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
    """

    def __init__(self,
                 authors=None,
                 publication_date=None,
                 title=None,
                 image=None,
                 feeds=None):
        """
        Initialize a MetadataResult object.

        :param list[Author] authors: (optional) The authors of the document.
        :param str publication_date: (optional) The publication date in the format ISO
        8601.
        :param str title: (optional) The title of the document.
        :param str image: (optional) URL of a prominent image on the webpage.
        :param list[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
        """
        self.authors = authors
        self.publication_date = publication_date
        self.title = title
        self.image = image
        self.feeds = feeds

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MetadataResult object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this MetadataResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Model(object):
    """
    Model.

    :attr str status: (optional) When the status is `available`, the model is ready to
    use.
    :attr str model_id: (optional) Unique model ID.
    :attr str language: (optional) ISO 639-1 code indicating the language of the model.
    :attr str description: (optional) Model description.
    :attr str workspace_id: (optional) ID of the Watson Knowledge Studio workspace that
    deployed this model to Natural Language Understanding.
    :attr str version: (optional) The model version, if it was manually provided in Watson
    Knowledge Studio.
    :attr str version_description: (optional) The description of the version, if it was
    manually provided in Watson Knowledge Studio.
    :attr datetime created: (optional) A dateTime indicating when the model was created.
    """

    def __init__(self,
                 status=None,
                 model_id=None,
                 language=None,
                 description=None,
                 workspace_id=None,
                 version=None,
                 version_description=None,
                 created=None):
        """
        Initialize a Model object.

        :param str status: (optional) When the status is `available`, the model is ready
        to use.
        :param str model_id: (optional) Unique model ID.
        :param str language: (optional) ISO 639-1 code indicating the language of the
        model.
        :param str description: (optional) Model description.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio workspace
        that deployed this model to Natural Language Understanding.
        :param str version: (optional) The model version, if it was manually provided in
        Watson Knowledge Studio.
        :param str version_description: (optional) The description of the version, if it
        was manually provided in Watson Knowledge Studio.
        :param datetime created: (optional) A dateTime indicating when the model was
        created.
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
    def _from_dict(cls, _dict):
        """Initialize a Model object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Model object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationArgument(object):
    """
    RelationArgument.

    :attr list[RelationEntity] entities: (optional) An array of extracted entities.
    :attr list[int] location: (optional) Character offsets indicating the beginning and
    end of the mention in the analyzed text.
    :attr str text: (optional) Text that corresponds to the argument.
    """

    def __init__(self, entities=None, location=None, text=None):
        """
        Initialize a RelationArgument object.

        :param list[RelationEntity] entities: (optional) An array of extracted entities.
        :param list[int] location: (optional) Character offsets indicating the beginning
        and end of the mention in the analyzed text.
        :param str text: (optional) Text that corresponds to the argument.
        """
        self.entities = entities
        self.location = location
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationArgument object from a json dictionary."""
        args = {}
        if 'entities' in _dict:
            args['entities'] = [
                RelationEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this RelationArgument object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationEntity(object):
    """
    An entity that corresponds with an argument in a relation.

    :attr str text: (optional) Text that corresponds to the entity.
    :attr str type: (optional) Entity type.
    """

    def __init__(self, text=None, type=None):
        """
        Initialize a RelationEntity object.

        :param str text: (optional) Text that corresponds to the entity.
        :param str type: (optional) Entity type.
        """
        self.text = text
        self.type = type

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationEntity object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def __str__(self):
        """Return a `str` version of this RelationEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsOptions(object):
    """
    Recognizes when two entities are related and identifies the type of relation. For
    example, an `awardedTo` relation might connect the entities "Nobel Prize" and "Albert
    Einstein". See [Relation
    types](/docs/services/natural-language-understanding/relations.html).
    Supported languages: Arabic, English, German, Japanese, Korean, Spanish. Chinese,
    Dutch, French, Italian, and Portuguese custom models are also supported.

    :attr str model: (optional) Enter a [custom
    model](/docs/services/natural-language-understanding/customizing.html) ID to override
    the default model.
    """

    def __init__(self, model=None):
        """
        Initialize a RelationsOptions object.

        :param str model: (optional) Enter a [custom
        model](/docs/services/natural-language-understanding/customizing.html) ID to
        override the default model.
        """
        self.model = model

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsOptions object from a json dictionary."""
        args = {}
        if 'model' in _dict:
            args['model'] = _dict.get('model')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def __str__(self):
        """Return a `str` version of this RelationsOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsResult(object):
    """
    The relations between entities found in the content.

    :attr float score: (optional) Confidence score for the relation. Higher values
    indicate greater confidence.
    :attr str sentence: (optional) The sentence that contains the relation.
    :attr str type: (optional) The type of the relation.
    :attr list[RelationArgument] arguments: (optional) Entity mentions that are involved
    in the relation.
    """

    def __init__(self, score=None, sentence=None, type=None, arguments=None):
        """
        Initialize a RelationsResult object.

        :param float score: (optional) Confidence score for the relation. Higher values
        indicate greater confidence.
        :param str sentence: (optional) The sentence that contains the relation.
        :param str type: (optional) The type of the relation.
        :param list[RelationArgument] arguments: (optional) Entity mentions that are
        involved in the relation.
        """
        self.score = score
        self.sentence = sentence
        self.type = type
        self.arguments = arguments

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsResult object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this RelationsResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesAction(object):
    """
    SemanticRolesAction.

    :attr str text: (optional) Analyzed text that corresponds to the action.
    :attr str normalized: (optional) normalized version of the action.
    :attr SemanticRolesVerb verb: (optional)
    """

    def __init__(self, text=None, normalized=None, verb=None):
        """
        Initialize a SemanticRolesAction object.

        :param str text: (optional) Analyzed text that corresponds to the action.
        :param str normalized: (optional) normalized version of the action.
        :param SemanticRolesVerb verb: (optional)
        """
        self.text = text
        self.normalized = normalized
        self.verb = verb

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesAction object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'normalized' in _dict:
            args['normalized'] = _dict.get('normalized')
        if 'verb' in _dict:
            args['verb'] = SemanticRolesVerb._from_dict(_dict.get('verb'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'normalized') and self.normalized is not None:
            _dict['normalized'] = self.normalized
        if hasattr(self, 'verb') and self.verb is not None:
            _dict['verb'] = self.verb._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesAction object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesEntity(object):
    """
    SemanticRolesEntity.

    :attr str type: (optional) Entity type.
    :attr str text: (optional) The entity text.
    """

    def __init__(self, type=None, text=None):
        """
        Initialize a SemanticRolesEntity object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The entity text.
        """
        self.type = type
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesEntity object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesKeyword(object):
    """
    SemanticRolesKeyword.

    :attr str text: (optional) The keyword text.
    """

    def __init__(self, text=None):
        """
        Initialize a SemanticRolesKeyword object.

        :param str text: (optional) The keyword text.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesKeyword object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesKeyword object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesObject(object):
    """
    SemanticRolesObject.

    :attr str text: (optional) Object text.
    :attr list[SemanticRolesKeyword] keywords: (optional) An array of extracted keywords.
    """

    def __init__(self, text=None, keywords=None):
        """
        Initialize a SemanticRolesObject object.

        :param str text: (optional) Object text.
        :param list[SemanticRolesKeyword] keywords: (optional) An array of extracted
        keywords.
        """
        self.text = text
        self.keywords = keywords

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesObject object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'keywords' in _dict:
            args['keywords'] = [
                SemanticRolesKeyword._from_dict(x)
                for x in (_dict.get('keywords'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = [x._to_dict() for x in self.keywords]
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesObject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesOptions(object):
    """
    Parses sentences into subject, action, and object form.
    Supported languages: English, German, Japanese, Korean, Spanish.

    :attr int limit: (optional) Maximum number of semantic_roles results to return.
    :attr bool keywords: (optional) Set this to `true` to return keyword information for
    subjects and objects.
    :attr bool entities: (optional) Set this to `true` to return entity information for
    subjects and objects.
    """

    def __init__(self, limit=None, keywords=None, entities=None):
        """
        Initialize a SemanticRolesOptions object.

        :param int limit: (optional) Maximum number of semantic_roles results to return.
        :param bool keywords: (optional) Set this to `true` to return keyword information
        for subjects and objects.
        :param bool entities: (optional) Set this to `true` to return entity information
        for subjects and objects.
        """
        self.limit = limit
        self.keywords = keywords
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesOptions object from a json dictionary."""
        args = {}
        if 'limit' in _dict:
            args['limit'] = _dict.get('limit')
        if 'keywords' in _dict:
            args['keywords'] = _dict.get('keywords')
        if 'entities' in _dict:
            args['entities'] = _dict.get('entities')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResult(object):
    """
    The object containing the actions and the objects the actions act upon.

    :attr str sentence: (optional) Sentence from the source that contains the subject,
    action, and object.
    :attr SemanticRolesSubject subject: (optional) The extracted subject from the
    sentence.
    :attr SemanticRolesAction action: (optional) The extracted action from the sentence.
    :attr SemanticRolesObject object: (optional) The extracted object from the sentence.
    """

    def __init__(self, sentence=None, subject=None, action=None, object=None):
        """
        Initialize a SemanticRolesResult object.

        :param str sentence: (optional) Sentence from the source that contains the
        subject, action, and object.
        :param SemanticRolesSubject subject: (optional) The extracted subject from the
        sentence.
        :param SemanticRolesAction action: (optional) The extracted action from the
        sentence.
        :param SemanticRolesObject object: (optional) The extracted object from the
        sentence.
        """
        self.sentence = sentence
        self.subject = subject
        self.action = action
        self.object = object

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResult object from a json dictionary."""
        args = {}
        if 'sentence' in _dict:
            args['sentence'] = _dict.get('sentence')
        if 'subject' in _dict:
            args['subject'] = SemanticRolesSubject._from_dict(
                _dict.get('subject'))
        if 'action' in _dict:
            args['action'] = SemanticRolesAction._from_dict(_dict.get('action'))
        if 'object' in _dict:
            args['object'] = SemanticRolesObject._from_dict(_dict.get('object'))
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this SemanticRolesResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesSubject(object):
    """
    SemanticRolesSubject.

    :attr str text: (optional) Text that corresponds to the subject role.
    :attr list[SemanticRolesEntity] entities: (optional) An array of extracted entities.
    :attr list[SemanticRolesKeyword] keywords: (optional) An array of extracted keywords.
    """

    def __init__(self, text=None, entities=None, keywords=None):
        """
        Initialize a SemanticRolesSubject object.

        :param str text: (optional) Text that corresponds to the subject role.
        :param list[SemanticRolesEntity] entities: (optional) An array of extracted
        entities.
        :param list[SemanticRolesKeyword] keywords: (optional) An array of extracted
        keywords.
        """
        self.text = text
        self.entities = entities
        self.keywords = keywords

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesSubject object from a json dictionary."""
        args = {}
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = [x._to_dict() for x in self.keywords]
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesSubject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesVerb(object):
    """
    SemanticRolesVerb.

    :attr str text: (optional) The keyword text.
    :attr str tense: (optional) Verb tense.
    """

    def __init__(self, text=None, tense=None):
        """
        Initialize a SemanticRolesVerb object.

        :param str text: (optional) The keyword text.
        :param str tense: (optional) Verb tense.
        """
        self.text = text
        self.tense = tense

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesVerb object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'tense' in _dict:
            args['tense'] = _dict.get('tense')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tense') and self.tense is not None:
            _dict['tense'] = self.tense
        return _dict

    def __str__(self):
        """Return a `str` version of this SemanticRolesVerb object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentOptions(object):
    """
    Analyzes the general sentiment of your content or the sentiment toward specific target
    phrases. You can analyze sentiment for detected entities with `entities.sentiment` and
    for keywords with `keywords.sentiment`.
     Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Russian, Spanish.

    :attr bool document: (optional) Set this to `false` to hide document-level sentiment
    results.
    :attr list[str] targets: (optional) Sentiment results will be returned for each target
    string that is found in the document.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a SentimentOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
        sentiment results.
        :param list[str] targets: (optional) Sentiment results will be returned for each
        target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentOptions object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = _dict.get('document')
        if 'targets' in _dict:
            args['targets'] = _dict.get('targets')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def __str__(self):
        """Return a `str` version of this SentimentOptions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentResult(object):
    """
    The sentiment of the content.

    :attr DocumentSentimentResults document: (optional) The document level sentiment.
    :attr list[TargetedSentimentResults] targets: (optional) The targeted sentiment to
    analyze.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a SentimentResult object.

        :param DocumentSentimentResults document: (optional) The document level sentiment.
        :param list[TargetedSentimentResults] targets: (optional) The targeted sentiment
        to analyze.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentResult object from a json dictionary."""
        args = {}
        if 'document' in _dict:
            args['document'] = DocumentSentimentResults._from_dict(
                _dict.get('document'))
        if 'targets' in _dict:
            args['targets'] = [
                TargetedSentimentResults._from_dict(x)
                for x in (_dict.get('targets'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document._to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = [x._to_dict() for x in self.targets]
        return _dict

    def __str__(self):
        """Return a `str` version of this SentimentResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedEmotionResults(object):
    """
    Emotion results for a specified target.

    :attr str text: (optional) Targeted text.
    :attr EmotionScores emotion: (optional) The emotion results for the target.
    """

    def __init__(self, text=None, emotion=None):
        """
        Initialize a TargetedEmotionResults object.

        :param str text: (optional) Targeted text.
        :param EmotionScores emotion: (optional) The emotion results for the target.
        """
        self.text = text
        self.emotion = emotion

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedEmotionResults object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'emotion' in _dict:
            args['emotion'] = EmotionScores._from_dict(_dict.get('emotion'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this TargetedEmotionResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedSentimentResults(object):
    """
    TargetedSentimentResults.

    :attr str text: (optional) Targeted text.
    :attr float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
    """

    def __init__(self, text=None, score=None):
        """
        Initialize a TargetedSentimentResults object.

        :param str text: (optional) Targeted text.
        :param float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
        """
        self.text = text
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedSentimentResults object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this TargetedSentimentResults object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Usage(object):
    """
    Usage information.

    :attr int features: (optional) Number of features used in the API call.
    :attr int text_characters: (optional) Number of text characters processed.
    :attr int text_units: (optional) Number of 10,000-character units processed.
    """

    def __init__(self, features=None, text_characters=None, text_units=None):
        """
        Initialize a Usage object.

        :param int features: (optional) Number of features used in the API call.
        :param int text_characters: (optional) Number of text characters processed.
        :param int text_units: (optional) Number of 10,000-character units processed.
        """
        self.features = features
        self.text_characters = text_characters
        self.text_units = text_units

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Usage object from a json dictionary."""
        args = {}
        if 'features' in _dict:
            args['features'] = _dict.get('features')
        if 'text_characters' in _dict:
            args['text_characters'] = _dict.get('text_characters')
        if 'text_units' in _dict:
            args['text_units'] = _dict.get('text_units')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Usage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
