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
The AlchemyAPI Vision service
(http://www.alchemyapi.com/products/alchemyvision)
"""

from .watson_developer_cloud_service import WatsonDeveloperCloudService
from .watson_developer_cloud_service import WatsonInvalidArgument


class AlchemyVisionV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway-a.watsonplatform.net/calls'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(self, 'alchemy_api', url, **kwargs)

    def recognize_faces(self, image_file=None, image_url=None, knowledge_graph=False):
        params = {'outputMode': 'json'}
        if knowledge_graph:
            params['knowledgeGraph'] = 1
        headers = {}
        image_contents = None

        if image_file:
            params['imagePostMode'] = 'raw'
            image_contents = image_file.read()
            # headers['content-length'] = sys.getsizeof(image_contents)
            url = '/image/ImageGetRankedImageFaceTags'
        elif image_url:
            params['imagePostMode'] = 'not-raw'
            params['url'] = image_url
            url = '/url/URLGetRankedImageFaceTags'
        else:
            raise WatsonInvalidArgument('image_file or image_url must be specified')

        # Params sent as url parameters here
        return self.request(method='POST', url=url, params=params, data=image_contents, headers=headers,
                            accept_json=True)
