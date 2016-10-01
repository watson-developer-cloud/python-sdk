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
The AlchemyAPI Vision service
(https://www.ibm.com/watson/developercloud/visual-recognition.html)
"""
from __future__ import print_function
from .watson_developer_cloud_service import WatsonDeveloperCloudService



class AlchemyVisionV1(WatsonDeveloperCloudService):
    """AlchemyVision was deprecated, migrate your application to use VisualRecognition."""
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)
        print('WARNING: The AlchemyVision service was deprecated, use VisualRecognitionV3 instead')

    def get_image_keywords(self, image_file=None, image_url=None, knowledge_graph=False, force_show_all=False):
        method_name = 'GetRankedImageKeywords'
        params = {'knowledgeGraph': knowledge_graph,
                  'forceShowAll': force_show_all}
        return self._alchemy_image_request(method_name, image_file, image_url, params)

    def recognize_faces(self, image_file=None, image_url=None, knowledge_graph=False):
        method_name = 'GetRankedImageFaceTags'
        params = {'knowledgeGraph': knowledge_graph}
        return self._alchemy_image_request(method_name, image_file, image_url, params)

    def get_image_scene_text(self, image_file=None, image_url=None):
        method_name = 'GetRankedImageSceneText'
        return self._alchemy_image_request(method_name, image_file, image_url)

    def get_image_links(self, url=None, html=None):
        method_name = 'GetImage'
        return self._alchemy_html_request(method_name, url=url, html=html)
