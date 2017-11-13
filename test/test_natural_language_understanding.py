from unittest import TestCase
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import \
     Features, ConceptsOptions, EntitiesOptions, KeywordsOptions, CategoriesOptions, \
     EmotionOptions, MetadataOptions, SemanticRolesOptions, RelationsOptions, \
     SentimentOptions

import os
import pytest
import responses


base_url = 'https://gateway.watsonplatform.net'
default_url = '{0}/natural-language-understanding/api'.format(base_url)


class TestFeatures(TestCase):
    def test_concepts(self):
        c = Features(concepts=ConceptsOptions())
        assert c._to_dict() == {'concepts': {}}
        c = Features(concepts=ConceptsOptions(limit=10))
        assert c._to_dict() == {'concepts': {'limit': 10}}

    def test_entities(self):
        e = Features(entities=EntitiesOptions())
        assert e._to_dict() == {'entities': {}}

    def test_keywords(self):
        k = Features(keywords=KeywordsOptions())
        assert k._to_dict() == {'keywords': {}}

    def test_categories(self):
        c = Features(categories=CategoriesOptions())
        assert c._to_dict() == {'categories': {}}

    def test_emotion(self):
        e = Features(emotion=EmotionOptions())
        assert e._to_dict() == {'emotion': {}}

    def test_metadata(self):
        m = Features(metadata=MetadataOptions())
        assert m._to_dict() == {'metadata': {}}

    def test_semantic_roles(self):
        s = Features(semantic_roles=SemanticRolesOptions())
        assert s._to_dict() == {'semantic_roles': {}}

    def test_relations(self):
        r = Features(relations=RelationsOptions())
        assert r._to_dict() == {'relations': {}}

    def test_sentiment(self):
        s = Features(sentiment=SentimentOptions())
        assert s._to_dict() == {'sentiment': {}}


class TestNaturalLanguageUnderstanding(TestCase):
    def test_version_date(self):
        with pytest.raises(TypeError):
            NaturalLanguageUnderstandingV1() # pylint: disable=E1120
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        assert nlu

    @pytest.mark.skipif(os.getenv('VCAP_SERVICES') is not None,
                        reason='credentials may come from VCAP_SERVICES')
    def test_missing_credentials(self):
        with pytest.raises(ValueError):
            NaturalLanguageUnderstandingV1(version='2016-01-23')
        with pytest.raises(ValueError):
            NaturalLanguageUnderstandingV1(version='2016-01-23',
                                           url='https://bogus.com')

    def test_analyze_throws(self):
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        with pytest.raises(ValueError):
            nlu.analyze(None, text="this will not work")

    @responses.activate
    def test_text_analyze(self):
        nlu_url = "http://bogus.com/v1/analyze"
        responses.add(responses.POST, nlu_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        nlu.analyze(Features(sentiment=SentimentOptions()), text="hello this is a test")
        assert len(responses.calls) == 1

    @responses.activate
    def test_html_analyze(self):
        nlu_url = "http://bogus.com/v1/analyze"
        responses.add(responses.POST, nlu_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        nlu.analyze(Features(sentiment=SentimentOptions(),
                             emotion=EmotionOptions(document=False)),
                    html="<span>hello this is a test</span>")
        assert len(responses.calls) == 1

    @responses.activate
    def test_url_analyze(self):
        nlu_url = "http://bogus.com/v1/analyze"
        responses.add(responses.POST, nlu_url,
                      body="{\"resulting_key\": true}", status=200,
                      content_type='application/json')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        nlu.analyze(Features(sentiment=SentimentOptions(),
                             emotion=EmotionOptions(document=False)),
                    url="http://cnn.com",
                    xpath="/bogus/xpath", language="en")
        assert len(responses.calls) == 1

    @responses.activate
    def test_list_models(self):
        nlu_url = "http://bogus.com/v1/models"
        responses.add(responses.GET, nlu_url, status=200,
                      body="{\"resulting_key\": true}",
                      content_type='application/json')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        nlu.list_models()
        assert len(responses.calls) == 1

    @responses.activate
    def test_delete_model(self):
        model_id = "invalid_model_id"
        nlu_url = "http://bogus.com/v1/models/" + model_id
        responses.add(responses.DELETE, nlu_url, status=200,
                      body="{}", content_type='application/json')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        nlu.delete_model(model_id)
        assert len(responses.calls) == 1
