from unittest import TestCase
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import WatsonException
from watson_developer_cloud.natural_language_understanding.features import (
    v1 as features)
import pytest
import responses


base_url = 'https://gateway.watsonplatform.net'
default_url = '{0}/natural-language-understanding/api'.format(base_url)


class TestFeatures(TestCase):
    def test_concepts(self):
        c = features.Concepts()
        assert(c.name() == 'concepts')
        assert(c.toDict() == {})
        c = features.Concepts(limit=10)
        assert(c.name() == 'concepts')
        assert(c.toDict() == {'limit': 10})

    def test_entities(self):
        e = features.Entities()
        assert(e.name() == 'entities')

    def test_keywords(self):
        k = features.Keywords()
        assert(k.name() == 'keywords')

    def test_categories(self):
        c = features.Categories()
        assert(c.name() == 'categories')
        assert(c.toDict() == {})

    def test_emotion(self):
        e = features.Emotion()
        assert(e.name() == 'emotion')

    def test_metadata(self):
        m = features.MetaData()
        assert(m.name() == 'metadata')

    def test_semantic_roles(self):
        s = features.SemanticRoles()
        assert(s.name() == 'semantic_roles')

    def test_relations(self):
        r = features.Relations()
        assert(r.name() == 'relations')

    def test_sentiment(self):
        s = features.Sentiment()
        assert(s.name() == 'sentiment')
        assert(s.toDict() == {})


class TestNaturalLanguageUnderstanding(TestCase):
    def test_version_date(self):
        with pytest.raises(TypeError):
            NaturalLanguageUnderstandingV1()
        # with pytest.raises(WatsonException):
        #     NaturalLanguageUnderstandingV1(version='2016-01-23')
        # with pytest.raises(WatsonException):
        #     NaturalLanguageUnderstandingV1(version='2016-01-23',
        #                                    url='https://bogus.com')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        assert(nlu)

    def test_analyze_throws(self):
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        with pytest.raises(ValueError):
            nlu.analyze([features.Sentiment()])
        with pytest.raises(ValueError):
            nlu.analyze([], text="this will not work")

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
        nlu.analyze([features.Sentiment()], text="hello this is a test")
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
        nlu.analyze([features.Sentiment(),
                     features.Emotion(document=False)],
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
        nlu.analyze([features.Sentiment(),
                     features.Emotion(document=False)], url="http://cnn.com",
                    xpath="/bogus/xpath", language="en")
        assert len(responses.calls) == 1
