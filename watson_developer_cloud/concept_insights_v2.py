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
The v2 Concept Insights service
(https://http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/concept-insights.html)
"""
from .watson_developer_cloud_service import WatsonDeveloperCloudService


class ConceptInsightsV2(WatsonDeveloperCloudService):
    """The IBM Watson Concept Insights service provides APIs
    that enable you to work with concepts and identify conceptual
    associations in the content that you provide as input to the service.
    Input content is auto-tagged against a concept graph, which is a formal
    representation of the relationship(s) between concepts. The concept
    graph used by the Concept Insights service is based on content that
    has been ingested from the English language Wikipedia.
    """
    DEFAULT_URL = 'https://gateway.watsonplatform.net/concept-insights/api'
    CORPORA_PATH = '/v2/corpora'
    WIKIPEDIA_ACCOUNT = 'wikipedia'

    def __init__(self, url=DEFAULT_URL, **kwargs):
        WatsonDeveloperCloudService.__init__(
            self, 'concept_insights', url, **kwargs)
        self.cached_account = None

    def get_default_account(self):
        if self.cached_account:
            return self.cached_account
        self.cached_account = self.get_accounts_info()[0]['account_id']
        return self.cached_account

    def set_username_and_password(self, username=None, password=None):
        self.cached_account = None
        WatsonDeveloperCloudService.set_username_and_password(
            self, username=username, password=password)

    def _get_corpus_id_path(self, corpus, account_id=None):
        if not account_id:
            account_id = self.get_default_account()
        return '{}/{}/{}/'.format(self.CORPORA_PATH, account_id, corpus)

    def get_accounts_info(self):
        return self.request(method='GET', url='/v2/accounts', accept_json=True)

    def get_concept(self, graph_id, concept_id, account_id=None):
        return self.request(method='GET', url='/v2/{}'.format(concept_id), accept_json=True)

    # def annotate_text(self, text, account_id=WIKIPEDIA_ACCOUNT, graph=WIKIPEDIA_EN_LATEST):
    #     return self.request(method='GET', url='/v2/'
    #                         )
