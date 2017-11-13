# Copyright 2016 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
The v1 Retrieve and Rank service
(https://www.ibm.com/watson/developercloud/retrieve-rank.html)
"""

import json
import pysolr
from watson_developer_cloud.watson_service import WatsonService


class RetrieveAndRankV1(WatsonService):
    default_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api'

    def __init__(self, url=default_url, **kwargs):
        WatsonService.__init__(self, 'retrieve_and_rank', url, **kwargs)

    def list_solr_clusters(self):
        return self.request(method='GET', url='/v1/solr_clusters',
                            accept_json=True)

    def create_solr_cluster(self, cluster_name=None, cluster_size=None):
        if cluster_size:
            cluster_size = str(cluster_size)
        params = {'cluster_name': cluster_name, 'cluster_size': cluster_size}
        return self.request(method='POST', url='/v1/solr_clusters',
                            accept_json=True, json=params)

    def delete_solr_cluster(self, solr_cluster_id):
        return self.request(method='DELETE',
                            url='/v1/solr_clusters/{0}'.format(
                                solr_cluster_id),
                            accept_json=True)

    def get_solr_cluster_status(self, solr_cluster_id):
        return self.request(method='GET',
                            url='/v1/solr_clusters/{0}'.format(
                                solr_cluster_id),
                            accept_json=True)

    def list_configs(self, solr_cluster_id):
        return self.request(method='GET',
                            url='/v1/solr_clusters/{0}/config'.format(
                                solr_cluster_id), accept_json=True)

    # Need to test
    def create_config(self, solr_cluster_id, config_name, config):
        return self.request(method='POST',
                            url='/v1/solr_clusters/{0}/config/{1}'.format(
                                solr_cluster_id, config_name),
                            files={'body': config},
                            headers={'content-type': 'application/zip'},
                            accept_json=True)

    def delete_config(self, solr_cluster_id, config_name):
        return self.request(method='DELETE',
                            url='/v1/solr_clusters/{0}/config/{1}'.format(
                                solr_cluster_id, config_name),
                            accept_json=True)

    def get_config(self, solr_cluster_id, config_name):
        return self.request(method='GET',
                            url='/v1/solr_clusters/{0}/config/{1}'.format(
                                solr_cluster_id, config_name))

    def list_collections(self, solr_cluster_id):
        params = {'action': 'LIST', 'wt': 'json'}
        return self.request(method='GET',
                            url='/v1/solr_clusters/{0}/solr/admin/collections'
                            .format(solr_cluster_id),
                            params=params, accept_json=True)

    def create_collection(self, solr_cluster_id, collection_name, config_name):
        params = {'collection.configName': config_name,
                  'name': collection_name,
                  'action': 'CREATE', 'wt': 'json'}
        return self.request(method='POST',
                            url='/v1/solr_clusters/{0}/solr/admin/collections'
                            .format(solr_cluster_id),
                            params=params, accept_json=True)

    def delete_collection(self, solr_cluster_id, collection_name,
                          config_name=None):
        params = {'name': collection_name, 'action': 'DELETE', 'wt': 'json'}
        return self.request(method='POST',
                            url='/v1/solr_clusters/{0}/solr/admin/collections'
                            .format(solr_cluster_id),
                            params=params, accept_json=True)

    def get_pysolr_client(self, solr_cluster_id, collection_name):
        base_url = self.url.replace('https://',
                                    'https://' + self.username + ':' +
                                    self.password + '@')
        url = base_url + '/v1/solr_clusters/{0}/solr/{1}'.format(
            solr_cluster_id, collection_name)
        return pysolr.Solr(url)

    def create_ranker(self, training_data, name=None):
        data = None
        if name:
            data = {'training_metadata': json.dumps({'name': name})}
        return self.request(method='POST', url='/v1/rankers', accept_json=True,
                            files=[('training_data', training_data)],
                            data=data)

    def list_rankers(self):
        return self.request(method='GET', url='/v1/rankers', accept_json=True)

    def get_ranker_status(self, ranker_id):
        return self.request(method='GET',
                            url='/v1/rankers/{0}'.format(ranker_id),
                            accept_json=True)

    def rank(self, ranker_id, answer_data, top_answers=10):
        data = {'answers': + top_answers}
        return self.request(method='POST',
                            url='/v1/rankers/{0}/rank'.format(ranker_id),
                            files=[('answer_data', answer_data)], data=data,
                            accept_json=True)

    def delete_ranker(self, ranker_id):
        return self.request(method='DELETE',
                            url='/v1/rankers/{0}'.format(ranker_id),
                            accept_json=True)
