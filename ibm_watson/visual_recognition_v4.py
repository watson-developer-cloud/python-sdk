# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2020.
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
Provide images to the IBM Watson&trade; Visual Recognition service for analysis. The
service detects objects based on a set of images with training data.
"""

import json
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from .common import get_sdk_headers
from datetime import datetime
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import DetailedResponse
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from typing import BinaryIO
from typing import Dict
from typing import List
from typing import TextIO

##############################################################################
# Service
##############################################################################


class VisualRecognitionV4(BaseService):
    """The Visual Recognition V4 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/visual-recognition/api'
    DEFAULT_SERVICE_NAME = 'visual_recognition'

    def __init__(
            self,
            version: str,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Visual Recognition service.

        :param str version: The API version date to use with the service, in
               "YYYY-MM-DD" format. Whenever the API is changed in a backwards
               incompatible way, a new minor version of the API is released.
               The service uses the API version for the date you specify, or
               the most recent version before that date. Note that you should
               not programmatically specify the current date at runtime, in
               case the API has been updated since your application's release.
               Instead, specify a version date that is compatible with your
               application, and don't change it until your application is
               ready for a later version.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator,
                             disable_ssl_verification=False)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Analysis
    #########################

    def analyze(self,
                collection_ids: str,
                features: str,
                *,
                images_file: BinaryIO = None,
                image_url: str = None,
                threshold: float = None,
                **kwargs) -> 'DetailedResponse':
        """
        Analyze images.

        Analyze images by URL, by file, or both against your own collection. Make sure
        that **training_status.objects.ready** is `true` for the feature before you use a
        collection to analyze images.
        Encode the image and .zip file names in UTF-8 if they contain non-ASCII
        characters. The service assumes UTF-8 encoding if it encounters non-ASCII
        characters.

        :param List[str] collection_ids: The IDs of the collections to analyze.
        :param List[str] features: The features to analyze.
        :param list[FileWithMetadata] images_file: (optional) An array of image
               files (.jpg or .png) or .zip files with images.
               - Include a maximum of 20 images in a request.
               - Limit the .zip file to 100 MB.
               - Limit each image file to 10 MB.
               You can also include an image with the **image_url** parameter.
        :param List[str] image_url: (optional) An array of URLs of image files
               (.jpg or .png).
               - Include a maximum of 20 images in a request.
               - Limit each image file to 10 MB.
               - Minimum width and height is 30 pixels, but the service tends to perform
               better with images that are at least 300 x 300 pixels. Maximum is 5400
               pixels for either height or width.
               You can also include images with the **images_file** parameter.
        :param float threshold: (optional) The minimum score a feature must have to
               be returned.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_ids is None:
            raise ValueError('collection_ids must be provided')
        if features is None:
            raise ValueError('features must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='analyze')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        collection_ids = self._convert_list(collection_ids)
        form_data.append(
            ('collection_ids', (None, collection_ids, 'text/plain')))
        features = self._convert_list(features)
        form_data.append(('features', (None, features, 'text/plain')))
        if images_file:
            for item in images_file:
                form_data.append(('images_file', (item.filename, item.data,
                                                  item.content_type or
                                                  'application/octet-stream')))
        if image_url:
            for item in image_url:
                form_data.append(
                    ('image_url', (None, item, 'application/json')))
        if threshold:
            threshold = str(threshold)
            form_data.append(('threshold', (None, threshold, 'text/plain')))

        url = '/v4/analyze'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Collections
    #########################

    def create_collection(self,
                          *,
                          name: str = None,
                          description: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Create a collection.

        Create a collection that can be used to store images.
        To create a collection without specifying a name and description, include an empty
        JSON object in the request body.
        Encode the name and description in UTF-8 if they contain non-ASCII characters. The
        service assumes UTF-8 encoding if it encounters non-ASCII characters.

        :param str name: (optional) The name of the collection. The name can
               contain alphanumeric, underscore, hyphen, and dot characters. It cannot
               begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='create_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'name': name, 'description': description}

        url = '/v4/collections'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def list_collections(self, **kwargs) -> 'DetailedResponse':
        """
        List collections.

        Retrieves a list of collections for the service instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='list_collections')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_collection(self, collection_id: str,
                       **kwargs) -> 'DetailedResponse':
        """
        Get collection details.

        Get details of one collection.

        :param str collection_id: The identifier of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_collection(self,
                          collection_id: str,
                          *,
                          name: str = None,
                          description: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Update a collection.

        Update the name or description of a collection.
        Encode the name and description in UTF-8 if they contain non-ASCII characters. The
        service assumes UTF-8 encoding if it encounters non-ASCII characters.

        :param str collection_id: The identifier of the collection.
        :param str name: (optional) The name of the collection. The name can
               contain alphanumeric, underscore, hyphen, and dot characters. It cannot
               begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='update_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'name': name, 'description': description}

        url = '/v4/collections/{0}'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def delete_collection(self, collection_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Delete a collection.

        Delete a collection from the service instance.

        :param str collection_id: The identifier of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='delete_collection')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Images
    #########################

    def add_images(self,
                   collection_id: str,
                   *,
                   images_file: BinaryIO = None,
                   image_url: str = None,
                   training_data: str = None,
                   **kwargs) -> 'DetailedResponse':
        """
        Add images.

        Add images to a collection by URL, by file, or both.
        Encode the image and .zip file names in UTF-8 if they contain non-ASCII
        characters. The service assumes UTF-8 encoding if it encounters non-ASCII
        characters.

        :param str collection_id: The identifier of the collection.
        :param list[FileWithMetadata] images_file: (optional) An array of image
               files (.jpg or .png) or .zip files with images.
               - Include a maximum of 20 images in a request.
               - Limit the .zip file to 100 MB.
               - Limit each image file to 10 MB.
               You can also include an image with the **image_url** parameter.
        :param List[str] image_url: (optional) The array of URLs of image files
               (.jpg or .png).
               - Include a maximum of 20 images in a request.
               - Limit each image file to 10 MB.
               - Minimum width and height is 30 pixels, but the service tends to perform
               better with images that are at least 300 x 300 pixels. Maximum is 5400
               pixels for either height or width.
               You can also include images with the **images_file** parameter.
        :param str training_data: (optional) Training data for a single image.
               Include training data only if you add one image with the request.
               The `object` property can contain alphanumeric, underscore, hyphen, space,
               and dot characters. It cannot begin with the reserved prefix `sys-` and
               must be no longer than 32 characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='add_images')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        if images_file:
            for item in images_file:
                form_data.append(('images_file', (item.filename, item.data,
                                                  item.content_type or
                                                  'application/octet-stream')))
        if image_url:
            for item in image_url:
                form_data.append(
                    ('image_url', (None, item, 'application/json')))
        if training_data:
            training_data = str(training_data)
            form_data.append(
                ('training_data', (None, training_data, 'text/plain')))

        url = '/v4/collections/{0}/images'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def list_images(self, collection_id: str, **kwargs) -> 'DetailedResponse':
        """
        List images.

        Retrieves a list of images in a collection.

        :param str collection_id: The identifier of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='list_images')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/images'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_image_details(self, collection_id: str, image_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Get image details.

        Get the details of an image in a collection.

        :param str collection_id: The identifier of the collection.
        :param str image_id: The identifier of the image.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if image_id is None:
            raise ValueError('image_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_image_details')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/images/{1}'.format(
            *self._encode_path_vars(collection_id, image_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_image(self, collection_id: str, image_id: str,
                     **kwargs) -> 'DetailedResponse':
        """
        Delete an image.

        Delete one image from a collection.

        :param str collection_id: The identifier of the collection.
        :param str image_id: The identifier of the image.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if image_id is None:
            raise ValueError('image_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='delete_image')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/images/{1}'.format(
            *self._encode_path_vars(collection_id, image_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_jpeg_image(self,
                       collection_id: str,
                       image_id: str,
                       *,
                       size: str = None,
                       **kwargs) -> 'DetailedResponse':
        """
        Get a JPEG file of an image.

        Download a JPEG representation of an image.

        :param str collection_id: The identifier of the collection.
        :param str image_id: The identifier of the image.
        :param str size: (optional) The image size. Specify `thumbnail` to return a
               version that maintains the original aspect ratio but is no larger than 200
               pixels in the larger dimension. For example, an original 800 x 1000 image
               is resized to 160 x 200 pixels.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if image_id is None:
            raise ValueError('image_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_jpeg_image')
        headers.update(sdk_headers)

        params = {'version': self.version, 'size': size}

        url = '/v4/collections/{0}/images/{1}/jpeg'.format(
            *self._encode_path_vars(collection_id, image_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Objects
    #########################

    def list_object_metadata(self, collection_id: str,
                             **kwargs) -> 'DetailedResponse':
        """
        List object metadata.

        Retrieves a list of object names in a collection.

        :param str collection_id: The identifier of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='list_object_metadata')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/objects'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_object_metadata(self, collection_id: str, object: str,
                               new_object: str, **kwargs) -> 'DetailedResponse':
        """
        Update an object name.

        Update the name of an object. A successful request updates the training data for
        all images that use the object.

        :param str collection_id: The identifier of the collection.
        :param str object: The name of the object.
        :param str new_object: The updated name of the object. The name can contain
               alphanumeric, underscore, hyphen, space, and dot characters. It cannot
               begin with the reserved prefix `sys-`.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if object is None:
            raise ValueError('object must be provided')
        if new_object is None:
            raise ValueError('new_object must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='update_object_metadata')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'object': new_object}

        url = '/v4/collections/{0}/objects/{1}'.format(
            *self._encode_path_vars(collection_id, object))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def get_object_metadata(self, collection_id: str, object: str,
                            **kwargs) -> 'DetailedResponse':
        """
        Get object metadata.

        Get the number of bounding boxes for a single object in a collection.

        :param str collection_id: The identifier of the collection.
        :param str object: The name of the object.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if object is None:
            raise ValueError('object must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_object_metadata')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/objects/{1}'.format(
            *self._encode_path_vars(collection_id, object))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def delete_object(self, collection_id: str, object: str,
                      **kwargs) -> 'DetailedResponse':
        """
        Delete an object.

        Delete one object from a collection. A successful request deletes the training
        data from all images that use the object.

        :param str collection_id: The identifier of the collection.
        :param str object: The name of the object.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if object is None:
            raise ValueError('object must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='delete_object')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/objects/{1}'.format(
            *self._encode_path_vars(collection_id, object))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Training
    #########################

    def train(self, collection_id: str, **kwargs) -> 'DetailedResponse':
        """
        Train a collection.

        Start training on images in a collection. The collection must have enough training
        data and untrained data (the **training_status.objects.data_changed** is `true`).
        If training is in progress, the request queues the next training job.

        :param str collection_id: The identifier of the collection.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='train')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v4/collections/{0}/train'.format(
            *self._encode_path_vars(collection_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def add_image_training_data(self,
                                collection_id: str,
                                image_id: str,
                                *,
                                objects: List['TrainingDataObject'] = None,
                                **kwargs) -> 'DetailedResponse':
        """
        Add training data to an image.

        Add, update, or delete training data for an image. Encode the object name in UTF-8
        if it contains non-ASCII characters. The service assumes UTF-8 encoding if it
        encounters non-ASCII characters.
        Elements in the request replace the existing elements.
        - To update the training data, provide both the unchanged and the new or changed
        values.
        - To delete the training data, provide an empty value for the training data.

        :param str collection_id: The identifier of the collection.
        :param str image_id: The identifier of the image.
        :param List[TrainingDataObject] objects: (optional) Training data for
               specific objects.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if collection_id is None:
            raise ValueError('collection_id must be provided')
        if image_id is None:
            raise ValueError('image_id must be provided')
        if objects is not None:
            objects = [self._convert_model(x) for x in objects]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='add_image_training_data')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'objects': objects}

        url = '/v4/collections/{0}/images/{1}/training_data'.format(
            *self._encode_path_vars(collection_id, image_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request)
        return response

    def get_training_usage(self,
                           *,
                           start_time: str = None,
                           end_time: str = None,
                           **kwargs) -> 'DetailedResponse':
        """
        Get training usage.

        Information about the completed training events. You can use this information to
        determine how close you are to the training limits for the month.

        :param str start_time: (optional) The earliest day to include training
               events. Specify dates in YYYY-MM-DD format. If empty or not specified, the
               earliest training event is included.
        :param str end_time: (optional) The most recent day to include training
               events. Specify dates in YYYY-MM-DD format. All events for the day are
               included. If empty or not specified, the current day is used. Specify the
               same value as `start_time` to request events for a single day.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='get_training_usage')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'start_time': start_time,
            'end_time': end_time
        }

        url = '/v4/training_usage'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id: str,
                         **kwargs) -> 'DetailedResponse':
        """
        Delete labeled data.

        Deletes all data associated with a specified customer ID. The method has no effect
        if no data is associated with the customer ID.
        You associate a customer ID with data by passing the `X-Watson-Metadata` header
        with a request that passes data. For more information about personal data and
        customer IDs, see [Information
        security](https://cloud.ibm.com/docs/visual-recognition?topic=visual-recognition-information-security).

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if customer_id is None:
            raise ValueError('customer_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V4',
                                      operation_id='delete_user_data')
        headers.update(sdk_headers)

        params = {'version': self.version, 'customer_id': customer_id}

        url = '/v4/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class AnalyzeEnums(object):

    class Features(Enum):
        """
        The features to analyze.
        """
        OBJECTS = 'objects'


class GetJpegImageEnums(object):

    class Size(Enum):
        """
        The image size. Specify `thumbnail` to return a version that maintains the
        original aspect ratio but is no larger than 200 pixels in the larger dimension.
        For example, an original 800 x 1000 image is resized to 160 x 200 pixels.
        """
        FULL = 'full'
        THUMBNAIL = 'thumbnail'


##############################################################################
# Models
##############################################################################


class AnalyzeResponse():
    """
    Results for all images.

    :attr List[Image] images: Analyzed images.
    :attr List[Warning] warnings: (optional) Information about what might cause less
          than optimal output.
    :attr str trace: (optional) A unique identifier of the request. Included only
          when an error or warning is returned.
    """

    def __init__(self,
                 images: List['Image'],
                 *,
                 warnings: List['Warning'] = None,
                 trace: str = None) -> None:
        """
        Initialize a AnalyzeResponse object.

        :param List[Image] images: Analyzed images.
        :param List[Warning] warnings: (optional) Information about what might
               cause less than optimal output.
        :param str trace: (optional) A unique identifier of the request. Included
               only when an error or warning is returned.
        """
        self.images = images
        self.warnings = warnings
        self.trace = trace

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyzeResponse':
        """Initialize a AnalyzeResponse object from a json dictionary."""
        args = {}
        valid_keys = ['images', 'warnings', 'trace']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class AnalyzeResponse: '
                + ', '.join(bad_keys))
        if 'images' in _dict:
            args['images'] = [
                Image._from_dict(x) for x in (_dict.get('images'))
            ]
        else:
            raise ValueError(
                'Required property \'images\' not present in AnalyzeResponse JSON'
            )
        if 'warnings' in _dict:
            args['warnings'] = [
                Warning._from_dict(x) for x in (_dict.get('warnings'))
            ]
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyzeResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x._to_dict() for x in self.images]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyzeResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'AnalyzeResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyzeResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Collection():
    """
    Details about a collection.

    :attr str collection_id: The identifier of the collection.
    :attr str name: The name of the collection.
    :attr str description: The description of the collection.
    :attr datetime created: Date and time in Coordinated Universal Time (UTC) that
          the collection was created.
    :attr datetime updated: Date and time in Coordinated Universal Time (UTC) that
          the collection was most recently updated.
    :attr int image_count: Number of images in the collection.
    :attr TrainingStatus training_status: Training status information for the
          collection.
    """

    def __init__(self, collection_id: str, name: str, description: str,
                 created: datetime, updated: datetime, image_count: int,
                 training_status: 'TrainingStatus') -> None:
        """
        Initialize a Collection object.

        :param str collection_id: The identifier of the collection.
        :param str name: The name of the collection.
        :param str description: The description of the collection.
        :param datetime created: Date and time in Coordinated Universal Time (UTC)
               that the collection was created.
        :param datetime updated: Date and time in Coordinated Universal Time (UTC)
               that the collection was most recently updated.
        :param int image_count: Number of images in the collection.
        :param TrainingStatus training_status: Training status information for the
               collection.
        """
        self.collection_id = collection_id
        self.name = name
        self.description = description
        self.created = created
        self.updated = updated
        self.image_count = image_count
        self.training_status = training_status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Collection':
        """Initialize a Collection object from a json dictionary."""
        args = {}
        valid_keys = [
            'collection_id', 'name', 'description', 'created', 'updated',
            'image_count', 'training_status'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Collection: '
                + ', '.join(bad_keys))
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in Collection JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Collection JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in Collection JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        else:
            raise ValueError(
                'Required property \'created\' not present in Collection JSON')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        else:
            raise ValueError(
                'Required property \'updated\' not present in Collection JSON')
        if 'image_count' in _dict:
            args['image_count'] = _dict.get('image_count')
        else:
            raise ValueError(
                'Required property \'image_count\' not present in Collection JSON'
            )
        if 'training_status' in _dict:
            args['training_status'] = TrainingStatus._from_dict(
                _dict.get('training_status'))
        else:
            raise ValueError(
                'Required property \'training_status\' not present in Collection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Collection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'image_count') and self.image_count is not None:
            _dict['image_count'] = self.image_count
        if hasattr(self,
                   'training_status') and self.training_status is not None:
            _dict['training_status'] = self.training_status._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Collection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Collection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionObjects():
    """
    The objects in a collection that are detected in an image.

    :attr str collection_id: The identifier of the collection.
    :attr List[ObjectDetail] objects: The identified objects in a collection.
    """

    def __init__(self, collection_id: str,
                 objects: List['ObjectDetail']) -> None:
        """
        Initialize a CollectionObjects object.

        :param str collection_id: The identifier of the collection.
        :param List[ObjectDetail] objects: The identified objects in a collection.
        """
        self.collection_id = collection_id
        self.objects = objects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionObjects':
        """Initialize a CollectionObjects object from a json dictionary."""
        args = {}
        valid_keys = ['collection_id', 'objects']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionObjects: '
                + ', '.join(bad_keys))
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        else:
            raise ValueError(
                'Required property \'collection_id\' not present in CollectionObjects JSON'
            )
        if 'objects' in _dict:
            args['objects'] = [
                ObjectDetail._from_dict(x) for x in (_dict.get('objects'))
            ]
        else:
            raise ValueError(
                'Required property \'objects\' not present in CollectionObjects JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionObjects object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = [x._to_dict() for x in self.objects]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionObjects object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionObjects') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionObjects') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionsList():
    """
    A container for the list of collections.

    :attr List[Collection] collections: The collections in this service instance.
    """

    def __init__(self, collections: List['Collection']) -> None:
        """
        Initialize a CollectionsList object.

        :param List[Collection] collections: The collections in this service
               instance.
        """
        self.collections = collections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionsList':
        """Initialize a CollectionsList object from a json dictionary."""
        args = {}
        valid_keys = ['collections']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionsList: '
                + ', '.join(bad_keys))
        if 'collections' in _dict:
            args['collections'] = [
                Collection._from_dict(x) for x in (_dict.get('collections'))
            ]
        else:
            raise ValueError(
                'Required property \'collections\' not present in CollectionsList JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = [x._to_dict() for x in self.collections]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionsList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DetectedObjects():
    """
    Container for the list of collections that have objects detected in an image.

    :attr List[CollectionObjects] collections: (optional) The collections with
          identified objects.
    """

    def __init__(self,
                 *,
                 collections: List['CollectionObjects'] = None) -> None:
        """
        Initialize a DetectedObjects object.

        :param List[CollectionObjects] collections: (optional) The collections with
               identified objects.
        """
        self.collections = collections

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DetectedObjects':
        """Initialize a DetectedObjects object from a json dictionary."""
        args = {}
        valid_keys = ['collections']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DetectedObjects: '
                + ', '.join(bad_keys))
        if 'collections' in _dict:
            args['collections'] = [
                CollectionObjects._from_dict(x)
                for x in (_dict.get('collections'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DetectedObjects object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'collections') and self.collections is not None:
            _dict['collections'] = [x._to_dict() for x in self.collections]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DetectedObjects object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'DetectedObjects') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DetectedObjects') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Error():
    """
    Details about an error.

    :attr str code: Identifier of the problem.
    :attr str message: An explanation of the problem with possible solutions.
    :attr str more_info: (optional) A URL for more information about the solution.
    :attr ErrorTarget target: (optional) Details about the specific area of the
          problem.
    """

    def __init__(self,
                 code: str,
                 message: str,
                 *,
                 more_info: str = None,
                 target: 'ErrorTarget' = None) -> None:
        """
        Initialize a Error object.

        :param str code: Identifier of the problem.
        :param str message: An explanation of the problem with possible solutions.
        :param str more_info: (optional) A URL for more information about the
               solution.
        :param ErrorTarget target: (optional) Details about the specific area of
               the problem.
        """
        self.code = code
        self.message = message
        self.more_info = more_info
        self.target = target

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Error':
        """Initialize a Error object from a json dictionary."""
        args = {}
        valid_keys = ['code', 'message', 'more_info', 'target']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Error: ' +
                ', '.join(bad_keys))
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError(
                'Required property \'code\' not present in Error JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError(
                'Required property \'message\' not present in Error JSON')
        if 'more_info' in _dict:
            args['more_info'] = _dict.get('more_info')
        if 'target' in _dict:
            args['target'] = ErrorTarget._from_dict(_dict.get('target'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Error object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Error object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Error') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Error') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CodeEnum(Enum):
        """
        Identifier of the problem.
        """
        INVALID_FIELD = "invalid_field"
        INVALID_HEADER = "invalid_header"
        INVALID_METHOD = "invalid_method"
        MISSING_FIELD = "missing_field"
        SERVER_ERROR = "server_error"


class ErrorTarget():
    """
    Details about the specific area of the problem.

    :attr str type: The parameter or property that is the focus of the problem.
    :attr str name: The property that is identified with the problem.
    """

    def __init__(self, type: str, name: str) -> None:
        """
        Initialize a ErrorTarget object.

        :param str type: The parameter or property that is the focus of the
               problem.
        :param str name: The property that is identified with the problem.
        """
        self.type = type
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorTarget':
        """Initialize a ErrorTarget object from a json dictionary."""
        args = {}
        valid_keys = ['type', 'name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ErrorTarget: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in ErrorTarget JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in ErrorTarget JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorTarget object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorTarget object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ErrorTarget') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorTarget') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The parameter or property that is the focus of the problem.
        """
        FIELD = "field"
        PARAMETER = "parameter"
        HEADER = "header"


class Image():
    """
    Details about an image.

    :attr ImageSource source: The source type of the image.
    :attr ImageDimensions dimensions: Height and width of an image.
    :attr DetectedObjects objects: Container for the list of collections that have
          objects detected in an image.
    :attr List[Error] errors: (optional) A container for the problems in the
          request.
    """

    def __init__(self,
                 source: 'ImageSource',
                 dimensions: 'ImageDimensions',
                 objects: 'DetectedObjects',
                 *,
                 errors: List['Error'] = None) -> None:
        """
        Initialize a Image object.

        :param ImageSource source: The source type of the image.
        :param ImageDimensions dimensions: Height and width of an image.
        :param DetectedObjects objects: Container for the list of collections that
               have objects detected in an image.
        :param List[Error] errors: (optional) A container for the problems in the
               request.
        """
        self.source = source
        self.dimensions = dimensions
        self.objects = objects
        self.errors = errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Image':
        """Initialize a Image object from a json dictionary."""
        args = {}
        valid_keys = ['source', 'dimensions', 'objects', 'errors']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Image: ' +
                ', '.join(bad_keys))
        if 'source' in _dict:
            args['source'] = ImageSource._from_dict(_dict.get('source'))
        else:
            raise ValueError(
                'Required property \'source\' not present in Image JSON')
        if 'dimensions' in _dict:
            args['dimensions'] = ImageDimensions._from_dict(
                _dict.get('dimensions'))
        else:
            raise ValueError(
                'Required property \'dimensions\' not present in Image JSON')
        if 'objects' in _dict:
            args['objects'] = DetectedObjects._from_dict(_dict.get('objects'))
        else:
            raise ValueError(
                'Required property \'objects\' not present in Image JSON')
        if 'errors' in _dict:
            args['errors'] = [
                Error._from_dict(x) for x in (_dict.get('errors'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Image object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source._to_dict()
        if hasattr(self, 'dimensions') and self.dimensions is not None:
            _dict['dimensions'] = self.dimensions._to_dict()
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = self.objects._to_dict()
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x._to_dict() for x in self.errors]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Image object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Image') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Image') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageDetails():
    """
    Details about an image.

    :attr str image_id: (optional) The identifier of the image.
    :attr datetime updated: (optional) Date and time in Coordinated Universal Time
          (UTC) that the image was most recently updated.
    :attr datetime created: (optional) Date and time in Coordinated Universal Time
          (UTC) that the image was created.
    :attr ImageSource source: The source type of the image.
    :attr ImageDimensions dimensions: (optional) Height and width of an image.
    :attr List[Error] errors: (optional)
    :attr TrainingDataObjects training_data: (optional) Training data for all
          objects.
    """

    def __init__(self,
                 source: 'ImageSource',
                 *,
                 image_id: str = None,
                 updated: datetime = None,
                 created: datetime = None,
                 dimensions: 'ImageDimensions' = None,
                 errors: List['Error'] = None,
                 training_data: 'TrainingDataObjects' = None) -> None:
        """
        Initialize a ImageDetails object.

        :param ImageSource source: The source type of the image.
        :param str image_id: (optional) The identifier of the image.
        :param datetime updated: (optional) Date and time in Coordinated Universal
               Time (UTC) that the image was most recently updated.
        :param datetime created: (optional) Date and time in Coordinated Universal
               Time (UTC) that the image was created.
        :param ImageDimensions dimensions: (optional) Height and width of an image.
        :param List[Error] errors: (optional)
        :param TrainingDataObjects training_data: (optional) Training data for all
               objects.
        """
        self.image_id = image_id
        self.updated = updated
        self.created = created
        self.source = source
        self.dimensions = dimensions
        self.errors = errors
        self.training_data = training_data

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDetails':
        """Initialize a ImageDetails object from a json dictionary."""
        args = {}
        valid_keys = [
            'image_id', 'updated', 'created', 'source', 'dimensions', 'errors',
            'training_data'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageDetails: '
                + ', '.join(bad_keys))
        if 'image_id' in _dict:
            args['image_id'] = _dict.get('image_id')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'source' in _dict:
            args['source'] = ImageSource._from_dict(_dict.get('source'))
        else:
            raise ValueError(
                'Required property \'source\' not present in ImageDetails JSON')
        if 'dimensions' in _dict:
            args['dimensions'] = ImageDimensions._from_dict(
                _dict.get('dimensions'))
        if 'errors' in _dict:
            args['errors'] = [
                Error._from_dict(x) for x in (_dict.get('errors'))
            ]
        if 'training_data' in _dict:
            args['training_data'] = TrainingDataObjects._from_dict(
                _dict.get('training_data'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'image_id') and self.image_id is not None:
            _dict['image_id'] = self.image_id
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source._to_dict()
        if hasattr(self, 'dimensions') and self.dimensions is not None:
            _dict['dimensions'] = self.dimensions._to_dict()
        if hasattr(self, 'errors') and self.errors is not None:
            _dict['errors'] = [x._to_dict() for x in self.errors]
        if hasattr(self, 'training_data') and self.training_data is not None:
            _dict['training_data'] = self.training_data._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageDetailsList():
    """
    List of information about the images.

    :attr List[ImageDetails] images: (optional) The images in the collection.
    :attr List[Warning] warnings: (optional) Information about what might cause less
          than optimal output.
    :attr str trace: (optional) A unique identifier of the request. Included only
          when an error or warning is returned.
    """

    def __init__(self,
                 *,
                 images: List['ImageDetails'] = None,
                 warnings: List['Warning'] = None,
                 trace: str = None) -> None:
        """
        Initialize a ImageDetailsList object.

        :param List[ImageDetails] images: (optional) The images in the collection.
        :param List[Warning] warnings: (optional) Information about what might
               cause less than optimal output.
        :param str trace: (optional) A unique identifier of the request. Included
               only when an error or warning is returned.
        """
        self.images = images
        self.warnings = warnings
        self.trace = trace

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDetailsList':
        """Initialize a ImageDetailsList object from a json dictionary."""
        args = {}
        valid_keys = ['images', 'warnings', 'trace']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageDetailsList: '
                + ', '.join(bad_keys))
        if 'images' in _dict:
            args['images'] = [
                ImageDetails._from_dict(x) for x in (_dict.get('images'))
            ]
        if 'warnings' in _dict:
            args['warnings'] = [
                Warning._from_dict(x) for x in (_dict.get('warnings'))
            ]
        if 'trace' in _dict:
            args['trace'] = _dict.get('trace')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDetailsList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x._to_dict() for x in self.images]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        if hasattr(self, 'trace') and self.trace is not None:
            _dict['trace'] = self.trace
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDetailsList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageDetailsList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDetailsList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageDimensions():
    """
    Height and width of an image.

    :attr int height: (optional) Height in pixels of the image.
    :attr int width: (optional) Width in pixels of the image.
    """

    def __init__(self, *, height: int = None, width: int = None) -> None:
        """
        Initialize a ImageDimensions object.

        :param int height: (optional) Height in pixels of the image.
        :param int width: (optional) Width in pixels of the image.
        """
        self.height = height
        self.width = width

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageDimensions':
        """Initialize a ImageDimensions object from a json dictionary."""
        args = {}
        valid_keys = ['height', 'width']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageDimensions: '
                + ', '.join(bad_keys))
        if 'height' in _dict:
            args['height'] = _dict.get('height')
        if 'width' in _dict:
            args['width'] = _dict.get('width')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageDimensions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'height') and self.height is not None:
            _dict['height'] = self.height
        if hasattr(self, 'width') and self.width is not None:
            _dict['width'] = self.width
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageDimensions object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageDimensions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageDimensions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageSource():
    """
    The source type of the image.

    :attr str type: The source type of the image.
    :attr str filename: (optional) Name of the image file if uploaded. Not returned
          when the image is passed by URL.
    :attr str archive_filename: (optional) Name of the .zip file of images if
          uploaded. Not returned when the image is passed directly or by URL.
    :attr str source_url: (optional) Source of the image before any redirects. Not
          returned when the image is uploaded.
    :attr str resolved_url: (optional) Fully resolved URL of the image after
          redirects are followed. Not returned when the image is uploaded.
    """

    def __init__(self,
                 type: str,
                 *,
                 filename: str = None,
                 archive_filename: str = None,
                 source_url: str = None,
                 resolved_url: str = None) -> None:
        """
        Initialize a ImageSource object.

        :param str type: The source type of the image.
        :param str filename: (optional) Name of the image file if uploaded. Not
               returned when the image is passed by URL.
        :param str archive_filename: (optional) Name of the .zip file of images if
               uploaded. Not returned when the image is passed directly or by URL.
        :param str source_url: (optional) Source of the image before any redirects.
               Not returned when the image is uploaded.
        :param str resolved_url: (optional) Fully resolved URL of the image after
               redirects are followed. Not returned when the image is uploaded.
        """
        self.type = type
        self.filename = filename
        self.archive_filename = archive_filename
        self.source_url = source_url
        self.resolved_url = resolved_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageSource':
        """Initialize a ImageSource object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'filename', 'archive_filename', 'source_url', 'resolved_url'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageSource: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in ImageSource JSON')
        if 'filename' in _dict:
            args['filename'] = _dict.get('filename')
        if 'archive_filename' in _dict:
            args['archive_filename'] = _dict.get('archive_filename')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'resolved_url' in _dict:
            args['resolved_url'] = _dict.get('resolved_url')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self,
                   'archive_filename') and self.archive_filename is not None:
            _dict['archive_filename'] = self.archive_filename
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'resolved_url') and self.resolved_url is not None:
            _dict['resolved_url'] = self.resolved_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageSource object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The source type of the image.
        """
        FILE = "file"
        URL = "url"


class ImageSummary():
    """
    Basic information about an image.

    :attr str image_id: (optional) The identifier of the image.
    :attr datetime updated: (optional) Date and time in Coordinated Universal Time
          (UTC) that the image was most recently updated.
    """

    def __init__(self,
                 *,
                 image_id: str = None,
                 updated: datetime = None) -> None:
        """
        Initialize a ImageSummary object.

        :param str image_id: (optional) The identifier of the image.
        :param datetime updated: (optional) Date and time in Coordinated Universal
               Time (UTC) that the image was most recently updated.
        """
        self.image_id = image_id
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageSummary':
        """Initialize a ImageSummary object from a json dictionary."""
        args = {}
        valid_keys = ['image_id', 'updated']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageSummary: '
                + ', '.join(bad_keys))
        if 'image_id' in _dict:
            args['image_id'] = _dict.get('image_id')
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageSummary object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'image_id') and self.image_id is not None:
            _dict['image_id'] = self.image_id
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageSummary object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageSummary') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageSummary') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageSummaryList():
    """
    List of images.

    :attr List[ImageSummary] images: The images in the collection.
    """

    def __init__(self, images: List['ImageSummary']) -> None:
        """
        Initialize a ImageSummaryList object.

        :param List[ImageSummary] images: The images in the collection.
        """
        self.images = images

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ImageSummaryList':
        """Initialize a ImageSummaryList object from a json dictionary."""
        args = {}
        valid_keys = ['images']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ImageSummaryList: '
                + ', '.join(bad_keys))
        if 'images' in _dict:
            args['images'] = [
                ImageSummary._from_dict(x) for x in (_dict.get('images'))
            ]
        else:
            raise ValueError(
                'Required property \'images\' not present in ImageSummaryList JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageSummaryList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x._to_dict() for x in self.images]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ImageSummaryList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ImageSummaryList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ImageSummaryList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Location():
    """
    Defines the location of the bounding box around the object.

    :attr int top: Y-position of top-left pixel of the bounding box.
    :attr int left: X-position of top-left pixel of the bounding box.
    :attr int width: Width in pixels of of the bounding box.
    :attr int height: Height in pixels of the bounding box.
    """

    def __init__(self, top: int, left: int, width: int, height: int) -> None:
        """
        Initialize a Location object.

        :param int top: Y-position of top-left pixel of the bounding box.
        :param int left: X-position of top-left pixel of the bounding box.
        :param int width: Width in pixels of of the bounding box.
        :param int height: Height in pixels of the bounding box.
        """
        self.top = top
        self.left = left
        self.width = width
        self.height = height

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Location':
        """Initialize a Location object from a json dictionary."""
        args = {}
        valid_keys = ['top', 'left', 'width', 'height']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Location: '
                + ', '.join(bad_keys))
        if 'top' in _dict:
            args['top'] = _dict.get('top')
        else:
            raise ValueError(
                'Required property \'top\' not present in Location JSON')
        if 'left' in _dict:
            args['left'] = _dict.get('left')
        else:
            raise ValueError(
                'Required property \'left\' not present in Location JSON')
        if 'width' in _dict:
            args['width'] = _dict.get('width')
        else:
            raise ValueError(
                'Required property \'width\' not present in Location JSON')
        if 'height' in _dict:
            args['height'] = _dict.get('height')
        else:
            raise ValueError(
                'Required property \'height\' not present in Location JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Location object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'top') and self.top is not None:
            _dict['top'] = self.top
        if hasattr(self, 'left') and self.left is not None:
            _dict['left'] = self.left
        if hasattr(self, 'width') and self.width is not None:
            _dict['width'] = self.width
        if hasattr(self, 'height') and self.height is not None:
            _dict['height'] = self.height
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Location object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Location') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Location') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectDetail():
    """
    Details about an object in the collection.

    :attr str object: The label for the object.
    :attr Location location: Defines the location of the bounding box around the
          object.
    :attr float score: Confidence score for the object in the range of 0 to 1. A
          higher score indicates greater likelihood that the object is depicted at this
          location in the image.
    """

    def __init__(self, object: str, location: 'Location', score: float) -> None:
        """
        Initialize a ObjectDetail object.

        :param str object: The label for the object.
        :param Location location: Defines the location of the bounding box around
               the object.
        :param float score: Confidence score for the object in the range of 0 to 1.
               A higher score indicates greater likelihood that the object is depicted at
               this location in the image.
        """
        self.object = object
        self.location = location
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectDetail':
        """Initialize a ObjectDetail object from a json dictionary."""
        args = {}
        valid_keys = ['object', 'location', 'score']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ObjectDetail: '
                + ', '.join(bad_keys))
        if 'object' in _dict:
            args['object'] = _dict.get('object')
        else:
            raise ValueError(
                'Required property \'object\' not present in ObjectDetail JSON')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        else:
            raise ValueError(
                'Required property \'location\' not present in ObjectDetail JSON'
            )
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in ObjectDetail JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectDetail object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'object') and self.object is not None:
            _dict['object'] = self.object
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectDetail object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ObjectDetail') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectDetail') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectMetadata():
    """
    Basic information about an object.

    :attr str object: (optional) The name of the object.
    :attr int count: (optional) Number of bounding boxes with this object name in
          the collection.
    """

    def __init__(self, *, object: str = None, count: int = None) -> None:
        """
        Initialize a ObjectMetadata object.

        :param str object: (optional) The name of the object.
        :param int count: (optional) Number of bounding boxes with this object name
               in the collection.
        """
        self.object = object
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectMetadata':
        """Initialize a ObjectMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['object', 'count']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ObjectMetadata: '
                + ', '.join(bad_keys))
        if 'object' in _dict:
            args['object'] = _dict.get('object')
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'object') and self.object is not None:
            _dict['object'] = self.object
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ObjectMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectMetadataList():
    """
    List of objects.

    :attr int object_count: Number of unique named objects in the collection.
    :attr List[ObjectMetadata] objects: (optional) The objects in the collection.
    """

    def __init__(self,
                 object_count: int,
                 *,
                 objects: List['ObjectMetadata'] = None) -> None:
        """
        Initialize a ObjectMetadataList object.

        :param int object_count: Number of unique named objects in the collection.
        :param List[ObjectMetadata] objects: (optional) The objects in the
               collection.
        """
        self.object_count = object_count
        self.objects = objects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectMetadataList':
        """Initialize a ObjectMetadataList object from a json dictionary."""
        args = {}
        valid_keys = ['object_count', 'objects']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ObjectMetadataList: '
                + ', '.join(bad_keys))
        if 'object_count' in _dict:
            args['object_count'] = _dict.get('object_count')
        else:
            raise ValueError(
                'Required property \'object_count\' not present in ObjectMetadataList JSON'
            )
        if 'objects' in _dict:
            args['objects'] = [
                ObjectMetadata._from_dict(x) for x in (_dict.get('objects'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectMetadataList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'object_count') and self.object_count is not None:
            _dict['object_count'] = self.object_count
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = [x._to_dict() for x in self.objects]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectMetadataList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ObjectMetadataList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectMetadataList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ObjectTrainingStatus():
    """
    Training status for the objects in the collection.

    :attr bool ready: Whether you can analyze images in the collection with the
          **objects** feature.
    :attr bool in_progress: Whether training is in progress.
    :attr bool data_changed: Whether there are changes to the training data since
          the most recent training.
    :attr bool latest_failed: Whether the most recent training failed.
    :attr str description: Details about the training. If training is in progress,
          includes information about the status. If training is not in progress, includes
          a success message or information about why training failed.
    """

    def __init__(self, ready: bool, in_progress: bool, data_changed: bool,
                 latest_failed: bool, description: str) -> None:
        """
        Initialize a ObjectTrainingStatus object.

        :param bool ready: Whether you can analyze images in the collection with
               the **objects** feature.
        :param bool in_progress: Whether training is in progress.
        :param bool data_changed: Whether there are changes to the training data
               since the most recent training.
        :param bool latest_failed: Whether the most recent training failed.
        :param str description: Details about the training. If training is in
               progress, includes information about the status. If training is not in
               progress, includes a success message or information about why training
               failed.
        """
        self.ready = ready
        self.in_progress = in_progress
        self.data_changed = data_changed
        self.latest_failed = latest_failed
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ObjectTrainingStatus':
        """Initialize a ObjectTrainingStatus object from a json dictionary."""
        args = {}
        valid_keys = [
            'ready', 'in_progress', 'data_changed', 'latest_failed',
            'description'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ObjectTrainingStatus: '
                + ', '.join(bad_keys))
        if 'ready' in _dict:
            args['ready'] = _dict.get('ready')
        else:
            raise ValueError(
                'Required property \'ready\' not present in ObjectTrainingStatus JSON'
            )
        if 'in_progress' in _dict:
            args['in_progress'] = _dict.get('in_progress')
        else:
            raise ValueError(
                'Required property \'in_progress\' not present in ObjectTrainingStatus JSON'
            )
        if 'data_changed' in _dict:
            args['data_changed'] = _dict.get('data_changed')
        else:
            raise ValueError(
                'Required property \'data_changed\' not present in ObjectTrainingStatus JSON'
            )
        if 'latest_failed' in _dict:
            args['latest_failed'] = _dict.get('latest_failed')
        else:
            raise ValueError(
                'Required property \'latest_failed\' not present in ObjectTrainingStatus JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in ObjectTrainingStatus JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ObjectTrainingStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'ready') and self.ready is not None:
            _dict['ready'] = self.ready
        if hasattr(self, 'in_progress') and self.in_progress is not None:
            _dict['in_progress'] = self.in_progress
        if hasattr(self, 'data_changed') and self.data_changed is not None:
            _dict['data_changed'] = self.data_changed
        if hasattr(self, 'latest_failed') and self.latest_failed is not None:
            _dict['latest_failed'] = self.latest_failed
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ObjectTrainingStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ObjectTrainingStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ObjectTrainingStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingDataObject():
    """
    Details about the training data.

    :attr str object: (optional) The name of the object.
    :attr Location location: (optional) Defines the location of the bounding box
          around the object.
    """

    def __init__(self,
                 *,
                 object: str = None,
                 location: 'Location' = None) -> None:
        """
        Initialize a TrainingDataObject object.

        :param str object: (optional) The name of the object.
        :param Location location: (optional) Defines the location of the bounding
               box around the object.
        """
        self.object = object
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingDataObject':
        """Initialize a TrainingDataObject object from a json dictionary."""
        args = {}
        valid_keys = ['object', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingDataObject: '
                + ', '.join(bad_keys))
        if 'object' in _dict:
            args['object'] = _dict.get('object')
        if 'location' in _dict:
            args['location'] = Location._from_dict(_dict.get('location'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingDataObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'object') and self.object is not None:
            _dict['object'] = self.object
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingDataObject object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingDataObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingDataObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingDataObjects():
    """
    Training data for all objects.

    :attr List[TrainingDataObject] objects: (optional) Training data for specific
          objects.
    """

    def __init__(self, *, objects: List['TrainingDataObject'] = None) -> None:
        """
        Initialize a TrainingDataObjects object.

        :param List[TrainingDataObject] objects: (optional) Training data for
               specific objects.
        """
        self.objects = objects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingDataObjects':
        """Initialize a TrainingDataObjects object from a json dictionary."""
        args = {}
        valid_keys = ['objects']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingDataObjects: '
                + ', '.join(bad_keys))
        if 'objects' in _dict:
            args['objects'] = [
                TrainingDataObject._from_dict(x) for x in (_dict.get('objects'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingDataObjects object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = [x._to_dict() for x in self.objects]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingDataObjects object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingDataObjects') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingDataObjects') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingEvent():
    """
    Details about the training event.

    :attr str type: (optional) Trained object type. Only `objects` is currently
          supported.
    :attr str collection_id: (optional) Identifier of the trained collection.
    :attr datetime completion_time: (optional) Date and time in Coordinated
          Universal Time (UTC) that training on the collection finished.
    :attr str status: (optional) Training status of the training event.
    :attr int image_count: (optional) The total number of images that were used in
          training for this training event.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 collection_id: str = None,
                 completion_time: datetime = None,
                 status: str = None,
                 image_count: int = None) -> None:
        """
        Initialize a TrainingEvent object.

        :param str type: (optional) Trained object type. Only `objects` is
               currently supported.
        :param str collection_id: (optional) Identifier of the trained collection.
        :param datetime completion_time: (optional) Date and time in Coordinated
               Universal Time (UTC) that training on the collection finished.
        :param str status: (optional) Training status of the training event.
        :param int image_count: (optional) The total number of images that were
               used in training for this training event.
        """
        self.type = type
        self.collection_id = collection_id
        self.completion_time = completion_time
        self.status = status
        self.image_count = image_count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingEvent':
        """Initialize a TrainingEvent object from a json dictionary."""
        args = {}
        valid_keys = [
            'type', 'collection_id', 'completion_time', 'status', 'image_count'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingEvent: '
                + ', '.join(bad_keys))
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'collection_id' in _dict:
            args['collection_id'] = _dict.get('collection_id')
        if 'completion_time' in _dict:
            args['completion_time'] = string_to_datetime(
                _dict.get('completion_time'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'image_count' in _dict:
            args['image_count'] = _dict.get('image_count')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'collection_id') and self.collection_id is not None:
            _dict['collection_id'] = self.collection_id
        if hasattr(self,
                   'completion_time') and self.completion_time is not None:
            _dict['completion_time'] = datetime_to_string(self.completion_time)
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'image_count') and self.image_count is not None:
            _dict['image_count'] = self.image_count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingEvent object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingEvent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingEvent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        Trained object type. Only `objects` is currently supported.
        """
        OBJECTS = "objects"

    class StatusEnum(Enum):
        """
        Training status of the training event.
        """
        FAILED = "failed"
        SUCCEEDED = "succeeded"


class TrainingEvents():
    """
    Details about the training events.

    :attr datetime start_time: (optional) The starting day for the returned training
          events in Coordinated Universal Time (UTC). If not specified in the request, it
          identifies the earliest training event.
    :attr datetime end_time: (optional) The ending day for the returned training
          events in Coordinated Universal Time (UTC). If not specified in the request, it
          lists the current time.
    :attr int completed_events: (optional) The total number of training events in
          the response for the start and end times.
    :attr int trained_images: (optional) The total number of images that were used
          in training for the start and end times.
    :attr List[TrainingEvent] events: (optional) The completed training events for
          the start and end time.
    """

    def __init__(self,
                 *,
                 start_time: datetime = None,
                 end_time: datetime = None,
                 completed_events: int = None,
                 trained_images: int = None,
                 events: List['TrainingEvent'] = None) -> None:
        """
        Initialize a TrainingEvents object.

        :param datetime start_time: (optional) The starting day for the returned
               training events in Coordinated Universal Time (UTC). If not specified in
               the request, it identifies the earliest training event.
        :param datetime end_time: (optional) The ending day for the returned
               training events in Coordinated Universal Time (UTC). If not specified in
               the request, it lists the current time.
        :param int completed_events: (optional) The total number of training events
               in the response for the start and end times.
        :param int trained_images: (optional) The total number of images that were
               used in training for the start and end times.
        :param List[TrainingEvent] events: (optional) The completed training events
               for the start and end time.
        """
        self.start_time = start_time
        self.end_time = end_time
        self.completed_events = completed_events
        self.trained_images = trained_images
        self.events = events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingEvents':
        """Initialize a TrainingEvents object from a json dictionary."""
        args = {}
        valid_keys = [
            'start_time', 'end_time', 'completed_events', 'trained_images',
            'events'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingEvents: '
                + ', '.join(bad_keys))
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'end_time' in _dict:
            args['end_time'] = string_to_datetime(_dict.get('end_time'))
        if 'completed_events' in _dict:
            args['completed_events'] = _dict.get('completed_events')
        if 'trained_images' in _dict:
            args['trained_images'] = _dict.get('trained_images')
        if 'events' in _dict:
            args['events'] = [
                TrainingEvent._from_dict(x) for x in (_dict.get('events'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingEvents object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = datetime_to_string(self.end_time)
        if hasattr(self,
                   'completed_events') and self.completed_events is not None:
            _dict['completed_events'] = self.completed_events
        if hasattr(self, 'trained_images') and self.trained_images is not None:
            _dict['trained_images'] = self.trained_images
        if hasattr(self, 'events') and self.events is not None:
            _dict['events'] = [x._to_dict() for x in self.events]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingEvents object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingEvents') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingEvents') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TrainingStatus():
    """
    Training status information for the collection.

    :attr ObjectTrainingStatus objects: Training status for the objects in the
          collection.
    """

    def __init__(self, objects: 'ObjectTrainingStatus') -> None:
        """
        Initialize a TrainingStatus object.

        :param ObjectTrainingStatus objects: Training status for the objects in the
               collection.
        """
        self.objects = objects

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TrainingStatus':
        """Initialize a TrainingStatus object from a json dictionary."""
        args = {}
        valid_keys = ['objects']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class TrainingStatus: '
                + ', '.join(bad_keys))
        if 'objects' in _dict:
            args['objects'] = ObjectTrainingStatus._from_dict(
                _dict.get('objects'))
        else:
            raise ValueError(
                'Required property \'objects\' not present in TrainingStatus JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TrainingStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'objects') and self.objects is not None:
            _dict['objects'] = self.objects._to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TrainingStatus object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'TrainingStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TrainingStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdateObjectMetadata():
    """
    Basic information about an updated object.

    :attr str object: The updated name of the object. The name can contain
          alphanumeric, underscore, hyphen, space, and dot characters. It cannot begin
          with the reserved prefix `sys-`.
    :attr int count: Number of bounding boxes in the collection with the
          updated object name.
    """

    def __init__(self, object: str, count: int) -> None:
        """
        Initialize a UpdateObjectMetadata object.

        :param str object: The updated name of the object. The name can contain
               alphanumeric, underscore, hyphen, space, and dot characters. It cannot
               begin with the reserved prefix `sys-`.
        :param int count: Number of bounding boxes in the collection
               with the updated object name.
        """
        self.object = object
        self.count = count

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateObjectMetadata':
        """Initialize a UpdateObjectMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['object', 'count']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class UpdateObjectMetadata: '
                + ', '.join(bad_keys))
        if 'object' in _dict:
            args['object'] = _dict.get('object')
        else:
            raise ValueError(
                'Required property \'object\' not present in UpdateObjectMetadata JSON'
            )
        if 'count' in _dict:
            args['count'] = _dict.get('count')
        else:
            raise ValueError(
                'Required property \'count\' not present in UpdateObjectMetadata JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateObjectMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'object') and self.object is not None:
            _dict['object'] = self.object
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateObjectMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'UpdateObjectMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateObjectMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Warning():
    """
    Details about a problem.

    :attr str code: Identifier of the problem.
    :attr str message: An explanation of the problem with possible solutions.
    :attr str more_info: (optional) A URL for more information about the solution.
    """

    def __init__(self,
                 code: str,
                 message: str,
                 *,
                 more_info: str = None) -> None:
        """
        Initialize a Warning object.

        :param str code: Identifier of the problem.
        :param str message: An explanation of the problem with possible solutions.
        :param str more_info: (optional) A URL for more information about the
               solution.
        """
        self.code = code
        self.message = message
        self.more_info = more_info

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Warning':
        """Initialize a Warning object from a json dictionary."""
        args = {}
        valid_keys = ['code', 'message', 'more_info']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Warning: ' +
                ', '.join(bad_keys))
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError(
                'Required property \'code\' not present in Warning JSON')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError(
                'Required property \'message\' not present in Warning JSON')
        if 'more_info' in _dict:
            args['more_info'] = _dict.get('more_info')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Warning object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'more_info') and self.more_info is not None:
            _dict['more_info'] = self.more_info
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Warning object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Warning') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Warning') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class CodeEnum(Enum):
        """
        Identifier of the problem.
        """
        INVALID_FIELD = "invalid_field"
        INVALID_HEADER = "invalid_header"
        INVALID_METHOD = "invalid_method"
        MISSING_FIELD = "missing_field"
        SERVER_ERROR = "server_error"


class FileWithMetadata():
    """
    A file with its associated metadata.

    :attr BinaryIO data: The data / content for the file.
    :attr str filename: (optional) The filename of the file.
    :attr str content_type: (optional) The content type of the file.
    """

    def __init__(self,
                 data: BinaryIO,
                 *,
                 filename: str = None,
                 content_type: str = None) -> None:
        """
        Initialize a FileWithMetadata object.

        :param BinaryIO data: The data / content for the file.
        :param str filename: (optional) The filename of the file.
        :param str content_type: (optional) The content type of the file.
        """
        self.data = data
        self.filename = filename
        self.content_type = content_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FileWithMetadata':
        """Initialize a FileWithMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['data', 'filename', 'content_type']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class FileWithMetadata: '
                + ', '.join(bad_keys))
        if 'data' in _dict:
            args['data'] = _dict.get('data')
        else:
            raise ValueError(
                'Required property \'data\' not present in FileWithMetadata JSON'
            )
        if 'filename' in _dict:
            args['filename'] = _dict.get('filename')
        if 'content_type' in _dict:
            args['content_type'] = _dict.get('content_type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FileWithMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'data') and self.data is not None:
            _dict['data'] = self.data
        if hasattr(self, 'filename') and self.filename is not None:
            _dict['filename'] = self.filename
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FileWithMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'FileWithMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FileWithMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
