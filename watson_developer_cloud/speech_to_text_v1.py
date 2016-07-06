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
The v1 Speech to Text service
(https://www.ibm.com/watson/developercloud/speech-to-text.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class SpeechToTextV1(WatsonDeveloperCloudService):
    default_url = "https://stream.watsonplatform.net/speech-to-text/api"

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):

        WatsonDeveloperCloudService.__init__(
            self, 'speech_to_text', url, username, password, use_vcap_services)

    def recognize(self, audio, content_type, continuous=False, model=None, inactivity_timeout=None,
                  keywords=None, keywords_threshold=None, max_alternatives=None, word_alternatives_threshold=None,
                  word_confidence=None, timestamps=None, interim_results=None):
        """
        Returns the recognized text from the audio input
        """
        headers = {'content-type': content_type}
        params = {'continuous': continuous,
                  'inactivityTimeout': inactivity_timeout,
                  'keywords': keywords,
                  'keywordsThreshold': keywords_threshold,
                  'maxAlternatives': max_alternatives,
                  'model': model,
                  'wordAlternativesThreshold': word_alternatives_threshold,
                  'wordConfidence': word_confidence,
                  'timestamps': timestamps,
                  'interimResults': interim_results}

        return self.request(method='POST', url='/v1/recognize', headers=headers, data=audio, params=params,
                            stream=True, accept_json=True)

    def models(self):
        """
        Returns the list of available models to use with recognize
        """
        return self.request(method='GET', url='/v1/models', accept_json=True)
