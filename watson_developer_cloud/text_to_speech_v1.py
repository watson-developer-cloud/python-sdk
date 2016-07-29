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
The v1 Text to Speech service
(https://www.ibm.com/watson/developercloud/text-to-speech.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class TextToSpeechV1(WatsonDeveloperCloudService):

    """Client for the Text to Speech service"""
    default_url = "https://stream.watsonplatform.net/text-to-speech/api"

    def __init__(self, url=default_url, **kwargs):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """
        WatsonDeveloperCloudService.__init__(self, 'text_to_speech', url, **kwargs)

    def synthesize(self, text, voice=None, accept=None, customization_id=None):
        """
        Returns the get HTTP response by doing a POST to /synthesize with text, voice, accept
        """
        params = {'voice': voice, 'accept': accept, 'customization_id': customization_id}
        data = {'text': text}
        response = self.request(
            method='POST', url='/v1/synthesize', stream=True, params=params, json=data)
        return response.content

    def voices(self):
        """
        Returns the list of available voices to use with synthesize
        """
        return self.request(method='GET', url='/v1/voices', accept_json=True)

    def pronunciation(self, text, voice=None, pronunciation_format='ipa'):
        params = {
            'text': text,
            'voice': voice,
            'format': pronunciation_format
        }
        return self.request(method='GET', url='/v1/pronunciation', params=params, accept_json=True)

    def customizations(self, language=None):
        params = {
            'language': language
        }
        return self.request(method='GET', url='/v1/customizations', params=params, accept_json=True)

    def get_customization(self, customization_id):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        return self.request(method='GET', url='/v1/customizations/{0}'.format(customization_id), accept_json=True)

    def create_customization(self, name, language=None, description=None):
        body = {
            'name': name,
            'language': language,
            'description': description
        }
        return self.request(method='POST', url='/v1/customizations', json=body, accept_json=True)

    def update_customization(self, customization_id, name=None, description=None, words=None):
        body = {
            'name': name,
            'description': description,
            'words': words
        }
        return self.request(method='POST', url='/v1/customizations/{0}'.format(customization_id), json=body)

    def delete_customization(self, customization_id):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        return self.request(method='DELETE', url='/v1/customizations/{0}'.format(customization_id))

    def get_customization_words(self, customization_id):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        return self.request(method='GET', url='/v1/customizations/{0}/words'.format(customization_id), accept_json=True)

    def add_customization_words(self, customization_id, words):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        body = {
            'words': words
        }
        return self.request(method='POST', url='/v1/customizations/{0}/words'.format(customization_id), json=body)

    def get_customization_word(self, customization_id, word):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        return self.request(method='GET', url='/v1/customizations/{0}/words/{1}'.format(customization_id, word),
                            accept_json=True)

    def set_customization_word(self, customization_id, word, translation):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        body = {
            'translation': translation
        }
        return self.request(method='PUT', url='/v1/customizations/{0}/words/{1}'.format(customization_id, word),
                            json=body)

    def delete_customization_word(self, customization_id, word):
        customization_id = self.unpack_id(customization_id, 'customization_id')
        return self.request(method='DELETE', url='/v1/customizations/{0}/words/{1}'.format(customization_id, word))
