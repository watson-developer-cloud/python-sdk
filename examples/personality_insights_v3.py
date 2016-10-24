import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3

"""
The example returns a JSON response whose content is the same as that in
   ../resources/personality-v3-expect2.txt
"""

personality_insights = PersonalityInsightsV3(
    version='2016-10-20',
    username='daa4e679-184b-4ea4-bcf5-325431b92991',
    password='OCMwTTWKU6l2')

with open(join(dirname(__file__), '../resources/personality-v3.json')) as profile_json:
    profile = personality_insights.profile(
        profile_json.read(), content_type='application/json',
        raw_scores=True, consumption_preferences=True)

    print(json.dumps(profile, indent=2))
