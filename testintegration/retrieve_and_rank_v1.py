import json
import os
import time
import sys
from watson_developer_cloud import RetrieveAndRankV1


retrieve_and_rank = RetrieveAndRankV1(
    username='YOUR SERVICE USERNAME',
    password='YOUR SERVICE PASSWORD')

# End to End integration retrieve test
mycluster = retrieve_and_rank.create_solr_cluster(cluster_name='Python Test Cluster', cluster_size=None)
print(json.dumps(mycluster, indent=2))

retrieve_results = retrieve_and_rank.list_solr_clusters()
print(json.dumps(retrieve_results, indent=2))

retrieve_status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=mycluster['solr_cluster_id'])
print(json.dumps(retrieve_status, indent=2))

# 10 minutes should be plenty for a cluster to complete
trainingtimeout = time.time() + 60 * 10
print ('Waiting for Cluster to become available!')   
while retrieve_status['solr_cluster_status'] != "READY":
    time.sleep(5)
    if time.time() > trainingtimeout:
        print ('Cluster creation failed!')
        retrieve_results = retrieve_and_rank.delete_solr_cluster(mycluster['solr_cluster_id'])
        sys.exit(1)
    retrieve_status = retrieve_and_rank.get_solr_cluster_status(solr_cluster_id=mycluster['solr_cluster_id'])

with open(os.path.join(os.path.dirname(__file__), '../resources/solr_config.zip'), 'rb') as config:
    retrieve_results = retrieve_and_rank.create_config(mycluster['solr_cluster_id'], 'python-test-config', config)
    print(json.dumps(retrieve_results, indent=2))

retrieve_results = retrieve_and_rank.list_configs(solr_cluster_id=mycluster['solr_cluster_id'])
print(json.dumps(retrieve_results, indent=2))

retrieve_results = retrieve_and_rank.get_config(mycluster['solr_cluster_id'], 'python-test-config')
print(retrieve_results)

retrieve_results = retrieve_and_rank.create_collection(mycluster['solr_cluster_id'], 'python-test-collection', 'python-test-config')
print(json.dumps(retrieve_results, indent=2))

retrieve_results = retrieve_and_rank.list_collections(solr_cluster_id=mycluster['solr_cluster_id'])
print(json.dumps(retrieve_results, indent=2))

pysolr_client = retrieve_and_rank.get_pysolr_client(mycluster['solr_cluster_id'], 'python-test-collection')
query_results = pysolr_client.search('bananas')
print('{0} documents found'.format(len(query_results.docs)))

retrieve_results = retrieve_and_rank.delete_collection(mycluster['solr_cluster_id'], 'python-test-collection', 'python-test-config')
print(json.dumps(retrieve_results, indent=2))

retrieve_results = retrieve_and_rank.delete_config(mycluster['solr_cluster_id'], 'python-test-config')
print(json.dumps(retrieve_results, indent=2))

retrieve_results = retrieve_and_rank.delete_solr_cluster(mycluster['solr_cluster_id'])
print(json.dumps(retrieve_results, indent=2))

# End to End integration ranker test
with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_training_data.csv'), 'rb') as training_data:
    myranker = retrieve_and_rank.create_ranker(training_data=training_data, name='Python Test Ranker')
print(json.dumps(myranker, indent=2))
 
ranker_results = retrieve_and_rank.list_rankers()
print(json.dumps(ranker_results, indent=2))
 
ranker_status = retrieve_and_rank.get_ranker_status(myranker['ranker_id'])
print(json.dumps(ranker_status, indent=2))
 
# 10 minutes should be plenty for a train to complete
trainingtimeout = time.time() + 60 * 10
print ('Waiting for Ranker to become available!')   
while ranker_status['status'] != "Available":
    time.sleep(5)
    if time.time() > trainingtimeout:
        print ('Ranker Training failed!')
        ranker_results = retrieve_and_rank.delete_ranker(myranker['ranker_id'])
        sys.exit(1)
    ranker_status = retrieve_and_rank.get_ranker_status(myranker['ranker_id'])
    
with open(os.path.join(os.path.dirname(__file__), '../resources/ranker_answer_data.csv'), 'rb') as answer_data:
    ranker_results = retrieve_and_rank.rank(myranker['ranker_id'], answer_data)
    print(json.dumps(ranker_results, indent=2))
 
ranker_results = retrieve_and_rank.delete_ranker(myranker['ranker_id'])
print(json.dumps(ranker_results))
