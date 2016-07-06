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
The v1 beta Relationship Extraction service
(https://www.ibm.com/watson/developercloud/relationship-extraction.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class RelationshipExtractionV1Beta(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/relationship-extraction-beta/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(self, 'relationship_extraction', url, username, password,
                                             use_vcap_services)

    def extract(self, text, dataset='ie-en-news', return_type='xml'):
        """
        Extractions entities and relations from the source text.
        dataset can be either 'ie-en-news' or 'ie-es-news'
        returns an xml string
        """
        params = {'txt': text, 'rt': return_type, 'sid': dataset}

        is_json = (return_type == 'json')

        response = self.request(method='POST', url='/v1/sire/0', data=params, accept_json=is_json)
        if is_json:
            return response
        else:
            return response.text
