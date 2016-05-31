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
The v3 Tone Analyzer service
(https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/tone-analyzer.html)
"""


from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService


class ToneAnalyzerV3(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/tone-analyzer/api'
    latest_version = '2016-02-11'

    def __init__(self, version, url=default_url, username=None, password=None, use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'tone_analyzer', url, username, password, use_vcap_services)
        self.version = version

    def tone(self, text):
        """
        The tone API is the main API call: it analyzes the "tone" of a piece of text. The message is analyzed from
        several tones (social tone, emotional tone, writing tone), and for each of them various traits are derived
        (such as conscientiousness, agreeableness, openness).
        :param text: Text to analyze
        """
        params = {'version': self.version}
        data = {'text': text}
        return self.request(method='POST', url='/v3/tone', params=params, json=data, accept_json=True)
