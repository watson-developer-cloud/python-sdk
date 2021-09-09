# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2018, 2021.
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
Unit Tests for PersonalityInsightsV3
"""

from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import re
import requests
import responses
import urllib
from ibm_watson.personality_insights_v3 import *

version = 'testString'

_service = PersonalityInsightsV3(
    authenticator=NoAuthAuthenticator(),
    version=version
    )

_base_url = 'https://api.us-south.personality-insights.watson.cloud.ibm.com'
_service.set_service_url(_base_url)

##############################################################################
# Start of Service: Methods
##############################################################################
# region

class TestProfile():
    """
    Test Class for profile
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
    def test_profile_all_params(self):
        """
        profile()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/profile')
        mock_response = '{"processed_language": "ar", "word_count": 10, "word_count_message": "word_count_message", "personality": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "needs": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "values": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "behavior": [{"trait_id": "trait_id", "name": "name", "category": "category", "percentage": 10}], "consumption_preferences": [{"consumption_preference_category_id": "consumption_preference_category_id", "name": "name", "consumption_preferences": [{"consumption_preference_id": "consumption_preference_id", "name": "name", "score": 0.0}]}], "warnings": [{"warning_id": "WORD_COUNT_MESSAGE", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ContentItem model
        content_item_model = {}
        content_item_model['content'] = 'testString'
        content_item_model['id'] = 'testString'
        content_item_model['created'] = 26
        content_item_model['updated'] = 26
        content_item_model['contenttype'] = 'text/plain'
        content_item_model['language'] = 'en'
        content_item_model['parentid'] = 'testString'
        content_item_model['reply'] = False
        content_item_model['forward'] = False

        # Construct a dict representation of a Content model
        content_model = {}
        content_model['contentItems'] = [content_item_model]

        # Set up parameter values
        content = content_model
        accept = 'application/json'
        content_type = 'text/plain'
        content_language = 'en'
        accept_language = 'en'
        raw_scores = False
        csv_headers = False
        consumption_preferences = False

        # Invoke method
        response = _service.profile(
            content,
            accept,
            content_type=content_type,
            content_language=content_language,
            accept_language=accept_language,
            raw_scores=raw_scores,
            csv_headers=csv_headers,
            consumption_preferences=consumption_preferences,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate query params
        query_string = responses.calls[0].request.url.split('?',1)[1]
        query_string = urllib.parse.unquote_plus(query_string)
        assert 'raw_scores={}'.format('true' if raw_scores else 'false') in query_string
        assert 'csv_headers={}'.format('true' if csv_headers else 'false') in query_string
        assert 'consumption_preferences={}'.format('true' if consumption_preferences else 'false') in query_string
        # Validate body params


    @responses.activate
    def test_profile_required_params(self):
        """
        test_profile_required_params()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/profile')
        mock_response = '{"processed_language": "ar", "word_count": 10, "word_count_message": "word_count_message", "personality": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "needs": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "values": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "behavior": [{"trait_id": "trait_id", "name": "name", "category": "category", "percentage": 10}], "consumption_preferences": [{"consumption_preference_category_id": "consumption_preference_category_id", "name": "name", "consumption_preferences": [{"consumption_preference_id": "consumption_preference_id", "name": "name", "score": 0.0}]}], "warnings": [{"warning_id": "WORD_COUNT_MESSAGE", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ContentItem model
        content_item_model = {}
        content_item_model['content'] = 'testString'
        content_item_model['id'] = 'testString'
        content_item_model['created'] = 26
        content_item_model['updated'] = 26
        content_item_model['contenttype'] = 'text/plain'
        content_item_model['language'] = 'en'
        content_item_model['parentid'] = 'testString'
        content_item_model['reply'] = False
        content_item_model['forward'] = False

        # Construct a dict representation of a Content model
        content_model = {}
        content_model['contentItems'] = [content_item_model]

        # Set up parameter values
        content = content_model
        accept = 'application/json'

        # Invoke method
        response = _service.profile(
            content,
            accept,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params


    @responses.activate
    def test_profile_value_error(self):
        """
        test_profile_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/profile')
        mock_response = '{"processed_language": "ar", "word_count": 10, "word_count_message": "word_count_message", "personality": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "needs": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "values": [{"trait_id": "trait_id", "name": "name", "category": "personality", "percentile": 10, "raw_score": 9, "significant": false}], "behavior": [{"trait_id": "trait_id", "name": "name", "category": "category", "percentage": 10}], "consumption_preferences": [{"consumption_preference_category_id": "consumption_preference_category_id", "name": "name", "consumption_preferences": [{"consumption_preference_id": "consumption_preference_id", "name": "name", "score": 0.0}]}], "warnings": [{"warning_id": "WORD_COUNT_MESSAGE", "message": "message"}]}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ContentItem model
        content_item_model = {}
        content_item_model['content'] = 'testString'
        content_item_model['id'] = 'testString'
        content_item_model['created'] = 26
        content_item_model['updated'] = 26
        content_item_model['contenttype'] = 'text/plain'
        content_item_model['language'] = 'en'
        content_item_model['parentid'] = 'testString'
        content_item_model['reply'] = False
        content_item_model['forward'] = False

        # Construct a dict representation of a Content model
        content_model = {}
        content_model['contentItems'] = [content_item_model]

        # Set up parameter values
        content = content_model
        accept = 'application/json'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "content": content,
            "accept": accept,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.profile(**req_copy)



# endregion
##############################################################################
# End of Service: Methods
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Behavior():
    """
    Test Class for Behavior
    """

    def test_behavior_serialization(self):
        """
        Test serialization/deserialization for Behavior
        """

        # Construct a json representation of a Behavior model
        behavior_model_json = {}
        behavior_model_json['trait_id'] = 'testString'
        behavior_model_json['name'] = 'testString'
        behavior_model_json['category'] = 'testString'
        behavior_model_json['percentage'] = 72.5

        # Construct a model instance of Behavior by calling from_dict on the json representation
        behavior_model = Behavior.from_dict(behavior_model_json)
        assert behavior_model != False

        # Construct a model instance of Behavior by calling from_dict on the json representation
        behavior_model_dict = Behavior.from_dict(behavior_model_json).__dict__
        behavior_model2 = Behavior(**behavior_model_dict)

        # Verify the model instances are equivalent
        assert behavior_model == behavior_model2

        # Convert model instance back to dict and verify no loss of data
        behavior_model_json2 = behavior_model.to_dict()
        assert behavior_model_json2 == behavior_model_json

class TestModel_ConsumptionPreferences():
    """
    Test Class for ConsumptionPreferences
    """

    def test_consumption_preferences_serialization(self):
        """
        Test serialization/deserialization for ConsumptionPreferences
        """

        # Construct a json representation of a ConsumptionPreferences model
        consumption_preferences_model_json = {}
        consumption_preferences_model_json['consumption_preference_id'] = 'testString'
        consumption_preferences_model_json['name'] = 'testString'
        consumption_preferences_model_json['score'] = 0.0

        # Construct a model instance of ConsumptionPreferences by calling from_dict on the json representation
        consumption_preferences_model = ConsumptionPreferences.from_dict(consumption_preferences_model_json)
        assert consumption_preferences_model != False

        # Construct a model instance of ConsumptionPreferences by calling from_dict on the json representation
        consumption_preferences_model_dict = ConsumptionPreferences.from_dict(consumption_preferences_model_json).__dict__
        consumption_preferences_model2 = ConsumptionPreferences(**consumption_preferences_model_dict)

        # Verify the model instances are equivalent
        assert consumption_preferences_model == consumption_preferences_model2

        # Convert model instance back to dict and verify no loss of data
        consumption_preferences_model_json2 = consumption_preferences_model.to_dict()
        assert consumption_preferences_model_json2 == consumption_preferences_model_json

class TestModel_ConsumptionPreferencesCategory():
    """
    Test Class for ConsumptionPreferencesCategory
    """

    def test_consumption_preferences_category_serialization(self):
        """
        Test serialization/deserialization for ConsumptionPreferencesCategory
        """

        # Construct dict forms of any model objects needed in order to build this model.

        consumption_preferences_model = {} # ConsumptionPreferences
        consumption_preferences_model['consumption_preference_id'] = 'testString'
        consumption_preferences_model['name'] = 'testString'
        consumption_preferences_model['score'] = 0.0

        # Construct a json representation of a ConsumptionPreferencesCategory model
        consumption_preferences_category_model_json = {}
        consumption_preferences_category_model_json['consumption_preference_category_id'] = 'testString'
        consumption_preferences_category_model_json['name'] = 'testString'
        consumption_preferences_category_model_json['consumption_preferences'] = [consumption_preferences_model]

        # Construct a model instance of ConsumptionPreferencesCategory by calling from_dict on the json representation
        consumption_preferences_category_model = ConsumptionPreferencesCategory.from_dict(consumption_preferences_category_model_json)
        assert consumption_preferences_category_model != False

        # Construct a model instance of ConsumptionPreferencesCategory by calling from_dict on the json representation
        consumption_preferences_category_model_dict = ConsumptionPreferencesCategory.from_dict(consumption_preferences_category_model_json).__dict__
        consumption_preferences_category_model2 = ConsumptionPreferencesCategory(**consumption_preferences_category_model_dict)

        # Verify the model instances are equivalent
        assert consumption_preferences_category_model == consumption_preferences_category_model2

        # Convert model instance back to dict and verify no loss of data
        consumption_preferences_category_model_json2 = consumption_preferences_category_model.to_dict()
        assert consumption_preferences_category_model_json2 == consumption_preferences_category_model_json

class TestModel_Content():
    """
    Test Class for Content
    """

    def test_content_serialization(self):
        """
        Test serialization/deserialization for Content
        """

        # Construct dict forms of any model objects needed in order to build this model.

        content_item_model = {} # ContentItem
        content_item_model['content'] = 'testString'
        content_item_model['id'] = 'testString'
        content_item_model['created'] = 26
        content_item_model['updated'] = 26
        content_item_model['contenttype'] = 'text/plain'
        content_item_model['language'] = 'en'
        content_item_model['parentid'] = 'testString'
        content_item_model['reply'] = False
        content_item_model['forward'] = False

        # Construct a json representation of a Content model
        content_model_json = {}
        content_model_json['contentItems'] = [content_item_model]

        # Construct a model instance of Content by calling from_dict on the json representation
        content_model = Content.from_dict(content_model_json)
        assert content_model != False

        # Construct a model instance of Content by calling from_dict on the json representation
        content_model_dict = Content.from_dict(content_model_json).__dict__
        content_model2 = Content(**content_model_dict)

        # Verify the model instances are equivalent
        assert content_model == content_model2

        # Convert model instance back to dict and verify no loss of data
        content_model_json2 = content_model.to_dict()
        assert content_model_json2 == content_model_json

class TestModel_ContentItem():
    """
    Test Class for ContentItem
    """

    def test_content_item_serialization(self):
        """
        Test serialization/deserialization for ContentItem
        """

        # Construct a json representation of a ContentItem model
        content_item_model_json = {}
        content_item_model_json['content'] = 'testString'
        content_item_model_json['id'] = 'testString'
        content_item_model_json['created'] = 26
        content_item_model_json['updated'] = 26
        content_item_model_json['contenttype'] = 'text/plain'
        content_item_model_json['language'] = 'en'
        content_item_model_json['parentid'] = 'testString'
        content_item_model_json['reply'] = False
        content_item_model_json['forward'] = False

        # Construct a model instance of ContentItem by calling from_dict on the json representation
        content_item_model = ContentItem.from_dict(content_item_model_json)
        assert content_item_model != False

        # Construct a model instance of ContentItem by calling from_dict on the json representation
        content_item_model_dict = ContentItem.from_dict(content_item_model_json).__dict__
        content_item_model2 = ContentItem(**content_item_model_dict)

        # Verify the model instances are equivalent
        assert content_item_model == content_item_model2

        # Convert model instance back to dict and verify no loss of data
        content_item_model_json2 = content_item_model.to_dict()
        assert content_item_model_json2 == content_item_model_json

class TestModel_Profile():
    """
    Test Class for Profile
    """

    def test_profile_serialization(self):
        """
        Test serialization/deserialization for Profile
        """

        # Construct dict forms of any model objects needed in order to build this model.

        trait_model = {} # Trait
        trait_model['trait_id'] = 'big5_openness'
        trait_model['name'] = 'Openness'
        trait_model['category'] = 'personality'
        trait_model['percentile'] = 0.8011555009553
        trait_model['raw_score'] = 0.77565404255038
        trait_model['significant'] = True

        behavior_model = {} # Behavior
        behavior_model['trait_id'] = 'behavior_sunday'
        behavior_model['name'] = 'Sunday'
        behavior_model['category'] = 'behavior'
        behavior_model['percentage'] = 0.21392532795156

        consumption_preferences_model = {} # ConsumptionPreferences
        consumption_preferences_model['consumption_preference_id'] = 'consumption_preferences_automobile_ownership_cost'
        consumption_preferences_model['name'] = 'Likely to be sensitive to ownership cost when buying automobiles'
        consumption_preferences_model['score'] = 0

        consumption_preferences_category_model = {} # ConsumptionPreferencesCategory
        consumption_preferences_category_model['consumption_preference_category_id'] = 'consumption_preferences_shopping'
        consumption_preferences_category_model['name'] = 'Purchasing Preferences'
        consumption_preferences_category_model['consumption_preferences'] = [consumption_preferences_model]

        warning_model = {} # Warning
        warning_model['warning_id'] = 'WORD_COUNT_MESSAGE'
        warning_model['message'] = 'testString'

        # Construct a json representation of a Profile model
        profile_model_json = {}
        profile_model_json['processed_language'] = 'ar'
        profile_model_json['word_count'] = 38
        profile_model_json['word_count_message'] = 'testString'
        profile_model_json['personality'] = [trait_model]
        profile_model_json['needs'] = [trait_model]
        profile_model_json['values'] = [trait_model]
        profile_model_json['behavior'] = [behavior_model]
        profile_model_json['consumption_preferences'] = [consumption_preferences_category_model]
        profile_model_json['warnings'] = [warning_model]

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model = Profile.from_dict(profile_model_json)
        assert profile_model != False

        # Construct a model instance of Profile by calling from_dict on the json representation
        profile_model_dict = Profile.from_dict(profile_model_json).__dict__
        profile_model2 = Profile(**profile_model_dict)

        # Verify the model instances are equivalent
        assert profile_model == profile_model2

        # Convert model instance back to dict and verify no loss of data
        profile_model_json2 = profile_model.to_dict()
        assert profile_model_json2 == profile_model_json

class TestModel_Trait():
    """
    Test Class for Trait
    """

    def test_trait_serialization(self):
        """
        Test serialization/deserialization for Trait
        """

        # Construct a json representation of a Trait model
        trait_model_json = {}
        trait_model_json['trait_id'] = 'testString'
        trait_model_json['name'] = 'testString'
        trait_model_json['category'] = 'personality'
        trait_model_json['percentile'] = 72.5
        trait_model_json['raw_score'] = 72.5
        trait_model_json['significant'] = True

        # Construct a model instance of Trait by calling from_dict on the json representation
        trait_model = Trait.from_dict(trait_model_json)
        assert trait_model != False

        # Construct a model instance of Trait by calling from_dict on the json representation
        trait_model_dict = Trait.from_dict(trait_model_json).__dict__
        trait_model2 = Trait(**trait_model_dict)

        # Verify the model instances are equivalent
        assert trait_model == trait_model2

        # Convert model instance back to dict and verify no loss of data
        trait_model_json2 = trait_model.to_dict()
        assert trait_model_json2 == trait_model_json

class TestModel_Warning():
    """
    Test Class for Warning
    """

    def test_warning_serialization(self):
        """
        Test serialization/deserialization for Warning
        """

        # Construct a json representation of a Warning model
        warning_model_json = {}
        warning_model_json['warning_id'] = 'WORD_COUNT_MESSAGE'
        warning_model_json['message'] = 'testString'

        # Construct a model instance of Warning by calling from_dict on the json representation
        warning_model = Warning.from_dict(warning_model_json)
        assert warning_model != False

        # Construct a model instance of Warning by calling from_dict on the json representation
        warning_model_dict = Warning.from_dict(warning_model_json).__dict__
        warning_model2 = Warning(**warning_model_dict)

        # Verify the model instances are equivalent
        assert warning_model == warning_model2

        # Convert model instance back to dict and verify no loss of data
        warning_model_json2 = warning_model.to_dict()
        assert warning_model_json2 == warning_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
