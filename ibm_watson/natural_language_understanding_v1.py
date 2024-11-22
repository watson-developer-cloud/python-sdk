# coding: utf-8

# (C) Copyright IBM Corp. 2017, 2024.
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

# IBM OpenAPI SDK Code Generator Version: 3.97.0-0e90eab1-20241120-170029
"""
Analyze various features of text content at scale. Provide text, raw HTML, or a public URL
and IBM Watson Natural Language Understanding will give you results for the features you
request. The service cleans HTML content before analysis by default, so the results can
ignore most advertisements and other unwanted content.
You can create [custom
models](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
with Watson Knowledge Studio to detect custom entities and relations in Natural Language
Understanding.

API Version: 1.0
See: https://cloud.ibm.com/docs/natural-language-understanding
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List, Optional
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class NaturalLanguageUnderstandingV1(BaseService):
    """The Natural Language Understanding V1 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.natural-language-understanding.watson.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'natural-language-understanding'

    def __init__(
        self,
        version: str,
        authenticator: Authenticator = None,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Natural Language Understanding service.

        :param str version: Release date of the API version you want to use.
               Specify dates in YYYY-MM-DD format. The current version is `2022-04-07`.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        if version is None:
            raise ValueError('version must be provided')

        if not authenticator:
            authenticator = get_authenticator_from_environment(service_name)
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)
        self.version = version
        self.configure_service(service_name)

    #########################
    # Analyze
    #########################

    def analyze(
        self,
        features: 'Features',
        *,
        text: Optional[str] = None,
        html: Optional[str] = None,
        url: Optional[str] = None,
        clean: Optional[bool] = None,
        xpath: Optional[str] = None,
        fallback_to_raw: Optional[bool] = None,
        return_analyzed_text: Optional[bool] = None,
        language: Optional[str] = None,
        limit_text_characters: Optional[int] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Analyze text.

        Analyzes text, HTML, or a public webpage for the following features:
        - Categories
        - Classifications
        - Concepts
        - Emotion
        - Entities
        - Keywords
        - Metadata
        - Relations
        - Semantic roles
        - Sentiment
        - Syntax
        If a language for the input text is not specified with the `language` parameter,
        the service [automatically detects the
        language](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-detectable-languages).

        :param Features features: Specific features to analyze the document for.
        :param str text: (optional) The plain text to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param str html: (optional) The HTML file to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param str url: (optional) The webpage to analyze. One of the `text`,
               `html`, or `url` parameters is required.
        :param bool clean: (optional) Set this to `false` to disable webpage
               cleaning. For more information about webpage cleaning, see [Analyzing
               webpages](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-analyzing-webpages).
        :param str xpath: (optional) An [XPath
               query](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-analyzing-webpages#xpath)
               to perform on `html` or `url` input. Results of the query will be appended
               to the cleaned webpage text before it is analyzed. To analyze only the
               results of the XPath query, set the `clean` parameter to `false`.
        :param bool fallback_to_raw: (optional) Whether to use raw HTML content if
               text cleaning fails.
        :param bool return_analyzed_text: (optional) Whether or not to return the
               analyzed text.
        :param str language: (optional) ISO 639-1 code that specifies the language
               of your text. This overrides automatic language detection. Language support
               differs depending on the features you include in your analysis. For more
               information, see [Language
               support](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-language-support).
        :param int limit_text_characters: (optional) Sets the maximum number of
               characters that are processed by the service.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalysisResults` object
        """

        if features is None:
            raise ValueError('features must be provided')
        features = convert_model(features)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='analyze',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'features': features,
            'text': text,
            'html': html,
            'url': url,
            'clean': clean,
            'xpath': xpath,
            'fallback_to_raw': fallback_to_raw,
            'return_analyzed_text': return_analyzed_text,
            'language': language,
            'limit_text_characters': limit_text_characters,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/analyze'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Manage models
    #########################

    def list_models(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List models.

        Lists Watson Knowledge Studio [custom entities and relations
        models](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
        that are deployed to your Natural Language Understanding service.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ListModelsResults` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_models',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete model.

        Deletes a custom model.

        :param str model_id: Model ID of the model to delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteModelResults` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Manage categories models
    #########################

    def create_categories_model(
        self,
        language: str,
        training_data: BinaryIO,
        *,
        training_data_content_type: Optional[str] = None,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create categories model.

        (Beta) Creates a custom categories model by uploading training data and associated
        metadata. The model begins the training and deploying process and is ready to use
        when the `status` is `available`.

        :param str language: The 2-letter language code of this model.
        :param BinaryIO training_data: Training data in JSON format. For more
               information, see [Categories training data
               requirements](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories##categories-training-data-requirements).
        :param str training_data_content_type: (optional) The content type of
               training_data.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CategoriesModel` object
        """

        if not language:
            raise ValueError('language must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_categories_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(('language', (None, language, 'text/plain')))
        form_data.append(('training_data',
                          (None, training_data, training_data_content_type or
                           'application/octet-stream')))
        if name:
            form_data.append(('name', (None, name, 'text/plain')))
        if user_metadata:
            form_data.append(('user_metadata', (None, json.dumps(user_metadata),
                                                'application/json')))
        if description:
            form_data.append(('description', (None, description, 'text/plain')))
        if model_version:
            form_data.append(
                ('model_version', (None, model_version, 'text/plain')))
        if workspace_id:
            form_data.append(
                ('workspace_id', (None, workspace_id, 'text/plain')))
        if version_description:
            form_data.append(('version_description', (None, version_description,
                                                      'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models/categories'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_categories_models(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List categories models.

        (Beta) Returns all custom categories models associated with this service instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CategoriesModelList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_categories_models',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models/categories'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_categories_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get categories model details.

        (Beta) Returns the status of the categories model with the given model ID.

        :param str model_id: ID of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CategoriesModel` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_categories_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/categories/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_categories_model(
        self,
        model_id: str,
        language: str,
        training_data: BinaryIO,
        *,
        training_data_content_type: Optional[str] = None,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update categories model.

        (Beta) Overwrites the training data associated with this custom categories model
        and retrains the model. The new model replaces the current deployment.

        :param str model_id: ID of the model.
        :param str language: The 2-letter language code of this model.
        :param BinaryIO training_data: Training data in JSON format. For more
               information, see [Categories training data
               requirements](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories##categories-training-data-requirements).
        :param str training_data_content_type: (optional) The content type of
               training_data.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CategoriesModel` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        if not language:
            raise ValueError('language must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_categories_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(('language', (None, language, 'text/plain')))
        form_data.append(('training_data',
                          (None, training_data, training_data_content_type or
                           'application/octet-stream')))
        if name:
            form_data.append(('name', (None, name, 'text/plain')))
        if user_metadata:
            form_data.append(('user_metadata', (None, json.dumps(user_metadata),
                                                'application/json')))
        if description:
            form_data.append(('description', (None, description, 'text/plain')))
        if model_version:
            form_data.append(
                ('model_version', (None, model_version, 'text/plain')))
        if workspace_id:
            form_data.append(
                ('workspace_id', (None, workspace_id, 'text/plain')))
        if version_description:
            form_data.append(('version_description', (None, version_description,
                                                      'text/plain')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/categories/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_categories_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete categories model.

        (Beta) Un-deploys the custom categories model with the given model ID and deletes
        all associated customer data, including any training data or binary artifacts.

        :param str model_id: ID of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteModelResults` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_categories_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/categories/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Manage classifications models
    #########################

    def create_classifications_model(
        self,
        language: str,
        training_data: BinaryIO,
        *,
        training_data_content_type: Optional[str] = None,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        training_parameters: Optional[
            'ClassificationsTrainingParameters'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create classifications model.

        Creates a custom classifications model by uploading training data and associated
        metadata. The model begins the training and deploying process and is ready to use
        when the `status` is `available`.

        :param str language: The 2-letter language code of this model.
        :param BinaryIO training_data: Training data in JSON format. For more
               information, see [Classifications training data
               requirements](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-classifications#classification-training-data-requirements).
        :param str training_data_content_type: (optional) The content type of
               training_data.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param ClassificationsTrainingParameters training_parameters: (optional)
               Optional classifications training parameters along with model train
               requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClassificationsModel` object
        """

        if not language:
            raise ValueError('language must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_classifications_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(('language', (None, language, 'text/plain')))
        form_data.append(('training_data',
                          (None, training_data, training_data_content_type or
                           'application/octet-stream')))
        if name:
            form_data.append(('name', (None, name, 'text/plain')))
        if user_metadata:
            form_data.append(('user_metadata', (None, json.dumps(user_metadata),
                                                'application/json')))
        if description:
            form_data.append(('description', (None, description, 'text/plain')))
        if model_version:
            form_data.append(
                ('model_version', (None, model_version, 'text/plain')))
        if workspace_id:
            form_data.append(
                ('workspace_id', (None, workspace_id, 'text/plain')))
        if version_description:
            form_data.append(('version_description', (None, version_description,
                                                      'text/plain')))
        if training_parameters:
            form_data.append(
                ('training_parameters', (None, json.dumps(training_parameters),
                                         'application/json')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models/classifications'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_classifications_models(
        self,
        **kwargs,
    ) -> DetailedResponse:
        """
        List classifications models.

        Returns all custom classifications models associated with this service instance.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClassificationsModelList` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_classifications_models',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/models/classifications'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_classifications_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get classifications model details.

        Returns the status of the classifications model with the given model ID.

        :param str model_id: ID of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClassificationsModel` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_classifications_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/classifications/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_classifications_model(
        self,
        model_id: str,
        language: str,
        training_data: BinaryIO,
        *,
        training_data_content_type: Optional[str] = None,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        training_parameters: Optional[
            'ClassificationsTrainingParameters'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update classifications model.

        Overwrites the training data associated with this custom classifications model and
        retrains the model. The new model replaces the current deployment.

        :param str model_id: ID of the model.
        :param str language: The 2-letter language code of this model.
        :param BinaryIO training_data: Training data in JSON format. For more
               information, see [Classifications training data
               requirements](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-classifications#classification-training-data-requirements).
        :param str training_data_content_type: (optional) The content type of
               training_data.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param ClassificationsTrainingParameters training_parameters: (optional)
               Optional classifications training parameters along with model train
               requests.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ClassificationsModel` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        if not language:
            raise ValueError('language must be provided')
        if training_data is None:
            raise ValueError('training_data must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_classifications_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        form_data = []
        form_data.append(('language', (None, language, 'text/plain')))
        form_data.append(('training_data',
                          (None, training_data, training_data_content_type or
                           'application/octet-stream')))
        if name:
            form_data.append(('name', (None, name, 'text/plain')))
        if user_metadata:
            form_data.append(('user_metadata', (None, json.dumps(user_metadata),
                                                'application/json')))
        if description:
            form_data.append(('description', (None, description, 'text/plain')))
        if model_version:
            form_data.append(
                ('model_version', (None, model_version, 'text/plain')))
        if workspace_id:
            form_data.append(
                ('workspace_id', (None, workspace_id, 'text/plain')))
        if version_description:
            form_data.append(('version_description', (None, version_description,
                                                      'text/plain')))
        if training_parameters:
            form_data.append(
                ('training_parameters', (None, json.dumps(training_parameters),
                                         'application/json')))

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/classifications/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='PUT',
            url=url,
            headers=headers,
            params=params,
            files=form_data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_classifications_model(
        self,
        model_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete classifications model.

        Un-deploys the custom classifications model with the given model ID and deletes
        all associated customer data, including any training data or binary artifacts.

        :param str model_id: ID of the model.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DeleteModelResults` object
        """

        if not model_id:
            raise ValueError('model_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_classifications_model',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['model_id']
        path_param_values = self.encode_path_vars(model_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/models/classifications/{model_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


class CreateCategoriesModelEnums:
    """
    Enums for create_categories_model parameters.
    """

    class TrainingDataContentType(str, Enum):
        """
        The content type of training_data.
        """

        JSON = 'json'
        APPLICATION_JSON = 'application/json'


class UpdateCategoriesModelEnums:
    """
    Enums for update_categories_model parameters.
    """

    class TrainingDataContentType(str, Enum):
        """
        The content type of training_data.
        """

        JSON = 'json'
        APPLICATION_JSON = 'application/json'


class CreateClassificationsModelEnums:
    """
    Enums for create_classifications_model parameters.
    """

    class TrainingDataContentType(str, Enum):
        """
        The content type of training_data.
        """

        JSON = 'json'
        APPLICATION_JSON = 'application/json'


class UpdateClassificationsModelEnums:
    """
    Enums for update_classifications_model parameters.
    """

    class TrainingDataContentType(str, Enum):
        """
        The content type of training_data.
        """

        JSON = 'json'
        APPLICATION_JSON = 'application/json'


##############################################################################
# Models
##############################################################################


class AnalysisResults:
    """
    Results of the analysis, organized by feature.

    :param str language: (optional) Language used to analyze the text.
    :param str analyzed_text: (optional) Text that was used in the analysis.
    :param str retrieved_url: (optional) URL of the webpage that was analyzed.
    :param AnalysisResultsUsage usage: (optional) API usage information for the
          request.
    :param List[ConceptsResult] concepts: (optional) The general concepts referenced
          or alluded to in the analyzed text.
    :param List[EntitiesResult] entities: (optional) The entities detected in the
          analyzed text.
    :param List[KeywordsResult] keywords: (optional) The keywords from the analyzed
          text.
    :param List[CategoriesResult] categories: (optional) The categories that the
          service assigned to the analyzed text.
    :param List[ClassificationsResult] classifications: (optional) The
          classifications assigned to the analyzed text.
    :param EmotionResult emotion: (optional) The anger, disgust, fear, joy, or
          sadness conveyed by the content.
    :param FeaturesResultsMetadata metadata: (optional) Webpage metadata, such as
          the author and the title of the page.
    :param List[RelationsResult] relations: (optional) The relationships between
          entities in the content.
    :param List[SemanticRolesResult] semantic_roles: (optional) Sentences parsed
          into `subject`, `action`, and `object` form.
    :param SentimentResult sentiment: (optional) The sentiment of the content.
    :param SyntaxResult syntax: (optional) Tokens and sentences returned from syntax
          analysis.
    """

    def __init__(
        self,
        *,
        language: Optional[str] = None,
        analyzed_text: Optional[str] = None,
        retrieved_url: Optional[str] = None,
        usage: Optional['AnalysisResultsUsage'] = None,
        concepts: Optional[List['ConceptsResult']] = None,
        entities: Optional[List['EntitiesResult']] = None,
        keywords: Optional[List['KeywordsResult']] = None,
        categories: Optional[List['CategoriesResult']] = None,
        classifications: Optional[List['ClassificationsResult']] = None,
        emotion: Optional['EmotionResult'] = None,
        metadata: Optional['FeaturesResultsMetadata'] = None,
        relations: Optional[List['RelationsResult']] = None,
        semantic_roles: Optional[List['SemanticRolesResult']] = None,
        sentiment: Optional['SentimentResult'] = None,
        syntax: Optional['SyntaxResult'] = None,
    ) -> None:
        """
        Initialize a AnalysisResults object.

        :param str language: (optional) Language used to analyze the text.
        :param str analyzed_text: (optional) Text that was used in the analysis.
        :param str retrieved_url: (optional) URL of the webpage that was analyzed.
        :param AnalysisResultsUsage usage: (optional) API usage information for the
               request.
        :param List[ConceptsResult] concepts: (optional) The general concepts
               referenced or alluded to in the analyzed text.
        :param List[EntitiesResult] entities: (optional) The entities detected in
               the analyzed text.
        :param List[KeywordsResult] keywords: (optional) The keywords from the
               analyzed text.
        :param List[CategoriesResult] categories: (optional) The categories that
               the service assigned to the analyzed text.
        :param List[ClassificationsResult] classifications: (optional) The
               classifications assigned to the analyzed text.
        :param EmotionResult emotion: (optional) The anger, disgust, fear, joy, or
               sadness conveyed by the content.
        :param FeaturesResultsMetadata metadata: (optional) Webpage metadata, such
               as the author and the title of the page.
        :param List[RelationsResult] relations: (optional) The relationships
               between entities in the content.
        :param List[SemanticRolesResult] semantic_roles: (optional) Sentences
               parsed into `subject`, `action`, and `object` form.
        :param SentimentResult sentiment: (optional) The sentiment of the content.
        :param SyntaxResult syntax: (optional) Tokens and sentences returned from
               syntax analysis.
        """
        self.language = language
        self.analyzed_text = analyzed_text
        self.retrieved_url = retrieved_url
        self.usage = usage
        self.concepts = concepts
        self.entities = entities
        self.keywords = keywords
        self.categories = categories
        self.classifications = classifications
        self.emotion = emotion
        self.metadata = metadata
        self.relations = relations
        self.semantic_roles = semantic_roles
        self.sentiment = sentiment
        self.syntax = syntax

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalysisResults':
        """Initialize a AnalysisResults object from a json dictionary."""
        args = {}
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        if (analyzed_text := _dict.get('analyzed_text')) is not None:
            args['analyzed_text'] = analyzed_text
        if (retrieved_url := _dict.get('retrieved_url')) is not None:
            args['retrieved_url'] = retrieved_url
        if (usage := _dict.get('usage')) is not None:
            args['usage'] = AnalysisResultsUsage.from_dict(usage)
        if (concepts := _dict.get('concepts')) is not None:
            args['concepts'] = [ConceptsResult.from_dict(v) for v in concepts]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [EntitiesResult.from_dict(v) for v in entities]
        if (keywords := _dict.get('keywords')) is not None:
            args['keywords'] = [KeywordsResult.from_dict(v) for v in keywords]
        if (categories := _dict.get('categories')) is not None:
            args['categories'] = [
                CategoriesResult.from_dict(v) for v in categories
            ]
        if (classifications := _dict.get('classifications')) is not None:
            args['classifications'] = [
                ClassificationsResult.from_dict(v) for v in classifications
            ]
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionResult.from_dict(emotion)
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = FeaturesResultsMetadata.from_dict(metadata)
        if (relations := _dict.get('relations')) is not None:
            args['relations'] = [
                RelationsResult.from_dict(v) for v in relations
            ]
        if (semantic_roles := _dict.get('semantic_roles')) is not None:
            args['semantic_roles'] = [
                SemanticRolesResult.from_dict(v) for v in semantic_roles
            ]
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = SentimentResult.from_dict(sentiment)
        if (syntax := _dict.get('syntax')) is not None:
            args['syntax'] = SyntaxResult.from_dict(syntax)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'analyzed_text') and self.analyzed_text is not None:
            _dict['analyzed_text'] = self.analyzed_text
        if hasattr(self, 'retrieved_url') and self.retrieved_url is not None:
            _dict['retrieved_url'] = self.retrieved_url
        if hasattr(self, 'usage') and self.usage is not None:
            if isinstance(self.usage, dict):
                _dict['usage'] = self.usage
            else:
                _dict['usage'] = self.usage.to_dict()
        if hasattr(self, 'concepts') and self.concepts is not None:
            concepts_list = []
            for v in self.concepts:
                if isinstance(v, dict):
                    concepts_list.append(v)
                else:
                    concepts_list.append(v.to_dict())
            _dict['concepts'] = concepts_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'keywords') and self.keywords is not None:
            keywords_list = []
            for v in self.keywords:
                if isinstance(v, dict):
                    keywords_list.append(v)
                else:
                    keywords_list.append(v.to_dict())
            _dict['keywords'] = keywords_list
        if hasattr(self, 'categories') and self.categories is not None:
            categories_list = []
            for v in self.categories:
                if isinstance(v, dict):
                    categories_list.append(v)
                else:
                    categories_list.append(v.to_dict())
            _dict['categories'] = categories_list
        if hasattr(self,
                   'classifications') and self.classifications is not None:
            classifications_list = []
            for v in self.classifications:
                if isinstance(v, dict):
                    classifications_list.append(v)
                else:
                    classifications_list.append(v.to_dict())
            _dict['classifications'] = classifications_list
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            if isinstance(self.metadata, dict):
                _dict['metadata'] = self.metadata
            else:
                _dict['metadata'] = self.metadata.to_dict()
        if hasattr(self, 'relations') and self.relations is not None:
            relations_list = []
            for v in self.relations:
                if isinstance(v, dict):
                    relations_list.append(v)
                else:
                    relations_list.append(v.to_dict())
            _dict['relations'] = relations_list
        if hasattr(self, 'semantic_roles') and self.semantic_roles is not None:
            semantic_roles_list = []
            for v in self.semantic_roles:
                if isinstance(v, dict):
                    semantic_roles_list.append(v)
                else:
                    semantic_roles_list.append(v.to_dict())
            _dict['semantic_roles'] = semantic_roles_list
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            if isinstance(self.sentiment, dict):
                _dict['sentiment'] = self.sentiment
            else:
                _dict['sentiment'] = self.sentiment.to_dict()
        if hasattr(self, 'syntax') and self.syntax is not None:
            if isinstance(self.syntax, dict):
                _dict['syntax'] = self.syntax
            else:
                _dict['syntax'] = self.syntax.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalysisResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalysisResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalysisResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalysisResultsUsage:
    """
    API usage information for the request.

    :param int features: (optional) Number of features used in the API call.
    :param int text_characters: (optional) Number of text characters processed.
    :param int text_units: (optional) Number of 10,000-character units processed.
    """

    def __init__(
        self,
        *,
        features: Optional[int] = None,
        text_characters: Optional[int] = None,
        text_units: Optional[int] = None,
    ) -> None:
        """
        Initialize a AnalysisResultsUsage object.

        :param int features: (optional) Number of features used in the API call.
        :param int text_characters: (optional) Number of text characters processed.
        :param int text_units: (optional) Number of 10,000-character units
               processed.
        """
        self.features = features
        self.text_characters = text_characters
        self.text_units = text_units

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalysisResultsUsage':
        """Initialize a AnalysisResultsUsage object from a json dictionary."""
        args = {}
        if (features := _dict.get('features')) is not None:
            args['features'] = features
        if (text_characters := _dict.get('text_characters')) is not None:
            args['text_characters'] = text_characters
        if (text_units := _dict.get('text_units')) is not None:
            args['text_units'] = text_units
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalysisResultsUsage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features
        if hasattr(self,
                   'text_characters') and self.text_characters is not None:
            _dict['text_characters'] = self.text_characters
        if hasattr(self, 'text_units') and self.text_units is not None:
            _dict['text_units'] = self.text_units
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalysisResultsUsage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalysisResultsUsage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalysisResultsUsage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Author:
    """
    The author of the analyzed content.

    :param str name: (optional) Name of the author.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
    ) -> None:
        """
        Initialize a Author object.

        :param str name: (optional) Name of the author.
        """
        self.name = name

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Author':
        """Initialize a Author object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Author object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Author object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Author') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Author') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesModel:
    """
    Categories model.

    :param str name: (optional) An optional name for the model.
    :param dict user_metadata: (optional) An optional map of metadata key-value
          pairs to store with this model.
    :param str language: The 2-letter language code of this model.
    :param str description: (optional) An optional description of the model.
    :param str model_version: (optional) An optional version string.
    :param str workspace_id: (optional) ID of the Watson Knowledge Studio workspace
          that deployed this model to Natural Language Understanding.
    :param str version_description: (optional) The description of the version.
    :param List[str] features: (optional) The service features that are supported by
          the custom model.
    :param str status: When the status is `available`, the model is ready to use.
    :param str model_id: Unique model ID.
    :param datetime created: dateTime indicating when the model was created.
    :param List[Notice] notices: (optional)
    :param datetime last_trained: (optional) dateTime of last successful model
          training.
    :param datetime last_deployed: (optional) dateTime of last successful model
          deployment.
    """

    def __init__(
        self,
        language: str,
        status: str,
        model_id: str,
        created: datetime,
        *,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        features: Optional[List[str]] = None,
        notices: Optional[List['Notice']] = None,
        last_trained: Optional[datetime] = None,
        last_deployed: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a CategoriesModel object.

        :param str language: The 2-letter language code of this model.
        :param str status: When the status is `available`, the model is ready to
               use.
        :param str model_id: Unique model ID.
        :param datetime created: dateTime indicating when the model was created.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param List[str] features: (optional) The service features that are
               supported by the custom model.
        :param List[Notice] notices: (optional)
        :param datetime last_trained: (optional) dateTime of last successful model
               training.
        :param datetime last_deployed: (optional) dateTime of last successful model
               deployment.
        """
        self.name = name
        self.user_metadata = user_metadata
        self.language = language
        self.description = description
        self.model_version = model_version
        self.workspace_id = workspace_id
        self.version_description = version_description
        self.features = features
        self.status = status
        self.model_id = model_id
        self.created = created
        self.notices = notices
        self.last_trained = last_trained
        self.last_deployed = last_deployed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesModel':
        """Initialize a CategoriesModel object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (user_metadata := _dict.get('user_metadata')) is not None:
            args['user_metadata'] = user_metadata
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in CategoriesModel JSON'
            )
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (model_version := _dict.get('model_version')) is not None:
            args['model_version'] = model_version
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (version_description :=
                _dict.get('version_description')) is not None:
            args['version_description'] = version_description
        if (features := _dict.get('features')) is not None:
            args['features'] = features
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in CategoriesModel JSON'
            )
        if (model_id := _dict.get('model_id')) is not None:
            args['model_id'] = model_id
        else:
            raise ValueError(
                'Required property \'model_id\' not present in CategoriesModel JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        else:
            raise ValueError(
                'Required property \'created\' not present in CategoriesModel JSON'
            )
        if (notices := _dict.get('notices')) is not None:
            args['notices'] = [Notice.from_dict(v) for v in notices]
        if (last_trained := _dict.get('last_trained')) is not None:
            args['last_trained'] = string_to_datetime(last_trained)
        if (last_deployed := _dict.get('last_deployed')) is not None:
            args['last_deployed'] = string_to_datetime(last_deployed)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'user_metadata') and self.user_metadata is not None:
            _dict['user_metadata'] = self.user_metadata
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(
                self,
                'version_description') and self.version_description is not None:
            _dict['version_description'] = self.version_description
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'notices') and self.notices is not None:
            notices_list = []
            for v in self.notices:
                if isinstance(v, dict):
                    notices_list.append(v)
                else:
                    notices_list.append(v.to_dict())
            _dict['notices'] = notices_list
        if hasattr(self, 'last_trained') and self.last_trained is not None:
            _dict['last_trained'] = datetime_to_string(self.last_trained)
        if hasattr(self, 'last_deployed') and self.last_deployed is not None:
            _dict['last_deployed'] = datetime_to_string(self.last_deployed)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        When the status is `available`, the model is ready to use.
        """

        STARTING = 'starting'
        TRAINING = 'training'
        DEPLOYING = 'deploying'
        AVAILABLE = 'available'
        ERROR = 'error'
        DELETED = 'deleted'


class CategoriesModelList:
    """
    List of categories models.

    :param List[CategoriesModel] models: (optional) The categories models.
    """

    def __init__(
        self,
        *,
        models: Optional[List['CategoriesModel']] = None,
    ) -> None:
        """
        Initialize a CategoriesModelList object.

        :param List[CategoriesModel] models: (optional) The categories models.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesModelList':
        """Initialize a CategoriesModelList object from a json dictionary."""
        args = {}
        if (models := _dict.get('models')) is not None:
            args['models'] = [CategoriesModel.from_dict(v) for v in models]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesModelList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            models_list = []
            for v in self.models:
                if isinstance(v, dict):
                    models_list.append(v)
                else:
                    models_list.append(v.to_dict())
            _dict['models'] = models_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesModelList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesModelList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesModelList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesOptions:
    """
    Returns a hierarchical taxonomy of the content. The top three categories are returned
    by default.
    Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Spanish.

    :param bool explanation: (optional) Set this to `true` to return explanations
          for each categorization. **This is available only for English categories.**.
    :param int limit: (optional) Maximum number of categories to return.
    :param str model: (optional) (Beta) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the standard categories model. **This is available only for
          English categories.**.
    """

    def __init__(
        self,
        *,
        explanation: Optional[bool] = None,
        limit: Optional[int] = None,
        model: Optional[str] = None,
    ) -> None:
        """
        Initialize a CategoriesOptions object.

        :param bool explanation: (optional) Set this to `true` to return
               explanations for each categorization. **This is available only for English
               categories.**.
        :param int limit: (optional) Maximum number of categories to return.
        :param str model: (optional) (Beta) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the standard categories model. **This is available only for
               English categories.**.
        """
        self.explanation = explanation
        self.limit = limit
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesOptions':
        """Initialize a CategoriesOptions object from a json dictionary."""
        args = {}
        if (explanation := _dict.get('explanation')) is not None:
            args['explanation'] = explanation
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (model := _dict.get('model')) is not None:
            args['model'] = model
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'explanation') and self.explanation is not None:
            _dict['explanation'] = self.explanation
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesRelevantText:
    """
    Relevant text that contributed to the categorization.

    :param str text: (optional) Text from the analyzed source that supports the
          categorization.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
    ) -> None:
        """
        Initialize a CategoriesRelevantText object.

        :param str text: (optional) Text from the analyzed source that supports the
               categorization.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesRelevantText':
        """Initialize a CategoriesRelevantText object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesRelevantText object from a json dictionary."""
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
        """Return a `str` version of this CategoriesRelevantText object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesRelevantText') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesRelevantText') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesResult:
    """
    A categorization of the analyzed text.

    :param str label: (optional) The path to the category through the multi-level
          taxonomy hierarchy. For more information about the categories, see [Categories
          hierarchy](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories#categories-hierarchy).
    :param float score: (optional) Confidence score for the category classification.
          Higher values indicate greater confidence.
    :param CategoriesResultExplanation explanation: (optional) Information that
          helps to explain what contributed to the categories result.
    """

    def __init__(
        self,
        *,
        label: Optional[str] = None,
        score: Optional[float] = None,
        explanation: Optional['CategoriesResultExplanation'] = None,
    ) -> None:
        """
        Initialize a CategoriesResult object.

        :param str label: (optional) The path to the category through the
               multi-level taxonomy hierarchy. For more information about the categories,
               see [Categories
               hierarchy](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-categories#categories-hierarchy).
        :param float score: (optional) Confidence score for the category
               classification. Higher values indicate greater confidence.
        :param CategoriesResultExplanation explanation: (optional) Information that
               helps to explain what contributed to the categories result.
        """
        self.label = label
        self.score = score
        self.explanation = explanation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesResult':
        """Initialize a CategoriesResult object from a json dictionary."""
        args = {}
        if (label := _dict.get('label')) is not None:
            args['label'] = label
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        if (explanation := _dict.get('explanation')) is not None:
            args['explanation'] = CategoriesResultExplanation.from_dict(
                explanation)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'explanation') and self.explanation is not None:
            if isinstance(self.explanation, dict):
                _dict['explanation'] = self.explanation
            else:
                _dict['explanation'] = self.explanation.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CategoriesResultExplanation:
    """
    Information that helps to explain what contributed to the categories result.

    :param List[CategoriesRelevantText] relevant_text: (optional) An array of
          relevant text from the source that contributed to the categorization. The sorted
          array begins with the phrase that contributed most significantly to the result,
          followed by phrases that were less and less impactful.
    """

    def __init__(
        self,
        *,
        relevant_text: Optional[List['CategoriesRelevantText']] = None,
    ) -> None:
        """
        Initialize a CategoriesResultExplanation object.

        :param List[CategoriesRelevantText] relevant_text: (optional) An array of
               relevant text from the source that contributed to the categorization. The
               sorted array begins with the phrase that contributed most significantly to
               the result, followed by phrases that were less and less impactful.
        """
        self.relevant_text = relevant_text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CategoriesResultExplanation':
        """Initialize a CategoriesResultExplanation object from a json dictionary."""
        args = {}
        if (relevant_text := _dict.get('relevant_text')) is not None:
            args['relevant_text'] = [
                CategoriesRelevantText.from_dict(v) for v in relevant_text
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CategoriesResultExplanation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'relevant_text') and self.relevant_text is not None:
            relevant_text_list = []
            for v in self.relevant_text:
                if isinstance(v, dict):
                    relevant_text_list.append(v)
                else:
                    relevant_text_list.append(v.to_dict())
            _dict['relevant_text'] = relevant_text_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CategoriesResultExplanation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CategoriesResultExplanation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CategoriesResultExplanation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassificationsModel:
    """
    Classifications model.

    :param str name: (optional) An optional name for the model.
    :param dict user_metadata: (optional) An optional map of metadata key-value
          pairs to store with this model.
    :param str language: The 2-letter language code of this model.
    :param str description: (optional) An optional description of the model.
    :param str model_version: (optional) An optional version string.
    :param str workspace_id: (optional) ID of the Watson Knowledge Studio workspace
          that deployed this model to Natural Language Understanding.
    :param str version_description: (optional) The description of the version.
    :param List[str] features: (optional) The service features that are supported by
          the custom model.
    :param str status: When the status is `available`, the model is ready to use.
    :param str model_id: Unique model ID.
    :param datetime created: dateTime indicating when the model was created.
    :param List[Notice] notices: (optional)
    :param datetime last_trained: (optional) dateTime of last successful model
          training.
    :param datetime last_deployed: (optional) dateTime of last successful model
          deployment.
    """

    def __init__(
        self,
        language: str,
        status: str,
        model_id: str,
        created: datetime,
        *,
        name: Optional[str] = None,
        user_metadata: Optional[dict] = None,
        description: Optional[str] = None,
        model_version: Optional[str] = None,
        workspace_id: Optional[str] = None,
        version_description: Optional[str] = None,
        features: Optional[List[str]] = None,
        notices: Optional[List['Notice']] = None,
        last_trained: Optional[datetime] = None,
        last_deployed: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a ClassificationsModel object.

        :param str language: The 2-letter language code of this model.
        :param str status: When the status is `available`, the model is ready to
               use.
        :param str model_id: Unique model ID.
        :param datetime created: dateTime indicating when the model was created.
        :param str name: (optional) An optional name for the model.
        :param dict user_metadata: (optional) An optional map of metadata key-value
               pairs to store with this model.
        :param str description: (optional) An optional description of the model.
        :param str model_version: (optional) An optional version string.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str version_description: (optional) The description of the version.
        :param List[str] features: (optional) The service features that are
               supported by the custom model.
        :param List[Notice] notices: (optional)
        :param datetime last_trained: (optional) dateTime of last successful model
               training.
        :param datetime last_deployed: (optional) dateTime of last successful model
               deployment.
        """
        self.name = name
        self.user_metadata = user_metadata
        self.language = language
        self.description = description
        self.model_version = model_version
        self.workspace_id = workspace_id
        self.version_description = version_description
        self.features = features
        self.status = status
        self.model_id = model_id
        self.created = created
        self.notices = notices
        self.last_trained = last_trained
        self.last_deployed = last_deployed

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationsModel':
        """Initialize a ClassificationsModel object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (user_metadata := _dict.get('user_metadata')) is not None:
            args['user_metadata'] = user_metadata
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in ClassificationsModel JSON'
            )
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (model_version := _dict.get('model_version')) is not None:
            args['model_version'] = model_version
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (version_description :=
                _dict.get('version_description')) is not None:
            args['version_description'] = version_description
        if (features := _dict.get('features')) is not None:
            args['features'] = features
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        else:
            raise ValueError(
                'Required property \'status\' not present in ClassificationsModel JSON'
            )
        if (model_id := _dict.get('model_id')) is not None:
            args['model_id'] = model_id
        else:
            raise ValueError(
                'Required property \'model_id\' not present in ClassificationsModel JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        else:
            raise ValueError(
                'Required property \'created\' not present in ClassificationsModel JSON'
            )
        if (notices := _dict.get('notices')) is not None:
            args['notices'] = [Notice.from_dict(v) for v in notices]
        if (last_trained := _dict.get('last_trained')) is not None:
            args['last_trained'] = string_to_datetime(last_trained)
        if (last_deployed := _dict.get('last_deployed')) is not None:
            args['last_deployed'] = string_to_datetime(last_deployed)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationsModel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'user_metadata') and self.user_metadata is not None:
            _dict['user_metadata'] = self.user_metadata
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(
                self,
                'version_description') and self.version_description is not None:
            _dict['version_description'] = self.version_description
        if hasattr(self, 'features') and self.features is not None:
            _dict['features'] = self.features
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'notices') and self.notices is not None:
            notices_list = []
            for v in self.notices:
                if isinstance(v, dict):
                    notices_list.append(v)
                else:
                    notices_list.append(v.to_dict())
            _dict['notices'] = notices_list
        if hasattr(self, 'last_trained') and self.last_trained is not None:
            _dict['last_trained'] = datetime_to_string(self.last_trained)
        if hasattr(self, 'last_deployed') and self.last_deployed is not None:
            _dict['last_deployed'] = datetime_to_string(self.last_deployed)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationsModel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationsModel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationsModel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        When the status is `available`, the model is ready to use.
        """

        STARTING = 'starting'
        TRAINING = 'training'
        DEPLOYING = 'deploying'
        AVAILABLE = 'available'
        ERROR = 'error'
        DELETED = 'deleted'


class ClassificationsModelList:
    """
    List of classifications models.

    :param List[ClassificationsModel] models: (optional) The classifications models.
    """

    def __init__(
        self,
        *,
        models: Optional[List['ClassificationsModel']] = None,
    ) -> None:
        """
        Initialize a ClassificationsModelList object.

        :param List[ClassificationsModel] models: (optional) The classifications
               models.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationsModelList':
        """Initialize a ClassificationsModelList object from a json dictionary."""
        args = {}
        if (models := _dict.get('models')) is not None:
            args['models'] = [ClassificationsModel.from_dict(v) for v in models]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationsModelList object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            models_list = []
            for v in self.models:
                if isinstance(v, dict):
                    models_list.append(v)
                else:
                    models_list.append(v.to_dict())
            _dict['models'] = models_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationsModelList object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationsModelList') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationsModelList') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassificationsOptions:
    """
    Returns text classifications for the content.

    :param str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID of the classifications model to be used.
          You can analyze tone by using a language-specific model ID. See [Tone analytics
          (Classifications)](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-tone_analytics)
          for more information.
    """

    def __init__(
        self,
        *,
        model: Optional[str] = None,
    ) -> None:
        """
        Initialize a ClassificationsOptions object.

        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID of the classifications model to be used.
               You can analyze tone by using a language-specific model ID. See [Tone
               analytics
               (Classifications)](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-tone_analytics)
               for more information.
        """
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationsOptions':
        """Initialize a ClassificationsOptions object from a json dictionary."""
        args = {}
        if (model := _dict.get('model')) is not None:
            args['model'] = model
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationsOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassificationsResult:
    """
    A classification of the analyzed text.

    :param str class_name: (optional) Classification assigned to the text.
    :param float confidence: (optional) Confidence score for the classification.
          Higher values indicate greater confidence.
    """

    def __init__(
        self,
        *,
        class_name: Optional[str] = None,
        confidence: Optional[float] = None,
    ) -> None:
        """
        Initialize a ClassificationsResult object.

        :param str class_name: (optional) Classification assigned to the text.
        :param float confidence: (optional) Confidence score for the
               classification. Higher values indicate greater confidence.
        """
        self.class_name = class_name
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationsResult':
        """Initialize a ClassificationsResult object from a json dictionary."""
        args = {}
        if (class_name := _dict.get('class_name')) is not None:
            args['class_name'] = class_name
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'class_name') and self.class_name is not None:
            _dict['class_name'] = self.class_name
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ClassificationsTrainingParameters:
    """
    Optional classifications training parameters along with model train requests.

    :param str model_type: (optional) Model type selector to train either a
          single_label or a multi_label classifier.
    """

    def __init__(
        self,
        *,
        model_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a ClassificationsTrainingParameters object.

        :param str model_type: (optional) Model type selector to train either a
               single_label or a multi_label classifier.
        """
        self.model_type = model_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ClassificationsTrainingParameters':
        """Initialize a ClassificationsTrainingParameters object from a json dictionary."""
        args = {}
        if (model_type := _dict.get('model_type')) is not None:
            args['model_type'] = model_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ClassificationsTrainingParameters object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model_type') and self.model_type is not None:
            _dict['model_type'] = self.model_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ClassificationsTrainingParameters object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ClassificationsTrainingParameters') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ClassificationsTrainingParameters') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ModelTypeEnum(str, Enum):
        """
        Model type selector to train either a single_label or a multi_label classifier.
        """

        SINGLE_LABEL = 'single_label'
        MULTI_LABEL = 'multi_label'


class ConceptsOptions:
    """
    Returns high-level concepts in the content. For example, a research paper about deep
    learning might return the concept, "Artificial Intelligence" although the term is not
    mentioned.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Spanish.

    :param int limit: (optional) Maximum number of concepts to return.
    """

    def __init__(
        self,
        *,
        limit: Optional[int] = None,
    ) -> None:
        """
        Initialize a ConceptsOptions object.

        :param int limit: (optional) Maximum number of concepts to return.
        """
        self.limit = limit

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConceptsOptions':
        """Initialize a ConceptsOptions object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConceptsOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConceptsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConceptsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ConceptsResult:
    """
    The general concepts referenced or alluded to in the analyzed text.

    :param str text: (optional) Name of the concept.
    :param float relevance: (optional) Relevance score between 0 and 1. Higher
          scores indicate greater relevance.
    :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
          resource.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        relevance: Optional[float] = None,
        dbpedia_resource: Optional[str] = None,
    ) -> None:
        """
        Initialize a ConceptsResult object.

        :param str text: (optional) Name of the concept.
        :param float relevance: (optional) Relevance score between 0 and 1. Higher
               scores indicate greater relevance.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
               resource.
        """
        self.text = text
        self.relevance = relevance
        self.dbpedia_resource = dbpedia_resource

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ConceptsResult':
        """Initialize a ConceptsResult object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (relevance := _dict.get('relevance')) is not None:
            args['relevance'] = relevance
        if (dbpedia_resource := _dict.get('dbpedia_resource')) is not None:
            args['dbpedia_resource'] = dbpedia_resource
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ConceptsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self,
                   'dbpedia_resource') and self.dbpedia_resource is not None:
            _dict['dbpedia_resource'] = self.dbpedia_resource
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ConceptsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ConceptsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ConceptsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DeleteModelResults:
    """
    Delete model results.

    :param str deleted: (optional) model_id of the deleted model.
    """

    def __init__(
        self,
        *,
        deleted: Optional[str] = None,
    ) -> None:
        """
        Initialize a DeleteModelResults object.

        :param str deleted: (optional) model_id of the deleted model.
        """
        self.deleted = deleted

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DeleteModelResults':
        """Initialize a DeleteModelResults object from a json dictionary."""
        args = {}
        if (deleted := _dict.get('deleted')) is not None:
            args['deleted'] = deleted
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DeleteModelResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deleted') and self.deleted is not None:
            _dict['deleted'] = self.deleted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DeleteModelResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DeleteModelResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DeleteModelResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DisambiguationResult:
    """
    Disambiguation information for the entity.

    :param str name: (optional) Common entity name.
    :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
          resource.
    :param List[str] subtype: (optional) Entity subtype information.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        dbpedia_resource: Optional[str] = None,
        subtype: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a DisambiguationResult object.

        :param str name: (optional) Common entity name.
        :param str dbpedia_resource: (optional) Link to the corresponding DBpedia
               resource.
        :param List[str] subtype: (optional) Entity subtype information.
        """
        self.name = name
        self.dbpedia_resource = dbpedia_resource
        self.subtype = subtype

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DisambiguationResult':
        """Initialize a DisambiguationResult object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (dbpedia_resource := _dict.get('dbpedia_resource')) is not None:
            args['dbpedia_resource'] = dbpedia_resource
        if (subtype := _dict.get('subtype')) is not None:
            args['subtype'] = subtype
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DisambiguationResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self,
                   'dbpedia_resource') and self.dbpedia_resource is not None:
            _dict['dbpedia_resource'] = self.dbpedia_resource
        if hasattr(self, 'subtype') and self.subtype is not None:
            _dict['subtype'] = self.subtype
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DisambiguationResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DisambiguationResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DisambiguationResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentEmotionResults:
    """
    Emotion results for the document as a whole.

    :param EmotionScores emotion: (optional) Emotion results for the document as a
          whole.
    """

    def __init__(
        self,
        *,
        emotion: Optional['EmotionScores'] = None,
    ) -> None:
        """
        Initialize a DocumentEmotionResults object.

        :param EmotionScores emotion: (optional) Emotion results for the document
               as a whole.
        """
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentEmotionResults':
        """Initialize a DocumentEmotionResults object from a json dictionary."""
        args = {}
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionScores.from_dict(emotion)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentEmotionResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentEmotionResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentEmotionResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentEmotionResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DocumentSentimentResults:
    """
    DocumentSentimentResults.

    :param str label: (optional) Indicates whether the sentiment is positive,
          neutral, or negative.
    :param float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(
        self,
        *,
        label: Optional[str] = None,
        score: Optional[float] = None,
    ) -> None:
        """
        Initialize a DocumentSentimentResults object.

        :param str label: (optional) Indicates whether the sentiment is positive,
               neutral, or negative.
        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.label = label
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DocumentSentimentResults':
        """Initialize a DocumentSentimentResults object from a json dictionary."""
        args = {}
        if (label := _dict.get('label')) is not None:
            args['label'] = label
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DocumentSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DocumentSentimentResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DocumentSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DocumentSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionOptions:
    """
    Detects anger, disgust, fear, joy, or sadness that is conveyed in the content or by
    the context around target phrases specified in the targets parameter. You can analyze
    emotion for detected entities with `entities.emotion` and for keywords with
    `keywords.emotion`.
    Supported languages: English.

    :param bool document: (optional) Set this to `false` to hide document-level
          emotion results.
    :param List[str] targets: (optional) Emotion results will be returned for each
          target string that is found in the document.
    """

    def __init__(
        self,
        *,
        document: Optional[bool] = None,
        targets: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a EmotionOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
               emotion results.
        :param List[str] targets: (optional) Emotion results will be returned for
               each target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionOptions':
        """Initialize a EmotionOptions object from a json dictionary."""
        args = {}
        if (document := _dict.get('document')) is not None:
            args['document'] = document
        if (targets := _dict.get('targets')) is not None:
            args['targets'] = targets
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EmotionOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionResult:
    """
    The detected anger, disgust, fear, joy, or sadness that is conveyed by the content.
    Emotion information can be returned for detected entities, keywords, or user-specified
    target phrases found in the text.

    :param DocumentEmotionResults document: (optional) Emotion results for the
          document as a whole.
    :param List[TargetedEmotionResults] targets: (optional) Emotion results for
          specified targets.
    """

    def __init__(
        self,
        *,
        document: Optional['DocumentEmotionResults'] = None,
        targets: Optional[List['TargetedEmotionResults']] = None,
    ) -> None:
        """
        Initialize a EmotionResult object.

        :param DocumentEmotionResults document: (optional) Emotion results for the
               document as a whole.
        :param List[TargetedEmotionResults] targets: (optional) Emotion results for
               specified targets.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionResult':
        """Initialize a EmotionResult object from a json dictionary."""
        args = {}
        if (document := _dict.get('document')) is not None:
            args['document'] = DocumentEmotionResults.from_dict(document)
        if (targets := _dict.get('targets')) is not None:
            args['targets'] = [
                TargetedEmotionResults.from_dict(v) for v in targets
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            if isinstance(self.document, dict):
                _dict['document'] = self.document
            else:
                _dict['document'] = self.document.to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            targets_list = []
            for v in self.targets:
                if isinstance(v, dict):
                    targets_list.append(v)
                else:
                    targets_list.append(v.to_dict())
            _dict['targets'] = targets_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EmotionResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EmotionScores:
    """
    EmotionScores.

    :param float anger: (optional) Anger score from 0 to 1. A higher score means
          that the text is more likely to convey anger.
    :param float disgust: (optional) Disgust score from 0 to 1. A higher score means
          that the text is more likely to convey disgust.
    :param float fear: (optional) Fear score from 0 to 1. A higher score means that
          the text is more likely to convey fear.
    :param float joy: (optional) Joy score from 0 to 1. A higher score means that
          the text is more likely to convey joy.
    :param float sadness: (optional) Sadness score from 0 to 1. A higher score means
          that the text is more likely to convey sadness.
    """

    def __init__(
        self,
        *,
        anger: Optional[float] = None,
        disgust: Optional[float] = None,
        fear: Optional[float] = None,
        joy: Optional[float] = None,
        sadness: Optional[float] = None,
    ) -> None:
        """
        Initialize a EmotionScores object.

        :param float anger: (optional) Anger score from 0 to 1. A higher score
               means that the text is more likely to convey anger.
        :param float disgust: (optional) Disgust score from 0 to 1. A higher score
               means that the text is more likely to convey disgust.
        :param float fear: (optional) Fear score from 0 to 1. A higher score means
               that the text is more likely to convey fear.
        :param float joy: (optional) Joy score from 0 to 1. A higher score means
               that the text is more likely to convey joy.
        :param float sadness: (optional) Sadness score from 0 to 1. A higher score
               means that the text is more likely to convey sadness.
        """
        self.anger = anger
        self.disgust = disgust
        self.fear = fear
        self.joy = joy
        self.sadness = sadness

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EmotionScores':
        """Initialize a EmotionScores object from a json dictionary."""
        args = {}
        if (anger := _dict.get('anger')) is not None:
            args['anger'] = anger
        if (disgust := _dict.get('disgust')) is not None:
            args['disgust'] = disgust
        if (fear := _dict.get('fear')) is not None:
            args['fear'] = fear
        if (joy := _dict.get('joy')) is not None:
            args['joy'] = joy
        if (sadness := _dict.get('sadness')) is not None:
            args['sadness'] = sadness
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EmotionScores object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'anger') and self.anger is not None:
            _dict['anger'] = self.anger
        if hasattr(self, 'disgust') and self.disgust is not None:
            _dict['disgust'] = self.disgust
        if hasattr(self, 'fear') and self.fear is not None:
            _dict['fear'] = self.fear
        if hasattr(self, 'joy') and self.joy is not None:
            _dict['joy'] = self.joy
        if hasattr(self, 'sadness') and self.sadness is not None:
            _dict['sadness'] = self.sadness
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EmotionScores object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EmotionScores') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EmotionScores') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesOptions:
    """
    Identifies people, cities, organizations, and other entities in the content. For more
    information, see [Entity types and
    subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-type-systems).
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are supported only through
    custom models.

    :param int limit: (optional) Maximum number of entities to return.
    :param bool mentions: (optional) Set this to `true` to return locations of
          entity mentions.
    :param str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the standard entity detection model.
    :param bool sentiment: (optional) Set this to `true` to return sentiment
          information for detected entities.
    :param bool emotion: (optional) Set this to `true` to analyze emotion for
          detected keywords.
    """

    def __init__(
        self,
        *,
        limit: Optional[int] = None,
        mentions: Optional[bool] = None,
        model: Optional[str] = None,
        sentiment: Optional[bool] = None,
        emotion: Optional[bool] = None,
    ) -> None:
        """
        Initialize a EntitiesOptions object.

        :param int limit: (optional) Maximum number of entities to return.
        :param bool mentions: (optional) Set this to `true` to return locations of
               entity mentions.
        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the standard entity detection model.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
               information for detected entities.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for
               detected keywords.
        """
        self.limit = limit
        self.mentions = mentions
        self.model = model
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntitiesOptions':
        """Initialize a EntitiesOptions object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (mentions := _dict.get('mentions')) is not None:
            args['mentions'] = mentions
        if (model := _dict.get('model')) is not None:
            args['model'] = model
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = sentiment
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = emotion
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = self.mentions
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntitiesOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntitiesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntitiesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntitiesResult:
    """
    The important people, places, geopolitical entities and other types of entities in
    your content.

    :param str type: (optional) Entity type.
    :param str text: (optional) The name of the entity.
    :param float relevance: (optional) Relevance score from 0 to 1. Higher values
          indicate greater relevance.
    :param float confidence: (optional) Confidence in the entity identification from
          0 to 1. Higher values indicate higher confidence. In standard entities requests,
          confidence is returned only for English text. All entities requests that use
          custom models return the confidence score.
    :param List[EntityMention] mentions: (optional) Entity mentions and locations.
    :param int count: (optional) How many times the entity was mentioned in the
          text.
    :param EmotionScores emotion: (optional) Emotion analysis results for the
          entity, enabled with the `emotion` option.
    :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results
          for the entity, enabled with the `sentiment` option.
    :param DisambiguationResult disambiguation: (optional) Disambiguation
          information for the entity.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        text: Optional[str] = None,
        relevance: Optional[float] = None,
        confidence: Optional[float] = None,
        mentions: Optional[List['EntityMention']] = None,
        count: Optional[int] = None,
        emotion: Optional['EmotionScores'] = None,
        sentiment: Optional['FeatureSentimentResults'] = None,
        disambiguation: Optional['DisambiguationResult'] = None,
    ) -> None:
        """
        Initialize a EntitiesResult object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The name of the entity.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher
               values indicate greater relevance.
        :param float confidence: (optional) Confidence in the entity identification
               from 0 to 1. Higher values indicate higher confidence. In standard entities
               requests, confidence is returned only for English text. All entities
               requests that use custom models return the confidence score.
        :param List[EntityMention] mentions: (optional) Entity mentions and
               locations.
        :param int count: (optional) How many times the entity was mentioned in the
               text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the
               entity, enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis
               results for the entity, enabled with the `sentiment` option.
        :param DisambiguationResult disambiguation: (optional) Disambiguation
               information for the entity.
        """
        self.type = type
        self.text = text
        self.relevance = relevance
        self.confidence = confidence
        self.mentions = mentions
        self.count = count
        self.emotion = emotion
        self.sentiment = sentiment
        self.disambiguation = disambiguation

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntitiesResult':
        """Initialize a EntitiesResult object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (relevance := _dict.get('relevance')) is not None:
            args['relevance'] = relevance
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        if (mentions := _dict.get('mentions')) is not None:
            args['mentions'] = [EntityMention.from_dict(v) for v in mentions]
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionScores.from_dict(emotion)
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = FeatureSentimentResults.from_dict(sentiment)
        if (disambiguation := _dict.get('disambiguation')) is not None:
            args['disambiguation'] = DisambiguationResult.from_dict(
                disambiguation)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntitiesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'mentions') and self.mentions is not None:
            mentions_list = []
            for v in self.mentions:
                if isinstance(v, dict):
                    mentions_list.append(v)
                else:
                    mentions_list.append(v.to_dict())
            _dict['mentions'] = mentions_list
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            if isinstance(self.sentiment, dict):
                _dict['sentiment'] = self.sentiment
            else:
                _dict['sentiment'] = self.sentiment.to_dict()
        if hasattr(self, 'disambiguation') and self.disambiguation is not None:
            if isinstance(self.disambiguation, dict):
                _dict['disambiguation'] = self.disambiguation
            else:
                _dict['disambiguation'] = self.disambiguation.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntitiesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntitiesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntitiesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMention:
    """
    EntityMention.

    :param str text: (optional) Entity mention text.
    :param List[int] location: (optional) Character offsets indicating the beginning
          and end of the mention in the analyzed text.
    :param float confidence: (optional) Confidence in the entity identification from
          0 to 1. Higher values indicate higher confidence. In standard entities requests,
          confidence is returned only for English text. All entities requests that use
          custom models return the confidence score.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        location: Optional[List[int]] = None,
        confidence: Optional[float] = None,
    ) -> None:
        """
        Initialize a EntityMention object.

        :param str text: (optional) Entity mention text.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the mention in the analyzed text.
        :param float confidence: (optional) Confidence in the entity identification
               from 0 to 1. Higher values indicate higher confidence. In standard entities
               requests, confidence is returned only for English text. All entities
               requests that use custom models return the confidence score.
        """
        self.text = text
        self.location = location
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityMention':
        """Initialize a EntityMention object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMention object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EntityMention object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntityMention') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityMention') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeatureSentimentResults:
    """
    FeatureSentimentResults.

    :param float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(
        self,
        *,
        score: Optional[float] = None,
    ) -> None:
        """
        Initialize a FeatureSentimentResults object.

        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeatureSentimentResults':
        """Initialize a FeatureSentimentResults object from a json dictionary."""
        args = {}
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeatureSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeatureSentimentResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FeatureSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeatureSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Features:
    """
    Analysis features and options.

    :param ClassificationsOptions classifications: (optional) Returns text
          classifications for the content.
    :param ConceptsOptions concepts: (optional) Returns high-level concepts in the
          content. For example, a research paper about deep learning might return the
          concept, "Artificial Intelligence" although the term is not mentioned.
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Spanish.
    :param EmotionOptions emotion: (optional) Detects anger, disgust, fear, joy, or
          sadness that is conveyed in the content or by the context around target phrases
          specified in the targets parameter. You can analyze emotion for detected
          entities with `entities.emotion` and for keywords with `keywords.emotion`.
          Supported languages: English.
    :param EntitiesOptions entities: (optional) Identifies people, cities,
          organizations, and other entities in the content. For more information, see
          [Entity types and
          subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-type-systems).
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are supported
          only through custom models.
    :param KeywordsOptions keywords: (optional) Returns important keywords in the
          content.
          Supported languages: English, French, German, Italian, Japanese, Korean,
          Portuguese, Russian, Spanish, Swedish.
    :param dict metadata: (optional) Returns information from the document,
          including author name, title, RSS/ATOM feeds, prominent page image, and
          publication date. Supports URL and HTML input types only.
    :param RelationsOptions relations: (optional) Recognizes when two entities are
          related and identifies the type of relation. For example, an `awardedTo`
          relation might connect the entities "Nobel Prize" and "Albert Einstein". For
          more information, see [Relation
          types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
          Supported languages: Arabic, English, German, Japanese, Korean, Spanish.
          Chinese, Dutch, French, Italian, and Portuguese custom models are also
          supported.
    :param SemanticRolesOptions semantic_roles: (optional) Parses sentences into
          subject, action, and object form.
          Supported languages: English, German, Japanese, Korean, Spanish.
    :param SentimentOptions sentiment: (optional) Analyzes the general sentiment of
          your content or the sentiment toward specific target phrases. You can analyze
          sentiment for detected entities with `entities.sentiment` and for keywords with
          `keywords.sentiment`.
           Supported languages: Arabic, English, French, German, Italian, Japanese,
          Korean, Portuguese, Russian, Spanish.
    :param CategoriesOptions categories: (optional) Returns a hierarchical taxonomy
          of the content. The top three categories are returned by default.
          Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
          Portuguese, Spanish.
    :param SyntaxOptions syntax: (optional) Returns tokens and sentences from the
          input text.
    """

    def __init__(
        self,
        *,
        classifications: Optional['ClassificationsOptions'] = None,
        concepts: Optional['ConceptsOptions'] = None,
        emotion: Optional['EmotionOptions'] = None,
        entities: Optional['EntitiesOptions'] = None,
        keywords: Optional['KeywordsOptions'] = None,
        metadata: Optional[dict] = None,
        relations: Optional['RelationsOptions'] = None,
        semantic_roles: Optional['SemanticRolesOptions'] = None,
        sentiment: Optional['SentimentOptions'] = None,
        categories: Optional['CategoriesOptions'] = None,
        syntax: Optional['SyntaxOptions'] = None,
    ) -> None:
        """
        Initialize a Features object.

        :param ClassificationsOptions classifications: (optional) Returns text
               classifications for the content.
        :param ConceptsOptions concepts: (optional) Returns high-level concepts in
               the content. For example, a research paper about deep learning might return
               the concept, "Artificial Intelligence" although the term is not mentioned.
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Spanish.
        :param EmotionOptions emotion: (optional) Detects anger, disgust, fear,
               joy, or sadness that is conveyed in the content or by the context around
               target phrases specified in the targets parameter. You can analyze emotion
               for detected entities with `entities.emotion` and for keywords with
               `keywords.emotion`.
               Supported languages: English.
        :param EntitiesOptions entities: (optional) Identifies people, cities,
               organizations, and other entities in the content. For more information, see
               [Entity types and
               subtypes](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-entity-type-systems).
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Russian, Spanish, Swedish. Arabic, Chinese, and Dutch are
               supported only through custom models.
        :param KeywordsOptions keywords: (optional) Returns important keywords in
               the content.
               Supported languages: English, French, German, Italian, Japanese, Korean,
               Portuguese, Russian, Spanish, Swedish.
        :param dict metadata: (optional) Returns information from the document,
               including author name, title, RSS/ATOM feeds, prominent page image, and
               publication date. Supports URL and HTML input types only.
        :param RelationsOptions relations: (optional) Recognizes when two entities
               are related and identifies the type of relation. For example, an
               `awardedTo` relation might connect the entities "Nobel Prize" and "Albert
               Einstein". For more information, see [Relation
               types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
               Supported languages: Arabic, English, German, Japanese, Korean, Spanish.
               Chinese, Dutch, French, Italian, and Portuguese custom models are also
               supported.
        :param SemanticRolesOptions semantic_roles: (optional) Parses sentences
               into subject, action, and object form.
               Supported languages: English, German, Japanese, Korean, Spanish.
        :param SentimentOptions sentiment: (optional) Analyzes the general
               sentiment of your content or the sentiment toward specific target phrases.
               You can analyze sentiment for detected entities with `entities.sentiment`
               and for keywords with `keywords.sentiment`.
                Supported languages: Arabic, English, French, German, Italian, Japanese,
               Korean, Portuguese, Russian, Spanish.
        :param CategoriesOptions categories: (optional) Returns a hierarchical
               taxonomy of the content. The top three categories are returned by default.
               Supported languages: Arabic, English, French, German, Italian, Japanese,
               Korean, Portuguese, Spanish.
        :param SyntaxOptions syntax: (optional) Returns tokens and sentences from
               the input text.
        """
        self.classifications = classifications
        self.concepts = concepts
        self.emotion = emotion
        self.entities = entities
        self.keywords = keywords
        self.metadata = metadata
        self.relations = relations
        self.semantic_roles = semantic_roles
        self.sentiment = sentiment
        self.categories = categories
        self.syntax = syntax

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Features':
        """Initialize a Features object from a json dictionary."""
        args = {}
        if (classifications := _dict.get('classifications')) is not None:
            args['classifications'] = ClassificationsOptions.from_dict(
                classifications)
        if (concepts := _dict.get('concepts')) is not None:
            args['concepts'] = ConceptsOptions.from_dict(concepts)
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionOptions.from_dict(emotion)
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = EntitiesOptions.from_dict(entities)
        if (keywords := _dict.get('keywords')) is not None:
            args['keywords'] = KeywordsOptions.from_dict(keywords)
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (relations := _dict.get('relations')) is not None:
            args['relations'] = RelationsOptions.from_dict(relations)
        if (semantic_roles := _dict.get('semantic_roles')) is not None:
            args['semantic_roles'] = SemanticRolesOptions.from_dict(
                semantic_roles)
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = SentimentOptions.from_dict(sentiment)
        if (categories := _dict.get('categories')) is not None:
            args['categories'] = CategoriesOptions.from_dict(categories)
        if (syntax := _dict.get('syntax')) is not None:
            args['syntax'] = SyntaxOptions.from_dict(syntax)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Features object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'classifications') and self.classifications is not None:
            if isinstance(self.classifications, dict):
                _dict['classifications'] = self.classifications
            else:
                _dict['classifications'] = self.classifications.to_dict()
        if hasattr(self, 'concepts') and self.concepts is not None:
            if isinstance(self.concepts, dict):
                _dict['concepts'] = self.concepts
            else:
                _dict['concepts'] = self.concepts.to_dict()
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        if hasattr(self, 'entities') and self.entities is not None:
            if isinstance(self.entities, dict):
                _dict['entities'] = self.entities
            else:
                _dict['entities'] = self.entities.to_dict()
        if hasattr(self, 'keywords') and self.keywords is not None:
            if isinstance(self.keywords, dict):
                _dict['keywords'] = self.keywords
            else:
                _dict['keywords'] = self.keywords.to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'relations') and self.relations is not None:
            if isinstance(self.relations, dict):
                _dict['relations'] = self.relations
            else:
                _dict['relations'] = self.relations.to_dict()
        if hasattr(self, 'semantic_roles') and self.semantic_roles is not None:
            if isinstance(self.semantic_roles, dict):
                _dict['semantic_roles'] = self.semantic_roles
            else:
                _dict['semantic_roles'] = self.semantic_roles.to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            if isinstance(self.sentiment, dict):
                _dict['sentiment'] = self.sentiment
            else:
                _dict['sentiment'] = self.sentiment.to_dict()
        if hasattr(self, 'categories') and self.categories is not None:
            if isinstance(self.categories, dict):
                _dict['categories'] = self.categories
            else:
                _dict['categories'] = self.categories.to_dict()
        if hasattr(self, 'syntax') and self.syntax is not None:
            if isinstance(self.syntax, dict):
                _dict['syntax'] = self.syntax
            else:
                _dict['syntax'] = self.syntax.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Features object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Features') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Features') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class FeaturesResultsMetadata:
    """
    Webpage metadata, such as the author and the title of the page.

    :param List[Author] authors: (optional) The authors of the document.
    :param str publication_date: (optional) The publication date in the format ISO
          8601.
    :param str title: (optional) The title of the document.
    :param str image: (optional) URL of a prominent image on the webpage.
    :param List[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
    """

    def __init__(
        self,
        *,
        authors: Optional[List['Author']] = None,
        publication_date: Optional[str] = None,
        title: Optional[str] = None,
        image: Optional[str] = None,
        feeds: Optional[List['Feed']] = None,
    ) -> None:
        """
        Initialize a FeaturesResultsMetadata object.

        :param List[Author] authors: (optional) The authors of the document.
        :param str publication_date: (optional) The publication date in the format
               ISO 8601.
        :param str title: (optional) The title of the document.
        :param str image: (optional) URL of a prominent image on the webpage.
        :param List[Feed] feeds: (optional) RSS/ATOM feeds found on the webpage.
        """
        self.authors = authors
        self.publication_date = publication_date
        self.title = title
        self.image = image
        self.feeds = feeds

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'FeaturesResultsMetadata':
        """Initialize a FeaturesResultsMetadata object from a json dictionary."""
        args = {}
        if (authors := _dict.get('authors')) is not None:
            args['authors'] = [Author.from_dict(v) for v in authors]
        if (publication_date := _dict.get('publication_date')) is not None:
            args['publication_date'] = publication_date
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (image := _dict.get('image')) is not None:
            args['image'] = image
        if (feeds := _dict.get('feeds')) is not None:
            args['feeds'] = [Feed.from_dict(v) for v in feeds]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a FeaturesResultsMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authors') and self.authors is not None:
            authors_list = []
            for v in self.authors:
                if isinstance(v, dict):
                    authors_list.append(v)
                else:
                    authors_list.append(v.to_dict())
            _dict['authors'] = authors_list
        if hasattr(self,
                   'publication_date') and self.publication_date is not None:
            _dict['publication_date'] = self.publication_date
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'image') and self.image is not None:
            _dict['image'] = self.image
        if hasattr(self, 'feeds') and self.feeds is not None:
            feeds_list = []
            for v in self.feeds:
                if isinstance(v, dict):
                    feeds_list.append(v)
                else:
                    feeds_list.append(v.to_dict())
            _dict['feeds'] = feeds_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this FeaturesResultsMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'FeaturesResultsMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'FeaturesResultsMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Feed:
    """
    RSS or ATOM feed found on the webpage.

    :param str link: (optional) URL of the RSS or ATOM feed.
    """

    def __init__(
        self,
        *,
        link: Optional[str] = None,
    ) -> None:
        """
        Initialize a Feed object.

        :param str link: (optional) URL of the RSS or ATOM feed.
        """
        self.link = link

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Feed':
        """Initialize a Feed object from a json dictionary."""
        args = {}
        if (link := _dict.get('link')) is not None:
            args['link'] = link
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Feed object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'link') and self.link is not None:
            _dict['link'] = self.link
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Feed object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Feed') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Feed') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsOptions:
    """
    Returns important keywords in the content.
    Supported languages: English, French, German, Italian, Japanese, Korean, Portuguese,
    Russian, Spanish, Swedish.

    :param int limit: (optional) Maximum number of keywords to return.
    :param bool sentiment: (optional) Set this to `true` to return sentiment
          information for detected keywords.
    :param bool emotion: (optional) Set this to `true` to analyze emotion for
          detected keywords.
    """

    def __init__(
        self,
        *,
        limit: Optional[int] = None,
        sentiment: Optional[bool] = None,
        emotion: Optional[bool] = None,
    ) -> None:
        """
        Initialize a KeywordsOptions object.

        :param int limit: (optional) Maximum number of keywords to return.
        :param bool sentiment: (optional) Set this to `true` to return sentiment
               information for detected keywords.
        :param bool emotion: (optional) Set this to `true` to analyze emotion for
               detected keywords.
        """
        self.limit = limit
        self.sentiment = sentiment
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeywordsOptions':
        """Initialize a KeywordsOptions object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = sentiment
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = emotion
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            _dict['sentiment'] = self.sentiment
        if hasattr(self, 'emotion') and self.emotion is not None:
            _dict['emotion'] = self.emotion
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeywordsOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'KeywordsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeywordsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class KeywordsResult:
    """
    The important keywords in the content, organized by relevance.

    :param int count: (optional) Number of times the keyword appears in the analyzed
          text.
    :param float relevance: (optional) Relevance score from 0 to 1. Higher values
          indicate greater relevance.
    :param str text: (optional) The keyword text.
    :param EmotionScores emotion: (optional) Emotion analysis results for the
          keyword, enabled with the `emotion` option.
    :param FeatureSentimentResults sentiment: (optional) Sentiment analysis results
          for the keyword, enabled with the `sentiment` option.
    """

    def __init__(
        self,
        *,
        count: Optional[int] = None,
        relevance: Optional[float] = None,
        text: Optional[str] = None,
        emotion: Optional['EmotionScores'] = None,
        sentiment: Optional['FeatureSentimentResults'] = None,
    ) -> None:
        """
        Initialize a KeywordsResult object.

        :param int count: (optional) Number of times the keyword appears in the
               analyzed text.
        :param float relevance: (optional) Relevance score from 0 to 1. Higher
               values indicate greater relevance.
        :param str text: (optional) The keyword text.
        :param EmotionScores emotion: (optional) Emotion analysis results for the
               keyword, enabled with the `emotion` option.
        :param FeatureSentimentResults sentiment: (optional) Sentiment analysis
               results for the keyword, enabled with the `sentiment` option.
        """
        self.count = count
        self.relevance = relevance
        self.text = text
        self.emotion = emotion
        self.sentiment = sentiment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'KeywordsResult':
        """Initialize a KeywordsResult object from a json dictionary."""
        args = {}
        if (count := _dict.get('count')) is not None:
            args['count'] = count
        if (relevance := _dict.get('relevance')) is not None:
            args['relevance'] = relevance
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionScores.from_dict(emotion)
        if (sentiment := _dict.get('sentiment')) is not None:
            args['sentiment'] = FeatureSentimentResults.from_dict(sentiment)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a KeywordsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'count') and self.count is not None:
            _dict['count'] = self.count
        if hasattr(self, 'relevance') and self.relevance is not None:
            _dict['relevance'] = self.relevance
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        if hasattr(self, 'sentiment') and self.sentiment is not None:
            if isinstance(self.sentiment, dict):
                _dict['sentiment'] = self.sentiment
            else:
                _dict['sentiment'] = self.sentiment.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this KeywordsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'KeywordsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'KeywordsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ListModelsResults:
    """
    Custom models that are available for entities and relations.

    :param List[Model] models: (optional) An array of available models.
    """

    def __init__(
        self,
        *,
        models: Optional[List['Model']] = None,
    ) -> None:
        """
        Initialize a ListModelsResults object.

        :param List[Model] models: (optional) An array of available models.
        """
        self.models = models

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ListModelsResults':
        """Initialize a ListModelsResults object from a json dictionary."""
        args = {}
        if (models := _dict.get('models')) is not None:
            args['models'] = [Model.from_dict(v) for v in models]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ListModelsResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'models') and self.models is not None:
            models_list = []
            for v in self.models:
                if isinstance(v, dict):
                    models_list.append(v)
                else:
                    models_list.append(v.to_dict())
            _dict['models'] = models_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ListModelsResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ListModelsResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ListModelsResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Model:
    """
    Model.

    :param str status: (optional) When the status is `available`, the model is ready
          to use.
    :param str model_id: (optional) Unique model ID.
    :param str language: (optional) ISO 639-1 code that indicates the language of
          the model.
    :param str description: (optional) Model description.
    :param str workspace_id: (optional) ID of the Watson Knowledge Studio workspace
          that deployed this model to Natural Language Understanding.
    :param str model_version: (optional) The model version, if it was manually
          provided in Watson Knowledge Studio.
    :param str version: (optional) Deprecated: Deprecated — use `model_version`.
    :param str version_description: (optional) The description of the version, if it
          was manually provided in Watson Knowledge Studio.
    :param datetime created: (optional) A dateTime indicating when the model was
          created.
    """

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        model_id: Optional[str] = None,
        language: Optional[str] = None,
        description: Optional[str] = None,
        workspace_id: Optional[str] = None,
        model_version: Optional[str] = None,
        version: Optional[str] = None,
        version_description: Optional[str] = None,
        created: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Model object.

        :param str status: (optional) When the status is `available`, the model is
               ready to use.
        :param str model_id: (optional) Unique model ID.
        :param str language: (optional) ISO 639-1 code that indicates the language
               of the model.
        :param str description: (optional) Model description.
        :param str workspace_id: (optional) ID of the Watson Knowledge Studio
               workspace that deployed this model to Natural Language Understanding.
        :param str model_version: (optional) The model version, if it was manually
               provided in Watson Knowledge Studio.
        :param str version: (optional) Deprecated: Deprecated — use
               `model_version`.
        :param str version_description: (optional) The description of the version,
               if it was manually provided in Watson Knowledge Studio.
        :param datetime created: (optional) A dateTime indicating when the model
               was created.
        """
        self.status = status
        self.model_id = model_id
        self.language = language
        self.description = description
        self.workspace_id = workspace_id
        self.model_version = model_version
        self.version = version
        self.version_description = version_description
        self.created = created

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Model':
        """Initialize a Model object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (model_id := _dict.get('model_id')) is not None:
            args['model_id'] = model_id
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (model_version := _dict.get('model_version')) is not None:
            args['model_version'] = model_version
        if (version := _dict.get('version')) is not None:
            args['version'] = version
        if (version_description :=
                _dict.get('version_description')) is not None:
            args['version_description'] = version_description
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Model object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'model_id') and self.model_id is not None:
            _dict['model_id'] = self.model_id
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'model_version') and self.model_version is not None:
            _dict['model_version'] = self.model_version
        if hasattr(self, 'version') and self.version is not None:
            _dict['version'] = self.version
        if hasattr(
                self,
                'version_description') and self.version_description is not None:
            _dict['version_description'] = self.version_description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Model object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Model') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Model') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        When the status is `available`, the model is ready to use.
        """

        STARTING = 'starting'
        TRAINING = 'training'
        DEPLOYING = 'deploying'
        AVAILABLE = 'available'
        ERROR = 'error'
        DELETED = 'deleted'


class Notice:
    """
    A list of messages describing model training issues when model status is `error`.

    :param str message: (optional) Describes deficiencies or inconsistencies in
          training data.
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a Notice object.

        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Notice':
        """Initialize a Notice object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Notice object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and getattr(self, 'message') is not None:
            _dict['message'] = getattr(self, 'message')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Notice object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Notice') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationArgument:
    """
    RelationArgument.

    :param List[RelationEntity] entities: (optional) An array of extracted entities.
    :param List[int] location: (optional) Character offsets indicating the beginning
          and end of the mention in the analyzed text.
    :param str text: (optional) Text that corresponds to the argument.
    """

    def __init__(
        self,
        *,
        entities: Optional[List['RelationEntity']] = None,
        location: Optional[List[int]] = None,
        text: Optional[str] = None,
    ) -> None:
        """
        Initialize a RelationArgument object.

        :param List[RelationEntity] entities: (optional) An array of extracted
               entities.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the mention in the analyzed text.
        :param str text: (optional) Text that corresponds to the argument.
        """
        self.entities = entities
        self.location = location
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationArgument':
        """Initialize a RelationArgument object from a json dictionary."""
        args = {}
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RelationEntity.from_dict(v) for v in entities]
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationArgument object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationArgument object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RelationArgument') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationArgument') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationEntity:
    """
    An entity that corresponds with an argument in a relation.

    :param str text: (optional) Text that corresponds to the entity.
    :param str type: (optional) Entity type.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a RelationEntity object.

        :param str text: (optional) Text that corresponds to the entity.
        :param str type: (optional) Entity type.
        """
        self.text = text
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationEntity':
        """Initialize a RelationEntity object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RelationEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsOptions:
    """
    Recognizes when two entities are related and identifies the type of relation. For
    example, an `awardedTo` relation might connect the entities "Nobel Prize" and "Albert
    Einstein". For more information, see [Relation
    types](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-relations).
    Supported languages: Arabic, English, German, Japanese, Korean, Spanish. Chinese,
    Dutch, French, Italian, and Portuguese custom models are also supported.

    :param str model: (optional) Enter a [custom
          model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
          ID to override the default model.
    """

    def __init__(
        self,
        *,
        model: Optional[str] = None,
    ) -> None:
        """
        Initialize a RelationsOptions object.

        :param str model: (optional) Enter a [custom
               model](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-customizing)
               ID to override the default model.
        """
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationsOptions':
        """Initialize a RelationsOptions object from a json dictionary."""
        args = {}
        if (model := _dict.get('model')) is not None:
            args['model'] = model
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'model') and self.model is not None:
            _dict['model'] = self.model
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationsOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RelationsOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationsOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RelationsResult:
    """
    The relations between entities found in the content.

    :param float score: (optional) Confidence score for the relation. Higher values
          indicate greater confidence.
    :param str sentence: (optional) The sentence that contains the relation.
    :param str type: (optional) The type of the relation.
    :param List[RelationArgument] arguments: (optional) Entity mentions that are
          involved in the relation.
    """

    def __init__(
        self,
        *,
        score: Optional[float] = None,
        sentence: Optional[str] = None,
        type: Optional[str] = None,
        arguments: Optional[List['RelationArgument']] = None,
    ) -> None:
        """
        Initialize a RelationsResult object.

        :param float score: (optional) Confidence score for the relation. Higher
               values indicate greater confidence.
        :param str sentence: (optional) The sentence that contains the relation.
        :param str type: (optional) The type of the relation.
        :param List[RelationArgument] arguments: (optional) Entity mentions that
               are involved in the relation.
        """
        self.score = score
        self.sentence = sentence
        self.type = type
        self.arguments = arguments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RelationsResult':
        """Initialize a RelationsResult object from a json dictionary."""
        args = {}
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        if (sentence := _dict.get('sentence')) is not None:
            args['sentence'] = sentence
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (arguments := _dict.get('arguments')) is not None:
            args['arguments'] = [
                RelationArgument.from_dict(v) for v in arguments
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RelationsResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        if hasattr(self, 'sentence') and self.sentence is not None:
            _dict['sentence'] = self.sentence
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'arguments') and self.arguments is not None:
            arguments_list = []
            for v in self.arguments:
                if isinstance(v, dict):
                    arguments_list.append(v)
                else:
                    arguments_list.append(v.to_dict())
            _dict['arguments'] = arguments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RelationsResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RelationsResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RelationsResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesEntity:
    """
    SemanticRolesEntity.

    :param str type: (optional) Entity type.
    :param str text: (optional) The entity text.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        text: Optional[str] = None,
    ) -> None:
        """
        Initialize a SemanticRolesEntity object.

        :param str type: (optional) Entity type.
        :param str text: (optional) The entity text.
        """
        self.type = type
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesEntity':
        """Initialize a SemanticRolesEntity object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesKeyword:
    """
    SemanticRolesKeyword.

    :param str text: (optional) The keyword text.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
    ) -> None:
        """
        Initialize a SemanticRolesKeyword object.

        :param str text: (optional) The keyword text.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesKeyword':
        """Initialize a SemanticRolesKeyword object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesKeyword object from a json dictionary."""
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
        """Return a `str` version of this SemanticRolesKeyword object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesKeyword') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesKeyword') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesOptions:
    """
    Parses sentences into subject, action, and object form.
    Supported languages: English, German, Japanese, Korean, Spanish.

    :param int limit: (optional) Maximum number of semantic_roles results to return.
    :param bool keywords: (optional) Set this to `true` to return keyword
          information for subjects and objects.
    :param bool entities: (optional) Set this to `true` to return entity information
          for subjects and objects.
    """

    def __init__(
        self,
        *,
        limit: Optional[int] = None,
        keywords: Optional[bool] = None,
        entities: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SemanticRolesOptions object.

        :param int limit: (optional) Maximum number of semantic_roles results to
               return.
        :param bool keywords: (optional) Set this to `true` to return keyword
               information for subjects and objects.
        :param bool entities: (optional) Set this to `true` to return entity
               information for subjects and objects.
        """
        self.limit = limit
        self.keywords = keywords
        self.entities = entities

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesOptions':
        """Initialize a SemanticRolesOptions object from a json dictionary."""
        args = {}
        if (limit := _dict.get('limit')) is not None:
            args['limit'] = limit
        if (keywords := _dict.get('keywords')) is not None:
            args['keywords'] = keywords
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = entities
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'limit') and self.limit is not None:
            _dict['limit'] = self.limit
        if hasattr(self, 'keywords') and self.keywords is not None:
            _dict['keywords'] = self.keywords
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = self.entities
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResult:
    """
    The object containing the actions and the objects the actions act upon.

    :param str sentence: (optional) Sentence from the source that contains the
          subject, action, and object.
    :param SemanticRolesResultSubject subject: (optional) The extracted subject from
          the sentence.
    :param SemanticRolesResultAction action: (optional) The extracted action from
          the sentence.
    :param SemanticRolesResultObject object: (optional) The extracted object from
          the sentence.
    """

    def __init__(
        self,
        *,
        sentence: Optional[str] = None,
        subject: Optional['SemanticRolesResultSubject'] = None,
        action: Optional['SemanticRolesResultAction'] = None,
        object: Optional['SemanticRolesResultObject'] = None,
    ) -> None:
        """
        Initialize a SemanticRolesResult object.

        :param str sentence: (optional) Sentence from the source that contains the
               subject, action, and object.
        :param SemanticRolesResultSubject subject: (optional) The extracted subject
               from the sentence.
        :param SemanticRolesResultAction action: (optional) The extracted action
               from the sentence.
        :param SemanticRolesResultObject object: (optional) The extracted object
               from the sentence.
        """
        self.sentence = sentence
        self.subject = subject
        self.action = action
        self.object = object

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResult':
        """Initialize a SemanticRolesResult object from a json dictionary."""
        args = {}
        if (sentence := _dict.get('sentence')) is not None:
            args['sentence'] = sentence
        if (subject := _dict.get('subject')) is not None:
            args['subject'] = SemanticRolesResultSubject.from_dict(subject)
        if (action := _dict.get('action')) is not None:
            args['action'] = SemanticRolesResultAction.from_dict(action)
        if (object := _dict.get('object')) is not None:
            args['object'] = SemanticRolesResultObject.from_dict(object)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sentence') and self.sentence is not None:
            _dict['sentence'] = self.sentence
        if hasattr(self, 'subject') and self.subject is not None:
            if isinstance(self.subject, dict):
                _dict['subject'] = self.subject
            else:
                _dict['subject'] = self.subject.to_dict()
        if hasattr(self, 'action') and self.action is not None:
            if isinstance(self.action, dict):
                _dict['action'] = self.action
            else:
                _dict['action'] = self.action.to_dict()
        if hasattr(self, 'object') and self.object is not None:
            if isinstance(self.object, dict):
                _dict['object'] = self.object
            else:
                _dict['object'] = self.object.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultAction:
    """
    The extracted action from the sentence.

    :param str text: (optional) Analyzed text that corresponds to the action.
    :param str normalized: (optional) normalized version of the action.
    :param SemanticRolesVerb verb: (optional)
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        normalized: Optional[str] = None,
        verb: Optional['SemanticRolesVerb'] = None,
    ) -> None:
        """
        Initialize a SemanticRolesResultAction object.

        :param str text: (optional) Analyzed text that corresponds to the action.
        :param str normalized: (optional) normalized version of the action.
        :param SemanticRolesVerb verb: (optional)
        """
        self.text = text
        self.normalized = normalized
        self.verb = verb

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultAction':
        """Initialize a SemanticRolesResultAction object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (normalized := _dict.get('normalized')) is not None:
            args['normalized'] = normalized
        if (verb := _dict.get('verb')) is not None:
            args['verb'] = SemanticRolesVerb.from_dict(verb)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'normalized') and self.normalized is not None:
            _dict['normalized'] = self.normalized
        if hasattr(self, 'verb') and self.verb is not None:
            if isinstance(self.verb, dict):
                _dict['verb'] = self.verb
            else:
                _dict['verb'] = self.verb.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultObject:
    """
    The extracted object from the sentence.

    :param str text: (optional) Object text.
    :param List[SemanticRolesKeyword] keywords: (optional) An array of extracted
          keywords.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        keywords: Optional[List['SemanticRolesKeyword']] = None,
    ) -> None:
        """
        Initialize a SemanticRolesResultObject object.

        :param str text: (optional) Object text.
        :param List[SemanticRolesKeyword] keywords: (optional) An array of
               extracted keywords.
        """
        self.text = text
        self.keywords = keywords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultObject':
        """Initialize a SemanticRolesResultObject object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (keywords := _dict.get('keywords')) is not None:
            args['keywords'] = [
                SemanticRolesKeyword.from_dict(v) for v in keywords
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultObject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'keywords') and self.keywords is not None:
            keywords_list = []
            for v in self.keywords:
                if isinstance(v, dict):
                    keywords_list.append(v)
                else:
                    keywords_list.append(v.to_dict())
            _dict['keywords'] = keywords_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultObject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultObject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultObject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesResultSubject:
    """
    The extracted subject from the sentence.

    :param str text: (optional) Text that corresponds to the subject role.
    :param List[SemanticRolesEntity] entities: (optional) An array of extracted
          entities.
    :param List[SemanticRolesKeyword] keywords: (optional) An array of extracted
          keywords.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        entities: Optional[List['SemanticRolesEntity']] = None,
        keywords: Optional[List['SemanticRolesKeyword']] = None,
    ) -> None:
        """
        Initialize a SemanticRolesResultSubject object.

        :param str text: (optional) Text that corresponds to the subject role.
        :param List[SemanticRolesEntity] entities: (optional) An array of extracted
               entities.
        :param List[SemanticRolesKeyword] keywords: (optional) An array of
               extracted keywords.
        """
        self.text = text
        self.entities = entities
        self.keywords = keywords

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesResultSubject':
        """Initialize a SemanticRolesResultSubject object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [
                SemanticRolesEntity.from_dict(v) for v in entities
            ]
        if (keywords := _dict.get('keywords')) is not None:
            args['keywords'] = [
                SemanticRolesKeyword.from_dict(v) for v in keywords
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesResultSubject object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'keywords') and self.keywords is not None:
            keywords_list = []
            for v in self.keywords:
                if isinstance(v, dict):
                    keywords_list.append(v)
                else:
                    keywords_list.append(v.to_dict())
            _dict['keywords'] = keywords_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesResultSubject object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesResultSubject') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesResultSubject') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SemanticRolesVerb:
    """
    SemanticRolesVerb.

    :param str text: (optional) The keyword text.
    :param str tense: (optional) Verb tense.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        tense: Optional[str] = None,
    ) -> None:
        """
        Initialize a SemanticRolesVerb object.

        :param str text: (optional) The keyword text.
        :param str tense: (optional) Verb tense.
        """
        self.text = text
        self.tense = tense

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SemanticRolesVerb':
        """Initialize a SemanticRolesVerb object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (tense := _dict.get('tense')) is not None:
            args['tense'] = tense
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SemanticRolesVerb object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'tense') and self.tense is not None:
            _dict['tense'] = self.tense
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SemanticRolesVerb object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SemanticRolesVerb') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SemanticRolesVerb') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentenceResult:
    """
    SentenceResult.

    :param str text: (optional) The sentence.
    :param List[int] location: (optional) Character offsets indicating the beginning
          and end of the sentence in the analyzed text.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        location: Optional[List[int]] = None,
    ) -> None:
        """
        Initialize a SentenceResult object.

        :param str text: (optional) The sentence.
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the sentence in the analyzed text.
        """
        self.text = text
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentenceResult':
        """Initialize a SentenceResult object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentenceResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentenceResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SentenceResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentenceResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentOptions:
    """
    Analyzes the general sentiment of your content or the sentiment toward specific target
    phrases. You can analyze sentiment for detected entities with `entities.sentiment` and
    for keywords with `keywords.sentiment`.
     Supported languages: Arabic, English, French, German, Italian, Japanese, Korean,
    Portuguese, Russian, Spanish.

    :param bool document: (optional) Set this to `false` to hide document-level
          sentiment results.
    :param List[str] targets: (optional) Sentiment results will be returned for each
          target string that is found in the document.
    """

    def __init__(
        self,
        *,
        document: Optional[bool] = None,
        targets: Optional[List[str]] = None,
    ) -> None:
        """
        Initialize a SentimentOptions object.

        :param bool document: (optional) Set this to `false` to hide document-level
               sentiment results.
        :param List[str] targets: (optional) Sentiment results will be returned for
               each target string that is found in the document.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentimentOptions':
        """Initialize a SentimentOptions object from a json dictionary."""
        args = {}
        if (document := _dict.get('document')) is not None:
            args['document'] = document
        if (targets := _dict.get('targets')) is not None:
            args['targets'] = targets
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            _dict['document'] = self.document
        if hasattr(self, 'targets') and self.targets is not None:
            _dict['targets'] = self.targets
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentimentOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SentimentOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentimentOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SentimentResult:
    """
    The sentiment of the content.

    :param DocumentSentimentResults document: (optional) The document level
          sentiment.
    :param List[TargetedSentimentResults] targets: (optional) The targeted sentiment
          to analyze.
    """

    def __init__(
        self,
        *,
        document: Optional['DocumentSentimentResults'] = None,
        targets: Optional[List['TargetedSentimentResults']] = None,
    ) -> None:
        """
        Initialize a SentimentResult object.

        :param DocumentSentimentResults document: (optional) The document level
               sentiment.
        :param List[TargetedSentimentResults] targets: (optional) The targeted
               sentiment to analyze.
        """
        self.document = document
        self.targets = targets

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SentimentResult':
        """Initialize a SentimentResult object from a json dictionary."""
        args = {}
        if (document := _dict.get('document')) is not None:
            args['document'] = DocumentSentimentResults.from_dict(document)
        if (targets := _dict.get('targets')) is not None:
            args['targets'] = [
                TargetedSentimentResults.from_dict(v) for v in targets
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SentimentResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'document') and self.document is not None:
            if isinstance(self.document, dict):
                _dict['document'] = self.document
            else:
                _dict['document'] = self.document.to_dict()
        if hasattr(self, 'targets') and self.targets is not None:
            targets_list = []
            for v in self.targets:
                if isinstance(v, dict):
                    targets_list.append(v)
                else:
                    targets_list.append(v.to_dict())
            _dict['targets'] = targets_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SentimentResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SentimentResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SentimentResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxOptions:
    """
    Returns tokens and sentences from the input text.

    :param SyntaxOptionsTokens tokens: (optional) Tokenization options.
    :param bool sentences: (optional) Set this to `true` to return sentence
          information.
    """

    def __init__(
        self,
        *,
        tokens: Optional['SyntaxOptionsTokens'] = None,
        sentences: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SyntaxOptions object.

        :param SyntaxOptionsTokens tokens: (optional) Tokenization options.
        :param bool sentences: (optional) Set this to `true` to return sentence
               information.
        """
        self.tokens = tokens
        self.sentences = sentences

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxOptions':
        """Initialize a SyntaxOptions object from a json dictionary."""
        args = {}
        if (tokens := _dict.get('tokens')) is not None:
            args['tokens'] = SyntaxOptionsTokens.from_dict(tokens)
        if (sentences := _dict.get('sentences')) is not None:
            args['sentences'] = sentences
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tokens') and self.tokens is not None:
            if isinstance(self.tokens, dict):
                _dict['tokens'] = self.tokens
            else:
                _dict['tokens'] = self.tokens.to_dict()
        if hasattr(self, 'sentences') and self.sentences is not None:
            _dict['sentences'] = self.sentences
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxOptionsTokens:
    """
    Tokenization options.

    :param bool lemma: (optional) Set this to `true` to return the lemma for each
          token.
    :param bool part_of_speech: (optional) Set this to `true` to return the part of
          speech for each token.
    """

    def __init__(
        self,
        *,
        lemma: Optional[bool] = None,
        part_of_speech: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SyntaxOptionsTokens object.

        :param bool lemma: (optional) Set this to `true` to return the lemma for
               each token.
        :param bool part_of_speech: (optional) Set this to `true` to return the
               part of speech for each token.
        """
        self.lemma = lemma
        self.part_of_speech = part_of_speech

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxOptionsTokens':
        """Initialize a SyntaxOptionsTokens object from a json dictionary."""
        args = {}
        if (lemma := _dict.get('lemma')) is not None:
            args['lemma'] = lemma
        if (part_of_speech := _dict.get('part_of_speech')) is not None:
            args['part_of_speech'] = part_of_speech
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxOptionsTokens object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'lemma') and self.lemma is not None:
            _dict['lemma'] = self.lemma
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxOptionsTokens object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxOptionsTokens') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxOptionsTokens') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SyntaxResult:
    """
    Tokens and sentences returned from syntax analysis.

    :param List[TokenResult] tokens: (optional)
    :param List[SentenceResult] sentences: (optional)
    """

    def __init__(
        self,
        *,
        tokens: Optional[List['TokenResult']] = None,
        sentences: Optional[List['SentenceResult']] = None,
    ) -> None:
        """
        Initialize a SyntaxResult object.

        :param List[TokenResult] tokens: (optional)
        :param List[SentenceResult] sentences: (optional)
        """
        self.tokens = tokens
        self.sentences = sentences

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SyntaxResult':
        """Initialize a SyntaxResult object from a json dictionary."""
        args = {}
        if (tokens := _dict.get('tokens')) is not None:
            args['tokens'] = [TokenResult.from_dict(v) for v in tokens]
        if (sentences := _dict.get('sentences')) is not None:
            args['sentences'] = [SentenceResult.from_dict(v) for v in sentences]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SyntaxResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tokens') and self.tokens is not None:
            tokens_list = []
            for v in self.tokens:
                if isinstance(v, dict):
                    tokens_list.append(v)
                else:
                    tokens_list.append(v.to_dict())
            _dict['tokens'] = tokens_list
        if hasattr(self, 'sentences') and self.sentences is not None:
            sentences_list = []
            for v in self.sentences:
                if isinstance(v, dict):
                    sentences_list.append(v)
                else:
                    sentences_list.append(v.to_dict())
            _dict['sentences'] = sentences_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SyntaxResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SyntaxResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SyntaxResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedEmotionResults:
    """
    Emotion results for a specified target.

    :param str text: (optional) Targeted text.
    :param EmotionScores emotion: (optional) The emotion results for the target.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        emotion: Optional['EmotionScores'] = None,
    ) -> None:
        """
        Initialize a TargetedEmotionResults object.

        :param str text: (optional) Targeted text.
        :param EmotionScores emotion: (optional) The emotion results for the
               target.
        """
        self.text = text
        self.emotion = emotion

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetedEmotionResults':
        """Initialize a TargetedEmotionResults object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (emotion := _dict.get('emotion')) is not None:
            args['emotion'] = EmotionScores.from_dict(emotion)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedEmotionResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'emotion') and self.emotion is not None:
            if isinstance(self.emotion, dict):
                _dict['emotion'] = self.emotion
            else:
                _dict['emotion'] = self.emotion.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetedEmotionResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetedEmotionResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetedEmotionResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TargetedSentimentResults:
    """
    TargetedSentimentResults.

    :param str text: (optional) Targeted text.
    :param float score: (optional) Sentiment score from -1 (negative) to 1
          (positive).
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        score: Optional[float] = None,
    ) -> None:
        """
        Initialize a TargetedSentimentResults object.

        :param str text: (optional) Targeted text.
        :param float score: (optional) Sentiment score from -1 (negative) to 1
               (positive).
        """
        self.text = text
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TargetedSentimentResults':
        """Initialize a TargetedSentimentResults object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TargetedSentimentResults object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TargetedSentimentResults object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TargetedSentimentResults') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TargetedSentimentResults') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TokenResult:
    """
    TokenResult.

    :param str text: (optional) The token as it appears in the analyzed text.
    :param str part_of_speech: (optional) The part of speech of the token. For more
          information about the values, see [Universal Dependencies POS
          tags](https://universaldependencies.org/u/pos/).
    :param List[int] location: (optional) Character offsets indicating the beginning
          and end of the token in the analyzed text.
    :param str lemma: (optional) The
          [lemma](https://wikipedia.org/wiki/Lemma_%28morphology%29) of the token.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        part_of_speech: Optional[str] = None,
        location: Optional[List[int]] = None,
        lemma: Optional[str] = None,
    ) -> None:
        """
        Initialize a TokenResult object.

        :param str text: (optional) The token as it appears in the analyzed text.
        :param str part_of_speech: (optional) The part of speech of the token. For
               more information about the values, see [Universal Dependencies POS
               tags](https://universaldependencies.org/u/pos/).
        :param List[int] location: (optional) Character offsets indicating the
               beginning and end of the token in the analyzed text.
        :param str lemma: (optional) The
               [lemma](https://wikipedia.org/wiki/Lemma_%28morphology%29) of the token.
        """
        self.text = text
        self.part_of_speech = part_of_speech
        self.location = location
        self.lemma = lemma

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TokenResult':
        """Initialize a TokenResult object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (part_of_speech := _dict.get('part_of_speech')) is not None:
            args['part_of_speech'] = part_of_speech
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (lemma := _dict.get('lemma')) is not None:
            args['lemma'] = lemma
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TokenResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'part_of_speech') and self.part_of_speech is not None:
            _dict['part_of_speech'] = self.part_of_speech
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'lemma') and self.lemma is not None:
            _dict['lemma'] = self.lemma
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TokenResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TokenResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TokenResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PartOfSpeechEnum(str, Enum):
        """
        The part of speech of the token. For more information about the values, see
        [Universal Dependencies POS tags](https://universaldependencies.org/u/pos/).
        """

        ADJ = 'ADJ'
        ADP = 'ADP'
        ADV = 'ADV'
        AUX = 'AUX'
        CCONJ = 'CCONJ'
        DET = 'DET'
        INTJ = 'INTJ'
        NOUN = 'NOUN'
        NUM = 'NUM'
        PART = 'PART'
        PRON = 'PRON'
        PROPN = 'PROPN'
        PUNCT = 'PUNCT'
        SCONJ = 'SCONJ'
        SYM = 'SYM'
        VERB = 'VERB'
        X = 'X'
