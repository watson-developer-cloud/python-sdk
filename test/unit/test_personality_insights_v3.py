# coding: utf-8
import responses
import ibm_watson
import os
import codecs
from ibm_watson.personality_insights_v3 import Profile
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

profile_url = 'https://gateway.watsonplatform.net/personality-insights/api/v3/profile'

@responses.activate
def test_plain_to_json():
    authenticator = BasicAuthenticator('username', 'password')
    personality_insights = ibm_watson.PersonalityInsightsV3('2016-10-20', authenticator=authenticator)

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3-expect1.txt'), 'r') as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3.txt'), 'rb') as personality_text:
        response = personality_insights.profile(
            personality_text, 'application/json', content_type='text/plain;charset=utf-8').get_result()

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)

@responses.activate
def test_json_to_json():

    authenticator = BasicAuthenticator('username', 'password')
    personality_insights = ibm_watson.PersonalityInsightsV3('2016-10-20', authenticator=authenticator)

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3-expect2.txt'), 'r') as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3.json'), 'rb') as personality_text:
        response = personality_insights.profile(
            personality_text, accept='application/json',
            content_type='application/json',
            raw_scores=True,
            consumption_preferences=True).get_result()

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert 'raw_scores=true' in responses.calls[0].request.url
    assert 'consumption_preferences=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)

@responses.activate
def test_json_to_csv():

    authenticator = BasicAuthenticator('username', 'password')
    personality_insights = ibm_watson.PersonalityInsightsV3('2016-10-20', authenticator=authenticator)

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3-expect3.txt'), 'r') as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='text/csv')

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3.json'), 'rb') as personality_text:
        personality_insights.profile(
            personality_text,
            'text/csv',
            content_type='application/json',
            csv_headers=True,
            raw_scores=True,
            consumption_preferences=True)

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert 'raw_scores=true' in responses.calls[0].request.url
    assert 'consumption_preferences=true' in responses.calls[0].request.url
    assert 'csv_headers=true' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1


@responses.activate
def test_plain_to_json_es():

    authenticator = BasicAuthenticator('username', 'password')
    personality_insights = ibm_watson.PersonalityInsightsV3('2016-10-20', authenticator=authenticator)

    with codecs.open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3-expect4.txt'), 'r') as expect_file:
        profile_response = expect_file.read()

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../../resources/personality-v3-es.txt'), 'rb') as personality_text:
        response = personality_insights.profile(
            personality_text,
            'application/json',
            content_type='text/plain;charset=utf-8',
            content_language='es',
            accept_language='es').get_result()

    assert 'version=2016-10-20' in responses.calls[0].request.url
    assert responses.calls[0].response.text == profile_response
    assert len(responses.calls) == 1
    # Verify that response can be converted to a Profile
    Profile._from_dict(response)
