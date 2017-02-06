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

from watson_developer_cloud.watson_developer_cloud_service import \
    WatsonDeveloperCloudService
import json

base_url = 'https://gateway.watsonplatform.net'
default_url = '{0}/natural-language-understanding/api'.format(base_url)
latest_version = '2017-01-23'


class NaturalLanguageUnderstandingV1(WatsonDeveloperCloudService):
    def __init__(self,
                 version,
                 url=default_url,
                 username=None,
                 password=None,
                 use_vcap_services=True):
        WatsonDeveloperCloudService.__init__(
            self, 'natural_language_understanding', url,
            username, password, use_vcap_services)
        self.version = version

    def _analyze(self, features, content, contentKind):
        body = None
        feature_dict = {}
        for feature in features:
            feature_dict[feature.name()] = feature.toDict()

        if contentKind == 'text':
            body = json.dumps({'text': content, 'features': feature_dict})
        elif contentKind == 'html':
            body = json.dumps({'html': content, 'features': feature_dict})
        elif contentKind == 'url':
            body = json.dumps({'url': content, 'features': feature_dict})
        else:
            msg = "contentKind must be one of html, text, or url"
            raise ValueError(msg)

        return self.request(method='POST', url='/v1/analyze',
                            params={"version": self.version},
                            headers={'content-type': 'application/json'},
                            data=body,
                            accept_json=True)

    def analyzeText(self, features, text):
        return self._analyze(features, text, 'text')

    def analyzeHtml(self, features, html):
        return self._analyze(features, html, 'html')

    def analyzeURL(self, features, url):
        return self._analyze(features, url, 'url')
