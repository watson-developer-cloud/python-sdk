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
The AlchemyAPI Language service
(http://www.alchemyapi.com/products/alchemylanguage)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class AlchemyLanguageV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)

    def sentiment(self, html=None, text=None, url=None):
        return self._alchemy_html_request('GetTextSentiment', html=html, text=text, url=url)

    # FIXME: Should provide a way to provide multiple targets
    def targeted_sentiment(self, target, html=None, text=None, url=None):
        params = {'target': target}
        return self._alchemy_html_request('GetTargetedSentiment', html=html, text=text, url=url, params=params)
