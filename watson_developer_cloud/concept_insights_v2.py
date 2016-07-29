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
The v2 Concept Insights service
(https://www.ibm.com/watson/developercloud/concept-insights.html)
"""
from .watson_developer_cloud_service import WatsonDeveloperCloudService
import json


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
    WIKIPEDIA_EN_LATEST = '/graphs/wikipedia/en-latest'

    def __init__(self, url=DEFAULT_URL, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'concept_insights', url, **kwargs)
        self.cached_account = None

    def get_default_account(self):
        if self.cached_account:
            return self.cached_account
        self.cached_account = self.get_accounts_info()['accounts'][0]['account_id']
        return self.cached_account

    def set_username_and_password(self, username=None, password=None):
        self.cached_account = None
        WatsonDeveloperCloudService.set_username_and_password(
            self, username=username, password=password)

    def get_accounts_info(self):
        return self.request(method='GET', url='/v2/accounts', accept_json=True)

    def get_concept(self, concept_id, graph=WIKIPEDIA_EN_LATEST):
        return self.request(method='GET', url='/v2/{0}/concepts/{1}'.format(graph, concept_id), accept_json=True)

    def search_concept_by_label(self, label, graph=WIKIPEDIA_EN_LATEST, concept_fields=None):
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        params = {'query': label, 'concept_fields': concept_fields}
        return self.request(method='GET', url='/v2/{0}/label_search'.format(graph), params=params, accept_json=True)

    def get_graphs(self):
        return self.request(method='GET', url='/v2/graphs', accept_json=True)

    @staticmethod
    def _expand_concept_or_document_ids(ids, graph):
        try:
            string = basestring
        except NameError:
            string = str
        if isinstance(ids, string):
            ids = [ids]
        ids = [item_id if item_id.startswith('/graphs/') or item_id.startswith('/corpora/')
               else graph + '/concepts/' + item_id for item_id in ids]
        return ids

    def get_related_concepts(self, concept_ids, level=1, limit=10, concept_fields=None, graph=WIKIPEDIA_EN_LATEST):
        concept_ids = self._expand_concept_or_document_ids(concept_ids, graph)
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        params = {'concepts': json.dumps(concept_ids),
                  'concept_fields': concept_fields,
                  'level': level,
                  'limit': limit}
        return self.request(method='GET', url='/v2/{0}/related_concepts'.format(graph), params=params, accept_json=True)

    def get_relation_scores(self, concept_id, concept_ids, graph=WIKIPEDIA_EN_LATEST):
        concept_ids = self._expand_concept_or_document_ids(concept_ids, graph)
        params = {'concepts': json.dumps(concept_ids)}
        return self.request(method='GET', url='/v2/{0}/concepts/{1}/relation_scores'.format(graph, concept_id),
                            params=params, accept_json=True)

    def annotate_text(self, text, graph=WIKIPEDIA_EN_LATEST):
        return self.request(method='POST', url='/v2/{0}/annotate_text'.format(graph), data=text,
                            headers={'content-type': 'text/plain'}, accept_json=True)

    def list_corpora(self, account=None):
        return self.request(method='GET', url='/v2/corpora/{0}'.format(account), accept_json=True)

    def _get_full_corpus_path(self, corpus, account=None):
        if corpus.count('/') == 3:
            return corpus
        if account is None:
            account = self.get_default_account()
        return '/corpora/{0}/{1}'.format(account, corpus)

    def get_corpus(self, corpus, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}'.format(full_corpus_path), accept_json=True)

    def get_corpus_processing_state(self, corpus, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}/processing_state'.format(full_corpus_path), accept_json=True)

    def get_corpus_stats(self, corpus, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}/stats'.format(full_corpus_path), accept_json=True)

    def create_corpus(self, corpus, users=None, access=None, public_fields=None, ttl_hours=None, expires_on=None,
                      account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        corpus_body = {'access': access,
                       'users': users,
                       'public_fields': public_fields,
                       'ttl_hours': ttl_hours,
                       'expires_on': expires_on}
        return self.request(method='PUT', url='/v2/{0}'.format(full_corpus_path), json=corpus_body)

    def delete_corpus(self, corpus, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='DELETE', url='/v2/{0}'.format(full_corpus_path))

    def update_corpus_metadata(self, corpus, users, access=None, public_fields=None, ttl_hours=None,
                               expires_on=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        corpus_body = {'access': access,
                       'users': users,
                       'public_fields': public_fields,
                       'ttl_hours': ttl_hours,
                       'expires_on': expires_on}
        return self.request(method='POST', url='/v2/{0}'.format(full_corpus_path), json=corpus_body)

    def search_corpus_by_label(self, corpus, query, concepts=False, prefix=False, limit=10, concept_fields=None,
                               document_fields=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        if isinstance(document_fields, dict):
            document_fields = json.dumps(document_fields)
        params = {'query': query,
                  'concepts': concepts,
                  'prefix': prefix,
                  'limit': limit,
                  'concept_fields': concept_fields,
                  'document_fields': document_fields}
        return self.request(method='GET', url='/v2/{0}/label_search'.format(full_corpus_path), params=params,
                            accept_json=True)

    def get_corpus_related_concepts(self, corpus, level=1, limit=10, concept_fields=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        params = {'level': level,
                  'limit': limit,
                  'concept_fields': concept_fields}
        return self.request(method='GET', url='/v2/{0}/related_concepts'.format(full_corpus_path), params=params,
                            accept_json=True)

    def get_corpus_relation_scores(self, corpus, concepts, graph=WIKIPEDIA_EN_LATEST, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        concepts = self._expand_concept_or_document_ids(concepts, graph)
        params = {'concepts': json.dumps(concepts)}
        return self.request(method='GET', url='/v2/{0}/relation_scores'.format(full_corpus_path), params=params,
                            accept_json=True)

    def get_corpus_related_documents(self, corpus, ids, graph=WIKIPEDIA_EN_LATEST, cursor=0, limit=10,
                                     concept_fields=None, document_fields=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        ids = self._expand_concept_or_document_ids(ids, graph)
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        if isinstance(document_fields, dict):
            document_fields = json.dumps(document_fields)
        params = {
            'ids': json.dumps(ids),
            'cursor': cursor,
            'limit': limit,
            'concept_fields': concept_fields,
            'document_fields': document_fields
        }
        return self.request(method='GET', url='/v2/{0}/conceptual_search'.format(full_corpus_path), params=params,
                            accept_json=True)

    def list_documents(self, corpus, limit=20, cursor=0, query=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        params = {
            'limit': limit,
            'cursor': cursor,
            'query': query
        }
        return self.request(method='GET', url='/v2/{0}/documents'.format(full_corpus_path), params=params,
                            accept_json=True)

    def get_document(self, corpus, document, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}/documents/{1}'.format(full_corpus_path, document),
                            accept_json=True)

    def get_document_annotations(self, corpus, document, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}/documents/{1}/annotations'.format(full_corpus_path, document),
                            accept_json=True)

    def get_document_processing_state(self, corpus, document, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='GET', url='/v2/{0}/documents/{1}/processing_state'.format(full_corpus_path, document),
                            accept_json=True)

    def get_document_related_concepts(self, corpus, document, level=1, limit=10, concept_fields=None, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        if isinstance(concept_fields, dict):
            concept_fields = json.dumps(concept_fields)
        params = {
            'level': level,
            'limit': limit,
            'concept_fields': concept_fields
        }
        return self.request(method='GET',
                            url='/v2/{0}/documents/{1}/related_concepts'.format(full_corpus_path, document),
                            params=params, accept_json=True)

    def get_document_relation_scores(self, corpus, document, concepts, graph=WIKIPEDIA_EN_LATEST, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        concept_ids = self._expand_concept_or_document_ids(concepts, graph)
        params = {'concepts': json.dumps(concept_ids)}
        return self.request(method='GET',
                            url='/v2/{0}/documents/{1}/relation_scores'.format(full_corpus_path, document),
                            params=params, accept_json=True)

    def create_document(self, corpus, document, document_contents, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='PUT', url='/v2/{0}/documents/{1}'.format(full_corpus_path, document),
                            json=document_contents)

    def update_document(self, corpus, document, document_contents, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='POST', url='/v2/{0}/documents/{1}'.format(full_corpus_path, document),
                            json=document_contents)

    def delete_document(self, corpus, document, account=None):
        full_corpus_path = self._get_full_corpus_path(corpus, account)
        return self.request(method='DELETE', url='/v2/{0}/documents/{1}'.format(full_corpus_path, document))
