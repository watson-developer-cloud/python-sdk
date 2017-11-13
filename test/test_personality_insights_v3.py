import responses
import watson_developer_cloud
import os
import codecs
from watson_developer_cloud.personality_insights_v3 import Profile

profile_url = 'https://gateway.watsonplatform.net/personality-insights/api/v3/profile'

@responses.activate
def test_plain_to_json():

    personality_insights = watson_developer_cloud.PersonalityInsightsV3(
        '2016-10-20', username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3-expect1.txt')) as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3.txt')) as personality_text:
        response = personality_insights.profile(
            personality_text, content_type='text/plain;charset=utf-8')

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)

@responses.activate
def test_json_to_json():

    personality_insights = watson_developer_cloud.PersonalityInsightsV3(
        '2016-10-20', username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3-expect2.txt')) as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3.json')) as personality_text:
        response = personality_insights.profile(
            personality_text, content_type='application/json',
            raw_scores=True, consumption_preferences=True)

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert 'raw_scores=true' in responses.calls[0].request.url
    assert 'consumption_preferences=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)

@responses.activate
def test_json_to_csv():

    personality_insights = watson_developer_cloud.PersonalityInsightsV3(
        '2016-10-20', username="username", password="password")

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3-expect3.txt')) as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='text/csv')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3.json')) as personality_text:
        personality_insights.profile(
            personality_text, content_type='application/json',
            accept='text/csv', csv_headers=True,
            raw_scores=True, consumption_preferences=True)

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert 'raw_scores=true' in responses.calls[0].request.url
    assert 'consumption_preferences=true' in responses.calls[0].request.url
    assert 'csv_headers=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1


@responses.activate
def test_plain_to_json_es():

    personality_insights = watson_developer_cloud.PersonalityInsightsV3(
        '2016-10-20', username="username", password="password")

    with codecs.open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3-expect4.txt'), \
            encoding='utf-8') as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality-v3-es.txt')) as personality_text:
        response = personality_insights.profile(
            personality_text, content_type='text/plain;charset=utf-8',
            content_language='es', accept_language='es')

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)
