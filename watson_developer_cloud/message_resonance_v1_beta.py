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


class MessageResonanceV1Beta(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/message-resonance-beta/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'message_resonance', url, username, password, use_vcap_services)

    def datasets(self):
        """
        Returns the list of available datasets
        """
        return self.request(method='GET', url='/v1/datasets', accept_json=True)

    def resonance_for_word(self, word, dataset):
        """
        :param word: A single word to retrieve a resonance score for (for a longer input use resonance()
        :param dataset: The index of the dataset to use
        :return: Information about the resonance information (prevalence, volume, etc.) for the word.
        """
        params = {'text': word, 'dataset': dataset}

        return self.request(method='GET', url='/v1/ringscore', params=params, accept_json=True)

    def resonance(self, text, dataset):
        """
        :param text: A string that can contain multiple words
        :param dataset: The index of the dataset to use
        :return: An array of resonance information for each word in the input
        """
        return [self.resonance_for_word(word, dataset) for word in text.split()]
