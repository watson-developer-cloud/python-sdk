# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2015, 2021.
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
Unit Tests for NaturalLanguageClassifierV1
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import io
import json
import pytest
import re
import responses
import tempfile
import urllib
from ibm_watson.natural_language_classifier_v1 import *


_service = NaturalLanguageClassifierV1(
    authenticator=NoAuthAuthenticator()
    )

_base_url = 'https://api.us-south.natural-language-classifier.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: ClassifyText
##############################################################################
# region

class TestClassify():
    """
    Test Class for classify
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_classify_all_params(self):
        """
        classify()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString/classify')
        mock_response = '{"classifier_id": "classifier_id", "url": "url", "text": "text", "top_class": "top_class", "classes": [{"confidence": 10, "class_name": "class_name"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'
        text = 'testString'

        # Invoke method
        response = _service.classify(
            classifier_id,
            text,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['text'] == 'testString'


    @responses.activate
    def test_classify_value_error(self):
        """
        test_classify_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString/classify')
        mock_response = '{"classifier_id": "classifier_id", "url": "url", "text": "text", "top_class": "top_class", "classes": [{"confidence": 10, "class_name": "class_name"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'
        text = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
            "text": text,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.classify(**req_copy)



class TestClassifyCollection():
    """
    Test Class for classify_collection
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_classify_collection_all_params(self):
        """
        classify_collection()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString/classify_collection')
        mock_response = '{"classifier_id": "classifier_id", "url": "url", "collection": [{"text": "text", "top_class": "top_class", "classes": [{"confidence": 10, "class_name": "class_name"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ClassifyInput model
        classify_input_model = {}
        classify_input_model['text'] = 'How hot will it be today?'

        # Set up parameter values
        classifier_id = 'testString'
        collection = [classify_input_model]

        # Invoke method
        response = _service.classify_collection(
            classifier_id,
            collection,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['collection'] == [classify_input_model]


    @responses.activate
    def test_classify_collection_value_error(self):
        """
        test_classify_collection_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString/classify_collection')
        mock_response = '{"classifier_id": "classifier_id", "url": "url", "collection": [{"text": "text", "top_class": "top_class", "classes": [{"confidence": 10, "class_name": "class_name"}]}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ClassifyInput model
        classify_input_model = {}
        classify_input_model['text'] = 'How hot will it be today?'

        # Set up parameter values
        classifier_id = 'testString'
        collection = [classify_input_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
            "collection": collection,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.classify_collection(**req_copy)



# endregion
##############################################################################
# End of Service: ClassifyText
##############################################################################

##############################################################################
# Start of Service: ManageClassifiers
##############################################################################
# region

class TestCreateClassifier():
    """
    Test Class for create_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_classifier_all_params(self):
        """
        create_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers')
        mock_response = '{"name": "name", "url": "url", "status": "Non Existent", "classifier_id": "classifier_id", "created": "2019-01-01T12:00:00.000Z", "status_description": "status_description", "language": "language"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        training_metadata = io.BytesIO(b'This is a mock file.').getvalue()
        training_data = io.BytesIO(b'This is a mock file.').getvalue()

        # Invoke method
        response = _service.create_classifier(
            training_metadata,
            training_data,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_create_classifier_value_error(self):
        """
        test_create_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers')
        mock_response = '{"name": "name", "url": "url", "status": "Non Existent", "classifier_id": "classifier_id", "created": "2019-01-01T12:00:00.000Z", "status_description": "status_description", "language": "language"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        training_metadata = io.BytesIO(b'This is a mock file.').getvalue()
        training_data = io.BytesIO(b'This is a mock file.').getvalue()

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "training_metadata": training_metadata,
            "training_data": training_data,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_classifier(**req_copy)



class TestListClassifiers():
    """
    Test Class for list_classifiers
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_classifiers_all_params(self):
        """
        list_classifiers()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers')
        mock_response = '{"classifiers": [{"name": "name", "url": "url", "status": "Non Existent", "classifier_id": "classifier_id", "created": "2019-01-01T12:00:00.000Z", "status_description": "status_description", "language": "language"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Invoke method
        response = _service.list_classifiers()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


class TestGetClassifier():
    """
    Test Class for get_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_classifier_all_params(self):
        """
        get_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString')
        mock_response = '{"name": "name", "url": "url", "status": "Non Existent", "classifier_id": "classifier_id", "created": "2019-01-01T12:00:00.000Z", "status_description": "status_description", "language": "language"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.get_classifier(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_classifier_value_error(self):
        """
        test_get_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString')
        mock_response = '{"name": "name", "url": "url", "status": "Non Existent", "classifier_id": "classifier_id", "created": "2019-01-01T12:00:00.000Z", "status_description": "status_description", "language": "language"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_classifier(**req_copy)



class TestDeleteClassifier():
    """
    Test Class for delete_classifier
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_classifier_all_params(self):
        """
        delete_classifier()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Invoke method
        response = _service.delete_classifier(
            classifier_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_delete_classifier_value_error(self):
        """
        test_delete_classifier_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v1/classifiers/testString')
        responses.add(responses.DELETE,
                      url,
                      status=200)

        # Set up parameter values
        classifier_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "classifier_id": classifier_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_classifier(**req_copy)



# endregion
##############################################################################
# End of Service: ManageClassifiers
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Classification():
    """
    Test Class for Classification
    """

    def test_classification_serialization(self):
        """
        Test serialization/deserialization for Classification
        """

        # Construct dict forms of any model objects needed in order to build this model.

        classified_class_model = {} # ClassifiedClass
        classified_class_model['confidence'] = 72.5
        classified_class_model['class_name'] = 'testString'

        # Construct a json representation of a Classification model
        classification_model_json = {}
        classification_model_json['classifier_id'] = 'testString'
        classification_model_json['url'] = 'testString'
        classification_model_json['text'] = 'testString'
        classification_model_json['top_class'] = 'testString'
        classification_model_json['classes'] = [classified_class_model]

        # Construct a model instance of Classification by calling from_dict on the json representation
        classification_model = Classification.from_dict(classification_model_json)
        assert classification_model != False

        # Construct a model instance of Classification by calling from_dict on the json representation
        classification_model_dict = Classification.from_dict(classification_model_json).__dict__
        classification_model2 = Classification(**classification_model_dict)

        # Verify the model instances are equivalent
        assert classification_model == classification_model2

        # Convert model instance back to dict and verify no loss of data
        classification_model_json2 = classification_model.to_dict()
        assert classification_model_json2 == classification_model_json

class TestModel_ClassificationCollection():
    """
    Test Class for ClassificationCollection
    """

    def test_classification_collection_serialization(self):
        """
        Test serialization/deserialization for ClassificationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        classified_class_model = {} # ClassifiedClass
        classified_class_model['confidence'] = 72.5
        classified_class_model['class_name'] = 'testString'

        collection_item_model = {} # CollectionItem
        collection_item_model['text'] = 'testString'
        collection_item_model['top_class'] = 'testString'
        collection_item_model['classes'] = [classified_class_model]

        # Construct a json representation of a ClassificationCollection model
        classification_collection_model_json = {}
        classification_collection_model_json['classifier_id'] = 'testString'
        classification_collection_model_json['url'] = 'testString'
        classification_collection_model_json['collection'] = [collection_item_model]

        # Construct a model instance of ClassificationCollection by calling from_dict on the json representation
        classification_collection_model = ClassificationCollection.from_dict(classification_collection_model_json)
        assert classification_collection_model != False

        # Construct a model instance of ClassificationCollection by calling from_dict on the json representation
        classification_collection_model_dict = ClassificationCollection.from_dict(classification_collection_model_json).__dict__
        classification_collection_model2 = ClassificationCollection(**classification_collection_model_dict)

        # Verify the model instances are equivalent
        assert classification_collection_model == classification_collection_model2

        # Convert model instance back to dict and verify no loss of data
        classification_collection_model_json2 = classification_collection_model.to_dict()
        assert classification_collection_model_json2 == classification_collection_model_json

class TestModel_ClassifiedClass():
    """
    Test Class for ClassifiedClass
    """

    def test_classified_class_serialization(self):
        """
        Test serialization/deserialization for ClassifiedClass
        """

        # Construct a json representation of a ClassifiedClass model
        classified_class_model_json = {}
        classified_class_model_json['confidence'] = 72.5
        classified_class_model_json['class_name'] = 'testString'

        # Construct a model instance of ClassifiedClass by calling from_dict on the json representation
        classified_class_model = ClassifiedClass.from_dict(classified_class_model_json)
        assert classified_class_model != False

        # Construct a model instance of ClassifiedClass by calling from_dict on the json representation
        classified_class_model_dict = ClassifiedClass.from_dict(classified_class_model_json).__dict__
        classified_class_model2 = ClassifiedClass(**classified_class_model_dict)

        # Verify the model instances are equivalent
        assert classified_class_model == classified_class_model2

        # Convert model instance back to dict and verify no loss of data
        classified_class_model_json2 = classified_class_model.to_dict()
        assert classified_class_model_json2 == classified_class_model_json

class TestModel_Classifier():
    """
    Test Class for Classifier
    """

    def test_classifier_serialization(self):
        """
        Test serialization/deserialization for Classifier
        """

        # Construct a json representation of a Classifier model
        classifier_model_json = {}
        classifier_model_json['name'] = 'testString'
        classifier_model_json['url'] = 'testString'
        classifier_model_json['status'] = 'Non Existent'
        classifier_model_json['classifier_id'] = 'testString'
        classifier_model_json['created'] = "2019-01-01T12:00:00Z"
        classifier_model_json['status_description'] = 'testString'
        classifier_model_json['language'] = 'testString'

        # Construct a model instance of Classifier by calling from_dict on the json representation
        classifier_model = Classifier.from_dict(classifier_model_json)
        assert classifier_model != False

        # Construct a model instance of Classifier by calling from_dict on the json representation
        classifier_model_dict = Classifier.from_dict(classifier_model_json).__dict__
        classifier_model2 = Classifier(**classifier_model_dict)

        # Verify the model instances are equivalent
        assert classifier_model == classifier_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_model_json2 = classifier_model.to_dict()
        assert classifier_model_json2 == classifier_model_json

class TestModel_ClassifierList():
    """
    Test Class for ClassifierList
    """

    def test_classifier_list_serialization(self):
        """
        Test serialization/deserialization for ClassifierList
        """

        # Construct dict forms of any model objects needed in order to build this model.

        classifier_model = {} # Classifier
        classifier_model['name'] = 'testString'
        classifier_model['url'] = 'testString'
        classifier_model['status'] = 'Non Existent'
        classifier_model['classifier_id'] = 'testString'
        classifier_model['created'] = "2019-01-01T12:00:00Z"
        classifier_model['status_description'] = 'testString'
        classifier_model['language'] = 'testString'

        # Construct a json representation of a ClassifierList model
        classifier_list_model_json = {}
        classifier_list_model_json['classifiers'] = [classifier_model]

        # Construct a model instance of ClassifierList by calling from_dict on the json representation
        classifier_list_model = ClassifierList.from_dict(classifier_list_model_json)
        assert classifier_list_model != False

        # Construct a model instance of ClassifierList by calling from_dict on the json representation
        classifier_list_model_dict = ClassifierList.from_dict(classifier_list_model_json).__dict__
        classifier_list_model2 = ClassifierList(**classifier_list_model_dict)

        # Verify the model instances are equivalent
        assert classifier_list_model == classifier_list_model2

        # Convert model instance back to dict and verify no loss of data
        classifier_list_model_json2 = classifier_list_model.to_dict()
        assert classifier_list_model_json2 == classifier_list_model_json

class TestModel_ClassifyInput():
    """
    Test Class for ClassifyInput
    """

    def test_classify_input_serialization(self):
        """
        Test serialization/deserialization for ClassifyInput
        """

        # Construct a json representation of a ClassifyInput model
        classify_input_model_json = {}
        classify_input_model_json['text'] = 'testString'

        # Construct a model instance of ClassifyInput by calling from_dict on the json representation
        classify_input_model = ClassifyInput.from_dict(classify_input_model_json)
        assert classify_input_model != False

        # Construct a model instance of ClassifyInput by calling from_dict on the json representation
        classify_input_model_dict = ClassifyInput.from_dict(classify_input_model_json).__dict__
        classify_input_model2 = ClassifyInput(**classify_input_model_dict)

        # Verify the model instances are equivalent
        assert classify_input_model == classify_input_model2

        # Convert model instance back to dict and verify no loss of data
        classify_input_model_json2 = classify_input_model.to_dict()
        assert classify_input_model_json2 == classify_input_model_json

class TestModel_CollectionItem():
    """
    Test Class for CollectionItem
    """

    def test_collection_item_serialization(self):
        """
        Test serialization/deserialization for CollectionItem
        """

        # Construct dict forms of any model objects needed in order to build this model.

        classified_class_model = {} # ClassifiedClass
        classified_class_model['confidence'] = 72.5
        classified_class_model['class_name'] = 'testString'

        # Construct a json representation of a CollectionItem model
        collection_item_model_json = {}
        collection_item_model_json['text'] = 'testString'
        collection_item_model_json['top_class'] = 'testString'
        collection_item_model_json['classes'] = [classified_class_model]

        # Construct a model instance of CollectionItem by calling from_dict on the json representation
        collection_item_model = CollectionItem.from_dict(collection_item_model_json)
        assert collection_item_model != False

        # Construct a model instance of CollectionItem by calling from_dict on the json representation
        collection_item_model_dict = CollectionItem.from_dict(collection_item_model_json).__dict__
        collection_item_model2 = CollectionItem(**collection_item_model_dict)

        # Verify the model instances are equivalent
        assert collection_item_model == collection_item_model2

        # Convert model instance back to dict and verify no loss of data
        collection_item_model_json2 = collection_item_model.to_dict()
        assert collection_item_model_json2 == collection_item_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
