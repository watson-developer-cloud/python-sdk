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
The v1 Language Translation service
(https://http://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/language-translation.html)
"""

from watson_developer_cloud.watson_developer_cloud_service import WatsonDeveloperCloudService


class LanguageTranslationV2(WatsonDeveloperCloudService):
    default_url = "https://gateway.watsonplatform.net/language-translation/api"

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(
            self, 'language_translation', url, **kwargs)

    def identify(self, text):
        """
        Identifies the language of given source text
        """
        return self.request(method='POST', url='/v2/identify', data=text, headers={'content-type': 'text/plain'},
                            accept_json=True)

    def get_models(self, default=None, source=None, target=None):
        """
        Get the available models for translation
        """
        params = {'default': default, 'source': source, 'target': target}
        return self.request(method='GET', url='/v2/models', params=params, accept_json=True)

    def translate(self, text, source=None, target=None, model=None):
        """
        Translates text from a source language to a target language
        """
        data = {'text': text, 'source': source,
                'target': target, 'model': model}

        # data=data or json=data
        return self.request(method='POST', url='/v2/translate', json=data).text
