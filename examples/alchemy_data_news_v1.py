import json
from watson_developer_cloud import AlchemyDataNewsV1

alchemy_data_news = AlchemyDataNewsV1(api_key='YOUR API KEY')

results = alchemy_data_news.get_news_documents(start='now-7d', end='now', time_slice='12h')

print(json.dumps(results, indent=2))
