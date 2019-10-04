"""
The example returns a JSON response whose content is the same as that in
  ../resources/personality-v3-expect2.txt
"""
import json
from os.path import join, dirname
from ibm_watson import PersonalityInsightsV3
import csv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('your_api_key')
service = PersonalityInsightsV3(
    version='2017-10-13',
    authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/personality-insights/api')

############################
# Profile with JSON output #
############################

with open(join(dirname(__file__), '../resources/personality-v3.json')) as \
        profile_json:
    profile = service.profile(
        profile_json.read(),
        'application/json',
        raw_scores=True,
        consumption_preferences=True).get_result()

    print(json.dumps(profile, indent=2))

###########################
# Profile with CSV output #
###########################

with open(join(dirname(__file__), '../resources/personality-v3.json'), 'r') as \
        profile_json:
    response = service.profile(
        profile_json.read(),
        accept='text/csv',
        csv_headers=True).get_result()

profile = response.content
cr = csv.reader(profile.decode('utf-8').splitlines())
my_list = list(cr)
for row in my_list:
    print(row)
