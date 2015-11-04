import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='YOUR API KEY')

# print(json.dumps(alchemy_language.targeted_sentiment(text='I love cats! Dogs are the worst.', target='dogs'), indent=2))

# print(json.dumps(alchemy_language.author(url='https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'), indent=2))

# print(json.dumps(alchemy_language.keywords(max_keywords=5, url='https://developer.ibm.com/watson/blog/2015/11/03/price-reduction-for-watson-personality-insights/'), indent=2))
