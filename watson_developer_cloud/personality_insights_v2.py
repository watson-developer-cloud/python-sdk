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
The v2 Personality Insights service
(https://www.ibm.com/watson/developercloud/personality-insights.html)
"""

import json
from .watson_developer_cloud_service import WatsonDeveloperCloudService


class PersonalityInsightsV2(WatsonDeveloperCloudService):
    """Wrapper of the Personality Insights service"""
    default_url = 'https://gateway.watsonplatform.net/personality-insights/api'

    def __init__(self, url=default_url, **kwargs):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """

        WatsonDeveloperCloudService.__init__(
            self, 'personality_insights', url, **kwargs)

    def profile(self, text, content_type='text/plain',
                accept='application/json', language=None, csv_headers=False):
        """
        Returns a personality profile given input text (at least 100 unique
        words)
        content_type can be 'text/plain', 'application/json' or 'text/html'
        if accept is set to 'text/csv', returns csv output (with a header row
        if csv_headers is set to True)
        """

        if isinstance(text, dict):
            text = json.dumps(text)
            content_type = 'application/json'

        headers = {'content-type': content_type, 'accept': accept}

        if language:
            headers['content-language'] = language

        params = {}
        if accept == 'text/csv' and csv_headers:
            params['headers'] = 'true'

        response = self.request(
            method='POST', url='/v2/profile', data=text, params=params,
            headers=headers)
        if accept == 'application/json':
            return response.json()
        return response.text
