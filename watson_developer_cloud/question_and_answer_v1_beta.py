# Copyright 2015 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class QuestionAndAnswerV1Beta(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/question-and-answer-beta/api'
    default_dataset = 'healthcare'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):

        WatsonDeveloperCloudService.__init__(
            self, 'question_and_answer', url, username, password, use_vcap_services)

    def datasets(self):
        """
        Returns the list of available datasets
        """
        return self.request(method='GET', url='/v1/services', accept_json=True)

    def ask(self, question, dataset=default_dataset, items=5):
        """
        Returns an answer to a natural language question
        """

        params = {'question': {
            'evidenceRequest': {'items': items}, 'questionText': question, 'items': items}}
        headers = {'x-synctimeout': 30}

        return self.request(method='POST', url='/v1/question/{}'.format(dataset), json=params, accept_json=True,
                            headers=headers)
