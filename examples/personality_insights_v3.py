"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import PersonalityInsightsV3
import csv

# # If service instance provides API key authentication
# service = PersonalityInsightsV3(
#     version='2017-10-13',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/personality-insights/api',
#     iam_apikey='your_apikey')

service = PersonalityInsightsV3(
    version='2017-10-13',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/personality-insights/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

############################
# Profile with JSON output #
############################

with open(join(dirname(__file__), '../resources/personality-v3.json')) as \
        profile_json:
    profile = service.profile(
        profile_json.read(),
        content_type='application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()

    print(json.dumps(profile, indent=2))

###########################
# Profile with CSV output #
###########################

with open(join(dirname(__file__), '../resources/personality-v3.json')) as \
        profile_json:
    response = service.profile(
        profile_json.read(),
        content_type='application/json',
        accept="text/csv",
        csv_headers=True).get_result()

profile = response.content
cr = csv.reader(profile.splitlines())
my_list = list(cr)
for row in my_list:
    print(row)
