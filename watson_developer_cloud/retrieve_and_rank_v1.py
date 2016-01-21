# Copyright 2015 IBM All Rights Reserved.
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
(http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/retrieve-rank.html)
"""

import json
from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService


class RetrieveAndRankV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/retrieve-and-rank/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(self, 'retrieve_and_rank', url, username, password,
                                             use_vcap_services)

    def create_ranker(self, training_data, name=None):
        data = None
        if name:
            data = {'training_metadata': json.dumps({'name': name})}
        return self.request(method='POST', url='/v1/rankers', accept_json=True,
                            files=[('training_data', training_data)], data=data)

    def list_rankers(self):
        return self.request(method='GET', url='/v1/rankers', accept_json=True)

    def get_ranker_status(self, ranker_id):
        return self.request(method='GET', url='/v1/rankers/{}'.format(ranker_id), accept_json=True)

    def rank(self, ranker_id, answer_data, top_answers=10):
        data = {'answer_metadata': json.dumps({'answers': + top_answers})}
        return self.request(method='POST', url='/v1/rankers/{}/rank'.format(ranker_id),
                            files=[('answer_data', answer_data)], data=data, accept_json=True)

    def delete_ranker(self, ranker_id):
        return self.request(method='DELETE', url='/v1/rankers/{}'.format(ranker_id), accept_json=True)
