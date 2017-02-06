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
    """
    All methods taking features use the feature classes
    from watson_developer_cloud/nlu/features/v1

    """
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

    def _analyze(self, featureList, content, contentKind):
        body = None
        feature_dict = {}
        for feature in featureList:
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

        if len(featureList) < 1:
            raise ValueError("Must supply at least one feature")

        return self.request(method='POST', url='/v1/analyze',
                            params={"version": self.version},
                            headers={'content-type': 'application/json'},
                            data=body,
                            accept_json=True)

    def analyzeText(self, features, text):
        """
        Analyze the supplied text for the supplied features.
        :param features: a list of features
        :param text: the text to analyze
        :return: a diction of the resulting data
        """
        return self._analyze(features, text, 'text')

    def analyzeHtml(self, features, html):
        """
        Analyse the supplied html for the supplied features
        :param features: a list of features
        :param html: the html to analyze
        :return: a diction of the resulting data
        """
        return self._analyze(features, html, 'html')

    def analyzeURL(self, features, url):
        """
        Fetch the supplied url and analyze it
        :param features: a list of features
        :param url: the url to fetch
        :return: a diction of the resulting data
        """
        return self._analyze(features, url, 'url')
