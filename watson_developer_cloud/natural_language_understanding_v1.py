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
Analyze various features of text content at scale. Provide text, raw HTML, or a public
URL, and IBM Watson Natural Language Understanding will give you results for the features
you request. The service cleans HTML content before analysis by default, so the results
can ignore most advertisements and other unwanted content.

### Concepts
Identify general concepts that are referenced or alluded to in your content. Concepts that
are detected typically have an associated link to a DBpedia resource.

### Entities
Detect important people, places, geopolitical entities and other types of entities in your
content. Entity detection recognizes consecutive coreferences of each entity. For example,
analysis of the following text would count "Barack Obama" and "He" as the same entity:

"Barack Obama was the 44th President of the United States. He took office in January
2009."

### Keywords
Determine the most important keywords in your content. Keyword phrases are organized by
relevance in the results.

### Categories
Categorize your content into a hierarchical 5-level taxonomy. For example, "Leonardo
DiCaprio won an Oscar" returns "/art and entertainment/movies and tv/movies" as the most
confident classification.

### Sentiment
Determine whether your content conveys postive or negative sentiment. Sentiment
information can be returned for detected entities, keywords, or user-specified target
phrases found in the text.

### Emotion
Detect anger, disgust, fear, joy, or sadness that is conveyed by your content. Emotion
information can be returned for detected entities, keywords, or user-specified target
phrases found in the text.

### Relations
Recognize when two entities are related, and identify the type of relation.  For example,
you can identify an "awardedTo" relation between an award and its recipient.

### Semantic Roles
Parse sentences into subject-action-object form, and identify entities and keywords that
are subjects or objects of an action.

### Metadata
Get author information, publication date, and the title of your text/HTML content.
"""

from __future__ import absolute_import

import json
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class NaturalLanguageUnderstandingV1(WatsonService):
    """The Natural Language Understanding V1 service."""

    default_url = 'https://gateway.watsonplatform.net/natural-language-understanding/api'

    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
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

        :param str iam_api_key: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.ng.bluemix.net/identity/token'.
        """

        WatsonService.__init__(
            self,
            vcap_services_name='natural-language-understanding',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # analyze
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
        Analyze text, HTML, or a public webpage.

        Analyzes text, HTML, or a public webpage with one or more text analysis features.

        :param Features features: Specific features to analyze the document for.
        :param str text: The plain text to analyze.
        :param str html: The HTML file to analyze.
        :param str url: The web page to analyze.
        :param bool clean: Remove website elements, such as links, ads, etc.
        :param str xpath: XPath query for targeting nodes in HTML.
        :param bool fallback_to_raw: Whether to use raw HTML content if text cleaning fails.
        :param bool return_analyzed_text: Whether or not to return the analyzed text.
        :param str language: ISO 639-1 code indicating the language to use in the analysis.
        :param int limit_text_characters: Sets the maximum number of characters that are processed by the service.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `AnalysisResults` response.
        :rtype: dict
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
    # modelManagement
    #########################

    def delete_model(self, model_id, **kwargs):
        """
        Delete model.

        Deletes a custom model.

        :param str model_id: model_id of the model to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `InlineResponse200` response.
        :rtype: dict
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

        Lists available models for Relations and Entities features, including Watson
        Knowledge Studio custom models that you have created and linked to your Natural
        Language Understanding service.

        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ListModelsResults` response.
        :rtype: dict
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
    :attr str retrieved_url: (optional) URL that was used to retrieve HTML content.
    :attr Usage usage: (optional) API usage information for the request.
    :attr list[ConceptsResult] concepts: (optional) The general concepts referenced or alluded to in the specified content.
    :attr list[EntitiesResult] entities: (optional) The important entities in the specified content.
    :attr list[KeywordsResult] keywords: (optional) The important keywords in content organized by relevance.
    :attr list[CategoriesResult] categories: (optional) The hierarchical 5-level taxonomy the content is categorized into.
    :attr EmotionResult emotion: (optional) The anger, disgust, fear, joy, or sadness conveyed by the content.
    :attr MetadataResult metadata: (optional) The metadata holds author information, publication date and the title of the text/HTML content.
    :attr list[RelationsResult] relations: (optional) The relationships between entities in the content.
    :attr list[SemanticRolesResult] semantic_roles: (optional) The subjects of actions and the objects the actions act upon.
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
        :param str retrieved_url: (optional) URL that was used to retrieve HTML content.
        :param Usage usage: (optional) API usage information for the request.
        :param list[ConceptsResult] concepts: (optional) The general concepts referenced or alluded to in the specified content.
        :param list[EntitiesResult] entities: (optional) The important entities in the specified content.
        :param list[KeywordsResult] keywords: (optional) The important keywords in content organized by relevance.
        :param list[CategoriesResult] categories: (optional) The hierarchical 5-level taxonomy the content is categorized into.
        :param EmotionResult emotion: (optional) The anger, disgust, fear, joy, or sadness conveyed by the content.
        :param MetadataResult metadata: (optional) The metadata holds author information, publication date and the title of the text/HTML content.
        :param list[RelationsResult] relations: (optional) The relationships between entities in the content.
        :param list[SemanticRolesResult] semantic_roles: (optional) The subjects of actions and the objects the actions act upon.
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
    The hierarchical 5-level taxonomy the content is categorized into.

    """

    def __init__(self, **kwargs):
        """
        Initialize a CategoriesOptions object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesOptions object from a json dictionary."""
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
            super(CategoriesOptions, self).__setattr__('_additionalProperties',
                                                       set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(CategoriesOptions, self).__setattr__(name, value)

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
    The hierarchical 5-level taxonomy the content is categorized into.

    :attr str label: (optional) The path to the category through the taxonomy hierarchy.
    :attr float score: (optional) Confidence score for the category classification. Higher values indicate greater confidence.
    """

    def __init__(self, label=None, score=None):
        """
        Initialize a CategoriesResult object.

        :param str label: (optional) The path to the category through the taxonomy hierarchy.
        :param float score: (optional) Confidence score for the category classification. Higher values indicate greater confidence.
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
    Whether or not to analyze content for general concepts that are referenced or alluded
    to.

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
    The general concepts referenced or alluded to in the specified content.

    :attr str text: (optional) Name of the concept.
    :attr float relevance: (optional) Relevance score between 0 and 1. Higher scores indicate greater relevance.
    :attr str dbpedia_resource: (optional) Link to the corresponding DBpedia resource.
    """

    def __init__(self, text=None, relevance=None, dbpedia_resource=None):
        """
        Initialize a ConceptsResult object.

        :param str text: (optional) Name of the concept.
        :param float relevance: (optional) Relevance score between 0 and 1. Higher scores indicate greater relevance.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia resource.
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
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia resource.
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
    An object containing the emotion results of a document.

    :attr EmotionScores emotion: (optional) An object containing the emotion results for the document.
    """

    def __init__(self, emotion=None):
        """
        Initialize a DocumentEmotionResults object.

        :param EmotionScores emotion: (optional) An object containing the emotion results for the document.
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

    :attr str label: (optional) Indicates whether the sentiment is positive, neutral, or negative.
    :attr float score: (optional) Sentiment score from -1 (negative) to 1 (positive).
    """

    def __init__(self, label=None, score=None):
        """
        Initialize a DocumentSentimentResults object.

        :param str label: (optional) Indicates whether the sentiment is positive, neutral, or negative.
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
    Whether or not to return emotion analysis of the content.

    :attr bool document: (optional) Set this to false to hide document-level emotion results.
    :attr list[str] targets: (optional) Emotion results will be returned for each target string that is found in the document.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a EmotionOptions object.

        :param bool document: (optional) Set this to false to hide document-level emotion results.
        :param list[str] targets: (optional) Emotion results will be returned for each target string that is found in the document.
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

    :attr DocumentEmotionResults document: (optional) The returned emotion results across the document.
    :attr list[TargetedEmotionResults] targets: (optional) The returned emotion results per specified target.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a EmotionResult object.

        :param DocumentEmotionResults document: (optional) The returned emotion results across the document.
        :param list[TargetedEmotionResults] targets: (optional) The returned emotion results per specified target.
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

    :attr float anger: (optional) Anger score from 0 to 1. A higher score means that the text is more likely to convey anger.
    :attr float disgust: (optional) Disgust score from 0 to 1. A higher score means that the text is more likely to convey disgust.
    :attr float fear: (optional) Fear score from 0 to 1. A higher score means that the text is more likely to convey fear.
    :attr float joy: (optional) Joy score from 0 to 1. A higher score means that the text is more likely to convey joy.
    :attr float sadness: (optional) Sadness score from 0 to 1. A higher score means that the text is more likely to convey sadness.
    """

    def __init__(self,
                 anger=None,
                 disgust=None,
                 fear=None,
                 joy=None,
                 sadness=None):
        """
        Initialize a EmotionScores object.

        :param float anger: (optional) Anger score from 0 to 1. A higher score means that the text is more likely to convey anger.
        :param float disgust: (optional) Disgust score from 0 to 1. A higher score means that the text is more likely to convey disgust.
        :param float fear: (optional) Fear score from 0 to 1. A higher score means that the text is more likely to convey fear.
        :param float joy: (optional) Joy score from 0 to 1. A higher score means that the text is more likely to convey joy.
        :param float sadness: (optional) Sadness score from 0 to 1. A higher score means that the text is more likely to convey sadness.
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
    Whether or not to return important people, places, geopolitical, and other entities
    detected in the analyzed content.

    :attr int limit: (optional) Maximum number of entities to return.
    :attr bool mentions: (optional) Set this to true to return locations of entity mentions.
    :attr str model: (optional) Enter a custom model ID to override the standard entity detection model.
    :attr bool sentiment: (optional) Set this to true to return sentiment information for detected entities.
    :attr bool emotion: (optional) Set this to true to analyze emotion for detected keywords.
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
        :param bool mentions: (optional) Set this to true to return locations of entity mentions.
        :param str model: (optional) Enter a custom model ID to override the standard entity detection model.
        :param bool sentiment: (optional) Set this to true to return sentiment information for detected entities.
        :param bool emotion: (optional) Set this to true to analyze emotion for detected keywords.
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
    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values indicate greater relevance.
    :attr list[EntityMention] mentions: (optional) Entity mentions and locations.
    :attr int count: (optional) How many times the entity was mentioned in the text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the entity, enabled with the "emotion" option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the entity, enabled with the "sentiment" option.
    :attr DisambiguationResult disambiguation: (optional) Disambiguation information for the entity.
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
        :param float relevance: (optional) Relevance score from 0 to 1. Higher values indicate greater relevance.
        :param list[EntityMention] mentions: (optional) Entity mentions and locations.
        :param int count: (optional) How many times the entity was mentioned in the text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the entity, enabled with the "emotion" option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the entity, enabled with the "sentiment" option.
        :param DisambiguationResult disambiguation: (optional) Disambiguation information for the entity.
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
    :attr list[int] location: (optional) Character offsets indicating the beginning and end of the mention in the analyzed text.
    """

    def __init__(self, text=None, location=None):
        """
        Initialize a EntityMention object.

        :param str text: (optional) Entity mention text.
        :param list[int] location: (optional) Character offsets indicating the beginning and end of the mention in the analyzed text.
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

    :attr ConceptsOptions concepts: (optional) Whether or not to return the concepts that are mentioned in the analyzed text.
    :attr EmotionOptions emotion: (optional) Whether or not to extract the emotions implied in the analyzed text.
    :attr EntitiesOptions entities: (optional) Whether or not to extract detected entity objects from the analyzed text.
    :attr KeywordsOptions keywords: (optional) Whether or not to return the keywords in the analyzed text.
    :attr MetadataOptions metadata: (optional) Whether or not the author, publication date, and title of the analyzed text should be returned. This parameter is only available for URL and HTML input.
    :attr RelationsOptions relations: (optional) Whether or not to return the relationships between detected entities in the analyzed text.
    :attr SemanticRolesOptions semantic_roles: (optional) Whether or not to return the subject-action-object relations from the analyzed text.
    :attr SentimentOptions sentiment: (optional) Whether or not to return the overall sentiment of the analyzed text.
    :attr CategoriesOptions categories: (optional) Whether or not to return the high level category the content is categorized as (i.e. news, art).
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

        :param ConceptsOptions concepts: (optional) Whether or not to return the concepts that are mentioned in the analyzed text.
        :param EmotionOptions emotion: (optional) Whether or not to extract the emotions implied in the analyzed text.
        :param EntitiesOptions entities: (optional) Whether or not to extract detected entity objects from the analyzed text.
        :param KeywordsOptions keywords: (optional) Whether or not to return the keywords in the analyzed text.
        :param MetadataOptions metadata: (optional) Whether or not the author, publication date, and title of the analyzed text should be returned. This parameter is only available for URL and HTML input.
        :param RelationsOptions relations: (optional) Whether or not to return the relationships between detected entities in the analyzed text.
        :param SemanticRolesOptions semantic_roles: (optional) Whether or not to return the subject-action-object relations from the analyzed text.
        :param SentimentOptions sentiment: (optional) Whether or not to return the overall sentiment of the analyzed text.
        :param CategoriesOptions categories: (optional) Whether or not to return the high level category the content is categorized as (i.e. news, art).
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
            args['concepts'] = ConceptsOptions._from_dict(
                _dict.get('concepts'))
        if 'emotion' in _dict:
            args['emotion'] = EmotionOptions._from_dict(_dict.get('emotion'))
        if 'entities' in _dict:
            args['entities'] = EntitiesOptions._from_dict(
                _dict.get('entities'))
        if 'keywords' in _dict:
            args['keywords'] = KeywordsOptions._from_dict(
                _dict.get('keywords'))
        if 'metadata' in _dict:
            args['metadata'] = MetadataOptions._from_dict(
                _dict.get('metadata'))
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


class InlineResponse200(object):
    """
    InlineResponse200.

    :attr str deleted: (optional) model_id of the deleted model.
    """

    def __init__(self, deleted=None):
        """
        Initialize a InlineResponse200 object.

        :param str deleted: (optional) model_id of the deleted model.
        """
        self.deleted = deleted

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InlineResponse200 object from a json dictionary."""
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
        """Return a `str` version of this InlineResponse200 object."""
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
    An option indicating whether or not important keywords from the analyzed content
    should be returned.

    :attr int limit: (optional) Maximum number of keywords to return.
    :attr bool sentiment: (optional) Set this to true to return sentiment information for detected keywords.
    :attr bool emotion: (optional) Set this to true to analyze emotion for detected keywords.
    """

    def __init__(self, limit=None, sentiment=None, emotion=None):
        """
        Initialize a KeywordsOptions object.

        :param int limit: (optional) Maximum number of keywords to return.
        :param bool sentiment: (optional) Set this to true to return sentiment information for detected keywords.
        :param bool emotion: (optional) Set this to true to analyze emotion for detected keywords.
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
    The most important keywords in the content, organized by relevance.

    :attr float relevance: (optional) Relevance score from 0 to 1. Higher values indicate greater relevance.
    :attr str text: (optional) The keyword text.
    :attr EmotionScores emotion: (optional) Emotion analysis results for the keyword, enabled with the "emotion" option.
    :attr FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the keyword, enabled with the "sentiment" option.
    """

    def __init__(self, relevance=None, text=None, emotion=None,
                 sentiment=None):
        """
        Initialize a KeywordsResult object.

        :param float relevance: (optional) Relevance score from 0 to 1. Higher values indicate greater relevance.
        :param str text: (optional) The keyword text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the keyword, enabled with the "emotion" option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results for the keyword, enabled with the "sentiment" option.
        """
        self.relevance = relevance
        self.text = text
        self.emotion = emotion
        self.sentiment = sentiment

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsResult object from a json dictionary."""
        args = {}
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

    :attr list[Model] models: (optional)
    """

    def __init__(self, models=None):
        """
        Initialize a ListModelsResults object.

        :param list[Model] models: (optional)
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
    The Authors, Publication Date, and Title of the document. Supports URL and HTML input
    types.

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
    The Authors, Publication Date, and Title of the document. Supports URL and HTML input
    types.

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
        :param str publication_date: (optional) The publication date in the format ISO 8601.
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
            args['feeds'] = [Feed._from_dict(x) for x in _dict.get('feeds')]
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

    :attr str status: (optional) Shows as available if the model is ready for use.
    :attr str model_id: (optional) Unique model ID.
    :attr str language: (optional) ISO 639-1 code indicating the language of the model.
    :attr str description: (optional) Model description.
    """

    def __init__(self,
                 status=None,
                 model_id=None,
                 language=None,
                 description=None):
        """
        Initialize a Model object.

        :param str status: (optional) Shows as available if the model is ready for use.
        :param str model_id: (optional) Unique model ID.
        :param str language: (optional) ISO 639-1 code indicating the language of the model.
        :param str description: (optional) Model description.
        """
        self.status = status
        self.model_id = model_id
        self.language = language
        self.description = description

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

    :attr list[RelationEntity] entities: (optional)
    :attr list[int] location: (optional) Character offsets indicating the beginning and end of the mention in the analyzed text.
    :attr str text: (optional) Text that corresponds to the argument.
    """

    def __init__(self, entities=None, location=None, text=None):
        """
        Initialize a RelationArgument object.

        :param list[RelationEntity] entities: (optional)
        :param list[int] location: (optional) Character offsets indicating the beginning and end of the mention in the analyzed text.
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
    An option specifying if the relationships found between entities in the analyzed
    content should be returned.

    :attr str model: (optional) Enter a custom model ID to override the default model.
    """

    def __init__(self, model=None):
        """
        Initialize a RelationsOptions object.

        :param str model: (optional) Enter a custom model ID to override the default model.
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

    :attr float score: (optional) Confidence score for the relation. Higher values indicate greater confidence.
    :attr str sentence: (optional) The sentence that contains the relation.
    :attr str type: (optional) The type of the relation.
    :attr list[RelationArgument] arguments: (optional) The extracted relation objects from the text.
    """

    def __init__(self, score=None, sentence=None, type=None, arguments=None):
        """
        Initialize a RelationsResult object.

        :param float score: (optional) Confidence score for the relation. Higher values indicate greater confidence.
        :param str sentence: (optional) The sentence that contains the relation.
        :param str type: (optional) The type of the relation.
        :param list[RelationArgument] arguments: (optional) The extracted relation objects from the text.
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
                RelationArgument._from_dict(x)
                for x in (_dict.get('arguments'))
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
    :attr list[SemanticRolesKeyword] keywords: (optional)
    """

    def __init__(self, text=None, keywords=None):
        """
        Initialize a SemanticRolesObject object.

        :param str text: (optional) Object text.
        :param list[SemanticRolesKeyword] keywords: (optional)
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
    An option specifying whether or not to identify the subjects, actions, and verbs in
    the analyzed content.

    :attr int limit: (optional) Maximum number of semantic_roles results to return.
    :attr bool keywords: (optional) Set this to true to return keyword information for subjects and objects.
    :attr bool entities: (optional) Set this to true to return entity information for subjects and objects.
    """

    def __init__(self, limit=None, keywords=None, entities=None):
        """
        Initialize a SemanticRolesOptions object.

        :param int limit: (optional) Maximum number of semantic_roles results to return.
        :param bool keywords: (optional) Set this to true to return keyword information for subjects and objects.
        :param bool entities: (optional) Set this to true to return entity information for subjects and objects.
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

    :attr str sentence: (optional) Sentence from the source that contains the subject, action, and object.
    :attr SemanticRolesSubject subject: (optional) The extracted subject from the sentence.
    :attr SemanticRolesAction action: (optional) The extracted action from the sentence.
    :attr SemanticRolesObject object: (optional) The extracted object from the sentence.
    """

    def __init__(self, sentence=None, subject=None, action=None, object=None):
        """
        Initialize a SemanticRolesResult object.

        :param str sentence: (optional) Sentence from the source that contains the subject, action, and object.
        :param SemanticRolesSubject subject: (optional) The extracted subject from the sentence.
        :param SemanticRolesAction action: (optional) The extracted action from the sentence.
        :param SemanticRolesObject object: (optional) The extracted object from the sentence.
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
            args['action'] = SemanticRolesAction._from_dict(
                _dict.get('action'))
        if 'object' in _dict:
            args['object'] = SemanticRolesObject._from_dict(
                _dict.get('object'))
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
    :attr list[SemanticRolesEntity] entities: (optional)
    :attr list[SemanticRolesKeyword] keywords: (optional)
    """

    def __init__(self, text=None, entities=None, keywords=None):
        """
        Initialize a SemanticRolesSubject object.

        :param str text: (optional) Text that corresponds to the subject role.
        :param list[SemanticRolesEntity] entities: (optional)
        :param list[SemanticRolesKeyword] keywords: (optional)
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
    An option specifying if sentiment of detected entities, keywords, or phrases should be
    returned.

    :attr bool document: (optional) Set this to false to hide document-level sentiment results.
    :attr list[str] targets: (optional) Sentiment results will be returned for each target string that is found in the document.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a SentimentOptions object.

        :param bool document: (optional) Set this to false to hide document-level sentiment results.
        :param list[str] targets: (optional) Sentiment results will be returned for each target string that is found in the document.
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
    :attr list[TargetedSentimentResults] targets: (optional) The targeted sentiment to analyze.
    """

    def __init__(self, document=None, targets=None):
        """
        Initialize a SentimentResult object.

        :param DocumentSentimentResults document: (optional) The document level sentiment.
        :param list[TargetedSentimentResults] targets: (optional) The targeted sentiment to analyze.
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
    An object containing the emotion results for the target.

    :attr str text: (optional) Targeted text.
    :attr EmotionScores emotion: (optional) An object containing the emotion results for the target.
    """

    def __init__(self, text=None, emotion=None):
        """
        Initialize a TargetedEmotionResults object.

        :param str text: (optional) Targeted text.
        :param EmotionScores emotion: (optional) An object containing the emotion results for the target.
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
