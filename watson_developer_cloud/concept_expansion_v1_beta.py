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

from .watson_developer_cloud_service import WatsonDeveloperCloudService


def _format_status(status):
    status_mapping = {'A': {'status': 'awaiting work'},
                      'G': {'status': 'in progress'},
                      'F': {'status': 'failed', 'error': 'job failed'},
                      'D': {'status': 'done'}}
    try:
        return status_mapping[status['state']]
    except ValueError:
        return {'status': 'error', 'error': 'invalid json: {0}'.format(status)}
    except KeyError:
        return {'status': 'error', 'error': 'missing json data: {0}'.format(status)}


class ConceptExpansionV1Beta(WatsonDeveloperCloudService):

    """The Concept Expansion service analyzes text and interprets its meaning
    based on usage in other similar contexts.
    """
    default_url = 'https://gateway.watsonplatform.net/concept-expansion-beta/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'concept_expansion', url, username, password, use_vcap_services)

    def create_job(self, dataset, seeds, label=''):
        """
        Creates a new asynchronous job that will compute the
        list of expanded concepts

        @param dataset  the domain to use ('mtsamples' or 'social')
        @param seeds  the list of initial search terms
        @param label  label of the new job
        """
        params = {'dataset': dataset, 'seeds': seeds, 'label': label}
        return self.request(method='POST', url='/v1/upload', json=params, accept_json=True)

    def get_status(self, job_id):
        """
        Checks the status of a previously created job

        @param job_id  job id to get status of
        """
        if isinstance(job_id, dict) and 'jobid' in job_id:
            job_id = job_id['jobid']
        params = {'jobid': job_id}
        results = self.request(
            method='GET', url='/v1/status', params=params, accept_json=True)
        return _format_status(results)

    def get_results(self, job_id):
        """
        Returns the results of a previously created job

        @param job_id  job id to get status of
        """
        if isinstance(job_id, dict) and 'jobid' in job_id:
            job_id = job_id['jobid']
        params = {'jobid': job_id}
        return self.request(method='PUT', url='/v1/result', json=params, accept_json=True)
