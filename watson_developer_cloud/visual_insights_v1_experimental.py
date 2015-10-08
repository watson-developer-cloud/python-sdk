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

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class VisualInsightsV1Experimental(WatsonDeveloperCloudService):
    """Client for the Visual Insights service"""
    default_url = 'https://gateway.watsonplatform.net/visual-insights-experimental/api'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'visual_insights', url, **kwargs)

    def classifiers(self):
        return self.request(method='GET', url='/v1/classifiers', accept_json=True)

    def summary(self, images_file):
        return self.request(method='POST', url='/v1/summary', files={'images_file': images_file}, accept_json=True)
