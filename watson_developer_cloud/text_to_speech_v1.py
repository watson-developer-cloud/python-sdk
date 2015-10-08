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
The v1 Text to Speech service
(https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/text-to-speech.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class TextToSpeechV1(WatsonDeveloperCloudService):

    """Client for the Text to Speech service"""
    default_url = "https://stream.watsonplatform.net/text-to-speech/api"

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """
        WatsonDeveloperCloudService.__init__(
            self, 'text_to_speech', url, username, password, use_vcap_services)

    def synthesize(self, text, voice=None, accept=None):
        """
        Returns the get HTTP response by doing a GET to /synthesize with text, voice, accept
        """
        params = {'text': text, 'voice': voice, 'accept': accept}
        response = self.request(
            method='GET', url='/v1/synthesize', stream=True, params=params)
        return response.content

    def voices(self):
        """
        Returns the list of available voices to use with synthesize
        """
        return self.request(method='GET', url='/v1/voices', accept_json=True)
