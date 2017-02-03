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
The v1 Natural Language Classifier service
(https://www.ibm.com/watson/developercloud/nl-classifier.html)
"""

import json
from watson_developer_cloud.watson_developer_cloud_service import \
    WatsonDeveloperCloudService


class NaturalLanguageClassifierV1(WatsonDeveloperCloudService):
    default_url = 'https://gateway.watsonplatform.net/natural-language' \
                  '-classifier/api'

    def __init__(self, url=default_url, **kwargs):
        WatsonDeveloperCloudService.__init__(
            self, 'natural_language_classifier', url, **kwargs)

    def create(self, training_data, name=None, language='en'):
        """
        :param training_data: A csv file representing the training data
        :param name: The optional descriptive name for the classifier
        :param language: The language of the input data, i.e. 'en'
        :return: A JSON object with the classifier_id of the newly created
        classifier, still in training
        """
        params = {'language': language, 'name': name}
        return self.request(method='POST', url='/v1/classifiers',
                            accept_json=True,
                            files=[('training_metadata',
                                    ('training.json', json.dumps(params))),
                                   ('training_data', training_data)])

    def list(self):
        return self.request(method='GET', url='/v1/classifiers',
                            accept_json=True)

    def status(self, classifier_id):
        classifier_id = self.unpack_id(classifier_id, 'classifier_id')
        return self.request(method='GET',
                            url='/v1/classifiers/{0}'.format(classifier_id),
                            accept_json=True)

    def classify(self, classifier_id, text):
        classifier_id = self.unpack_id(classifier_id, 'classifier_id')
        return self.request(method='POST',
                            url='/v1/classifiers/{0}/classify'.format(
                                classifier_id), accept_json=True,
                            json={'text': text})

    def remove(self, classifier_id):
        classifier_id = self.unpack_id(classifier_id, 'classifier_id')
        return self.request(method='DELETE',
                            url='/v1/classifiers/{0}'.format(classifier_id),
                            accept_json=True)
