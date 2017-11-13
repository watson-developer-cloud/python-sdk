from unittest import TestCase
import watson_developer_cloud
import responses
import pytest


class TestAlchemyLanguageV1(TestCase):

    def test_api_key(self):
        default_url = 'https://gateway-a.watsonplatform.net/calls'
        inited = watson_developer_cloud.AlchemyLanguageV1(url=default_url, api_key='boguskey',
                                                          x_watson_learning_opt_out=True)
        assert inited.api_key == 'boguskey'
        assert inited.url == default_url
        inited.set_url(url="http://google.com")
        assert inited.url == "http://google.com"

        # with pytest.raises(watson_developer_cloud.WatsonException):
        #     watson_developer_cloud.AlchemyLanguageV1()

        # with pytest.raises(watson_developer_cloud.WatsonException):
        #     watson_developer_cloud.AlchemyLanguageV1(api_key='YOUR API KEY')

    def test_unpack_id(self):

        testdict = {'one': 10}
        assert watson_developer_cloud.AlchemyLanguageV1.unpack_id(testdict, 'one') == 10
        assert watson_developer_cloud.AlchemyLanguageV1.unpack_id(testdict, 'two') == testdict

    @responses.activate
    def test_author(self):
        url = 'https://gateway-a.watsonplatform.net'
        default_url = 'https://gateway-a.watsonplatform.net/calls'
        responses.add(responses.POST, '{0}/html/HTMLGetAuthor'.format(url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')
        responses.add(responses.POST, '{0}/url/URLGetAuthor'.format(url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')
        responses.add(responses.POST, '{0}/html/HTMLGetAuthor'.format(default_url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')
        responses.add(responses.POST, '{0}/url/URLGetAuthor'.format(default_url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')
        alang = watson_developer_cloud.AlchemyLanguageV1(url=url, api_key='boguskey', x_watson_learning_opt_out=True)
        alang.author(html="I'm html")
        alang.author(url="http://google.com")
        with pytest.raises(watson_developer_cloud.WatsonInvalidArgument):
            alang.author()

        alang = watson_developer_cloud.AlchemyLanguageV1(url=default_url, api_key='boguskey',
                                                         x_watson_learning_opt_out=True)
        alang.author(html="I'm html")
        alang.author(url="http://google.com")
        assert len(responses.calls) == 4

    @responses.activate
    def test_auth_exception(self):
        default_url = 'https://gateway-a.watsonplatform.net/calls'
        responses.add(responses.POST, '{0}/url/URLGetAuthor'.format(default_url),
                      body='{"bogus": "response"}', status=401,
                      content_type='application/json')

        alang = watson_developer_cloud.AlchemyLanguageV1(url=default_url, api_key='boguskey',
                                                         x_watson_learning_opt_out=True)
        with pytest.raises(watson_developer_cloud.WatsonException):
            alang.author(url="http://google.com")
        assert len(responses.calls) == 1

    @responses.activate
    def test_authors(self):
        default_url = 'https://gateway-a.watsonplatform.net/calls'
        responses.add(responses.POST, '{0}/url/URLGetAuthors'.format(default_url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')
        responses.add(responses.POST, '{0}/html/HTMLGetAuthors'.format(default_url),
                      body='{"bogus": "response"}', status=200,
                      content_type='application/json')

        alang = watson_developer_cloud.AlchemyLanguageV1(url=default_url, api_key='boguskey',
                                                         x_watson_learning_opt_out=True)
        alang.authors(url="http://google.com")
        alang.authors(html="<h1>Author</h1>")
        assert len(responses.calls) == 2
