# Copyright 2016 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The v1 Tradeoff Analytics service
(https://www.ibm.com/watson/developercloud/tradeoff-analytics.html)
"""

from .watson_service import WatsonService


class TradeoffAnalyticsV1(WatsonService):
    """Wrapper for the Tradeoff Analytics service"""
    default_url = 'https://gateway.watsonplatform.net/tradeoff-analytics/api'

    def __init__(self, url=default_url, **kwargs):
        WatsonService.__init__(self, 'tradeoff_analytics', url, **kwargs)

    def dilemmas(self, params,
                 generate_visualization=True,
                 find_preferable_options=False):
        """
        :param params: The JSON problem (subject, columns, and options)
        :param generate_visualization: If True, returns the map visualization
        used by the Tradeoff Analytics widget
        :param find_preferable_options: If True, returns a refined subset of
        best candidate options that will most likely satisfy the greatest number
        of users
        :return: A dilemma that contains the problem and its resolution
        """

        parameters = {
            'generate_visualization': generate_visualization,
            'find_preferable_options': find_preferable_options
        }

        return self.request(method='POST', url='/v1/dilemmas', json=params,
                            params=parameters, accept_json=True)
