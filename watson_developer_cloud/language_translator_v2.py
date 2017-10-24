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
The v2 Language Translator service
(https://www.ibm.com/watson/developercloud/language-translator.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService
from .watson_developer_cloud_service import WatsonInvalidArgument


class LanguageTranslatorV2(WatsonDeveloperCloudService):
    default_url = "https://gateway.watsonplatform.net/language-translator/api"

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'language_translator', url,
                                             **kwargs)

    def identify(self, text):
        """
        Identifies the language of given source text
        """
        return self.request(method='POST', url='/v2/identify', data=text,
                            headers={'content-type': 'text/plain'},
                            accept_json=True)

    def get_identifiable_languages(self):
        return self.request(method='GET', url='/v2/identifiable_languages',
                            accept_json=True)

    def get_models(self, default=None, source=None, target=None):
        """
        Get the available models for translation
        """
        params = {'default': default, 'source': source, 'target': target}
        return self.request(method='GET', url='/v2/models', params=params,
                            accept_json=True)

    def create_model(self, base_model_id, name=None, forced_glossary=None,
                     parallel_corpus=None,
                     monolingual_corpus=None):
        if forced_glossary is None and parallel_corpus is None and \
                        monolingual_corpus is None:
            raise WatsonInvalidArgument(
                'A glossary or corpus must be provided')
        params = {'name': name,
                  'base_model_id': base_model_id}
        files = {'forced_glossary': forced_glossary,
                 'parallel_corpus': parallel_corpus,
                 'monolingual_corpus': monolingual_corpus}
        return self.request(method='POST', url='/v2/models', params=params,
                            files=files, accept_json=True)

    def get_model(self, model_id):
        return self.request(method='GET',
                            url='/v2/models/{0}'.format(model_id),
                            accept_json=True)

    def delete_model(self, model_id):
        return self.request(method='DELETE',
                            url='/v2/models/{0}'.format(model_id),
                            accept_json=True)

    def translate(self, text, source=None, target=None, model_id=None):
        """
        Translates text from a source language to a target language
        """
        if model_id is None and (source is None or target is None):
            raise WatsonInvalidArgument(
                'Either model_id or source and target must be specified')

        data = {'text': text, 'source': source, 'target': target,
                'model_id': model_id}

        # data=data or json=data
        return self.request(method='POST', url='/v2/translate', json=data).text
