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
The v1 Visual Recognition service
(https://www.ibm.com/smarterplanet/us/en/ibmwatson/developercloud/visual-recognition.html)
"""
import json
from .watson_developer_cloud_service import WatsonDeveloperCloudService


class VisualRecognitionV1Beta(WatsonDeveloperCloudService):

    """Client for the Visual Recognition service"""

    default_url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api'

    def __init__(self, url=default_url, username=None, password=None, use_vcap_services=True):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """

        WatsonDeveloperCloudService.__init__(
            self, 'visual_recognition', url, username, password, use_vcap_services)

    def labels(self, labels_to_check=None):
        """
        Returns a personality profile given input text (at least 100 unique words)
        """

        if isinstance(labels_to_check, dict):
            labels_to_check = json.dumps(labels_to_check)

        params = {'labels_to_check': labels_to_check}
        return self.request(method='GET', url='/v1/tag/labels', params=params, accept_json=True)

    def recognize(self, image_file, labels_to_check=None):
        """
        Provides a set of tags for in image. Set labels_to_check to limit the possible tags (and increase speed).
        labels_to_check should be a dict or string of the form: {"label_groups": [...], "labels": [...]}
        where either label_groups, labels or both are a list of strings.
        """

        if isinstance(labels_to_check, dict):
            labels_to_check = json.dumps(labels_to_check)

        params = {'labels_to_check': labels_to_check}
        # Params sent as url parameters here
        return self.request(method='POST', url='/v1/tag/recognize', files={'image_file': image_file}, data=params,
                            accept_json=True)
