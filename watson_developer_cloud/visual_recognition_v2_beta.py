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


class VisualRecognitionV2Beta(WatsonDeveloperCloudService):

    """Client for the Visual Recognition service"""

    default_url = 'https://gateway.watsonplatform.net/visual-recognition-beta/api'
    latest_version = '2015-12-02'

    def __init__(self, version, url=default_url, username=None, password=None, use_vcap_services=True):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        :param version: specifies the specific version-date of the service to use
        """

        WatsonDeveloperCloudService.__init__(
            self, 'visual_recognition', url, username, password, use_vcap_services)
        self.version = version

    def get_classifier(self, classifier_id):
        """
        Retrieves information about a specific classifier.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='GET', url='/v2/classifiers/{0}'.format(classifier_id), params=params,
                            accept_json=True)

    def delete_classifier(self, classifier_id):
        """
        Deletes a custom classifier with the specified classifier id.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='DELETE', url='/v2/classifiers/{0}'.format(classifier_id), params=params,
                            accept_json=True)

    def list_classifiers(self, verbose=False):
        """
        Returns a list of user-created and built-in classifiers. (May change in the future to only user-created.)
        :param verbose: Specifies whether to return more information about each classifier, such as the author
        """

        params = {'verbose': verbose, 'version': self.version}
        return self.request(method='GET', url='/v2/classifiers', params=params, accept_json=True)

    def create_classifier(self, name, positive_examples, negative_examples):
        """
        Train a new classifier from example images which are uploaded.
        :param name: The desired short name of the new classifier.
        :param positive_examples: A zip file of images that depict the subject of the new classifier.
        :param negative_examples: A zip file of images that do not depict the subject of the new classifier.
        :return:
        """

        params = {'version': self.version}
        data = {'name': name}
        # Params sent as url parameters here
        return self.request(method='POST', url='/v2/classifiers', files={'positive_examples': positive_examples,
                                                                         'negative_examples': negative_examples},
                            data=data, params=params, accept_json=True)

    def classify(self, images_file, classifier_ids=None):
        """
        Returns a list of classification scores for one or more input images.
        :param images_file: An image file or zip file of image files to analyze.
        :param classifier_ids: The ids of classifiers to consider. When absence, considers all classifiers.
        :return:
        """

        if isinstance(classifier_ids, list):
            classifier_ids = json.dumps(classifier_ids)
        if classifier_ids:
            classifier_ids = '{"classifier_ids": ' + classifier_ids + '}'

        params = {'version': self.version}
        data = {'classifier_ids': classifier_ids}
        # Params sent as url parameters here
        return self.request(method='POST', url='/v2/classify', files={'images_file': images_file}, data=data,
                            params=params, accept_json=True)
