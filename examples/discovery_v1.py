# coding: utf-8
from __future__ import print_function
import json
from watson_developer_cloud import DiscoveryV1

# If service instance provides API key authentication
# discovery = DiscoveryV1(
#     version='2018-08-01',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/discovery/api',
#     iam_apikey='iam_apikey')

discovery = DiscoveryV1(
    version='2018-08-01',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/discovery/api',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

environments = discovery.list_environments().get_result()
print(json.dumps(environments, indent=2))

news_environment_id = 'system'
print(json.dumps(news_environment_id, indent=2))

collections = discovery.list_collections(news_environment_id).get_result()
news_collections = [x for x in collections['collections']]
print(json.dumps(collections, indent=2))

configurations = discovery.list_configurations(
    environment_id=news_environment_id).get_result()
print(json.dumps(configurations, indent=2))

query_results = discovery.query(
    news_environment_id,
    news_collections[0]['collection_id'],
    filter='extracted_metadata.sha1::f5*',
    return_fields='extracted_metadata.sha1').get_result()
print(json.dumps(query_results, indent=2))

# new_environment = discovery.create_environment(name="new env", description="bogus env").get_result()
# print(new_environment)

# environment = discovery.get_environment(environment_id=new_environment['environment_id']).get_result()
# if environment['status'] == 'active':
#     writable_environment_id = new_environment['environment_id']
#     new_collection = discovery.create_collection(environment_id=writable_environment_id,
#                                                  name='Example Collection',
#                                                  description="just a test").get_result()

# print(new_collection)

# collections = discovery.list_collections(environment_id=writable_environment_id).get_result()
# print(collections)

# res = discovery.delete_collection(environment_id='<YOUR ENVIRONMENT ID>',
#                                   collection_id=new_collection['collection_id']).get_result()
# print(res)

# collections = discovery.list_collections(environment_id=writable_environment_id).get_result()
# print(collections)

# # with open(os.path.join(os.getcwd(),'..', 'resources','simple.html')) as fileinfo:
# #    print(discovery.test_document(environment_id=writable_environment_id, fileinfo=fileinfo).get_result())

# with open(os.path.join(os.getcwd(), '..','resources', 'simple.html')) as fileinfo:
#     res = discovery.add_document(environment_id=writable_environment_id,
#                                  collection_id=collections['collections'][0]['collection_id'],
#                                  file=fileinfo).get_result()
# print(res)

# res = discovery.get_collection(environment_id=writable_environment_id,
#                                collection_id=collections['collections'][0]['collection_id']).get_result()
# print(res['document_counts'])

#res = discovery.delete_environment(environment_id=writable_environment_id).get_result()
#print(res)
