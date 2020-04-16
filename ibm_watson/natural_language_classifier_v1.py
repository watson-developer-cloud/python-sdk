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
IBM Watson&trade; Natural Language Classifier uses machine learning algorithms to return
the top matching predefined classes for short text input. You create and train a
classifier to connect predefined classes to example texts so that the service can apply
those classes to new inputs.
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

##############################################################################
# Service
##############################################################################


class NaturalLanguageClassifierV1(BaseService):
    """The Natural Language Classifier V1 service."""

    DEFAULT_SERVICE_URL = 'https://gateway.watsonplatform.net/natural-language-classifier/api'
    DEFAULT_SERVICE_NAME = 'natural_language_classifier'

    def __init__(
            self,
            authenticator: Authenticator = None,
            service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Natural Language Classifier service.

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
        self.configure_service(service_name)

    #########################
    # Classify text
    #########################

    def classify(self, classifier_id: str, text: str,
                 **kwargs) -> 'DetailedResponse':
        """
        Classify a phrase.

        Returns label information for the input. The status must be `Available` before you
        can use the classifier to classify text.

        :param str classifier_id: Classifier ID to use.
        :param str text: The submitted phrase. The maximum length is 2048
               characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='classify')
        headers.update(sdk_headers)

        data = {'text': text}

        url = '/v1/classifiers/{0}/classify'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    def classify_collection(self, classifier_id: str,
                            collection: List['ClassifyInput'],
                            **kwargs) -> 'DetailedResponse':
        """
        Classify multiple phrases.

        Returns label information for multiple phrases. The status must be `Available`
        before you can use the classifier to classify text.
        Note that classifying Japanese texts is a beta feature.

        :param str classifier_id: Classifier ID to use.
        :param List[ClassifyInput] collection: The submitted phrases.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        if collection is None:
            raise ValueError('collection must be provided')
        collection = [self._convert_model(x) for x in collection]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='classify_collection')
        headers.update(sdk_headers)

        data = {'collection': collection}

        url = '/v1/classifiers/{0}/classify_collection'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response

    #########################
    # Manage classifiers
    #########################

    def create_classifier(self, training_metadata: BinaryIO,
                          training_data: BinaryIO,
                          **kwargs) -> 'DetailedResponse':
        """
        Create classifier.

        Sends data to create and train a classifier and returns information about the new
        classifier.

        :param TextIO training_metadata: Metadata in JSON format. The metadata
               identifies the language of the data, and an optional name to identify the
               classifier. Specify the language with the 2-letter primary language code as
               assigned in ISO standard 639.
               Supported languages are English (`en`), Arabic (`ar`), French (`fr`),
               German, (`de`), Italian (`it`), Japanese (`ja`), Korean (`ko`), Brazilian
               Portuguese (`pt`), and Spanish (`es`).
        :param TextIO training_data: Training data in CSV format. Each text value
               must have at least one class. The data can include up to 3,000 classes and
               20,000 records. For details, see [Data
               preparation](https://cloud.ibm.com/docs/natural-language-classifier?topic=natural-language-classifier-using-your-data).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if training_metadata is None:
            raise ValueError('training_metadata must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='create_classifier')
        headers.update(sdk_headers)

        form_data = []
        form_data.append(('training_metadata', (None, training_metadata,
                                                'application/json')))
        form_data.append(('training_data', (None, training_data, 'text/csv')))

        url = '/v1/classifiers'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       files=form_data)

        response = self.send(request)
        return response

    def list_classifiers(self, **kwargs) -> 'DetailedResponse':
        """
        List classifiers.

        Returns an empty array if no classifiers are available.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V1',
                                      operation_id='list_classifiers')
        headers.update(sdk_headers)

        url = '/v1/classifiers'
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request)
        return response

    def get_classifier(self, classifier_id: str,
                       **kwargs) -> 'DetailedResponse':
        """
        Get information about a classifier.

        Returns status and other information about a classifier.

        :param str classifier_id: Classifier ID to query.
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
                                      service_version='V1',
                                      operation_id='get_classifier')
        headers.update(sdk_headers)

        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='GET', url=url, headers=headers)

        response = self.send(request)
        return response

    def delete_classifier(self, classifier_id: str,
                          **kwargs) -> 'DetailedResponse':
        """
        Delete classifier.

        :param str classifier_id: Classifier ID to delete.
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
                                      service_version='V1',
                                      operation_id='delete_classifier')
        headers.update(sdk_headers)

        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class Classification():
    """
    Response from the classifier for a phrase.

    :attr str classifier_id: (optional) Unique identifier for this classifier.
    :attr str url: (optional) Link to the classifier.
    :attr str text: (optional) The submitted phrase.
    :attr str top_class: (optional) The class with the highest confidence.
    :attr List[ClassifiedClass] classes: (optional) An array of up to ten
          class-confidence pairs sorted in descending order of confidence.
    """

    def __init__(self,
                 *,
                 classifier_id: str = None,
                 url: str = None,
                 text: str = None,
                 top_class: str = None,
                 classes: List['ClassifiedClass'] = None) -> None:
        """
        Initialize a Classification object.

        :param str classifier_id: (optional) Unique identifier for this classifier.
        :param str url: (optional) Link to the classifier.
        :param str text: (optional) The submitted phrase.
        :param str top_class: (optional) The class with the highest confidence.
        :param List[ClassifiedClass] classes: (optional) An array of up to ten
               class-confidence pairs sorted in descending order of confidence.
        """
        self.classifier_id = classifier_id
        self.url = url
        self.text = text
        self.top_class = top_class
        self.classes = classes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Classification':
        """Initialize a Classification object from a json dictionary."""
        args = {}
        valid_keys = ['classifier_id', 'url', 'text', 'top_class', 'classes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Classification: '
                + ', '.join(bad_keys))
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'top_class' in _dict:
            args['top_class'] = _dict.get('top_class')
        if 'classes' in _dict:
            args['classes'] = [
                ClassifiedClass._from_dict(x) for x in (_dict.get('classes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classification object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'top_class') and self.top_class is not None:
            _dict['top_class'] = self.top_class
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Classification object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'Classification') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Classification') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassificationCollection():
    """
    Response from the classifier for multiple phrases.

    :attr str classifier_id: (optional) Unique identifier for this classifier.
    :attr str url: (optional) Link to the classifier.
    :attr List[CollectionItem] collection: (optional) An array of classifier
          responses for each submitted phrase.
    """

    def __init__(self,
                 *,
                 classifier_id: str = None,
                 url: str = None,
                 collection: List['CollectionItem'] = None) -> None:
        """
        Initialize a ClassificationCollection object.

        :param str classifier_id: (optional) Unique identifier for this classifier.
        :param str url: (optional) Link to the classifier.
        :param List[CollectionItem] collection: (optional) An array of classifier
               responses for each submitted phrase.
        """
        self.classifier_id = classifier_id
        self.url = url
        self.collection = collection

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationCollection':
        """Initialize a ClassificationCollection object from a json dictionary."""
        args = {}
        valid_keys = ['classifier_id', 'url', 'collection']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassificationCollection: '
                + ', '.join(bad_keys))
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'collection' in _dict:
            args['collection'] = [
                CollectionItem._from_dict(x) for x in (_dict.get('collection'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'collection') and self.collection is not None:
            _dict['collection'] = [x._to_dict() for x in self.collection]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedClass():
    """
    Class and confidence.

    :attr float confidence: (optional) A decimal percentage that represents the
          confidence that Watson has in this class. Higher values represent higher
          confidences.
    :attr str class_name: (optional) Class label.
    """

    def __init__(self,
                 *,
                 confidence: float = None,
                 class_name: str = None) -> None:
        """
        Initialize a ClassifiedClass object.

        :param float confidence: (optional) A decimal percentage that represents
               the confidence that Watson has in this class. Higher values represent
               higher confidences.
        :param str class_name: (optional) Class label.
        """
        self.confidence = confidence
        self.class_name = class_name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifiedClass':
        """Initialize a ClassifiedClass object from a json dictionary."""
        args = {}
        valid_keys = ['confidence', 'class_name']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifiedClass: '
                + ', '.join(bad_keys))
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'class_name' in _dict:
            args['class_name'] = _dict.get('class_name')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedClass object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'class_name') and self.class_name is not None:
            _dict['class_name'] = self.class_name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifiedClass object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifiedClass') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifiedClass') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Classifier():
    """
    A classifier for natural language phrases.

    :attr str name: (optional) User-supplied name for the classifier.
    :attr str url: Link to the classifier.
    :attr str status: (optional) The state of the classifier.
    :attr str classifier_id: Unique identifier for this classifier.
    :attr datetime created: (optional) Date and time (UTC) the classifier was
          created.
    :attr str status_description: (optional) Additional detail about the status.
    :attr str language: (optional) The language used for the classifier.
    """

    def __init__(self,
                 url: str,
                 classifier_id: str,
                 *,
                 name: str = None,
                 status: str = None,
                 created: datetime = None,
                 status_description: str = None,
                 language: str = None) -> None:
        """
        Initialize a Classifier object.

        :param str url: Link to the classifier.
        :param str classifier_id: Unique identifier for this classifier.
        :param str name: (optional) User-supplied name for the classifier.
        :param str status: (optional) The state of the classifier.
        :param datetime created: (optional) Date and time (UTC) the classifier was
               created.
        :param str status_description: (optional) Additional detail about the
               status.
        :param str language: (optional) The language used for the classifier.
        """
        self.name = name
        self.url = url
        self.status = status
        self.classifier_id = classifier_id
        self.created = created
        self.status_description = status_description
        self.language = language

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Classifier':
        """Initialize a Classifier object from a json dictionary."""
        args = {}
        valid_keys = [
            'name', 'url', 'status', 'classifier_id', 'created',
            'status_description', 'language'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Classifier: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in Classifier JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        else:
            raise ValueError(
                'Required property \'classifier_id\' not present in Classifier JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classifier object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(
                self,
                'status_description') and self.status_description is not None:
            _dict['status_description'] = self.status_description
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
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
        The state of the classifier.
        """
        NON_EXISTENT = "Non Existent"
        TRAINING = "Training"
        FAILED = "Failed"
        AVAILABLE = "Available"
        UNAVAILABLE = "Unavailable"


class ClassifierList():
    """
    List of available classifiers.

    :attr List[Classifier] classifiers: The classifiers available to the user.
          Returns an empty array if no classifiers are available.
    """

    def __init__(self, classifiers: List['Classifier']) -> None:
        """
        Initialize a ClassifierList object.

        :param List[Classifier] classifiers: The classifiers available to the user.
               Returns an empty array if no classifiers are available.
        """
        self.classifiers = classifiers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifierList':
        """Initialize a ClassifierList object from a json dictionary."""
        args = {}
        valid_keys = ['classifiers']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifierList: '
                + ', '.join(bad_keys))
        if 'classifiers' in _dict:
            args['classifiers'] = [
                Classifier._from_dict(x) for x in (_dict.get('classifiers'))
            ]
        else:
            raise ValueError(
                'Required property \'classifiers\' not present in ClassifierList JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierList object from a json dictionary."""
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
        """Return a `str` version of this ClassifierList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifierList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifierList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifyInput():
    """
    Request payload to classify.

    :attr str text: The submitted phrase. The maximum length is 2048 characters.
    """

    def __init__(self, text: str) -> None:
        """
        Initialize a ClassifyInput object.

        :param str text: The submitted phrase. The maximum length is 2048
               characters.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassifyInput':
        """Initialize a ClassifyInput object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ClassifyInput: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in ClassifyInput JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifyInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassifyInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'ClassifyInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassifyInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionItem():
    """
    Response from the classifier for a phrase in a collection.

    :attr str text: (optional) The submitted phrase. The maximum length is 2048
          characters.
    :attr str top_class: (optional) The class with the highest confidence.
    :attr List[ClassifiedClass] classes: (optional) An array of up to ten
          class-confidence pairs sorted in descending order of confidence.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 top_class: str = None,
                 classes: List['ClassifiedClass'] = None) -> None:
        """
        Initialize a CollectionItem object.

        :param str text: (optional) The submitted phrase. The maximum length is
               2048 characters.
        :param str top_class: (optional) The class with the highest confidence.
        :param List[ClassifiedClass] classes: (optional) An array of up to ten
               class-confidence pairs sorted in descending order of confidence.
        """
        self.text = text
        self.top_class = top_class
        self.classes = classes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CollectionItem':
        """Initialize a CollectionItem object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'top_class', 'classes']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CollectionItem: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'top_class' in _dict:
            args['top_class'] = _dict.get('top_class')
        if 'classes' in _dict:
            args['classes'] = [
                ClassifiedClass._from_dict(x) for x in (_dict.get('classes'))
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'top_class') and self.top_class is not None:
            _dict['top_class'] = self.top_class
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CollectionItem object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other: 'CollectionItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CollectionItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
