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

    def __init__(self,
                 url=default_url,
                 username=None,
                 password=None,
                 iam_api_key=None,
                 iam_access_token=None,
                 iam_url=None):
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
            vcap_services_name='natural_language_classifier',
            url=url,
            username=username,
            password=password,
            iam_api_key=iam_api_key,
            iam_access_token=iam_access_token,
            iam_url=iam_url,
            use_vcap_services=True)

    #########################
    # Classify text
    #########################

    def classify(self, classifier_id, text, **kwargs):
        """
        Returns label information for the input. The status must be `Available` before you
        can use the classifier to classify text.

        :param str classifier_id: Classifier ID to use.
        :param str text: The submitted phrase.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classification` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {'text': text}
        url = '/v1/classifiers/{0}/classify'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    def classify_collection(self, classifier_id, collection, **kwargs):
        """
        Returns label information for multiple phrases. The status must be `Available`
        before you can use the classifier to classify text.  Note that classifying
        Japanese texts is a beta feature.

        :param str classifier_id: Classifier ID to use.
        :param list[ClassifyInput] collection: The submitted phrases.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ClassificationCollection` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        if collection is None:
            raise ValueError('collection must be provided')
        collection = [
            self._convert_model(x, ClassifyInput) for x in collection
        ]
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        data = {'collection': collection}
        url = '/v1/classifiers/{0}/classify_collection'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='POST',
            url=url,
            headers=headers,
            json=data,
            accept_json=True)
        return response

    #########################
    # Manage classifiers
    #########################

    def create_classifier(self,
                          metadata,
                          training_data,
                          metadata_filename=None,
                          training_data_filename=None,
                          **kwargs):
        """
        Create classifier.

        Sends data to create and train a classifier and returns information about the new
        classifier.

        :param file metadata: Metadata in JSON format. The metadata identifies the language of the data, and an optional name to identify the classifier. Specify the language with the 2-letter primary language code as assigned in ISO standard 639.  Supported languages are English (`en`), Arabic (`ar`), French (`fr`), German, (`de`), Italian (`it`), Japanese (`ja`), Korean (`ko`), Brazilian Portuguese (`pt`), and Spanish (`es`).
        :param file training_data: Training data in CSV format. Each text value must have at least one class. The data can include up to 20,000 records. For details, see [Data preparation](https://console.bluemix.net/docs/services/natural-language-classifier/using-your-data.html).
        :param str metadata_filename: The filename for training_metadata.
        :param str training_data_filename: The filename for training_data.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if metadata is None:
            raise ValueError('metadata must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
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
            headers=headers,
            files={
                'training_metadata': metadata_tuple,
                'training_data': training_data_tuple
            },
            accept_json=True)
        return response

    def delete_classifier(self, classifier_id, **kwargs):
        """
        Delete classifier.

        :param str classifier_id: Classifier ID to delete.
        :param dict headers: A `dict` containing the request headers
        :rtype: None
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        self.request(
            method='DELETE', url=url, headers=headers, accept_json=True)
        return None

    def get_classifier(self, classifier_id, **kwargs):
        """
        Get information about a classifier.

        Returns status and other information about a classifier.

        :param str classifier_id: Classifier ID to query.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `Classifier` response.
        :rtype: dict
        """
        if classifier_id is None:
            raise ValueError('classifier_id must be provided')
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/classifiers/{0}'.format(
            *self._encode_path_vars(classifier_id))
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
        return response

    def list_classifiers(self, **kwargs):
        """
        List classifiers.

        Returns an empty array if no classifiers are available.

        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `ClassifierList` response.
        :rtype: dict
        """
        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        url = '/v1/classifiers'
        response = self.request(
            method='GET', url=url, headers=headers, accept_json=True)
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


class ClassificationCollection(object):
    """
    Response from the classifier for multiple phrases.

    :attr str classifier_id: (optional) Unique identifier for this classifier.
    :attr str url: (optional) Link to the classifier.
    :attr list[CollectionItem] collection: (optional) An array of classifier responses for each submitted phrase.
    """

    def __init__(self, classifier_id=None, url=None, collection=None):
        """
        Initialize a ClassificationCollection object.

        :param str classifier_id: (optional) Unique identifier for this classifier.
        :param str url: (optional) Link to the classifier.
        :param list[CollectionItem] collection: (optional) An array of classifier responses for each submitted phrase.
        """
        self.classifier_id = classifier_id
        self.url = url
        self.collection = collection

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationCollection object from a json dictionary."""
        args = {}
        if 'classifier_id' in _dict:
            args['classifier_id'] = _dict.get('classifier_id')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'collection' in _dict:
            args['collection'] = [
                CollectionItem._from_dict(x) for x in (_dict.get('collection'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'classifier_id') and self.classifier_id is not None:
            _dict['classifier_id'] = self.classifier_id
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'collection') and self.collection is not None:
            _dict['collection'] = [x._to_dict() for x in self.collection]
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassificationCollection object."""
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
            args['confidence'] = _dict.get('confidence')
        if 'class_name' in _dict:
            args['class_name'] = _dict.get('class_name')
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
                Classifier._from_dict(x) for x in (_dict.get('classifiers'))
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


class ClassifyInput(object):
    """
    Request payload to classify.

    :attr str text: The submitted phrase.
    """

    def __init__(self, text):
        """
        Initialize a ClassifyInput object.

        :param str text: The submitted phrase.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassifyInput object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in ClassifyInput JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this ClassifyInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CollectionItem(object):
    """
    Response from the classifier for a phrase in a collection.

    :attr str text: (optional) The submitted phrase.
    :attr str top_class: (optional) The class with the highest confidence.
    :attr list[ClassifiedClass] classes: (optional) An array of up to ten class-confidence pairs sorted in descending order of confidence.
    """

    def __init__(self, text=None, top_class=None, classes=None):
        """
        Initialize a CollectionItem object.

        :param str text: (optional) The submitted phrase.
        :param str top_class: (optional) The class with the highest confidence.
        :param list[ClassifiedClass] classes: (optional) An array of up to ten class-confidence pairs sorted in descending order of confidence.
        """
        self.text = text
        self.top_class = top_class
        self.classes = classes

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CollectionItem object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'top_class' in _dict:
            args['top_class'] = _dict.get('top_class')
        if 'classes' in _dict:
            args['classes'] = [
                ClassifiedClass._from_dict(x) for x in (_dict.get('classes'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'top_class') and self.top_class is not None:
            _dict['top_class'] = self.top_class
        if hasattr(self, 'classes') and self.classes is not None:
            _dict['classes'] = [x._to_dict() for x in self.classes]
        return _dict

    def __str__(self):
        """Return a `str` version of this CollectionItem object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
