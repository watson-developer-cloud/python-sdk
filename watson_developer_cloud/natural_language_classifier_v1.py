# coding: utf-8

# Copyright 2017 IBM All Rights Reserved.
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
IBM Watson Natural Language Classifier uses machine learning algorithms to return the top
matching predefined classes for short text input. You create and train a classifier to
connect predefined classes to example texts so that the service can apply those classes to
new inputs.
"""

from __future__ import absolute_import

import json
from .watson_service import datetime_to_string, string_to_datetime
from .watson_service import WatsonService

##############################################################################
# Service
##############################################################################


class NaturalLanguageClassifierV1(WatsonService):
    """The Natural Language Classifier V1 service."""

    default_url = 'https://gateway.watsonplatform.net/natural-language-classifier/api'

    def __init__(self, url=default_url, username=None, password=None):
        """
        Construct a new client for the Natural Language Classifier service.

        :param str url: The base url to use when contacting the service (e.g.
               "https://gateway.watsonplatform.net/natural-language-classifier/api").
               The base url may differ between Bluemix regions.

        :param str username: The username used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        :param str password: The password used to authenticate with the service.
               Username and password credentials are only required to run your
               application locally or outside of Bluemix. When running on
               Bluemix, the credentials will be automatically loaded from the
               `VCAP_SERVICES` environment variable.

        """

        WatsonService.__init__(
            self,
            vcap_services_name='natural_language_classifier',
            url=url,
            username=username,
            password=password,
            use_vcap_services=True)

    #########################
    # naturallanguageclassifier
    #########################

    def classify(self, classifier_id, text):
        """
        Returns label information for the input.

        The status must be `Available` before you can use the classifier to classify text.
        Use `Get information about a classifier` to retrieve the status.

        :param str classifier_id: Classifier ID to use.
        :param str text: The submitted phrase.
        :return: A `dict` containing the `Classification` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        data = {'text': text}
        url = '/v1/classifiers/{0}/classify'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='POST', url=url, json=data, accept_json=True)
        return response

    def create_classifier(self,
                          metadata,
                          training_data,
                          metadata_filename=None,
                          training_data_filename=None):
        """
        Create classifier.

        Sends data to create and train a classifier and returns information about the new
        classifier.

        :param file metadata: Metadata in JSON format. The metadata identifies the language of the data, and an optional name to identify the classifier. For details, see the [API reference](https://www.ibm.com/watson/developercloud/natural-language-classifier/api/v1/#create_classifier).
        :param file training_data: Training data in CSV format. Each text value must have at least one class. The data can include up to 15,000 records. For details, see [Using your own data](https://www.ibm.com/watson/developercloud/doc/natural-language-classifier/using-your-data.html).
        :param str metadata_filename: The filename for training_metadata.
        :param str training_data_filename: The filename for training_data.
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if metadata is None:
            raise ValueError('metadata must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        if not metadata_filename and hasattr(metadata, 'name'):
            metadata_filename = metadata.name
        mime_type = 'application/json'
        metadata_tuple = (metadata_filename, metadata, mime_type)
        if not training_data_filename and hasattr(training_data, 'name'):
            training_data_filename = training_data.name
        mime_type = 'text/csv'
        training_data_tuple = (training_data_filename, training_data, mime_type)
        url = '/v1/classifiers'
        response = self.request(
            method='POST',
            url=url,
            files={
                'training_metadata': metadata_tuple,
                'training_data': training_data_tuple
            },
            accept_json=True)
        return response

    def delete_classifier(self, classifier_id):
        """
        Delete classifier.

        :param str classifier_id: Classifier ID to delete.
        :rtype: None
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        self.request(method='DELETE', url=url, accept_json=True)
        return None

    def get_classifier(self, classifier_id):
        """
        Get information about a classifier.

        Returns status and other information about a classifier.

        :param str classifier_id: Classifier ID to query.
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(method='GET', url=url, accept_json=True)
        return response

    def list_classifiers(self):
        """
        List classifiers.

        Returns an empty array if no classifiers are available.

        :return: A `dict` containing the `ClassifierList` response.
        :rtype: dict
        """
        url = '/v1/classifiers'
        response = self.request(method='GET', url=url, accept_json=True)
        return response


##############################################################################
# Models
##############################################################################


class Classification(object):
    """
    Response from the classifier for a phrase.

    :attr str classifier_id: (optional) Unique identifier for this classifier.
    :attr str url: (optional) Link to the classifier.
    :attr str text: (optional) The submitted phrase.
    :attr str top_class: (optional) The class with the highest confidence.
    :attr list[ClassifiedClass] classes: (optional) An array of up to ten class-confidence pairs sorted in descending order of confidence.
    """

    def __init__(self,
                 classifier_id=None,
                 url=None,
                 text=None,
                 top_class=None,
                 classes=None):
        """
        Initialize a Classification object.

        :param str classifier_id: (optional) Unique identifier for this classifier.
        :param str url: (optional) Link to the classifier.
        :param str text: (optional) The submitted phrase.
        :param str top_class: (optional) The class with the highest confidence.
        :param list[ClassifiedClass] classes: (optional) An array of up to ten class-confidence pairs sorted in descending order of confidence.
        """
        self.classifier_id = classifier_id
        self.url = url
        self.text = text
        self.top_class = top_class
        self.classes = classes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Classification object from a json dictionary."""
        args = {}
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict['classifier_id']
        if 'url' in _dict:
            args['url'] = _dict['url']
        if 'text' in _dict:
            args['text'] = _dict['text']
        if 'top_class' in _dict:
            args['top_class'] = _dict['top_class']
        if 'classes' in _dict:
            args['classes'] = [
                ClassifiedClass._from_dict(x) for x in _dict['classes']
            ]
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Classification object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassifiedClass(object):
    """
    Class and confidence.

    :attr float confidence: (optional) A decimal percentage that represents the confidence that Watson has in this class. Higher values represent higher confidences.
    :attr str class_name: (optional) Class label.
    """

    def __init__(self, confidence=None, class_name=None):
        """
        Initialize a ClassifiedClass object.

        :param float confidence: (optional) A decimal percentage that represents the confidence that Watson has in this class. Higher values represent higher confidences.
        :param str class_name: (optional) Class label.
        """
        self.confidence = confidence
        self.class_name = class_name

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifiedClass object from a json dictionary."""
        args = {}
        if 'confidence' in _dict:
            args['confidence'] = _dict['confidence']
        if 'class_name' in _dict:
            args['class_name'] = _dict['class_name']
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'class_name') and self.class_name is not None:
            _dict['class_name'] = self.class_name
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifiedClass object."""
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
    A classifier for natural language phrases.

    :attr str name: (optional) User-supplied name for the classifier.
    :attr str url: Link to the classifier.
    :attr str status: (optional) The state of the classifier.
    :attr str classifier_id: Unique identifier for this classifier.
    :attr datetime created: (optional) Date and time (UTC) the classifier was created.
    :attr str status_description: (optional) Additional detail about the status.
    :attr str language: (optional) The language used for the classifier.
    """

    def __init__(self,
                 url,
                 classifier_id,
                 name=None,
                 status=None,
                 created=None,
                 status_description=None,
                 language=None):
        """
        Initialize a Classifier object.

        :param str url: Link to the classifier.
        :param str classifier_id: Unique identifier for this classifier.
        :param str name: (optional) User-supplied name for the classifier.
        :param str status: (optional) The state of the classifier.
        :param datetime created: (optional) Date and time (UTC) the classifier was created.
        :param str status_description: (optional) Additional detail about the status.
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
    def _from_dict(cls, _dict):
        """Initialize a Classifier object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict['name']
        if 'url' in _dict:
            args['url'] = _dict['url']
        else:
            raise ValueError(
                'Required property \'url\' not present in Classifier JSON')
        if 'status' in _dict:
            args['status'] = _dict['status']
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict['classifier_id']
        else:
            raise ValueError(
                'Required property \'classifier_id\' not present in Classifier JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict['created'])
        if 'status_description' in _dict:
            args['status_description'] = _dict['status_description']
        if 'language' in _dict:
            args['language'] = _dict['language']
        return cls(**args)

    def _to_dict(self):
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


class ClassifierList(object):
    """
    List of available classifiers.

    :attr list[Classifier] classifiers: The classifiers available to the user. Returns an empty array if no classifiers are available.
    """

    def __init__(self, classifiers):
        """
        Initialize a ClassifierList object.

        :param list[Classifier] classifiers: The classifiers available to the user. Returns an empty array if no classifiers are available.
        """
        self.classifiers = classifiers

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifierList object from a json dictionary."""
        args = {}
        if 'classifiers' in _dict:
            args['classifiers'] = [
                Classifier._from_dict(x) for x in _dict['classifiers']
            ]
        else:
            raise ValueError(
                'Required property \'classifiers\' not present in ClassifierList JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifiers') and self.classifiers is not None:
            _dict['classifiers'] = [x._to_dict() for x in self.classifiers]
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifierList object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
