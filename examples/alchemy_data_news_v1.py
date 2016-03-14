import json
from watson_developer_cloud import AlchemyDataNewsV1

alchemy_data_news = AlchemyDataNewsV1(api_key='YOUR API KEY')

results = alchemy_data_news.get_news_documents(start='now-7d', end='now', time_slice='12h')
print(json.dumps(results, indent=2))

results = alchemy_data_news.get_news_documents(
    start='1453334400',
    end='1454022000',
    return_fields=['enriched.url.title',
                   'enriched.url.url',
                   'enriched.url.author',
                   'enriched.url.publicationDate'],
    query_fields={'q.enriched.url.enrichedTitle.entities.entity': '|text=IBM,type=company|'})
print(json.dumps(results, indent=2))
