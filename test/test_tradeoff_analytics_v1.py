# coding=utf-8
import json
import os
import responses
import watson_developer_cloud

dilemmas_url = 'https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas'

@responses.activate
def test_visualization_no_preferable_options():

    with open(os.path.join(os.path.dirname(__file__), '../resources/tradeoff-expect1.txt')) as expect_file:
        dilemmas_response = expect_file.read()

    responses.add(responses.POST, dilemmas_url,
                  body=dilemmas_response, status=200,
                  content_type='application/json')

    tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
        tradeoff_analytics.dilemmas(json.load(data_file))

    assert 'generate_visualization=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == dilemmas_response
    assert len(responses.calls) == 1

@responses.activate
def test_no_visualization_no_preferable_options():

    with open(os.path.join(os.path.dirname(__file__), '../resources/tradeoff-expect2.txt')) as expect_file:
        dilemmas_response = expect_file.read()

    responses.add(responses.POST, dilemmas_url,
                  body=dilemmas_response, status=200,
                  content_type='application/json')

    tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
        tradeoff_analytics.dilemmas(json.load(data_file), generate_visualization=False)

    assert 'generate_visualization=false' in responses.calls[0].request.url
    assert responses.calls[0].response.text == dilemmas_response
    assert len(responses.calls) == 1

@responses.activate
def test_no_visualization_preferable_options():
    with open(os.path.join(os.path.dirname(__file__), '../resources/tradeoff-expect3.txt')) as expect_file:
        dilemmas_response = expect_file.read()

    responses.add(responses.POST, dilemmas_url,
                  body=dilemmas_response, status=200,
                  content_type='application/json')

    tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
        tradeoff_analytics.dilemmas(
            json.load(data_file),
            generate_visualization=False,
            find_preferable_options=True)

    assert 'find_preferable_options=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == dilemmas_response
    assert len(responses.calls) == 1


@responses.activate
def test_visualization_preferable_options():
    with open(os.path.join(os.path.dirname(__file__), '../resources/tradeoff-expect4.txt')) as expect_file:
        dilemmas_response = expect_file.read()

    responses.add(responses.POST, dilemmas_url,
                  body=dilemmas_response, status=200,
                  content_type='application/json')
    tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
        tradeoff_analytics.dilemmas(
            json.load(data_file),
            find_preferable_options=True)

    assert 'generate_visualization=true' in responses.calls[0].request.url
    assert 'find_preferable_options=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == dilemmas_response
    assert len(responses.calls) == 1
