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
The AlchemyData News service
(https://www.ibm.com/watson/developercloud/alchemy-data-news.html)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class AlchemyDataNewsV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)

    def get_news_documents(self, start, end, max_results=10, query_fields=None, return_fields=None, time_slice=None,
                           next_page=None, dedup=None, dedup_threshold=None, rank=None):
        if isinstance(return_fields, list):
            return_fields = ','.join(return_fields)
        params = {'start': start,
                  'end': end,
                  'maxResults': max_results,
                  'return': return_fields,
                  'timeSlice': time_slice,
                  'next': next_page,
                  'dedup': dedup,
                  'dedupThreshold': dedup_threshold,
                  'rank': rank}
        if isinstance(query_fields, dict):
            for key in query_fields:
                params[key if key.startswith('q.') else 'q.' + key] = query_fields[key]
        return self._alchemy_html_request(method_url='/data/GetNews', method='GET', params=params)
