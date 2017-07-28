import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    Features


natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2017-02-27',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[Features.Entities(), Features.Keywords()])

print(json.dumps(response, indent=2))
