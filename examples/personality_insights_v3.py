"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/personality-insights/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

## If service instance provides API key authentication
# personality_insights = PersonalityInsightsV3(
#     version='2016-10-20',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/personality-insights/api',
#     iam_api_key='your_api_key')

with open(join(dirname(__file__), '../resources/personality-v3.json')) as \
        profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))
