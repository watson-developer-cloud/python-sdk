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
The AlchemyData News service
(http://www.alchemyapi.com/products/alchemydata-news)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class AlchemyDataNewsV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)

    # INCOMPLETE
    def get_news_documents(self, start, end, max_results=10, return_fields=None):
        params = {'start': start,
                  'end': end,
                  'maxResults': max_results}
        return self._alchemy_html_request(method_url='/data/GetNews', method='GET', params=params)

    # INCOMPLETE
    def get_volume(self, start, end, time_slice=None):
        params = {'start': start,
                  'end': end,
                  'timeSlice': time_slice}
        return self._alchemy_html_request(method_url='/data/GetNews', method='GET', params=params)
