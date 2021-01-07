# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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
Unit Tests for NaturalLanguageUnderstandingV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_watson.natural_language_understanding_v1 import *

version = 'testString'

service = NaturalLanguageUnderstandingV1(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

base_url = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com'
service.set_service_url(base_url)

##############################################################################
# Start of Service: Analyze
##############################################################################
# region

class TestAnalyze():
    """
    Test Class for analyze
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_analyze_all_params(self):
        """
        analyze()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/analyze')
        mock_response = '{"language": "language", "analyzed_text": "analyzed_text", "retrieved_url": "retrieved_url", "usage": {"features": 8, "text_characters": 15, "text_units": 10}, "concepts": [{"text": "text", "relevance": 9, "dbpedia_resource": "dbpedia_resource"}], "entities": [{"type": "type", "text": "text", "relevance": 9, "confidence": 10, "mentions": [{"text": "text", "location": [8], "confidence": 10}], "count": 5, "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}, "sentiment": {"score": 5}, "disambiguation": {"name": "name", "dbpedia_resource": "dbpedia_resource", "subtype": ["subtype"]}}], "keywords": [{"count": 5, "relevance": 9, "text": "text", "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}, "sentiment": {"score": 5}}], "categories": [{"label": "label", "score": 5, "explanation": {"relevant_text": [{"text": "text"}]}}], "emotion": {"document": {"emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}}, "targets": [{"text": "text", "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}}]}, "metadata": {"authors": [{"name": "name"}], "publication_date": "publication_date", "title": "title", "image": "image", "feeds": [{"link": "link"}]}, "relations": [{"score": 5, "sentence": "sentence", "type": "type", "arguments": [{"entities": [{"text": "text", "type": "type"}], "location": [8], "text": "text"}]}], "semantic_roles": [{"sentence": "sentence", "subject": {"text": "text", "entities": [{"type": "type", "text": "text"}], "keywords": [{"text": "text"}]}, "action": {"text": "text", "normalized": "normalized", "verb": {"text": "text", "tense": "tense"}}, "object": {"text": "text", "keywords": [{"text": "text"}]}}], "sentiment": {"document": {"label": "label", "score": 5}, "targets": [{"text": "text", "score": 5}]}, "syntax": {"tokens": [{"text": "text", "part_of_speech": "ADJ", "location": [8], "lemma": "lemma"}], "sentences": [{"text": "text", "location": [8]}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ConceptsOptions model
        concepts_options_model = {}
        concepts_options_model['limit'] = 50

        # Construct a dict representation of a EmotionOptions model
        emotion_options_model = {}
        emotion_options_model['document'] = True
        emotion_options_model['targets'] = ['testString']

        # Construct a dict representation of a EntitiesOptions model
        entities_options_model = {}
        entities_options_model['limit'] = 250
        entities_options_model['mentions'] = True
        entities_options_model['model'] = 'testString'
        entities_options_model['sentiment'] = True
        entities_options_model['emotion'] = True

        # Construct a dict representation of a KeywordsOptions model
        keywords_options_model = {}
        keywords_options_model['limit'] = 250
        keywords_options_model['sentiment'] = True
        keywords_options_model['emotion'] = True

        # Construct a dict representation of a RelationsOptions model
        relations_options_model = {}
        relations_options_model['model'] = 'testString'

        # Construct a dict representation of a SemanticRolesOptions model
        semantic_roles_options_model = {}
        semantic_roles_options_model['limit'] = 38
        semantic_roles_options_model['keywords'] = True
        semantic_roles_options_model['entities'] = True

        # Construct a dict representation of a SentimentOptions model
        sentiment_options_model = {}
        sentiment_options_model['document'] = True
        sentiment_options_model['targets'] = ['testString']

        # Construct a dict representation of a CategoriesOptions model
        categories_options_model = {}
        categories_options_model['explanation'] = True
        categories_options_model['limit'] = 10
        categories_options_model['model'] = 'testString'

        # Construct a dict representation of a SyntaxOptionsTokens model
        syntax_options_tokens_model = {}
        syntax_options_tokens_model['lemma'] = True
        syntax_options_tokens_model['part_of_speech'] = True

        # Construct a dict representation of a SyntaxOptions model
        syntax_options_model = {}
        syntax_options_model['tokens'] = syntax_options_tokens_model
        syntax_options_model['sentences'] = True

        # Construct a dict representation of a Features model
        features_model = {}
        features_model['concepts'] = concepts_options_model
        features_model['emotion'] = emotion_options_model
        features_model['entities'] = entities_options_model
        features_model['keywords'] = keywords_options_model
        features_model['metadata'] = { 'foo': 'bar' }
        features_model['relations'] = relations_options_model
        features_model['semantic_roles'] = semantic_roles_options_model
        features_model['sentiment'] = sentiment_options_model
        features_model['categories'] = categories_options_model
        features_model['syntax'] = syntax_options_model

        # Set up parameter values
        features = features_model
        text = 'testString'
        html = 'testString'
        url = 'testString'
        clean = True
        xpath = 'testString'
        fallback_to_raw = True
        return_analyzed_text = True
        language = 'testString'
        limit_text_characters = 38

        # Invoke method
        response = service.analyze(
            features,
            text=text,
            html=html,
            url=url,
            clean=clean,
            xpath=xpath,
            fallback_to_raw=fallback_to_raw,
            return_analyzed_text=return_analyzed_text,
            language=language,
            limit_text_characters=limit_text_characters,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['features'] == features_model
        assert req_body['text'] == 'testString'
        assert req_body['html'] == 'testString'
        assert req_body['url'] == 'testString'
        assert req_body['clean'] == True
        assert req_body['xpath'] == 'testString'
        assert req_body['fallback_to_raw'] == True
        assert req_body['return_analyzed_text'] == True
        assert req_body['language'] == 'testString'
        assert req_body['limit_text_characters'] == 38


    @responses.activate
    def test_analyze_value_error(self):
        """
        test_analyze_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/analyze')
        mock_response = '{"language": "language", "analyzed_text": "analyzed_text", "retrieved_url": "retrieved_url", "usage": {"features": 8, "text_characters": 15, "text_units": 10}, "concepts": [{"text": "text", "relevance": 9, "dbpedia_resource": "dbpedia_resource"}], "entities": [{"type": "type", "text": "text", "relevance": 9, "confidence": 10, "mentions": [{"text": "text", "location": [8], "confidence": 10}], "count": 5, "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}, "sentiment": {"score": 5}, "disambiguation": {"name": "name", "dbpedia_resource": "dbpedia_resource", "subtype": ["subtype"]}}], "keywords": [{"count": 5, "relevance": 9, "text": "text", "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}, "sentiment": {"score": 5}}], "categories": [{"label": "label", "score": 5, "explanation": {"relevant_text": [{"text": "text"}]}}], "emotion": {"document": {"emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}}, "targets": [{"text": "text", "emotion": {"anger": 5, "disgust": 7, "fear": 4, "joy": 3, "sadness": 7}}]}, "metadata": {"authors": [{"name": "name"}], "publication_date": "publication_date", "title": "title", "image": "image", "feeds": [{"link": "link"}]}, "relations": [{"score": 5, "sentence": "sentence", "type": "type", "arguments": [{"entities": [{"text": "text", "type": "type"}], "location": [8], "text": "text"}]}], "semantic_roles": [{"sentence": "sentence", "subject": {"text": "text", "entities": [{"type": "type", "text": "text"}], "keywords": [{"text": "text"}]}, "action": {"text": "text", "normalized": "normalized", "verb": {"text": "text", "tense": "tense"}}, "object": {"text": "text", "keywords": [{"text": "text"}]}}], "sentiment": {"document": {"label": "label", "score": 5}, "targets": [{"text": "text", "score": 5}]}, "syntax": {"tokens": [{"text": "text", "part_of_speech": "ADJ", "location": [8], "lemma": "lemma"}], "sentences": [{"text": "text", "location": [8]}]}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ConceptsOptions model
        concepts_options_model = {}
        concepts_options_model['limit'] = 50

        # Construct a dict representation of a EmotionOptions model
        emotion_options_model = {}
        emotion_options_model['document'] = True
        emotion_options_model['targets'] = ['testString']

        # Construct a dict representation of a EntitiesOptions model
        entities_options_model = {}
        entities_options_model['limit'] = 250
        entities_options_model['mentions'] = True
        entities_options_model['model'] = 'testString'
        entities_options_model['sentiment'] = True
        entities_options_model['emotion'] = True

        # Construct a dict representation of a KeywordsOptions model
        keywords_options_model = {}
        keywords_options_model['limit'] = 250
        keywords_options_model['sentiment'] = True
        keywords_options_model['emotion'] = True

        # Construct a dict representation of a RelationsOptions model
        relations_options_model = {}
        relations_options_model['model'] = 'testString'

        # Construct a dict representation of a SemanticRolesOptions model
        semantic_roles_options_model = {}
        semantic_roles_options_model['limit'] = 38
        semantic_roles_options_model['keywords'] = True
        semantic_roles_options_model['entities'] = True

        # Construct a dict representation of a SentimentOptions model
        sentiment_options_model = {}
        sentiment_options_model['document'] = True
        sentiment_options_model['targets'] = ['testString']

        # Construct a dict representation of a CategoriesOptions model
        categories_options_model = {}
        categories_options_model['explanation'] = True
        categories_options_model['limit'] = 10
        categories_options_model['model'] = 'testString'

        # Construct a dict representation of a SyntaxOptionsTokens model
        syntax_options_tokens_model = {}
        syntax_options_tokens_model['lemma'] = True
        syntax_options_tokens_model['part_of_speech'] = True

        # Construct a dict representation of a SyntaxOptions model
        syntax_options_model = {}
        syntax_options_model['tokens'] = syntax_options_tokens_model
        syntax_options_model['sentences'] = True

        # Construct a dict representation of a Features model
        features_model = {}
        features_model['concepts'] = concepts_options_model
        features_model['emotion'] = emotion_options_model
        features_model['entities'] = entities_options_model
        features_model['keywords'] = keywords_options_model
        features_model['metadata'] = { 'foo': 'bar' }
        features_model['relations'] = relations_options_model
        features_model['semantic_roles'] = semantic_roles_options_model
        features_model['sentiment'] = sentiment_options_model
        features_model['categories'] = categories_options_model
        features_model['syntax'] = syntax_options_model

        # Set up parameter values
        features = features_model
        text = 'testString'
        html = 'testString'
        url = 'testString'
        clean = True
        xpath = 'testString'
        fallback_to_raw = True
        return_analyzed_text = True
        language = 'testString'
        limit_text_characters = 38

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "features": features,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.analyze(**req_copy)



# endregion
##############################################################################
# End of Service: Analyze
##############################################################################

##############################################################################
# Start of Service: ManageModels
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
        url = self.preprocess_url(base_url + '/v1/models')
        mock_response = '{"models": [{"status": "starting", "model_id": "model_id", "language": "language", "description": "description", "workspace_id": "workspace_id", "model_version": "model_version", "version": "version", "version_description": "version_description", "created": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = service.list_models()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_list_models_value_error(self):
        """
        test_list_models_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/models')
        mock_response = '{"models": [{"status": "starting", "model_id": "model_id", "language": "language", "description": "description", "workspace_id": "workspace_id", "model_version": "model_version", "version": "version", "version_description": "version_description", "created": "2019-01-01T12:00:00"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.list_models(**req_copy)



class TestDeleteModel():
    """
    Test Class for delete_model
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_model_all_params(self):
        """
        delete_model()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/models/testString')
        mock_response = '{"deleted": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Invoke method
        response = service.delete_model(
            model_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_model_value_error(self):
        """
        test_delete_model_value_error()
        """
        # Set up mock
        url = self.preprocess_url(base_url + '/v1/models/testString')
        mock_response = '{"deleted": "deleted"}'
        responses.add(responses.DELETE,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        model_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "model_id": model_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                service.delete_model(**req_copy)



# endregion
##############################################################################
# End of Service: ManageModels
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestAnalysisResults():
    """
    Test Class for AnalysisResults
    """

    def test_analysis_results_serialization(self):
        """
        Test serialization/deserialization for AnalysisResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analysis_results_usage_model = {} # AnalysisResultsUsage
        analysis_results_usage_model['features'] = 38
        analysis_results_usage_model['text_characters'] = 38
        analysis_results_usage_model['text_units'] = 38

        concepts_result_model = {} # ConceptsResult
        concepts_result_model['text'] = 'Social network service'
        concepts_result_model['relevance'] = 0.92186
        concepts_result_model['dbpedia_resource'] = 'http://dbpedia.org/resource/Social_network_service'

        entity_mention_model = {} # EntityMention
        entity_mention_model['text'] = 'testString'
        entity_mention_model['location'] = [38]
        entity_mention_model['confidence'] = 72.5

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 72.5
        emotion_scores_model['disgust'] = 72.5
        emotion_scores_model['fear'] = 72.5
        emotion_scores_model['joy'] = 72.5
        emotion_scores_model['sadness'] = 72.5

        feature_sentiment_results_model = {} # FeatureSentimentResults
        feature_sentiment_results_model['score'] = 72.5

        disambiguation_result_model = {} # DisambiguationResult
        disambiguation_result_model['name'] = 'testString'
        disambiguation_result_model['dbpedia_resource'] = 'testString'
        disambiguation_result_model['subtype'] = ['testString']

        entities_result_model = {} # EntitiesResult
        entities_result_model['type'] = 'testString'
        entities_result_model['text'] = 'Social network service'
        entities_result_model['relevance'] = 0.92186
        entities_result_model['confidence'] = 72.5
        entities_result_model['mentions'] = [entity_mention_model]
        entities_result_model['count'] = 38
        entities_result_model['emotion'] = emotion_scores_model
        entities_result_model['sentiment'] = feature_sentiment_results_model
        entities_result_model['disambiguation'] = disambiguation_result_model

        keywords_result_model = {} # KeywordsResult
        keywords_result_model['count'] = 1
        keywords_result_model['relevance'] = 0.864624
        keywords_result_model['text'] = 'curated online courses'
        keywords_result_model['emotion'] = emotion_scores_model
        keywords_result_model['sentiment'] = feature_sentiment_results_model

        categories_relevant_text_model = {} # CategoriesRelevantText
        categories_relevant_text_model['text'] = 'testString'

        categories_result_explanation_model = {} # CategoriesResultExplanation
        categories_result_explanation_model['relevant_text'] = [categories_relevant_text_model]

        categories_result_model = {} # CategoriesResult
        categories_result_model['label'] = '/technology and computing/software'
        categories_result_model['score'] = 0.594296
        categories_result_model['explanation'] = categories_result_explanation_model

        document_emotion_results_model = {} # DocumentEmotionResults
        document_emotion_results_model['emotion'] = emotion_scores_model

        targeted_emotion_results_model = {} # TargetedEmotionResults
        targeted_emotion_results_model['text'] = 'testString'
        targeted_emotion_results_model['emotion'] = emotion_scores_model

        emotion_result_model = {} # EmotionResult
        emotion_result_model['document'] = document_emotion_results_model
        emotion_result_model['targets'] = [targeted_emotion_results_model]

        author_model = {} # Author
        author_model['name'] = 'testString'

        feed_model = {} # Feed
        feed_model['link'] = 'testString'

        features_results_metadata_model = {} # FeaturesResultsMetadata
        features_results_metadata_model['authors'] = [author_model]
        features_results_metadata_model['publication_date'] = 'testString'
        features_results_metadata_model['title'] = 'testString'
        features_results_metadata_model['image'] = 'testString'
        features_results_metadata_model['feeds'] = [feed_model]

        relation_entity_model = {} # RelationEntity
        relation_entity_model['text'] = 'Best Actor'
        relation_entity_model['type'] = 'EntertainmentAward'

        relation_argument_model = {} # RelationArgument
        relation_argument_model['entities'] = [relation_entity_model]
        relation_argument_model['location'] = [38]
        relation_argument_model['text'] = 'Best Actor'

        relations_result_model = {} # RelationsResult
        relations_result_model['score'] = 0.680715
        relations_result_model['sentence'] = 'Leonardo DiCaprio won Best Actor in a Leading Role for his performance.'
        relations_result_model['type'] = 'awardedTo'
        relations_result_model['arguments'] = [relation_argument_model]

        semantic_roles_entity_model = {} # SemanticRolesEntity
        semantic_roles_entity_model['type'] = 'testString'
        semantic_roles_entity_model['text'] = 'testString'

        semantic_roles_keyword_model = {} # SemanticRolesKeyword
        semantic_roles_keyword_model['text'] = 'testString'

        semantic_roles_result_subject_model = {} # SemanticRolesResultSubject
        semantic_roles_result_subject_model['text'] = 'IBM'
        semantic_roles_result_subject_model['entities'] = [semantic_roles_entity_model]
        semantic_roles_result_subject_model['keywords'] = [semantic_roles_keyword_model]

        semantic_roles_verb_model = {} # SemanticRolesVerb
        semantic_roles_verb_model['text'] = 'have'
        semantic_roles_verb_model['tense'] = 'present'

        semantic_roles_result_action_model = {} # SemanticRolesResultAction
        semantic_roles_result_action_model['text'] = 'has'
        semantic_roles_result_action_model['normalized'] = 'have'
        semantic_roles_result_action_model['verb'] = semantic_roles_verb_model

        semantic_roles_result_object_model = {} # SemanticRolesResultObject
        semantic_roles_result_object_model['text'] = 'one of the largest workforces in the world'
        semantic_roles_result_object_model['keywords'] = [semantic_roles_keyword_model]

        semantic_roles_result_model = {} # SemanticRolesResult
        semantic_roles_result_model['sentence'] = 'IBM has one of the largest workforces in the world'
        semantic_roles_result_model['subject'] = semantic_roles_result_subject_model
        semantic_roles_result_model['action'] = semantic_roles_result_action_model
        semantic_roles_result_model['object'] = semantic_roles_result_object_model

        document_sentiment_results_model = {} # DocumentSentimentResults
        document_sentiment_results_model['label'] = 'testString'
        document_sentiment_results_model['score'] = 72.5

        targeted_sentiment_results_model = {} # TargetedSentimentResults
        targeted_sentiment_results_model['text'] = 'testString'
        targeted_sentiment_results_model['score'] = 72.5

        sentiment_result_model = {} # SentimentResult
        sentiment_result_model['document'] = document_sentiment_results_model
        sentiment_result_model['targets'] = [targeted_sentiment_results_model]

        token_result_model = {} # TokenResult
        token_result_model['text'] = 'testString'
        token_result_model['part_of_speech'] = 'ADJ'
        token_result_model['location'] = [38]
        token_result_model['lemma'] = 'testString'

        sentence_result_model = {} # SentenceResult
        sentence_result_model['text'] = 'testString'
        sentence_result_model['location'] = [38]

        syntax_result_model = {} # SyntaxResult
        syntax_result_model['tokens'] = [token_result_model]
        syntax_result_model['sentences'] = [sentence_result_model]

        # Construct a json representation of a AnalysisResults model
        analysis_results_model_json = {}
        analysis_results_model_json['language'] = 'testString'
        analysis_results_model_json['analyzed_text'] = 'testString'
        analysis_results_model_json['retrieved_url'] = 'testString'
        analysis_results_model_json['usage'] = analysis_results_usage_model
        analysis_results_model_json['concepts'] = [concepts_result_model]
        analysis_results_model_json['entities'] = [entities_result_model]
        analysis_results_model_json['keywords'] = [keywords_result_model]
        analysis_results_model_json['categories'] = [categories_result_model]
        analysis_results_model_json['emotion'] = emotion_result_model
        analysis_results_model_json['metadata'] = features_results_metadata_model
        analysis_results_model_json['relations'] = [relations_result_model]
        analysis_results_model_json['semantic_roles'] = [semantic_roles_result_model]
        analysis_results_model_json['sentiment'] = sentiment_result_model
        analysis_results_model_json['syntax'] = syntax_result_model

        # Construct a model instance of AnalysisResults by calling from_dict on the json representation
        analysis_results_model = AnalysisResults.from_dict(analysis_results_model_json)
        assert analysis_results_model != False

        # Construct a model instance of AnalysisResults by calling from_dict on the json representation
        analysis_results_model_dict = AnalysisResults.from_dict(analysis_results_model_json).__dict__
        analysis_results_model2 = AnalysisResults(**analysis_results_model_dict)

        # Verify the model instances are equivalent
        assert analysis_results_model == analysis_results_model2

        # Convert model instance back to dict and verify no loss of data
        analysis_results_model_json2 = analysis_results_model.to_dict()
        assert analysis_results_model_json2 == analysis_results_model_json

class TestAnalysisResultsUsage():
    """
    Test Class for AnalysisResultsUsage
    """

    def test_analysis_results_usage_serialization(self):
        """
        Test serialization/deserialization for AnalysisResultsUsage
        """

        # Construct a json representation of a AnalysisResultsUsage model
        analysis_results_usage_model_json = {}
        analysis_results_usage_model_json['features'] = 38
        analysis_results_usage_model_json['text_characters'] = 38
        analysis_results_usage_model_json['text_units'] = 38

        # Construct a model instance of AnalysisResultsUsage by calling from_dict on the json representation
        analysis_results_usage_model = AnalysisResultsUsage.from_dict(analysis_results_usage_model_json)
        assert analysis_results_usage_model != False

        # Construct a model instance of AnalysisResultsUsage by calling from_dict on the json representation
        analysis_results_usage_model_dict = AnalysisResultsUsage.from_dict(analysis_results_usage_model_json).__dict__
        analysis_results_usage_model2 = AnalysisResultsUsage(**analysis_results_usage_model_dict)

        # Verify the model instances are equivalent
        assert analysis_results_usage_model == analysis_results_usage_model2

        # Convert model instance back to dict and verify no loss of data
        analysis_results_usage_model_json2 = analysis_results_usage_model.to_dict()
        assert analysis_results_usage_model_json2 == analysis_results_usage_model_json

class TestAuthor():
    """
    Test Class for Author
    """

    def test_author_serialization(self):
        """
        Test serialization/deserialization for Author
        """

        # Construct a json representation of a Author model
        author_model_json = {}
        author_model_json['name'] = 'testString'

        # Construct a model instance of Author by calling from_dict on the json representation
        author_model = Author.from_dict(author_model_json)
        assert author_model != False

        # Construct a model instance of Author by calling from_dict on the json representation
        author_model_dict = Author.from_dict(author_model_json).__dict__
        author_model2 = Author(**author_model_dict)

        # Verify the model instances are equivalent
        assert author_model == author_model2

        # Convert model instance back to dict and verify no loss of data
        author_model_json2 = author_model.to_dict()
        assert author_model_json2 == author_model_json

class TestCategoriesOptions():
    """
    Test Class for CategoriesOptions
    """

    def test_categories_options_serialization(self):
        """
        Test serialization/deserialization for CategoriesOptions
        """

        # Construct a json representation of a CategoriesOptions model
        categories_options_model_json = {}
        categories_options_model_json['explanation'] = True
        categories_options_model_json['limit'] = 10
        categories_options_model_json['model'] = 'testString'

        # Construct a model instance of CategoriesOptions by calling from_dict on the json representation
        categories_options_model = CategoriesOptions.from_dict(categories_options_model_json)
        assert categories_options_model != False

        # Construct a model instance of CategoriesOptions by calling from_dict on the json representation
        categories_options_model_dict = CategoriesOptions.from_dict(categories_options_model_json).__dict__
        categories_options_model2 = CategoriesOptions(**categories_options_model_dict)

        # Verify the model instances are equivalent
        assert categories_options_model == categories_options_model2

        # Convert model instance back to dict and verify no loss of data
        categories_options_model_json2 = categories_options_model.to_dict()
        assert categories_options_model_json2 == categories_options_model_json

class TestCategoriesRelevantText():
    """
    Test Class for CategoriesRelevantText
    """

    def test_categories_relevant_text_serialization(self):
        """
        Test serialization/deserialization for CategoriesRelevantText
        """

        # Construct a json representation of a CategoriesRelevantText model
        categories_relevant_text_model_json = {}
        categories_relevant_text_model_json['text'] = 'testString'

        # Construct a model instance of CategoriesRelevantText by calling from_dict on the json representation
        categories_relevant_text_model = CategoriesRelevantText.from_dict(categories_relevant_text_model_json)
        assert categories_relevant_text_model != False

        # Construct a model instance of CategoriesRelevantText by calling from_dict on the json representation
        categories_relevant_text_model_dict = CategoriesRelevantText.from_dict(categories_relevant_text_model_json).__dict__
        categories_relevant_text_model2 = CategoriesRelevantText(**categories_relevant_text_model_dict)

        # Verify the model instances are equivalent
        assert categories_relevant_text_model == categories_relevant_text_model2

        # Convert model instance back to dict and verify no loss of data
        categories_relevant_text_model_json2 = categories_relevant_text_model.to_dict()
        assert categories_relevant_text_model_json2 == categories_relevant_text_model_json

class TestCategoriesResult():
    """
    Test Class for CategoriesResult
    """

    def test_categories_result_serialization(self):
        """
        Test serialization/deserialization for CategoriesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        categories_relevant_text_model = {} # CategoriesRelevantText
        categories_relevant_text_model['text'] = 'testString'

        categories_result_explanation_model = {} # CategoriesResultExplanation
        categories_result_explanation_model['relevant_text'] = [categories_relevant_text_model]

        # Construct a json representation of a CategoriesResult model
        categories_result_model_json = {}
        categories_result_model_json['label'] = 'testString'
        categories_result_model_json['score'] = 72.5
        categories_result_model_json['explanation'] = categories_result_explanation_model

        # Construct a model instance of CategoriesResult by calling from_dict on the json representation
        categories_result_model = CategoriesResult.from_dict(categories_result_model_json)
        assert categories_result_model != False

        # Construct a model instance of CategoriesResult by calling from_dict on the json representation
        categories_result_model_dict = CategoriesResult.from_dict(categories_result_model_json).__dict__
        categories_result_model2 = CategoriesResult(**categories_result_model_dict)

        # Verify the model instances are equivalent
        assert categories_result_model == categories_result_model2

        # Convert model instance back to dict and verify no loss of data
        categories_result_model_json2 = categories_result_model.to_dict()
        assert categories_result_model_json2 == categories_result_model_json

class TestCategoriesResultExplanation():
    """
    Test Class for CategoriesResultExplanation
    """

    def test_categories_result_explanation_serialization(self):
        """
        Test serialization/deserialization for CategoriesResultExplanation
        """

        # Construct dict forms of any model objects needed in order to build this model.

        categories_relevant_text_model = {} # CategoriesRelevantText
        categories_relevant_text_model['text'] = 'testString'

        # Construct a json representation of a CategoriesResultExplanation model
        categories_result_explanation_model_json = {}
        categories_result_explanation_model_json['relevant_text'] = [categories_relevant_text_model]

        # Construct a model instance of CategoriesResultExplanation by calling from_dict on the json representation
        categories_result_explanation_model = CategoriesResultExplanation.from_dict(categories_result_explanation_model_json)
        assert categories_result_explanation_model != False

        # Construct a model instance of CategoriesResultExplanation by calling from_dict on the json representation
        categories_result_explanation_model_dict = CategoriesResultExplanation.from_dict(categories_result_explanation_model_json).__dict__
        categories_result_explanation_model2 = CategoriesResultExplanation(**categories_result_explanation_model_dict)

        # Verify the model instances are equivalent
        assert categories_result_explanation_model == categories_result_explanation_model2

        # Convert model instance back to dict and verify no loss of data
        categories_result_explanation_model_json2 = categories_result_explanation_model.to_dict()
        assert categories_result_explanation_model_json2 == categories_result_explanation_model_json

class TestConceptsOptions():
    """
    Test Class for ConceptsOptions
    """

    def test_concepts_options_serialization(self):
        """
        Test serialization/deserialization for ConceptsOptions
        """

        # Construct a json representation of a ConceptsOptions model
        concepts_options_model_json = {}
        concepts_options_model_json['limit'] = 50

        # Construct a model instance of ConceptsOptions by calling from_dict on the json representation
        concepts_options_model = ConceptsOptions.from_dict(concepts_options_model_json)
        assert concepts_options_model != False

        # Construct a model instance of ConceptsOptions by calling from_dict on the json representation
        concepts_options_model_dict = ConceptsOptions.from_dict(concepts_options_model_json).__dict__
        concepts_options_model2 = ConceptsOptions(**concepts_options_model_dict)

        # Verify the model instances are equivalent
        assert concepts_options_model == concepts_options_model2

        # Convert model instance back to dict and verify no loss of data
        concepts_options_model_json2 = concepts_options_model.to_dict()
        assert concepts_options_model_json2 == concepts_options_model_json

class TestConceptsResult():
    """
    Test Class for ConceptsResult
    """

    def test_concepts_result_serialization(self):
        """
        Test serialization/deserialization for ConceptsResult
        """

        # Construct a json representation of a ConceptsResult model
        concepts_result_model_json = {}
        concepts_result_model_json['text'] = 'testString'
        concepts_result_model_json['relevance'] = 72.5
        concepts_result_model_json['dbpedia_resource'] = 'testString'

        # Construct a model instance of ConceptsResult by calling from_dict on the json representation
        concepts_result_model = ConceptsResult.from_dict(concepts_result_model_json)
        assert concepts_result_model != False

        # Construct a model instance of ConceptsResult by calling from_dict on the json representation
        concepts_result_model_dict = ConceptsResult.from_dict(concepts_result_model_json).__dict__
        concepts_result_model2 = ConceptsResult(**concepts_result_model_dict)

        # Verify the model instances are equivalent
        assert concepts_result_model == concepts_result_model2

        # Convert model instance back to dict and verify no loss of data
        concepts_result_model_json2 = concepts_result_model.to_dict()
        assert concepts_result_model_json2 == concepts_result_model_json

class TestDeleteModelResults():
    """
    Test Class for DeleteModelResults
    """

    def test_delete_model_results_serialization(self):
        """
        Test serialization/deserialization for DeleteModelResults
        """

        # Construct a json representation of a DeleteModelResults model
        delete_model_results_model_json = {}
        delete_model_results_model_json['deleted'] = 'testString'

        # Construct a model instance of DeleteModelResults by calling from_dict on the json representation
        delete_model_results_model = DeleteModelResults.from_dict(delete_model_results_model_json)
        assert delete_model_results_model != False

        # Construct a model instance of DeleteModelResults by calling from_dict on the json representation
        delete_model_results_model_dict = DeleteModelResults.from_dict(delete_model_results_model_json).__dict__
        delete_model_results_model2 = DeleteModelResults(**delete_model_results_model_dict)

        # Verify the model instances are equivalent
        assert delete_model_results_model == delete_model_results_model2

        # Convert model instance back to dict and verify no loss of data
        delete_model_results_model_json2 = delete_model_results_model.to_dict()
        assert delete_model_results_model_json2 == delete_model_results_model_json

class TestDisambiguationResult():
    """
    Test Class for DisambiguationResult
    """

    def test_disambiguation_result_serialization(self):
        """
        Test serialization/deserialization for DisambiguationResult
        """

        # Construct a json representation of a DisambiguationResult model
        disambiguation_result_model_json = {}
        disambiguation_result_model_json['name'] = 'testString'
        disambiguation_result_model_json['dbpedia_resource'] = 'testString'
        disambiguation_result_model_json['subtype'] = ['testString']

        # Construct a model instance of DisambiguationResult by calling from_dict on the json representation
        disambiguation_result_model = DisambiguationResult.from_dict(disambiguation_result_model_json)
        assert disambiguation_result_model != False

        # Construct a model instance of DisambiguationResult by calling from_dict on the json representation
        disambiguation_result_model_dict = DisambiguationResult.from_dict(disambiguation_result_model_json).__dict__
        disambiguation_result_model2 = DisambiguationResult(**disambiguation_result_model_dict)

        # Verify the model instances are equivalent
        assert disambiguation_result_model == disambiguation_result_model2

        # Convert model instance back to dict and verify no loss of data
        disambiguation_result_model_json2 = disambiguation_result_model.to_dict()
        assert disambiguation_result_model_json2 == disambiguation_result_model_json

class TestDocumentEmotionResults():
    """
    Test Class for DocumentEmotionResults
    """

    def test_document_emotion_results_serialization(self):
        """
        Test serialization/deserialization for DocumentEmotionResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 72.5
        emotion_scores_model['disgust'] = 72.5
        emotion_scores_model['fear'] = 72.5
        emotion_scores_model['joy'] = 72.5
        emotion_scores_model['sadness'] = 72.5

        # Construct a json representation of a DocumentEmotionResults model
        document_emotion_results_model_json = {}
        document_emotion_results_model_json['emotion'] = emotion_scores_model

        # Construct a model instance of DocumentEmotionResults by calling from_dict on the json representation
        document_emotion_results_model = DocumentEmotionResults.from_dict(document_emotion_results_model_json)
        assert document_emotion_results_model != False

        # Construct a model instance of DocumentEmotionResults by calling from_dict on the json representation
        document_emotion_results_model_dict = DocumentEmotionResults.from_dict(document_emotion_results_model_json).__dict__
        document_emotion_results_model2 = DocumentEmotionResults(**document_emotion_results_model_dict)

        # Verify the model instances are equivalent
        assert document_emotion_results_model == document_emotion_results_model2

        # Convert model instance back to dict and verify no loss of data
        document_emotion_results_model_json2 = document_emotion_results_model.to_dict()
        assert document_emotion_results_model_json2 == document_emotion_results_model_json

class TestDocumentSentimentResults():
    """
    Test Class for DocumentSentimentResults
    """

    def test_document_sentiment_results_serialization(self):
        """
        Test serialization/deserialization for DocumentSentimentResults
        """

        # Construct a json representation of a DocumentSentimentResults model
        document_sentiment_results_model_json = {}
        document_sentiment_results_model_json['label'] = 'testString'
        document_sentiment_results_model_json['score'] = 72.5

        # Construct a model instance of DocumentSentimentResults by calling from_dict on the json representation
        document_sentiment_results_model = DocumentSentimentResults.from_dict(document_sentiment_results_model_json)
        assert document_sentiment_results_model != False

        # Construct a model instance of DocumentSentimentResults by calling from_dict on the json representation
        document_sentiment_results_model_dict = DocumentSentimentResults.from_dict(document_sentiment_results_model_json).__dict__
        document_sentiment_results_model2 = DocumentSentimentResults(**document_sentiment_results_model_dict)

        # Verify the model instances are equivalent
        assert document_sentiment_results_model == document_sentiment_results_model2

        # Convert model instance back to dict and verify no loss of data
        document_sentiment_results_model_json2 = document_sentiment_results_model.to_dict()
        assert document_sentiment_results_model_json2 == document_sentiment_results_model_json

class TestEmotionOptions():
    """
    Test Class for EmotionOptions
    """

    def test_emotion_options_serialization(self):
        """
        Test serialization/deserialization for EmotionOptions
        """

        # Construct a json representation of a EmotionOptions model
        emotion_options_model_json = {}
        emotion_options_model_json['document'] = True
        emotion_options_model_json['targets'] = ['testString']

        # Construct a model instance of EmotionOptions by calling from_dict on the json representation
        emotion_options_model = EmotionOptions.from_dict(emotion_options_model_json)
        assert emotion_options_model != False

        # Construct a model instance of EmotionOptions by calling from_dict on the json representation
        emotion_options_model_dict = EmotionOptions.from_dict(emotion_options_model_json).__dict__
        emotion_options_model2 = EmotionOptions(**emotion_options_model_dict)

        # Verify the model instances are equivalent
        assert emotion_options_model == emotion_options_model2

        # Convert model instance back to dict and verify no loss of data
        emotion_options_model_json2 = emotion_options_model.to_dict()
        assert emotion_options_model_json2 == emotion_options_model_json

class TestEmotionResult():
    """
    Test Class for EmotionResult
    """

    def test_emotion_result_serialization(self):
        """
        Test serialization/deserialization for EmotionResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 0.041796
        emotion_scores_model['disgust'] = 0.022637
        emotion_scores_model['fear'] = 0.033387
        emotion_scores_model['joy'] = 0.563273
        emotion_scores_model['sadness'] = 0.32665

        document_emotion_results_model = {} # DocumentEmotionResults
        document_emotion_results_model['emotion'] = emotion_scores_model

        targeted_emotion_results_model = {} # TargetedEmotionResults
        targeted_emotion_results_model['text'] = 'apples'
        targeted_emotion_results_model['emotion'] = emotion_scores_model

        # Construct a json representation of a EmotionResult model
        emotion_result_model_json = {}
        emotion_result_model_json['document'] = document_emotion_results_model
        emotion_result_model_json['targets'] = [targeted_emotion_results_model]

        # Construct a model instance of EmotionResult by calling from_dict on the json representation
        emotion_result_model = EmotionResult.from_dict(emotion_result_model_json)
        assert emotion_result_model != False

        # Construct a model instance of EmotionResult by calling from_dict on the json representation
        emotion_result_model_dict = EmotionResult.from_dict(emotion_result_model_json).__dict__
        emotion_result_model2 = EmotionResult(**emotion_result_model_dict)

        # Verify the model instances are equivalent
        assert emotion_result_model == emotion_result_model2

        # Convert model instance back to dict and verify no loss of data
        emotion_result_model_json2 = emotion_result_model.to_dict()
        assert emotion_result_model_json2 == emotion_result_model_json

class TestEmotionScores():
    """
    Test Class for EmotionScores
    """

    def test_emotion_scores_serialization(self):
        """
        Test serialization/deserialization for EmotionScores
        """

        # Construct a json representation of a EmotionScores model
        emotion_scores_model_json = {}
        emotion_scores_model_json['anger'] = 72.5
        emotion_scores_model_json['disgust'] = 72.5
        emotion_scores_model_json['fear'] = 72.5
        emotion_scores_model_json['joy'] = 72.5
        emotion_scores_model_json['sadness'] = 72.5

        # Construct a model instance of EmotionScores by calling from_dict on the json representation
        emotion_scores_model = EmotionScores.from_dict(emotion_scores_model_json)
        assert emotion_scores_model != False

        # Construct a model instance of EmotionScores by calling from_dict on the json representation
        emotion_scores_model_dict = EmotionScores.from_dict(emotion_scores_model_json).__dict__
        emotion_scores_model2 = EmotionScores(**emotion_scores_model_dict)

        # Verify the model instances are equivalent
        assert emotion_scores_model == emotion_scores_model2

        # Convert model instance back to dict and verify no loss of data
        emotion_scores_model_json2 = emotion_scores_model.to_dict()
        assert emotion_scores_model_json2 == emotion_scores_model_json

class TestEntitiesOptions():
    """
    Test Class for EntitiesOptions
    """

    def test_entities_options_serialization(self):
        """
        Test serialization/deserialization for EntitiesOptions
        """

        # Construct a json representation of a EntitiesOptions model
        entities_options_model_json = {}
        entities_options_model_json['limit'] = 250
        entities_options_model_json['mentions'] = True
        entities_options_model_json['model'] = 'testString'
        entities_options_model_json['sentiment'] = True
        entities_options_model_json['emotion'] = True

        # Construct a model instance of EntitiesOptions by calling from_dict on the json representation
        entities_options_model = EntitiesOptions.from_dict(entities_options_model_json)
        assert entities_options_model != False

        # Construct a model instance of EntitiesOptions by calling from_dict on the json representation
        entities_options_model_dict = EntitiesOptions.from_dict(entities_options_model_json).__dict__
        entities_options_model2 = EntitiesOptions(**entities_options_model_dict)

        # Verify the model instances are equivalent
        assert entities_options_model == entities_options_model2

        # Convert model instance back to dict and verify no loss of data
        entities_options_model_json2 = entities_options_model.to_dict()
        assert entities_options_model_json2 == entities_options_model_json

class TestEntitiesResult():
    """
    Test Class for EntitiesResult
    """

    def test_entities_result_serialization(self):
        """
        Test serialization/deserialization for EntitiesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        entity_mention_model = {} # EntityMention
        entity_mention_model['text'] = 'testString'
        entity_mention_model['location'] = [38]
        entity_mention_model['confidence'] = 72.5

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 72.5
        emotion_scores_model['disgust'] = 72.5
        emotion_scores_model['fear'] = 72.5
        emotion_scores_model['joy'] = 72.5
        emotion_scores_model['sadness'] = 72.5

        feature_sentiment_results_model = {} # FeatureSentimentResults
        feature_sentiment_results_model['score'] = 72.5

        disambiguation_result_model = {} # DisambiguationResult
        disambiguation_result_model['name'] = 'testString'
        disambiguation_result_model['dbpedia_resource'] = 'testString'
        disambiguation_result_model['subtype'] = ['testString']

        # Construct a json representation of a EntitiesResult model
        entities_result_model_json = {}
        entities_result_model_json['type'] = 'testString'
        entities_result_model_json['text'] = 'testString'
        entities_result_model_json['relevance'] = 72.5
        entities_result_model_json['confidence'] = 72.5
        entities_result_model_json['mentions'] = [entity_mention_model]
        entities_result_model_json['count'] = 38
        entities_result_model_json['emotion'] = emotion_scores_model
        entities_result_model_json['sentiment'] = feature_sentiment_results_model
        entities_result_model_json['disambiguation'] = disambiguation_result_model

        # Construct a model instance of EntitiesResult by calling from_dict on the json representation
        entities_result_model = EntitiesResult.from_dict(entities_result_model_json)
        assert entities_result_model != False

        # Construct a model instance of EntitiesResult by calling from_dict on the json representation
        entities_result_model_dict = EntitiesResult.from_dict(entities_result_model_json).__dict__
        entities_result_model2 = EntitiesResult(**entities_result_model_dict)

        # Verify the model instances are equivalent
        assert entities_result_model == entities_result_model2

        # Convert model instance back to dict and verify no loss of data
        entities_result_model_json2 = entities_result_model.to_dict()
        assert entities_result_model_json2 == entities_result_model_json

class TestEntityMention():
    """
    Test Class for EntityMention
    """

    def test_entity_mention_serialization(self):
        """
        Test serialization/deserialization for EntityMention
        """

        # Construct a json representation of a EntityMention model
        entity_mention_model_json = {}
        entity_mention_model_json['text'] = 'testString'
        entity_mention_model_json['location'] = [38]
        entity_mention_model_json['confidence'] = 72.5

        # Construct a model instance of EntityMention by calling from_dict on the json representation
        entity_mention_model = EntityMention.from_dict(entity_mention_model_json)
        assert entity_mention_model != False

        # Construct a model instance of EntityMention by calling from_dict on the json representation
        entity_mention_model_dict = EntityMention.from_dict(entity_mention_model_json).__dict__
        entity_mention_model2 = EntityMention(**entity_mention_model_dict)

        # Verify the model instances are equivalent
        assert entity_mention_model == entity_mention_model2

        # Convert model instance back to dict and verify no loss of data
        entity_mention_model_json2 = entity_mention_model.to_dict()
        assert entity_mention_model_json2 == entity_mention_model_json

class TestFeatureSentimentResults():
    """
    Test Class for FeatureSentimentResults
    """

    def test_feature_sentiment_results_serialization(self):
        """
        Test serialization/deserialization for FeatureSentimentResults
        """

        # Construct a json representation of a FeatureSentimentResults model
        feature_sentiment_results_model_json = {}
        feature_sentiment_results_model_json['score'] = 72.5

        # Construct a model instance of FeatureSentimentResults by calling from_dict on the json representation
        feature_sentiment_results_model = FeatureSentimentResults.from_dict(feature_sentiment_results_model_json)
        assert feature_sentiment_results_model != False

        # Construct a model instance of FeatureSentimentResults by calling from_dict on the json representation
        feature_sentiment_results_model_dict = FeatureSentimentResults.from_dict(feature_sentiment_results_model_json).__dict__
        feature_sentiment_results_model2 = FeatureSentimentResults(**feature_sentiment_results_model_dict)

        # Verify the model instances are equivalent
        assert feature_sentiment_results_model == feature_sentiment_results_model2

        # Convert model instance back to dict and verify no loss of data
        feature_sentiment_results_model_json2 = feature_sentiment_results_model.to_dict()
        assert feature_sentiment_results_model_json2 == feature_sentiment_results_model_json

class TestFeatures():
    """
    Test Class for Features
    """

    def test_features_serialization(self):
        """
        Test serialization/deserialization for Features
        """

        # Construct dict forms of any model objects needed in order to build this model.

        concepts_options_model = {} # ConceptsOptions
        concepts_options_model['limit'] = 50

        emotion_options_model = {} # EmotionOptions
        emotion_options_model['document'] = True
        emotion_options_model['targets'] = ['testString']

        entities_options_model = {} # EntitiesOptions
        entities_options_model['limit'] = 250
        entities_options_model['mentions'] = True
        entities_options_model['model'] = 'testString'
        entities_options_model['sentiment'] = True
        entities_options_model['emotion'] = True

        keywords_options_model = {} # KeywordsOptions
        keywords_options_model['limit'] = 250
        keywords_options_model['sentiment'] = True
        keywords_options_model['emotion'] = True

        relations_options_model = {} # RelationsOptions
        relations_options_model['model'] = 'testString'

        semantic_roles_options_model = {} # SemanticRolesOptions
        semantic_roles_options_model['limit'] = 38
        semantic_roles_options_model['keywords'] = True
        semantic_roles_options_model['entities'] = True

        sentiment_options_model = {} # SentimentOptions
        sentiment_options_model['document'] = True
        sentiment_options_model['targets'] = ['testString']

        categories_options_model = {} # CategoriesOptions
        categories_options_model['explanation'] = True
        categories_options_model['limit'] = 10
        categories_options_model['model'] = 'testString'

        syntax_options_tokens_model = {} # SyntaxOptionsTokens
        syntax_options_tokens_model['lemma'] = True
        syntax_options_tokens_model['part_of_speech'] = True

        syntax_options_model = {} # SyntaxOptions
        syntax_options_model['tokens'] = syntax_options_tokens_model
        syntax_options_model['sentences'] = True

        # Construct a json representation of a Features model
        features_model_json = {}
        features_model_json['concepts'] = concepts_options_model
        features_model_json['emotion'] = emotion_options_model
        features_model_json['entities'] = entities_options_model
        features_model_json['keywords'] = keywords_options_model
        features_model_json['metadata'] = { 'foo': 'bar' }
        features_model_json['relations'] = relations_options_model
        features_model_json['semantic_roles'] = semantic_roles_options_model
        features_model_json['sentiment'] = sentiment_options_model
        features_model_json['categories'] = categories_options_model
        features_model_json['syntax'] = syntax_options_model

        # Construct a model instance of Features by calling from_dict on the json representation
        features_model = Features.from_dict(features_model_json)
        assert features_model != False

        # Construct a model instance of Features by calling from_dict on the json representation
        features_model_dict = Features.from_dict(features_model_json).__dict__
        features_model2 = Features(**features_model_dict)

        # Verify the model instances are equivalent
        assert features_model == features_model2

        # Convert model instance back to dict and verify no loss of data
        features_model_json2 = features_model.to_dict()
        assert features_model_json2 == features_model_json

class TestFeaturesResultsMetadata():
    """
    Test Class for FeaturesResultsMetadata
    """

    def test_features_results_metadata_serialization(self):
        """
        Test serialization/deserialization for FeaturesResultsMetadata
        """

        # Construct dict forms of any model objects needed in order to build this model.

        author_model = {} # Author
        author_model['name'] = 'testString'

        feed_model = {} # Feed
        feed_model['link'] = 'testString'

        # Construct a json representation of a FeaturesResultsMetadata model
        features_results_metadata_model_json = {}
        features_results_metadata_model_json['authors'] = [author_model]
        features_results_metadata_model_json['publication_date'] = 'testString'
        features_results_metadata_model_json['title'] = 'testString'
        features_results_metadata_model_json['image'] = 'testString'
        features_results_metadata_model_json['feeds'] = [feed_model]

        # Construct a model instance of FeaturesResultsMetadata by calling from_dict on the json representation
        features_results_metadata_model = FeaturesResultsMetadata.from_dict(features_results_metadata_model_json)
        assert features_results_metadata_model != False

        # Construct a model instance of FeaturesResultsMetadata by calling from_dict on the json representation
        features_results_metadata_model_dict = FeaturesResultsMetadata.from_dict(features_results_metadata_model_json).__dict__
        features_results_metadata_model2 = FeaturesResultsMetadata(**features_results_metadata_model_dict)

        # Verify the model instances are equivalent
        assert features_results_metadata_model == features_results_metadata_model2

        # Convert model instance back to dict and verify no loss of data
        features_results_metadata_model_json2 = features_results_metadata_model.to_dict()
        assert features_results_metadata_model_json2 == features_results_metadata_model_json

class TestFeed():
    """
    Test Class for Feed
    """

    def test_feed_serialization(self):
        """
        Test serialization/deserialization for Feed
        """

        # Construct a json representation of a Feed model
        feed_model_json = {}
        feed_model_json['link'] = 'testString'

        # Construct a model instance of Feed by calling from_dict on the json representation
        feed_model = Feed.from_dict(feed_model_json)
        assert feed_model != False

        # Construct a model instance of Feed by calling from_dict on the json representation
        feed_model_dict = Feed.from_dict(feed_model_json).__dict__
        feed_model2 = Feed(**feed_model_dict)

        # Verify the model instances are equivalent
        assert feed_model == feed_model2

        # Convert model instance back to dict and verify no loss of data
        feed_model_json2 = feed_model.to_dict()
        assert feed_model_json2 == feed_model_json

class TestKeywordsOptions():
    """
    Test Class for KeywordsOptions
    """

    def test_keywords_options_serialization(self):
        """
        Test serialization/deserialization for KeywordsOptions
        """

        # Construct a json representation of a KeywordsOptions model
        keywords_options_model_json = {}
        keywords_options_model_json['limit'] = 250
        keywords_options_model_json['sentiment'] = True
        keywords_options_model_json['emotion'] = True

        # Construct a model instance of KeywordsOptions by calling from_dict on the json representation
        keywords_options_model = KeywordsOptions.from_dict(keywords_options_model_json)
        assert keywords_options_model != False

        # Construct a model instance of KeywordsOptions by calling from_dict on the json representation
        keywords_options_model_dict = KeywordsOptions.from_dict(keywords_options_model_json).__dict__
        keywords_options_model2 = KeywordsOptions(**keywords_options_model_dict)

        # Verify the model instances are equivalent
        assert keywords_options_model == keywords_options_model2

        # Convert model instance back to dict and verify no loss of data
        keywords_options_model_json2 = keywords_options_model.to_dict()
        assert keywords_options_model_json2 == keywords_options_model_json

class TestKeywordsResult():
    """
    Test Class for KeywordsResult
    """

    def test_keywords_result_serialization(self):
        """
        Test serialization/deserialization for KeywordsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 72.5
        emotion_scores_model['disgust'] = 72.5
        emotion_scores_model['fear'] = 72.5
        emotion_scores_model['joy'] = 72.5
        emotion_scores_model['sadness'] = 72.5

        feature_sentiment_results_model = {} # FeatureSentimentResults
        feature_sentiment_results_model['score'] = 72.5

        # Construct a json representation of a KeywordsResult model
        keywords_result_model_json = {}
        keywords_result_model_json['count'] = 38
        keywords_result_model_json['relevance'] = 72.5
        keywords_result_model_json['text'] = 'testString'
        keywords_result_model_json['emotion'] = emotion_scores_model
        keywords_result_model_json['sentiment'] = feature_sentiment_results_model

        # Construct a model instance of KeywordsResult by calling from_dict on the json representation
        keywords_result_model = KeywordsResult.from_dict(keywords_result_model_json)
        assert keywords_result_model != False

        # Construct a model instance of KeywordsResult by calling from_dict on the json representation
        keywords_result_model_dict = KeywordsResult.from_dict(keywords_result_model_json).__dict__
        keywords_result_model2 = KeywordsResult(**keywords_result_model_dict)

        # Verify the model instances are equivalent
        assert keywords_result_model == keywords_result_model2

        # Convert model instance back to dict and verify no loss of data
        keywords_result_model_json2 = keywords_result_model.to_dict()
        assert keywords_result_model_json2 == keywords_result_model_json

class TestListModelsResults():
    """
    Test Class for ListModelsResults
    """

    def test_list_models_results_serialization(self):
        """
        Test serialization/deserialization for ListModelsResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        model_model = {} # Model
        model_model['status'] = 'starting'
        model_model['model_id'] = 'testString'
        model_model['language'] = 'testString'
        model_model['description'] = 'testString'
        model_model['workspace_id'] = 'testString'
        model_model['model_version'] = 'testString'
        model_model['version'] = 'testString'
        model_model['version_description'] = 'testString'
        model_model['created'] = '2020-01-28T18:40:40.123456Z'

        # Construct a json representation of a ListModelsResults model
        list_models_results_model_json = {}
        list_models_results_model_json['models'] = [model_model]

        # Construct a model instance of ListModelsResults by calling from_dict on the json representation
        list_models_results_model = ListModelsResults.from_dict(list_models_results_model_json)
        assert list_models_results_model != False

        # Construct a model instance of ListModelsResults by calling from_dict on the json representation
        list_models_results_model_dict = ListModelsResults.from_dict(list_models_results_model_json).__dict__
        list_models_results_model2 = ListModelsResults(**list_models_results_model_dict)

        # Verify the model instances are equivalent
        assert list_models_results_model == list_models_results_model2

        # Convert model instance back to dict and verify no loss of data
        list_models_results_model_json2 = list_models_results_model.to_dict()
        assert list_models_results_model_json2 == list_models_results_model_json

class TestModel():
    """
    Test Class for Model
    """

    def test_model_serialization(self):
        """
        Test serialization/deserialization for Model
        """

        # Construct a json representation of a Model model
        model_model_json = {}
        model_model_json['status'] = 'starting'
        model_model_json['model_id'] = 'testString'
        model_model_json['language'] = 'testString'
        model_model_json['description'] = 'testString'
        model_model_json['workspace_id'] = 'testString'
        model_model_json['model_version'] = 'testString'
        model_model_json['version'] = 'testString'
        model_model_json['version_description'] = 'testString'
        model_model_json['created'] = '2020-01-28T18:40:40.123456Z'

        # Construct a model instance of Model by calling from_dict on the json representation
        model_model = Model.from_dict(model_model_json)
        assert model_model != False

        # Construct a model instance of Model by calling from_dict on the json representation
        model_model_dict = Model.from_dict(model_model_json).__dict__
        model_model2 = Model(**model_model_dict)

        # Verify the model instances are equivalent
        assert model_model == model_model2

        # Convert model instance back to dict and verify no loss of data
        model_model_json2 = model_model.to_dict()
        assert model_model_json2 == model_model_json

class TestRelationArgument():
    """
    Test Class for RelationArgument
    """

    def test_relation_argument_serialization(self):
        """
        Test serialization/deserialization for RelationArgument
        """

        # Construct dict forms of any model objects needed in order to build this model.

        relation_entity_model = {} # RelationEntity
        relation_entity_model['text'] = 'testString'
        relation_entity_model['type'] = 'testString'

        # Construct a json representation of a RelationArgument model
        relation_argument_model_json = {}
        relation_argument_model_json['entities'] = [relation_entity_model]
        relation_argument_model_json['location'] = [38]
        relation_argument_model_json['text'] = 'testString'

        # Construct a model instance of RelationArgument by calling from_dict on the json representation
        relation_argument_model = RelationArgument.from_dict(relation_argument_model_json)
        assert relation_argument_model != False

        # Construct a model instance of RelationArgument by calling from_dict on the json representation
        relation_argument_model_dict = RelationArgument.from_dict(relation_argument_model_json).__dict__
        relation_argument_model2 = RelationArgument(**relation_argument_model_dict)

        # Verify the model instances are equivalent
        assert relation_argument_model == relation_argument_model2

        # Convert model instance back to dict and verify no loss of data
        relation_argument_model_json2 = relation_argument_model.to_dict()
        assert relation_argument_model_json2 == relation_argument_model_json

class TestRelationEntity():
    """
    Test Class for RelationEntity
    """

    def test_relation_entity_serialization(self):
        """
        Test serialization/deserialization for RelationEntity
        """

        # Construct a json representation of a RelationEntity model
        relation_entity_model_json = {}
        relation_entity_model_json['text'] = 'testString'
        relation_entity_model_json['type'] = 'testString'

        # Construct a model instance of RelationEntity by calling from_dict on the json representation
        relation_entity_model = RelationEntity.from_dict(relation_entity_model_json)
        assert relation_entity_model != False

        # Construct a model instance of RelationEntity by calling from_dict on the json representation
        relation_entity_model_dict = RelationEntity.from_dict(relation_entity_model_json).__dict__
        relation_entity_model2 = RelationEntity(**relation_entity_model_dict)

        # Verify the model instances are equivalent
        assert relation_entity_model == relation_entity_model2

        # Convert model instance back to dict and verify no loss of data
        relation_entity_model_json2 = relation_entity_model.to_dict()
        assert relation_entity_model_json2 == relation_entity_model_json

class TestRelationsOptions():
    """
    Test Class for RelationsOptions
    """

    def test_relations_options_serialization(self):
        """
        Test serialization/deserialization for RelationsOptions
        """

        # Construct a json representation of a RelationsOptions model
        relations_options_model_json = {}
        relations_options_model_json['model'] = 'testString'

        # Construct a model instance of RelationsOptions by calling from_dict on the json representation
        relations_options_model = RelationsOptions.from_dict(relations_options_model_json)
        assert relations_options_model != False

        # Construct a model instance of RelationsOptions by calling from_dict on the json representation
        relations_options_model_dict = RelationsOptions.from_dict(relations_options_model_json).__dict__
        relations_options_model2 = RelationsOptions(**relations_options_model_dict)

        # Verify the model instances are equivalent
        assert relations_options_model == relations_options_model2

        # Convert model instance back to dict and verify no loss of data
        relations_options_model_json2 = relations_options_model.to_dict()
        assert relations_options_model_json2 == relations_options_model_json

class TestRelationsResult():
    """
    Test Class for RelationsResult
    """

    def test_relations_result_serialization(self):
        """
        Test serialization/deserialization for RelationsResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        relation_entity_model = {} # RelationEntity
        relation_entity_model['text'] = 'testString'
        relation_entity_model['type'] = 'testString'

        relation_argument_model = {} # RelationArgument
        relation_argument_model['entities'] = [relation_entity_model]
        relation_argument_model['location'] = [38]
        relation_argument_model['text'] = 'testString'

        # Construct a json representation of a RelationsResult model
        relations_result_model_json = {}
        relations_result_model_json['score'] = 72.5
        relations_result_model_json['sentence'] = 'testString'
        relations_result_model_json['type'] = 'testString'
        relations_result_model_json['arguments'] = [relation_argument_model]

        # Construct a model instance of RelationsResult by calling from_dict on the json representation
        relations_result_model = RelationsResult.from_dict(relations_result_model_json)
        assert relations_result_model != False

        # Construct a model instance of RelationsResult by calling from_dict on the json representation
        relations_result_model_dict = RelationsResult.from_dict(relations_result_model_json).__dict__
        relations_result_model2 = RelationsResult(**relations_result_model_dict)

        # Verify the model instances are equivalent
        assert relations_result_model == relations_result_model2

        # Convert model instance back to dict and verify no loss of data
        relations_result_model_json2 = relations_result_model.to_dict()
        assert relations_result_model_json2 == relations_result_model_json

class TestSemanticRolesEntity():
    """
    Test Class for SemanticRolesEntity
    """

    def test_semantic_roles_entity_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesEntity
        """

        # Construct a json representation of a SemanticRolesEntity model
        semantic_roles_entity_model_json = {}
        semantic_roles_entity_model_json['type'] = 'testString'
        semantic_roles_entity_model_json['text'] = 'testString'

        # Construct a model instance of SemanticRolesEntity by calling from_dict on the json representation
        semantic_roles_entity_model = SemanticRolesEntity.from_dict(semantic_roles_entity_model_json)
        assert semantic_roles_entity_model != False

        # Construct a model instance of SemanticRolesEntity by calling from_dict on the json representation
        semantic_roles_entity_model_dict = SemanticRolesEntity.from_dict(semantic_roles_entity_model_json).__dict__
        semantic_roles_entity_model2 = SemanticRolesEntity(**semantic_roles_entity_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_entity_model == semantic_roles_entity_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_entity_model_json2 = semantic_roles_entity_model.to_dict()
        assert semantic_roles_entity_model_json2 == semantic_roles_entity_model_json

class TestSemanticRolesKeyword():
    """
    Test Class for SemanticRolesKeyword
    """

    def test_semantic_roles_keyword_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesKeyword
        """

        # Construct a json representation of a SemanticRolesKeyword model
        semantic_roles_keyword_model_json = {}
        semantic_roles_keyword_model_json['text'] = 'testString'

        # Construct a model instance of SemanticRolesKeyword by calling from_dict on the json representation
        semantic_roles_keyword_model = SemanticRolesKeyword.from_dict(semantic_roles_keyword_model_json)
        assert semantic_roles_keyword_model != False

        # Construct a model instance of SemanticRolesKeyword by calling from_dict on the json representation
        semantic_roles_keyword_model_dict = SemanticRolesKeyword.from_dict(semantic_roles_keyword_model_json).__dict__
        semantic_roles_keyword_model2 = SemanticRolesKeyword(**semantic_roles_keyword_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_keyword_model == semantic_roles_keyword_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_keyword_model_json2 = semantic_roles_keyword_model.to_dict()
        assert semantic_roles_keyword_model_json2 == semantic_roles_keyword_model_json

class TestSemanticRolesOptions():
    """
    Test Class for SemanticRolesOptions
    """

    def test_semantic_roles_options_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesOptions
        """

        # Construct a json representation of a SemanticRolesOptions model
        semantic_roles_options_model_json = {}
        semantic_roles_options_model_json['limit'] = 38
        semantic_roles_options_model_json['keywords'] = True
        semantic_roles_options_model_json['entities'] = True

        # Construct a model instance of SemanticRolesOptions by calling from_dict on the json representation
        semantic_roles_options_model = SemanticRolesOptions.from_dict(semantic_roles_options_model_json)
        assert semantic_roles_options_model != False

        # Construct a model instance of SemanticRolesOptions by calling from_dict on the json representation
        semantic_roles_options_model_dict = SemanticRolesOptions.from_dict(semantic_roles_options_model_json).__dict__
        semantic_roles_options_model2 = SemanticRolesOptions(**semantic_roles_options_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_options_model == semantic_roles_options_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_options_model_json2 = semantic_roles_options_model.to_dict()
        assert semantic_roles_options_model_json2 == semantic_roles_options_model_json

class TestSemanticRolesResult():
    """
    Test Class for SemanticRolesResult
    """

    def test_semantic_roles_result_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        semantic_roles_entity_model = {} # SemanticRolesEntity
        semantic_roles_entity_model['type'] = 'testString'
        semantic_roles_entity_model['text'] = 'testString'

        semantic_roles_keyword_model = {} # SemanticRolesKeyword
        semantic_roles_keyword_model['text'] = 'testString'

        semantic_roles_result_subject_model = {} # SemanticRolesResultSubject
        semantic_roles_result_subject_model['text'] = 'testString'
        semantic_roles_result_subject_model['entities'] = [semantic_roles_entity_model]
        semantic_roles_result_subject_model['keywords'] = [semantic_roles_keyword_model]

        semantic_roles_verb_model = {} # SemanticRolesVerb
        semantic_roles_verb_model['text'] = 'testString'
        semantic_roles_verb_model['tense'] = 'testString'

        semantic_roles_result_action_model = {} # SemanticRolesResultAction
        semantic_roles_result_action_model['text'] = 'testString'
        semantic_roles_result_action_model['normalized'] = 'testString'
        semantic_roles_result_action_model['verb'] = semantic_roles_verb_model

        semantic_roles_result_object_model = {} # SemanticRolesResultObject
        semantic_roles_result_object_model['text'] = 'testString'
        semantic_roles_result_object_model['keywords'] = [semantic_roles_keyword_model]

        # Construct a json representation of a SemanticRolesResult model
        semantic_roles_result_model_json = {}
        semantic_roles_result_model_json['sentence'] = 'testString'
        semantic_roles_result_model_json['subject'] = semantic_roles_result_subject_model
        semantic_roles_result_model_json['action'] = semantic_roles_result_action_model
        semantic_roles_result_model_json['object'] = semantic_roles_result_object_model

        # Construct a model instance of SemanticRolesResult by calling from_dict on the json representation
        semantic_roles_result_model = SemanticRolesResult.from_dict(semantic_roles_result_model_json)
        assert semantic_roles_result_model != False

        # Construct a model instance of SemanticRolesResult by calling from_dict on the json representation
        semantic_roles_result_model_dict = SemanticRolesResult.from_dict(semantic_roles_result_model_json).__dict__
        semantic_roles_result_model2 = SemanticRolesResult(**semantic_roles_result_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_result_model == semantic_roles_result_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_result_model_json2 = semantic_roles_result_model.to_dict()
        assert semantic_roles_result_model_json2 == semantic_roles_result_model_json

class TestSemanticRolesResultAction():
    """
    Test Class for SemanticRolesResultAction
    """

    def test_semantic_roles_result_action_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesResultAction
        """

        # Construct dict forms of any model objects needed in order to build this model.

        semantic_roles_verb_model = {} # SemanticRolesVerb
        semantic_roles_verb_model['text'] = 'testString'
        semantic_roles_verb_model['tense'] = 'testString'

        # Construct a json representation of a SemanticRolesResultAction model
        semantic_roles_result_action_model_json = {}
        semantic_roles_result_action_model_json['text'] = 'testString'
        semantic_roles_result_action_model_json['normalized'] = 'testString'
        semantic_roles_result_action_model_json['verb'] = semantic_roles_verb_model

        # Construct a model instance of SemanticRolesResultAction by calling from_dict on the json representation
        semantic_roles_result_action_model = SemanticRolesResultAction.from_dict(semantic_roles_result_action_model_json)
        assert semantic_roles_result_action_model != False

        # Construct a model instance of SemanticRolesResultAction by calling from_dict on the json representation
        semantic_roles_result_action_model_dict = SemanticRolesResultAction.from_dict(semantic_roles_result_action_model_json).__dict__
        semantic_roles_result_action_model2 = SemanticRolesResultAction(**semantic_roles_result_action_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_result_action_model == semantic_roles_result_action_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_result_action_model_json2 = semantic_roles_result_action_model.to_dict()
        assert semantic_roles_result_action_model_json2 == semantic_roles_result_action_model_json

class TestSemanticRolesResultObject():
    """
    Test Class for SemanticRolesResultObject
    """

    def test_semantic_roles_result_object_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesResultObject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        semantic_roles_keyword_model = {} # SemanticRolesKeyword
        semantic_roles_keyword_model['text'] = 'testString'

        # Construct a json representation of a SemanticRolesResultObject model
        semantic_roles_result_object_model_json = {}
        semantic_roles_result_object_model_json['text'] = 'testString'
        semantic_roles_result_object_model_json['keywords'] = [semantic_roles_keyword_model]

        # Construct a model instance of SemanticRolesResultObject by calling from_dict on the json representation
        semantic_roles_result_object_model = SemanticRolesResultObject.from_dict(semantic_roles_result_object_model_json)
        assert semantic_roles_result_object_model != False

        # Construct a model instance of SemanticRolesResultObject by calling from_dict on the json representation
        semantic_roles_result_object_model_dict = SemanticRolesResultObject.from_dict(semantic_roles_result_object_model_json).__dict__
        semantic_roles_result_object_model2 = SemanticRolesResultObject(**semantic_roles_result_object_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_result_object_model == semantic_roles_result_object_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_result_object_model_json2 = semantic_roles_result_object_model.to_dict()
        assert semantic_roles_result_object_model_json2 == semantic_roles_result_object_model_json

class TestSemanticRolesResultSubject():
    """
    Test Class for SemanticRolesResultSubject
    """

    def test_semantic_roles_result_subject_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesResultSubject
        """

        # Construct dict forms of any model objects needed in order to build this model.

        semantic_roles_entity_model = {} # SemanticRolesEntity
        semantic_roles_entity_model['type'] = 'testString'
        semantic_roles_entity_model['text'] = 'testString'

        semantic_roles_keyword_model = {} # SemanticRolesKeyword
        semantic_roles_keyword_model['text'] = 'testString'

        # Construct a json representation of a SemanticRolesResultSubject model
        semantic_roles_result_subject_model_json = {}
        semantic_roles_result_subject_model_json['text'] = 'testString'
        semantic_roles_result_subject_model_json['entities'] = [semantic_roles_entity_model]
        semantic_roles_result_subject_model_json['keywords'] = [semantic_roles_keyword_model]

        # Construct a model instance of SemanticRolesResultSubject by calling from_dict on the json representation
        semantic_roles_result_subject_model = SemanticRolesResultSubject.from_dict(semantic_roles_result_subject_model_json)
        assert semantic_roles_result_subject_model != False

        # Construct a model instance of SemanticRolesResultSubject by calling from_dict on the json representation
        semantic_roles_result_subject_model_dict = SemanticRolesResultSubject.from_dict(semantic_roles_result_subject_model_json).__dict__
        semantic_roles_result_subject_model2 = SemanticRolesResultSubject(**semantic_roles_result_subject_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_result_subject_model == semantic_roles_result_subject_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_result_subject_model_json2 = semantic_roles_result_subject_model.to_dict()
        assert semantic_roles_result_subject_model_json2 == semantic_roles_result_subject_model_json

class TestSemanticRolesVerb():
    """
    Test Class for SemanticRolesVerb
    """

    def test_semantic_roles_verb_serialization(self):
        """
        Test serialization/deserialization for SemanticRolesVerb
        """

        # Construct a json representation of a SemanticRolesVerb model
        semantic_roles_verb_model_json = {}
        semantic_roles_verb_model_json['text'] = 'testString'
        semantic_roles_verb_model_json['tense'] = 'testString'

        # Construct a model instance of SemanticRolesVerb by calling from_dict on the json representation
        semantic_roles_verb_model = SemanticRolesVerb.from_dict(semantic_roles_verb_model_json)
        assert semantic_roles_verb_model != False

        # Construct a model instance of SemanticRolesVerb by calling from_dict on the json representation
        semantic_roles_verb_model_dict = SemanticRolesVerb.from_dict(semantic_roles_verb_model_json).__dict__
        semantic_roles_verb_model2 = SemanticRolesVerb(**semantic_roles_verb_model_dict)

        # Verify the model instances are equivalent
        assert semantic_roles_verb_model == semantic_roles_verb_model2

        # Convert model instance back to dict and verify no loss of data
        semantic_roles_verb_model_json2 = semantic_roles_verb_model.to_dict()
        assert semantic_roles_verb_model_json2 == semantic_roles_verb_model_json

class TestSentenceResult():
    """
    Test Class for SentenceResult
    """

    def test_sentence_result_serialization(self):
        """
        Test serialization/deserialization for SentenceResult
        """

        # Construct a json representation of a SentenceResult model
        sentence_result_model_json = {}
        sentence_result_model_json['text'] = 'testString'
        sentence_result_model_json['location'] = [38]

        # Construct a model instance of SentenceResult by calling from_dict on the json representation
        sentence_result_model = SentenceResult.from_dict(sentence_result_model_json)
        assert sentence_result_model != False

        # Construct a model instance of SentenceResult by calling from_dict on the json representation
        sentence_result_model_dict = SentenceResult.from_dict(sentence_result_model_json).__dict__
        sentence_result_model2 = SentenceResult(**sentence_result_model_dict)

        # Verify the model instances are equivalent
        assert sentence_result_model == sentence_result_model2

        # Convert model instance back to dict and verify no loss of data
        sentence_result_model_json2 = sentence_result_model.to_dict()
        assert sentence_result_model_json2 == sentence_result_model_json

class TestSentimentOptions():
    """
    Test Class for SentimentOptions
    """

    def test_sentiment_options_serialization(self):
        """
        Test serialization/deserialization for SentimentOptions
        """

        # Construct a json representation of a SentimentOptions model
        sentiment_options_model_json = {}
        sentiment_options_model_json['document'] = True
        sentiment_options_model_json['targets'] = ['testString']

        # Construct a model instance of SentimentOptions by calling from_dict on the json representation
        sentiment_options_model = SentimentOptions.from_dict(sentiment_options_model_json)
        assert sentiment_options_model != False

        # Construct a model instance of SentimentOptions by calling from_dict on the json representation
        sentiment_options_model_dict = SentimentOptions.from_dict(sentiment_options_model_json).__dict__
        sentiment_options_model2 = SentimentOptions(**sentiment_options_model_dict)

        # Verify the model instances are equivalent
        assert sentiment_options_model == sentiment_options_model2

        # Convert model instance back to dict and verify no loss of data
        sentiment_options_model_json2 = sentiment_options_model.to_dict()
        assert sentiment_options_model_json2 == sentiment_options_model_json

class TestSentimentResult():
    """
    Test Class for SentimentResult
    """

    def test_sentiment_result_serialization(self):
        """
        Test serialization/deserialization for SentimentResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        document_sentiment_results_model = {} # DocumentSentimentResults
        document_sentiment_results_model['label'] = 'positive'
        document_sentiment_results_model['score'] = 0.127034

        targeted_sentiment_results_model = {} # TargetedSentimentResults
        targeted_sentiment_results_model['text'] = 'stocks'
        targeted_sentiment_results_model['score'] = 0.279964

        # Construct a json representation of a SentimentResult model
        sentiment_result_model_json = {}
        sentiment_result_model_json['document'] = document_sentiment_results_model
        sentiment_result_model_json['targets'] = [targeted_sentiment_results_model]

        # Construct a model instance of SentimentResult by calling from_dict on the json representation
        sentiment_result_model = SentimentResult.from_dict(sentiment_result_model_json)
        assert sentiment_result_model != False

        # Construct a model instance of SentimentResult by calling from_dict on the json representation
        sentiment_result_model_dict = SentimentResult.from_dict(sentiment_result_model_json).__dict__
        sentiment_result_model2 = SentimentResult(**sentiment_result_model_dict)

        # Verify the model instances are equivalent
        assert sentiment_result_model == sentiment_result_model2

        # Convert model instance back to dict and verify no loss of data
        sentiment_result_model_json2 = sentiment_result_model.to_dict()
        assert sentiment_result_model_json2 == sentiment_result_model_json

class TestSyntaxOptions():
    """
    Test Class for SyntaxOptions
    """

    def test_syntax_options_serialization(self):
        """
        Test serialization/deserialization for SyntaxOptions
        """

        # Construct dict forms of any model objects needed in order to build this model.

        syntax_options_tokens_model = {} # SyntaxOptionsTokens
        syntax_options_tokens_model['lemma'] = True
        syntax_options_tokens_model['part_of_speech'] = True

        # Construct a json representation of a SyntaxOptions model
        syntax_options_model_json = {}
        syntax_options_model_json['tokens'] = syntax_options_tokens_model
        syntax_options_model_json['sentences'] = True

        # Construct a model instance of SyntaxOptions by calling from_dict on the json representation
        syntax_options_model = SyntaxOptions.from_dict(syntax_options_model_json)
        assert syntax_options_model != False

        # Construct a model instance of SyntaxOptions by calling from_dict on the json representation
        syntax_options_model_dict = SyntaxOptions.from_dict(syntax_options_model_json).__dict__
        syntax_options_model2 = SyntaxOptions(**syntax_options_model_dict)

        # Verify the model instances are equivalent
        assert syntax_options_model == syntax_options_model2

        # Convert model instance back to dict and verify no loss of data
        syntax_options_model_json2 = syntax_options_model.to_dict()
        assert syntax_options_model_json2 == syntax_options_model_json

class TestSyntaxOptionsTokens():
    """
    Test Class for SyntaxOptionsTokens
    """

    def test_syntax_options_tokens_serialization(self):
        """
        Test serialization/deserialization for SyntaxOptionsTokens
        """

        # Construct a json representation of a SyntaxOptionsTokens model
        syntax_options_tokens_model_json = {}
        syntax_options_tokens_model_json['lemma'] = True
        syntax_options_tokens_model_json['part_of_speech'] = True

        # Construct a model instance of SyntaxOptionsTokens by calling from_dict on the json representation
        syntax_options_tokens_model = SyntaxOptionsTokens.from_dict(syntax_options_tokens_model_json)
        assert syntax_options_tokens_model != False

        # Construct a model instance of SyntaxOptionsTokens by calling from_dict on the json representation
        syntax_options_tokens_model_dict = SyntaxOptionsTokens.from_dict(syntax_options_tokens_model_json).__dict__
        syntax_options_tokens_model2 = SyntaxOptionsTokens(**syntax_options_tokens_model_dict)

        # Verify the model instances are equivalent
        assert syntax_options_tokens_model == syntax_options_tokens_model2

        # Convert model instance back to dict and verify no loss of data
        syntax_options_tokens_model_json2 = syntax_options_tokens_model.to_dict()
        assert syntax_options_tokens_model_json2 == syntax_options_tokens_model_json

class TestSyntaxResult():
    """
    Test Class for SyntaxResult
    """

    def test_syntax_result_serialization(self):
        """
        Test serialization/deserialization for SyntaxResult
        """

        # Construct dict forms of any model objects needed in order to build this model.

        token_result_model = {} # TokenResult
        token_result_model['text'] = 'testString'
        token_result_model['part_of_speech'] = 'ADJ'
        token_result_model['location'] = [38]
        token_result_model['lemma'] = 'testString'

        sentence_result_model = {} # SentenceResult
        sentence_result_model['text'] = 'testString'
        sentence_result_model['location'] = [38]

        # Construct a json representation of a SyntaxResult model
        syntax_result_model_json = {}
        syntax_result_model_json['tokens'] = [token_result_model]
        syntax_result_model_json['sentences'] = [sentence_result_model]

        # Construct a model instance of SyntaxResult by calling from_dict on the json representation
        syntax_result_model = SyntaxResult.from_dict(syntax_result_model_json)
        assert syntax_result_model != False

        # Construct a model instance of SyntaxResult by calling from_dict on the json representation
        syntax_result_model_dict = SyntaxResult.from_dict(syntax_result_model_json).__dict__
        syntax_result_model2 = SyntaxResult(**syntax_result_model_dict)

        # Verify the model instances are equivalent
        assert syntax_result_model == syntax_result_model2

        # Convert model instance back to dict and verify no loss of data
        syntax_result_model_json2 = syntax_result_model.to_dict()
        assert syntax_result_model_json2 == syntax_result_model_json

class TestTargetedEmotionResults():
    """
    Test Class for TargetedEmotionResults
    """

    def test_targeted_emotion_results_serialization(self):
        """
        Test serialization/deserialization for TargetedEmotionResults
        """

        # Construct dict forms of any model objects needed in order to build this model.

        emotion_scores_model = {} # EmotionScores
        emotion_scores_model['anger'] = 72.5
        emotion_scores_model['disgust'] = 72.5
        emotion_scores_model['fear'] = 72.5
        emotion_scores_model['joy'] = 72.5
        emotion_scores_model['sadness'] = 72.5

        # Construct a json representation of a TargetedEmotionResults model
        targeted_emotion_results_model_json = {}
        targeted_emotion_results_model_json['text'] = 'testString'
        targeted_emotion_results_model_json['emotion'] = emotion_scores_model

        # Construct a model instance of TargetedEmotionResults by calling from_dict on the json representation
        targeted_emotion_results_model = TargetedEmotionResults.from_dict(targeted_emotion_results_model_json)
        assert targeted_emotion_results_model != False

        # Construct a model instance of TargetedEmotionResults by calling from_dict on the json representation
        targeted_emotion_results_model_dict = TargetedEmotionResults.from_dict(targeted_emotion_results_model_json).__dict__
        targeted_emotion_results_model2 = TargetedEmotionResults(**targeted_emotion_results_model_dict)

        # Verify the model instances are equivalent
        assert targeted_emotion_results_model == targeted_emotion_results_model2

        # Convert model instance back to dict and verify no loss of data
        targeted_emotion_results_model_json2 = targeted_emotion_results_model.to_dict()
        assert targeted_emotion_results_model_json2 == targeted_emotion_results_model_json

class TestTargetedSentimentResults():
    """
    Test Class for TargetedSentimentResults
    """

    def test_targeted_sentiment_results_serialization(self):
        """
        Test serialization/deserialization for TargetedSentimentResults
        """

        # Construct a json representation of a TargetedSentimentResults model
        targeted_sentiment_results_model_json = {}
        targeted_sentiment_results_model_json['text'] = 'testString'
        targeted_sentiment_results_model_json['score'] = 72.5

        # Construct a model instance of TargetedSentimentResults by calling from_dict on the json representation
        targeted_sentiment_results_model = TargetedSentimentResults.from_dict(targeted_sentiment_results_model_json)
        assert targeted_sentiment_results_model != False

        # Construct a model instance of TargetedSentimentResults by calling from_dict on the json representation
        targeted_sentiment_results_model_dict = TargetedSentimentResults.from_dict(targeted_sentiment_results_model_json).__dict__
        targeted_sentiment_results_model2 = TargetedSentimentResults(**targeted_sentiment_results_model_dict)

        # Verify the model instances are equivalent
        assert targeted_sentiment_results_model == targeted_sentiment_results_model2

        # Convert model instance back to dict and verify no loss of data
        targeted_sentiment_results_model_json2 = targeted_sentiment_results_model.to_dict()
        assert targeted_sentiment_results_model_json2 == targeted_sentiment_results_model_json

class TestTokenResult():
    """
    Test Class for TokenResult
    """

    def test_token_result_serialization(self):
        """
        Test serialization/deserialization for TokenResult
        """

        # Construct a json representation of a TokenResult model
        token_result_model_json = {}
        token_result_model_json['text'] = 'testString'
        token_result_model_json['part_of_speech'] = 'ADJ'
        token_result_model_json['location'] = [38]
        token_result_model_json['lemma'] = 'testString'

        # Construct a model instance of TokenResult by calling from_dict on the json representation
        token_result_model = TokenResult.from_dict(token_result_model_json)
        assert token_result_model != False

        # Construct a model instance of TokenResult by calling from_dict on the json representation
        token_result_model_dict = TokenResult.from_dict(token_result_model_json).__dict__
        token_result_model2 = TokenResult(**token_result_model_dict)

        # Verify the model instances are equivalent
        assert token_result_model == token_result_model2

        # Convert model instance back to dict and verify no loss of data
        token_result_model_json2 = token_result_model.to_dict()
        assert token_result_model_json2 == token_result_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
