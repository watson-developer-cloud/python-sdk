# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
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

from .visual_recognition_v3 import VisualRecognitionV3
from os.path import basename

class VisualRecognitionV3Adapter(VisualRecognitionV3):
    def create_classifier(self,
                          name,
                          **kwargs):
        """
        Create a classifier.
        :param str name: The name of the new classifier. Encode special characters in UTF-8.
        :param file <NAME>_positive_examples: A compressed (.zip) file of images that depict the visual subject for a class within the new classifier. Include at least 10 images in .jpg or .png format. The minimum recommended image resolution is 32X32 pixels. The maximum number of images is 10,000 images or 100 MB per .zip file. Encode special characters in the file name in UTF-8.
        :param file negative_examples: A compressed (.zip) file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images. Encode special characters in the file name in UTF-8.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if name is None:
            raise ValueError('name must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        data = {'name': name}
        url = '/v3/classifiers'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
            files=kwargs,
            accept_json=True)
        return response

    def update_classifier(self,
                          classifier_id,
                          **kwargs):
        """
        Update a classifier.
        :param str classifier_id: The ID of the classifier.
        :param file <NAME>_positive_examples: A .zip file of images that depict the visual subject of a class in the classifier. The positive examples create or update classes in the classifier. You can include more than one positive example file in a call. Include at least 10 images in .jpg or .png format. The minimum recommended image resolution is 32X32 pixels. The maximum number of images is 10,000 images or 100 MB per .zip file. Encode special characters in the file name in UTF-8.
        :param file negative_examples: A .zip file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images. Encode special characters in the file name in UTF-8.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=kwargs,
            accept_json=True)
        return response

    #########################
    # General
    #########################

    def classify(self,
                 images_file=None,
                 accept_language=None,
                 url=None,
                 threshold=None,
                 owners=None,
                 classifier_ids=None,
                 images_file_content_type=None,
                 images_filename=None,
                 **kwargs):
        """
        Classify images.

        Classify images with built-in or custom classifiers.

        :param file images_file: An image file (.jpg, .png) or .zip file with images.
        Maximum image size is 10 MB. Include no more than 20 images and limit the .zip
        file to 100 MB. Encode the image and .zip file names in UTF-8 if they contain
        non-ASCII characters. The service assumes UTF-8 encoding if it encounters
        non-ASCII characters.
        You can also include an image with the **url** parameter.
        :param str accept_language: The language of the output class names. The full set
        of languages is supported for the built-in classifier IDs: `default`, `food`, and
        `explicit`. The class names of custom classifiers are not translated.
        The response might not be in the specified language when the requested language is
        not supported or when there is no translation for the class name.
        :param str url: The URL of an image to analyze. Must be in .jpg, or .png format.
        The minimum recommended pixel density is 32X32 pixels per inch, and the maximum
        image size is 10 MB.
        You can also include images with the **images_file** parameter.
        :param float threshold: The minimum score a class must have to be displayed in the
        response. Set the threshold to `0.0` to ignore the classification score and return
        all values.
        :param list[str] owners: The categories of classifiers to apply. Use `IBM` to
        classify against the `default` general classifier, and use `me` to classify
        against your custom classifiers. To analyze the image against both classifier
        categories, set the value to both `IBM` and `me`.
        The built-in `default` classifier is used if both **classifier_ids** and
        **owners** parameters are empty.
        The **classifier_ids** parameter overrides **owners**, so make sure that
        **classifier_ids** is empty.
        :param list[str] classifier_ids: Which classifiers to apply. Overrides the
        **owners** parameter. You can specify both custom and built-in classifier IDs. The
        built-in `default` classifier is used if both **classifier_ids** and **owners**
        parameters are empty.
        The following built-in classifier IDs require no training:
        - `default`: Returns classes from thousands of general tags.
        - `food`: Enhances specificity and accuracy for images of food items.
        - `explicit`: Evaluates whether the image might be pornographic.
        :param str images_file_content_type: The content type of images_file.
        :param str images_filename: The filename for images_file.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """
        headers = {'Accept-Language': accept_language}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        images_file_tuple = None
        if images_file:
            if not images_filename and hasattr(images_file, 'name'):
                images_filename = images_file.name
                images_filename = basename(images_filename)
            mime_type = images_file_content_type or 'application/octet-stream'
            images_file_tuple = (images_filename, images_file, mime_type)
        url_tuple = None
        if url:
            url_tuple = (None, url, 'text/plain')
        threshold_tuple = None
        if threshold:
            threshold_tuple = (None, threshold, 'application/json')
        owners_tuple = None
        if owners:
            owners = self._convert_list(owners)
            owners_tuple = (None, owners, 'application/json')
        classifier_ids_tuple = None
        if classifier_ids:
            classifier_ids = self._convert_list(classifier_ids)
            classifier_ids_tuple = (None, classifier_ids, 'application/json')
        url = '/v3/classify'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={
                'images_file': images_file_tuple,
                'url': url_tuple,
                'threshold': threshold_tuple,
                'owners': owners_tuple,
                'classifier_ids': classifier_ids_tuple
            },
            accept_json=True)
        return response
