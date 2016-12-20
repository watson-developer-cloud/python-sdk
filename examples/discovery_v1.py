# coding: utf-8

# In[1]:

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'..'))
import watson_developer_cloud

discovery = watson_developer_cloud.DiscoveryV1(
    '2016-11-07',
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

environments = discovery.get_environments()
print(environments)

news_environments = [x for x in environments['environments'] if
                     x['name'] == 'Watson News Environment']
news_environment_id = news_environments[0]['environment_id']
print(news_environment_id)

collections = discovery.list_collections(news_environment_id)
news_collections = [x for x in collections['collections']]
print(collections)

print(discovery.list_configurations(environment_id=news_environment_id))
default_config_id = discovery.get_default_configuration_id(environment_id=news_environment_id)
print(default_config_id)

default_config = discovery.get_configuration(environment_id=news_environment_id, configuration_id=default_config_id)
print(default_config)


# new_environment = discovery.create_environment(name="new env", description="bogus env")
# print(new_environment)

#if (discovery.get_environment(environment_id=new_environment['environment_id'])['status'] == 'active'):
#    writable_environment_id = new_environment['environment_id']
#    new_collection = discovery.create_collection(environment_id=writable_environment_id,
#                                                name='Example Collection',
#                                                description="just a test")
#
#    print(new_collection)
    #print(discovery.get_collections(environment_id=writable_environment_id))
    #res = discovery.delete_collection(environment_id='10b733d0-1232-4924-a670-e6ffaed2e641',
    #                                  collection_id=new_collection['collection_id'])
#    print(res)

# collections = discovery.list_collections(environment_id=writable_environment_id)
# print(collections)

#with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
#    print(discovery.test_document(environment_id=writable_environment_id, fileinfo=fileinfo))


# In[25]:

# with open(os.path.join(os.getcwd(),'..','resources','simple.html')) as fileinfo:
#     res = discovery.add_document(environment_id=writable_environment_id,
#                                 collection_id=collections['collections'][0]['collection_id'],
#                                 fileinfo=fileinfo)
#    print(res)


#res = discovery.get_collection(environment_id=writable_environment_id,
#                               collection_id=collections['collections'][0]['collection_id'])
#print(res['document_counts'])


#res = discovery.delete_environment(environment_id=writable_environment_id)
#print(res)
