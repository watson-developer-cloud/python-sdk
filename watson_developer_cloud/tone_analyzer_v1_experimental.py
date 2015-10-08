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
The v1-experimental Tone Analyzer service
(https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/tone-analyzer.html)
"""

from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService


class ToneAnalyzerV1Experimental(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/tone-analyzer-experimental/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'tone_analyzer', url, username, password, use_vcap_services)

    def scorecards(self):
        """
        Returns a list of available scorecards. Scorecards are implementations of Tone evaluations for different
        domains. When calling the Tone API, a specific scorecard can be requested to be used. The default scorecard is
        "email", for business communications.

        This API returns only one scorecard, which is the initial implementation, and is left reserved to list
        additional scorecards in future versions.
        """

        response = self.request(
            method='GET', url='/v1/scorecards', headers={'accept': 'application/json'})
        return response.json()

    def synonym(self, words, limit=None, traits=None, hops=None, context=None, index=None):
        """
        The Synonym API call returns words or terms related to an input word. Each word includes a score, a correlation
        to a given trait: allowing to determine if replacing that word would level up or down a given trait.

        @param words  array of words
        """
        data = {'words': words, 'limit': limit, 'traits': traits,
                'hops': hops, 'context': context, 'index': index}
        return self.request(method='Post', url='/v1/synonym', json=data, accept_json=True)

    def tone(self, text, scorecard=None):
        """
        The tone API is the main API call: it analyzes the "tone" of a piece of text. The message is analyzed from
        several tones (social tone, emotional tone, writing tone), and for each of them various traits are derived
        (such as conscientiousness, agreeableness, openness).

        This API call takes a POST http verb. It accepts both a text/plain and application/json media types, and
        returns a application/json response. The first one just analyzes a piece of text using the default scorecard.
        The JSON version allows to specify the scorecard to use (though the initial version of the service supports a
        single scorecard: business email)
        """
        data = {'text': text, 'scorecard': scorecard}
        return self.request(method='POST', url='/v1/tone', json=data, accept_json=True)
