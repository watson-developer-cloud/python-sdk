# coding=utf-8
import watson_developer_cloud
import os, json

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-11-07',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

environments = discovery.get_environments()
news_environments = [x for x in environments['environments'] if
                     x['name'] == 'Watson News Environment']
news_environment_id = news_environments[0]['environment_id']
print(news_environment_id)

collections = discovery.get_collections(news_environment_id)
news_collections = [x for x in collections['collections']]
print(collections)
