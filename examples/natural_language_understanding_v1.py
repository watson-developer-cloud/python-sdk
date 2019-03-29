from __future__ import print_function
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions

# If service instance provides API key authentication
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    iam_apikey='YOUR APIKEY')

# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     # url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD')

response = service.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
    'Superman fears not Banner, but Wayne.',
    features=Features(entities=EntitiesOptions(),
                      keywords=KeywordsOptions())).get_result()

print(json.dumps(response, indent=2))
