# coding: utf-8

# (C) Copyright IBM Corp. 2016, 2020.
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
The IBM Watson&trade; Visual Recognition service uses deep learning algorithms to identify
scenes and objects in images that you upload to the service. You can create and train a
custom classifier to identify subjects that suit your needs.
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
from os.path import basename
from typing import BinaryIO
from typing import Dict
from typing import List

##############################################################################
# Service
##############################################################################


class VisualRecognitionV3(BaseService):
    """The Visual Recognition V3 service."""

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
    # General
    #########################

    def classify(self,
                 *,
                 images_file: BinaryIO = None,
                 images_filename: str = None,
                 images_file_content_type: str = None,
                 url: str = None,
                 threshold: float = None,
                 owners: str = None,
                 classifier_ids: str = None,
                 accept_language: str = None,
                 **kwargs) -> 'DetailedResponse':
        """
        Classify images.

        Classify images with built-in or custom classifiers.

        :param TextIO images_file: (optional) An image file (.gif, .jpg, .png,
               .tif) or .zip file with images. Maximum image size is 10 MB. Include no
               more than 20 images and limit the .zip file to 100 MB. Encode the image and
               .zip file names in UTF-8 if they contain non-ASCII characters. The service
               assumes UTF-8 encoding if it encounters non-ASCII characters.
               You can also include an image with the **url** parameter.
        :param str images_filename: (optional) The filename for images_file.
        :param str images_file_content_type: (optional) The content type of
               images_file.
        :param str url: (optional) The URL of an image (.gif, .jpg, .png, .tif) to
               analyze. The minimum recommended pixel density is 32X32 pixels, but the
               service tends to perform better with images that are at least 224 x 224
               pixels. The maximum image size is 10 MB.
               You can also include images with the **images_file** parameter.
        :param float threshold: (optional) The minimum score a class must have to
               be displayed in the response. Set the threshold to `0.0` to return all
               identified classes.
        :param List[str] owners: (optional) The categories of classifiers to apply.
               The **classifier_ids** parameter overrides **owners**, so make sure that
               **classifier_ids** is empty.
               - Use `IBM` to classify against the `default` general classifier. You get
               the same result if both **classifier_ids** and **owners** parameters are
               empty.
               - Use `me` to classify against all your custom classifiers. However, for
               better performance use **classifier_ids** to specify the specific custom
               classifiers to apply.
               - Use both `IBM` and `me` to analyze the image against both classifier
               categories.
        :param List[str] classifier_ids: (optional) Which classifiers to apply.
               Overrides the **owners** parameter. You can specify both custom and
               built-in classifier IDs. The built-in `default` classifier is used if both
               **classifier_ids** and **owners** parameters are empty.
               The following built-in classifier IDs require no training:
               - `default`: Returns classes from thousands of general tags.
               - `food`: Enhances specificity and accuracy for images of food items.
               - `explicit`: Evaluates whether the image might be pornographic.
        :param str accept_language: (optional) The desired language of parts of the
               response. See the response for details.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {'Accept-Language': accept_language}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='classify')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        if images_file:
            if not images_filename and hasattr(images_file, 'name'):
                images_filename = basename(images_file.name)
            if not images_filename:
                raise ValueError('images_filename must be provided')
            form_data.append(('images_file', (images_filename, images_file,
                                              images_file_content_type or
                                              'application/octet-stream')))
        if url:
            url = str(url)
            form_data.append(('url', (None, url, 'text/plain')))
        if threshold:
            threshold = str(threshold)
            form_data.append(('threshold', (None, threshold, 'text/plain')))
        if owners:
            owners = self._convert_list(owners)
            form_data.append(('owners', (None, owners, 'text/plain')))
        if classifier_ids:
            classifier_ids = self._convert_list(classifier_ids)
            form_data.append(
                ('classifier_ids', (None, classifier_ids, 'text/plain')))

        url = '/v3/classify'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    #########################
    # Custom
    #########################

    def create_classifier(self,
                          name: str,
                          positive_examples: BinaryIO,
                          *,
                          negative_examples: BinaryIO = None,
                          negative_examples_filename: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Create a classifier.

        Train a new multi-faceted classifier on the uploaded image data. Create your
        custom classifier with positive or negative example training images. Include at
        least two sets of examples, either two positive example files or one positive and
        one negative file. You can upload a maximum of 256 MB per call.
        **Tips when creating:**
        - If you set the **X-Watson-Learning-Opt-Out** header parameter to `true` when you
        create a classifier, the example training images are not stored. Save your
        training images locally. For more information, see [Data
        collection](#data-collection).
        - Encode all names in UTF-8 if they contain non-ASCII characters (.zip and image
        file names, and classifier and class names). The service assumes UTF-8 encoding if
        it encounters non-ASCII characters.

        :param str name: The name of the new classifier. Encode special characters
               in UTF-8.
        :param dict positive_examples: A dictionary that contains the value for
               each classname. The value is a .zip file of images that depict the visual
               subject of a class in the new classifier. You can include more than one
               positive example file in a call.
               Specify the parameter name by appending `_positive_examples` to the class
               name. For example, `goldenretriever_positive_examples` creates the class
               **goldenretriever**. The string cannot contain the following characters:
               ``$ * - { } \ | / ' " ` [ ]``.
               Include at least 10 images in .jpg or .png format. The minimum recommended
               image resolution is 32X32 pixels. The maximum number of images is 10,000
               images or 100 MB per .zip file.
               Encode special characters in the file name in UTF-8.
        :param TextIO negative_examples: (optional) A .zip file of images that do
               not depict the visual subject of any of the classes of the new classifier.
               Must contain a minimum of 10 images.
               Encode special characters in the file name in UTF-8.
        :param str negative_examples_filename: (optional) The filename for
               negative_examples.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if name is None:
            raise ValueError('name must be provided')
        if not positive_examples:
            raise ValueError('positive_examples must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='create_classifier')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        name = str(name)
        form_data.append(('name', (None, name, 'text/plain')))
        for key in positive_examples.keys():
            part_name = '%s_positive_examples' % (key)
            value = positive_examples[key]
            if hasattr(value, 'name'):
                filename = basename(value.name)
                form_data.append(
                    (part_name, (filename, value, 'application/octet-stream')))
        if negative_examples:
            if not negative_examples_filename and hasattr(
                    negative_examples, 'name'):
                negative_examples_filename = basename(negative_examples.name)
            if not negative_examples_filename:
                raise ValueError('negative_examples_filename must be provided')
            form_data.append(('negative_examples',
                              (negative_examples_filename, negative_examples,
                               'application/octet-stream')))

        url = '/v3/classifiers'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def list_classifiers(self,
                         *,
                         verbose: bool = None,
                         **kwargs) -> 'DetailedResponse':
        """
        Retrieve a list of classifiers.

        :param bool verbose: (optional) Specify `true` to return details about the
               classifiers. Omit this parameter to return a brief list of classifiers.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='list_classifiers')
        headers.update(sdk_headers)

        params = {'version': self.version, 'verbose': verbose}

        url = '/v3/classifiers'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def get_classifier(self, classifier_id: str,
                       **kwargs) -> 'DetailedResponse':
        """
        Retrieve classifier details.

        Retrieve information about a custom classifier.

        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_classifier')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    def update_classifier(self,
                          classifier_id: str,
                          *,
                          positive_examples: BinaryIO = {},
                          negative_examples: BinaryIO = None,
                          negative_examples_filename: str = None,
                          **kwargs) -> 'DetailedResponse':
        """
        Update a classifier.

        Update a custom classifier by adding new positive or negative classes or by adding
        new images to existing classes. You must supply at least one set of positive or
        negative examples. For details, see [Updating custom
        classifiers](https://cloud.ibm.com/docs/visual-recognition?topic=visual-recognition-customizing#updating-custom-classifiers).
        Encode all names in UTF-8 if they contain non-ASCII characters (.zip and image
        file names, and classifier and class names). The service assumes UTF-8 encoding if
        it encounters non-ASCII characters.
        **Tips about retraining:**
        - You can't update the classifier if the **X-Watson-Learning-Opt-Out** header
        parameter was set to `true` when the classifier was created. Training images are
        not stored in that case. Instead, create another classifier. For more information,
        see [Data collection](#data-collection).
        - Don't make retraining calls on a classifier until the status is ready. When you
        submit retraining requests in parallel, the last request overwrites the previous
        requests. The `retrained` property shows the last time the classifier retraining
        finished.

        :param str classifier_id: The ID of the classifier.
        :param dict positive_examples: (optional) A dictionary that contains the
               value for each classname. The value is a .zip file of images that depict
               the visual subject of a class in the classifier. The positive examples
               create or update classes in the classifier. You can include more than one
               positive example file in a call.
               Specify the parameter name by appending `_positive_examples` to the class
               name. For example, `goldenretriever_positive_examples` creates the class
               `goldenretriever`. The string cannot contain the following characters: ``$
               * - { } \ | / ' " ` [ ]``.
               Include at least 10 images in .jpg or .png format. The minimum recommended
               image resolution is 32X32 pixels. The maximum number of images is 10,000
               images or 100 MB per .zip file.
               Encode special characters in the file name in UTF-8.
        :param TextIO negative_examples: (optional) A .zip file of images that do
               not depict the visual subject of any of the classes of the new classifier.
               Must contain a minimum of 10 images.
               Encode special characters in the file name in UTF-8.
        :param str negative_examples_filename: (optional) The filename for
               negative_examples.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='update_classifier')
        headers.update(sdk_headers)

        params = {'version': self.version}

        form_data = []
        for key in positive_examples.keys():
            part_name = '%s_positive_examples' % (key)
            value = positive_examples[key]
            if hasattr(value, 'name'):
                filename = basename(value.name)
                form_data.append(
                    (part_name, (filename, value, 'application/octet-stream')))
        if negative_examples:
            if not negative_examples_filename and hasattr(
                    negative_examples, 'name'):
                negative_examples_filename = basename(negative_examples.name)
            if not negative_examples_filename:
                raise ValueError('negative_examples_filename must be provided')
            form_data.append(('negative_examples',
                              (negative_examples_filename, negative_examples,
                               'application/octet-stream')))

        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       files=form_data)

        response = self.send(request)
        return response

    def delete_classifier(self, classifier_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Delete a classifier.

        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='delete_classifier')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v3/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response

    #########################
    # Core ML
    #########################

    def get_core_ml_model(self, classifier_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Retrieve a Core ML model of a classifier.

        Download a Core ML model file (.mlmodel) of a custom classifier that returns
        <tt>"core_ml_enabled": true</tt> in the classifier details.

        :param str classifier_id: The ID of the classifier.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_core_ml_model')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v3/classifiers/{0}/core_ml_model'.format(
            *self._encode_path_vars(classifier_id))
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
                                      service_version='V3',
                                      operation_id='delete_user_data')
        headers.update(sdk_headers)

        params = {'version': self.version, 'customer_id': customer_id}

        url = '/v3/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request)
        return response


class ClassifyEnums(object):

    class AcceptLanguage(Enum):
        """
        The desired language of parts of the response. See the response for details.
        """
        EN = 'en'
        AR = 'ar'
        DE = 'de'
        ES = 'es'
        FR = 'fr'
        IT = 'it'
        JA = 'ja'
        KO = 'ko'
        PT_BR = 'pt-br'
        ZH_CN = 'zh-cn'
        ZH_TW = 'zh-tw'


##############################################################################
# Models
##############################################################################


class Class():
    """
    A category within a classifier.

    :attr str class_: The name of the class.
    """

    def __init__(self, class_: str) -> None:
        """
        Initialize a Class object.

        :param str class_: The name of the class.
        """
        self.class_ = class_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Class':
        """Initialize a Class object from a json dictionary."""
        args = {}
        valid_keys = ['class_', 'class']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Class: ' +
                ', '.join(bad_keys))
        if 'class' in _dict:
            args['class_'] = _dict.get('class')
        else:
            raise ValueError(
                'Required property \'class\' not present in Class JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Class object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'class_') and self.class_ is not None:
            _dict['class'] = self.class_
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Class object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Class') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Class') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassResult():
    """
    Result of a class within a classifier.

    :attr str class_: Name of the class.
          Class names are translated in the language defined by the **Accept-Language**
          request header for the build-in classifier IDs (`default`, `food`, and
          `explicit`). Class names of custom classifiers are not translated. The response
          might not be in the specified language when the requested language is not
          supported or when there is no translation for the class name.
    :attr float score: Confidence score for the property in the range of 0 to 1. A
          higher score indicates greater likelihood that the class is depicted in the
          image. The default threshold for returning scores from a classifier is 0.5.
    :attr str type_hierarchy: (optional) Knowledge graph of the property. For
          example, `/fruit/pome/apple/eating apple/Granny Smith`. Included only if
          identified.
    """

    def __init__(self,
                 class_: str,
                 score: float,
                 *,
                 type_hierarchy: str = None) -> None:
        """
        Initialize a ClassResult object.

        :param str class_: Name of the class.
               Class names are translated in the language defined by the
               **Accept-Language** request header for the build-in classifier IDs
               (`default`, `food`, and `explicit`). Class names of custom classifiers are
               not translated. The response might not be in the specified language when
               the requested language is not supported or when there is no translation for
               the class name.
        :param float score: Confidence score for the property in the range of 0 to
               1. A higher score indicates greater likelihood that the class is depicted
               in the image. The default threshold for returning scores from a classifier
               is 0.5.
        :param str type_hierarchy: (optional) Knowledge graph of the property. For
               example, `/fruit/pome/apple/eating apple/Granny Smith`. Included only if
               identified.
        """
        self.class_ = class_
        self.score = score
        self.type_hierarchy = type_hierarchy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassResult':
        """Initialize a ClassResult object from a json dictionary."""
        args = {}
        valid_keys = ['class_', 'class', 'score', 'type_hierarchy']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassResult: '
                + ', '.join(bad_keys))
        if 'class' in _dict:
            args['class_'] = _dict.get('class')
        else:
            raise ValueError(
                'Required property \'class\' not present in ClassResult JSON')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
        else:
            raise ValueError(
                'Required property \'score\' not present in ClassResult JSON')
        if 'type_hierarchy' in _dict:
            args['type_hierarchy'] = _dict.get('type_hierarchy')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'class_') and self.class_ is not None:
            _dict['class'] = self.class_
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'type_hierarchy') and self.type_hierarchy is not None:
            _dict['type_hierarchy'] = self.type_hierarchy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedImage():
    """
    Results for one image.

    :attr str source_url: (optional) Source of the image before any redirects. Not
          returned when the image is uploaded.
    :attr str resolved_url: (optional) Fully resolved URL of the image after
          redirects are followed. Not returned when the image is uploaded.
    :attr str image: (optional) Relative path of the image file if uploaded
          directly. Not returned when the image is passed by URL.
    :attr ErrorInfo error: (optional) Information about what might have caused a
          failure, such as an image that is too large. Not returned when there is no
          error.
    :attr List[ClassifierResult] classifiers: The classifiers.
    """

    def __init__(self,
                 classifiers: List['ClassifierResult'],
                 *,
                 source_url: str = None,
                 resolved_url: str = None,
                 image: str = None,
                 error: 'ErrorInfo' = None) -> None:
        """
        Initialize a ClassifiedImage object.

        :param List[ClassifierResult] classifiers: The classifiers.
        :param str source_url: (optional) Source of the image before any redirects.
               Not returned when the image is uploaded.
        :param str resolved_url: (optional) Fully resolved URL of the image after
               redirects are followed. Not returned when the image is uploaded.
        :param str image: (optional) Relative path of the image file if uploaded
               directly. Not returned when the image is passed by URL.
        :param ErrorInfo error: (optional) Information about what might have caused
               a failure, such as an image that is too large. Not returned when there is
               no error.
        """
        self.source_url = source_url
        self.resolved_url = resolved_url
        self.image = image
        self.error = error
        self.classifiers = classifiers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifiedImage':
        """Initialize a ClassifiedImage object from a json dictionary."""
        args = {}
        valid_keys = [
            'source_url', 'resolved_url', 'image', 'error', 'classifiers'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifiedImage: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedImage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifiedImage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifiedImage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifiedImage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedImages():
    """
    Results for all images.

    :attr int custom_classes: (optional) Number of custom classes identified in the
          images.
    :attr int images_processed: (optional) Number of images processed for the API
          call.
    :attr List[ClassifiedImage] images: Classified images.
    :attr List[WarningInfo] warnings: (optional) Information about what might cause
          less than optimal output. For example, a request sent with a corrupt .zip file
          and a list of image URLs will still complete, but does not return the expected
          output. Not returned when there is no warning.
    """

    def __init__(self,
                 images: List['ClassifiedImage'],
                 *,
                 custom_classes: int = None,
                 images_processed: int = None,
                 warnings: List['WarningInfo'] = None) -> None:
        """
        Initialize a ClassifiedImages object.

        :param List[ClassifiedImage] images: Classified images.
        :param int custom_classes: (optional) Number of custom classes identified
               in the images.
        :param int images_processed: (optional) Number of images processed for the
               API call.
        :param List[WarningInfo] warnings: (optional) Information about what might
               cause less than optimal output. For example, a request sent with a corrupt
               .zip file and a list of image URLs will still complete, but does not return
               the expected output. Not returned when there is no warning.
        """
        self.custom_classes = custom_classes
        self.images_processed = images_processed
        self.images = images
        self.warnings = warnings

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifiedImages':
        """Initialize a ClassifiedImages object from a json dictionary."""
        args = {}
        valid_keys = [
            'custom_classes', 'images_processed', 'images', 'warnings'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifiedImages: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedImages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifiedImages object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifiedImages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifiedImages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Classifier():
    """
    Information about a classifier.

    :attr str classifier_id: ID of a classifier identified in the image.
    :attr str name: Name of the classifier.
    :attr str owner: (optional) Unique ID of the account who owns the classifier.
          Might not be returned by some requests.
    :attr str status: (optional) Training status of classifier.
    :attr bool core_ml_enabled: (optional) Whether the classifier can be downloaded
          as a Core ML model after the training status is `ready`.
    :attr str explanation: (optional) If classifier training has failed, this field
          might explain why.
    :attr datetime created: (optional) Date and time in Coordinated Universal Time
          (UTC) that the classifier was created.
    :attr List[Class] classes: (optional) Classes that define a classifier.
    :attr datetime retrained: (optional) Date and time in Coordinated Universal Time
          (UTC) that the classifier was updated. Might not be returned by some requests.
          Identical to `updated` and retained for backward compatibility.
    :attr datetime updated: (optional) Date and time in Coordinated Universal Time
          (UTC) that the classifier was most recently updated. The field matches either
          `retrained` or `created`. Might not be returned by some requests.
    """

    def __init__(self,
                 classifier_id: str,
                 name: str,
                 *,
                 owner: str = None,
                 status: str = None,
                 core_ml_enabled: bool = None,
                 explanation: str = None,
                 created: datetime = None,
                 classes: List['Class'] = None,
                 retrained: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a Classifier object.

        :param str classifier_id: ID of a classifier identified in the image.
        :param str name: Name of the classifier.
        :param str owner: (optional) Unique ID of the account who owns the
               classifier. Might not be returned by some requests.
        :param str status: (optional) Training status of classifier.
        :param bool core_ml_enabled: (optional) Whether the classifier can be
               downloaded as a Core ML model after the training status is `ready`.
        :param str explanation: (optional) If classifier training has failed, this
               field might explain why.
        :param datetime created: (optional) Date and time in Coordinated Universal
               Time (UTC) that the classifier was created.
        :param List[Class] classes: (optional) Classes that define a classifier.
        :param datetime retrained: (optional) Date and time in Coordinated
               Universal Time (UTC) that the classifier was updated. Might not be returned
               by some requests. Identical to `updated` and retained for backward
               compatibility.
        :param datetime updated: (optional) Date and time in Coordinated Universal
               Time (UTC) that the classifier was most recently updated. The field matches
               either `retrained` or `created`. Might not be returned by some requests.
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
    def from_dict(cls, _dict: Dict) -> 'Classifier':
        """Initialize a Classifier object from a json dictionary."""
        args = {}
        valid_keys = [
            'classifier_id', 'name', 'owner', 'status', 'core_ml_enabled',
            'explanation', 'created', 'classes', 'retrained', 'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Classifier: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classifier object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
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

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Classifier object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Classifier') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Classifier') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        Training status of classifier.
        """
        READY = "ready"
        TRAINING = "training"
        RETRAINING = "retraining"
        FAILED = "failed"


class ClassifierResult():
    """
    Classifier and score combination.

    :attr str name: Name of the classifier.
    :attr str classifier_id: ID of a classifier identified in the image.
    :attr List[ClassResult] classes: Classes within the classifier.
    """

    def __init__(self, name: str, classifier_id: str,
                 classes: List['ClassResult']) -> None:
        """
        Initialize a ClassifierResult object.

        :param str name: Name of the classifier.
        :param str classifier_id: ID of a classifier identified in the image.
        :param List[ClassResult] classes: Classes within the classifier.
        """
        self.name = name
        self.classifier_id = classifier_id
        self.classes = classes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifierResult':
        """Initialize a ClassifierResult object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'classifier_id', 'classes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifierResult: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifierResult object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifierResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifierResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Classifiers():
    """
    A container for the list of classifiers.

    :attr List[Classifier] classifiers: List of classifiers.
    """

    def __init__(self, classifiers: List['Classifier']) -> None:
        """
        Initialize a Classifiers object.

        :param List[Classifier] classifiers: List of classifiers.
        """
        self.classifiers = classifiers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Classifiers':
        """Initialize a Classifiers object from a json dictionary."""
        args = {}
        valid_keys = ['classifiers']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Classifiers: '
                + ', '.join(bad_keys))
        if 'classifiers' in _dict:
            args['classifiers'] = [
                Classifier._from_dict(x) for x in (_dict.get('classifiers'))
            ]
        else:
            raise ValueError(
                'Required property \'classifiers\' not present in Classifiers JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classifiers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifiers') and self.classifiers is not None:
            _dict['classifiers'] = [x._to_dict() for x in self.classifiers]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Classifiers object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Classifiers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Classifiers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ErrorInfo():
    """
    Information about what might have caused a failure, such as an image that is too
    large. Not returned when there is no error.

    :attr int code: HTTP status code.
    :attr str description: Human-readable error description. For example, `File size
          limit exceeded`.
    :attr str error_id: Codified error string. For example, `limit_exceeded`.
    """

    def __init__(self, code: int, description: str, error_id: str) -> None:
        """
        Initialize a ErrorInfo object.

        :param int code: HTTP status code.
        :param str description: Human-readable error description. For example,
               `File size limit exceeded`.
        :param str error_id: Codified error string. For example, `limit_exceeded`.
        """
        self.code = code
        self.description = description
        self.error_id = error_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ErrorInfo':
        """Initialize a ErrorInfo object from a json dictionary."""
        args = {}
        valid_keys = ['code', 'description', 'error_id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ErrorInfo: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ErrorInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'error_id') and self.error_id is not None:
            _dict['error_id'] = self.error_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ErrorInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ErrorInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ErrorInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WarningInfo():
    """
    Information about something that went wrong.

    :attr str warning_id: Codified warning string, such as `limit_reached`.
    :attr str description: Information about the error.
    """

    def __init__(self, warning_id: str, description: str) -> None:
        """
        Initialize a WarningInfo object.

        :param str warning_id: Codified warning string, such as `limit_reached`.
        :param str description: Information about the error.
        """
        self.warning_id = warning_id
        self.description = description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WarningInfo':
        """Initialize a WarningInfo object from a json dictionary."""
        args = {}
        valid_keys = ['warning_id', 'description']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WarningInfo: '
                + ', '.join(bad_keys))
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

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WarningInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'warning_id') and self.warning_id is not None:
            _dict['warning_id'] = self.warning_id
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WarningInfo object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'WarningInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WarningInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
