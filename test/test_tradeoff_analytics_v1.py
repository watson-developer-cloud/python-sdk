# coding=utf-8
import json
import os
import responses
import watson_developer_cloud


@responses.activate
def test_success():
    dilemmas_url = 'https://gateway.watsonplatform.net/tradeoff-analytics/api/v1/dilemmas'
    dilemmas_response = '{"problem": {"options": [{"values": {"price": 239, "RAM": 2048, "weight": 130}, "name": ' \
                        '"Samsung Galaxy S4 White", "key": " 1", "description_html": ""}, {"values": {"price": 240, ' \
                        '"RAM": 2048, "weight": 130}, "name": "Samsung Galaxy S4 Black", "key": "2", ' \
                        '"description_html": ""}, {"values": {"price": 79, "RAM": 2048, "weight": 133}, "name": ' \
                        '"Samsung Galaxy S3 White", "key": "3", "description_html": ""}], "columns": [{"full_name": ' \
                        '"Price (Eur)", "is_objective": true, "type": "numeric", "goal": "min", "key": "price"}, ' \
                        '{"full_name": "RAM (MB)", "is_objective": false, "type": "numeric", "goal": "max", "key": ' \
                        '"RAM"}, {"full_name": "Weight (gr)", "is_objective": true, "type": "numeric", "goal": ' \
                        '"min", "key": "weight"}], "subject": "phone"}, "resolution": {"solutions": [{"status": ' \
                        '"FRONT", "solution_ref": " 1"}, {"status": "EXCLUDED", "solution_ref": "2"}, {"status": ' \
                        '"FRONT", "solution_ref": "3"}]}}'

    responses.add(responses.POST, dilemmas_url,
                  body=dilemmas_response, status=200,
                  content_type='application/json')

    tradeoff_analytics = watson_developer_cloud.TradeoffAnalyticsV1(
        username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/problem.json')) as data_file:
        problem_data = json.load(data_file)
        tradeoff_analytics.dilemmas(problem_data)
        assert responses.calls[0].request.url == dilemmas_url
        assert responses.calls[0].response.text == dilemmas_response

    assert len(responses.calls) == 1
