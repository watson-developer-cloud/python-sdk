from __future__ import print_function
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

# If service instance provides API key authentication
# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     iam_apikey='your_apikey')

service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

response = service.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
    'Superman fears not Banner, but Wayne.',
    features=Features(entities=EntitiesOptions(),
                      keywords=KeywordsOptions())).get_result()

print(json.dumps(response, indent=2))
