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
The v3 Visual Recognition service
(https://www.ibm.com/watson/developercloud/visual-recognition.html)
"""
import json
import mimetypes

from .watson_developer_cloud_service import WatsonDeveloperCloudService


class VisualRecognitionV3(WatsonDeveloperCloudService):
    """Client for the Visual Recognition service"""

    default_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api'
    latest_version = '2016-05-20'

    def __init__(self, version, url=default_url, **kwargs):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        :param version: specifies the specific version-date of the service to
        use, for example '2016-05-20'
        :param api_key: specifies the credentials for the service (doesn't
        use username and password)
        """

        WatsonDeveloperCloudService.__init__(self, 'watson_vision_combined',
                                             url, **kwargs)
        self.version = version

    def get_classifier(self, classifier_id):
        """
        Retrieves information about a specific classifier.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='GET',
                            url='/v3/classifiers/{0}'.format(classifier_id),
                            params=params,
                            accept_json=True)

    def delete_classifier(self, classifier_id):
        """
        Deletes a custom classifier with the specified classifier id.
        :param classifier_id: The classifier id
        """

        params = {'version': self.version}
        return self.request(method='DELETE',
                            url='/v3/classifiers/{0}'.format(classifier_id),
                            params=params,
                            accept_json=True)

    def list_classifiers(self, verbose=False):
        """
        Returns a list of user-created and built-in classifiers. (May change
        in the future to only user-created.)
        :param verbose: Specifies whether to return more information about
        each classifier, such as the author
        """

        params = {'verbose': verbose, 'version': self.version}
        return self.request(method='GET', url='/v3/classifiers', params=params,
                            accept_json=True)

    def create_classifier(self, name, **kwargs):
        """
        Train a new classifier from example images which are uploaded.
        :param name: The desired short name of the new classifier.
        :param <NAME>_positive_examples: zip files of images that depict the
        subject of the new classifier.
        :param negative_examples: A zip file of images that do not depict the
        subject of the new classifier.
        :return:
        """

        params = {'version': self.version}
        data = {'name': name}
        # Params sent as url parameters here
        return self.request(method='POST', url='/v3/classifiers', files=kwargs,
                            data=data, params=params,
                            accept_json=True)

    def update_classifier(self, classifier_id, **kwargs):
        """
        Updates an existing classifier by adding images to existing or new
        classes.
        :param classifier_id: The id of the classifier to update.
        :param <NAME>_positive_examples: zip files of images that depict the
        subject of the class.
        :param negative_examples: A zip file of images that do not depict the
        subject of any of the classes.
        :return:
        """

        params = {'version': self.version}
        # Params sent as url parameters here
        return self.request(method='POST',
                            url='/v3/classifiers/{0}'.format(classifier_id),
                            files=kwargs,
                            params=params, accept_json=True)

    def _image_call(self, url, images_file=None, images_url=None, params=None):
        if images_file is None and images_url is None:
            raise AssertionError('You must specify either a file or a url')

        if images_url:
            params['url'] = images_url
            return self.request(method='GET', url=url, params=params,
                                accept_json=True)
        filename = images_file.name
        mime_type = mimetypes.guess_type(
            filename)[0] or 'application/octet-stream'
        return self.request(method='POST', url=url,
                            files={'images_file': (
                                filename, images_file, mime_type)},
                            params=params,
                            accept_json=True)

    def classify(self, images_file=None, images_url=None, classifier_ids=None,
                 owners=None, threshold=None):
        """
        Returns a list of classification scores for one or more input images.
        :param images_file: An image file or zip file of image files to
        analyze.
        :param images_url: The url for an image file or zip file of images to
        analyze.
        :param classifier_ids: The ids of classifiers to consider. When
        absent, considers all classifiers.
        :return:
        """

        if isinstance(classifier_ids, list):
            classifier_ids = ','.join(classifier_ids)
        if isinstance(owners, list):
            owners = ','.join(owners)

        params = {'version': self.version, 'classifier_ids': classifier_ids,
                  'owners': owners, 'threshold': threshold}
        return self._image_call('/v3/classify', images_file, images_url,
                                params)

    def detect_faces(self, images_file=None, images_url=None):
        """
        Returns a list of faces detected.  This includes identities for
        famous people.
        :param images_file: An image file or zip file of image files to
        analyze.
        :param images_url: The url for an image file or zip file of images to
        analyze.
        :return:
        """

        params = {'version': self.version}
        return self._image_call('/v3/detect_faces', images_file, images_url,
                                params)

    def recognize_text(self, images_file=None, images_url=None):
        """
        Returns a list of recognized text
        :param images_file: An image file or zip file of image files to
        analyze.
        :param images_url: The url for an image file or zip file of images to
        analyze.
        :return:
        """

        params = {'version': self.version}
        return self._image_call('/v3/recognize_text', images_file, images_url,
                                params)

    def create_collection(self, name):
        """
        Create a new collection of images to search. You can create a maximum
        of 5 collections.

        :param name:   The name of the new collection. The name can be a
        maximum of 128 UTF8 characters, with no spaces.
        :return:
        """

        return self.request(method='POST', url='/v3/collections',
                            params={'version': self.version},
                            files={'name': (None, name)},
                            accept_json=True)

    def get_collection(self, collection_id):
        """
        Retrieve collection details
        :param collection_id: a valid collection id
        :return:
        """
        return self.request(method='POST',
                            url='/v3/collections/{0}'.format(collection_id),
                            params={'version': self.version},
                            accept_json=True)

    def list_collections(self):
        """
        List all custom collections.
        :return:
        """
        return self.request(method='GET', url='/v3/collections',
                            params={'version': self.version},
                            accept_json=True)

    def delete_collection(self, collection_id):
        """
        Delete a user created collection
        :param collection_id: a valid collection id
        :return:
        """
        return self.request(method='DELETE',
                            url='/v3/collections/{0}'.format(collection_id),
                            params={'version': self.version},
                            accept_json=True)

    def add_image(self, collection_id, image_file, metadata=None):
        """
        Add an image to a collection
        :param collection_id: a valid collection id
        :param image_file: a file object of an image
        :param metadata: metadata describing the image, must be convertable to
        JSON
        :return:
        """
        metadata = metadata or {}
        filename = image_file.name
        mime_type = mimetypes.guess_type(
            filename)[0] or 'application/octet-stream'
        return self.request(method='POST',
                            url='/v3/collections/{0}/images'.format(
                                collection_id),
                            params={'version': self.version},
                            files={
                                'image_file': (
                                    filename, image_file, mime_type),
                                'metadata': (
                                    'metadata.json', json.dumps(metadata),
                                    'application/json')},
                            accept_json=True)

    def list_images(self, collection_id):
        """
        list images in a given collection
        :param collection_id:  valid collection id
        :return:
        """
        return self.request(method='GET',
                            url='/v3/collections/{0}/images'.format(
                                collection_id),
                            params={'version': self.version},
                            accept_json=True)

    def get_image(self, collection_id, image_id):
        """
        Get an image from a collection
        :param collection_id: valid collection id
        :param image_id: valid image id
        :return:
        """
        return self.request(method='GET',
                            url='/v3/collections/{0}/images/{1}'.format(
                                collection_id, image_id),
                            params={'version': self.version},
                            accept_json=True)

    def delete_image(self, collection_id, image_id):
        """
        delete the specified image
        :param collection_id: valid collection id
        :param image_id: valid image id
        :return:
        """
        return self.request(method='DELETE',
                            url='/v3/collections/{0}/images/{1}'.format(
                                collection_id, image_id),
                            params={'version': self.version},
                            accept_json=True)

    def set_image_metadata(self, collection_id, image_id, metadata):
        """
        sets/overwrites the image metadata
        :param collection_id: valid collection id
        :param image_id: valid image id
        :param metadata: key/value hash to set for the metadata
        :return:
        """
        return self.request(method='PUT',
                            url='/v3/collections/{0}/images/{1}/metadata'
                            .format(collection_id, image_id),
                            params={'version': self.version},
                            files={'metadata': (
                                'metadata.json', json.dumps(metadata),
                                'application/json')},
                            accept_json=True)

    def get_image_metadata(self, collection_id, image_id):
        """
        Return image metadata
        :param collection_id: valid collection id
        :param image_id: valid image id
        :return:
        """
        return self.request(method='GET',
                            url='/v3/collections/{0}/images/{1}/metadata'
                            .format(collection_id, image_id),
                            params={'version': self.version},
                            accept_json=True)

    def delete_image_metadata(self, collection_id, image_id):
        """
        Delete image metadata
        :param collection_id: valid collection id
        :param image_id: valid image id
        :return:
        """
        return self.request(method='DELETE',
                            url='/v3/collections/{0}/images/{1}/metadata'
                            .format(collection_id, image_id),
                            params={'version': self.version},
                            accept_json=True)

    def find_similar(self, collection_id, image_file, limit=10):
        """
        find similar images
        :param collection_id: valid collection id
        :param image_file: image file to use for searching
        :param limit: number of returned results (default is 10)
        :return:
        {
           "similar_images":[
             {
              "image_id":"dresses_1257263",
              "created":"2016-09-04T21:49:16.908Z",
              "metadata":{
                "weight":10,
                "cut":"a line",
                "color":"red"
               },
               "score":"0.79"
             }
            ],
           "image_file":"red_dress.jpg",
           "images_processed": 1
        }
        """
        mime_type = mimetypes.guess_type(
            image_file.name)[0] or 'application/octet-stream'
        return self.request(method='POST',
                            url='/v3/collections/{0}/find_similar'.format(
                                collection_id),
                            params={'version': self.version, 'limit': limit},
                            files={'image_file': (image_file.name, image_file,
                                                  mime_type)},
                            accept_json=True)
