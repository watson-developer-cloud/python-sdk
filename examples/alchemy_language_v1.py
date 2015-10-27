import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='YOUR API KEY')

# print(json.dumps(alchemy_language.targeted_sentiment(text='I love cats! Dogs are the worst.', target='dogs'), indent=2))
