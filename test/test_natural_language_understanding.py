from unittest import TestCase
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud import WatsonException
import watson_developer_cloud.nlu.features.v1 as features
import pytest
import responses
import json


base_url = 'https://gateway.watsonplatform.net'
default_url = '{0}/natural-language-understanding/api'.format(base_url)


@responses.activate
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


class TestNaturalLanguageUnderstanding(TestCase):
    def test_version_date(self):
        with pytest.raises(TypeError):
            NaturalLanguageUnderstandingV1()
        with pytest.raises(WatsonException):
            NaturalLanguageUnderstandingV1(version='2016-01-23')
        with pytest.raises(WatsonException):
            NaturalLanguageUnderstandingV1(version='2016-01-23',
                                           url='https://bogus.com')
        nlu = NaturalLanguageUnderstandingV1(version='2016-01-23',
                                             url='http://bogus.com',
                                             username='username',
                                             password='password')
        assert(nlu)

    def test_text_analyze(self):
        assert(False)
