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
The v2-experimental Tone Analyzer service
(https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/tone-analyzer.html)
"""


from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService


class ToneAnalyzerV2Experimental(WatsonDeveloperCloudService):
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
        return self.request(method='GET', url='/v2/scorecards', accept_json=True)

    def synonyms(self, word):
        """
        The Synonyms API call returns words or terms related to an input word. Each word includes a score, a correlation
        to a given trait: allowing to determine if replacing that word would level up or down a given trait.

        @param word  the word or phrase to lookup synonyms for
        """
        params = {'word': word}
        return self.request(method='GET', url='/v2/synonyms', params=params, accept_json=True)

    def tone(self, text, scorecard=None):
        """
        The tone API is the main API call: it analyzes the "tone" of a piece of text. The message is analyzed from
        several tones (social tone, emotional tone, writing tone), and for each of them various traits are derived
        (such as conscientiousness, agreeableness, openness).
        """
        data = {'text': text, 'scorecard': scorecard}
        return self.request(method='POST', url='/v2/tone', json=data, accept_json=True)
