import responses
import watson_developer_cloud
import os


@responses.activate
def test_success():
    profile_url = 'https://gateway.watsonplatform.net/personality-insights/api/v2/profile'
    profile_response = '{"tree":{"children":[{"children":[{"category":"personality","percentage":0.9493716242287923,' \
                       '"children":[{"category":"personality","name":"Openness","sampling_error":0.14430105599999998,' \
                       '"id":"Openness","percentage":0.9493716242287923,"children":[{"category":"personality",' \
                       '"percentage":0.7224550516937974,"id":"Adventurousness","sampling_error":0.11646272,"name":' \
                       '"Adventurousness"}]}]}]}]}}'

    responses.add(responses.POST, profile_url,
                  body=profile_response, status=200,
                  content_type='application/json')

    with open(os.path.join(os.path.dirname(__file__), '../resources/personality.txt')) as personality_text:
        personality_insights = watson_developer_cloud.PersonalityInsightsV2(
            username="username", password="password")
        personality_insights.profile(personality_text)

    assert responses.calls[0].request.url == profile_url
    assert responses.calls[0].response.text == profile_response

    assert len(responses.calls) == 1
