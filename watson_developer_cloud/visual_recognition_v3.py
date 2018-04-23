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
"""
The IBM Watson Visual Recognition service uses deep learning algorithms to identify
scenes, objects, and faces  in images you upload to the service. You can create and train
a custom classifier to identify subjects that suit your needs.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class VisualRecognitionV3(WatsonService):
    """The Visual Recognition V3 service."""

    default_url = 'https://gateway-a.watsonplatform.net/visual-recognition/api'

    def __init__(self,
                 version,
                 url=default_url,
                 api_key=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
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

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway-a.watsonplatform.net/visual-recognition/api").
               The base url may differ between Bluemix regions.

        :param str api_key: The API Key used to authenticate.

        :param str iam_api_key: An API key that can be used to request IAM tokens. If
               this API key is provided, the SDK will manage the token and handle the
               refreshing.

        :param str iam_access_token:  An IAM access token is fully managed by the application.
               Responsibility falls on the application to refresh the token, either before
               it expires or reactively upon receiving a 401 from the service as any requests
               made with an expired token will fail.

        :param str iam_url: An optional URL for the IAM service API. Defaults to
               'https://iam.ng.bluemix.net/identity/token'.
        """

        WatsonService.__init__(
            self,
            vcap_services_name='watson_vision_combined',
            url=url,
            api_key=api_key,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)
        self.version = version

    #########################
    # General
    #########################

    def classify(self,
                 images_file=None,
                 parameters=None,
                 accept_language=None,
                 images_file_content_type=None,
                 images_filename=None,
                 url=None,
                 threshold=None,
                 owners=None,
                 classifier_ids=None,
                 **kwargs):
        """
        Classify images.

        Classify images with built-in or custom classifiers.

        :param file images_file: An image file (.jpg, .png) or .zip file with images. Maximum image size is 10 MB. Include no more than 20 images and limit the .zip file to 100 MB. Encode the image and .zip file names in UTF-8 if they contain non-ASCII characters. The service assumes UTF-8 encoding if it encounters non-ASCII characters. You can also include images with the `url` property in the **parameters** object.
        :param str parameters: (Deprecated) A JSON object that specifies additional request options. The parameter can be sent as a string or a file, and can include these inputs:  - **url**: A string with the image URL to analyze. Must be in .jpg, or .png format. The minimum recommended pixel density is 32X32 pixels per inch, and the maximum image size is 10 MB. You can also include images in the **images_file** parameter. - **threshold**: A floating point value that specifies the minimum score a class must have to be displayed in the response. The default threshold for returning scores from a classifier is `0.5`. Set the threshold to `0.0` to ignore the classification score and return all values. - **owners**: An array of the categories of classifiers to apply. Use `IBM` to classify against the `default` general classifier, and use `me` to classify against your custom classifiers. To analyze the image against both classifier categories, set the value to both `IBM` and `me`. The built-in `default` classifier is used if both **classifier_ids** and **owners** parameters are empty.      The **classifier_ids** parameter overrides **owners**, so make sure that **classifier_ids** is empty. - **classifier_ids**: Specifies which classifiers to apply and overrides the **owners** parameter. You can specify both custom and built-in classifiers. The built-in `default` classifier is used if both **classifier_ids** and **owners** parameters are empty.  The following built-in classifier IDs require no training: - `default`: Returns classes from thousands of general tags. - `food`: (Beta) Enhances specificity and accuracy for images of food items. - `explicit`: (Beta) Evaluates whether the image might be pornographic.  Example: `{\"classifier_ids\":[\"CarsvsTrucks_1479118188\",\"explicit\"],\"threshold\":0.6}`.
        :param str accept_language: Specifies the language of the output class names.  Can be `en` (English), `ar` (Arabic), `de` (German), `es` (Spanish), `it` (Italian), `ja` (Japanese), or `ko` (Korean).  Classes for which no translation is available are omitted.  The response might not be in the specified language under these conditions: - English is returned when the requested language is not supported. - Classes are not returned when there is no translation for them. - Custom classifiers returned with this method return tags in the language of the custom classifier.
        :param str images_file_content_type: The content type of images_file.
        :param str images_filename: The filename for images_file.
        :param str url: A string with the image URL to analyze. Must be in .jpg, or .png format. The minimum recommended pixel density is 32X32 pixels per inch, and the maximum image size is 10 MB. You can also include images in the **images_file** parameter.
        :param float threshold: A floating point value that specifies the minimum score a class must have to be displayed in the response. The default threshold for returning scores from a classifier is `0.5`. Set the threshold to `0.0` to ignore the classification score and return all values.
        :param list[str] owners: An array of the categories of classifiers to apply. Use `IBM` to classify against the `default` general classifier, and use `me` to classify against your custom classifiers. To analyze the image against both classifier categories, set the value to both `IBM` and `me`.   The built-in `default` classifier is used if both **classifier_ids** and **owners** parameters are empty.  The **classifier_ids** parameter overrides **owners**, so make sure that **classifier_ids** is empty.
        :param list[str] classifier_ids: The **classifier_ids** parameter overrides **owners**, so make sure that **classifier_ids** is empty. - **classifier_ids**: Specifies which classifiers to apply and overrides the **owners** parameter. You can specify both custom and built-in classifiers. The built-in `default` classifier is used if both **classifier_ids** and **owners** parameters are empty.  The following built-in classifier IDs require no training: - `default`: Returns classes from thousands of general tags. - `food`: (Beta) Enhances specificity and accuracy for images of food items. - `explicit`: (Beta) Evaluates whether the image might be pornographic.  Example: `\"classifier_ids=\"CarsvsTrucks_1479118188\",\"explicit\"`.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ClassifiedImages` response.
        :rtype: dict
        """
        headers = {'Accept-Language': accept_language}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        images_file_tuple = None
        if images_file:
            if not images_filename and hasattr(images_file, 'name'):
                images_filename = images_file.name
            mime_type = images_file_content_type or 'application/octet-stream'
            images_file_tuple = (images_filename, images_file, mime_type)

        parameters_tuple = None
        if parameters is not None:
            parameters_tuple = (None, parameters, 'text/plain')

        url_tuple = None
        if url:
            url_tuple = (None, url, 'text/plain')
        threshold_tuple = None
        if threshold:
            threshold_tuple = (None, threshold, 'application/json')
        owners_tuple = None
        if owners:
            if isinstance(owners, (list,)):
                owners = ','.join(owners)
            owners_tuple = (None, owners, 'application/json')
        classifier_ids_tuple = None
        if classifier_ids:
            if isinstance(classifier_ids, (list,)):
                classifier_ids = ','.join(classifier_ids)
            classifier_ids_tuple = (None, classifier_ids, 'application/json')
        url = '/v3/classify'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={
                'parameters': parameters_tuple,
                'images_file': images_file_tuple,
                'url': url_tuple,
                'threshold': threshold_tuple,
                'owners': owners_tuple,
                'classifier_ids': classifier_ids_tuple
            },
            accept_json=True)
        return response

    #########################
    # Face
    #########################

    def detect_faces(self,
                     images_file=None,
                     parameters=None,
                     images_file_content_type=None,
                     images_filename=None,
                     url=None,
                     **kwargs):
        """
        Detect faces in images.

        Analyze and get data about faces in images. Responses can include estimated age
        and gender, and the service can identify celebrities. This feature uses a built-in
        classifier, so you do not train it on custom classifiers. The Detect faces method
        does not support general biometric facial recognition.

        :param file images_file: An image file (.jpg, .png) or .zip file with images. Include no more than 15 images. You can also include images with the `url` property in the **parameters** object.  All faces are detected, but if there are more than 10 faces in an image, age and gender confidence scores might return scores of 0.
        :param str parameters: (Deprecated) A JSON object that specifies a single image (.jpg, .png) to analyze by URL. The parameter can be sent as a string or a file.  Example: `{\"url\":\"http://www.example.com/images/myimage.jpg\"}`.
        :param str images_file_content_type: The content type of images_file.
        :param str images_filename: The filename for images_file.
        :param str url: The URL of an image to analyze. Must be in .gif, .jpg, .png, or .tif format. The minimum recommended pixel density is 32X32 pixels per inch, and the maximum image size is 10 MB. Redirects are followed, so you can use a shortened URL.  You can also include images with the **images_file** parameter.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DetectedFaces` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        images_file_tuple = None
        if images_file:
            if not images_filename and hasattr(images_file, 'name'):
                images_filename = images_file.name
            mime_type = images_file_content_type or 'application/octet-stream'
            images_file_tuple = (images_filename, images_file, mime_type)
        parameters_tuple = None
        if parameters is not None:
            parameters_tuple = (None, parameters, 'text/plain')
        url_tuple = None
        if url:
            url_tuple = (None, url, 'text/plain')
        url = '/v3/detect_faces'
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files={'images_file': images_file_tuple,
                   'parameters': parameters_tuple,
                   'url': url_tuple},
            accept_json=True)
        return response

    #########################
    # Custom
    #########################

    def create_classifier(self,
                          name,
                          **kwargs):
        """
        Create a classifier.
        :param str name: The name of the new classifier. Encode special characters in UTF-8.
        :param file <NAME>_positive_examples: A compressed (.zip) file of images that depict the visual subject for a class within the new classifier. Must contain a minimum of 10 images. The swagger limits you to training only one class. To train more classes, use the API functionality.
        :param file negative_examples: A compressed (.zip) file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images.
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

    def delete_classifier(self, classifier_id, **kwargs):
        """
        Delete a classifier.

        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        self.request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return None

    def get_classifier(self, classifier_id, **kwargs):
        """
        Retrieve information about a custom classifier.

        :param str classifier_id: The ID of the classifier.
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
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def list_classifiers(self, verbose=None, **kwargs):
        """
        Retrieve a list of classifiers.

        :param bool verbose: Specify `true` to return details about the classifiers. Omit this parameter to return a brief list of classifiers.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifiers` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version, 'verbose': verbose}
        url = '/v3/classifiers'
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=True)
        return response

    def update_classifier(self,
                          classifier_id,
                          **kwargs):
        """
        Update a classifier.
        :param str classifier_id: The ID of the classifier.
        :param file <NAME>_positive_examples: A compressed (.zip) file of images that depict the visual subject for a class within the classifier. Must contain a minimum of 10 images.
        :param file negative_examples: A compressed (.zip) file of images that do not depict the visual subject of any of the classes of the new classifier. Must contain a minimum of 10 images.
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
    # Core ML
    #########################

    def get_core_ml_model(self, classifier_id, **kwargs):
        """
        Retrieve a Core ML model of a classifier.

        Download a Core ML model file (.mlmodel) of a custom classifier that returns
        core_ml_enabled: true in the classifier details.

        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `Response <Response>` object representing the response.
        :rtype: requests.models.Response
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        params = {'version': self.version}
        url = '/v3/classifiers/{0}/core_ml_model'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
            accept_json=False)
        return response

##############################################################################
# Models
##############################################################################


class Class(object):
    """
    A category within a classifier.

    :attr str class_name: The name of the class.
    """

    def __init__(self, class_name):
        """
        Initialize a Class object.

        :param str class_name: The name of the class.
        """
        self.class_name = class_name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Class object from a json dictionary."""
        args = {}
        if 'class' in _dict or 'class_name' in _dict:
            args['class_name'] = _dict.get('class') or _dict.get('class_name')
        else:
            raise ValueError(
                'Required property \'class\' not present in Class JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'class_name') and self.class_name is not None:
            _dict['class'] = self.class_name
        return _dict

    def __str__(self):
        """Return a `str` version of this Class object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassResult(object):
    """
    Result of a class within a classifier.

    :attr str class_name: The name of the class.
    :attr float score: (optional) Confidence score for the property in the range of 0 to 1. A higher score indicates greater likelihood that the class is depicted in the image. The default threshold for returning scores from a classifier is 0.5.
    :attr str type_hierarchy: (optional) Knowledge graph of the property. For example, `/fruit/pome/apple/eating apple/Granny Smith`. Included only if identified.
    """

    def __init__(self, class_name, score=None, type_hierarchy=None):
        """
        Initialize a ClassResult object.

        :param str class_name: The name of the class.
        :param float score: (optional) Confidence score for the property in the range of 0 to 1. A higher score indicates greater likelihood that the class is depicted in the image. The default threshold for returning scores from a classifier is 0.5.
        :param str type_hierarchy: (optional) Knowledge graph of the property. For example, `/fruit/pome/apple/eating apple/Granny Smith`. Included only if identified.
        """
        self.class_name = class_name
        self.score = score
        self.type_hierarchy = type_hierarchy

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassResult object from a json dictionary."""
        args = {}
        if 'class' in _dict or 'class_name' in _dict:
            args['class_name'] = _dict.get('class') or _dict.get('class_name')
        else:
            raise ValueError(
                'Required property \'class\' not present in ClassResult JSON')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        if 'type_hierarchy' in _dict:
            args['type_hierarchy'] = _dict.get('type_hierarchy')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'class_name') and self.class_name is not None:
            _dict['class'] = self.class_name
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'type_hierarchy') and self.type_hierarchy is not None:
            _dict['type_hierarchy'] = self.type_hierarchy
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedImage(object):
    """
    Classifier results for one image.

    :attr str source_url: (optional) Source of the image before any redirects. Not returned when the image is uploaded.
    :attr str resolved_url: (optional) Fully resolved URL of the image after redirects are followed. Not returned when the image is uploaded.
    :attr str image: (optional) Relative path of the image file if uploaded directly. Not returned when the image is passed by URL.
    :attr ErrorInfo error: (optional)
    :attr list[ClassifierResult] classifiers:
    """

    def __init__(self,
                 classifiers,
                 source_url=None,
                 resolved_url=None,
                 image=None,
                 error=None):
        """
        Initialize a ClassifiedImage object.

        :param list[ClassifierResult] classifiers:
        :param str source_url: (optional) Source of the image before any redirects. Not returned when the image is uploaded.
        :param str resolved_url: (optional) Fully resolved URL of the image after redirects are followed. Not returned when the image is uploaded.
        :param str image: (optional) Relative path of the image file if uploaded directly. Not returned when the image is passed by URL.
        :param ErrorInfo error: (optional)
        """
        self.source_url = source_url
        self.resolved_url = resolved_url
        self.image = image
        self.error = error
        self.classifiers = classifiers

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedImage object from a json dictionary."""
        args = {}
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'resolved_url' in _dict:
            args['resolved_url'] = _dict.get('resolved_url')
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        if 'error' in _dict:
            args['error'] = ErrorInfo._from_dict(_dict.get('error'))
        if 'classifiers' in _dict:
            args['classifiers'] = [
                ClassifierResult._from_dict(x)
                for x in (_dict.get('classifiers'))
            ]
        else:
            raise ValueError(
                'Required property \'classifiers\' not present in ClassifiedImage JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'resolved_url') and self.resolved_url is not None:
            _dict['resolved_url'] = self.resolved_url
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error._to_dict()
        if hasattr(self, 'classifiers') and self.classifiers is not None:
            _dict['classifiers'] = [x._to_dict() for x in self.classifiers]
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifiedImage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedImages(object):
    """
    Classify results for multiple images.

    :attr int custom_classes: (optional) The number of custom classes identified in the images.
    :attr int images_processed: (optional) Number of images processed for the API call.
    :attr list[ClassifiedImage] images: The array of classified images.
    :attr list[WarningInfo] warnings: (optional) Information about what might cause less than optimal output. For example, a request sent with a corrupt .zip file and a list of image URLs will still complete, but does not return the expected output. Not returned when there is no warning.
    """

    def __init__(self,
                 images,
                 custom_classes=None,
                 images_processed=None,
                 warnings=None):
        """
        Initialize a ClassifiedImages object.

        :param list[ClassifiedImage] images: The array of classified images.
        :param int custom_classes: (optional) The number of custom classes identified in the images.
        :param int images_processed: (optional) Number of images processed for the API call.
        :param list[WarningInfo] warnings: (optional) Information about what might cause less than optimal output. For example, a request sent with a corrupt .zip file and a list of image URLs will still complete, but does not return the expected output. Not returned when there is no warning.
        """
        self.custom_classes = custom_classes
        self.images_processed = images_processed
        self.images = images
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedImages object from a json dictionary."""
        args = {}
        if 'custom_classes' in _dict:
            args['custom_classes'] = _dict.get('custom_classes')
        if 'images_processed' in _dict:
            args['images_processed'] = _dict.get('images_processed')
        if 'images' in _dict:
            args['images'] = [
                ClassifiedImage._from_dict(x) for x in (_dict.get('images'))
            ]
        else:
            raise ValueError(
                'Required property \'images\' not present in ClassifiedImages JSON'
            )
        if 'warnings' in _dict:
            args['warnings'] = [
                WarningInfo._from_dict(x) for x in (_dict.get('warnings'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'custom_classes') and self.custom_classes is not None:
            _dict['custom_classes'] = self.custom_classes
        if hasattr(self,
                   'images_processed') and self.images_processed is not None:
            _dict['images_processed'] = self.images_processed
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x._to_dict() for x in self.images]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifiedImages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Classifier(object):
    """
    Information about a classifier.

    :attr str classifier_id: ID of a classifier identified in the image.
    :attr str name: Name of the classifier.
    :attr str owner: (optional) Unique ID of the account who owns the classifier. Returned when verbose=`true`. Might not be returned by some requests.
    :attr str status: (optional) The training status of classifier.
    :attr bool core_ml_enabled: Whether the classifier can be downloaded as a Core ML model after the training status is `ready`.
    :attr str explanation: (optional) If classifier training has failed, this field may explain why.
    :attr datetime created: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was created.
    :attr list[Class] classes: (optional) Array of classes that define a classifier.
    :attr datetime retrained: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was updated. Returned when verbose=`true`. Might not be returned by some requests. Identical to `updated` and retained for backward compatibility.
    :attr datetime updated: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was most recently updated. The field matches either `retrained` or `created`.  Returned when verbose=`true`. Might not be returned by some requests.
    """

    def __init__(self,
                 classifier_id,
                 name,
                 core_ml_enabled,
                 owner=None,
                 status=None,
                 explanation=None,
                 created=None,
                 classes=None,
                 retrained=None,
                 updated=None):
        """
        Initialize a Classifier object.

        :param str classifier_id: ID of a classifier identified in the image.
        :param str name: Name of the classifier.
        :param bool core_ml_enabled: Whether the classifier can be downloaded as a Core ML model after the training status is `ready`.
        :param str owner: (optional) Unique ID of the account who owns the classifier. Returned when verbose=`true`. Might not be returned by some requests.
        :param str status: (optional) The training status of classifier.
        :param str explanation: (optional) If classifier training has failed, this field may explain why.
        :param datetime created: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was created.
        :param list[Class] classes: (optional) Array of classes that define a classifier.
        :param datetime retrained: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was updated. Returned when verbose=`true`. Might not be returned by some requests. Identical to `updated` and retained for backward compatibility.
        :param datetime updated: (optional) Date and time in Coordinated Universal Time (UTC) that the classifier was most recently updated. The field matches either `retrained` or `created`.  Returned when verbose=`true`. Might not be returned by some requests.
        """
        self.classifier_id = classifier_id
        self.name = name
        self.owner = owner
        self.status = status
        self.core_ml_enabled = core_ml_enabled
        self.explanation = explanation
        self.created = created
        self.classes = classes
        self.retrained = retrained
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classifier object from a json dictionary."""
        args = {}
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        else:
            raise ValueError(
                'Required property \'classifier_id\' not present in Classifier JSON'
            )
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Classifier JSON')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'core_ml_enabled' in _dict:
            args['core_ml_enabled'] = _dict.get('core_ml_enabled')
        else:
            raise ValueError(
                'Required property \'core_ml_enabled\' not present in Classifier JSON'
            )
        if 'explanation' in _dict:
            args['explanation'] = _dict.get('explanation')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'classes' in _dict:
            args['classes'] = [
                Class._from_dict(x) for x in (_dict.get('classes'))
            ]
        if 'retrained' in _dict:
            args['retrained'] = string_to_datetime(_dict.get('retrained'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self,
                   'core_ml_enabled') and self.core_ml_enabled is not None:
            _dict['core_ml_enabled'] = self.core_ml_enabled
        if hasattr(self, 'explanation') and self.explanation is not None:
            _dict['explanation'] = self.explanation
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        if hasattr(self, 'retrained') and self.retrained is not None:
            _dict['retrained'] = datetime_to_string(self.retrained)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this Classifier object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifierResult(object):
    """
    Classifier and score combination.

    :attr str name: Name of the classifier.
    :attr str classifier_id: The ID of a classifier identified in the image.
    :attr list[ClassResult] classes: An array of classes within the classifier.
    """

    def __init__(self, name, classifier_id, classes):
        """
        Initialize a ClassifierResult object.

        :param str name: Name of the classifier.
        :param str classifier_id: The ID of a classifier identified in the image.
        :param list[ClassResult] classes: An array of classes within the classifier.
        """
        self.name = name
        self.classifier_id = classifier_id
        self.classes = classes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierResult object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in ClassifierResult JSON'
            )
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        else:
            raise ValueError(
                'Required property \'classifier_id\' not present in ClassifierResult JSON'
            )
        if 'classes' in _dict:
            args['classes'] = [
                ClassResult._from_dict(x) for x in (_dict.get('classes'))
            ]
        else:
            raise ValueError(
                'Required property \'classes\' not present in ClassifierResult JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifierResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Classifiers(object):
    """
    List of classifiers.

    :attr list[Classifier] classifiers:
    """

    def __init__(self, classifiers):
        """
        Initialize a Classifiers object.

        :param list[Classifier] classifiers:
        """
        self.classifiers = classifiers

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classifiers object from a json dictionary."""
        args = {}
        if 'classifiers' in _dict:
            args['classifiers'] = [
                Classifier._from_dict(x) for x in (_dict.get('classifiers'))
            ]
        else:
            raise ValueError(
                'Required property \'classifiers\' not present in Classifiers JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifiers') and self.classifiers is not None:
            _dict['classifiers'] = [x._to_dict() for x in self.classifiers]
        return _dict

    def __str__(self):
        """Return a `str` version of this Classifiers object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DetectedFaces(object):
    """
    DetectedFaces.

    :attr int images_processed: (optional) Number of images processed for the API call.
    :attr list[ImageWithFaces] images: The array of images.
    :attr list[WarningInfo] warnings: (optional) Information about what might cause less than optimal output. For example, a request sent with a corrupt .zip file and a list of image URLs will still complete, but does not return the expected output. Not returned when there is no warning.
    """

    def __init__(self, images, images_processed=None, warnings=None):
        """
        Initialize a DetectedFaces object.

        :param list[ImageWithFaces] images: The array of images.
        :param int images_processed: (optional) Number of images processed for the API call.
        :param list[WarningInfo] warnings: (optional) Information about what might cause less than optimal output. For example, a request sent with a corrupt .zip file and a list of image URLs will still complete, but does not return the expected output. Not returned when there is no warning.
        """
        self.images_processed = images_processed
        self.images = images
        self.warnings = warnings

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DetectedFaces object from a json dictionary."""
        args = {}
        if 'images_processed' in _dict:
            args['images_processed'] = _dict.get('images_processed')
        if 'images' in _dict:
            args['images'] = [
                ImageWithFaces._from_dict(x) for x in (_dict.get('images'))
            ]
        else:
            raise ValueError(
                'Required property \'images\' not present in DetectedFaces JSON'
            )
        if 'warnings' in _dict:
            args['warnings'] = [
                WarningInfo._from_dict(x) for x in (_dict.get('warnings'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'images_processed') and self.images_processed is not None:
            _dict['images_processed'] = self.images_processed
        if hasattr(self, 'images') and self.images is not None:
            _dict['images'] = [x._to_dict() for x in self.images]
        if hasattr(self, 'warnings') and self.warnings is not None:
            _dict['warnings'] = [x._to_dict() for x in self.warnings]
        return _dict

    def __str__(self):
        """Return a `str` version of this DetectedFaces object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorInfo(object):
    """
    Information about what might have caused a failure, such as an image that is too
    large. Not returned when there is no error.

    :attr int code: HTTP status code.
    :attr str description: Human-readable error description. For example, `File size limit exceeded`.
    :attr str error_id: Codified error string. For example, `limit_exceeded`.
    """

    def __init__(self, code, description, error_id):
        """
        Initialize a ErrorInfo object.

        :param int code: HTTP status code.
        :param str description: Human-readable error description. For example, `File size limit exceeded`.
        :param str error_id: Codified error string. For example, `limit_exceeded`.
        """
        self.code = code
        self.description = description
        self.error_id = error_id

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorInfo object from a json dictionary."""
        args = {}
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError(
                'Required property \'code\' not present in ErrorInfo JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in ErrorInfo JSON'
            )
        if 'error_id' in _dict:
            args['error_id'] = _dict.get('error_id')
        else:
            raise ValueError(
                'Required property \'error_id\' not present in ErrorInfo JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'error_id') and self.error_id is not None:
            _dict['error_id'] = self.error_id
        return _dict

    def __str__(self):
        """Return a `str` version of this ErrorInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Face(object):
    """
    Provides information about the face.

    :attr FaceAge age: (optional)
    :attr FaceGender gender: (optional)
    :attr FaceLocation face_location: (optional)
    """

    def __init__(self, age=None, gender=None, face_location=None):
        """
        Initialize a Face object.

        :param FaceAge age: (optional)
        :param FaceGender gender: (optional)
        :param FaceLocation face_location: (optional)
        """
        self.age = age
        self.gender = gender
        self.face_location = face_location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Face object from a json dictionary."""
        args = {}
        if 'age' in _dict:
            args['age'] = FaceAge._from_dict(_dict.get('age'))
        if 'gender' in _dict:
            args['gender'] = FaceGender._from_dict(_dict.get('gender'))
        if 'face_location' in _dict:
            args['face_location'] = FaceLocation._from_dict(
                _dict.get('face_location'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'age') and self.age is not None:
            _dict['age'] = self.age._to_dict()
        if hasattr(self, 'gender') and self.gender is not None:
            _dict['gender'] = self.gender._to_dict()
        if hasattr(self, 'face_location') and self.face_location is not None:
            _dict['face_location'] = self.face_location._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this Face object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FaceAge(object):
    """
    Provides age information about a face.

    :attr int min: (optional) Estimated minimum age.
    :attr int max: (optional) Estimated maximum age.
    :attr float score: (optional) Confidence score in the range of 0 to 1. A higher score indicates greater confidence in the estimated value for the property.
    """

    def __init__(self, min=None, max=None, score=None):
        """
        Initialize a FaceAge object.

        :param int min: (optional) Estimated minimum age.
        :param int max: (optional) Estimated maximum age.
        :param float score: (optional) Confidence score in the range of 0 to 1. A higher score indicates greater confidence in the estimated value for the property.
        """
        self.min = min
        self.max = max
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FaceAge object from a json dictionary."""
        args = {}
        if 'min' in _dict:
            args['min'] = _dict.get('min')
        if 'max' in _dict:
            args['max'] = _dict.get('max')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'min') and self.min is not None:
            _dict['min'] = self.min
        if hasattr(self, 'max') and self.max is not None:
            _dict['max'] = self.max
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this FaceAge object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FaceGender(object):
    """
    Provides information about the gender of the face.

    :attr str gender: Gender identified by the face. For example, `MALE` or `FEMALE`.
    :attr float score: (optional) Confidence score in the range of 0 to 1. A higher score indicates greater confidence in the estimated value for the property.
    """

    def __init__(self, gender, score=None):
        """
        Initialize a FaceGender object.

        :param str gender: Gender identified by the face. For example, `MALE` or `FEMALE`.
        :param float score: (optional) Confidence score in the range of 0 to 1. A higher score indicates greater confidence in the estimated value for the property.
        """
        self.gender = gender
        self.score = score

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FaceGender object from a json dictionary."""
        args = {}
        if 'gender' in _dict:
            args['gender'] = _dict.get('gender')
        else:
            raise ValueError(
                'Required property \'gender\' not present in FaceGender JSON')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'gender') and self.gender is not None:
            _dict['gender'] = self.gender
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def __str__(self):
        """Return a `str` version of this FaceGender object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FaceLocation(object):
    """
    Defines the location of the bounding box around the face.

    :attr float width: Width in pixels of face region.
    :attr float height: Height in pixels of face region.
    :attr float left: X-position of top-left pixel of face region.
    :attr float top: Y-position of top-left pixel of face region.
    """

    def __init__(self, width, height, left, top):
        """
        Initialize a FaceLocation object.

        :param float width: Width in pixels of face region.
        :param float height: Height in pixels of face region.
        :param float left: X-position of top-left pixel of face region.
        :param float top: Y-position of top-left pixel of face region.
        """
        self.width = width
        self.height = height
        self.left = left
        self.top = top

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FaceLocation object from a json dictionary."""
        args = {}
        if 'width' in _dict:
            args['width'] = _dict.get('width')
        else:
            raise ValueError(
                'Required property \'width\' not present in FaceLocation JSON')
        if 'height' in _dict:
            args['height'] = _dict.get('height')
        else:
            raise ValueError(
                'Required property \'height\' not present in FaceLocation JSON'
            )
        if 'left' in _dict:
            args['left'] = _dict.get('left')
        else:
            raise ValueError(
                'Required property \'left\' not present in FaceLocation JSON')
        if 'top' in _dict:
            args['top'] = _dict.get('top')
        else:
            raise ValueError(
                'Required property \'top\' not present in FaceLocation JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'width') and self.width is not None:
            _dict['width'] = self.width
        if hasattr(self, 'height') and self.height is not None:
            _dict['height'] = self.height
        if hasattr(self, 'left') and self.left is not None:
            _dict['left'] = self.left
        if hasattr(self, 'top') and self.top is not None:
            _dict['top'] = self.top
        return _dict

    def __str__(self):
        """Return a `str` version of this FaceLocation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ImageWithFaces(object):
    """
    ImageWithFaces.

    :attr list[Face] faces: An array of the faces detected in the images.
    :attr str image: (optional) Relative path of the image file if uploaded directly. Not returned when the image is passed by URL.
    :attr str source_url: (optional) Source of the image before any redirects. Not returned when the image is uploaded.
    :attr str resolved_url: (optional) Fully resolved URL of the image after redirects are followed. Not returned when the image is uploaded.
    :attr ErrorInfo error: (optional)
    """

    def __init__(self,
                 faces,
                 image=None,
                 source_url=None,
                 resolved_url=None,
                 error=None):
        """
        Initialize a ImageWithFaces object.

        :param list[Face] faces: An array of the faces detected in the images.
        :param str image: (optional) Relative path of the image file if uploaded directly. Not returned when the image is passed by URL.
        :param str source_url: (optional) Source of the image before any redirects. Not returned when the image is uploaded.
        :param str resolved_url: (optional) Fully resolved URL of the image after redirects are followed. Not returned when the image is uploaded.
        :param ErrorInfo error: (optional)
        """
        self.faces = faces
        self.image = image
        self.source_url = source_url
        self.resolved_url = resolved_url
        self.error = error

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ImageWithFaces object from a json dictionary."""
        args = {}
        if 'faces' in _dict:
            args['faces'] = [Face._from_dict(x) for x in (_dict.get('faces'))]
        else:
            raise ValueError(
                'Required property \'faces\' not present in ImageWithFaces JSON'
            )
        if 'image' in _dict:
            args['image'] = _dict.get('image')
        if 'source_url' in _dict:
            args['source_url'] = _dict.get('source_url')
        if 'resolved_url' in _dict:
            args['resolved_url'] = _dict.get('resolved_url')
        if 'error' in _dict:
            args['error'] = ErrorInfo._from_dict(_dict.get('error'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'faces') and self.faces is not None:
            _dict['faces'] = [x._to_dict() for x in self.faces]
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        if hasattr(self, 'source_url') and self.source_url is not None:
            _dict['source_url'] = self.source_url
        if hasattr(self, 'resolved_url') and self.resolved_url is not None:
            _dict['resolved_url'] = self.resolved_url
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ImageWithFaces object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WarningInfo(object):
    """
    Information about something that went wrong.

    :attr str warning_id: Codified warning string, such as `limit_reached`.
    :attr str description: Information about the error.
    """

    def __init__(self, warning_id, description):
        """
        Initialize a WarningInfo object.

        :param str warning_id: Codified warning string, such as `limit_reached`.
        :param str description: Information about the error.
        """
        self.warning_id = warning_id
        self.description = description

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WarningInfo object from a json dictionary."""
        args = {}
        if 'warning_id' in _dict:
            args['warning_id'] = _dict.get('warning_id')
        else:
            raise ValueError(
                'Required property \'warning_id\' not present in WarningInfo JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        else:
            raise ValueError(
                'Required property \'description\' not present in WarningInfo JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'warning_id') and self.warning_id is not None:
            _dict['warning_id'] = self.warning_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def __str__(self):
        """Return a `str` version of this WarningInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
