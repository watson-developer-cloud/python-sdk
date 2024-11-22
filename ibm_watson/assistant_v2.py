# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2024.
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
The IBM&reg; watsonx&trade; Assistant service combines machine learning, natural language
understanding, and an integrated dialog editor to create conversation flows between your
apps and your users.
The Assistant v2 API provides runtime methods your client application can use to send user
input to an assistant and receive a response.
You need a paid Plus plan or higher to use the watsonx Assistant v2 API.

API Version: 2.0
See: https://cloud.ibm.com/docs/assistant
"""

from datetime import datetime
from enum import Enum
from typing import BinaryIO, Dict, List, Optional
import json
import sys

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################


class AssistantV2(BaseService):
    """The Assistant V2 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.assistant.watson.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'assistant'

    def __init__(
        self,
        version: str,
        authenticator: Authenticator = None,
        service_name: str = DEFAULT_SERVICE_NAME,
    ) -> None:
        """
        Construct a new client for the Assistant service.

        :param str version: Release date of the API version you want to use.
               Specify dates in YYYY-MM-DD format. The current version is `2023-06-15`.

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
    # Conversational skill providers
    #########################

    def create_provider(
        self,
        provider_id: str,
        specification: 'ProviderSpecification',
        private: 'ProviderPrivate',
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a conversational skill provider.

        Create a new conversational skill provider.

        :param str provider_id: The unique identifier of the provider.
        :param ProviderSpecification specification: The specification of the
               provider.
        :param ProviderPrivate private: Private information of the provider.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderResponse` object
        """

        if provider_id is None:
            raise ValueError('provider_id must be provided')
        if specification is None:
            raise ValueError('specification must be provided')
        if private is None:
            raise ValueError('private must be provided')
        specification = convert_model(specification)
        private = convert_model(private)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_provider',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'provider_id': provider_id,
            'specification': specification,
            'private': private,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/providers'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_providers(
        self,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List conversational skill providers.

        List the conversational skill providers associated with a Watson Assistant service
        instance.

        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned conversational
               skill providers will be sorted. To reverse the sort order, prefix the value
               with a minus sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_providers',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/providers'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_provider(
        self,
        provider_id: str,
        specification: 'ProviderSpecification',
        private: 'ProviderPrivate',
        **kwargs,
    ) -> DetailedResponse:
        """
        Update a conversational skill provider.

        Update a new conversational skill provider.

        :param str provider_id: Unique identifier of the conversational skill
               provider.
        :param ProviderSpecification specification: The specification of the
               provider.
        :param ProviderPrivate private: Private information of the provider.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ProviderResponse` object
        """

        if not provider_id:
            raise ValueError('provider_id must be provided')
        if specification is None:
            raise ValueError('specification must be provided')
        if private is None:
            raise ValueError('private must be provided')
        specification = convert_model(specification)
        private = convert_model(private)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_provider',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'specification': specification,
            'private': private,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['provider_id']
        path_param_values = self.encode_path_vars(provider_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/providers/{provider_id}'.format(**path_param_dict)
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
    # Assistants
    #########################

    def create_assistant(
        self,
        *,
        language: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create an assistant.

        Create a new assistant.

        :param str language: (optional) The language of the assistant.
        :param str name: (optional) The name of the assistant. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the assistant. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AssistantData` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_assistant',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'language': language,
            'name': name,
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/assistants'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_assistants(
        self,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List assistants.

        List the assistants associated with a watsonx Assistant service instance.

        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned assistants will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AssistantCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_assistants',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/assistants'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_assistant(
        self,
        assistant_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete assistant.

        Delete an assistant.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_assistant',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Sessions
    #########################

    def create_session(
        self,
        assistant_id: str,
        *,
        analytics: Optional['RequestAnalytics'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create a session.

        Create a new session. A session is used to send user input to a skill and receive
        responses. It also maintains the state of the conversation. A session persists
        until it is deleted, or until it times out because of inactivity. (For more
        information, see the
        [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-assistant-settings).).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param RequestAnalytics analytics: (optional) An optional object containing
               analytics data. Currently, this data is used only for events sent to the
               Segment extension.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SessionResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if analytics is not None:
            analytics = convert_model(analytics)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_session',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'analytics': analytics,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/sessions'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_session(
        self,
        assistant_id: str,
        session_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete session.

        Deletes a session explicitly before it times out. (For more information about the
        session inactivity timeout, see the
        [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-assistant-settings)).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str session_id: Unique identifier of the session.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not session_id:
            raise ValueError('session_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_session',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'session_id']
        path_param_values = self.encode_path_vars(assistant_id, session_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/sessions/{session_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Message
    #########################

    def message(
        self,
        assistant_id: str,
        environment_id: str,
        session_id: str,
        *,
        input: Optional['MessageInput'] = None,
        context: Optional['MessageContext'] = None,
        user_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Send user input to assistant (stateful).

        Send user input to an assistant and receive a response, with conversation state
        (including context data) stored by watsonx Assistant for the duration of the
        session.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param str session_id: Unique identifier of the session.
        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to set or modify context variables,
               which can also be accessed by dialog nodes. The context is stored by the
               assistant on a per-session basis.
               **Note:** The total size of the context data stored for a stateful session
               cannot exceed 100KB.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context. If **user_id** is specified in both locations, the
               value specified at the root is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StatefulMessageResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        if not session_id:
            raise ValueError('session_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='message',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'input': input,
            'context': context,
            'user_id': user_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'environment_id', 'session_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id,
                                                  session_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/sessions/{session_id}/message'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def message_stateless(
        self,
        assistant_id: str,
        environment_id: str,
        *,
        input: Optional['StatelessMessageInput'] = None,
        context: Optional['StatelessMessageContext'] = None,
        user_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Send user input to assistant (stateless).

        Send user input to an assistant and receive a response, with conversation state
        (including context data) managed by your application.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param StatelessMessageInput input: (optional) An input object that
               includes the input text.
        :param StatelessMessageContext context: (optional) Context data for the
               conversation. You can use this property to set or modify context variables,
               which can also be accessed by dialog nodes. The context is not stored by
               the assistant. To maintain session state, include the context from the
               previous response.
               **Note:** The total size of the context data for a stateless session cannot
               exceed 250KB.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `StatelessMessageResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='message_stateless',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'input': input,
            'context': context,
            'user_id': user_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'environment_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/message'.format(**path_param_dict)
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
    # Message Stream
    #########################

    def message_stream(
        self,
        assistant_id: str,
        environment_id: str,
        session_id: str,
        *,
        input: Optional['MessageInput'] = None,
        context: Optional['MessageContext'] = None,
        user_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Send user input to assistant (stateful).

        Send user input to an assistant and receive a streamed response, with conversation
        state (including context data) stored by watsonx Assistant for the duration of the
        session.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param str session_id: Unique identifier of the session.
        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to set or modify context variables,
               which can also be accessed by dialog nodes. The context is stored by the
               assistant on a per-session basis.
               **Note:** The total size of the context data stored for a stateful session
               cannot exceed 100KB.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context. If **user_id** is specified in both locations, the
               value specified at the root is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        if not session_id:
            raise ValueError('session_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='message_stream',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'input': input,
            'context': context,
            'user_id': user_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'text/event-stream'

        path_param_keys = ['assistant_id', 'environment_id', 'session_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id,
                                                  session_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/environments/{environment_id}/sessions/{session_id}/message_stream'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def message_stream_stateless(
        self,
        assistant_id: str,
        environment_id: str,
        *,
        input: Optional['MessageInput'] = None,
        context: Optional['MessageContext'] = None,
        user_id: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Send user input to assistant (stateless).

        Send user input to an assistant and receive a response, with conversation state
        (including context data) managed by your application.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to set or modify context variables,
               which can also be accessed by dialog nodes. The context is stored by the
               assistant on a per-session basis.
               **Note:** The total size of the context data stored for a stateful session
               cannot exceed 100KB.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context. If **user_id** is specified in both locations, the
               value specified at the root is used.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `BinaryIO` result
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='message_stream_stateless',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'input': input,
            'context': context,
            'user_id': user_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'text/event-stream'

        path_param_keys = ['assistant_id', 'environment_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/environments/{environment_id}/message_stream'.format(
            **path_param_dict)
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
    # Bulk classify
    #########################

    def bulk_classify(
        self,
        skill_id: str,
        input: List['BulkClassifyUtterance'],
        **kwargs,
    ) -> DetailedResponse:
        """
        Identify intents and entities in multiple user utterances.

        Send multiple user inputs to a dialog skill in a single request and receive
        information about the intents and entities recognized in each input. This method
        is useful for testing and comparing the performance of different skills or skill
        versions.
        This method is available only with Enterprise with Data Isolation plans.

        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the watsonx Assistant user interface, open the skill settings and click
               **API Details**.
        :param List[BulkClassifyUtterance] input: An array of input utterances to
               classify.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BulkClassifyResponse` object
        """

        if not skill_id:
            raise ValueError('skill_id must be provided')
        if input is None:
            raise ValueError('input must be provided')
        input = [convert_model(x) for x in input]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='bulk_classify',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'input': input,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['skill_id']
        path_param_values = self.encode_path_vars(skill_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/skills/{skill_id}/workspace/bulk_classify'.format(
            **path_param_dict)
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
    # Logs
    #########################

    def list_logs(
        self,
        assistant_id: str,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        page_limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List log events for an assistant.

        List the events from the log of an assistant.
        This method requires Manager access.
        **Note:** If you use the **cursor** parameter to retrieve results one page at a
        time, subsequent requests must be no more than 5 minutes apart. Any returned value
        for the **cursor** parameter becomes invalid after 5 minutes. For more information
        about using pagination, see [Pagination](#pagination).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str sort: (optional) How to sort the returned log events. You can
               sort by **request_timestamp**. To reverse the sort order, prefix the
               parameter value with a minus sign (`-`).
        :param str filter: (optional) A cacheable parameter that limits the results
               to those matching the specified filter. For more information, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-filter-reference#filter-reference).
        :param int page_limit: (optional) The number of records to return in each
               page of results.
               **Note:** If the API is not returning your data, try lowering the
               page_limit value.
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogCollection` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_logs',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'sort': sort,
            'filter': filter,
            'page_limit': page_limit,
            'cursor': cursor,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/logs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(
        self,
        customer_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete labeled data.

        Deletes all data associated with a specified customer ID. The method has no effect
        if no data is associated with the customer ID.
        You associate a customer ID with data by passing the `X-Watson-Metadata` header
        with a request that passes data. For more information about personal data and
        customer IDs, see [Information
        security](https://cloud.ibm.com/docs/assistant?topic=assistant-information-security#information-security).
        **Note:** This operation is intended only for deleting data associated with a
        single specific customer, not for deleting data associated with multiple customers
        or for any other purpose. For more information, see [Labeling and deleting data in
        watsonx
        Assistant](https://cloud.ibm.com/docs/assistant?topic=assistant-information-security#information-security-gdpr-wa).

        :param str customer_id: The customer ID for which all data is to be
               deleted.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not customer_id:
            raise ValueError('customer_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_user_data',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'customer_id': customer_id,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v2/user_data'
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Environments
    #########################

    def list_environments(
        self,
        assistant_id: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List environments.

        List the environments associated with an assistant.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned environments
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EnvironmentCollection` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_environments',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/environments'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_environment(
        self,
        assistant_id: str,
        environment_id: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get environment.

        Get information about an environment. For more information about environments, see
        [Environments](https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-publish-overview#environments).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_environment',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'environment_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/environments/{environment_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_environment(
        self,
        assistant_id: str,
        environment_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        orchestration: Optional['UpdateEnvironmentOrchestration'] = None,
        session_timeout: Optional[int] = None,
        skill_references: Optional[List['EnvironmentSkill']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update environment.

        Update an environment with new or modified data. For more information about
        environments, see
        [Environments](https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-publish-overview#environments).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the watsonx Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param str name: (optional) The name of the environment.
        :param str description: (optional) The description of the environment.
        :param UpdateEnvironmentOrchestration orchestration: (optional) The search
               skill orchestration settings for the environment.
        :param int session_timeout: (optional) The session inactivity timeout
               setting for the environment (in seconds).
        :param List[EnvironmentSkill] skill_references: (optional) An array of
               objects identifying the skills (such as action and dialog) that exist in
               the environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not environment_id:
            raise ValueError('environment_id must be provided')
        if orchestration is not None:
            orchestration = convert_model(orchestration)
        if skill_references is not None:
            skill_references = [convert_model(x) for x in skill_references]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_environment',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'orchestration': orchestration,
            'session_timeout': session_timeout,
            'skill_references': skill_references,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'environment_id']
        path_param_values = self.encode_path_vars(assistant_id, environment_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/environments/{environment_id}'.format(
            **path_param_dict)
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
    # Releases
    #########################

    def create_release(
        self,
        assistant_id: str,
        *,
        description: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create release.

        Create a new release using the current content of the dialog and action skills in
        the draft environment. (In the watsonx Assistant user interface, a release is
        called a *version*.).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str description: (optional) The description of the release.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Release` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_release',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'description': description,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def list_releases(
        self,
        assistant_id: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List releases.

        List the releases associated with an assistant. (In the watsonx Assistant user
        interface, a release is called a *version*.).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned workspaces will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ReleaseCollection` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='list_releases',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'include_count': include_count,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def get_release(
        self,
        assistant_id: str,
        release: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get release.

        Get information about a release.
        Release data is not available until publishing of the release completes. If
        publishing is still in progress, you can continue to poll by calling the same
        request again and checking the value of the **status** property. When processing
        has completed, the request returns the release data.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str release: Unique identifier of the release.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Release` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not release:
            raise ValueError('release must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_release',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'release']
        path_param_values = self.encode_path_vars(assistant_id, release)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases/{release}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_release(
        self,
        assistant_id: str,
        release: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete release.

        Delete a release. (In the watsonx Assistant user interface, a release is called a
        *version*.).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str release: Unique identifier of the release.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not release:
            raise ValueError('release must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='delete_release',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'release']
        path_param_values = self.encode_path_vars(assistant_id, release)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases/{release}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def deploy_release(
        self,
        assistant_id: str,
        release: str,
        environment_id: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Deploy release.

        Update the environment with the content of the release. All snapshots saved as
        part of the release become active in the environment.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str release: Unique identifier of the release.
        :param str environment_id: The environment ID of the environment where the
               release is to be deployed.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Environment` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not release:
            raise ValueError('release must be provided')
        if environment_id is None:
            raise ValueError('environment_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='deploy_release',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'environment_id': environment_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'release']
        path_param_values = self.encode_path_vars(assistant_id, release)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases/{release}/deploy'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def create_release_export(
        self,
        assistant_id: str,
        release: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create release export.

        Initiate an asynchronous process which will create a downloadable Zip file
        artifact (/package) for an assistant release. This artifact will contain Action
        and/or Dialog skills that are part of the release. The Dialog skill will only be
        included in the event that coexistence is enabled on the assistant. The expected
        workflow with the use of Release Export endpoint is to first initiate the creation
        of the artifact with the POST endpoint and then poll the GET endpoint to retrieve
        the artifact. Once the artifact has been created, it will last for the duration
        (/scope) of the release.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str release: Unique identifier of the release.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateReleaseExportWithStatusErrors` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not release:
            raise ValueError('release must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_release_export',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'release']
        path_param_values = self.encode_path_vars(assistant_id, release)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases/{release}/export'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def download_release_export(
        self,
        assistant_id: str,
        release: str,
        *,
        accept: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get release export.

        A dual function endpoint to either retrieve the Zip file artifact that is
        associated with an assistant release or, retrieve the status of the artifact's
        creation. It is assumed that the artifact creation was already initiated prior to
        calling this endpoint. In the event that the artifact is not yet created and ready
        for download, this endpoint can be used to poll the system until the creation is
        completed or has failed. On the other hand, if the artifact is created, this
        endpoint will return the Zip file artifact as an octet stream. Once the artifact
        has been created, it will last for the duration (/scope) of the release. <br /><br
        /> When you will have downloaded the Zip file artifact, you have one of three ways
        to import it into an assistant's draft environment. These are as follows. <br
        /><ol><li>Import the zip package in Tooling via <var>"Assistant Settings" ->
        "Download/Upload files" -> "Upload" -> "Assistant only"</var>.</li><li>Import the
        zip package via "Create release import" endpoint using the APIs.</li><li>Extract
        the contents of the Zip file artifact and individually import the skill JSONs via
        skill update endpoints.</li></ol>.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str release: Unique identifier of the release.
        :param str accept: (optional) The type of the response: application/json or
               application/octet-stream.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateReleaseExportWithStatusErrors` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not release:
            raise ValueError('release must be provided')
        headers = {
            'Accept': accept,
        }
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='download_release_export',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['assistant_id', 'release']
        path_param_values = self.encode_path_vars(assistant_id, release)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/releases/{release}/export'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_release_import(
        self,
        assistant_id: str,
        body: BinaryIO,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create release import.

        Import a previously exported assistant release Zip file artifact (/package) into
        an assistant. This endpoint creates (/initiates) an asynchronous task (/job) in
        the background which will import the artifact contents into the draft environment
        of the assistant on which this endpoint is called. Specifically, the asynchronous
        operation will override the action and/or dialog skills in the assistant. It will
        be worth noting that when the artifact that is provided to this endpoint is from
        an assistant release which has coexistence enabled (i.e., it has both action and
        dialog skills), the import process will automatically enable coexistence, if not
        already enabled, on the assistant into which said artifact is being uploaded to.
        On the other hand, if the artifact package being imported only has action skill in
        it, the import asynchronous process will only override the draft environment's
        action skill, regardless of whether coexistence is enabled on the assistant into
        which the package is being imported. Lastly, the system will only run one
        asynchronous import at a time on an assistant. As such, consecutive imports will
        override previous import's updates to the skills in the draft environment. Once
        created, you may poll the completion of the import via the "Get release import
        Status" endpoint.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param BinaryIO body: Request body is an Octet-stream of the artifact Zip
               file that is being imported.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CreateAssistantReleaseImportResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if body is None:
            raise ValueError('body must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='create_release_import',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = body
        headers['content-type'] = 'application/octet-stream'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/import'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_release_import_status(
        self,
        assistant_id: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get release import Status.

        Monitor the status of an assistant release import. You may poll this endpoint
        until the status of the import has either succeeded or failed.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MonitorAssistantReleaseImportArtifactResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_release_import_status',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/import'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Skills
    #########################

    def get_skill(
        self,
        assistant_id: str,
        skill_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get skill.

        Get information about a skill.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the watsonx Assistant user interface, open the skill settings and click
               **API Details**.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Skill` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not skill_id:
            raise ValueError('skill_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='get_skill',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'skill_id']
        path_param_values = self.encode_path_vars(assistant_id, skill_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/skills/{skill_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_skill(
        self,
        assistant_id: str,
        skill_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        workspace: Optional[dict] = None,
        dialog_settings: Optional[dict] = None,
        search_settings: Optional['SearchSettings'] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update skill.

        Update a skill with new or modified data.
          **Note:** The update is performed asynchronously; you can see the status of the
        update by calling the **Get skill** method and checking the value of the
        **status** property.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the watsonx Assistant user interface, open the skill settings and click
               **API Details**.
        :param str name: (optional) The name of the skill. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the skill. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict workspace: (optional) An object containing the conversational
               content of an action or dialog skill.
        :param dict dialog_settings: (optional) For internal use only.
        :param SearchSettings search_settings: (optional) An object describing the
               search skill configuration.
               **Note:** Search settings are not supported in **Import skills** requests,
               and are not included in **Export skills** responses.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Skill` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not skill_id:
            raise ValueError('skill_id must be provided')
        if search_settings is not None:
            search_settings = convert_model(search_settings)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='update_skill',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'workspace': workspace,
            'dialog_settings': dialog_settings,
            'search_settings': search_settings,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id', 'skill_id']
        path_param_values = self.encode_path_vars(assistant_id, skill_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/skills/{skill_id}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def export_skills(
        self,
        assistant_id: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Export skills.

        Asynchronously export the action skill and dialog skill (if enabled) for the
        assistant. Use this method to save all skill data so that you can import it to a
        different assistant using the **Import skills** method.
         A successful call to this method only initiates an asynchronous export. The
        exported JSON data is not available until processing completes.
         After the initial request is submitted, you can poll the status of the operation
        by calling the same request again and checking the value of the **status**
        property. If an error occurs (indicated by a **status** value of `Failed`), the
        `status_description` property provides more information about the error, and the
        `status_errors` property contains an array of error messages that caused the
        failure.
         When processing has completed, the request returns the exported JSON data.
        Remember that the usual rate limits apply.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SkillsExport` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='export_skills',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/skills_export'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def import_skills(
        self,
        assistant_id: str,
        assistant_skills: List['SkillImport'],
        assistant_state: 'AssistantState',
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Import skills.

        Asynchronously import skills into an existing assistant from a previously exported
        file.
         The request body for this method should contain the response data that was
        received from a previous call to the **Export skills** method, without
        modification.
         A successful call to this method initiates an asynchronous import. The updated
        skills belonging to the assistant are not available until processing completes. To
        check the status of the asynchronous import operation, use the **Get status of
        skills import** method.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param List[SkillImport] assistant_skills: An array of objects describing
               the skills for the assistant. Included in responses only if
               **status**=`Available`.
        :param AssistantState assistant_state: Status information about the skills
               for the assistant. Included in responses only if **status**=`Available`.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SkillsAsyncRequestStatus` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if assistant_skills is None:
            raise ValueError('assistant_skills must be provided')
        if assistant_state is None:
            raise ValueError('assistant_state must be provided')
        assistant_skills = [convert_model(x) for x in assistant_skills]
        assistant_state = convert_model(assistant_state)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='import_skills',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'assistant_skills': assistant_skills,
            'assistant_state': assistant_state,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/skills_import'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def import_skills_status(
        self,
        assistant_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get status of skills import.

        Retrieve the status of an asynchronous import operation previously initiated by
        using the **Import skills** method.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the watsonx Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SkillsAsyncRequestStatus` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V2',
            operation_id='import_skills_status',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/skills_import/status'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


class ListProvidersEnums:
    """
    Enums for list_providers parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned conversational skill providers will be sorted. To
        reverse the sort order, prefix the value with a minus sign (`-`).
        """

        NAME = 'name'
        UPDATED = 'updated'


class ListAssistantsEnums:
    """
    Enums for list_assistants parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned assistants will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        NAME = 'name'
        UPDATED = 'updated'


class ListEnvironmentsEnums:
    """
    Enums for list_environments parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned environments will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        NAME = 'name'
        UPDATED = 'updated'


class ListReleasesEnums:
    """
    Enums for list_releases parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned workspaces will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        NAME = 'name'
        UPDATED = 'updated'


class DownloadReleaseExportEnums:
    """
    Enums for download_release_export parameters.
    """

    class Accept(str, Enum):
        """
        The type of the response: application/json or application/octet-stream.
        """

        APPLICATION_JSON = 'application/json'
        APPLICATION_OCTET_STREAM = 'application/octet-stream'


##############################################################################
# Models
##############################################################################


class AgentAvailabilityMessage:
    """
    AgentAvailabilityMessage.

    :param str message: (optional) The text of the message.
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a AgentAvailabilityMessage object.

        :param str message: (optional) The text of the message.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AgentAvailabilityMessage':
        """Initialize a AgentAvailabilityMessage object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AgentAvailabilityMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AgentAvailabilityMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AgentAvailabilityMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AgentAvailabilityMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssistantCollection:
    """
    AssistantCollection.

    :param List[AssistantData] assistants: An array of objects describing the
          assistants associated with the instance.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        assistants: List['AssistantData'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a AssistantCollection object.

        :param List[AssistantData] assistants: An array of objects describing the
               assistants associated with the instance.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.assistants = assistants
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssistantCollection':
        """Initialize a AssistantCollection object from a json dictionary."""
        args = {}
        if (assistants := _dict.get('assistants')) is not None:
            args['assistants'] = [
                AssistantData.from_dict(v) for v in assistants
            ]
        else:
            raise ValueError(
                'Required property \'assistants\' not present in AssistantCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in AssistantCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssistantCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assistants') and self.assistants is not None:
            assistants_list = []
            for v in self.assistants:
                if isinstance(v, dict):
                    assistants_list.append(v)
                else:
                    assistants_list.append(v.to_dict())
            _dict['assistants'] = assistants_list
        if hasattr(self, 'pagination') and self.pagination is not None:
            if isinstance(self.pagination, dict):
                _dict['pagination'] = self.pagination
            else:
                _dict['pagination'] = self.pagination.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssistantCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssistantCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssistantCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssistantData:
    """
    AssistantData.

    :param str assistant_id: (optional) The unique identifier of the assistant.
    :param str name: (optional) The name of the assistant. This string cannot
          contain carriage return, newline, or tab characters.
    :param str description: (optional) The description of the assistant. This string
          cannot contain carriage return, newline, or tab characters.
    :param str language: The language of the assistant.
    :param List[AssistantSkill] assistant_skills: (optional) An array of skill
          references identifying the skills associated with the assistant.
    :param List[EnvironmentReference] assistant_environments: (optional) An array of
          objects describing the environments defined for the assistant.
    """

    def __init__(
        self,
        language: str,
        *,
        assistant_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        assistant_skills: Optional[List['AssistantSkill']] = None,
        assistant_environments: Optional[List['EnvironmentReference']] = None,
    ) -> None:
        """
        Initialize a AssistantData object.

        :param str language: The language of the assistant.
        :param str name: (optional) The name of the assistant. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the assistant. This
               string cannot contain carriage return, newline, or tab characters.
        """
        self.assistant_id = assistant_id
        self.name = name
        self.description = description
        self.language = language
        self.assistant_skills = assistant_skills
        self.assistant_environments = assistant_environments

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssistantData':
        """Initialize a AssistantData object from a json dictionary."""
        args = {}
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in AssistantData JSON'
            )
        if (assistant_skills := _dict.get('assistant_skills')) is not None:
            args['assistant_skills'] = [
                AssistantSkill.from_dict(v) for v in assistant_skills
            ]
        if (assistant_environments :=
                _dict.get('assistant_environments')) is not None:
            args['assistant_environments'] = [
                EnvironmentReference.from_dict(v)
                for v in assistant_environments
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssistantData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'assistant_skills') and getattr(
                self, 'assistant_skills') is not None:
            assistant_skills_list = []
            for v in getattr(self, 'assistant_skills'):
                if isinstance(v, dict):
                    assistant_skills_list.append(v)
                else:
                    assistant_skills_list.append(v.to_dict())
            _dict['assistant_skills'] = assistant_skills_list
        if hasattr(self, 'assistant_environments') and getattr(
                self, 'assistant_environments') is not None:
            assistant_environments_list = []
            for v in getattr(self, 'assistant_environments'):
                if isinstance(v, dict):
                    assistant_environments_list.append(v)
                else:
                    assistant_environments_list.append(v.to_dict())
            _dict['assistant_environments'] = assistant_environments_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssistantData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssistantData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssistantData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AssistantSkill:
    """
    AssistantSkill.

    :param str skill_id: The skill ID of the skill.
    :param str type: (optional) The type of the skill.
    """

    def __init__(
        self,
        skill_id: str,
        *,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a AssistantSkill object.

        :param str skill_id: The skill ID of the skill.
        :param str type: (optional) The type of the skill.
        """
        self.skill_id = skill_id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssistantSkill':
        """Initialize a AssistantSkill object from a json dictionary."""
        args = {}
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in AssistantSkill JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssistantSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'skill_id') and self.skill_id is not None:
            _dict['skill_id'] = self.skill_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssistantSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssistantSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssistantSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the skill.
        """

        DIALOG = 'dialog'
        ACTION = 'action'
        SEARCH = 'search'


class AssistantState:
    """
    Status information about the skills for the assistant. Included in responses only if
    **status**=`Available`.

    :param bool action_disabled: Whether the action skill is disabled in the draft
          environment.
    :param bool dialog_disabled: Whether the dialog skill is disabled in the draft
          environment.
    """

    def __init__(
        self,
        action_disabled: bool,
        dialog_disabled: bool,
    ) -> None:
        """
        Initialize a AssistantState object.

        :param bool action_disabled: Whether the action skill is disabled in the
               draft environment.
        :param bool dialog_disabled: Whether the dialog skill is disabled in the
               draft environment.
        """
        self.action_disabled = action_disabled
        self.dialog_disabled = dialog_disabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AssistantState':
        """Initialize a AssistantState object from a json dictionary."""
        args = {}
        if (action_disabled := _dict.get('action_disabled')) is not None:
            args['action_disabled'] = action_disabled
        else:
            raise ValueError(
                'Required property \'action_disabled\' not present in AssistantState JSON'
            )
        if (dialog_disabled := _dict.get('dialog_disabled')) is not None:
            args['dialog_disabled'] = dialog_disabled
        else:
            raise ValueError(
                'Required property \'dialog_disabled\' not present in AssistantState JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AssistantState object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'action_disabled') and self.action_disabled is not None:
            _dict['action_disabled'] = self.action_disabled
        if hasattr(self,
                   'dialog_disabled') and self.dialog_disabled is not None:
            _dict['dialog_disabled'] = self.dialog_disabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AssistantState object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AssistantState') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AssistantState') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BaseEnvironmentOrchestration:
    """
    The search skill orchestration settings for the environment.

    :param bool search_skill_fallback: (optional) Whether to fall back to a search
          skill when responding to messages that do not match any intent or action defined
          in dialog or action skills. (If no search skill is configured for the
          environment, this property is ignored.).
    """

    def __init__(
        self,
        *,
        search_skill_fallback: Optional[bool] = None,
    ) -> None:
        """
        Initialize a BaseEnvironmentOrchestration object.

        :param bool search_skill_fallback: (optional) Whether to fall back to a
               search skill when responding to messages that do not match any intent or
               action defined in dialog or action skills. (If no search skill is
               configured for the environment, this property is ignored.).
        """
        self.search_skill_fallback = search_skill_fallback

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BaseEnvironmentOrchestration':
        """Initialize a BaseEnvironmentOrchestration object from a json dictionary."""
        args = {}
        if (search_skill_fallback :=
                _dict.get('search_skill_fallback')) is not None:
            args['search_skill_fallback'] = search_skill_fallback
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BaseEnvironmentOrchestration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'search_skill_fallback'
                  ) and self.search_skill_fallback is not None:
            _dict['search_skill_fallback'] = self.search_skill_fallback
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BaseEnvironmentOrchestration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BaseEnvironmentOrchestration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BaseEnvironmentOrchestration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BaseEnvironmentReleaseReference:
    """
    An object describing the release that is currently deployed in the environment.

    :param str release: (optional) The name of the deployed release.
    """

    def __init__(
        self,
        *,
        release: Optional[str] = None,
    ) -> None:
        """
        Initialize a BaseEnvironmentReleaseReference object.

        :param str release: (optional) The name of the deployed release.
        """
        self.release = release

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BaseEnvironmentReleaseReference':
        """Initialize a BaseEnvironmentReleaseReference object from a json dictionary."""
        args = {}
        if (release := _dict.get('release')) is not None:
            args['release'] = release
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BaseEnvironmentReleaseReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'release') and self.release is not None:
            _dict['release'] = self.release
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BaseEnvironmentReleaseReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BaseEnvironmentReleaseReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BaseEnvironmentReleaseReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BulkClassifyOutput:
    """
    BulkClassifyOutput.

    :param BulkClassifyUtterance input: (optional) The user input utterance to
          classify.
    :param List[RuntimeEntity] entities: (optional) An array of entities identified
          in the utterance.
    :param List[RuntimeIntent] intents: (optional) An array of intents recognized in
          the utterance.
    """

    def __init__(
        self,
        *,
        input: Optional['BulkClassifyUtterance'] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        intents: Optional[List['RuntimeIntent']] = None,
    ) -> None:
        """
        Initialize a BulkClassifyOutput object.

        :param BulkClassifyUtterance input: (optional) The user input utterance to
               classify.
        :param List[RuntimeEntity] entities: (optional) An array of entities
               identified in the utterance.
        :param List[RuntimeIntent] intents: (optional) An array of intents
               recognized in the utterance.
        """
        self.input = input
        self.entities = entities
        self.intents = intents

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkClassifyOutput':
        """Initialize a BulkClassifyOutput object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = BulkClassifyUtterance.from_dict(input)
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkClassifyOutput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkClassifyOutput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkClassifyOutput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkClassifyOutput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BulkClassifyResponse:
    """
    BulkClassifyResponse.

    :param List[BulkClassifyOutput] output: (optional) An array of objects that
          contain classification information for the submitted input utterances.
    """

    def __init__(
        self,
        *,
        output: Optional[List['BulkClassifyOutput']] = None,
    ) -> None:
        """
        Initialize a BulkClassifyResponse object.

        :param List[BulkClassifyOutput] output: (optional) An array of objects that
               contain classification information for the submitted input utterances.
        """
        self.output = output

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkClassifyResponse':
        """Initialize a BulkClassifyResponse object from a json dictionary."""
        args = {}
        if (output := _dict.get('output')) is not None:
            args['output'] = [BulkClassifyOutput.from_dict(v) for v in output]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkClassifyResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'output') and self.output is not None:
            output_list = []
            for v in self.output:
                if isinstance(v, dict):
                    output_list.append(v)
                else:
                    output_list.append(v.to_dict())
            _dict['output'] = output_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this BulkClassifyResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkClassifyResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkClassifyResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class BulkClassifyUtterance:
    """
    The user input utterance to classify.

    :param str text: The text of the input utterance.
    """

    def __init__(
        self,
        text: str,
    ) -> None:
        """
        Initialize a BulkClassifyUtterance object.

        :param str text: The text of the input utterance.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkClassifyUtterance':
        """Initialize a BulkClassifyUtterance object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in BulkClassifyUtterance JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a BulkClassifyUtterance object from a json dictionary."""
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
        """Return a `str` version of this BulkClassifyUtterance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'BulkClassifyUtterance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'BulkClassifyUtterance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CaptureGroup:
    """
    CaptureGroup.

    :param str group: A recognized capture group for the entity.
    :param List[int] location: (optional) Zero-based character offsets that indicate
          where the entity value begins and ends in the input text.
    """

    def __init__(
        self,
        group: str,
        *,
        location: Optional[List[int]] = None,
    ) -> None:
        """
        Initialize a CaptureGroup object.

        :param str group: A recognized capture group for the entity.
        :param List[int] location: (optional) Zero-based character offsets that
               indicate where the entity value begins and ends in the input text.
        """
        self.group = group
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CaptureGroup':
        """Initialize a CaptureGroup object from a json dictionary."""
        args = {}
        if (group := _dict.get('group')) is not None:
            args['group'] = group
        else:
            raise ValueError(
                'Required property \'group\' not present in CaptureGroup JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CaptureGroup object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CaptureGroup object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CaptureGroup') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CaptureGroup') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ChannelTransferInfo:
    """
    Information used by an integration to transfer the conversation to a different
    channel.

    :param ChannelTransferTarget target: An object specifying target channels
          available for the transfer. Each property of this object represents an available
          transfer target. Currently, the only supported property is **chat**,
          representing the web chat integration.
    """

    def __init__(
        self,
        target: 'ChannelTransferTarget',
    ) -> None:
        """
        Initialize a ChannelTransferInfo object.

        :param ChannelTransferTarget target: An object specifying target channels
               available for the transfer. Each property of this object represents an
               available transfer target. Currently, the only supported property is
               **chat**, representing the web chat integration.
        """
        self.target = target

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelTransferInfo':
        """Initialize a ChannelTransferInfo object from a json dictionary."""
        args = {}
        if (target := _dict.get('target')) is not None:
            args['target'] = ChannelTransferTarget.from_dict(target)
        else:
            raise ValueError(
                'Required property \'target\' not present in ChannelTransferInfo JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelTransferInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            if isinstance(self.target, dict):
                _dict['target'] = self.target
            else:
                _dict['target'] = self.target.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelTransferInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelTransferInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelTransferInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ChannelTransferTarget:
    """
    An object specifying target channels available for the transfer. Each property of this
    object represents an available transfer target. Currently, the only supported property
    is **chat**, representing the web chat integration.

    :param ChannelTransferTargetChat chat: (optional) Information for transferring
          to the web chat integration.
    """

    def __init__(
        self,
        *,
        chat: Optional['ChannelTransferTargetChat'] = None,
    ) -> None:
        """
        Initialize a ChannelTransferTarget object.

        :param ChannelTransferTargetChat chat: (optional) Information for
               transferring to the web chat integration.
        """
        self.chat = chat

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelTransferTarget':
        """Initialize a ChannelTransferTarget object from a json dictionary."""
        args = {}
        if (chat := _dict.get('chat')) is not None:
            args['chat'] = ChannelTransferTargetChat.from_dict(chat)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelTransferTarget object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'chat') and self.chat is not None:
            if isinstance(self.chat, dict):
                _dict['chat'] = self.chat
            else:
                _dict['chat'] = self.chat.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelTransferTarget object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelTransferTarget') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelTransferTarget') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ChannelTransferTargetChat:
    """
    Information for transferring to the web chat integration.

    :param str url: (optional) The URL of the target web chat.
    """

    def __init__(
        self,
        *,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize a ChannelTransferTargetChat object.

        :param str url: (optional) The URL of the target web chat.
        """
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelTransferTargetChat':
        """Initialize a ChannelTransferTargetChat object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ChannelTransferTargetChat object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ChannelTransferTargetChat object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ChannelTransferTargetChat') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ChannelTransferTargetChat') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateAssistantReleaseImportResponse:
    """
    CreateAssistantReleaseImportResponse.

    :param str status: (optional) The current status of the artifact import process:
           - **Failed**: The asynchronous artifact import process has failed.
           - **Processing**: An asynchronous operation to import artifact is underway and
          not yet completed.
    :param str task_id: (optional) A unique identifier for a background asynchronous
          task that is executing or has executed the operation.
    :param str assistant_id: (optional) The ID of the assistant to which the release
          belongs.
    :param List[str] skill_impact_in_draft: (optional) An array of skill types in
          the draft environment which will be overridden with skills from the artifact
          being imported.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        task_id: Optional[str] = None,
        assistant_id: Optional[str] = None,
        skill_impact_in_draft: Optional[List[str]] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a CreateAssistantReleaseImportResponse object.

        :param List[str] skill_impact_in_draft: (optional) An array of skill types
               in the draft environment which will be overridden with skills from the
               artifact being imported.
        """
        self.status = status
        self.task_id = task_id
        self.assistant_id = assistant_id
        self.skill_impact_in_draft = skill_impact_in_draft
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateAssistantReleaseImportResponse':
        """Initialize a CreateAssistantReleaseImportResponse object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (task_id := _dict.get('task_id')) is not None:
            args['task_id'] = task_id
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (skill_impact_in_draft :=
                _dict.get('skill_impact_in_draft')) is not None:
            args['skill_impact_in_draft'] = skill_impact_in_draft
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateAssistantReleaseImportResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'task_id') and getattr(self, 'task_id') is not None:
            _dict['task_id'] = getattr(self, 'task_id')
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'skill_impact_in_draft'
                  ) and self.skill_impact_in_draft is not None:
            _dict['skill_impact_in_draft'] = self.skill_impact_in_draft
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateAssistantReleaseImportResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateAssistantReleaseImportResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateAssistantReleaseImportResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the artifact import process:
         - **Failed**: The asynchronous artifact import process has failed.
         - **Processing**: An asynchronous operation to import artifact is underway and
        not yet completed.
        """

        FAILED = 'Failed'
        PROCESSING = 'Processing'

    class SkillImpactInDraftEnum(str, Enum):
        """
        The type of the skill in the draft environment.
        """

        ACTION = 'action'
        DIALOG = 'dialog'


class CreateReleaseExportWithStatusErrors:
    """
    CreateReleaseExportWithStatusErrors.

    :param str status: (optional) The current status of the release export creation
          process:
           - **Available**: The release export package is available for download.
           - **Failed**: The asynchronous release export package creation process has
          failed.
           - **Processing**: An asynchronous operation to create the release export
          package is underway and not yet completed.
    :param str task_id: (optional) A unique identifier for a background asynchronous
          task that is executing or has executed the operation.
    :param str assistant_id: (optional) The ID of the assistant to which the release
          belongs.
    :param str release: (optional) The name of the release. The name is the version
          number (an integer), returned as a string.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :param str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    """

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        task_id: Optional[str] = None,
        assistant_id: Optional[str] = None,
        release: Optional[str] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        status_errors: Optional[List['StatusError']] = None,
        status_description: Optional[str] = None,
    ) -> None:
        """
        Initialize a CreateReleaseExportWithStatusErrors object.

        """
        self.status = status
        self.task_id = task_id
        self.assistant_id = assistant_id
        self.release = release
        self.created = created
        self.updated = updated
        self.status_errors = status_errors
        self.status_description = status_description

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateReleaseExportWithStatusErrors':
        """Initialize a CreateReleaseExportWithStatusErrors object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (task_id := _dict.get('task_id')) is not None:
            args['task_id'] = task_id
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (release := _dict.get('release')) is not None:
            args['release'] = release
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        if (status_description := _dict.get('status_description')) is not None:
            args['status_description'] = status_description
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateReleaseExportWithStatusErrors object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'task_id') and getattr(self, 'task_id') is not None:
            _dict['task_id'] = getattr(self, 'task_id')
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'release') and getattr(self, 'release') is not None:
            _dict['release'] = getattr(self, 'release')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'status_errors') and getattr(
                self, 'status_errors') is not None:
            status_errors_list = []
            for v in getattr(self, 'status_errors'):
                if isinstance(v, dict):
                    status_errors_list.append(v)
                else:
                    status_errors_list.append(v.to_dict())
            _dict['status_errors'] = status_errors_list
        if hasattr(self, 'status_description') and getattr(
                self, 'status_description') is not None:
            _dict['status_description'] = getattr(self, 'status_description')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateReleaseExportWithStatusErrors object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateReleaseExportWithStatusErrors') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateReleaseExportWithStatusErrors') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the release export creation process:
         - **Available**: The release export package is available for download.
         - **Failed**: The asynchronous release export package creation process has
        failed.
         - **Processing**: An asynchronous operation to create the release export package
        is underway and not yet completed.
        """

        AVAILABLE = 'Available'
        FAILED = 'Failed'
        PROCESSING = 'Processing'


class DialogLogMessage:
    """
    Dialog log message details.

    :param str level: The severity of the log message.
    :param str message: The text of the log message.
    :param str code: A code that indicates the category to which the error message
          belongs.
    :param LogMessageSource source: (optional) An object that identifies the dialog
          element that generated the error message.
    """

    def __init__(
        self,
        level: str,
        message: str,
        code: str,
        *,
        source: Optional['LogMessageSource'] = None,
    ) -> None:
        """
        Initialize a DialogLogMessage object.

        :param str level: The severity of the log message.
        :param str message: The text of the log message.
        :param str code: A code that indicates the category to which the error
               message belongs.
        :param LogMessageSource source: (optional) An object that identifies the
               dialog element that generated the error message.
        """
        self.level = level
        self.message = message
        self.code = code
        self.source = source

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogLogMessage':
        """Initialize a DialogLogMessage object from a json dictionary."""
        args = {}
        if (level := _dict.get('level')) is not None:
            args['level'] = level
        else:
            raise ValueError(
                'Required property \'level\' not present in DialogLogMessage JSON'
            )
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        else:
            raise ValueError(
                'Required property \'message\' not present in DialogLogMessage JSON'
            )
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        else:
            raise ValueError(
                'Required property \'code\' not present in DialogLogMessage JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = LogMessageSource.from_dict(source)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogLogMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogLogMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogLogMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogLogMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LevelEnum(str, Enum):
        """
        The severity of the log message.
        """

        INFO = 'info'
        ERROR = 'error'
        WARN = 'warn'


class DialogNodeAction:
    """
    DialogNodeAction.

    :param str name: The name of the action.
    :param str type: (optional) The type of action to invoke.
    :param dict parameters: (optional) A map of key/value pairs to be provided to
          the action.
    :param str result_variable: The location in the dialog context where the result
          of the action is stored.
    :param str credentials: (optional) The name of the context variable that the
          client application will use to pass in credentials for the action.
    """

    def __init__(
        self,
        name: str,
        result_variable: str,
        *,
        type: Optional[str] = None,
        parameters: Optional[dict] = None,
        credentials: Optional[str] = None,
    ) -> None:
        """
        Initialize a DialogNodeAction object.

        :param str name: The name of the action.
        :param str result_variable: The location in the dialog context where the
               result of the action is stored.
        :param str type: (optional) The type of action to invoke.
        :param dict parameters: (optional) A map of key/value pairs to be provided
               to the action.
        :param str credentials: (optional) The name of the context variable that
               the client application will use to pass in credentials for the action.
        """
        self.name = name
        self.type = type
        self.parameters = parameters
        self.result_variable = result_variable
        self.credentials = credentials

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeAction':
        """Initialize a DialogNodeAction object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in DialogNodeAction JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (parameters := _dict.get('parameters')) is not None:
            args['parameters'] = parameters
        if (result_variable := _dict.get('result_variable')) is not None:
            args['result_variable'] = result_variable
        else:
            raise ValueError(
                'Required property \'result_variable\' not present in DialogNodeAction JSON'
            )
        if (credentials := _dict.get('credentials')) is not None:
            args['credentials'] = credentials
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'parameters') and self.parameters is not None:
            _dict['parameters'] = self.parameters
        if hasattr(self,
                   'result_variable') and self.result_variable is not None:
            _dict['result_variable'] = self.result_variable
        if hasattr(self, 'credentials') and self.credentials is not None:
            _dict['credentials'] = self.credentials
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of action to invoke.
        """

        CLIENT = 'client'
        SERVER = 'server'
        WEB_ACTION = 'web-action'
        CLOUD_FUNCTION = 'cloud-function'


class DialogNodeOutputConnectToAgentTransferInfo:
    """
    Routing or other contextual information to be used by target service desk systems.

    :param dict target: (optional)
    """

    def __init__(
        self,
        *,
        target: Optional[dict] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputConnectToAgentTransferInfo object.

        :param dict target: (optional)
        """
        self.target = target

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'DialogNodeOutputConnectToAgentTransferInfo':
        """Initialize a DialogNodeOutputConnectToAgentTransferInfo object from a json dictionary."""
        args = {}
        if (target := _dict.get('target')) is not None:
            args['target'] = target
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputConnectToAgentTransferInfo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'target') and self.target is not None:
            _dict['target'] = self.target
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeOutputConnectToAgentTransferInfo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'DialogNodeOutputConnectToAgentTransferInfo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'DialogNodeOutputConnectToAgentTransferInfo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputOptionsElement:
    """
    DialogNodeOutputOptionsElement.

    :param str label: The user-facing label for the option.
    :param DialogNodeOutputOptionsElementValue value: An object defining the message
          input to be sent to the assistant if the user selects the corresponding option.
    """

    def __init__(
        self,
        label: str,
        value: 'DialogNodeOutputOptionsElementValue',
    ) -> None:
        """
        Initialize a DialogNodeOutputOptionsElement object.

        :param str label: The user-facing label for the option.
        :param DialogNodeOutputOptionsElementValue value: An object defining the
               message input to be sent to the assistant if the user selects the
               corresponding option.
        """
        self.label = label
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputOptionsElement':
        """Initialize a DialogNodeOutputOptionsElement object from a json dictionary."""
        args = {}
        if (label := _dict.get('label')) is not None:
            args['label'] = label
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogNodeOutputOptionsElement JSON'
            )
        if (value := _dict.get('value')) is not None:
            args['value'] = DialogNodeOutputOptionsElementValue.from_dict(value)
        else:
            raise ValueError(
                'Required property \'value\' not present in DialogNodeOutputOptionsElement JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputOptionsElement object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'value') and self.value is not None:
            if isinstance(self.value, dict):
                _dict['value'] = self.value
            else:
                _dict['value'] = self.value.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeOutputOptionsElement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeOutputOptionsElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeOutputOptionsElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputOptionsElementValue:
    """
    An object defining the message input to be sent to the assistant if the user selects
    the corresponding option.

    :param MessageInput input: (optional) An input object that includes the input
          text.
    """

    def __init__(
        self,
        *,
        input: Optional['MessageInput'] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputOptionsElementValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        """
        self.input = input

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputOptionsElementValue':
        """Initialize a DialogNodeOutputOptionsElementValue object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputOptionsElementValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeOutputOptionsElementValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeOutputOptionsElementValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeOutputOptionsElementValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeVisited:
    """
    An objects containing detailed diagnostic information about a dialog node that was
    visited during processing of the input message.

    :param str dialog_node: (optional) A dialog node that was visited during
          processing of the input message.
    :param str title: (optional) The title of the dialog node.
    :param str conditions: (optional) The conditions that trigger the dialog node.
    """

    def __init__(
        self,
        *,
        dialog_node: Optional[str] = None,
        title: Optional[str] = None,
        conditions: Optional[str] = None,
    ) -> None:
        """
        Initialize a DialogNodeVisited object.

        :param str dialog_node: (optional) A dialog node that was visited during
               processing of the input message.
        :param str title: (optional) The title of the dialog node.
        :param str conditions: (optional) The conditions that trigger the dialog
               node.
        """
        self.dialog_node = dialog_node
        self.title = title
        self.conditions = conditions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeVisited':
        """Initialize a DialogNodeVisited object from a json dictionary."""
        args = {}
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (conditions := _dict.get('conditions')) is not None:
            args['conditions'] = conditions
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeVisited object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = self.conditions
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeVisited object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeVisited') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeVisited') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestion:
    """
    DialogSuggestion.

    :param str label: The user-facing label for the suggestion. This label is taken
          from the **title** or **user_label** property of the corresponding dialog node,
          depending on the disambiguation options.
    :param DialogSuggestionValue value: An object defining the message input to be
          sent to the assistant if the user selects the corresponding disambiguation
          option.
           **Note:** This entire message input object must be included in the request body
          of the next message sent to the assistant. Do not modify or remove any of the
          included properties.
    :param dict output: (optional) The dialog output that will be returned from the
          watsonx Assistant service if the user selects the corresponding option.
    """

    def __init__(
        self,
        label: str,
        value: 'DialogSuggestionValue',
        *,
        output: Optional[dict] = None,
    ) -> None:
        """
        Initialize a DialogSuggestion object.

        :param str label: The user-facing label for the suggestion. This label is
               taken from the **title** or **user_label** property of the corresponding
               dialog node, depending on the disambiguation options.
        :param DialogSuggestionValue value: An object defining the message input to
               be sent to the assistant if the user selects the corresponding
               disambiguation option.
                **Note:** This entire message input object must be included in the request
               body of the next message sent to the assistant. Do not modify or remove any
               of the included properties.
        :param dict output: (optional) The dialog output that will be returned from
               the watsonx Assistant service if the user selects the corresponding option.
        """
        self.label = label
        self.value = value
        self.output = output

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogSuggestion':
        """Initialize a DialogSuggestion object from a json dictionary."""
        args = {}
        if (label := _dict.get('label')) is not None:
            args['label'] = label
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogSuggestion JSON'
            )
        if (value := _dict.get('value')) is not None:
            args['value'] = DialogSuggestionValue.from_dict(value)
        else:
            raise ValueError(
                'Required property \'value\' not present in DialogSuggestion JSON'
            )
        if (output := _dict.get('output')) is not None:
            args['output'] = output
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestion object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'value') and self.value is not None:
            if isinstance(self.value, dict):
                _dict['value'] = self.value
            else:
                _dict['value'] = self.value.to_dict()
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogSuggestion object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogSuggestion') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogSuggestion') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestionValue:
    """
    An object defining the message input to be sent to the assistant if the user selects
    the corresponding disambiguation option.
     **Note:** This entire message input object must be included in the request body of
    the next message sent to the assistant. Do not modify or remove any of the included
    properties.

    :param MessageInput input: (optional) An input object that includes the input
          text.
    """

    def __init__(
        self,
        *,
        input: Optional['MessageInput'] = None,
    ) -> None:
        """
        Initialize a DialogSuggestionValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        """
        self.input = input

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogSuggestionValue':
        """Initialize a DialogSuggestionValue object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestionValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogSuggestionValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogSuggestionValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogSuggestionValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Environment:
    """
    Environment.

    :param str name: (optional) The name of the environment.
    :param str description: (optional) The description of the environment.
    :param str assistant_id: (optional) The assistant ID of the assistant the
          environment is associated with.
    :param str environment_id: (optional) The environment ID of the environment.
    :param str environment: (optional) The type of the environment. All environments
          other than the `draft` and `live` environments have the type `staging`.
    :param BaseEnvironmentReleaseReference release_reference: (optional) An object
          describing the release that is currently deployed in the environment.
    :param BaseEnvironmentOrchestration orchestration: The search skill
          orchestration settings for the environment.
    :param int session_timeout: The session inactivity timeout setting for the
          environment (in seconds).
    :param List[IntegrationReference] integration_references: (optional) An array of
          objects describing the integrations that exist in the environment.
    :param List[EnvironmentSkill] skill_references: An array of objects identifying
          the skills (such as action and dialog) that exist in the environment.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        orchestration: 'BaseEnvironmentOrchestration',
        session_timeout: int,
        skill_references: List['EnvironmentSkill'],
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        assistant_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        environment: Optional[str] = None,
        release_reference: Optional['BaseEnvironmentReleaseReference'] = None,
        integration_references: Optional[List['IntegrationReference']] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Environment object.

        :param BaseEnvironmentOrchestration orchestration: The search skill
               orchestration settings for the environment.
        :param int session_timeout: The session inactivity timeout setting for the
               environment (in seconds).
        :param List[EnvironmentSkill] skill_references: An array of objects
               identifying the skills (such as action and dialog) that exist in the
               environment.
        :param str name: (optional) The name of the environment.
        :param str description: (optional) The description of the environment.
        """
        self.name = name
        self.description = description
        self.assistant_id = assistant_id
        self.environment_id = environment_id
        self.environment = environment
        self.release_reference = release_reference
        self.orchestration = orchestration
        self.session_timeout = session_timeout
        self.integration_references = integration_references
        self.skill_references = skill_references
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Environment':
        """Initialize a Environment object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (environment_id := _dict.get('environment_id')) is not None:
            args['environment_id'] = environment_id
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        if (release_reference := _dict.get('release_reference')) is not None:
            args[
                'release_reference'] = BaseEnvironmentReleaseReference.from_dict(
                    release_reference)
        if (orchestration := _dict.get('orchestration')) is not None:
            args['orchestration'] = BaseEnvironmentOrchestration.from_dict(
                orchestration)
        else:
            raise ValueError(
                'Required property \'orchestration\' not present in Environment JSON'
            )
        if (session_timeout := _dict.get('session_timeout')) is not None:
            args['session_timeout'] = session_timeout
        else:
            raise ValueError(
                'Required property \'session_timeout\' not present in Environment JSON'
            )
        if (integration_references :=
                _dict.get('integration_references')) is not None:
            args['integration_references'] = [
                IntegrationReference.from_dict(v)
                for v in integration_references
            ]
        if (skill_references := _dict.get('skill_references')) is not None:
            args['skill_references'] = [
                EnvironmentSkill.from_dict(v) for v in skill_references
            ]
        else:
            raise ValueError(
                'Required property \'skill_references\' not present in Environment JSON'
            )
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Environment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'environment_id') and getattr(
                self, 'environment_id') is not None:
            _dict['environment_id'] = getattr(self, 'environment_id')
        if hasattr(self, 'environment') and getattr(self,
                                                    'environment') is not None:
            _dict['environment'] = getattr(self, 'environment')
        if hasattr(self, 'release_reference') and getattr(
                self, 'release_reference') is not None:
            if isinstance(getattr(self, 'release_reference'), dict):
                _dict['release_reference'] = getattr(self, 'release_reference')
            else:
                _dict['release_reference'] = getattr(
                    self, 'release_reference').to_dict()
        if hasattr(self, 'orchestration') and self.orchestration is not None:
            if isinstance(self.orchestration, dict):
                _dict['orchestration'] = self.orchestration
            else:
                _dict['orchestration'] = self.orchestration.to_dict()
        if hasattr(self,
                   'session_timeout') and self.session_timeout is not None:
            _dict['session_timeout'] = self.session_timeout
        if hasattr(self, 'integration_references') and getattr(
                self, 'integration_references') is not None:
            integration_references_list = []
            for v in getattr(self, 'integration_references'):
                if isinstance(v, dict):
                    integration_references_list.append(v)
                else:
                    integration_references_list.append(v.to_dict())
            _dict['integration_references'] = integration_references_list
        if hasattr(self,
                   'skill_references') and self.skill_references is not None:
            skill_references_list = []
            for v in self.skill_references:
                if isinstance(v, dict):
                    skill_references_list.append(v)
                else:
                    skill_references_list.append(v.to_dict())
            _dict['skill_references'] = skill_references_list
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Environment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Environment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentCollection:
    """
    EnvironmentCollection.

    :param List[Environment] environments: An array of objects describing the
          environments associated with an assistant.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        environments: List['Environment'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a EnvironmentCollection object.

        :param List[Environment] environments: An array of objects describing the
               environments associated with an assistant.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.environments = environments
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentCollection':
        """Initialize a EnvironmentCollection object from a json dictionary."""
        args = {}
        if (environments := _dict.get('environments')) is not None:
            args['environments'] = [
                Environment.from_dict(v) for v in environments
            ]
        else:
            raise ValueError(
                'Required property \'environments\' not present in EnvironmentCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in EnvironmentCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'environments') and self.environments is not None:
            environments_list = []
            for v in self.environments:
                if isinstance(v, dict):
                    environments_list.append(v)
                else:
                    environments_list.append(v.to_dict())
            _dict['environments'] = environments_list
        if hasattr(self, 'pagination') and self.pagination is not None:
            if isinstance(self.pagination, dict):
                _dict['pagination'] = self.pagination
            else:
                _dict['pagination'] = self.pagination.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EnvironmentReference:
    """
    EnvironmentReference.

    :param str name: (optional) The name of the environment.
    :param str environment_id: (optional) The unique identifier of the environment.
    :param str environment: (optional) The type of the environment. All environments
          other than the draft and live environments have the type `staging`.
    """

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        environment_id: Optional[str] = None,
        environment: Optional[str] = None,
    ) -> None:
        """
        Initialize a EnvironmentReference object.

        :param str name: (optional) The name of the environment.
        """
        self.name = name
        self.environment_id = environment_id
        self.environment = environment

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentReference':
        """Initialize a EnvironmentReference object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (environment_id := _dict.get('environment_id')) is not None:
            args['environment_id'] = environment_id
        if (environment := _dict.get('environment')) is not None:
            args['environment'] = environment
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'environment_id') and getattr(
                self, 'environment_id') is not None:
            _dict['environment_id'] = getattr(self, 'environment_id')
        if hasattr(self, 'environment') and getattr(self,
                                                    'environment') is not None:
            _dict['environment'] = getattr(self, 'environment')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class EnvironmentEnum(str, Enum):
        """
        The type of the environment. All environments other than the draft and live
        environments have the type `staging`.
        """

        DRAFT = 'draft'
        LIVE = 'live'
        STAGING = 'staging'


class EnvironmentSkill:
    """
    EnvironmentSkill.

    :param str skill_id: The skill ID of the skill.
    :param str type: (optional) The type of the skill.
    :param bool disabled: (optional) Whether the skill is disabled. A disabled skill
          in the draft environment does not handle any messages at run time, and it is not
          included in saved releases.
    :param str snapshot: (optional) The name of the skill snapshot that is deployed
          to the environment (for example, `draft` or `1`).
    :param str skill_reference: (optional) The type of skill identified by the skill
          reference. The possible values are `main skill` (for a dialog skill), `actions
          skill`, and `search skill`.
    """

    def __init__(
        self,
        skill_id: str,
        *,
        type: Optional[str] = None,
        disabled: Optional[bool] = None,
        snapshot: Optional[str] = None,
        skill_reference: Optional[str] = None,
    ) -> None:
        """
        Initialize a EnvironmentSkill object.

        :param str skill_id: The skill ID of the skill.
        :param str type: (optional) The type of the skill.
        :param bool disabled: (optional) Whether the skill is disabled. A disabled
               skill in the draft environment does not handle any messages at run time,
               and it is not included in saved releases.
        :param str snapshot: (optional) The name of the skill snapshot that is
               deployed to the environment (for example, `draft` or `1`).
        :param str skill_reference: (optional) The type of skill identified by the
               skill reference. The possible values are `main skill` (for a dialog skill),
               `actions skill`, and `search skill`.
        """
        self.skill_id = skill_id
        self.type = type
        self.disabled = disabled
        self.snapshot = snapshot
        self.skill_reference = skill_reference

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EnvironmentSkill':
        """Initialize a EnvironmentSkill object from a json dictionary."""
        args = {}
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in EnvironmentSkill JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (disabled := _dict.get('disabled')) is not None:
            args['disabled'] = disabled
        if (snapshot := _dict.get('snapshot')) is not None:
            args['snapshot'] = snapshot
        if (skill_reference := _dict.get('skill_reference')) is not None:
            args['skill_reference'] = skill_reference
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EnvironmentSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'skill_id') and self.skill_id is not None:
            _dict['skill_id'] = self.skill_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'snapshot') and self.snapshot is not None:
            _dict['snapshot'] = self.snapshot
        if hasattr(self,
                   'skill_reference') and self.skill_reference is not None:
            _dict['skill_reference'] = self.skill_reference
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this EnvironmentSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EnvironmentSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EnvironmentSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the skill.
        """

        DIALOG = 'dialog'
        ACTION = 'action'
        SEARCH = 'search'


class IntegrationReference:
    """
    IntegrationReference.

    :param str integration_id: (optional) The integration ID of the integration.
    :param str type: (optional) The type of the integration.
    """

    def __init__(
        self,
        *,
        integration_id: Optional[str] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a IntegrationReference object.

        :param str integration_id: (optional) The integration ID of the
               integration.
        :param str type: (optional) The type of the integration.
        """
        self.integration_id = integration_id
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IntegrationReference':
        """Initialize a IntegrationReference object from a json dictionary."""
        args = {}
        if (integration_id := _dict.get('integration_id')) is not None:
            args['integration_id'] = integration_id
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntegrationReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'integration_id') and self.integration_id is not None:
            _dict['integration_id'] = self.integration_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this IntegrationReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IntegrationReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IntegrationReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Log:
    """
    Log.

    :param str log_id: A unique identifier for the logged event.
    :param LogRequest request: A message request formatted for the watsonx Assistant
          service.
    :param LogResponse response: A response from the watsonx Assistant service.
    :param str assistant_id: Unique identifier of the assistant.
    :param str session_id: The ID of the session the message was part of.
    :param str skill_id: The unique identifier of the skill that responded to the
          message.
    :param str snapshot: The name of the snapshot (dialog skill version) that
          responded to the message (for example, `draft`).
    :param str request_timestamp: The timestamp for receipt of the message.
    :param str response_timestamp: The timestamp for the system response to the
          message.
    :param str language: The language of the assistant to which the message request
          was made.
    :param str customer_id: (optional) The customer ID specified for the message, if
          any.
    """

    def __init__(
        self,
        log_id: str,
        request: 'LogRequest',
        response: 'LogResponse',
        assistant_id: str,
        session_id: str,
        skill_id: str,
        snapshot: str,
        request_timestamp: str,
        response_timestamp: str,
        language: str,
        *,
        customer_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a Log object.

        :param str log_id: A unique identifier for the logged event.
        :param LogRequest request: A message request formatted for the watsonx
               Assistant service.
        :param LogResponse response: A response from the watsonx Assistant service.
        :param str assistant_id: Unique identifier of the assistant.
        :param str session_id: The ID of the session the message was part of.
        :param str skill_id: The unique identifier of the skill that responded to
               the message.
        :param str snapshot: The name of the snapshot (dialog skill version) that
               responded to the message (for example, `draft`).
        :param str request_timestamp: The timestamp for receipt of the message.
        :param str response_timestamp: The timestamp for the system response to the
               message.
        :param str language: The language of the assistant to which the message
               request was made.
        :param str customer_id: (optional) The customer ID specified for the
               message, if any.
        """
        self.log_id = log_id
        self.request = request
        self.response = response
        self.assistant_id = assistant_id
        self.session_id = session_id
        self.skill_id = skill_id
        self.snapshot = snapshot
        self.request_timestamp = request_timestamp
        self.response_timestamp = response_timestamp
        self.language = language
        self.customer_id = customer_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Log':
        """Initialize a Log object from a json dictionary."""
        args = {}
        if (log_id := _dict.get('log_id')) is not None:
            args['log_id'] = log_id
        else:
            raise ValueError(
                'Required property \'log_id\' not present in Log JSON')
        if (request := _dict.get('request')) is not None:
            args['request'] = LogRequest.from_dict(request)
        else:
            raise ValueError(
                'Required property \'request\' not present in Log JSON')
        if (response := _dict.get('response')) is not None:
            args['response'] = LogResponse.from_dict(response)
        else:
            raise ValueError(
                'Required property \'response\' not present in Log JSON')
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        else:
            raise ValueError(
                'Required property \'assistant_id\' not present in Log JSON')
        if (session_id := _dict.get('session_id')) is not None:
            args['session_id'] = session_id
        else:
            raise ValueError(
                'Required property \'session_id\' not present in Log JSON')
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in Log JSON')
        if (snapshot := _dict.get('snapshot')) is not None:
            args['snapshot'] = snapshot
        else:
            raise ValueError(
                'Required property \'snapshot\' not present in Log JSON')
        if (request_timestamp := _dict.get('request_timestamp')) is not None:
            args['request_timestamp'] = request_timestamp
        else:
            raise ValueError(
                'Required property \'request_timestamp\' not present in Log JSON'
            )
        if (response_timestamp := _dict.get('response_timestamp')) is not None:
            args['response_timestamp'] = response_timestamp
        else:
            raise ValueError(
                'Required property \'response_timestamp\' not present in Log JSON'
            )
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in Log JSON')
        if (customer_id := _dict.get('customer_id')) is not None:
            args['customer_id'] = customer_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Log object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'log_id') and self.log_id is not None:
            _dict['log_id'] = self.log_id
        if hasattr(self, 'request') and self.request is not None:
            if isinstance(self.request, dict):
                _dict['request'] = self.request
            else:
                _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        if hasattr(self, 'assistant_id') and self.assistant_id is not None:
            _dict['assistant_id'] = self.assistant_id
        if hasattr(self, 'session_id') and self.session_id is not None:
            _dict['session_id'] = self.session_id
        if hasattr(self, 'skill_id') and self.skill_id is not None:
            _dict['skill_id'] = self.skill_id
        if hasattr(self, 'snapshot') and self.snapshot is not None:
            _dict['snapshot'] = self.snapshot
        if hasattr(self,
                   'request_timestamp') and self.request_timestamp is not None:
            _dict['request_timestamp'] = self.request_timestamp
        if hasattr(
                self,
                'response_timestamp') and self.response_timestamp is not None:
            _dict['response_timestamp'] = self.response_timestamp
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'customer_id') and self.customer_id is not None:
            _dict['customer_id'] = self.customer_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Log object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Log') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Log') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogCollection:
    """
    LogCollection.

    :param List[Log] logs: An array of objects describing log events.
    :param LogPagination pagination: The pagination data for the returned objects.
          For more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        logs: List['Log'],
        pagination: 'LogPagination',
    ) -> None:
        """
        Initialize a LogCollection object.

        :param List[Log] logs: An array of objects describing log events.
        :param LogPagination pagination: The pagination data for the returned
               objects. For more information about using pagination, see
               [Pagination](#pagination).
        """
        self.logs = logs
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogCollection':
        """Initialize a LogCollection object from a json dictionary."""
        args = {}
        if (logs := _dict.get('logs')) is not None:
            args['logs'] = [Log.from_dict(v) for v in logs]
        else:
            raise ValueError(
                'Required property \'logs\' not present in LogCollection JSON')
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = LogPagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in LogCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'logs') and self.logs is not None:
            logs_list = []
            for v in self.logs:
                if isinstance(v, dict):
                    logs_list.append(v)
                else:
                    logs_list.append(v.to_dict())
            _dict['logs'] = logs_list
        if hasattr(self, 'pagination') and self.pagination is not None:
            if isinstance(self.pagination, dict):
                _dict['pagination'] = self.pagination
            else:
                _dict['pagination'] = self.pagination.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessageSource:
    """
    An object that identifies the dialog element that generated the error message.

    """

    def __init__(self,) -> None:
        """
        Initialize a LogMessageSource object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'LogMessageSourceDialogNode', 'LogMessageSourceAction',
                'LogMessageSourceStep', 'LogMessageSourceHandler'
            ]))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSource':
        """Initialize a LogMessageSource object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'LogMessageSource'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join([
                'LogMessageSourceDialogNode', 'LogMessageSourceAction',
                'LogMessageSourceStep', 'LogMessageSourceHandler'
            ]))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a LogMessageSource object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['dialog_node'] = 'LogMessageSourceDialogNode'
        mapping['action'] = 'LogMessageSourceAction'
        mapping['step'] = 'LogMessageSourceStep'
        mapping['handler'] = 'LogMessageSourceHandler'
        disc_value = _dict.get('type')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'type\' not found in LogMessageSource JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class LogPagination:
    """
    The pagination data for the returned objects. For more information about using
    pagination, see [Pagination](#pagination).

    :param str next_url: (optional) The URL that will return the next page of
          results, if any.
    :param int matched: (optional) Reserved for future use.
    :param str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(
        self,
        *,
        next_url: Optional[str] = None,
        matched: Optional[int] = None,
        next_cursor: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogPagination object.

        :param str next_url: (optional) The URL that will return the next page of
               results, if any.
        :param int matched: (optional) Reserved for future use.
        :param str next_cursor: (optional) A token identifying the next page of
               results.
        """
        self.next_url = next_url
        self.matched = matched
        self.next_cursor = next_cursor

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogPagination':
        """Initialize a LogPagination object from a json dictionary."""
        args = {}
        if (next_url := _dict.get('next_url')) is not None:
            args['next_url'] = next_url
        if (matched := _dict.get('matched')) is not None:
            args['matched'] = matched
        if (next_cursor := _dict.get('next_cursor')) is not None:
            args['next_cursor'] = next_cursor
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogPagination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'matched') and self.matched is not None:
            _dict['matched'] = self.matched
        if hasattr(self, 'next_cursor') and self.next_cursor is not None:
            _dict['next_cursor'] = self.next_cursor
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogPagination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogPagination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogPagination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogRequest:
    """
    A message request formatted for the watsonx Assistant service.

    :param LogRequestInput input: (optional) An input object that includes the input
          text. All private data is masked or removed.
    :param MessageContext context: (optional) Context data for the conversation. You
          can use this property to set or modify context variables, which can also be
          accessed by dialog nodes. The context is stored by the assistant on a
          per-session basis.
          **Note:** The total size of the context data stored for a stateful session
          cannot exceed 100KB.
    :param str user_id: (optional) A string value that identifies the user who is
          interacting with the assistant. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context. If **user_id** is specified in both locations, the value
          specified at the root is used.
    """

    def __init__(
        self,
        *,
        input: Optional['LogRequestInput'] = None,
        context: Optional['MessageContext'] = None,
        user_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogRequest object.

        :param LogRequestInput input: (optional) An input object that includes the
               input text. All private data is masked or removed.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to set or modify context variables,
               which can also be accessed by dialog nodes. The context is stored by the
               assistant on a per-session basis.
               **Note:** The total size of the context data stored for a stateful session
               cannot exceed 100KB.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context. If **user_id** is specified in both locations, the
               value specified at the root is used.
        """
        self.input = input
        self.context = context
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogRequest':
        """Initialize a LogRequest object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = LogRequestInput.from_dict(input)
        if (context := _dict.get('context')) is not None:
            args['context'] = MessageContext.from_dict(context)
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogRequestInput:
    """
    An input object that includes the input text. All private data is masked or removed.

    :param str message_type: (optional) The type of the message:
          - `text`: The user input is processed normally by the assistant.
          - `search`: Only search results are returned. (Any dialog or action skill is
          bypassed.)
          **Note:** A `search` message results in an error if no search skill is
          configured for the assistant.
    :param str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :param List[RuntimeIntent] intents: (optional) Intents to use when evaluating
          the user input. Include intents from the previous response to continue using
          those intents rather than trying to recognize intents in the new input.
    :param List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :param str suggestion_id: (optional) For internal use only.
    :param List[MessageInputAttachment] attachments: (optional) An array of
          multimedia attachments to be sent with the message. Attachments are not
          processed by the assistant itself, but can be sent to external services by
          webhooks.
           **Note:** Attachments are not supported on IBM Cloud Pak for Data.
    :param RequestAnalytics analytics: (optional) An optional object containing
          analytics data. Currently, this data is used only for events sent to the Segment
          extension.
    :param MessageInputOptions options: (optional) Optional properties that control
          how the assistant responds.
    """

    def __init__(
        self,
        *,
        message_type: Optional[str] = None,
        text: Optional[str] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        suggestion_id: Optional[str] = None,
        attachments: Optional[List['MessageInputAttachment']] = None,
        analytics: Optional['RequestAnalytics'] = None,
        options: Optional['MessageInputOptions'] = None,
    ) -> None:
        """
        Initialize a LogRequestInput object.

        :param str message_type: (optional) The type of the message:
               - `text`: The user input is processed normally by the assistant.
               - `search`: Only search results are returned. (Any dialog or action skill
               is bypassed.)
               **Note:** A `search` message results in an error if no search skill is
               configured for the assistant.
        :param str text: (optional) The text of the user input. This string cannot
               contain carriage return, newline, or tab characters.
        :param List[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param List[RuntimeEntity] entities: (optional) Entities to use when
               evaluating the message. Include entities from the previous response to
               continue using those entities rather than detecting entities in the new
               input.
        :param str suggestion_id: (optional) For internal use only.
        :param List[MessageInputAttachment] attachments: (optional) An array of
               multimedia attachments to be sent with the message. Attachments are not
               processed by the assistant itself, but can be sent to external services by
               webhooks.
                **Note:** Attachments are not supported on IBM Cloud Pak for Data.
        :param RequestAnalytics analytics: (optional) An optional object containing
               analytics data. Currently, this data is used only for events sent to the
               Segment extension.
        :param MessageInputOptions options: (optional) Optional properties that
               control how the assistant responds.
        """
        self.message_type = message_type
        self.text = text
        self.intents = intents
        self.entities = entities
        self.suggestion_id = suggestion_id
        self.attachments = attachments
        self.analytics = analytics
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogRequestInput':
        """Initialize a LogRequestInput object from a json dictionary."""
        args = {}
        if (message_type := _dict.get('message_type')) is not None:
            args['message_type'] = message_type
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (suggestion_id := _dict.get('suggestion_id')) is not None:
            args['suggestion_id'] = suggestion_id
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = [
                MessageInputAttachment.from_dict(v) for v in attachments
            ]
        if (analytics := _dict.get('analytics')) is not None:
            args['analytics'] = RequestAnalytics.from_dict(analytics)
        if (options := _dict.get('options')) is not None:
            args['options'] = MessageInputOptions.from_dict(options)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogRequestInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message_type') and self.message_type is not None:
            _dict['message_type'] = self.message_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'suggestion_id') and self.suggestion_id is not None:
            _dict['suggestion_id'] = self.suggestion_id
        if hasattr(self, 'attachments') and self.attachments is not None:
            attachments_list = []
            for v in self.attachments:
                if isinstance(v, dict):
                    attachments_list.append(v)
                else:
                    attachments_list.append(v.to_dict())
            _dict['attachments'] = attachments_list
        if hasattr(self, 'analytics') and self.analytics is not None:
            if isinstance(self.analytics, dict):
                _dict['analytics'] = self.analytics
            else:
                _dict['analytics'] = self.analytics.to_dict()
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogRequestInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogRequestInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogRequestInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MessageTypeEnum(str, Enum):
        """
        The type of the message:
        - `text`: The user input is processed normally by the assistant.
        - `search`: Only search results are returned. (Any dialog or action skill is
        bypassed.)
        **Note:** A `search` message results in an error if no search skill is configured
        for the assistant.
        """

        TEXT = 'text'
        SEARCH = 'search'


class LogResponse:
    """
    A response from the watsonx Assistant service.

    :param LogResponseOutput output: Assistant output to be rendered or processed by
          the client. All private data is masked or removed.
    :param MessageContext context: (optional) Context data for the conversation. You
          can use this property to access context variables. The context is stored by the
          assistant on a per-session basis.
          **Note:** The context is included in message responses only if
          **return_context**=`true` in the message request. Full context is always
          included in logs.
    :param str user_id: A string value that identifies the user who is interacting
          with the assistant. The client must provide a unique identifier for each
          individual end user who accesses the application. For user-based plans, this
          user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context.
    """

    def __init__(
        self,
        output: 'LogResponseOutput',
        user_id: str,
        *,
        context: Optional['MessageContext'] = None,
    ) -> None:
        """
        Initialize a LogResponse object.

        :param LogResponseOutput output: Assistant output to be rendered or
               processed by the client. All private data is masked or removed.
        :param str user_id: A string value that identifies the user who is
               interacting with the assistant. The client must provide a unique identifier
               for each individual end user who accesses the application. For user-based
               plans, this user ID is used to identify unique users for billing purposes.
               This string cannot contain carriage return, newline, or tab characters. If
               no value is specified in the input, **user_id** is automatically set to the
               value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to access context variables. The
               context is stored by the assistant on a per-session basis.
               **Note:** The context is included in message responses only if
               **return_context**=`true` in the message request. Full context is always
               included in logs.
        """
        self.output = output
        self.context = context
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogResponse':
        """Initialize a LogResponse object from a json dictionary."""
        args = {}
        if (output := _dict.get('output')) is not None:
            args['output'] = LogResponseOutput.from_dict(output)
        else:
            raise ValueError(
                'Required property \'output\' not present in LogResponse JSON')
        if (context := _dict.get('context')) is not None:
            args['context'] = MessageContext.from_dict(context)
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        else:
            raise ValueError(
                'Required property \'user_id\' not present in LogResponse JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'output') and self.output is not None:
            if isinstance(self.output, dict):
                _dict['output'] = self.output
            else:
                _dict['output'] = self.output.to_dict()
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogResponseOutput:
    """
    Assistant output to be rendered or processed by the client. All private data is masked
    or removed.

    :param List[RuntimeResponseGeneric] generic: (optional) Output intended for any
          channel. It is the responsibility of the client application to implement the
          supported response types.
    :param List[RuntimeIntent] intents: (optional) An array of intents recognized in
          the user input, sorted in descending order of confidence.
    :param List[RuntimeEntity] entities: (optional) An array of entities identified
          in the user input.
    :param List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    :param MessageOutputDebug debug: (optional) Additional detailed information
          about a message response and how it was generated.
    :param dict user_defined: (optional) An object containing any custom properties
          included in the response. This object includes any arbitrary properties defined
          in the dialog JSON editor as part of the dialog node output.
    :param MessageOutputSpelling spelling: (optional) Properties describing any
          spelling corrections in the user input that was received.
    """

    def __init__(
        self,
        *,
        generic: Optional[List['RuntimeResponseGeneric']] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        actions: Optional[List['DialogNodeAction']] = None,
        debug: Optional['MessageOutputDebug'] = None,
        user_defined: Optional[dict] = None,
        spelling: Optional['MessageOutputSpelling'] = None,
    ) -> None:
        """
        Initialize a LogResponseOutput object.

        :param List[RuntimeResponseGeneric] generic: (optional) Output intended for
               any channel. It is the responsibility of the client application to
               implement the supported response types.
        :param List[RuntimeIntent] intents: (optional) An array of intents
               recognized in the user input, sorted in descending order of confidence.
        :param List[RuntimeEntity] entities: (optional) An array of entities
               identified in the user input.
        :param List[DialogNodeAction] actions: (optional) An array of objects
               describing any actions requested by the dialog node.
        :param MessageOutputDebug debug: (optional) Additional detailed information
               about a message response and how it was generated.
        :param dict user_defined: (optional) An object containing any custom
               properties included in the response. This object includes any arbitrary
               properties defined in the dialog JSON editor as part of the dialog node
               output.
        :param MessageOutputSpelling spelling: (optional) Properties describing any
               spelling corrections in the user input that was received.
        """
        self.generic = generic
        self.intents = intents
        self.entities = entities
        self.actions = actions
        self.debug = debug
        self.user_defined = user_defined
        self.spelling = spelling

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogResponseOutput':
        """Initialize a LogResponseOutput object from a json dictionary."""
        args = {}
        if (generic := _dict.get('generic')) is not None:
            args['generic'] = [
                RuntimeResponseGeneric.from_dict(v) for v in generic
            ]
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (actions := _dict.get('actions')) is not None:
            args['actions'] = [DialogNodeAction.from_dict(v) for v in actions]
        if (debug := _dict.get('debug')) is not None:
            args['debug'] = MessageOutputDebug.from_dict(debug)
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        if (spelling := _dict.get('spelling')) is not None:
            args['spelling'] = MessageOutputSpelling.from_dict(spelling)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogResponseOutput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'generic') and self.generic is not None:
            generic_list = []
            for v in self.generic:
                if isinstance(v, dict):
                    generic_list.append(v)
                else:
                    generic_list.append(v.to_dict())
            _dict['generic'] = generic_list
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'actions') and self.actions is not None:
            actions_list = []
            for v in self.actions:
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
        if hasattr(self, 'debug') and self.debug is not None:
            if isinstance(self.debug, dict):
                _dict['debug'] = self.debug
            else:
                _dict['debug'] = self.debug.to_dict()
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'spelling') and self.spelling is not None:
            if isinstance(self.spelling, dict):
                _dict['spelling'] = self.spelling
            else:
                _dict['spelling'] = self.spelling.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogResponseOutput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogResponseOutput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogResponseOutput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContext:
    """
    MessageContext.

    :param MessageContextGlobal global_: (optional) Session context data that is
          shared by all skills used by the assistant.
    :param MessageContextSkills skills: (optional) Context data specific to
          particular skills used by the assistant.
    :param dict integrations: (optional) An object containing context data that is
          specific to particular integrations. For more information, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
    """

    def __init__(
        self,
        *,
        global_: Optional['MessageContextGlobal'] = None,
        skills: Optional['MessageContextSkills'] = None,
        integrations: Optional[dict] = None,
    ) -> None:
        """
        Initialize a MessageContext object.

        :param MessageContextGlobal global_: (optional) Session context data that
               is shared by all skills used by the assistant.
        :param MessageContextSkills skills: (optional) Context data specific to
               particular skills used by the assistant.
        :param dict integrations: (optional) An object containing context data that
               is specific to particular integrations. For more information, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
        """
        self.global_ = global_
        self.skills = skills
        self.integrations = integrations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContext':
        """Initialize a MessageContext object from a json dictionary."""
        args = {}
        if (global_ := _dict.get('global')) is not None:
            args['global_'] = MessageContextGlobal.from_dict(global_)
        if (skills := _dict.get('skills')) is not None:
            args['skills'] = MessageContextSkills.from_dict(skills)
        if (integrations := _dict.get('integrations')) is not None:
            args['integrations'] = integrations
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'global_') and self.global_ is not None:
            if isinstance(self.global_, dict):
                _dict['global'] = self.global_
            else:
                _dict['global'] = self.global_.to_dict()
        if hasattr(self, 'skills') and self.skills is not None:
            if isinstance(self.skills, dict):
                _dict['skills'] = self.skills
            else:
                _dict['skills'] = self.skills.to_dict()
        if hasattr(self, 'integrations') and self.integrations is not None:
            _dict['integrations'] = self.integrations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextActionSkill:
    """
    Context variables that are used by the action skill. Private variables are persisted,
    but not shown.

    :param dict user_defined: (optional) An object containing any arbitrary
          variables that can be read and written by a particular skill.
    :param MessageContextSkillSystem system: (optional) System context data used by
          the skill.
    :param dict action_variables: (optional) An object containing action variables.
          Action variables can be accessed only by steps in the same action, and do not
          persist after the action ends.
    :param dict skill_variables: (optional) An object containing skill variables.
          (In the watsonx Assistant user interface, skill variables are called _session
          variables_.) Skill variables can be accessed by any action and persist for the
          duration of the session.
    """

    def __init__(
        self,
        *,
        user_defined: Optional[dict] = None,
        system: Optional['MessageContextSkillSystem'] = None,
        action_variables: Optional[dict] = None,
        skill_variables: Optional[dict] = None,
    ) -> None:
        """
        Initialize a MessageContextActionSkill object.

        :param dict user_defined: (optional) An object containing any arbitrary
               variables that can be read and written by a particular skill.
        :param MessageContextSkillSystem system: (optional) System context data
               used by the skill.
        :param dict action_variables: (optional) An object containing action
               variables. Action variables can be accessed only by steps in the same
               action, and do not persist after the action ends.
        :param dict skill_variables: (optional) An object containing skill
               variables. (In the watsonx Assistant user interface, skill variables are
               called _session variables_.) Skill variables can be accessed by any action
               and persist for the duration of the session.
        """
        self.user_defined = user_defined
        self.system = system
        self.action_variables = action_variables
        self.skill_variables = skill_variables

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextActionSkill':
        """Initialize a MessageContextActionSkill object from a json dictionary."""
        args = {}
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        if (system := _dict.get('system')) is not None:
            args['system'] = MessageContextSkillSystem.from_dict(system)
        if (action_variables := _dict.get('action_variables')) is not None:
            args['action_variables'] = action_variables
        if (skill_variables := _dict.get('skill_variables')) is not None:
            args['skill_variables'] = skill_variables
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextActionSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'system') and self.system is not None:
            if isinstance(self.system, dict):
                _dict['system'] = self.system
            else:
                _dict['system'] = self.system.to_dict()
        if hasattr(self,
                   'action_variables') and self.action_variables is not None:
            _dict['action_variables'] = self.action_variables
        if hasattr(self,
                   'skill_variables') and self.skill_variables is not None:
            _dict['skill_variables'] = self.skill_variables
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextActionSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextActionSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextActionSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextDialogSkill:
    """
    Context variables that are used by the dialog skill.

    :param dict user_defined: (optional) An object containing any arbitrary
          variables that can be read and written by a particular skill.
    :param MessageContextSkillSystem system: (optional) System context data used by
          the skill.
    """

    def __init__(
        self,
        *,
        user_defined: Optional[dict] = None,
        system: Optional['MessageContextSkillSystem'] = None,
    ) -> None:
        """
        Initialize a MessageContextDialogSkill object.

        :param dict user_defined: (optional) An object containing any arbitrary
               variables that can be read and written by a particular skill.
        :param MessageContextSkillSystem system: (optional) System context data
               used by the skill.
        """
        self.user_defined = user_defined
        self.system = system

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextDialogSkill':
        """Initialize a MessageContextDialogSkill object from a json dictionary."""
        args = {}
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        if (system := _dict.get('system')) is not None:
            args['system'] = MessageContextSkillSystem.from_dict(system)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextDialogSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'system') and self.system is not None:
            if isinstance(self.system, dict):
                _dict['system'] = self.system
            else:
                _dict['system'] = self.system.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextDialogSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextDialogSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextDialogSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextGlobal:
    """
    Session context data that is shared by all skills used by the assistant.

    :param MessageContextGlobalSystem system: (optional) Built-in system properties
          that apply to all skills used by the assistant.
    :param str session_id: (optional) The session ID.
    """

    def __init__(
        self,
        *,
        system: Optional['MessageContextGlobalSystem'] = None,
        session_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageContextGlobal object.

        :param MessageContextGlobalSystem system: (optional) Built-in system
               properties that apply to all skills used by the assistant.
        """
        self.system = system
        self.session_id = session_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextGlobal':
        """Initialize a MessageContextGlobal object from a json dictionary."""
        args = {}
        if (system := _dict.get('system')) is not None:
            args['system'] = MessageContextGlobalSystem.from_dict(system)
        if (session_id := _dict.get('session_id')) is not None:
            args['session_id'] = session_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextGlobal object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'system') and self.system is not None:
            if isinstance(self.system, dict):
                _dict['system'] = self.system
            else:
                _dict['system'] = self.system.to_dict()
        if hasattr(self, 'session_id') and getattr(self,
                                                   'session_id') is not None:
            _dict['session_id'] = getattr(self, 'session_id')
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextGlobal object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextGlobal') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextGlobal') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextGlobalSystem:
    """
    Built-in system properties that apply to all skills used by the assistant.

    :param str timezone: (optional) The user time zone. The assistant uses the time
          zone to correctly resolve relative time references.
    :param str user_id: (optional) A string value that identifies the user who is
          interacting with the assistant. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property at the root of
          the message body. If **user_id** is specified in both locations in a message
          request, the value specified at the root is used.
    :param int turn_count: (optional) A counter that is automatically incremented
          with each turn of the conversation. A value of 1 indicates that this is the the
          first turn of a new conversation, which can affect the behavior of some skills
          (for example, triggering the start node of a dialog).
    :param str locale: (optional) The language code for localization in the user
          input. The specified locale overrides the default for the assistant, and is used
          for interpreting entity values in user input such as date values. For example,
          `04/03/2018` might be interpreted either as April 3 or March 4, depending on the
          locale.
           This property is included only if the new system entities are enabled for the
          skill.
    :param str reference_time: (optional) The base time for interpreting any
          relative time mentions in the user input. The specified time overrides the
          current server time, and is used to calculate times mentioned in relative terms
          such as `now` or `tomorrow`. This can be useful for simulating past or future
          times for testing purposes, or when analyzing documents such as news articles.
          This value must be a UTC time value formatted according to ISO 8601 (for
          example, `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
          This property is included only if the new system entities are enabled for the
          skill.
    :param str session_start_time: (optional) The time at which the session started.
          With the stateful `message` method, the start time is always present, and is set
          by the service based on the time the session was created. With the stateless
          `message` method, the start time is set by the service in the response to the
          first message, and should be returned as part of the context with each
          subsequent message in the session.
          This value is a UTC time value formatted according to ISO 8601 (for example,
          `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
    :param str state: (optional) An encoded string that represents the configuration
          state of the assistant at the beginning of the conversation. If you are using
          the stateless `message` method, save this value and then send it in the context
          of the subsequent message request to avoid disruptions if there are
          configuration changes during the conversation (such as a change to a skill the
          assistant uses).
    :param bool skip_user_input: (optional) For internal use only.
    """

    def __init__(
        self,
        *,
        timezone: Optional[str] = None,
        user_id: Optional[str] = None,
        turn_count: Optional[int] = None,
        locale: Optional[str] = None,
        reference_time: Optional[str] = None,
        session_start_time: Optional[str] = None,
        state: Optional[str] = None,
        skip_user_input: Optional[bool] = None,
    ) -> None:
        """
        Initialize a MessageContextGlobalSystem object.

        :param str timezone: (optional) The user time zone. The assistant uses the
               time zone to correctly resolve relative time references.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property at the root
               of the message body. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        :param int turn_count: (optional) A counter that is automatically
               incremented with each turn of the conversation. A value of 1 indicates that
               this is the the first turn of a new conversation, which can affect the
               behavior of some skills (for example, triggering the start node of a
               dialog).
        :param str locale: (optional) The language code for localization in the
               user input. The specified locale overrides the default for the assistant,
               and is used for interpreting entity values in user input such as date
               values. For example, `04/03/2018` might be interpreted either as April 3 or
               March 4, depending on the locale.
                This property is included only if the new system entities are enabled for
               the skill.
        :param str reference_time: (optional) The base time for interpreting any
               relative time mentions in the user input. The specified time overrides the
               current server time, and is used to calculate times mentioned in relative
               terms such as `now` or `tomorrow`. This can be useful for simulating past
               or future times for testing purposes, or when analyzing documents such as
               news articles.
               This value must be a UTC time value formatted according to ISO 8601 (for
               example, `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
               This property is included only if the new system entities are enabled for
               the skill.
        :param str session_start_time: (optional) The time at which the session
               started. With the stateful `message` method, the start time is always
               present, and is set by the service based on the time the session was
               created. With the stateless `message` method, the start time is set by the
               service in the response to the first message, and should be returned as
               part of the context with each subsequent message in the session.
               This value is a UTC time value formatted according to ISO 8601 (for
               example, `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
        :param str state: (optional) An encoded string that represents the
               configuration state of the assistant at the beginning of the conversation.
               If you are using the stateless `message` method, save this value and then
               send it in the context of the subsequent message request to avoid
               disruptions if there are configuration changes during the conversation
               (such as a change to a skill the assistant uses).
        :param bool skip_user_input: (optional) For internal use only.
        """
        self.timezone = timezone
        self.user_id = user_id
        self.turn_count = turn_count
        self.locale = locale
        self.reference_time = reference_time
        self.session_start_time = session_start_time
        self.state = state
        self.skip_user_input = skip_user_input

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextGlobalSystem':
        """Initialize a MessageContextGlobalSystem object from a json dictionary."""
        args = {}
        if (timezone := _dict.get('timezone')) is not None:
            args['timezone'] = timezone
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        if (turn_count := _dict.get('turn_count')) is not None:
            args['turn_count'] = turn_count
        if (locale := _dict.get('locale')) is not None:
            args['locale'] = locale
        if (reference_time := _dict.get('reference_time')) is not None:
            args['reference_time'] = reference_time
        if (session_start_time := _dict.get('session_start_time')) is not None:
            args['session_start_time'] = session_start_time
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        if (skip_user_input := _dict.get('skip_user_input')) is not None:
            args['skip_user_input'] = skip_user_input
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextGlobalSystem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'timezone') and self.timezone is not None:
            _dict['timezone'] = self.timezone
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'turn_count') and self.turn_count is not None:
            _dict['turn_count'] = self.turn_count
        if hasattr(self, 'locale') and self.locale is not None:
            _dict['locale'] = self.locale
        if hasattr(self, 'reference_time') and self.reference_time is not None:
            _dict['reference_time'] = self.reference_time
        if hasattr(
                self,
                'session_start_time') and self.session_start_time is not None:
            _dict['session_start_time'] = self.session_start_time
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self,
                   'skip_user_input') and self.skip_user_input is not None:
            _dict['skip_user_input'] = self.skip_user_input
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextGlobalSystem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextGlobalSystem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextGlobalSystem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LocaleEnum(str, Enum):
        """
        The language code for localization in the user input. The specified locale
        overrides the default for the assistant, and is used for interpreting entity
        values in user input such as date values. For example, `04/03/2018` might be
        interpreted either as April 3 or March 4, depending on the locale.
         This property is included only if the new system entities are enabled for the
        skill.
        """

        EN_US = 'en-us'
        EN_CA = 'en-ca'
        EN_GB = 'en-gb'
        AR_AR = 'ar-ar'
        CS_CZ = 'cs-cz'
        DE_DE = 'de-de'
        ES_ES = 'es-es'
        FR_FR = 'fr-fr'
        IT_IT = 'it-it'
        JA_JP = 'ja-jp'
        KO_KR = 'ko-kr'
        NL_NL = 'nl-nl'
        PT_BR = 'pt-br'
        ZH_CN = 'zh-cn'
        ZH_TW = 'zh-tw'


class MessageContextSkillSystem:
    """
    System context data used by the skill.

    :param str state: (optional) An encoded string that represents the current
          conversation state. By saving this value and then sending it in the context of a
          subsequent message request, you can return to an earlier point in the
          conversation. If you are using stateful sessions, you can also use a stored
          state value to restore a paused conversation whose session is expired.

    This type supports additional properties of type object. For internal use only.
    """

    # The set of defined properties for the class
    _properties = frozenset(['state'])

    def __init__(
        self,
        *,
        state: Optional[str] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a MessageContextSkillSystem object.

        :param str state: (optional) An encoded string that represents the current
               conversation state. By saving this value and then sending it in the context
               of a subsequent message request, you can return to an earlier point in the
               conversation. If you are using stateful sessions, you can also use a stored
               state value to restore a paused conversation whose session is expired.
        :param object **kwargs: (optional) For internal use only.
        """
        self.state = state
        for k, v in kwargs.items():
            if k not in MessageContextSkillSystem._properties:
                if not isinstance(v, object):
                    raise ValueError(
                        'Value for additional property {} must be of type object'
                        .format(k))
                setattr(self, k, v)
            else:
                raise ValueError(
                    'Property {} cannot be specified as an additional property'.
                    format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkillSystem':
        """Initialize a MessageContextSkillSystem object from a json dictionary."""
        args = {}
        if (state := _dict.get('state')) is not None:
            args['state'] = state
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, object):
                    raise ValueError(
                        'Value for additional property {} must be of type object'
                        .format(k))
                args[k] = v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextSkillSystem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageContextSkillSystem._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of MessageContextSkillSystem in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageContextSkillSystem._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of MessageContextSkillSystem"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageContextSkillSystem._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in MessageContextSkillSystem._properties:
                if not isinstance(v, object):
                    raise ValueError(
                        'Value for additional property {} must be of type object'
                        .format(k))
                setattr(self, k, v)
            else:
                raise ValueError(
                    'Property {} cannot be specified as an additional property'.
                    format(k))

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextSkillSystem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextSkillSystem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextSkillSystem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextSkills:
    """
    Context data specific to particular skills used by the assistant.

    :param MessageContextDialogSkill main_skill: (optional) Context variables that
          are used by the dialog skill.
    :param MessageContextActionSkill actions_skill: (optional) Context variables
          that are used by the action skill. Private variables are persisted, but not
          shown.
    """

    def __init__(
        self,
        *,
        main_skill: Optional['MessageContextDialogSkill'] = None,
        actions_skill: Optional['MessageContextActionSkill'] = None,
    ) -> None:
        """
        Initialize a MessageContextSkills object.

        :param MessageContextDialogSkill main_skill: (optional) Context variables
               that are used by the dialog skill.
        :param MessageContextActionSkill actions_skill: (optional) Context
               variables that are used by the action skill. Private variables are
               persisted, but not shown.
        """
        self.main_skill = main_skill
        self.actions_skill = actions_skill

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkills':
        """Initialize a MessageContextSkills object from a json dictionary."""
        args = {}
        if (main_skill := _dict.get('main skill')) is not None:
            args['main_skill'] = MessageContextDialogSkill.from_dict(main_skill)
        if (actions_skill := _dict.get('actions skill')) is not None:
            args['actions_skill'] = MessageContextActionSkill.from_dict(
                actions_skill)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextSkills object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'main_skill') and self.main_skill is not None:
            if isinstance(self.main_skill, dict):
                _dict['main skill'] = self.main_skill
            else:
                _dict['main skill'] = self.main_skill.to_dict()
        if hasattr(self, 'actions_skill') and self.actions_skill is not None:
            if isinstance(self.actions_skill, dict):
                _dict['actions skill'] = self.actions_skill
            else:
                _dict['actions skill'] = self.actions_skill.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextSkills object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextSkills') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextSkills') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInput:
    """
    An input object that includes the input text.

    :param str message_type: (optional) The type of the message:
          - `text`: The user input is processed normally by the assistant.
          - `search`: Only search results are returned. (Any dialog or action skill is
          bypassed.)
          **Note:** A `search` message results in an error if no search skill is
          configured for the assistant.
    :param str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :param List[RuntimeIntent] intents: (optional) Intents to use when evaluating
          the user input. Include intents from the previous response to continue using
          those intents rather than trying to recognize intents in the new input.
    :param List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :param str suggestion_id: (optional) For internal use only.
    :param List[MessageInputAttachment] attachments: (optional) An array of
          multimedia attachments to be sent with the message. Attachments are not
          processed by the assistant itself, but can be sent to external services by
          webhooks.
           **Note:** Attachments are not supported on IBM Cloud Pak for Data.
    :param RequestAnalytics analytics: (optional) An optional object containing
          analytics data. Currently, this data is used only for events sent to the Segment
          extension.
    :param MessageInputOptions options: (optional) Optional properties that control
          how the assistant responds.
    """

    def __init__(
        self,
        *,
        message_type: Optional[str] = None,
        text: Optional[str] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        suggestion_id: Optional[str] = None,
        attachments: Optional[List['MessageInputAttachment']] = None,
        analytics: Optional['RequestAnalytics'] = None,
        options: Optional['MessageInputOptions'] = None,
    ) -> None:
        """
        Initialize a MessageInput object.

        :param str message_type: (optional) The type of the message:
               - `text`: The user input is processed normally by the assistant.
               - `search`: Only search results are returned. (Any dialog or action skill
               is bypassed.)
               **Note:** A `search` message results in an error if no search skill is
               configured for the assistant.
        :param str text: (optional) The text of the user input. This string cannot
               contain carriage return, newline, or tab characters.
        :param List[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param List[RuntimeEntity] entities: (optional) Entities to use when
               evaluating the message. Include entities from the previous response to
               continue using those entities rather than detecting entities in the new
               input.
        :param str suggestion_id: (optional) For internal use only.
        :param List[MessageInputAttachment] attachments: (optional) An array of
               multimedia attachments to be sent with the message. Attachments are not
               processed by the assistant itself, but can be sent to external services by
               webhooks.
                **Note:** Attachments are not supported on IBM Cloud Pak for Data.
        :param RequestAnalytics analytics: (optional) An optional object containing
               analytics data. Currently, this data is used only for events sent to the
               Segment extension.
        :param MessageInputOptions options: (optional) Optional properties that
               control how the assistant responds.
        """
        self.message_type = message_type
        self.text = text
        self.intents = intents
        self.entities = entities
        self.suggestion_id = suggestion_id
        self.attachments = attachments
        self.analytics = analytics
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInput':
        """Initialize a MessageInput object from a json dictionary."""
        args = {}
        if (message_type := _dict.get('message_type')) is not None:
            args['message_type'] = message_type
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (suggestion_id := _dict.get('suggestion_id')) is not None:
            args['suggestion_id'] = suggestion_id
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = [
                MessageInputAttachment.from_dict(v) for v in attachments
            ]
        if (analytics := _dict.get('analytics')) is not None:
            args['analytics'] = RequestAnalytics.from_dict(analytics)
        if (options := _dict.get('options')) is not None:
            args['options'] = MessageInputOptions.from_dict(options)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message_type') and self.message_type is not None:
            _dict['message_type'] = self.message_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'suggestion_id') and self.suggestion_id is not None:
            _dict['suggestion_id'] = self.suggestion_id
        if hasattr(self, 'attachments') and self.attachments is not None:
            attachments_list = []
            for v in self.attachments:
                if isinstance(v, dict):
                    attachments_list.append(v)
                else:
                    attachments_list.append(v.to_dict())
            _dict['attachments'] = attachments_list
        if hasattr(self, 'analytics') and self.analytics is not None:
            if isinstance(self.analytics, dict):
                _dict['analytics'] = self.analytics
            else:
                _dict['analytics'] = self.analytics.to_dict()
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MessageTypeEnum(str, Enum):
        """
        The type of the message:
        - `text`: The user input is processed normally by the assistant.
        - `search`: Only search results are returned. (Any dialog or action skill is
        bypassed.)
        **Note:** A `search` message results in an error if no search skill is configured
        for the assistant.
        """

        TEXT = 'text'
        SEARCH = 'search'


class MessageInputAttachment:
    """
    A reference to a media file to be sent as an attachment with the message.

    :param str url: The URL of the media file.
    :param str media_type: (optional) The media content type (such as a MIME type)
          of the attachment.
    """

    def __init__(
        self,
        url: str,
        *,
        media_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageInputAttachment object.

        :param str url: The URL of the media file.
        :param str media_type: (optional) The media content type (such as a MIME
               type) of the attachment.
        """
        self.url = url
        self.media_type = media_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInputAttachment':
        """Initialize a MessageInputAttachment object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in MessageInputAttachment JSON'
            )
        if (media_type := _dict.get('media_type')) is not None:
            args['media_type'] = media_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInputAttachment object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'media_type') and self.media_type is not None:
            _dict['media_type'] = self.media_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageInputAttachment object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInputAttachment') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInputAttachment') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInputOptions:
    """
    Optional properties that control how the assistant responds.

    :param bool restart: (optional) Whether to restart dialog processing at the root
          of the dialog, regardless of any previously visited nodes. **Note:** This does
          not affect `turn_count` or any other context variables.
    :param bool alternate_intents: (optional) Whether to return more than one
          intent. Set to `true` to return all matching intents.
    :param bool async_callout: (optional) Whether custom extension callouts are
          executed asynchronously. Asynchronous execution means the response to the
          extension callout will be processed on the subsequent message call, the initial
          message response signals to the client that the operation may be long running.
          With synchronous execution the custom extension is executed and returns the
          response in a single message turn. **Note:** **async_callout** defaults to true
          for API versions earlier than 2023-06-15.
    :param MessageInputOptionsSpelling spelling: (optional) Spelling correction
          options for the message. Any options specified on an individual message override
          the settings configured for the skill.
    :param bool debug: (optional) Whether to return additional diagnostic
          information. Set to `true` to return additional information in the
          `output.debug` property. If you also specify **return_context**=`true`, the
          returned skill context includes the `system.state` property.
    :param bool return_context: (optional) Whether to return session context with
          the response. If you specify `true`, the response includes the `context`
          property. If you also specify **debug**=`true`, the returned skill context
          includes the `system.state` property.
    :param bool export: (optional) Whether to return session context, including full
          conversation state. If you specify `true`, the response includes the `context`
          property, and the skill context includes the `system.state` property.
          **Note:** If **export**=`true`, the context is returned regardless of the value
          of **return_context**.
    """

    def __init__(
        self,
        *,
        restart: Optional[bool] = None,
        alternate_intents: Optional[bool] = None,
        async_callout: Optional[bool] = None,
        spelling: Optional['MessageInputOptionsSpelling'] = None,
        debug: Optional[bool] = None,
        return_context: Optional[bool] = None,
        export: Optional[bool] = None,
    ) -> None:
        """
        Initialize a MessageInputOptions object.

        :param bool restart: (optional) Whether to restart dialog processing at the
               root of the dialog, regardless of any previously visited nodes. **Note:**
               This does not affect `turn_count` or any other context variables.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. Set to `true` to return all matching intents.
        :param bool async_callout: (optional) Whether custom extension callouts are
               executed asynchronously. Asynchronous execution means the response to the
               extension callout will be processed on the subsequent message call, the
               initial message response signals to the client that the operation may be
               long running. With synchronous execution the custom extension is executed
               and returns the response in a single message turn. **Note:**
               **async_callout** defaults to true for API versions earlier than
               2023-06-15.
        :param MessageInputOptionsSpelling spelling: (optional) Spelling correction
               options for the message. Any options specified on an individual message
               override the settings configured for the skill.
        :param bool debug: (optional) Whether to return additional diagnostic
               information. Set to `true` to return additional information in the
               `output.debug` property. If you also specify **return_context**=`true`, the
               returned skill context includes the `system.state` property.
        :param bool return_context: (optional) Whether to return session context
               with the response. If you specify `true`, the response includes the
               `context` property. If you also specify **debug**=`true`, the returned
               skill context includes the `system.state` property.
        :param bool export: (optional) Whether to return session context, including
               full conversation state. If you specify `true`, the response includes the
               `context` property, and the skill context includes the `system.state`
               property.
               **Note:** If **export**=`true`, the context is returned regardless of the
               value of **return_context**.
        """
        self.restart = restart
        self.alternate_intents = alternate_intents
        self.async_callout = async_callout
        self.spelling = spelling
        self.debug = debug
        self.return_context = return_context
        self.export = export

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInputOptions':
        """Initialize a MessageInputOptions object from a json dictionary."""
        args = {}
        if (restart := _dict.get('restart')) is not None:
            args['restart'] = restart
        if (alternate_intents := _dict.get('alternate_intents')) is not None:
            args['alternate_intents'] = alternate_intents
        if (async_callout := _dict.get('async_callout')) is not None:
            args['async_callout'] = async_callout
        if (spelling := _dict.get('spelling')) is not None:
            args['spelling'] = MessageInputOptionsSpelling.from_dict(spelling)
        if (debug := _dict.get('debug')) is not None:
            args['debug'] = debug
        if (return_context := _dict.get('return_context')) is not None:
            args['return_context'] = return_context
        if (export := _dict.get('export')) is not None:
            args['export'] = export
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInputOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'restart') and self.restart is not None:
            _dict['restart'] = self.restart
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'async_callout') and self.async_callout is not None:
            _dict['async_callout'] = self.async_callout
        if hasattr(self, 'spelling') and self.spelling is not None:
            if isinstance(self.spelling, dict):
                _dict['spelling'] = self.spelling
            else:
                _dict['spelling'] = self.spelling.to_dict()
        if hasattr(self, 'debug') and self.debug is not None:
            _dict['debug'] = self.debug
        if hasattr(self, 'return_context') and self.return_context is not None:
            _dict['return_context'] = self.return_context
        if hasattr(self, 'export') and self.export is not None:
            _dict['export'] = self.export
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageInputOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInputOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInputOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInputOptionsSpelling:
    """
    Spelling correction options for the message. Any options specified on an individual
    message override the settings configured for the skill.

    :param bool suggestions: (optional) Whether to use spelling correction when
          processing the input. If spelling correction is used and **auto_correct** is
          `true`, any spelling corrections are automatically applied to the user input. If
          **auto_correct** is `false`, any suggested corrections are returned in the
          **output.spelling** property.
          This property overrides the value of the **spelling_suggestions** property in
          the workspace settings for the skill.
    :param bool auto_correct: (optional) Whether to use autocorrection when
          processing the input. If this property is `true`, any corrections are
          automatically applied to the user input, and the original text is returned in
          the **output.spelling** property of the message response. This property
          overrides the value of the **spelling_auto_correct** property in the workspace
          settings for the skill.
    """

    def __init__(
        self,
        *,
        suggestions: Optional[bool] = None,
        auto_correct: Optional[bool] = None,
    ) -> None:
        """
        Initialize a MessageInputOptionsSpelling object.

        :param bool suggestions: (optional) Whether to use spelling correction when
               processing the input. If spelling correction is used and **auto_correct**
               is `true`, any spelling corrections are automatically applied to the user
               input. If **auto_correct** is `false`, any suggested corrections are
               returned in the **output.spelling** property.
               This property overrides the value of the **spelling_suggestions** property
               in the workspace settings for the skill.
        :param bool auto_correct: (optional) Whether to use autocorrection when
               processing the input. If this property is `true`, any corrections are
               automatically applied to the user input, and the original text is returned
               in the **output.spelling** property of the message response. This property
               overrides the value of the **spelling_auto_correct** property in the
               workspace settings for the skill.
        """
        self.suggestions = suggestions
        self.auto_correct = auto_correct

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInputOptionsSpelling':
        """Initialize a MessageInputOptionsSpelling object from a json dictionary."""
        args = {}
        if (suggestions := _dict.get('suggestions')) is not None:
            args['suggestions'] = suggestions
        if (auto_correct := _dict.get('auto_correct')) is not None:
            args['auto_correct'] = auto_correct
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInputOptionsSpelling object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'suggestions') and self.suggestions is not None:
            _dict['suggestions'] = self.suggestions
        if hasattr(self, 'auto_correct') and self.auto_correct is not None:
            _dict['auto_correct'] = self.auto_correct
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageInputOptionsSpelling object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInputOptionsSpelling') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInputOptionsSpelling') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutput:
    """
    Assistant output to be rendered or processed by the client.

    :param List[RuntimeResponseGeneric] generic: (optional) Output intended for any
          channel. It is the responsibility of the client application to implement the
          supported response types.
    :param List[RuntimeIntent] intents: (optional) An array of intents recognized in
          the user input, sorted in descending order of confidence.
    :param List[RuntimeEntity] entities: (optional) An array of entities identified
          in the user input.
    :param List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    :param MessageOutputDebug debug: (optional) Additional detailed information
          about a message response and how it was generated.
    :param dict user_defined: (optional) An object containing any custom properties
          included in the response. This object includes any arbitrary properties defined
          in the dialog JSON editor as part of the dialog node output.
    :param MessageOutputSpelling spelling: (optional) Properties describing any
          spelling corrections in the user input that was received.
    """

    def __init__(
        self,
        *,
        generic: Optional[List['RuntimeResponseGeneric']] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        actions: Optional[List['DialogNodeAction']] = None,
        debug: Optional['MessageOutputDebug'] = None,
        user_defined: Optional[dict] = None,
        spelling: Optional['MessageOutputSpelling'] = None,
    ) -> None:
        """
        Initialize a MessageOutput object.

        :param List[RuntimeResponseGeneric] generic: (optional) Output intended for
               any channel. It is the responsibility of the client application to
               implement the supported response types.
        :param List[RuntimeIntent] intents: (optional) An array of intents
               recognized in the user input, sorted in descending order of confidence.
        :param List[RuntimeEntity] entities: (optional) An array of entities
               identified in the user input.
        :param List[DialogNodeAction] actions: (optional) An array of objects
               describing any actions requested by the dialog node.
        :param MessageOutputDebug debug: (optional) Additional detailed information
               about a message response and how it was generated.
        :param dict user_defined: (optional) An object containing any custom
               properties included in the response. This object includes any arbitrary
               properties defined in the dialog JSON editor as part of the dialog node
               output.
        :param MessageOutputSpelling spelling: (optional) Properties describing any
               spelling corrections in the user input that was received.
        """
        self.generic = generic
        self.intents = intents
        self.entities = entities
        self.actions = actions
        self.debug = debug
        self.user_defined = user_defined
        self.spelling = spelling

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageOutput':
        """Initialize a MessageOutput object from a json dictionary."""
        args = {}
        if (generic := _dict.get('generic')) is not None:
            args['generic'] = [
                RuntimeResponseGeneric.from_dict(v) for v in generic
            ]
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (actions := _dict.get('actions')) is not None:
            args['actions'] = [DialogNodeAction.from_dict(v) for v in actions]
        if (debug := _dict.get('debug')) is not None:
            args['debug'] = MessageOutputDebug.from_dict(debug)
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        if (spelling := _dict.get('spelling')) is not None:
            args['spelling'] = MessageOutputSpelling.from_dict(spelling)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'generic') and self.generic is not None:
            generic_list = []
            for v in self.generic:
                if isinstance(v, dict):
                    generic_list.append(v)
                else:
                    generic_list.append(v.to_dict())
            _dict['generic'] = generic_list
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'actions') and self.actions is not None:
            actions_list = []
            for v in self.actions:
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
        if hasattr(self, 'debug') and self.debug is not None:
            if isinstance(self.debug, dict):
                _dict['debug'] = self.debug
            else:
                _dict['debug'] = self.debug.to_dict()
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'spelling') and self.spelling is not None:
            if isinstance(self.spelling, dict):
                _dict['spelling'] = self.spelling
            else:
                _dict['spelling'] = self.spelling.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageOutput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageOutput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutputDebug:
    """
    Additional detailed information about a message response and how it was generated.

    :param List[DialogNodeVisited] nodes_visited: (optional) An array of objects
          containing detailed diagnostic information about dialog nodes that were visited
          during processing of the input message.
    :param List[DialogLogMessage] log_messages: (optional) An array of up to 50
          messages logged with the request.
    :param bool branch_exited: (optional) Assistant sets this to true when this
          message response concludes or interrupts a dialog.
    :param str branch_exited_reason: (optional) When `branch_exited` is set to
          `true` by the assistant, the `branch_exited_reason` specifies whether the dialog
          completed by itself or got interrupted.
    :param List[MessageOutputDebugTurnEvent] turn_events: (optional) An array of
          objects containing detailed diagnostic information about dialog nodes and
          actions that were visited during processing of the input message.
          This property is present only if the assistant has an action skill.
    """

    def __init__(
        self,
        *,
        nodes_visited: Optional[List['DialogNodeVisited']] = None,
        log_messages: Optional[List['DialogLogMessage']] = None,
        branch_exited: Optional[bool] = None,
        branch_exited_reason: Optional[str] = None,
        turn_events: Optional[List['MessageOutputDebugTurnEvent']] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebug object.

        :param List[DialogNodeVisited] nodes_visited: (optional) An array of
               objects containing detailed diagnostic information about dialog nodes that
               were visited during processing of the input message.
        :param List[DialogLogMessage] log_messages: (optional) An array of up to 50
               messages logged with the request.
        :param bool branch_exited: (optional) Assistant sets this to true when this
               message response concludes or interrupts a dialog.
        :param str branch_exited_reason: (optional) When `branch_exited` is set to
               `true` by the assistant, the `branch_exited_reason` specifies whether the
               dialog completed by itself or got interrupted.
        :param List[MessageOutputDebugTurnEvent] turn_events: (optional) An array
               of objects containing detailed diagnostic information about dialog nodes
               and actions that were visited during processing of the input message.
               This property is present only if the assistant has an action skill.
        """
        self.nodes_visited = nodes_visited
        self.log_messages = log_messages
        self.branch_exited = branch_exited
        self.branch_exited_reason = branch_exited_reason
        self.turn_events = turn_events

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageOutputDebug':
        """Initialize a MessageOutputDebug object from a json dictionary."""
        args = {}
        if (nodes_visited := _dict.get('nodes_visited')) is not None:
            args['nodes_visited'] = [
                DialogNodeVisited.from_dict(v) for v in nodes_visited
            ]
        if (log_messages := _dict.get('log_messages')) is not None:
            args['log_messages'] = [
                DialogLogMessage.from_dict(v) for v in log_messages
            ]
        if (branch_exited := _dict.get('branch_exited')) is not None:
            args['branch_exited'] = branch_exited
        if (branch_exited_reason :=
                _dict.get('branch_exited_reason')) is not None:
            args['branch_exited_reason'] = branch_exited_reason
        if (turn_events := _dict.get('turn_events')) is not None:
            args['turn_events'] = [
                MessageOutputDebugTurnEvent.from_dict(v) for v in turn_events
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebug object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nodes_visited') and self.nodes_visited is not None:
            nodes_visited_list = []
            for v in self.nodes_visited:
                if isinstance(v, dict):
                    nodes_visited_list.append(v)
                else:
                    nodes_visited_list.append(v.to_dict())
            _dict['nodes_visited'] = nodes_visited_list
        if hasattr(self, 'log_messages') and self.log_messages is not None:
            log_messages_list = []
            for v in self.log_messages:
                if isinstance(v, dict):
                    log_messages_list.append(v)
                else:
                    log_messages_list.append(v.to_dict())
            _dict['log_messages'] = log_messages_list
        if hasattr(self, 'branch_exited') and self.branch_exited is not None:
            _dict['branch_exited'] = self.branch_exited
        if hasattr(self, 'branch_exited_reason'
                  ) and self.branch_exited_reason is not None:
            _dict['branch_exited_reason'] = self.branch_exited_reason
        if hasattr(self, 'turn_events') and self.turn_events is not None:
            turn_events_list = []
            for v in self.turn_events:
                if isinstance(v, dict):
                    turn_events_list.append(v)
                else:
                    turn_events_list.append(v.to_dict())
            _dict['turn_events'] = turn_events_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebug object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageOutputDebug') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageOutputDebug') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class BranchExitedReasonEnum(str, Enum):
        """
        When `branch_exited` is set to `true` by the assistant, the `branch_exited_reason`
        specifies whether the dialog completed by itself or got interrupted.
        """

        COMPLETED = 'completed'
        FALLBACK = 'fallback'


class MessageOutputDebugTurnEvent:
    """
    MessageOutputDebugTurnEvent.

    """

    def __init__(self,) -> None:
        """
        Initialize a MessageOutputDebugTurnEvent object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'MessageOutputDebugTurnEventTurnEventActionVisited',
                'MessageOutputDebugTurnEventTurnEventActionFinished',
                'MessageOutputDebugTurnEventTurnEventStepVisited',
                'MessageOutputDebugTurnEventTurnEventStepAnswered',
                'MessageOutputDebugTurnEventTurnEventHandlerVisited',
                'MessageOutputDebugTurnEventTurnEventCallout',
                'MessageOutputDebugTurnEventTurnEventSearch',
                'MessageOutputDebugTurnEventTurnEventNodeVisited'
            ]))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageOutputDebugTurnEvent':
        """Initialize a MessageOutputDebugTurnEvent object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'MessageOutputDebugTurnEvent'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join([
                'MessageOutputDebugTurnEventTurnEventActionVisited',
                'MessageOutputDebugTurnEventTurnEventActionFinished',
                'MessageOutputDebugTurnEventTurnEventStepVisited',
                'MessageOutputDebugTurnEventTurnEventStepAnswered',
                'MessageOutputDebugTurnEventTurnEventHandlerVisited',
                'MessageOutputDebugTurnEventTurnEventCallout',
                'MessageOutputDebugTurnEventTurnEventSearch',
                'MessageOutputDebugTurnEventTurnEventNodeVisited'
            ]))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a MessageOutputDebugTurnEvent object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping[
            'action_visited'] = 'MessageOutputDebugTurnEventTurnEventActionVisited'
        mapping[
            'action_finished'] = 'MessageOutputDebugTurnEventTurnEventActionFinished'
        mapping[
            'step_visited'] = 'MessageOutputDebugTurnEventTurnEventStepVisited'
        mapping[
            'step_answered'] = 'MessageOutputDebugTurnEventTurnEventStepAnswered'
        mapping[
            'handler_visited'] = 'MessageOutputDebugTurnEventTurnEventHandlerVisited'
        mapping['callout'] = 'MessageOutputDebugTurnEventTurnEventCallout'
        mapping['search'] = 'MessageOutputDebugTurnEventTurnEventSearch'
        mapping[
            'node_visited'] = 'MessageOutputDebugTurnEventTurnEventNodeVisited'
        disc_value = _dict.get('event')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'event\' not found in MessageOutputDebugTurnEvent JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class MessageOutputSpelling:
    """
    Properties describing any spelling corrections in the user input that was received.

    :param str text: (optional) The user input text that was used to generate the
          response. If spelling autocorrection is enabled, this text reflects any spelling
          corrections that were applied.
    :param str original_text: (optional) The original user input text. This property
          is returned only if autocorrection is enabled and the user input was corrected.
    :param str suggested_text: (optional) Any suggested corrections of the input
          text. This property is returned only if spelling correction is enabled and
          autocorrection is disabled.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        original_text: Optional[str] = None,
        suggested_text: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageOutputSpelling object.

        :param str text: (optional) The user input text that was used to generate
               the response. If spelling autocorrection is enabled, this text reflects any
               spelling corrections that were applied.
        :param str original_text: (optional) The original user input text. This
               property is returned only if autocorrection is enabled and the user input
               was corrected.
        :param str suggested_text: (optional) Any suggested corrections of the
               input text. This property is returned only if spelling correction is
               enabled and autocorrection is disabled.
        """
        self.text = text
        self.original_text = original_text
        self.suggested_text = suggested_text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageOutputSpelling':
        """Initialize a MessageOutputSpelling object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (original_text := _dict.get('original_text')) is not None:
            args['original_text'] = original_text
        if (suggested_text := _dict.get('suggested_text')) is not None:
            args['suggested_text'] = suggested_text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputSpelling object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'original_text') and self.original_text is not None:
            _dict['original_text'] = self.original_text
        if hasattr(self, 'suggested_text') and self.suggested_text is not None:
            _dict['suggested_text'] = self.suggested_text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputSpelling object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageOutputSpelling') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageOutputSpelling') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Metadata:
    """
    Contains meta-information about the item(s) being streamed.

    :param int id: (optional) Identifies the index and sequence of the current
          streamed response item.
    """

    def __init__(
        self,
        *,
        id: Optional[int] = None,
    ) -> None:
        """
        Initialize a Metadata object.

        :param int id: (optional) Identifies the index and sequence of the current
               streamed response item.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Metadata':
        """Initialize a Metadata object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Metadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Metadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Metadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Metadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MonitorAssistantReleaseImportArtifactResponse:
    """
    MonitorAssistantReleaseImportArtifactResponse.

    :param str status: (optional) The current status of the release import process:
           - **Completed**: The artifact import has completed.
           - **Failed**: The asynchronous artifact import process has failed.
           - **Processing**: An asynchronous operation to import the artifact is underway
          and not yet completed.
    :param str task_id: (optional) A unique identifier for a background asynchronous
          task that is executing or has executed the operation.
    :param str assistant_id: (optional) The ID of the assistant to which the release
          belongs.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :param str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :param List[str] skill_impact_in_draft: (optional) An array of skill types in
          the draft environment which will be overridden with skills from the artifact
          being imported.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        *,
        status: Optional[str] = None,
        task_id: Optional[str] = None,
        assistant_id: Optional[str] = None,
        status_errors: Optional[List['StatusError']] = None,
        status_description: Optional[str] = None,
        skill_impact_in_draft: Optional[List[str]] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a MonitorAssistantReleaseImportArtifactResponse object.

        :param List[str] skill_impact_in_draft: (optional) An array of skill types
               in the draft environment which will be overridden with skills from the
               artifact being imported.
        """
        self.status = status
        self.task_id = task_id
        self.assistant_id = assistant_id
        self.status_errors = status_errors
        self.status_description = status_description
        self.skill_impact_in_draft = skill_impact_in_draft
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'MonitorAssistantReleaseImportArtifactResponse':
        """Initialize a MonitorAssistantReleaseImportArtifactResponse object from a json dictionary."""
        args = {}
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (task_id := _dict.get('task_id')) is not None:
            args['task_id'] = task_id
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        if (status_description := _dict.get('status_description')) is not None:
            args['status_description'] = status_description
        if (skill_impact_in_draft :=
                _dict.get('skill_impact_in_draft')) is not None:
            args['skill_impact_in_draft'] = skill_impact_in_draft
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MonitorAssistantReleaseImportArtifactResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'task_id') and getattr(self, 'task_id') is not None:
            _dict['task_id'] = getattr(self, 'task_id')
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'status_errors') and getattr(
                self, 'status_errors') is not None:
            status_errors_list = []
            for v in getattr(self, 'status_errors'):
                if isinstance(v, dict):
                    status_errors_list.append(v)
                else:
                    status_errors_list.append(v.to_dict())
            _dict['status_errors'] = status_errors_list
        if hasattr(self, 'status_description') and getattr(
                self, 'status_description') is not None:
            _dict['status_description'] = getattr(self, 'status_description')
        if hasattr(self, 'skill_impact_in_draft'
                  ) and self.skill_impact_in_draft is not None:
            _dict['skill_impact_in_draft'] = self.skill_impact_in_draft
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MonitorAssistantReleaseImportArtifactResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'MonitorAssistantReleaseImportArtifactResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'MonitorAssistantReleaseImportArtifactResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the release import process:
         - **Completed**: The artifact import has completed.
         - **Failed**: The asynchronous artifact import process has failed.
         - **Processing**: An asynchronous operation to import the artifact is underway
        and not yet completed.
        """

        COMPLETED = 'Completed'
        FAILED = 'Failed'
        PROCESSING = 'Processing'

    class SkillImpactInDraftEnum(str, Enum):
        """
        The type of the skill in the draft environment.
        """

        ACTION = 'action'
        DIALOG = 'dialog'


class Pagination:
    """
    The pagination data for the returned objects. For more information about using
    pagination, see [Pagination](#pagination).

    :param str refresh_url: The URL that will return the same page of results.
    :param str next_url: (optional) The URL that will return the next page of
          results.
    :param int total: (optional) The total number of objects that satisfy the
          request. This total includes all results, not just those included in the current
          page.
    :param int matched: (optional) Reserved for future use.
    :param str refresh_cursor: (optional) A token identifying the current page of
          results.
    :param str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(
        self,
        refresh_url: str,
        *,
        next_url: Optional[str] = None,
        total: Optional[int] = None,
        matched: Optional[int] = None,
        refresh_cursor: Optional[str] = None,
        next_cursor: Optional[str] = None,
    ) -> None:
        """
        Initialize a Pagination object.

        :param str refresh_url: The URL that will return the same page of results.
        :param str next_url: (optional) The URL that will return the next page of
               results.
        :param int total: (optional) The total number of objects that satisfy the
               request. This total includes all results, not just those included in the
               current page.
        :param int matched: (optional) Reserved for future use.
        :param str refresh_cursor: (optional) A token identifying the current page
               of results.
        :param str next_cursor: (optional) A token identifying the next page of
               results.
        """
        self.refresh_url = refresh_url
        self.next_url = next_url
        self.total = total
        self.matched = matched
        self.refresh_cursor = refresh_cursor
        self.next_cursor = next_cursor

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Pagination':
        """Initialize a Pagination object from a json dictionary."""
        args = {}
        if (refresh_url := _dict.get('refresh_url')) is not None:
            args['refresh_url'] = refresh_url
        else:
            raise ValueError(
                'Required property \'refresh_url\' not present in Pagination JSON'
            )
        if (next_url := _dict.get('next_url')) is not None:
            args['next_url'] = next_url
        if (total := _dict.get('total')) is not None:
            args['total'] = total
        if (matched := _dict.get('matched')) is not None:
            args['matched'] = matched
        if (refresh_cursor := _dict.get('refresh_cursor')) is not None:
            args['refresh_cursor'] = refresh_cursor
        if (next_cursor := _dict.get('next_cursor')) is not None:
            args['next_cursor'] = next_cursor
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Pagination object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'refresh_url') and self.refresh_url is not None:
            _dict['refresh_url'] = self.refresh_url
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'total') and self.total is not None:
            _dict['total'] = self.total
        if hasattr(self, 'matched') and self.matched is not None:
            _dict['matched'] = self.matched
        if hasattr(self, 'refresh_cursor') and self.refresh_cursor is not None:
            _dict['refresh_cursor'] = self.refresh_cursor
        if hasattr(self, 'next_cursor') and self.next_cursor is not None:
            _dict['next_cursor'] = self.next_cursor
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Pagination object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Pagination') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Pagination') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderAuthenticationOAuth2:
    """
    Non-private settings for oauth2 authentication.

    :param str preferred_flow: (optional) The preferred "flow" or "grant type" for
          the API client to fetch an access token from the authorization server.
    :param ProviderAuthenticationOAuth2Flows flows: (optional) Scenarios performed
          by the API client to fetch an access token from the authorization server.
    """

    def __init__(
        self,
        *,
        preferred_flow: Optional[str] = None,
        flows: Optional['ProviderAuthenticationOAuth2Flows'] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2 object.

        :param str preferred_flow: (optional) The preferred "flow" or "grant type"
               for the API client to fetch an access token from the authorization server.
        :param ProviderAuthenticationOAuth2Flows flows: (optional) Scenarios
               performed by the API client to fetch an access token from the authorization
               server.
        """
        self.preferred_flow = preferred_flow
        self.flows = flows

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderAuthenticationOAuth2':
        """Initialize a ProviderAuthenticationOAuth2 object from a json dictionary."""
        args = {}
        if (preferred_flow := _dict.get('preferred_flow')) is not None:
            args['preferred_flow'] = preferred_flow
        if (flows := _dict.get('flows')) is not None:
            args['flows'] = flows
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationOAuth2 object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'preferred_flow') and self.preferred_flow is not None:
            _dict['preferred_flow'] = self.preferred_flow
        if hasattr(self, 'flows') and self.flows is not None:
            if isinstance(self.flows, dict):
                _dict['flows'] = self.flows
            else:
                _dict['flows'] = self.flows.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationOAuth2 object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderAuthenticationOAuth2') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderAuthenticationOAuth2') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PreferredFlowEnum(str, Enum):
        """
        The preferred "flow" or "grant type" for the API client to fetch an access token
        from the authorization server.
        """

        PASSWORD = 'password'
        CLIENT_CREDENTIALS = 'client_credentials'
        AUTHORIZATION_CODE = 'authorization_code'
        CUSTOM_FLOW_NAME = '<$custom_flow_name>'


class ProviderAuthenticationOAuth2Flows:
    """
    Scenarios performed by the API client to fetch an access token from the authorization
    server.

    """

    def __init__(self,) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2Flows object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password',
                'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials',
                'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode'
            ]))
        raise Exception(msg)


class ProviderAuthenticationOAuth2PasswordUsername:
    """
    The username for oauth2 authentication when the preferred flow is "password".

    :param str type: (optional) The type of property observed in "value".
    :param str value: (optional) The stored information of the value.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2PasswordUsername object.

        :param str type: (optional) The type of property observed in "value".
        :param str value: (optional) The stored information of the value.
        """
        self.type = type
        self.value = value

    @classmethod
    def from_dict(
            cls, _dict: Dict) -> 'ProviderAuthenticationOAuth2PasswordUsername':
        """Initialize a ProviderAuthenticationOAuth2PasswordUsername object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationOAuth2PasswordUsername object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationOAuth2PasswordUsername object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'ProviderAuthenticationOAuth2PasswordUsername') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'ProviderAuthenticationOAuth2PasswordUsername') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of property observed in "value".
        """

        VALUE = 'value'


class ProviderAuthenticationTypeAndValue:
    """
    ProviderAuthenticationTypeAndValue.

    :param str type: (optional) The type of property observed in "value".
    :param str value: (optional) The stored information of the value.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationTypeAndValue object.

        :param str type: (optional) The type of property observed in "value".
        :param str value: (optional) The stored information of the value.
        """
        self.type = type
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderAuthenticationTypeAndValue':
        """Initialize a ProviderAuthenticationTypeAndValue object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationTypeAndValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationTypeAndValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderAuthenticationTypeAndValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderAuthenticationTypeAndValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of property observed in "value".
        """

        VALUE = 'value'


class ProviderCollection:
    """
    ProviderCollection.

    :param List[ProviderResponse] conversational_skill_providers: An array of
          objects describing the conversational skill providers associated with the
          instance.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        conversational_skill_providers: List['ProviderResponse'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a ProviderCollection object.

        :param List[ProviderResponse] conversational_skill_providers: An array of
               objects describing the conversational skill providers associated with the
               instance.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.conversational_skill_providers = conversational_skill_providers
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderCollection':
        """Initialize a ProviderCollection object from a json dictionary."""
        args = {}
        if (conversational_skill_providers :=
                _dict.get('conversational_skill_providers')) is not None:
            args['conversational_skill_providers'] = [
                ProviderResponse.from_dict(v)
                for v in conversational_skill_providers
            ]
        else:
            raise ValueError(
                'Required property \'conversational_skill_providers\' not present in ProviderCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ProviderCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'conversational_skill_providers'
                  ) and self.conversational_skill_providers is not None:
            conversational_skill_providers_list = []
            for v in self.conversational_skill_providers:
                if isinstance(v, dict):
                    conversational_skill_providers_list.append(v)
                else:
                    conversational_skill_providers_list.append(v.to_dict())
            _dict[
                'conversational_skill_providers'] = conversational_skill_providers_list
        if hasattr(self, 'pagination') and self.pagination is not None:
            if isinstance(self.pagination, dict):
                _dict['pagination'] = self.pagination
            else:
                _dict['pagination'] = self.pagination.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivate:
    """
    Private information of the provider.

    :param ProviderPrivateAuthentication authentication: Private authentication
          information of the provider.
    """

    def __init__(
        self,
        authentication: 'ProviderPrivateAuthentication',
    ) -> None:
        """
        Initialize a ProviderPrivate object.

        :param ProviderPrivateAuthentication authentication: Private authentication
               information of the provider.
        """
        self.authentication = authentication

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderPrivate':
        """Initialize a ProviderPrivate object from a json dictionary."""
        args = {}
        if (authentication := _dict.get('authentication')) is not None:
            args['authentication'] = authentication
        else:
            raise ValueError(
                'Required property \'authentication\' not present in ProviderPrivate JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authentication') and self.authentication is not None:
            if isinstance(self.authentication, dict):
                _dict['authentication'] = self.authentication
            else:
                _dict['authentication'] = self.authentication.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderPrivate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderPrivate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthentication:
    """
    Private authentication information of the provider.

    """

    def __init__(self,) -> None:
        """
        Initialize a ProviderPrivateAuthentication object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'ProviderPrivateAuthenticationBearerFlow',
                'ProviderPrivateAuthenticationBasicFlow',
                'ProviderPrivateAuthenticationOAuth2Flow'
            ]))
        raise Exception(msg)


class ProviderPrivateAuthenticationOAuth2FlowFlows:
    """
    Scenarios performed by the API client to fetch an access token from the authorization
    server.

    """

    def __init__(self,) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2FlowFlows object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password',
                'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials',
                'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode'
            ]))
        raise Exception(msg)


class ProviderPrivateAuthenticationOAuth2PasswordPassword:
    """
    The password for oauth2 authentication when the preferred flow is "password".

    :param str type: (optional) The type of property observed in "value".
    :param str value: (optional) The stored information of the value.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        value: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2PasswordPassword object.

        :param str type: (optional) The type of property observed in "value".
        :param str value: (optional) The stored information of the value.
        """
        self.type = type
        self.value = value

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'ProviderPrivateAuthenticationOAuth2PasswordPassword':
        """Initialize a ProviderPrivateAuthenticationOAuth2PasswordPassword object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationOAuth2PasswordPassword object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationOAuth2PasswordPassword object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'ProviderPrivateAuthenticationOAuth2PasswordPassword'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'ProviderPrivateAuthenticationOAuth2PasswordPassword'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of property observed in "value".
        """

        VALUE = 'value'


class ProviderResponse:
    """
    ProviderResponse.

    :param str provider_id: (optional) The unique identifier of the provider.
    :param ProviderResponseSpecification specification: (optional) The specification
          of the provider.
    """

    def __init__(
        self,
        *,
        provider_id: Optional[str] = None,
        specification: Optional['ProviderResponseSpecification'] = None,
    ) -> None:
        """
        Initialize a ProviderResponse object.

        :param str provider_id: (optional) The unique identifier of the provider.
        :param ProviderResponseSpecification specification: (optional) The
               specification of the provider.
        """
        self.provider_id = provider_id
        self.specification = specification

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderResponse':
        """Initialize a ProviderResponse object from a json dictionary."""
        args = {}
        if (provider_id := _dict.get('provider_id')) is not None:
            args['provider_id'] = provider_id
        if (specification := _dict.get('specification')) is not None:
            args['specification'] = ProviderResponseSpecification.from_dict(
                specification)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'provider_id') and self.provider_id is not None:
            _dict['provider_id'] = self.provider_id
        if hasattr(self, 'specification') and self.specification is not None:
            if isinstance(self.specification, dict):
                _dict['specification'] = self.specification
            else:
                _dict['specification'] = self.specification.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderResponseSpecification:
    """
    The specification of the provider.

    :param List[ProviderResponseSpecificationServersItem] servers: (optional) An
          array of objects defining all endpoints of the provider.
           **Note:** Multiple array items are reserved for future use.
    :param ProviderResponseSpecificationComponents components: (optional) An object
          defining various reusable definitions of the provider.
    """

    def __init__(
        self,
        *,
        servers: Optional[
            List['ProviderResponseSpecificationServersItem']] = None,
        components: Optional['ProviderResponseSpecificationComponents'] = None,
    ) -> None:
        """
        Initialize a ProviderResponseSpecification object.

        :param List[ProviderResponseSpecificationServersItem] servers: (optional)
               An array of objects defining all endpoints of the provider.
                **Note:** Multiple array items are reserved for future use.
        :param ProviderResponseSpecificationComponents components: (optional) An
               object defining various reusable definitions of the provider.
        """
        self.servers = servers
        self.components = components

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderResponseSpecification':
        """Initialize a ProviderResponseSpecification object from a json dictionary."""
        args = {}
        if (servers := _dict.get('servers')) is not None:
            args['servers'] = [
                ProviderResponseSpecificationServersItem.from_dict(v)
                for v in servers
            ]
        if (components := _dict.get('components')) is not None:
            args[
                'components'] = ProviderResponseSpecificationComponents.from_dict(
                    components)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponseSpecification object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'servers') and self.servers is not None:
            servers_list = []
            for v in self.servers:
                if isinstance(v, dict):
                    servers_list.append(v)
                else:
                    servers_list.append(v.to_dict())
            _dict['servers'] = servers_list
        if hasattr(self, 'components') and self.components is not None:
            if isinstance(self.components, dict):
                _dict['components'] = self.components
            else:
                _dict['components'] = self.components.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponseSpecification object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderResponseSpecification') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderResponseSpecification') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderResponseSpecificationComponents:
    """
    An object defining various reusable definitions of the provider.

    :param ProviderResponseSpecificationComponentsSecuritySchemes security_schemes:
          (optional) The definition of the security scheme for the provider.
    """

    def __init__(
        self,
        *,
        security_schemes: Optional[
            'ProviderResponseSpecificationComponentsSecuritySchemes'] = None,
    ) -> None:
        """
        Initialize a ProviderResponseSpecificationComponents object.

        :param ProviderResponseSpecificationComponentsSecuritySchemes
               security_schemes: (optional) The definition of the security scheme for the
               provider.
        """
        self.security_schemes = security_schemes

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'ProviderResponseSpecificationComponents':
        """Initialize a ProviderResponseSpecificationComponents object from a json dictionary."""
        args = {}
        if (security_schemes := _dict.get('securitySchemes')) is not None:
            args[
                'security_schemes'] = ProviderResponseSpecificationComponentsSecuritySchemes.from_dict(
                    security_schemes)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponseSpecificationComponents object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'security_schemes') and self.security_schemes is not None:
            if isinstance(self.security_schemes, dict):
                _dict['securitySchemes'] = self.security_schemes
            else:
                _dict['securitySchemes'] = self.security_schemes.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponseSpecificationComponents object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderResponseSpecificationComponents') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderResponseSpecificationComponents') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderResponseSpecificationComponentsSecuritySchemes:
    """
    The definition of the security scheme for the provider.

    :param str authentication_method: (optional) The authentication method required
          for requests made from watsonx Assistant to the conversational skill provider.
    :param ProviderResponseSpecificationComponentsSecuritySchemesBasic basic:
          (optional) Non-private settings for basic access authentication.
    :param ProviderAuthenticationOAuth2 oauth2: (optional) Non-private settings for
          oauth2 authentication.
    """

    def __init__(
        self,
        *,
        authentication_method: Optional[str] = None,
        basic: Optional[
            'ProviderResponseSpecificationComponentsSecuritySchemesBasic'] = None,
        oauth2: Optional['ProviderAuthenticationOAuth2'] = None,
    ) -> None:
        """
        Initialize a ProviderResponseSpecificationComponentsSecuritySchemes object.

        :param str authentication_method: (optional) The authentication method
               required for requests made from watsonx Assistant to the conversational
               skill provider.
        :param ProviderResponseSpecificationComponentsSecuritySchemesBasic basic:
               (optional) Non-private settings for basic access authentication.
        :param ProviderAuthenticationOAuth2 oauth2: (optional) Non-private settings
               for oauth2 authentication.
        """
        self.authentication_method = authentication_method
        self.basic = basic
        self.oauth2 = oauth2

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderResponseSpecificationComponentsSecuritySchemes':
        """Initialize a ProviderResponseSpecificationComponentsSecuritySchemes object from a json dictionary."""
        args = {}
        if (authentication_method :=
                _dict.get('authentication_method')) is not None:
            args['authentication_method'] = authentication_method
        if (basic := _dict.get('basic')) is not None:
            args[
                'basic'] = ProviderResponseSpecificationComponentsSecuritySchemesBasic.from_dict(
                    basic)
        if (oauth2 := _dict.get('oauth2')) is not None:
            args['oauth2'] = ProviderAuthenticationOAuth2.from_dict(oauth2)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponseSpecificationComponentsSecuritySchemes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authentication_method'
                  ) and self.authentication_method is not None:
            _dict['authentication_method'] = self.authentication_method
        if hasattr(self, 'basic') and self.basic is not None:
            if isinstance(self.basic, dict):
                _dict['basic'] = self.basic
            else:
                _dict['basic'] = self.basic.to_dict()
        if hasattr(self, 'oauth2') and self.oauth2 is not None:
            if isinstance(self.oauth2, dict):
                _dict['oauth2'] = self.oauth2
            else:
                _dict['oauth2'] = self.oauth2.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponseSpecificationComponentsSecuritySchemes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'ProviderResponseSpecificationComponentsSecuritySchemes'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'ProviderResponseSpecificationComponentsSecuritySchemes'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AuthenticationMethodEnum(str, Enum):
        """
        The authentication method required for requests made from watsonx Assistant to the
        conversational skill provider.
        """

        BASIC = 'basic'
        BEARER = 'bearer'
        API_KEY = 'api_key'
        OAUTH2 = 'oauth2'
        NONE = 'none'


class ProviderResponseSpecificationComponentsSecuritySchemesBasic:
    """
    Non-private settings for basic access authentication.

    :param ProviderAuthenticationTypeAndValue username: (optional) The username for
          basic access authentication.
    """

    def __init__(
        self,
        *,
        username: Optional['ProviderAuthenticationTypeAndValue'] = None,
    ) -> None:
        """
        Initialize a ProviderResponseSpecificationComponentsSecuritySchemesBasic object.

        :param ProviderAuthenticationTypeAndValue username: (optional) The username
               for basic access authentication.
        """
        self.username = username

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderResponseSpecificationComponentsSecuritySchemesBasic':
        """Initialize a ProviderResponseSpecificationComponentsSecuritySchemesBasic object from a json dictionary."""
        args = {}
        if (username := _dict.get('username')) is not None:
            args['username'] = ProviderAuthenticationTypeAndValue.from_dict(
                username)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponseSpecificationComponentsSecuritySchemesBasic object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'username') and self.username is not None:
            if isinstance(self.username, dict):
                _dict['username'] = self.username
            else:
                _dict['username'] = self.username.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponseSpecificationComponentsSecuritySchemesBasic object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self,
        other: 'ProviderResponseSpecificationComponentsSecuritySchemesBasic'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self,
        other: 'ProviderResponseSpecificationComponentsSecuritySchemesBasic'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderResponseSpecificationServersItem:
    """
    ProviderResponseSpecificationServersItem.

    :param str url: (optional) The URL of the conversational skill provider.
    """

    def __init__(
        self,
        *,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderResponseSpecificationServersItem object.

        :param str url: (optional) The URL of the conversational skill provider.
        """
        self.url = url

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'ProviderResponseSpecificationServersItem':
        """Initialize a ProviderResponseSpecificationServersItem object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderResponseSpecificationServersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderResponseSpecificationServersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderResponseSpecificationServersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderResponseSpecificationServersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderSpecification:
    """
    The specification of the provider.

    :param List[ProviderSpecificationServersItem] servers: An array of objects
          defining all endpoints of the provider.
           **Note:** Multiple array items are reserved for future use.
    :param ProviderSpecificationComponents components: (optional) An object defining
          various reusable definitions of the provider.
    """

    def __init__(
        self,
        servers: List['ProviderSpecificationServersItem'],
        *,
        components: Optional['ProviderSpecificationComponents'] = None,
    ) -> None:
        """
        Initialize a ProviderSpecification object.

        :param List[ProviderSpecificationServersItem] servers: An array of objects
               defining all endpoints of the provider.
                **Note:** Multiple array items are reserved for future use.
        :param ProviderSpecificationComponents components: (optional) An object
               defining various reusable definitions of the provider.
        """
        self.servers = servers
        self.components = components

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderSpecification':
        """Initialize a ProviderSpecification object from a json dictionary."""
        args = {}
        if (servers := _dict.get('servers')) is not None:
            args['servers'] = [
                ProviderSpecificationServersItem.from_dict(v) for v in servers
            ]
        else:
            raise ValueError(
                'Required property \'servers\' not present in ProviderSpecification JSON'
            )
        if (components := _dict.get('components')) is not None:
            args['components'] = ProviderSpecificationComponents.from_dict(
                components)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderSpecification object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'servers') and self.servers is not None:
            servers_list = []
            for v in self.servers:
                if isinstance(v, dict):
                    servers_list.append(v)
                else:
                    servers_list.append(v.to_dict())
            _dict['servers'] = servers_list
        if hasattr(self, 'components') and self.components is not None:
            if isinstance(self.components, dict):
                _dict['components'] = self.components
            else:
                _dict['components'] = self.components.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderSpecification object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderSpecification') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderSpecification') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderSpecificationComponents:
    """
    An object defining various reusable definitions of the provider.

    :param ProviderSpecificationComponentsSecuritySchemes security_schemes:
          (optional) The definition of the security scheme for the provider.
    """

    def __init__(
        self,
        *,
        security_schemes: Optional[
            'ProviderSpecificationComponentsSecuritySchemes'] = None,
    ) -> None:
        """
        Initialize a ProviderSpecificationComponents object.

        :param ProviderSpecificationComponentsSecuritySchemes security_schemes:
               (optional) The definition of the security scheme for the provider.
        """
        self.security_schemes = security_schemes

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderSpecificationComponents':
        """Initialize a ProviderSpecificationComponents object from a json dictionary."""
        args = {}
        if (security_schemes := _dict.get('securitySchemes')) is not None:
            args[
                'security_schemes'] = ProviderSpecificationComponentsSecuritySchemes.from_dict(
                    security_schemes)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderSpecificationComponents object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'security_schemes') and self.security_schemes is not None:
            if isinstance(self.security_schemes, dict):
                _dict['securitySchemes'] = self.security_schemes
            else:
                _dict['securitySchemes'] = self.security_schemes.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderSpecificationComponents object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderSpecificationComponents') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderSpecificationComponents') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderSpecificationComponentsSecuritySchemes:
    """
    The definition of the security scheme for the provider.

    :param str authentication_method: (optional) The authentication method required
          for requests made from watsonx Assistant to the conversational skill provider.
    :param ProviderSpecificationComponentsSecuritySchemesBasic basic: (optional)
          Non-private settings for basic access authentication.
    :param ProviderAuthenticationOAuth2 oauth2: (optional) Non-private settings for
          oauth2 authentication.
    """

    def __init__(
        self,
        *,
        authentication_method: Optional[str] = None,
        basic: Optional[
            'ProviderSpecificationComponentsSecuritySchemesBasic'] = None,
        oauth2: Optional['ProviderAuthenticationOAuth2'] = None,
    ) -> None:
        """
        Initialize a ProviderSpecificationComponentsSecuritySchemes object.

        :param str authentication_method: (optional) The authentication method
               required for requests made from watsonx Assistant to the conversational
               skill provider.
        :param ProviderSpecificationComponentsSecuritySchemesBasic basic:
               (optional) Non-private settings for basic access authentication.
        :param ProviderAuthenticationOAuth2 oauth2: (optional) Non-private settings
               for oauth2 authentication.
        """
        self.authentication_method = authentication_method
        self.basic = basic
        self.oauth2 = oauth2

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'ProviderSpecificationComponentsSecuritySchemes':
        """Initialize a ProviderSpecificationComponentsSecuritySchemes object from a json dictionary."""
        args = {}
        if (authentication_method :=
                _dict.get('authentication_method')) is not None:
            args['authentication_method'] = authentication_method
        if (basic := _dict.get('basic')) is not None:
            args[
                'basic'] = ProviderSpecificationComponentsSecuritySchemesBasic.from_dict(
                    basic)
        if (oauth2 := _dict.get('oauth2')) is not None:
            args['oauth2'] = ProviderAuthenticationOAuth2.from_dict(oauth2)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderSpecificationComponentsSecuritySchemes object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'authentication_method'
                  ) and self.authentication_method is not None:
            _dict['authentication_method'] = self.authentication_method
        if hasattr(self, 'basic') and self.basic is not None:
            if isinstance(self.basic, dict):
                _dict['basic'] = self.basic
            else:
                _dict['basic'] = self.basic.to_dict()
        if hasattr(self, 'oauth2') and self.oauth2 is not None:
            if isinstance(self.oauth2, dict):
                _dict['oauth2'] = self.oauth2
            else:
                _dict['oauth2'] = self.oauth2.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderSpecificationComponentsSecuritySchemes object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'ProviderSpecificationComponentsSecuritySchemes') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'ProviderSpecificationComponentsSecuritySchemes') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AuthenticationMethodEnum(str, Enum):
        """
        The authentication method required for requests made from watsonx Assistant to the
        conversational skill provider.
        """

        BASIC = 'basic'
        BEARER = 'bearer'
        API_KEY = 'api_key'
        OAUTH2 = 'oauth2'
        NONE = 'none'


class ProviderSpecificationComponentsSecuritySchemesBasic:
    """
    Non-private settings for basic access authentication.

    :param ProviderAuthenticationTypeAndValue username: (optional) The username for
          basic access authentication.
    """

    def __init__(
        self,
        *,
        username: Optional['ProviderAuthenticationTypeAndValue'] = None,
    ) -> None:
        """
        Initialize a ProviderSpecificationComponentsSecuritySchemesBasic object.

        :param ProviderAuthenticationTypeAndValue username: (optional) The username
               for basic access authentication.
        """
        self.username = username

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'ProviderSpecificationComponentsSecuritySchemesBasic':
        """Initialize a ProviderSpecificationComponentsSecuritySchemesBasic object from a json dictionary."""
        args = {}
        if (username := _dict.get('username')) is not None:
            args['username'] = ProviderAuthenticationTypeAndValue.from_dict(
                username)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderSpecificationComponentsSecuritySchemesBasic object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'username') and self.username is not None:
            if isinstance(self.username, dict):
                _dict['username'] = self.username
            else:
                _dict['username'] = self.username.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderSpecificationComponentsSecuritySchemesBasic object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'ProviderSpecificationComponentsSecuritySchemesBasic'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'ProviderSpecificationComponentsSecuritySchemesBasic'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderSpecificationServersItem:
    """
    ProviderSpecificationServersItem.

    :param str url: (optional) The URL of the conversational skill provider.
    """

    def __init__(
        self,
        *,
        url: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderSpecificationServersItem object.

        :param str url: (optional) The URL of the conversational skill provider.
        """
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderSpecificationServersItem':
        """Initialize a ProviderSpecificationServersItem object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderSpecificationServersItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderSpecificationServersItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderSpecificationServersItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderSpecificationServersItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Release:
    """
    Release.

    :param str release: (optional) The name of the release. The name is the version
          number (an integer), returned as a string.
    :param str description: (optional) The description of the release.
    :param List[EnvironmentReference] environment_references: (optional) An array of
          objects describing the environments where this release has been deployed.
    :param ReleaseContent content: (optional) An object identifying the versionable
          content objects (such as skill snapshots) that are included in the release.
    :param str status: (optional) The current status of the release:
           - **Available**: The release is available for deployment.
           - **Failed**: An asynchronous publish operation has failed.
           - **Processing**: An asynchronous publish operation has not yet completed.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        *,
        release: Optional[str] = None,
        description: Optional[str] = None,
        environment_references: Optional[List['EnvironmentReference']] = None,
        content: Optional['ReleaseContent'] = None,
        status: Optional[str] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Release object.

        :param str description: (optional) The description of the release.
        """
        self.release = release
        self.description = description
        self.environment_references = environment_references
        self.content = content
        self.status = status
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Release':
        """Initialize a Release object from a json dictionary."""
        args = {}
        if (release := _dict.get('release')) is not None:
            args['release'] = release
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (environment_references :=
                _dict.get('environment_references')) is not None:
            args['environment_references'] = [
                EnvironmentReference.from_dict(v)
                for v in environment_references
            ]
        if (content := _dict.get('content')) is not None:
            args['content'] = ReleaseContent.from_dict(content)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Release object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'release') and getattr(self, 'release') is not None:
            _dict['release'] = getattr(self, 'release')
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'environment_references') and getattr(
                self, 'environment_references') is not None:
            environment_references_list = []
            for v in getattr(self, 'environment_references'):
                if isinstance(v, dict):
                    environment_references_list.append(v)
                else:
                    environment_references_list.append(v.to_dict())
            _dict['environment_references'] = environment_references_list
        if hasattr(self, 'content') and getattr(self, 'content') is not None:
            if isinstance(getattr(self, 'content'), dict):
                _dict['content'] = getattr(self, 'content')
            else:
                _dict['content'] = getattr(self, 'content').to_dict()
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Release object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Release') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Release') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the release:
         - **Available**: The release is available for deployment.
         - **Failed**: An asynchronous publish operation has failed.
         - **Processing**: An asynchronous publish operation has not yet completed.
        """

        AVAILABLE = 'Available'
        FAILED = 'Failed'
        PROCESSING = 'Processing'


class ReleaseCollection:
    """
    ReleaseCollection.

    :param List[Release] releases: An array of objects describing the releases
          associated with an assistant.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        releases: List['Release'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a ReleaseCollection object.

        :param List[Release] releases: An array of objects describing the releases
               associated with an assistant.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.releases = releases
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReleaseCollection':
        """Initialize a ReleaseCollection object from a json dictionary."""
        args = {}
        if (releases := _dict.get('releases')) is not None:
            args['releases'] = [Release.from_dict(v) for v in releases]
        else:
            raise ValueError(
                'Required property \'releases\' not present in ReleaseCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ReleaseCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReleaseCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'releases') and self.releases is not None:
            releases_list = []
            for v in self.releases:
                if isinstance(v, dict):
                    releases_list.append(v)
                else:
                    releases_list.append(v.to_dict())
            _dict['releases'] = releases_list
        if hasattr(self, 'pagination') and self.pagination is not None:
            if isinstance(self.pagination, dict):
                _dict['pagination'] = self.pagination
            else:
                _dict['pagination'] = self.pagination.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReleaseCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReleaseCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReleaseCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReleaseContent:
    """
    An object identifying the versionable content objects (such as skill snapshots) that
    are included in the release.

    :param List[ReleaseSkill] skills: (optional) The skill snapshots that are
          included in the release.
    """

    def __init__(
        self,
        *,
        skills: Optional[List['ReleaseSkill']] = None,
    ) -> None:
        """
        Initialize a ReleaseContent object.

        """
        self.skills = skills

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReleaseContent':
        """Initialize a ReleaseContent object from a json dictionary."""
        args = {}
        if (skills := _dict.get('skills')) is not None:
            args['skills'] = [ReleaseSkill.from_dict(v) for v in skills]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReleaseContent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'skills') and getattr(self, 'skills') is not None:
            skills_list = []
            for v in getattr(self, 'skills'):
                if isinstance(v, dict):
                    skills_list.append(v)
                else:
                    skills_list.append(v.to_dict())
            _dict['skills'] = skills_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReleaseContent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReleaseContent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReleaseContent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ReleaseSkill:
    """
    ReleaseSkill.

    :param str skill_id: The skill ID of the skill.
    :param str type: (optional) The type of the skill.
    :param str snapshot: (optional) The name of the skill snapshot that is saved as
          part of the release (for example, `draft` or `1`).
    """

    def __init__(
        self,
        skill_id: str,
        *,
        type: Optional[str] = None,
        snapshot: Optional[str] = None,
    ) -> None:
        """
        Initialize a ReleaseSkill object.

        :param str skill_id: The skill ID of the skill.
        :param str type: (optional) The type of the skill.
        :param str snapshot: (optional) The name of the skill snapshot that is
               saved as part of the release (for example, `draft` or `1`).
        """
        self.skill_id = skill_id
        self.type = type
        self.snapshot = snapshot

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReleaseSkill':
        """Initialize a ReleaseSkill object from a json dictionary."""
        args = {}
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in ReleaseSkill JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (snapshot := _dict.get('snapshot')) is not None:
            args['snapshot'] = snapshot
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ReleaseSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'skill_id') and self.skill_id is not None:
            _dict['skill_id'] = self.skill_id
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'snapshot') and self.snapshot is not None:
            _dict['snapshot'] = self.snapshot
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ReleaseSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ReleaseSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ReleaseSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of the skill.
        """

        DIALOG = 'dialog'
        ACTION = 'action'
        SEARCH = 'search'


class RequestAnalytics:
    """
    An optional object containing analytics data. Currently, this data is used only for
    events sent to the Segment extension.

    :param str browser: (optional) The browser that was used to send the message
          that triggered the event.
    :param str device: (optional) The type of device that was used to send the
          message that triggered the event.
    :param str page_url: (optional) The URL of the web page that was used to send
          the message that triggered the event.
    """

    def __init__(
        self,
        *,
        browser: Optional[str] = None,
        device: Optional[str] = None,
        page_url: Optional[str] = None,
    ) -> None:
        """
        Initialize a RequestAnalytics object.

        :param str browser: (optional) The browser that was used to send the
               message that triggered the event.
        :param str device: (optional) The type of device that was used to send the
               message that triggered the event.
        :param str page_url: (optional) The URL of the web page that was used to
               send the message that triggered the event.
        """
        self.browser = browser
        self.device = device
        self.page_url = page_url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RequestAnalytics':
        """Initialize a RequestAnalytics object from a json dictionary."""
        args = {}
        if (browser := _dict.get('browser')) is not None:
            args['browser'] = browser
        if (device := _dict.get('device')) is not None:
            args['device'] = device
        if (page_url := _dict.get('pageUrl')) is not None:
            args['page_url'] = page_url
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RequestAnalytics object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'browser') and self.browser is not None:
            _dict['browser'] = self.browser
        if hasattr(self, 'device') and self.device is not None:
            _dict['device'] = self.device
        if hasattr(self, 'page_url') and self.page_url is not None:
            _dict['pageUrl'] = self.page_url
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RequestAnalytics object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RequestAnalytics') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RequestAnalytics') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ResponseGenericChannel:
    """
    ResponseGenericChannel.

    :param str channel: (optional) A channel for which the response is intended.
    """

    def __init__(
        self,
        *,
        channel: Optional[str] = None,
    ) -> None:
        """
        Initialize a ResponseGenericChannel object.

        :param str channel: (optional) A channel for which the response is
               intended.
        """
        self.channel = channel

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResponseGenericChannel':
        """Initialize a ResponseGenericChannel object from a json dictionary."""
        args = {}
        if (channel := _dict.get('channel')) is not None:
            args['channel'] = channel
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResponseGenericChannel object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'channel') and self.channel is not None:
            _dict['channel'] = self.channel
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResponseGenericChannel object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResponseGenericChannel') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResponseGenericChannel') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeEntity:
    """
    The entity value that was recognized in the user input.

    :param str entity: An entity detected in the input.
    :param List[int] location: (optional) An array of zero-based character offsets
          that indicate where the detected entity values begin and end in the input text.
    :param str value: The term in the input text that was recognized as an entity
          value.
    :param float confidence: (optional) A decimal percentage that represents
          confidence in the recognized entity.
    :param List[CaptureGroup] groups: (optional) The recognized capture groups for
          the entity, as defined by the entity pattern.
    :param RuntimeEntityInterpretation interpretation: (optional) An object
          containing detailed information about the entity recognized in the user input.
          This property is included only if the new system entities are enabled for the
          skill.
          For more information about how the new system entities are interpreted, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-beta-system-entities).
    :param List[RuntimeEntityAlternative] alternatives: (optional) An array of
          possible alternative values that the user might have intended instead of the
          value returned in the **value** property. This property is returned only for
          `@sys-time` and `@sys-date` entities when the user's input is ambiguous.
          This property is included only if the new system entities are enabled for the
          skill.
    :param RuntimeEntityRole role: (optional) An object describing the role played
          by a system entity that is specifies the beginning or end of a range recognized
          in the user input. This property is included only if the new system entities are
          enabled for the skill.
    :param str skill: (optional) The skill that recognized the entity value.
          Currently, the only possible values are `main skill` for the dialog skill (if
          enabled) and `actions skill` for the action skill.
          This property is present only if the assistant has both a dialog skill and an
          action skill.
    """

    def __init__(
        self,
        entity: str,
        value: str,
        *,
        location: Optional[List[int]] = None,
        confidence: Optional[float] = None,
        groups: Optional[List['CaptureGroup']] = None,
        interpretation: Optional['RuntimeEntityInterpretation'] = None,
        alternatives: Optional[List['RuntimeEntityAlternative']] = None,
        role: Optional['RuntimeEntityRole'] = None,
        skill: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeEntity object.

        :param str entity: An entity detected in the input.
        :param str value: The term in the input text that was recognized as an
               entity value.
        :param List[int] location: (optional) An array of zero-based character
               offsets that indicate where the detected entity values begin and end in the
               input text.
        :param float confidence: (optional) A decimal percentage that represents
               confidence in the recognized entity.
        :param List[CaptureGroup] groups: (optional) The recognized capture groups
               for the entity, as defined by the entity pattern.
        :param RuntimeEntityInterpretation interpretation: (optional) An object
               containing detailed information about the entity recognized in the user
               input. This property is included only if the new system entities are
               enabled for the skill.
               For more information about how the new system entities are interpreted, see
               the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-beta-system-entities).
        :param List[RuntimeEntityAlternative] alternatives: (optional) An array of
               possible alternative values that the user might have intended instead of
               the value returned in the **value** property. This property is returned
               only for `@sys-time` and `@sys-date` entities when the user's input is
               ambiguous.
               This property is included only if the new system entities are enabled for
               the skill.
        :param RuntimeEntityRole role: (optional) An object describing the role
               played by a system entity that is specifies the beginning or end of a range
               recognized in the user input. This property is included only if the new
               system entities are enabled for the skill.
        :param str skill: (optional) The skill that recognized the entity value.
               Currently, the only possible values are `main skill` for the dialog skill
               (if enabled) and `actions skill` for the action skill.
               This property is present only if the assistant has both a dialog skill and
               an action skill.
        """
        self.entity = entity
        self.location = location
        self.value = value
        self.confidence = confidence
        self.groups = groups
        self.interpretation = interpretation
        self.alternatives = alternatives
        self.role = role
        self.skill = skill

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntity':
        """Initialize a RuntimeEntity object from a json dictionary."""
        args = {}
        if (entity := _dict.get('entity')) is not None:
            args['entity'] = entity
        else:
            raise ValueError(
                'Required property \'entity\' not present in RuntimeEntity JSON'
            )
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError(
                'Required property \'value\' not present in RuntimeEntity JSON')
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        if (groups := _dict.get('groups')) is not None:
            args['groups'] = [CaptureGroup.from_dict(v) for v in groups]
        if (interpretation := _dict.get('interpretation')) is not None:
            args['interpretation'] = RuntimeEntityInterpretation.from_dict(
                interpretation)
        if (alternatives := _dict.get('alternatives')) is not None:
            args['alternatives'] = [
                RuntimeEntityAlternative.from_dict(v) for v in alternatives
            ]
        if (role := _dict.get('role')) is not None:
            args['role'] = RuntimeEntityRole.from_dict(role)
        if (skill := _dict.get('skill')) is not None:
            args['skill'] = skill
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'groups') and self.groups is not None:
            groups_list = []
            for v in self.groups:
                if isinstance(v, dict):
                    groups_list.append(v)
                else:
                    groups_list.append(v.to_dict())
            _dict['groups'] = groups_list
        if hasattr(self, 'interpretation') and self.interpretation is not None:
            if isinstance(self.interpretation, dict):
                _dict['interpretation'] = self.interpretation
            else:
                _dict['interpretation'] = self.interpretation.to_dict()
        if hasattr(self, 'alternatives') and self.alternatives is not None:
            alternatives_list = []
            for v in self.alternatives:
                if isinstance(v, dict):
                    alternatives_list.append(v)
                else:
                    alternatives_list.append(v.to_dict())
            _dict['alternatives'] = alternatives_list
        if hasattr(self, 'role') and self.role is not None:
            if isinstance(self.role, dict):
                _dict['role'] = self.role
            else:
                _dict['role'] = self.role.to_dict()
        if hasattr(self, 'skill') and self.skill is not None:
            _dict['skill'] = self.skill
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeEntityAlternative:
    """
    An alternative value for the recognized entity.

    :param str value: (optional) The entity value that was recognized in the user
          input.
    :param float confidence: (optional) A decimal percentage that represents
          confidence in the recognized entity.
    """

    def __init__(
        self,
        *,
        value: Optional[str] = None,
        confidence: Optional[float] = None,
    ) -> None:
        """
        Initialize a RuntimeEntityAlternative object.

        :param str value: (optional) The entity value that was recognized in the
               user input.
        :param float confidence: (optional) A decimal percentage that represents
               confidence in the recognized entity.
        """
        self.value = value
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntityAlternative':
        """Initialize a RuntimeEntityAlternative object from a json dictionary."""
        args = {}
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntityAlternative object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeEntityAlternative object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeEntityAlternative') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeEntityAlternative') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeEntityInterpretation:
    """
    RuntimeEntityInterpretation.

    :param str calendar_type: (optional) The calendar used to represent a recognized
          date (for example, `Gregorian`).
    :param str datetime_link: (optional) A unique identifier used to associate a
          recognized time and date. If the user input contains a date and time that are
          mentioned together (for example, `Today at 5`, the same **datetime_link** value
          is returned for both the `@sys-date` and `@sys-time` entities).
    :param str festival: (optional) A locale-specific holiday name (such as
          `thanksgiving` or `christmas`). This property is included when a `@sys-date`
          entity is recognized based on a holiday name in the user input.
    :param str granularity: (optional) The precision or duration of a time range
          specified by a recognized `@sys-time` or `@sys-date` entity.
    :param str range_link: (optional) A unique identifier used to associate multiple
          recognized `@sys-date`, `@sys-time`, or `@sys-number` entities that are
          recognized as a range of values in the user's input (for example, `from July 4
          until July 14` or `from 20 to 25`).
    :param str range_modifier: (optional) The word in the user input that indicates
          that a `sys-date` or `sys-time` entity is part of an implied range where only
          one date or time is specified (for example, `since` or `until`).
    :param float relative_day: (optional) A recognized mention of a relative day,
          represented numerically as an offset from the current date (for example, `-1`
          for `yesterday` or `10` for `in ten days`).
    :param float relative_month: (optional) A recognized mention of a relative
          month, represented numerically as an offset from the current month (for example,
          `1` for `next month` or `-3` for `three months ago`).
    :param float relative_week: (optional) A recognized mention of a relative week,
          represented numerically as an offset from the current week (for example, `2` for
          `in two weeks` or `-1` for `last week).
    :param float relative_weekend: (optional) A recognized mention of a relative
          date range for a weekend, represented numerically as an offset from the current
          weekend (for example, `0` for `this weekend` or `-1` for `last weekend`).
    :param float relative_year: (optional) A recognized mention of a relative year,
          represented numerically as an offset from the current year (for example, `1` for
          `next year` or `-5` for `five years ago`).
    :param float specific_day: (optional) A recognized mention of a specific date,
          represented numerically as the date within the month (for example, `30` for
          `June 30`.).
    :param str specific_day_of_week: (optional) A recognized mention of a specific
          day of the week as a lowercase string (for example, `monday`).
    :param float specific_month: (optional) A recognized mention of a specific
          month, represented numerically (for example, `7` for `July`).
    :param float specific_quarter: (optional) A recognized mention of a specific
          quarter, represented numerically (for example, `3` for `the third quarter`).
    :param float specific_year: (optional) A recognized mention of a specific year
          (for example, `2016`).
    :param float numeric_value: (optional) A recognized numeric value, represented
          as an integer or double.
    :param str subtype: (optional) The type of numeric value recognized in the user
          input (`integer` or `rational`).
    :param str part_of_day: (optional) A recognized term for a time that was
          mentioned as a part of the day in the user's input (for example, `morning` or
          `afternoon`).
    :param float relative_hour: (optional) A recognized mention of a relative hour,
          represented numerically as an offset from the current hour (for example, `3` for
          `in three hours` or `-1` for `an hour ago`).
    :param float relative_minute: (optional) A recognized mention of a relative
          time, represented numerically as an offset in minutes from the current time (for
          example, `5` for `in five minutes` or `-15` for `fifteen minutes ago`).
    :param float relative_second: (optional) A recognized mention of a relative
          time, represented numerically as an offset in seconds from the current time (for
          example, `10` for `in ten seconds` or `-30` for `thirty seconds ago`).
    :param float specific_hour: (optional) A recognized specific hour mentioned as
          part of a time value (for example, `10` for `10:15 AM`.).
    :param float specific_minute: (optional) A recognized specific minute mentioned
          as part of a time value (for example, `15` for `10:15 AM`.).
    :param float specific_second: (optional) A recognized specific second mentioned
          as part of a time value (for example, `30` for `10:15:30 AM`.).
    :param str timezone: (optional) A recognized time zone mentioned as part of a
          time value (for example, `EST`).
    """

    def __init__(
        self,
        *,
        calendar_type: Optional[str] = None,
        datetime_link: Optional[str] = None,
        festival: Optional[str] = None,
        granularity: Optional[str] = None,
        range_link: Optional[str] = None,
        range_modifier: Optional[str] = None,
        relative_day: Optional[float] = None,
        relative_month: Optional[float] = None,
        relative_week: Optional[float] = None,
        relative_weekend: Optional[float] = None,
        relative_year: Optional[float] = None,
        specific_day: Optional[float] = None,
        specific_day_of_week: Optional[str] = None,
        specific_month: Optional[float] = None,
        specific_quarter: Optional[float] = None,
        specific_year: Optional[float] = None,
        numeric_value: Optional[float] = None,
        subtype: Optional[str] = None,
        part_of_day: Optional[str] = None,
        relative_hour: Optional[float] = None,
        relative_minute: Optional[float] = None,
        relative_second: Optional[float] = None,
        specific_hour: Optional[float] = None,
        specific_minute: Optional[float] = None,
        specific_second: Optional[float] = None,
        timezone: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeEntityInterpretation object.

        :param str calendar_type: (optional) The calendar used to represent a
               recognized date (for example, `Gregorian`).
        :param str datetime_link: (optional) A unique identifier used to associate
               a recognized time and date. If the user input contains a date and time that
               are mentioned together (for example, `Today at 5`, the same
               **datetime_link** value is returned for both the `@sys-date` and
               `@sys-time` entities).
        :param str festival: (optional) A locale-specific holiday name (such as
               `thanksgiving` or `christmas`). This property is included when a
               `@sys-date` entity is recognized based on a holiday name in the user input.
        :param str granularity: (optional) The precision or duration of a time
               range specified by a recognized `@sys-time` or `@sys-date` entity.
        :param str range_link: (optional) A unique identifier used to associate
               multiple recognized `@sys-date`, `@sys-time`, or `@sys-number` entities
               that are recognized as a range of values in the user's input (for example,
               `from July 4 until July 14` or `from 20 to 25`).
        :param str range_modifier: (optional) The word in the user input that
               indicates that a `sys-date` or `sys-time` entity is part of an implied
               range where only one date or time is specified (for example, `since` or
               `until`).
        :param float relative_day: (optional) A recognized mention of a relative
               day, represented numerically as an offset from the current date (for
               example, `-1` for `yesterday` or `10` for `in ten days`).
        :param float relative_month: (optional) A recognized mention of a relative
               month, represented numerically as an offset from the current month (for
               example, `1` for `next month` or `-3` for `three months ago`).
        :param float relative_week: (optional) A recognized mention of a relative
               week, represented numerically as an offset from the current week (for
               example, `2` for `in two weeks` or `-1` for `last week).
        :param float relative_weekend: (optional) A recognized mention of a
               relative date range for a weekend, represented numerically as an offset
               from the current weekend (for example, `0` for `this weekend` or `-1` for
               `last weekend`).
        :param float relative_year: (optional) A recognized mention of a relative
               year, represented numerically as an offset from the current year (for
               example, `1` for `next year` or `-5` for `five years ago`).
        :param float specific_day: (optional) A recognized mention of a specific
               date, represented numerically as the date within the month (for example,
               `30` for `June 30`.).
        :param str specific_day_of_week: (optional) A recognized mention of a
               specific day of the week as a lowercase string (for example, `monday`).
        :param float specific_month: (optional) A recognized mention of a specific
               month, represented numerically (for example, `7` for `July`).
        :param float specific_quarter: (optional) A recognized mention of a
               specific quarter, represented numerically (for example, `3` for `the third
               quarter`).
        :param float specific_year: (optional) A recognized mention of a specific
               year (for example, `2016`).
        :param float numeric_value: (optional) A recognized numeric value,
               represented as an integer or double.
        :param str subtype: (optional) The type of numeric value recognized in the
               user input (`integer` or `rational`).
        :param str part_of_day: (optional) A recognized term for a time that was
               mentioned as a part of the day in the user's input (for example, `morning`
               or `afternoon`).
        :param float relative_hour: (optional) A recognized mention of a relative
               hour, represented numerically as an offset from the current hour (for
               example, `3` for `in three hours` or `-1` for `an hour ago`).
        :param float relative_minute: (optional) A recognized mention of a relative
               time, represented numerically as an offset in minutes from the current time
               (for example, `5` for `in five minutes` or `-15` for `fifteen minutes
               ago`).
        :param float relative_second: (optional) A recognized mention of a relative
               time, represented numerically as an offset in seconds from the current time
               (for example, `10` for `in ten seconds` or `-30` for `thirty seconds ago`).
        :param float specific_hour: (optional) A recognized specific hour mentioned
               as part of a time value (for example, `10` for `10:15 AM`.).
        :param float specific_minute: (optional) A recognized specific minute
               mentioned as part of a time value (for example, `15` for `10:15 AM`.).
        :param float specific_second: (optional) A recognized specific second
               mentioned as part of a time value (for example, `30` for `10:15:30 AM`.).
        :param str timezone: (optional) A recognized time zone mentioned as part of
               a time value (for example, `EST`).
        """
        self.calendar_type = calendar_type
        self.datetime_link = datetime_link
        self.festival = festival
        self.granularity = granularity
        self.range_link = range_link
        self.range_modifier = range_modifier
        self.relative_day = relative_day
        self.relative_month = relative_month
        self.relative_week = relative_week
        self.relative_weekend = relative_weekend
        self.relative_year = relative_year
        self.specific_day = specific_day
        self.specific_day_of_week = specific_day_of_week
        self.specific_month = specific_month
        self.specific_quarter = specific_quarter
        self.specific_year = specific_year
        self.numeric_value = numeric_value
        self.subtype = subtype
        self.part_of_day = part_of_day
        self.relative_hour = relative_hour
        self.relative_minute = relative_minute
        self.relative_second = relative_second
        self.specific_hour = specific_hour
        self.specific_minute = specific_minute
        self.specific_second = specific_second
        self.timezone = timezone

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntityInterpretation':
        """Initialize a RuntimeEntityInterpretation object from a json dictionary."""
        args = {}
        if (calendar_type := _dict.get('calendar_type')) is not None:
            args['calendar_type'] = calendar_type
        if (datetime_link := _dict.get('datetime_link')) is not None:
            args['datetime_link'] = datetime_link
        if (festival := _dict.get('festival')) is not None:
            args['festival'] = festival
        if (granularity := _dict.get('granularity')) is not None:
            args['granularity'] = granularity
        if (range_link := _dict.get('range_link')) is not None:
            args['range_link'] = range_link
        if (range_modifier := _dict.get('range_modifier')) is not None:
            args['range_modifier'] = range_modifier
        if (relative_day := _dict.get('relative_day')) is not None:
            args['relative_day'] = relative_day
        if (relative_month := _dict.get('relative_month')) is not None:
            args['relative_month'] = relative_month
        if (relative_week := _dict.get('relative_week')) is not None:
            args['relative_week'] = relative_week
        if (relative_weekend := _dict.get('relative_weekend')) is not None:
            args['relative_weekend'] = relative_weekend
        if (relative_year := _dict.get('relative_year')) is not None:
            args['relative_year'] = relative_year
        if (specific_day := _dict.get('specific_day')) is not None:
            args['specific_day'] = specific_day
        if (specific_day_of_week :=
                _dict.get('specific_day_of_week')) is not None:
            args['specific_day_of_week'] = specific_day_of_week
        if (specific_month := _dict.get('specific_month')) is not None:
            args['specific_month'] = specific_month
        if (specific_quarter := _dict.get('specific_quarter')) is not None:
            args['specific_quarter'] = specific_quarter
        if (specific_year := _dict.get('specific_year')) is not None:
            args['specific_year'] = specific_year
        if (numeric_value := _dict.get('numeric_value')) is not None:
            args['numeric_value'] = numeric_value
        if (subtype := _dict.get('subtype')) is not None:
            args['subtype'] = subtype
        if (part_of_day := _dict.get('part_of_day')) is not None:
            args['part_of_day'] = part_of_day
        if (relative_hour := _dict.get('relative_hour')) is not None:
            args['relative_hour'] = relative_hour
        if (relative_minute := _dict.get('relative_minute')) is not None:
            args['relative_minute'] = relative_minute
        if (relative_second := _dict.get('relative_second')) is not None:
            args['relative_second'] = relative_second
        if (specific_hour := _dict.get('specific_hour')) is not None:
            args['specific_hour'] = specific_hour
        if (specific_minute := _dict.get('specific_minute')) is not None:
            args['specific_minute'] = specific_minute
        if (specific_second := _dict.get('specific_second')) is not None:
            args['specific_second'] = specific_second
        if (timezone := _dict.get('timezone')) is not None:
            args['timezone'] = timezone
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntityInterpretation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'calendar_type') and self.calendar_type is not None:
            _dict['calendar_type'] = self.calendar_type
        if hasattr(self, 'datetime_link') and self.datetime_link is not None:
            _dict['datetime_link'] = self.datetime_link
        if hasattr(self, 'festival') and self.festival is not None:
            _dict['festival'] = self.festival
        if hasattr(self, 'granularity') and self.granularity is not None:
            _dict['granularity'] = self.granularity
        if hasattr(self, 'range_link') and self.range_link is not None:
            _dict['range_link'] = self.range_link
        if hasattr(self, 'range_modifier') and self.range_modifier is not None:
            _dict['range_modifier'] = self.range_modifier
        if hasattr(self, 'relative_day') and self.relative_day is not None:
            _dict['relative_day'] = self.relative_day
        if hasattr(self, 'relative_month') and self.relative_month is not None:
            _dict['relative_month'] = self.relative_month
        if hasattr(self, 'relative_week') and self.relative_week is not None:
            _dict['relative_week'] = self.relative_week
        if hasattr(self,
                   'relative_weekend') and self.relative_weekend is not None:
            _dict['relative_weekend'] = self.relative_weekend
        if hasattr(self, 'relative_year') and self.relative_year is not None:
            _dict['relative_year'] = self.relative_year
        if hasattr(self, 'specific_day') and self.specific_day is not None:
            _dict['specific_day'] = self.specific_day
        if hasattr(self, 'specific_day_of_week'
                  ) and self.specific_day_of_week is not None:
            _dict['specific_day_of_week'] = self.specific_day_of_week
        if hasattr(self, 'specific_month') and self.specific_month is not None:
            _dict['specific_month'] = self.specific_month
        if hasattr(self,
                   'specific_quarter') and self.specific_quarter is not None:
            _dict['specific_quarter'] = self.specific_quarter
        if hasattr(self, 'specific_year') and self.specific_year is not None:
            _dict['specific_year'] = self.specific_year
        if hasattr(self, 'numeric_value') and self.numeric_value is not None:
            _dict['numeric_value'] = self.numeric_value
        if hasattr(self, 'subtype') and self.subtype is not None:
            _dict['subtype'] = self.subtype
        if hasattr(self, 'part_of_day') and self.part_of_day is not None:
            _dict['part_of_day'] = self.part_of_day
        if hasattr(self, 'relative_hour') and self.relative_hour is not None:
            _dict['relative_hour'] = self.relative_hour
        if hasattr(self,
                   'relative_minute') and self.relative_minute is not None:
            _dict['relative_minute'] = self.relative_minute
        if hasattr(self,
                   'relative_second') and self.relative_second is not None:
            _dict['relative_second'] = self.relative_second
        if hasattr(self, 'specific_hour') and self.specific_hour is not None:
            _dict['specific_hour'] = self.specific_hour
        if hasattr(self,
                   'specific_minute') and self.specific_minute is not None:
            _dict['specific_minute'] = self.specific_minute
        if hasattr(self,
                   'specific_second') and self.specific_second is not None:
            _dict['specific_second'] = self.specific_second
        if hasattr(self, 'timezone') and self.timezone is not None:
            _dict['timezone'] = self.timezone
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeEntityInterpretation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeEntityInterpretation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeEntityInterpretation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class GranularityEnum(str, Enum):
        """
        The precision or duration of a time range specified by a recognized `@sys-time` or
        `@sys-date` entity.
        """

        DAY = 'day'
        FORTNIGHT = 'fortnight'
        HOUR = 'hour'
        INSTANT = 'instant'
        MINUTE = 'minute'
        MONTH = 'month'
        QUARTER = 'quarter'
        SECOND = 'second'
        WEEK = 'week'
        WEEKEND = 'weekend'
        YEAR = 'year'


class RuntimeEntityRole:
    """
    An object describing the role played by a system entity that is specifies the
    beginning or end of a range recognized in the user input. This property is included
    only if the new system entities are enabled for the skill.

    :param str type: (optional) The relationship of the entity to the range.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeEntityRole object.

        :param str type: (optional) The relationship of the entity to the range.
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntityRole':
        """Initialize a RuntimeEntityRole object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntityRole object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeEntityRole object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeEntityRole') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeEntityRole') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The relationship of the entity to the range.
        """

        DATE_FROM = 'date_from'
        DATE_TO = 'date_to'
        NUMBER_FROM = 'number_from'
        NUMBER_TO = 'number_to'
        TIME_FROM = 'time_from'
        TIME_TO = 'time_to'


class RuntimeIntent:
    """
    An intent identified in the user input.

    :param str intent: The name of the recognized intent.
    :param float confidence: (optional) A decimal percentage that represents
          confidence in the intent. If you are specifying an intent as part of a request,
          but you do not have a calculated confidence value, specify `1`.
    :param str skill: (optional) The skill that identified the intent. Currently,
          the only possible values are `main skill` for the dialog skill (if enabled) and
          `actions skill` for the action skill.
          This property is present only if the assistant has both a dialog skill and an
          action skill.
    """

    def __init__(
        self,
        intent: str,
        *,
        confidence: Optional[float] = None,
        skill: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeIntent object.

        :param str intent: The name of the recognized intent.
        :param float confidence: (optional) A decimal percentage that represents
               confidence in the intent. If you are specifying an intent as part of a
               request, but you do not have a calculated confidence value, specify `1`.
        :param str skill: (optional) The skill that identified the intent.
               Currently, the only possible values are `main skill` for the dialog skill
               (if enabled) and `actions skill` for the action skill.
               This property is present only if the assistant has both a dialog skill and
               an action skill.
        """
        self.intent = intent
        self.confidence = confidence
        self.skill = skill

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeIntent':
        """Initialize a RuntimeIntent object from a json dictionary."""
        args = {}
        if (intent := _dict.get('intent')) is not None:
            args['intent'] = intent
        else:
            raise ValueError(
                'Required property \'intent\' not present in RuntimeIntent JSON'
            )
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        if (skill := _dict.get('skill')) is not None:
            args['skill'] = skill
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeIntent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'skill') and self.skill is not None:
            _dict['skill'] = self.skill
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeIntent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'RuntimeIntent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'RuntimeIntent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGeneric:
    """
    RuntimeResponseGeneric.

    """

    def __init__(self,) -> None:
        """
        Initialize a RuntimeResponseGeneric object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'RuntimeResponseGenericRuntimeResponseTypeText',
                'RuntimeResponseGenericRuntimeResponseTypePause',
                'RuntimeResponseGenericRuntimeResponseTypeImage',
                'RuntimeResponseGenericRuntimeResponseTypeOption',
                'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent',
                'RuntimeResponseGenericRuntimeResponseTypeSuggestion',
                'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer',
                'RuntimeResponseGenericRuntimeResponseTypeSearch',
                'RuntimeResponseGenericRuntimeResponseTypeUserDefined',
                'RuntimeResponseGenericRuntimeResponseTypeVideo',
                'RuntimeResponseGenericRuntimeResponseTypeAudio',
                'RuntimeResponseGenericRuntimeResponseTypeIframe',
                'RuntimeResponseGenericRuntimeResponseTypeDate'
            ]))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeResponseGeneric':
        """Initialize a RuntimeResponseGeneric object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'RuntimeResponseGeneric'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join([
                'RuntimeResponseGenericRuntimeResponseTypeText',
                'RuntimeResponseGenericRuntimeResponseTypePause',
                'RuntimeResponseGenericRuntimeResponseTypeImage',
                'RuntimeResponseGenericRuntimeResponseTypeOption',
                'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent',
                'RuntimeResponseGenericRuntimeResponseTypeSuggestion',
                'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer',
                'RuntimeResponseGenericRuntimeResponseTypeSearch',
                'RuntimeResponseGenericRuntimeResponseTypeUserDefined',
                'RuntimeResponseGenericRuntimeResponseTypeVideo',
                'RuntimeResponseGenericRuntimeResponseTypeAudio',
                'RuntimeResponseGenericRuntimeResponseTypeIframe',
                'RuntimeResponseGenericRuntimeResponseTypeDate'
            ]))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a RuntimeResponseGeneric object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping['audio'] = 'RuntimeResponseGenericRuntimeResponseTypeAudio'
        mapping[
            'channel_transfer'] = 'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer'
        mapping[
            'connect_to_agent'] = 'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent'
        mapping['date'] = 'RuntimeResponseGenericRuntimeResponseTypeDate'
        mapping['iframe'] = 'RuntimeResponseGenericRuntimeResponseTypeIframe'
        mapping['image'] = 'RuntimeResponseGenericRuntimeResponseTypeImage'
        mapping['option'] = 'RuntimeResponseGenericRuntimeResponseTypeOption'
        mapping[
            'suggestion'] = 'RuntimeResponseGenericRuntimeResponseTypeSuggestion'
        mapping['pause'] = 'RuntimeResponseGenericRuntimeResponseTypePause'
        mapping['search'] = 'RuntimeResponseGenericRuntimeResponseTypeSearch'
        mapping['text'] = 'RuntimeResponseGenericRuntimeResponseTypeText'
        mapping[
            'user_defined'] = 'RuntimeResponseGenericRuntimeResponseTypeUserDefined'
        mapping['video'] = 'RuntimeResponseGenericRuntimeResponseTypeVideo'
        disc_value = _dict.get('response_type')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'response_type\' not found in RuntimeResponseGeneric JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class SearchResult:
    """
    SearchResult.

    :param str id: The unique identifier of the document in the Discovery service
          collection.
          This property is included in responses from search skills, which are available
          only to Plus or Enterprise plan users.
    :param SearchResultMetadata result_metadata: An object containing search result
          metadata from the Discovery service.
    :param str body: (optional) A description of the search result. This is taken
          from an abstract, summary, or highlight field in the Discovery service response,
          as specified in the search skill configuration.
    :param str title: (optional) The title of the search result. This is taken from
          a title or name field in the Discovery service response, as specified in the
          search skill configuration.
    :param str url: (optional) The URL of the original data object in its native
          data source.
    :param SearchResultHighlight highlight: (optional) An object containing segments
          of text from search results with query-matching text highlighted using HTML
          `<em>` tags.
    :param List[SearchResultAnswer] answers: (optional) An array specifying segments
          of text within the result that were identified as direct answers to the search
          query. Currently, only the single answer with the highest confidence (if any) is
          returned.
          **Notes:**
           - Answer finding is available only if the search skill is connected to a
          Discovery v2 service instance.
           - Answer finding is not supported on IBM Cloud Pak for Data.
    """

    def __init__(
        self,
        id: str,
        result_metadata: 'SearchResultMetadata',
        *,
        body: Optional[str] = None,
        title: Optional[str] = None,
        url: Optional[str] = None,
        highlight: Optional['SearchResultHighlight'] = None,
        answers: Optional[List['SearchResultAnswer']] = None,
    ) -> None:
        """
        Initialize a SearchResult object.

        :param str id: The unique identifier of the document in the Discovery
               service collection.
               This property is included in responses from search skills, which are
               available only to Plus or Enterprise plan users.
        :param SearchResultMetadata result_metadata: An object containing search
               result metadata from the Discovery service.
        :param str body: (optional) A description of the search result. This is
               taken from an abstract, summary, or highlight field in the Discovery
               service response, as specified in the search skill configuration.
        :param str title: (optional) The title of the search result. This is taken
               from a title or name field in the Discovery service response, as specified
               in the search skill configuration.
        :param str url: (optional) The URL of the original data object in its
               native data source.
        :param SearchResultHighlight highlight: (optional) An object containing
               segments of text from search results with query-matching text highlighted
               using HTML `<em>` tags.
        :param List[SearchResultAnswer] answers: (optional) An array specifying
               segments of text within the result that were identified as direct answers
               to the search query. Currently, only the single answer with the highest
               confidence (if any) is returned.
               **Notes:**
                - Answer finding is available only if the search skill is connected to a
               Discovery v2 service instance.
                - Answer finding is not supported on IBM Cloud Pak for Data.
        """
        self.id = id
        self.result_metadata = result_metadata
        self.body = body
        self.title = title
        self.url = url
        self.highlight = highlight
        self.answers = answers

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResult':
        """Initialize a SearchResult object from a json dictionary."""
        args = {}
        if (id := _dict.get('id')) is not None:
            args['id'] = id
        else:
            raise ValueError(
                'Required property \'id\' not present in SearchResult JSON')
        if (result_metadata := _dict.get('result_metadata')) is not None:
            args['result_metadata'] = SearchResultMetadata.from_dict(
                result_metadata)
        else:
            raise ValueError(
                'Required property \'result_metadata\' not present in SearchResult JSON'
            )
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (highlight := _dict.get('highlight')) is not None:
            args['highlight'] = SearchResultHighlight.from_dict(highlight)
        if (answers := _dict.get('answers')) is not None:
            args['answers'] = [SearchResultAnswer.from_dict(v) for v in answers]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResult object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self,
                   'result_metadata') and self.result_metadata is not None:
            if isinstance(self.result_metadata, dict):
                _dict['result_metadata'] = self.result_metadata
            else:
                _dict['result_metadata'] = self.result_metadata.to_dict()
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'highlight') and self.highlight is not None:
            if isinstance(self.highlight, dict):
                _dict['highlight'] = self.highlight
            else:
                _dict['highlight'] = self.highlight.to_dict()
        if hasattr(self, 'answers') and self.answers is not None:
            answers_list = []
            for v in self.answers:
                if isinstance(v, dict):
                    answers_list.append(v)
                else:
                    answers_list.append(v.to_dict())
            _dict['answers'] = answers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResult object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResult') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResult') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchResultAnswer:
    """
    An object specifing a segment of text that was identified as a direct answer to the
    search query.

    :param str text: The text of the answer.
    :param float confidence: The confidence score for the answer, as returned by the
          Discovery service.
    """

    def __init__(
        self,
        text: str,
        confidence: float,
    ) -> None:
        """
        Initialize a SearchResultAnswer object.

        :param str text: The text of the answer.
        :param float confidence: The confidence score for the answer, as returned
               by the Discovery service.
        """
        self.text = text
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultAnswer':
        """Initialize a SearchResultAnswer object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in SearchResultAnswer JSON'
            )
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        else:
            raise ValueError(
                'Required property \'confidence\' not present in SearchResultAnswer JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultAnswer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResultAnswer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResultAnswer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResultAnswer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchResultHighlight:
    """
    An object containing segments of text from search results with query-matching text
    highlighted using HTML `<em>` tags.

    :param List[str] body: (optional) An array of strings containing segments taken
          from body text in the search results, with query-matching substrings
          highlighted.
    :param List[str] title: (optional) An array of strings containing segments taken
          from title text in the search results, with query-matching substrings
          highlighted.
    :param List[str] url: (optional) An array of strings containing segments taken
          from URLs in the search results, with query-matching substrings highlighted.

    This type supports additional properties of type List[str]. An array of strings
    containing segments taken from a field in the search results that is not mapped to the
    `body`, `title`, or `url` property, with query-matching substrings highlighted. The
    property name is the name of the field in the Discovery collection.
    """

    # The set of defined properties for the class
    _properties = frozenset(['body', 'title', 'url'])

    def __init__(
        self,
        *,
        body: Optional[List[str]] = None,
        title: Optional[List[str]] = None,
        url: Optional[List[str]] = None,
        **kwargs: Optional[List[str]],
    ) -> None:
        """
        Initialize a SearchResultHighlight object.

        :param List[str] body: (optional) An array of strings containing segments
               taken from body text in the search results, with query-matching substrings
               highlighted.
        :param List[str] title: (optional) An array of strings containing segments
               taken from title text in the search results, with query-matching substrings
               highlighted.
        :param List[str] url: (optional) An array of strings containing segments
               taken from URLs in the search results, with query-matching substrings
               highlighted.
        :param List[str] **kwargs: (optional) An array of strings containing
               segments taken from a field in the search results that is not mapped to the
               `body`, `title`, or `url` property, with query-matching substrings
               highlighted. The property name is the name of the field in the Discovery
               collection.
        """
        self.body = body
        self.title = title
        self.url = url
        for k, v in kwargs.items():
            if k not in SearchResultHighlight._properties:
                if not isinstance(v, List):
                    raise ValueError(
                        'Value for additional property {} must be of type List[Foo]'
                        .format(k))
                _v = []
                for elem in v:
                    if not isinstance(elem, str):
                        raise ValueError(
                            'Value for additional property {} must be of type List[str]'
                            .format(k))
                    _v.append(elem)
                setattr(self, k, _v)
            else:
                raise ValueError(
                    'Property {} cannot be specified as an additional property'.
                    format(k))

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultHighlight':
        """Initialize a SearchResultHighlight object from a json dictionary."""
        args = {}
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        for k, v in _dict.items():
            if k not in cls._properties:
                if not isinstance(v, List):
                    raise ValueError(
                        'Value for additional property {} must be of type List[str]'
                        .format(k))
                _v = []
                for elem in v:
                    if not isinstance(elem, str):
                        raise ValueError(
                            'Value for additional property {} must be of type List[str]'
                            .format(k))
                    _v.append(elem)
                args[k] = _v
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultHighlight object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        for k in [
                _k for _k in vars(self).keys()
                if _k not in SearchResultHighlight._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of SearchResultHighlight in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in SearchResultHighlight._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of SearchResultHighlight"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in SearchResultHighlight._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in SearchResultHighlight._properties:
                if not isinstance(v, List):
                    raise ValueError(
                        'Value for additional property {} must be of type List[str]'
                        .format(k))
                _v = []
                for elem in v:
                    if not isinstance(elem, str):
                        raise ValueError(
                            'Value for additional property {} must be of type List[str]'
                            .format(k))
                    _v.append(elem)
                setattr(self, k, _v)
            else:
                raise ValueError(
                    'Property {} cannot be specified as an additional property'.
                    format(k))

    def __str__(self) -> str:
        """Return a `str` version of this SearchResultHighlight object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResultHighlight') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResultHighlight') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchResultMetadata:
    """
    An object containing search result metadata from the Discovery service.

    :param float confidence: (optional) The confidence score for the given result,
          as returned by the Discovery service.
    :param float score: (optional) An unbounded measure of the relevance of a
          particular result, dependent on the query and matching document. A higher score
          indicates a greater match to the query parameters.
    """

    def __init__(
        self,
        *,
        confidence: Optional[float] = None,
        score: Optional[float] = None,
    ) -> None:
        """
        Initialize a SearchResultMetadata object.

        :param float confidence: (optional) The confidence score for the given
               result, as returned by the Discovery service.
        :param float score: (optional) An unbounded measure of the relevance of a
               particular result, dependent on the query and matching document. A higher
               score indicates a greater match to the query parameters.
        """
        self.confidence = confidence
        self.score = score

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultMetadata':
        """Initialize a SearchResultMetadata object from a json dictionary."""
        args = {}
        if (confidence := _dict.get('confidence')) is not None:
            args['confidence'] = confidence
        if (score := _dict.get('score')) is not None:
            args['score'] = score
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchResultMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        if hasattr(self, 'score') and self.score is not None:
            _dict['score'] = self.score
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchResultMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchResultMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchResultMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettings:
    """
    An object describing the search skill configuration.
    **Note:** Search settings are not supported in **Import skills** requests, and are not
    included in **Export skills** responses.

    :param SearchSettingsDiscovery discovery: Configuration settings for the Watson
          Discovery service instance used by the search integration.
    :param SearchSettingsMessages messages: The messages included with responses
          from the search integration.
    :param SearchSettingsSchemaMapping schema_mapping: The mapping between fields in
          the Watson Discovery collection and properties in the search response.
    :param SearchSettingsElasticSearch elastic_search: (optional) Configuration
          settings for the Elasticsearch service used by the search integration. You can
          provide either basic auth or apiKey auth.
    :param SearchSettingsConversationalSearch conversational_search: (optional)
          Configuration settings for conversational search.
    :param SearchSettingsServerSideSearch server_side_search: (optional)
          Configuration settings for the server-side search service used by the search
          integration. You can provide either basic auth, apiKey auth or none.
    :param SearchSettingsClientSideSearch client_side_search: (optional)
          Configuration settings for the client-side search service or server-side search
          service used by the search integration.
    """

    def __init__(
        self,
        discovery: 'SearchSettingsDiscovery',
        messages: 'SearchSettingsMessages',
        schema_mapping: 'SearchSettingsSchemaMapping',
        *,
        elastic_search: Optional['SearchSettingsElasticSearch'] = None,
        conversational_search: Optional[
            'SearchSettingsConversationalSearch'] = None,
        server_side_search: Optional['SearchSettingsServerSideSearch'] = None,
        client_side_search: Optional['SearchSettingsClientSideSearch'] = None,
    ) -> None:
        """
        Initialize a SearchSettings object.

        :param SearchSettingsDiscovery discovery: Configuration settings for the
               Watson Discovery service instance used by the search integration.
        :param SearchSettingsMessages messages: The messages included with
               responses from the search integration.
        :param SearchSettingsSchemaMapping schema_mapping: The mapping between
               fields in the Watson Discovery collection and properties in the search
               response.
        :param SearchSettingsElasticSearch elastic_search: (optional) Configuration
               settings for the Elasticsearch service used by the search integration. You
               can provide either basic auth or apiKey auth.
        :param SearchSettingsConversationalSearch conversational_search: (optional)
               Configuration settings for conversational search.
        :param SearchSettingsServerSideSearch server_side_search: (optional)
               Configuration settings for the server-side search service used by the
               search integration. You can provide either basic auth, apiKey auth or none.
        :param SearchSettingsClientSideSearch client_side_search: (optional)
               Configuration settings for the client-side search service or server-side
               search service used by the search integration.
        """
        self.discovery = discovery
        self.messages = messages
        self.schema_mapping = schema_mapping
        self.elastic_search = elastic_search
        self.conversational_search = conversational_search
        self.server_side_search = server_side_search
        self.client_side_search = client_side_search

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettings':
        """Initialize a SearchSettings object from a json dictionary."""
        args = {}
        if (discovery := _dict.get('discovery')) is not None:
            args['discovery'] = SearchSettingsDiscovery.from_dict(discovery)
        else:
            raise ValueError(
                'Required property \'discovery\' not present in SearchSettings JSON'
            )
        if (messages := _dict.get('messages')) is not None:
            args['messages'] = SearchSettingsMessages.from_dict(messages)
        else:
            raise ValueError(
                'Required property \'messages\' not present in SearchSettings JSON'
            )
        if (schema_mapping := _dict.get('schema_mapping')) is not None:
            args['schema_mapping'] = SearchSettingsSchemaMapping.from_dict(
                schema_mapping)
        else:
            raise ValueError(
                'Required property \'schema_mapping\' not present in SearchSettings JSON'
            )
        if (elastic_search := _dict.get('elastic_search')) is not None:
            args['elastic_search'] = SearchSettingsElasticSearch.from_dict(
                elastic_search)
        if (conversational_search :=
                _dict.get('conversational_search')) is not None:
            args[
                'conversational_search'] = SearchSettingsConversationalSearch.from_dict(
                    conversational_search)
        if (server_side_search := _dict.get('server_side_search')) is not None:
            args[
                'server_side_search'] = SearchSettingsServerSideSearch.from_dict(
                    server_side_search)
        if (client_side_search := _dict.get('client_side_search')) is not None:
            args[
                'client_side_search'] = SearchSettingsClientSideSearch.from_dict(
                    client_side_search)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'discovery') and self.discovery is not None:
            if isinstance(self.discovery, dict):
                _dict['discovery'] = self.discovery
            else:
                _dict['discovery'] = self.discovery.to_dict()
        if hasattr(self, 'messages') and self.messages is not None:
            if isinstance(self.messages, dict):
                _dict['messages'] = self.messages
            else:
                _dict['messages'] = self.messages.to_dict()
        if hasattr(self, 'schema_mapping') and self.schema_mapping is not None:
            if isinstance(self.schema_mapping, dict):
                _dict['schema_mapping'] = self.schema_mapping
            else:
                _dict['schema_mapping'] = self.schema_mapping.to_dict()
        if hasattr(self, 'elastic_search') and self.elastic_search is not None:
            if isinstance(self.elastic_search, dict):
                _dict['elastic_search'] = self.elastic_search
            else:
                _dict['elastic_search'] = self.elastic_search.to_dict()
        if hasattr(self, 'conversational_search'
                  ) and self.conversational_search is not None:
            if isinstance(self.conversational_search, dict):
                _dict['conversational_search'] = self.conversational_search
            else:
                _dict[
                    'conversational_search'] = self.conversational_search.to_dict(
                    )
        if hasattr(
                self,
                'server_side_search') and self.server_side_search is not None:
            if isinstance(self.server_side_search, dict):
                _dict['server_side_search'] = self.server_side_search
            else:
                _dict['server_side_search'] = self.server_side_search.to_dict()
        if hasattr(
                self,
                'client_side_search') and self.client_side_search is not None:
            if isinstance(self.client_side_search, dict):
                _dict['client_side_search'] = self.client_side_search
            else:
                _dict['client_side_search'] = self.client_side_search.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsClientSideSearch:
    """
    Configuration settings for the client-side search service or server-side search
    service used by the search integration.

    :param str filter: (optional) The filter string that is applied to the search
          results.
    :param dict metadata: (optional) The metadata object.
    """

    def __init__(
        self,
        *,
        filter: Optional[str] = None,
        metadata: Optional[dict] = None,
    ) -> None:
        """
        Initialize a SearchSettingsClientSideSearch object.

        :param str filter: (optional) The filter string that is applied to the
               search results.
        :param dict metadata: (optional) The metadata object.
        """
        self.filter = filter
        self.metadata = metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsClientSideSearch':
        """Initialize a SearchSettingsClientSideSearch object from a json dictionary."""
        args = {}
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsClientSideSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsClientSideSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsClientSideSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsClientSideSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsConversationalSearch:
    """
    Configuration settings for conversational search.

    :param bool enabled: Whether to enable conversational search.
    :param SearchSettingsConversationalSearchResponseLength response_length:
          (optional)
    :param SearchSettingsConversationalSearchSearchConfidence search_confidence:
          (optional)
    """

    def __init__(
        self,
        enabled: bool,
        *,
        response_length: Optional[
            'SearchSettingsConversationalSearchResponseLength'] = None,
        search_confidence: Optional[
            'SearchSettingsConversationalSearchSearchConfidence'] = None,
    ) -> None:
        """
        Initialize a SearchSettingsConversationalSearch object.

        :param bool enabled: Whether to enable conversational search.
        :param SearchSettingsConversationalSearchResponseLength response_length:
               (optional)
        :param SearchSettingsConversationalSearchSearchConfidence
               search_confidence: (optional)
        """
        self.enabled = enabled
        self.response_length = response_length
        self.search_confidence = search_confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsConversationalSearch':
        """Initialize a SearchSettingsConversationalSearch object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        else:
            raise ValueError(
                'Required property \'enabled\' not present in SearchSettingsConversationalSearch JSON'
            )
        if (response_length := _dict.get('response_length')) is not None:
            args[
                'response_length'] = SearchSettingsConversationalSearchResponseLength.from_dict(
                    response_length)
        if (search_confidence := _dict.get('search_confidence')) is not None:
            args[
                'search_confidence'] = SearchSettingsConversationalSearchSearchConfidence.from_dict(
                    search_confidence)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsConversationalSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self,
                   'response_length') and self.response_length is not None:
            if isinstance(self.response_length, dict):
                _dict['response_length'] = self.response_length
            else:
                _dict['response_length'] = self.response_length.to_dict()
        if hasattr(self,
                   'search_confidence') and self.search_confidence is not None:
            if isinstance(self.search_confidence, dict):
                _dict['search_confidence'] = self.search_confidence
            else:
                _dict['search_confidence'] = self.search_confidence.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsConversationalSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsConversationalSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsConversationalSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsConversationalSearchResponseLength:
    """
    SearchSettingsConversationalSearchResponseLength.

    :param str option: (optional) The response length option. It controls the length
          of the generated response.
    """

    def __init__(
        self,
        *,
        option: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSettingsConversationalSearchResponseLength object.

        :param str option: (optional) The response length option. It controls the
               length of the generated response.
        """
        self.option = option

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'SearchSettingsConversationalSearchResponseLength':
        """Initialize a SearchSettingsConversationalSearchResponseLength object from a json dictionary."""
        args = {}
        if (option := _dict.get('option')) is not None:
            args['option'] = option
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsConversationalSearchResponseLength object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'option') and self.option is not None:
            _dict['option'] = self.option
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsConversationalSearchResponseLength object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'SearchSettingsConversationalSearchResponseLength') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'SearchSettingsConversationalSearchResponseLength') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class OptionEnum(str, Enum):
        """
        The response length option. It controls the length of the generated response.
        """

        CONCISE = 'concise'
        MODERATE = 'moderate'
        VERBOSE = 'verbose'


class SearchSettingsConversationalSearchSearchConfidence:
    """
    SearchSettingsConversationalSearchSearchConfidence.

    :param str threshold: (optional) The search confidence threshold.
           It controls the tendency for conversational search to produce “I don't know”
          answers.
    """

    def __init__(
        self,
        *,
        threshold: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSettingsConversationalSearchSearchConfidence object.

        :param str threshold: (optional) The search confidence threshold.
                It controls the tendency for conversational search to produce “I don't
               know” answers.
        """
        self.threshold = threshold

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'SearchSettingsConversationalSearchSearchConfidence':
        """Initialize a SearchSettingsConversationalSearchSearchConfidence object from a json dictionary."""
        args = {}
        if (threshold := _dict.get('threshold')) is not None:
            args['threshold'] = threshold
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsConversationalSearchSearchConfidence object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'threshold') and self.threshold is not None:
            _dict['threshold'] = self.threshold
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsConversationalSearchSearchConfidence object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'SearchSettingsConversationalSearchSearchConfidence'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'SearchSettingsConversationalSearchSearchConfidence'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ThresholdEnum(str, Enum):
        """
        The search confidence threshold.
         It controls the tendency for conversational search to produce “I don't know”
        answers.
        """

        RARELY = 'rarely'
        LESS_OFTEN = 'less_often'
        MORE_OFTEN = 'more_often'
        MOST_OFTEN = 'most_often'


class SearchSettingsDiscovery:
    """
    Configuration settings for the Watson Discovery service instance used by the search
    integration.

    :param str instance_id: The ID for the Watson Discovery service instance.
    :param str project_id: The ID for the Watson Discovery project.
    :param str url: The URL for the Watson Discovery service instance.
    :param int max_primary_results: (optional) The maximum number of primary results
          to include in the response.
    :param int max_total_results: (optional) The maximum total number of primary and
          additional results to include in the response.
    :param float confidence_threshold: (optional) The minimum confidence threshold
          for included results. Any results with a confidence below this threshold will be
          discarded.
    :param bool highlight: (optional) Whether to include the most relevant passages
          of text in the **highlight** property of each result.
    :param bool find_answers: (optional) Whether to use the answer finding feature
          to emphasize answers within highlighted passages. This property is ignored if
          **highlight**=`false`.
          **Notes:**
           - Answer finding is available only if the search skill is connected to a
          Discovery v2 service instance.
           - Answer finding is not supported on IBM Cloud Pak for Data.
    :param SearchSettingsDiscoveryAuthentication authentication: Authentication
          information for the Watson Discovery service. For more information, see the
          [Watson Discovery
          documentation](https://cloud.ibm.com/apidocs/discovery-data#authentication).
           **Note:** You must specify either **basic** or **bearer**, but not both.
    """

    def __init__(
        self,
        instance_id: str,
        project_id: str,
        url: str,
        authentication: 'SearchSettingsDiscoveryAuthentication',
        *,
        max_primary_results: Optional[int] = None,
        max_total_results: Optional[int] = None,
        confidence_threshold: Optional[float] = None,
        highlight: Optional[bool] = None,
        find_answers: Optional[bool] = None,
    ) -> None:
        """
        Initialize a SearchSettingsDiscovery object.

        :param str instance_id: The ID for the Watson Discovery service instance.
        :param str project_id: The ID for the Watson Discovery project.
        :param str url: The URL for the Watson Discovery service instance.
        :param SearchSettingsDiscoveryAuthentication authentication: Authentication
               information for the Watson Discovery service. For more information, see the
               [Watson Discovery
               documentation](https://cloud.ibm.com/apidocs/discovery-data#authentication).
                **Note:** You must specify either **basic** or **bearer**, but not both.
        :param int max_primary_results: (optional) The maximum number of primary
               results to include in the response.
        :param int max_total_results: (optional) The maximum total number of
               primary and additional results to include in the response.
        :param float confidence_threshold: (optional) The minimum confidence
               threshold for included results. Any results with a confidence below this
               threshold will be discarded.
        :param bool highlight: (optional) Whether to include the most relevant
               passages of text in the **highlight** property of each result.
        :param bool find_answers: (optional) Whether to use the answer finding
               feature to emphasize answers within highlighted passages. This property is
               ignored if **highlight**=`false`.
               **Notes:**
                - Answer finding is available only if the search skill is connected to a
               Discovery v2 service instance.
                - Answer finding is not supported on IBM Cloud Pak for Data.
        """
        self.instance_id = instance_id
        self.project_id = project_id
        self.url = url
        self.max_primary_results = max_primary_results
        self.max_total_results = max_total_results
        self.confidence_threshold = confidence_threshold
        self.highlight = highlight
        self.find_answers = find_answers
        self.authentication = authentication

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsDiscovery':
        """Initialize a SearchSettingsDiscovery object from a json dictionary."""
        args = {}
        if (instance_id := _dict.get('instance_id')) is not None:
            args['instance_id'] = instance_id
        else:
            raise ValueError(
                'Required property \'instance_id\' not present in SearchSettingsDiscovery JSON'
            )
        if (project_id := _dict.get('project_id')) is not None:
            args['project_id'] = project_id
        else:
            raise ValueError(
                'Required property \'project_id\' not present in SearchSettingsDiscovery JSON'
            )
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsDiscovery JSON'
            )
        if (max_primary_results :=
                _dict.get('max_primary_results')) is not None:
            args['max_primary_results'] = max_primary_results
        if (max_total_results := _dict.get('max_total_results')) is not None:
            args['max_total_results'] = max_total_results
        if (confidence_threshold :=
                _dict.get('confidence_threshold')) is not None:
            args['confidence_threshold'] = confidence_threshold
        if (highlight := _dict.get('highlight')) is not None:
            args['highlight'] = highlight
        if (find_answers := _dict.get('find_answers')) is not None:
            args['find_answers'] = find_answers
        if (authentication := _dict.get('authentication')) is not None:
            args[
                'authentication'] = SearchSettingsDiscoveryAuthentication.from_dict(
                    authentication)
        else:
            raise ValueError(
                'Required property \'authentication\' not present in SearchSettingsDiscovery JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsDiscovery object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'project_id') and self.project_id is not None:
            _dict['project_id'] = self.project_id
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(
                self,
                'max_primary_results') and self.max_primary_results is not None:
            _dict['max_primary_results'] = self.max_primary_results
        if hasattr(self,
                   'max_total_results') and self.max_total_results is not None:
            _dict['max_total_results'] = self.max_total_results
        if hasattr(self, 'confidence_threshold'
                  ) and self.confidence_threshold is not None:
            _dict['confidence_threshold'] = self.confidence_threshold
        if hasattr(self, 'highlight') and self.highlight is not None:
            _dict['highlight'] = self.highlight
        if hasattr(self, 'find_answers') and self.find_answers is not None:
            _dict['find_answers'] = self.find_answers
        if hasattr(self, 'authentication') and self.authentication is not None:
            if isinstance(self.authentication, dict):
                _dict['authentication'] = self.authentication
            else:
                _dict['authentication'] = self.authentication.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsDiscovery object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsDiscovery') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsDiscovery') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsDiscoveryAuthentication:
    """
    Authentication information for the Watson Discovery service. For more information, see
    the [Watson Discovery
    documentation](https://cloud.ibm.com/apidocs/discovery-data#authentication).
     **Note:** You must specify either **basic** or **bearer**, but not both.

    :param str basic: (optional) The HTTP basic authentication credentials for
          Watson Discovery. Specify your Watson Discovery API key in the format
          `apikey:{apikey}`.
    :param str bearer: (optional) The authentication bearer token for Watson
          Discovery.
    """

    def __init__(
        self,
        *,
        basic: Optional[str] = None,
        bearer: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSettingsDiscoveryAuthentication object.

        :param str basic: (optional) The HTTP basic authentication credentials for
               Watson Discovery. Specify your Watson Discovery API key in the format
               `apikey:{apikey}`.
        :param str bearer: (optional) The authentication bearer token for Watson
               Discovery.
        """
        self.basic = basic
        self.bearer = bearer

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsDiscoveryAuthentication':
        """Initialize a SearchSettingsDiscoveryAuthentication object from a json dictionary."""
        args = {}
        if (basic := _dict.get('basic')) is not None:
            args['basic'] = basic
        if (bearer := _dict.get('bearer')) is not None:
            args['bearer'] = bearer
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsDiscoveryAuthentication object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'basic') and self.basic is not None:
            _dict['basic'] = self.basic
        if hasattr(self, 'bearer') and self.bearer is not None:
            _dict['bearer'] = self.bearer
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsDiscoveryAuthentication object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsDiscoveryAuthentication') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsDiscoveryAuthentication') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsElasticSearch:
    """
    Configuration settings for the Elasticsearch service used by the search integration.
    You can provide either basic auth or apiKey auth.

    :param str url: The URL for the Elasticsearch service.
    :param str port: The port number for the Elasticsearch service URL.
           **Note:** It can be omitted if a port number is appended to the URL.
    :param str username: (optional) The username of the basic authentication method.
    :param str password: (optional) The password of the basic authentication method.
          The credentials are not returned due to security reasons.
    :param str index: The Elasticsearch index to use for the search integration.
    :param List[object] filter: (optional) An array of filters that can be applied
          to the search results via the `$FILTER` variable in the `query_body`.For more
          information, see [Elasticsearch filter
          documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/filter-search-results.html).
    :param dict query_body: (optional) The Elasticsearch query object. For more
          information, see [Elasticsearch search API
          documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html).
    :param str managed_index: (optional) The Elasticsearch index for uploading
          documents. It is created automatically when the upload document option is
          selected from the user interface.
    :param str apikey: (optional) The API key of the apiKey authentication method.
          Use either basic auth or apiKey auth. The credentials are not returned due to
          security reasons.
    """

    def __init__(
        self,
        url: str,
        port: str,
        index: str,
        *,
        username: Optional[str] = None,
        password: Optional[str] = None,
        filter: Optional[List[object]] = None,
        query_body: Optional[dict] = None,
        managed_index: Optional[str] = None,
        apikey: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSettingsElasticSearch object.

        :param str url: The URL for the Elasticsearch service.
        :param str port: The port number for the Elasticsearch service URL.
                **Note:** It can be omitted if a port number is appended to the URL.
        :param str index: The Elasticsearch index to use for the search
               integration.
        :param str username: (optional) The username of the basic authentication
               method.
        :param str password: (optional) The password of the basic authentication
               method. The credentials are not returned due to security reasons.
        :param List[object] filter: (optional) An array of filters that can be
               applied to the search results via the `$FILTER` variable in the
               `query_body`.For more information, see [Elasticsearch filter
               documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/filter-search-results.html).
        :param dict query_body: (optional) The Elasticsearch query object. For more
               information, see [Elasticsearch search API
               documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html).
        :param str managed_index: (optional) The Elasticsearch index for uploading
               documents. It is created automatically when the upload document option is
               selected from the user interface.
        :param str apikey: (optional) The API key of the apiKey authentication
               method. Use either basic auth or apiKey auth. The credentials are not
               returned due to security reasons.
        """
        self.url = url
        self.port = port
        self.username = username
        self.password = password
        self.index = index
        self.filter = filter
        self.query_body = query_body
        self.managed_index = managed_index
        self.apikey = apikey

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsElasticSearch':
        """Initialize a SearchSettingsElasticSearch object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsElasticSearch JSON'
            )
        if (port := _dict.get('port')) is not None:
            args['port'] = port
        else:
            raise ValueError(
                'Required property \'port\' not present in SearchSettingsElasticSearch JSON'
            )
        if (username := _dict.get('username')) is not None:
            args['username'] = username
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        if (index := _dict.get('index')) is not None:
            args['index'] = index
        else:
            raise ValueError(
                'Required property \'index\' not present in SearchSettingsElasticSearch JSON'
            )
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (query_body := _dict.get('query_body')) is not None:
            args['query_body'] = query_body
        if (managed_index := _dict.get('managed_index')) is not None:
            args['managed_index'] = managed_index
        if (apikey := _dict.get('apikey')) is not None:
            args['apikey'] = apikey
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsElasticSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'index') and self.index is not None:
            _dict['index'] = self.index
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'query_body') and self.query_body is not None:
            _dict['query_body'] = self.query_body
        if hasattr(self, 'managed_index') and self.managed_index is not None:
            _dict['managed_index'] = self.managed_index
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsElasticSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsElasticSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsElasticSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsMessages:
    """
    The messages included with responses from the search integration.

    :param str success: The message to include in the response to a successful
          query.
    :param str error: The message to include in the response when the query
          encounters an error.
    :param str no_result: The message to include in the response when there is no
          result from the query.
    """

    def __init__(
        self,
        success: str,
        error: str,
        no_result: str,
    ) -> None:
        """
        Initialize a SearchSettingsMessages object.

        :param str success: The message to include in the response to a successful
               query.
        :param str error: The message to include in the response when the query
               encounters an error.
        :param str no_result: The message to include in the response when there is
               no result from the query.
        """
        self.success = success
        self.error = error
        self.no_result = no_result

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsMessages':
        """Initialize a SearchSettingsMessages object from a json dictionary."""
        args = {}
        if (success := _dict.get('success')) is not None:
            args['success'] = success
        else:
            raise ValueError(
                'Required property \'success\' not present in SearchSettingsMessages JSON'
            )
        if (error := _dict.get('error')) is not None:
            args['error'] = error
        else:
            raise ValueError(
                'Required property \'error\' not present in SearchSettingsMessages JSON'
            )
        if (no_result := _dict.get('no_result')) is not None:
            args['no_result'] = no_result
        else:
            raise ValueError(
                'Required property \'no_result\' not present in SearchSettingsMessages JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsMessages object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'success') and self.success is not None:
            _dict['success'] = self.success
        if hasattr(self, 'error') and self.error is not None:
            _dict['error'] = self.error
        if hasattr(self, 'no_result') and self.no_result is not None:
            _dict['no_result'] = self.no_result
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsMessages object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsMessages') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsMessages') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsSchemaMapping:
    """
    The mapping between fields in the Watson Discovery collection and properties in the
    search response.

    :param str url: The field in the collection to map to the **url** property of
          the response.
    :param str body: The field in the collection to map to the **body** property in
          the response.
    :param str title: The field in the collection to map to the **title** property
          for the schema.
    """

    def __init__(
        self,
        url: str,
        body: str,
        title: str,
    ) -> None:
        """
        Initialize a SearchSettingsSchemaMapping object.

        :param str url: The field in the collection to map to the **url** property
               of the response.
        :param str body: The field in the collection to map to the **body**
               property in the response.
        :param str title: The field in the collection to map to the **title**
               property for the schema.
        """
        self.url = url
        self.body = body
        self.title = title

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsSchemaMapping':
        """Initialize a SearchSettingsSchemaMapping object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsSchemaMapping JSON'
            )
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        else:
            raise ValueError(
                'Required property \'body\' not present in SearchSettingsSchemaMapping JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        else:
            raise ValueError(
                'Required property \'title\' not present in SearchSettingsSchemaMapping JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsSchemaMapping object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsSchemaMapping object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsSchemaMapping') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsSchemaMapping') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SearchSettingsServerSideSearch:
    """
    Configuration settings for the server-side search service used by the search
    integration. You can provide either basic auth, apiKey auth or none.

    :param str url: The URL of the server-side search service.
    :param str port: (optional) The port number of the server-side search service.
    :param str username: (optional) The username of the basic authentication method.
    :param str password: (optional) The password of the basic authentication method.
          The credentials are not returned due to security reasons.
    :param str filter: (optional) The filter string that is applied to the search
          results.
    :param dict metadata: (optional) The metadata object.
    :param str apikey: (optional) The API key of the apiKey authentication method.
          The credentails are not returned due to security reasons.
    :param bool no_auth: (optional) To clear previous auth, specify `no_auth =
          true`.
    :param str auth_type: (optional) The authorization type that is used.
    """

    def __init__(
        self,
        url: str,
        *,
        port: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        filter: Optional[str] = None,
        metadata: Optional[dict] = None,
        apikey: Optional[str] = None,
        no_auth: Optional[bool] = None,
        auth_type: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSettingsServerSideSearch object.

        :param str url: The URL of the server-side search service.
        :param str port: (optional) The port number of the server-side search
               service.
        :param str username: (optional) The username of the basic authentication
               method.
        :param str password: (optional) The password of the basic authentication
               method. The credentials are not returned due to security reasons.
        :param str filter: (optional) The filter string that is applied to the
               search results.
        :param dict metadata: (optional) The metadata object.
        :param str apikey: (optional) The API key of the apiKey authentication
               method. The credentails are not returned due to security reasons.
        :param bool no_auth: (optional) To clear previous auth, specify `no_auth =
               true`.
        :param str auth_type: (optional) The authorization type that is used.
        """
        self.url = url
        self.port = port
        self.username = username
        self.password = password
        self.filter = filter
        self.metadata = metadata
        self.apikey = apikey
        self.no_auth = no_auth
        self.auth_type = auth_type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettingsServerSideSearch':
        """Initialize a SearchSettingsServerSideSearch object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsServerSideSearch JSON'
            )
        if (port := _dict.get('port')) is not None:
            args['port'] = port
        if (username := _dict.get('username')) is not None:
            args['username'] = username
        if (password := _dict.get('password')) is not None:
            args['password'] = password
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (apikey := _dict.get('apikey')) is not None:
            args['apikey'] = apikey
        if (no_auth := _dict.get('no_auth')) is not None:
            args['no_auth'] = no_auth
        if (auth_type := _dict.get('auth_type')) is not None:
            args['auth_type'] = auth_type
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSettingsServerSideSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'port') and self.port is not None:
            _dict['port'] = self.port
        if hasattr(self, 'username') and self.username is not None:
            _dict['username'] = self.username
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'apikey') and self.apikey is not None:
            _dict['apikey'] = self.apikey
        if hasattr(self, 'no_auth') and self.no_auth is not None:
            _dict['no_auth'] = self.no_auth
        if hasattr(self, 'auth_type') and self.auth_type is not None:
            _dict['auth_type'] = self.auth_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSettingsServerSideSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSettingsServerSideSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSettingsServerSideSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class AuthTypeEnum(str, Enum):
        """
        The authorization type that is used.
        """

        BASIC = 'basic'
        APIKEY = 'apikey'
        NONE = 'none'


class SearchSkillWarning:
    """
    A warning describing an error in the search skill configuration.

    :param str code: (optional) The error code.
    :param str path: (optional) The location of the error in the search skill
          configuration object.
    :param str message: (optional) The error message.
    """

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        path: Optional[str] = None,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a SearchSkillWarning object.

        :param str code: (optional) The error code.
        :param str path: (optional) The location of the error in the search skill
               configuration object.
        :param str message: (optional) The error message.
        """
        self.code = code
        self.path = path
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSkillWarning':
        """Initialize a SearchSkillWarning object from a json dictionary."""
        args = {}
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SearchSkillWarning object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SearchSkillWarning object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SearchSkillWarning') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SearchSkillWarning') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SessionResponse:
    """
    SessionResponse.

    :param str session_id: The session ID.
    """

    def __init__(
        self,
        session_id: str,
    ) -> None:
        """
        Initialize a SessionResponse object.

        :param str session_id: The session ID.
        """
        self.session_id = session_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionResponse':
        """Initialize a SessionResponse object from a json dictionary."""
        args = {}
        if (session_id := _dict.get('session_id')) is not None:
            args['session_id'] = session_id
        else:
            raise ValueError(
                'Required property \'session_id\' not present in SessionResponse JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SessionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'session_id') and self.session_id is not None:
            _dict['session_id'] = self.session_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SessionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SessionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SessionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Skill:
    """
    Skill.

    :param str name: (optional) The name of the skill. This string cannot contain
          carriage return, newline, or tab characters.
    :param str description: (optional) The description of the skill. This string
          cannot contain carriage return, newline, or tab characters.
    :param dict workspace: (optional) An object containing the conversational
          content of an action or dialog skill.
    :param str skill_id: (optional) The skill ID of the skill.
    :param str status: (optional) The current status of the skill:
           - **Available**: The skill is available and ready to process messages.
           - **Failed**: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - **Non Existent**: The skill does not exist.
           - **Processing**: An asynchronous operation has not yet completed.
           - **Training**: The skill is training based on new data.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :param str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :param dict dialog_settings: (optional) For internal use only.
    :param str assistant_id: (optional) The unique identifier of the assistant the
          skill is associated with.
    :param str workspace_id: (optional) The unique identifier of the workspace that
          contains the skill content. Included only for action and dialog skills.
    :param str environment_id: (optional) The unique identifier of the environment
          where the skill is defined. For action and dialog skills, this is always the
          draft environment.
    :param bool valid: (optional) Whether the skill is structurally valid.
    :param str next_snapshot_version: (optional) The name that will be given to the
          next snapshot that is created for the skill. A snapshot of each versionable
          skill is saved for each new release of an assistant.
    :param SearchSettings search_settings: (optional) An object describing the
          search skill configuration.
          **Note:** Search settings are not supported in **Import skills** requests, and
          are not included in **Export skills** responses.
    :param List[SearchSkillWarning] warnings: (optional) An array of warnings
          describing errors with the search skill configuration. Included only for search
          skills.
    :param str language: The language of the skill.
    :param str type: The type of skill.
    """

    def __init__(
        self,
        language: str,
        type: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        workspace: Optional[dict] = None,
        skill_id: Optional[str] = None,
        status: Optional[str] = None,
        status_errors: Optional[List['StatusError']] = None,
        status_description: Optional[str] = None,
        dialog_settings: Optional[dict] = None,
        assistant_id: Optional[str] = None,
        workspace_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        valid: Optional[bool] = None,
        next_snapshot_version: Optional[str] = None,
        search_settings: Optional['SearchSettings'] = None,
        warnings: Optional[List['SearchSkillWarning']] = None,
    ) -> None:
        """
        Initialize a Skill object.

        :param str language: The language of the skill.
        :param str type: The type of skill.
        :param str name: (optional) The name of the skill. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the skill. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict workspace: (optional) An object containing the conversational
               content of an action or dialog skill.
        :param dict dialog_settings: (optional) For internal use only.
        :param SearchSettings search_settings: (optional) An object describing the
               search skill configuration.
               **Note:** Search settings are not supported in **Import skills** requests,
               and are not included in **Export skills** responses.
        """
        self.name = name
        self.description = description
        self.workspace = workspace
        self.skill_id = skill_id
        self.status = status
        self.status_errors = status_errors
        self.status_description = status_description
        self.dialog_settings = dialog_settings
        self.assistant_id = assistant_id
        self.workspace_id = workspace_id
        self.environment_id = environment_id
        self.valid = valid
        self.next_snapshot_version = next_snapshot_version
        self.search_settings = search_settings
        self.warnings = warnings
        self.language = language
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Skill':
        """Initialize a Skill object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (workspace := _dict.get('workspace')) is not None:
            args['workspace'] = workspace
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        if (status_description := _dict.get('status_description')) is not None:
            args['status_description'] = status_description
        if (dialog_settings := _dict.get('dialog_settings')) is not None:
            args['dialog_settings'] = dialog_settings
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (environment_id := _dict.get('environment_id')) is not None:
            args['environment_id'] = environment_id
        if (valid := _dict.get('valid')) is not None:
            args['valid'] = valid
        if (next_snapshot_version :=
                _dict.get('next_snapshot_version')) is not None:
            args['next_snapshot_version'] = next_snapshot_version
        if (search_settings := _dict.get('search_settings')) is not None:
            args['search_settings'] = SearchSettings.from_dict(search_settings)
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = [
                SearchSkillWarning.from_dict(v) for v in warnings
            ]
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in Skill JSON')
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in Skill JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Skill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'workspace') and self.workspace is not None:
            _dict['workspace'] = self.workspace
        if hasattr(self, 'skill_id') and getattr(self, 'skill_id') is not None:
            _dict['skill_id'] = getattr(self, 'skill_id')
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'status_errors') and getattr(
                self, 'status_errors') is not None:
            status_errors_list = []
            for v in getattr(self, 'status_errors'):
                if isinstance(v, dict):
                    status_errors_list.append(v)
                else:
                    status_errors_list.append(v.to_dict())
            _dict['status_errors'] = status_errors_list
        if hasattr(self, 'status_description') and getattr(
                self, 'status_description') is not None:
            _dict['status_description'] = getattr(self, 'status_description')
        if hasattr(self,
                   'dialog_settings') and self.dialog_settings is not None:
            _dict['dialog_settings'] = self.dialog_settings
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'workspace_id') and getattr(
                self, 'workspace_id') is not None:
            _dict['workspace_id'] = getattr(self, 'workspace_id')
        if hasattr(self, 'environment_id') and getattr(
                self, 'environment_id') is not None:
            _dict['environment_id'] = getattr(self, 'environment_id')
        if hasattr(self, 'valid') and getattr(self, 'valid') is not None:
            _dict['valid'] = getattr(self, 'valid')
        if hasattr(self, 'next_snapshot_version') and getattr(
                self, 'next_snapshot_version') is not None:
            _dict['next_snapshot_version'] = getattr(self,
                                                     'next_snapshot_version')
        if hasattr(self,
                   'search_settings') and self.search_settings is not None:
            if isinstance(self.search_settings, dict):
                _dict['search_settings'] = self.search_settings
            else:
                _dict['search_settings'] = self.search_settings.to_dict()
        if hasattr(self, 'warnings') and getattr(self, 'warnings') is not None:
            warnings_list = []
            for v in getattr(self, 'warnings'):
                if isinstance(v, dict):
                    warnings_list.append(v)
                else:
                    warnings_list.append(v.to_dict())
            _dict['warnings'] = warnings_list
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Skill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Skill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Skill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the skill:
         - **Available**: The skill is available and ready to process messages.
         - **Failed**: An asynchronous operation has failed. See the **status_errors**
        property for more information about the cause of the failure.
         - **Non Existent**: The skill does not exist.
         - **Processing**: An asynchronous operation has not yet completed.
         - **Training**: The skill is training based on new data.
        """

        AVAILABLE = 'Available'
        FAILED = 'Failed'
        NON_EXISTENT = 'Non Existent'
        PROCESSING = 'Processing'
        TRAINING = 'Training'
        UNAVAILABLE = 'Unavailable'

    class TypeEnum(str, Enum):
        """
        The type of skill.
        """

        ACTION = 'action'
        DIALOG = 'dialog'
        SEARCH = 'search'


class SkillImport:
    """
    SkillImport.

    :param str name: (optional) The name of the skill. This string cannot contain
          carriage return, newline, or tab characters.
    :param str description: (optional) The description of the skill. This string
          cannot contain carriage return, newline, or tab characters.
    :param dict workspace: (optional) An object containing the conversational
          content of an action or dialog skill.
    :param str skill_id: (optional) The skill ID of the skill.
    :param str status: (optional) The current status of the skill:
           - **Available**: The skill is available and ready to process messages.
           - **Failed**: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - **Non Existent**: The skill does not exist.
           - **Processing**: An asynchronous operation has not yet completed.
           - **Training**: The skill is training based on new data.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :param str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :param dict dialog_settings: (optional) For internal use only.
    :param str assistant_id: (optional) The unique identifier of the assistant the
          skill is associated with.
    :param str workspace_id: (optional) The unique identifier of the workspace that
          contains the skill content. Included only for action and dialog skills.
    :param str environment_id: (optional) The unique identifier of the environment
          where the skill is defined. For action and dialog skills, this is always the
          draft environment.
    :param bool valid: (optional) Whether the skill is structurally valid.
    :param str next_snapshot_version: (optional) The name that will be given to the
          next snapshot that is created for the skill. A snapshot of each versionable
          skill is saved for each new release of an assistant.
    :param SearchSettings search_settings: (optional) An object describing the
          search skill configuration.
          **Note:** Search settings are not supported in **Import skills** requests, and
          are not included in **Export skills** responses.
    :param List[SearchSkillWarning] warnings: (optional) An array of warnings
          describing errors with the search skill configuration. Included only for search
          skills.
    :param str language: The language of the skill.
    :param str type: The type of skill.
    """

    def __init__(
        self,
        language: str,
        type: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        workspace: Optional[dict] = None,
        skill_id: Optional[str] = None,
        status: Optional[str] = None,
        status_errors: Optional[List['StatusError']] = None,
        status_description: Optional[str] = None,
        dialog_settings: Optional[dict] = None,
        assistant_id: Optional[str] = None,
        workspace_id: Optional[str] = None,
        environment_id: Optional[str] = None,
        valid: Optional[bool] = None,
        next_snapshot_version: Optional[str] = None,
        search_settings: Optional['SearchSettings'] = None,
        warnings: Optional[List['SearchSkillWarning']] = None,
    ) -> None:
        """
        Initialize a SkillImport object.

        :param str language: The language of the skill.
        :param str type: The type of skill.
        :param str name: (optional) The name of the skill. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the skill. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict workspace: (optional) An object containing the conversational
               content of an action or dialog skill.
        :param dict dialog_settings: (optional) For internal use only.
        :param SearchSettings search_settings: (optional) An object describing the
               search skill configuration.
               **Note:** Search settings are not supported in **Import skills** requests,
               and are not included in **Export skills** responses.
        """
        self.name = name
        self.description = description
        self.workspace = workspace
        self.skill_id = skill_id
        self.status = status
        self.status_errors = status_errors
        self.status_description = status_description
        self.dialog_settings = dialog_settings
        self.assistant_id = assistant_id
        self.workspace_id = workspace_id
        self.environment_id = environment_id
        self.valid = valid
        self.next_snapshot_version = next_snapshot_version
        self.search_settings = search_settings
        self.warnings = warnings
        self.language = language
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SkillImport':
        """Initialize a SkillImport object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (workspace := _dict.get('workspace')) is not None:
            args['workspace'] = workspace
        if (skill_id := _dict.get('skill_id')) is not None:
            args['skill_id'] = skill_id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        if (status_description := _dict.get('status_description')) is not None:
            args['status_description'] = status_description
        if (dialog_settings := _dict.get('dialog_settings')) is not None:
            args['dialog_settings'] = dialog_settings
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (environment_id := _dict.get('environment_id')) is not None:
            args['environment_id'] = environment_id
        if (valid := _dict.get('valid')) is not None:
            args['valid'] = valid
        if (next_snapshot_version :=
                _dict.get('next_snapshot_version')) is not None:
            args['next_snapshot_version'] = next_snapshot_version
        if (search_settings := _dict.get('search_settings')) is not None:
            args['search_settings'] = SearchSettings.from_dict(search_settings)
        if (warnings := _dict.get('warnings')) is not None:
            args['warnings'] = [
                SearchSkillWarning.from_dict(v) for v in warnings
            ]
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in SkillImport JSON'
            )
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in SkillImport JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SkillImport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'workspace') and self.workspace is not None:
            _dict['workspace'] = self.workspace
        if hasattr(self, 'skill_id') and getattr(self, 'skill_id') is not None:
            _dict['skill_id'] = getattr(self, 'skill_id')
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'status_errors') and getattr(
                self, 'status_errors') is not None:
            status_errors_list = []
            for v in getattr(self, 'status_errors'):
                if isinstance(v, dict):
                    status_errors_list.append(v)
                else:
                    status_errors_list.append(v.to_dict())
            _dict['status_errors'] = status_errors_list
        if hasattr(self, 'status_description') and getattr(
                self, 'status_description') is not None:
            _dict['status_description'] = getattr(self, 'status_description')
        if hasattr(self,
                   'dialog_settings') and self.dialog_settings is not None:
            _dict['dialog_settings'] = self.dialog_settings
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'workspace_id') and getattr(
                self, 'workspace_id') is not None:
            _dict['workspace_id'] = getattr(self, 'workspace_id')
        if hasattr(self, 'environment_id') and getattr(
                self, 'environment_id') is not None:
            _dict['environment_id'] = getattr(self, 'environment_id')
        if hasattr(self, 'valid') and getattr(self, 'valid') is not None:
            _dict['valid'] = getattr(self, 'valid')
        if hasattr(self, 'next_snapshot_version') and getattr(
                self, 'next_snapshot_version') is not None:
            _dict['next_snapshot_version'] = getattr(self,
                                                     'next_snapshot_version')
        if hasattr(self,
                   'search_settings') and self.search_settings is not None:
            if isinstance(self.search_settings, dict):
                _dict['search_settings'] = self.search_settings
            else:
                _dict['search_settings'] = self.search_settings.to_dict()
        if hasattr(self, 'warnings') and getattr(self, 'warnings') is not None:
            warnings_list = []
            for v in getattr(self, 'warnings'):
                if isinstance(v, dict):
                    warnings_list.append(v)
                else:
                    warnings_list.append(v.to_dict())
            _dict['warnings'] = warnings_list
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SkillImport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SkillImport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SkillImport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the skill:
         - **Available**: The skill is available and ready to process messages.
         - **Failed**: An asynchronous operation has failed. See the **status_errors**
        property for more information about the cause of the failure.
         - **Non Existent**: The skill does not exist.
         - **Processing**: An asynchronous operation has not yet completed.
         - **Training**: The skill is training based on new data.
        """

        AVAILABLE = 'Available'
        FAILED = 'Failed'
        NON_EXISTENT = 'Non Existent'
        PROCESSING = 'Processing'
        TRAINING = 'Training'
        UNAVAILABLE = 'Unavailable'

    class TypeEnum(str, Enum):
        """
        The type of skill.
        """

        ACTION = 'action'
        DIALOG = 'dialog'


class SkillsAsyncRequestStatus:
    """
    SkillsAsyncRequestStatus.

    :param str assistant_id: (optional) The assistant ID of the assistant.
    :param str status: (optional) The current status of the asynchronous operation:
           - `Available`: An asynchronous export is available.
           - `Completed`: An asynchronous import operation has completed successfully.
           - `Failed`: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - `Processing`: An asynchronous operation has not yet completed.
    :param str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    """

    def __init__(
        self,
        *,
        assistant_id: Optional[str] = None,
        status: Optional[str] = None,
        status_description: Optional[str] = None,
        status_errors: Optional[List['StatusError']] = None,
    ) -> None:
        """
        Initialize a SkillsAsyncRequestStatus object.

        """
        self.assistant_id = assistant_id
        self.status = status
        self.status_description = status_description
        self.status_errors = status_errors

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SkillsAsyncRequestStatus':
        """Initialize a SkillsAsyncRequestStatus object from a json dictionary."""
        args = {}
        if (assistant_id := _dict.get('assistant_id')) is not None:
            args['assistant_id'] = assistant_id
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_description := _dict.get('status_description')) is not None:
            args['status_description'] = status_description
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SkillsAsyncRequestStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'assistant_id') and getattr(
                self, 'assistant_id') is not None:
            _dict['assistant_id'] = getattr(self, 'assistant_id')
        if hasattr(self, 'status') and getattr(self, 'status') is not None:
            _dict['status'] = getattr(self, 'status')
        if hasattr(self, 'status_description') and getattr(
                self, 'status_description') is not None:
            _dict['status_description'] = getattr(self, 'status_description')
        if hasattr(self, 'status_errors') and getattr(
                self, 'status_errors') is not None:
            status_errors_list = []
            for v in getattr(self, 'status_errors'):
                if isinstance(v, dict):
                    status_errors_list.append(v)
                else:
                    status_errors_list.append(v.to_dict())
            _dict['status_errors'] = status_errors_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SkillsAsyncRequestStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SkillsAsyncRequestStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SkillsAsyncRequestStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the asynchronous operation:
         - `Available`: An asynchronous export is available.
         - `Completed`: An asynchronous import operation has completed successfully.
         - `Failed`: An asynchronous operation has failed. See the **status_errors**
        property for more information about the cause of the failure.
         - `Processing`: An asynchronous operation has not yet completed.
        """

        AVAILABLE = 'Available'
        COMPLETED = 'Completed'
        FAILED = 'Failed'
        PROCESSING = 'Processing'


class SkillsExport:
    """
    SkillsExport.

    :param List[Skill] assistant_skills: An array of objects describing the skills
          for the assistant. Included in responses only if **status**=`Available`.
    :param AssistantState assistant_state: Status information about the skills for
          the assistant. Included in responses only if **status**=`Available`.
    """

    def __init__(
        self,
        assistant_skills: List['Skill'],
        assistant_state: 'AssistantState',
    ) -> None:
        """
        Initialize a SkillsExport object.

        :param List[Skill] assistant_skills: An array of objects describing the
               skills for the assistant. Included in responses only if
               **status**=`Available`.
        :param AssistantState assistant_state: Status information about the skills
               for the assistant. Included in responses only if **status**=`Available`.
        """
        self.assistant_skills = assistant_skills
        self.assistant_state = assistant_state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SkillsExport':
        """Initialize a SkillsExport object from a json dictionary."""
        args = {}
        if (assistant_skills := _dict.get('assistant_skills')) is not None:
            args['assistant_skills'] = [
                Skill.from_dict(v) for v in assistant_skills
            ]
        else:
            raise ValueError(
                'Required property \'assistant_skills\' not present in SkillsExport JSON'
            )
        if (assistant_state := _dict.get('assistant_state')) is not None:
            args['assistant_state'] = AssistantState.from_dict(assistant_state)
        else:
            raise ValueError(
                'Required property \'assistant_state\' not present in SkillsExport JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SkillsExport object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'assistant_skills') and self.assistant_skills is not None:
            assistant_skills_list = []
            for v in self.assistant_skills:
                if isinstance(v, dict):
                    assistant_skills_list.append(v)
                else:
                    assistant_skills_list.append(v.to_dict())
            _dict['assistant_skills'] = assistant_skills_list
        if hasattr(self,
                   'assistant_state') and self.assistant_state is not None:
            if isinstance(self.assistant_state, dict):
                _dict['assistant_state'] = self.assistant_state
            else:
                _dict['assistant_state'] = self.assistant_state.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this SkillsExport object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SkillsExport') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SkillsExport') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatefulMessageResponse:
    """
    A response from the watsonx Assistant service.

    :param MessageOutput output: Assistant output to be rendered or processed by the
          client.
    :param MessageContext context: (optional) Context data for the conversation. You
          can use this property to access context variables. The context is stored by the
          assistant on a per-session basis.
          **Note:** The context is included in message responses only if
          **return_context**=`true` in the message request. Full context is always
          included in logs.
    :param str user_id: A string value that identifies the user who is interacting
          with the assistant. The client must provide a unique identifier for each
          individual end user who accesses the application. For user-based plans, this
          user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context.
    :param MessageOutput masked_output: (optional) Assistant output to be rendered
          or processed by the client. All private data is masked or removed.
    :param MessageInput masked_input: (optional) An input object that includes the
          input text. All private data is masked or removed.
    """

    def __init__(
        self,
        output: 'MessageOutput',
        user_id: str,
        *,
        context: Optional['MessageContext'] = None,
        masked_output: Optional['MessageOutput'] = None,
        masked_input: Optional['MessageInput'] = None,
    ) -> None:
        """
        Initialize a StatefulMessageResponse object.

        :param MessageOutput output: Assistant output to be rendered or processed
               by the client.
        :param str user_id: A string value that identifies the user who is
               interacting with the assistant. The client must provide a unique identifier
               for each individual end user who accesses the application. For user-based
               plans, this user ID is used to identify unique users for billing purposes.
               This string cannot contain carriage return, newline, or tab characters. If
               no value is specified in the input, **user_id** is automatically set to the
               value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context.
        :param MessageContext context: (optional) Context data for the
               conversation. You can use this property to access context variables. The
               context is stored by the assistant on a per-session basis.
               **Note:** The context is included in message responses only if
               **return_context**=`true` in the message request. Full context is always
               included in logs.
        :param MessageOutput masked_output: (optional) Assistant output to be
               rendered or processed by the client. All private data is masked or removed.
        :param MessageInput masked_input: (optional) An input object that includes
               the input text. All private data is masked or removed.
        """
        self.output = output
        self.context = context
        self.user_id = user_id
        self.masked_output = masked_output
        self.masked_input = masked_input

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatefulMessageResponse':
        """Initialize a StatefulMessageResponse object from a json dictionary."""
        args = {}
        if (output := _dict.get('output')) is not None:
            args['output'] = MessageOutput.from_dict(output)
        else:
            raise ValueError(
                'Required property \'output\' not present in StatefulMessageResponse JSON'
            )
        if (context := _dict.get('context')) is not None:
            args['context'] = MessageContext.from_dict(context)
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        else:
            raise ValueError(
                'Required property \'user_id\' not present in StatefulMessageResponse JSON'
            )
        if (masked_output := _dict.get('masked_output')) is not None:
            args['masked_output'] = MessageOutput.from_dict(masked_output)
        if (masked_input := _dict.get('masked_input')) is not None:
            args['masked_input'] = MessageInput.from_dict(masked_input)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatefulMessageResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'output') and self.output is not None:
            if isinstance(self.output, dict):
                _dict['output'] = self.output
            else:
                _dict['output'] = self.output.to_dict()
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        if hasattr(self, 'masked_output') and self.masked_output is not None:
            if isinstance(self.masked_output, dict):
                _dict['masked_output'] = self.masked_output
            else:
                _dict['masked_output'] = self.masked_output.to_dict()
        if hasattr(self, 'masked_input') and self.masked_input is not None:
            if isinstance(self.masked_input, dict):
                _dict['masked_input'] = self.masked_input
            else:
                _dict['masked_input'] = self.masked_input.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatefulMessageResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatefulMessageResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatefulMessageResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageContext:
    """
    StatelessMessageContext.

    :param StatelessMessageContextGlobal global_: (optional) Session context data
          that is shared by all skills used by the assistant.
    :param StatelessMessageContextSkills skills: (optional) Context data specific to
          particular skills used by the assistant.
    :param dict integrations: (optional) An object containing context data that is
          specific to particular integrations. For more information, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
    """

    def __init__(
        self,
        *,
        global_: Optional['StatelessMessageContextGlobal'] = None,
        skills: Optional['StatelessMessageContextSkills'] = None,
        integrations: Optional[dict] = None,
    ) -> None:
        """
        Initialize a StatelessMessageContext object.

        :param StatelessMessageContextGlobal global_: (optional) Session context
               data that is shared by all skills used by the assistant.
        :param StatelessMessageContextSkills skills: (optional) Context data
               specific to particular skills used by the assistant.
        :param dict integrations: (optional) An object containing context data that
               is specific to particular integrations. For more information, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
        """
        self.global_ = global_
        self.skills = skills
        self.integrations = integrations

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageContext':
        """Initialize a StatelessMessageContext object from a json dictionary."""
        args = {}
        if (global_ := _dict.get('global')) is not None:
            args['global_'] = StatelessMessageContextGlobal.from_dict(global_)
        if (skills := _dict.get('skills')) is not None:
            args['skills'] = StatelessMessageContextSkills.from_dict(skills)
        if (integrations := _dict.get('integrations')) is not None:
            args['integrations'] = integrations
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'global_') and self.global_ is not None:
            if isinstance(self.global_, dict):
                _dict['global'] = self.global_
            else:
                _dict['global'] = self.global_.to_dict()
        if hasattr(self, 'skills') and self.skills is not None:
            if isinstance(self.skills, dict):
                _dict['skills'] = self.skills
            else:
                _dict['skills'] = self.skills.to_dict()
        if hasattr(self, 'integrations') and self.integrations is not None:
            _dict['integrations'] = self.integrations
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageContextGlobal:
    """
    Session context data that is shared by all skills used by the assistant.

    :param MessageContextGlobalSystem system: (optional) Built-in system properties
          that apply to all skills used by the assistant.
    :param str session_id: (optional) The unique identifier of the session.
    """

    def __init__(
        self,
        *,
        system: Optional['MessageContextGlobalSystem'] = None,
        session_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a StatelessMessageContextGlobal object.

        :param MessageContextGlobalSystem system: (optional) Built-in system
               properties that apply to all skills used by the assistant.
        :param str session_id: (optional) The unique identifier of the session.
        """
        self.system = system
        self.session_id = session_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageContextGlobal':
        """Initialize a StatelessMessageContextGlobal object from a json dictionary."""
        args = {}
        if (system := _dict.get('system')) is not None:
            args['system'] = MessageContextGlobalSystem.from_dict(system)
        if (session_id := _dict.get('session_id')) is not None:
            args['session_id'] = session_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageContextGlobal object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'system') and self.system is not None:
            if isinstance(self.system, dict):
                _dict['system'] = self.system
            else:
                _dict['system'] = self.system.to_dict()
        if hasattr(self, 'session_id') and self.session_id is not None:
            _dict['session_id'] = self.session_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageContextGlobal object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageContextGlobal') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageContextGlobal') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageContextSkills:
    """
    Context data specific to particular skills used by the assistant.

    :param MessageContextDialogSkill main_skill: (optional) Context variables that
          are used by the dialog skill.
    :param StatelessMessageContextSkillsActionsSkill actions_skill: (optional)
          Context variables that are used by the action skill.
    """

    def __init__(
        self,
        *,
        main_skill: Optional['MessageContextDialogSkill'] = None,
        actions_skill: Optional[
            'StatelessMessageContextSkillsActionsSkill'] = None,
    ) -> None:
        """
        Initialize a StatelessMessageContextSkills object.

        :param MessageContextDialogSkill main_skill: (optional) Context variables
               that are used by the dialog skill.
        :param StatelessMessageContextSkillsActionsSkill actions_skill: (optional)
               Context variables that are used by the action skill.
        """
        self.main_skill = main_skill
        self.actions_skill = actions_skill

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageContextSkills':
        """Initialize a StatelessMessageContextSkills object from a json dictionary."""
        args = {}
        if (main_skill := _dict.get('main skill')) is not None:
            args['main_skill'] = MessageContextDialogSkill.from_dict(main_skill)
        if (actions_skill := _dict.get('actions skill')) is not None:
            args[
                'actions_skill'] = StatelessMessageContextSkillsActionsSkill.from_dict(
                    actions_skill)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageContextSkills object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'main_skill') and self.main_skill is not None:
            if isinstance(self.main_skill, dict):
                _dict['main skill'] = self.main_skill
            else:
                _dict['main skill'] = self.main_skill.to_dict()
        if hasattr(self, 'actions_skill') and self.actions_skill is not None:
            if isinstance(self.actions_skill, dict):
                _dict['actions skill'] = self.actions_skill
            else:
                _dict['actions skill'] = self.actions_skill.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageContextSkills object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageContextSkills') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageContextSkills') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageContextSkillsActionsSkill:
    """
    Context variables that are used by the action skill.

    :param dict user_defined: (optional) An object containing any arbitrary
          variables that can be read and written by a particular skill.
    :param MessageContextSkillSystem system: (optional) System context data used by
          the skill.
    :param dict action_variables: (optional) An object containing action variables.
          Action variables can be accessed only by steps in the same action, and do not
          persist after the action ends.
    :param dict skill_variables: (optional) An object containing skill variables.
          (In the watsonx Assistant user interface, skill variables are called _session
          variables_.) Skill variables can be accessed by any action and persist for the
          duration of the session.
    :param dict private_action_variables: (optional) An object containing private
          action variables. Action variables can be accessed only by steps in the same
          action, and do not persist after the action ends. Private variables are
          encrypted.
    :param dict private_skill_variables: (optional) An object containing private
          skill variables. (In the watsonx Assistant user interface, skill variables are
          called _session variables_.) Skill variables can be accessed by any action and
          persist for the duration of the session. Private variables are encrypted.
    """

    def __init__(
        self,
        *,
        user_defined: Optional[dict] = None,
        system: Optional['MessageContextSkillSystem'] = None,
        action_variables: Optional[dict] = None,
        skill_variables: Optional[dict] = None,
        private_action_variables: Optional[dict] = None,
        private_skill_variables: Optional[dict] = None,
    ) -> None:
        """
        Initialize a StatelessMessageContextSkillsActionsSkill object.

        :param dict user_defined: (optional) An object containing any arbitrary
               variables that can be read and written by a particular skill.
        :param MessageContextSkillSystem system: (optional) System context data
               used by the skill.
        :param dict action_variables: (optional) An object containing action
               variables. Action variables can be accessed only by steps in the same
               action, and do not persist after the action ends.
        :param dict skill_variables: (optional) An object containing skill
               variables. (In the watsonx Assistant user interface, skill variables are
               called _session variables_.) Skill variables can be accessed by any action
               and persist for the duration of the session.
        :param dict private_action_variables: (optional) An object containing
               private action variables. Action variables can be accessed only by steps in
               the same action, and do not persist after the action ends. Private
               variables are encrypted.
        :param dict private_skill_variables: (optional) An object containing
               private skill variables. (In the watsonx Assistant user interface, skill
               variables are called _session variables_.) Skill variables can be accessed
               by any action and persist for the duration of the session. Private
               variables are encrypted.
        """
        self.user_defined = user_defined
        self.system = system
        self.action_variables = action_variables
        self.skill_variables = skill_variables
        self.private_action_variables = private_action_variables
        self.private_skill_variables = private_skill_variables

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'StatelessMessageContextSkillsActionsSkill':
        """Initialize a StatelessMessageContextSkillsActionsSkill object from a json dictionary."""
        args = {}
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        if (system := _dict.get('system')) is not None:
            args['system'] = MessageContextSkillSystem.from_dict(system)
        if (action_variables := _dict.get('action_variables')) is not None:
            args['action_variables'] = action_variables
        if (skill_variables := _dict.get('skill_variables')) is not None:
            args['skill_variables'] = skill_variables
        if (private_action_variables :=
                _dict.get('private_action_variables')) is not None:
            args['private_action_variables'] = private_action_variables
        if (private_skill_variables :=
                _dict.get('private_skill_variables')) is not None:
            args['private_skill_variables'] = private_skill_variables
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageContextSkillsActionsSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'system') and self.system is not None:
            if isinstance(self.system, dict):
                _dict['system'] = self.system
            else:
                _dict['system'] = self.system.to_dict()
        if hasattr(self,
                   'action_variables') and self.action_variables is not None:
            _dict['action_variables'] = self.action_variables
        if hasattr(self,
                   'skill_variables') and self.skill_variables is not None:
            _dict['skill_variables'] = self.skill_variables
        if hasattr(self, 'private_action_variables'
                  ) and self.private_action_variables is not None:
            _dict['private_action_variables'] = self.private_action_variables
        if hasattr(self, 'private_skill_variables'
                  ) and self.private_skill_variables is not None:
            _dict['private_skill_variables'] = self.private_skill_variables
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageContextSkillsActionsSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'StatelessMessageContextSkillsActionsSkill') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'StatelessMessageContextSkillsActionsSkill') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageInput:
    """
    An input object that includes the input text.

    :param str message_type: (optional) The type of the message:
          - `text`: The user input is processed normally by the assistant.
          - `search`: Only search results are returned. (Any dialog or action skill is
          bypassed.)
          **Note:** A `search` message results in an error if no search skill is
          configured for the assistant.
    :param str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :param List[RuntimeIntent] intents: (optional) Intents to use when evaluating
          the user input. Include intents from the previous response to continue using
          those intents rather than trying to recognize intents in the new input.
    :param List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :param str suggestion_id: (optional) For internal use only.
    :param List[MessageInputAttachment] attachments: (optional) An array of
          multimedia attachments to be sent with the message. Attachments are not
          processed by the assistant itself, but can be sent to external services by
          webhooks.
           **Note:** Attachments are not supported on IBM Cloud Pak for Data.
    :param RequestAnalytics analytics: (optional) An optional object containing
          analytics data. Currently, this data is used only for events sent to the Segment
          extension.
    :param StatelessMessageInputOptions options: (optional) Optional properties that
          control how the assistant responds.
    """

    def __init__(
        self,
        *,
        message_type: Optional[str] = None,
        text: Optional[str] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        suggestion_id: Optional[str] = None,
        attachments: Optional[List['MessageInputAttachment']] = None,
        analytics: Optional['RequestAnalytics'] = None,
        options: Optional['StatelessMessageInputOptions'] = None,
    ) -> None:
        """
        Initialize a StatelessMessageInput object.

        :param str message_type: (optional) The type of the message:
               - `text`: The user input is processed normally by the assistant.
               - `search`: Only search results are returned. (Any dialog or action skill
               is bypassed.)
               **Note:** A `search` message results in an error if no search skill is
               configured for the assistant.
        :param str text: (optional) The text of the user input. This string cannot
               contain carriage return, newline, or tab characters.
        :param List[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param List[RuntimeEntity] entities: (optional) Entities to use when
               evaluating the message. Include entities from the previous response to
               continue using those entities rather than detecting entities in the new
               input.
        :param str suggestion_id: (optional) For internal use only.
        :param List[MessageInputAttachment] attachments: (optional) An array of
               multimedia attachments to be sent with the message. Attachments are not
               processed by the assistant itself, but can be sent to external services by
               webhooks.
                **Note:** Attachments are not supported on IBM Cloud Pak for Data.
        :param RequestAnalytics analytics: (optional) An optional object containing
               analytics data. Currently, this data is used only for events sent to the
               Segment extension.
        :param StatelessMessageInputOptions options: (optional) Optional properties
               that control how the assistant responds.
        """
        self.message_type = message_type
        self.text = text
        self.intents = intents
        self.entities = entities
        self.suggestion_id = suggestion_id
        self.attachments = attachments
        self.analytics = analytics
        self.options = options

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageInput':
        """Initialize a StatelessMessageInput object from a json dictionary."""
        args = {}
        if (message_type := _dict.get('message_type')) is not None:
            args['message_type'] = message_type
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (suggestion_id := _dict.get('suggestion_id')) is not None:
            args['suggestion_id'] = suggestion_id
        if (attachments := _dict.get('attachments')) is not None:
            args['attachments'] = [
                MessageInputAttachment.from_dict(v) for v in attachments
            ]
        if (analytics := _dict.get('analytics')) is not None:
            args['analytics'] = RequestAnalytics.from_dict(analytics)
        if (options := _dict.get('options')) is not None:
            args['options'] = StatelessMessageInputOptions.from_dict(options)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message_type') and self.message_type is not None:
            _dict['message_type'] = self.message_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
        if hasattr(self, 'entities') and self.entities is not None:
            entities_list = []
            for v in self.entities:
                if isinstance(v, dict):
                    entities_list.append(v)
                else:
                    entities_list.append(v.to_dict())
            _dict['entities'] = entities_list
        if hasattr(self, 'suggestion_id') and self.suggestion_id is not None:
            _dict['suggestion_id'] = self.suggestion_id
        if hasattr(self, 'attachments') and self.attachments is not None:
            attachments_list = []
            for v in self.attachments:
                if isinstance(v, dict):
                    attachments_list.append(v)
                else:
                    attachments_list.append(v.to_dict())
            _dict['attachments'] = attachments_list
        if hasattr(self, 'analytics') and self.analytics is not None:
            if isinstance(self.analytics, dict):
                _dict['analytics'] = self.analytics
            else:
                _dict['analytics'] = self.analytics.to_dict()
        if hasattr(self, 'options') and self.options is not None:
            if isinstance(self.options, dict):
                _dict['options'] = self.options
            else:
                _dict['options'] = self.options.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageInput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageInput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageInput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MessageTypeEnum(str, Enum):
        """
        The type of the message:
        - `text`: The user input is processed normally by the assistant.
        - `search`: Only search results are returned. (Any dialog or action skill is
        bypassed.)
        **Note:** A `search` message results in an error if no search skill is configured
        for the assistant.
        """

        TEXT = 'text'
        SEARCH = 'search'


class StatelessMessageInputOptions:
    """
    Optional properties that control how the assistant responds.

    :param bool restart: (optional) Whether to restart dialog processing at the root
          of the dialog, regardless of any previously visited nodes. **Note:** This does
          not affect `turn_count` or any other context variables.
    :param bool alternate_intents: (optional) Whether to return more than one
          intent. Set to `true` to return all matching intents.
    :param bool async_callout: (optional) Whether custom extension callouts are
          executed asynchronously. Asynchronous execution means the response to the
          extension callout will be processed on the subsequent message call, the initial
          message response signals to the client that the operation may be long running.
          With synchronous execution the custom extension is executed and returns the
          response in a single message turn. **Note:** **async_callout** defaults to true
          for API versions earlier than 2023-06-15.
    :param MessageInputOptionsSpelling spelling: (optional) Spelling correction
          options for the message. Any options specified on an individual message override
          the settings configured for the skill.
    :param bool debug: (optional) Whether to return additional diagnostic
          information. Set to `true` to return additional information in the
          `output.debug` property.
    """

    def __init__(
        self,
        *,
        restart: Optional[bool] = None,
        alternate_intents: Optional[bool] = None,
        async_callout: Optional[bool] = None,
        spelling: Optional['MessageInputOptionsSpelling'] = None,
        debug: Optional[bool] = None,
    ) -> None:
        """
        Initialize a StatelessMessageInputOptions object.

        :param bool restart: (optional) Whether to restart dialog processing at the
               root of the dialog, regardless of any previously visited nodes. **Note:**
               This does not affect `turn_count` or any other context variables.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. Set to `true` to return all matching intents.
        :param bool async_callout: (optional) Whether custom extension callouts are
               executed asynchronously. Asynchronous execution means the response to the
               extension callout will be processed on the subsequent message call, the
               initial message response signals to the client that the operation may be
               long running. With synchronous execution the custom extension is executed
               and returns the response in a single message turn. **Note:**
               **async_callout** defaults to true for API versions earlier than
               2023-06-15.
        :param MessageInputOptionsSpelling spelling: (optional) Spelling correction
               options for the message. Any options specified on an individual message
               override the settings configured for the skill.
        :param bool debug: (optional) Whether to return additional diagnostic
               information. Set to `true` to return additional information in the
               `output.debug` property.
        """
        self.restart = restart
        self.alternate_intents = alternate_intents
        self.async_callout = async_callout
        self.spelling = spelling
        self.debug = debug

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageInputOptions':
        """Initialize a StatelessMessageInputOptions object from a json dictionary."""
        args = {}
        if (restart := _dict.get('restart')) is not None:
            args['restart'] = restart
        if (alternate_intents := _dict.get('alternate_intents')) is not None:
            args['alternate_intents'] = alternate_intents
        if (async_callout := _dict.get('async_callout')) is not None:
            args['async_callout'] = async_callout
        if (spelling := _dict.get('spelling')) is not None:
            args['spelling'] = MessageInputOptionsSpelling.from_dict(spelling)
        if (debug := _dict.get('debug')) is not None:
            args['debug'] = debug
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageInputOptions object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'restart') and self.restart is not None:
            _dict['restart'] = self.restart
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'async_callout') and self.async_callout is not None:
            _dict['async_callout'] = self.async_callout
        if hasattr(self, 'spelling') and self.spelling is not None:
            if isinstance(self.spelling, dict):
                _dict['spelling'] = self.spelling
            else:
                _dict['spelling'] = self.spelling.to_dict()
        if hasattr(self, 'debug') and self.debug is not None:
            _dict['debug'] = self.debug
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageInputOptions object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageInputOptions') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageInputOptions') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatelessMessageResponse:
    """
    A stateless response from the watsonx Assistant service.

    :param MessageOutput output: Assistant output to be rendered or processed by the
          client.
    :param StatelessMessageContext context: Context data for the conversation. You
          can use this property to access context variables. The context is not stored by
          the assistant; to maintain session state, include the context from the response
          in the next message.
    :param MessageOutput masked_output: (optional) Assistant output to be rendered
          or processed by the client. All private data is masked or removed.
    :param MessageInput masked_input: (optional) An input object that includes the
          input text. All private data is masked or removed.
    :param str user_id: (optional) A string value that identifies the user who is
          interacting with the assistant. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context.
    """

    def __init__(
        self,
        output: 'MessageOutput',
        context: 'StatelessMessageContext',
        *,
        masked_output: Optional['MessageOutput'] = None,
        masked_input: Optional['MessageInput'] = None,
        user_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a StatelessMessageResponse object.

        :param MessageOutput output: Assistant output to be rendered or processed
               by the client.
        :param StatelessMessageContext context: Context data for the conversation.
               You can use this property to access context variables. The context is not
               stored by the assistant; to maintain session state, include the context
               from the response in the next message.
        :param MessageOutput masked_output: (optional) Assistant output to be
               rendered or processed by the client. All private data is masked or removed.
        :param MessageInput masked_input: (optional) An input object that includes
               the input text. All private data is masked or removed.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the assistant. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.global.session_id**.
               **Note:** This property is the same as the **user_id** property in the
               global system context.
        """
        self.output = output
        self.context = context
        self.masked_output = masked_output
        self.masked_input = masked_input
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatelessMessageResponse':
        """Initialize a StatelessMessageResponse object from a json dictionary."""
        args = {}
        if (output := _dict.get('output')) is not None:
            args['output'] = MessageOutput.from_dict(output)
        else:
            raise ValueError(
                'Required property \'output\' not present in StatelessMessageResponse JSON'
            )
        if (context := _dict.get('context')) is not None:
            args['context'] = StatelessMessageContext.from_dict(context)
        else:
            raise ValueError(
                'Required property \'context\' not present in StatelessMessageResponse JSON'
            )
        if (masked_output := _dict.get('masked_output')) is not None:
            args['masked_output'] = MessageOutput.from_dict(masked_output)
        if (masked_input := _dict.get('masked_input')) is not None:
            args['masked_input'] = MessageInput.from_dict(masked_input)
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatelessMessageResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'output') and self.output is not None:
            if isinstance(self.output, dict):
                _dict['output'] = self.output
            else:
                _dict['output'] = self.output.to_dict()
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'masked_output') and self.masked_output is not None:
            if isinstance(self.masked_output, dict):
                _dict['masked_output'] = self.masked_output
            else:
                _dict['masked_output'] = self.masked_output.to_dict()
        if hasattr(self, 'masked_input') and self.masked_input is not None:
            if isinstance(self.masked_input, dict):
                _dict['masked_input'] = self.masked_input
            else:
                _dict['masked_input'] = self.masked_input.to_dict()
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatelessMessageResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatelessMessageResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatelessMessageResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class StatusError:
    """
    An object describing an error that occurred during processing of an asynchronous
    operation.

    :param str message: (optional) The text of the error message.
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a StatusError object.

        :param str message: (optional) The text of the error message.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatusError':
        """Initialize a StatusError object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a StatusError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this StatusError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'StatusError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'StatusError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TurnEventActionSource:
    """
    TurnEventActionSource.

    :param str type: (optional) The type of turn event.
    :param str action: (optional) An action that was visited during processing of
          the message.
    :param str action_title: (optional) The title of the action.
    :param str condition: (optional) The condition that triggered the dialog node.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        action: Optional[str] = None,
        action_title: Optional[str] = None,
        condition: Optional[str] = None,
    ) -> None:
        """
        Initialize a TurnEventActionSource object.

        :param str type: (optional) The type of turn event.
        :param str action: (optional) An action that was visited during processing
               of the message.
        :param str action_title: (optional) The title of the action.
        :param str condition: (optional) The condition that triggered the dialog
               node.
        """
        self.type = type
        self.action = action
        self.action_title = action_title
        self.condition = condition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventActionSource':
        """Initialize a TurnEventActionSource object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (action := _dict.get('action')) is not None:
            args['action'] = action
        if (action_title := _dict.get('action_title')) is not None:
            args['action_title'] = action_title
        if (condition := _dict.get('condition')) is not None:
            args['condition'] = condition
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventActionSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'action_title') and self.action_title is not None:
            _dict['action_title'] = self.action_title
        if hasattr(self, 'condition') and self.condition is not None:
            _dict['condition'] = self.condition
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventActionSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventActionSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventActionSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of turn event.
        """

        ACTION = 'action'


class TurnEventCalloutCallout:
    """
    TurnEventCalloutCallout.

    :param str type: (optional) The type of callout. Currently, the only supported
          value is `integration_interaction` (for calls to extensions).
    :param dict internal: (optional) For internal use only.
    :param str result_variable: (optional) The name of the variable where the
          callout result is stored.
    :param TurnEventCalloutCalloutRequest request: (optional) The request object
          executed to the external server specified by the extension.
    :param TurnEventCalloutCalloutResponse response: (optional) The response object
          received by the external server made by the extension.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        internal: Optional[dict] = None,
        result_variable: Optional[str] = None,
        request: Optional['TurnEventCalloutCalloutRequest'] = None,
        response: Optional['TurnEventCalloutCalloutResponse'] = None,
    ) -> None:
        """
        Initialize a TurnEventCalloutCallout object.

        :param str type: (optional) The type of callout. Currently, the only
               supported value is `integration_interaction` (for calls to extensions).
        :param dict internal: (optional) For internal use only.
        :param str result_variable: (optional) The name of the variable where the
               callout result is stored.
        :param TurnEventCalloutCalloutRequest request: (optional) The request
               object executed to the external server specified by the extension.
        :param TurnEventCalloutCalloutResponse response: (optional) The response
               object received by the external server made by the extension.
        """
        self.type = type
        self.internal = internal
        self.result_variable = result_variable
        self.request = request
        self.response = response

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventCalloutCallout':
        """Initialize a TurnEventCalloutCallout object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (internal := _dict.get('internal')) is not None:
            args['internal'] = internal
        if (result_variable := _dict.get('result_variable')) is not None:
            args['result_variable'] = result_variable
        if (request := _dict.get('request')) is not None:
            args['request'] = TurnEventCalloutCalloutRequest.from_dict(request)
        if (response := _dict.get('response')) is not None:
            args['response'] = TurnEventCalloutCalloutResponse.from_dict(
                response)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventCalloutCallout object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'internal') and self.internal is not None:
            _dict['internal'] = self.internal
        if hasattr(self,
                   'result_variable') and self.result_variable is not None:
            _dict['result_variable'] = self.result_variable
        if hasattr(self, 'request') and self.request is not None:
            if isinstance(self.request, dict):
                _dict['request'] = self.request
            else:
                _dict['request'] = self.request.to_dict()
        if hasattr(self, 'response') and self.response is not None:
            if isinstance(self.response, dict):
                _dict['response'] = self.response
            else:
                _dict['response'] = self.response.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventCalloutCallout object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventCalloutCallout') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventCalloutCallout') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of callout. Currently, the only supported value is
        `integration_interaction` (for calls to extensions).
        """

        INTEGRATION_INTERACTION = 'integration_interaction'


class TurnEventCalloutCalloutRequest:
    """
    TurnEventCalloutCalloutRequest.

    :param str method: (optional) The REST method of the request.
    :param str url: (optional) The host URL of the request call.
    :param str path: (optional) The URL path of the request call.
    :param str query_parameters: (optional) Any query parameters appended to the URL
          of the request call.
    :param dict headers_: (optional) Any headers included in the request call.
    :param dict body: (optional) Contains the response of the external server or an
          object. In cases like timeouts or connections errors, it will contain details of
          why the callout to the external server failed.
    """

    def __init__(
        self,
        *,
        method: Optional[str] = None,
        url: Optional[str] = None,
        path: Optional[str] = None,
        query_parameters: Optional[str] = None,
        headers_: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> None:
        """
        Initialize a TurnEventCalloutCalloutRequest object.

        :param str method: (optional) The REST method of the request.
        :param str url: (optional) The host URL of the request call.
        :param str path: (optional) The URL path of the request call.
        :param str query_parameters: (optional) Any query parameters appended to
               the URL of the request call.
        :param dict headers_: (optional) Any headers included in the request call.
        :param dict body: (optional) Contains the response of the external server
               or an object. In cases like timeouts or connections errors, it will contain
               details of why the callout to the external server failed.
        """
        self.method = method
        self.url = url
        self.path = path
        self.query_parameters = query_parameters
        self.headers_ = headers_
        self.body = body

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventCalloutCalloutRequest':
        """Initialize a TurnEventCalloutCalloutRequest object from a json dictionary."""
        args = {}
        if (method := _dict.get('method')) is not None:
            args['method'] = method
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        if (path := _dict.get('path')) is not None:
            args['path'] = path
        if (query_parameters := _dict.get('query_parameters')) is not None:
            args['query_parameters'] = query_parameters
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = headers_
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventCalloutCalloutRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'method') and self.method is not None:
            _dict['method'] = self.method
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'path') and self.path is not None:
            _dict['path'] = self.path
        if hasattr(self,
                   'query_parameters') and self.query_parameters is not None:
            _dict['query_parameters'] = self.query_parameters
        if hasattr(self, 'headers_') and self.headers_ is not None:
            _dict['headers'] = self.headers_
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventCalloutCalloutRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventCalloutCalloutRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventCalloutCalloutRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class MethodEnum(str, Enum):
        """
        The REST method of the request.
        """

        GET = 'get'
        POST = 'post'
        PUT = 'put'
        DELETE = 'delete'
        PATCH = 'patch'


class TurnEventCalloutCalloutResponse:
    """
    TurnEventCalloutCalloutResponse.

    :param str body: (optional) The final response string. This response is a
          composition of every partial chunk received from the stream.
    :param int status_code: (optional) The final status code of the response.
    :param dict last_event: (optional) The response from the last chunk received
          from the response stream.
    """

    def __init__(
        self,
        *,
        body: Optional[str] = None,
        status_code: Optional[int] = None,
        last_event: Optional[dict] = None,
    ) -> None:
        """
        Initialize a TurnEventCalloutCalloutResponse object.

        :param str body: (optional) The final response string. This response is a
               composition of every partial chunk received from the stream.
        :param int status_code: (optional) The final status code of the response.
        :param dict last_event: (optional) The response from the last chunk
               received from the response stream.
        """
        self.body = body
        self.status_code = status_code
        self.last_event = last_event

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventCalloutCalloutResponse':
        """Initialize a TurnEventCalloutCalloutResponse object from a json dictionary."""
        args = {}
        if (body := _dict.get('body')) is not None:
            args['body'] = body
        if (status_code := _dict.get('status_code')) is not None:
            args['status_code'] = status_code
        if (last_event := _dict.get('last_event')) is not None:
            args['last_event'] = last_event
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventCalloutCalloutResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'body') and self.body is not None:
            _dict['body'] = self.body
        if hasattr(self, 'status_code') and self.status_code is not None:
            _dict['status_code'] = self.status_code
        if hasattr(self, 'last_event') and self.last_event is not None:
            _dict['last_event'] = self.last_event
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventCalloutCalloutResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventCalloutCalloutResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventCalloutCalloutResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TurnEventCalloutError:
    """
    TurnEventCalloutError.

    :param str message: (optional) Any error message returned by a failed call to an
          external service.
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a TurnEventCalloutError object.

        :param str message: (optional) Any error message returned by a failed call
               to an external service.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventCalloutError':
        """Initialize a TurnEventCalloutError object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventCalloutError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventCalloutError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventCalloutError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventCalloutError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class TurnEventNodeSource:
    """
    TurnEventNodeSource.

    :param str type: (optional) The type of turn event.
    :param str dialog_node: (optional) A dialog node that was visited during
          processing of the input message.
    :param str title: (optional) The title of the dialog node.
    :param str condition: (optional) The condition that triggered the dialog node.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        dialog_node: Optional[str] = None,
        title: Optional[str] = None,
        condition: Optional[str] = None,
    ) -> None:
        """
        Initialize a TurnEventNodeSource object.

        :param str type: (optional) The type of turn event.
        :param str dialog_node: (optional) A dialog node that was visited during
               processing of the input message.
        :param str title: (optional) The title of the dialog node.
        :param str condition: (optional) The condition that triggered the dialog
               node.
        """
        self.type = type
        self.dialog_node = dialog_node
        self.title = title
        self.condition = condition

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventNodeSource':
        """Initialize a TurnEventNodeSource object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (condition := _dict.get('condition')) is not None:
            args['condition'] = condition
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventNodeSource object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'condition') and self.condition is not None:
            _dict['condition'] = self.condition
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventNodeSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventNodeSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventNodeSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        The type of turn event.
        """

        DIALOG_NODE = 'dialog_node'


class TurnEventSearchError:
    """
    TurnEventSearchError.

    :param str message: (optional) Any error message returned by a failed call to a
          search skill.
    """

    def __init__(
        self,
        *,
        message: Optional[str] = None,
    ) -> None:
        """
        Initialize a TurnEventSearchError object.

        :param str message: (optional) Any error message returned by a failed call
               to a search skill.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventSearchError':
        """Initialize a TurnEventSearchError object from a json dictionary."""
        args = {}
        if (message := _dict.get('message')) is not None:
            args['message'] = message
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a TurnEventSearchError object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this TurnEventSearchError object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'TurnEventSearchError') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'TurnEventSearchError') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdateEnvironmentOrchestration:
    """
    The search skill orchestration settings for the environment.

    :param bool search_skill_fallback: (optional) Whether to fall back to a search
          skill when responding to messages that do not match any intent or action defined
          in dialog or action skills. (If no search skill is configured for the
          environment, this property is ignored.).
    """

    def __init__(
        self,
        *,
        search_skill_fallback: Optional[bool] = None,
    ) -> None:
        """
        Initialize a UpdateEnvironmentOrchestration object.

        :param bool search_skill_fallback: (optional) Whether to fall back to a
               search skill when responding to messages that do not match any intent or
               action defined in dialog or action skills. (If no search skill is
               configured for the environment, this property is ignored.).
        """
        self.search_skill_fallback = search_skill_fallback

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateEnvironmentOrchestration':
        """Initialize a UpdateEnvironmentOrchestration object from a json dictionary."""
        args = {}
        if (search_skill_fallback :=
                _dict.get('search_skill_fallback')) is not None:
            args['search_skill_fallback'] = search_skill_fallback
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateEnvironmentOrchestration object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'search_skill_fallback'
                  ) and self.search_skill_fallback is not None:
            _dict['search_skill_fallback'] = self.search_skill_fallback
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateEnvironmentOrchestration object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateEnvironmentOrchestration') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateEnvironmentOrchestration') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class UpdateEnvironmentReleaseReference:
    """
    An object describing the release that is currently deployed in the environment.

    :param str release: (optional) The name of the deployed release.
    """

    def __init__(
        self,
        *,
        release: Optional[str] = None,
    ) -> None:
        """
        Initialize a UpdateEnvironmentReleaseReference object.

        :param str release: (optional) The name of the deployed release.
        """
        self.release = release

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'UpdateEnvironmentReleaseReference':
        """Initialize a UpdateEnvironmentReleaseReference object from a json dictionary."""
        args = {}
        if (release := _dict.get('release')) is not None:
            args['release'] = release
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a UpdateEnvironmentReleaseReference object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'release') and self.release is not None:
            _dict['release'] = self.release
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this UpdateEnvironmentReleaseReference object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'UpdateEnvironmentReleaseReference') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'UpdateEnvironmentReleaseReference') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CompleteItem(RuntimeResponseGeneric):
    """
    CompleteItem.

    :param Metadata streaming_metadata:
    """

    def __init__(
        self,
        streaming_metadata: 'Metadata',
    ) -> None:
        """
        Initialize a CompleteItem object.

        :param Metadata streaming_metadata:
        """
        # pylint: disable=super-init-not-called
        self.streaming_metadata = streaming_metadata

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CompleteItem':
        """Initialize a CompleteItem object from a json dictionary."""
        args = {}
        if (streaming_metadata := _dict.get('streaming_metadata')) is not None:
            args['streaming_metadata'] = Metadata.from_dict(streaming_metadata)
        else:
            raise ValueError(
                'Required property \'streaming_metadata\' not present in CompleteItem JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CompleteItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(
                self,
                'streaming_metadata') and self.streaming_metadata is not None:
            if isinstance(self.streaming_metadata, dict):
                _dict['streaming_metadata'] = self.streaming_metadata
            else:
                _dict['streaming_metadata'] = self.streaming_metadata.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CompleteItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CompleteItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CompleteItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessageSourceAction(LogMessageSource):
    """
    An object that identifies the dialog element that generated the error message.

    :param str type: A string that indicates the type of dialog element that
          generated the error message.
    :param str action: The unique identifier of the action that generated the error
          message.
    """

    def __init__(
        self,
        type: str,
        action: str,
    ) -> None:
        """
        Initialize a LogMessageSourceAction object.

        :param str type: A string that indicates the type of dialog element that
               generated the error message.
        :param str action: The unique identifier of the action that generated the
               error message.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.action = action

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSourceAction':
        """Initialize a LogMessageSourceAction object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceAction JSON'
            )
        if (action := _dict.get('action')) is not None:
            args['action'] = action
        else:
            raise ValueError(
                'Required property \'action\' not present in LogMessageSourceAction JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessageSourceAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogMessageSourceAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessageSourceAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessageSourceAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessageSourceDialogNode(LogMessageSource):
    """
    An object that identifies the dialog element that generated the error message.

    :param str type: A string that indicates the type of dialog element that
          generated the error message.
    :param str dialog_node: The unique identifier of the dialog node that generated
          the error message.
    """

    def __init__(
        self,
        type: str,
        dialog_node: str,
    ) -> None:
        """
        Initialize a LogMessageSourceDialogNode object.

        :param str type: A string that indicates the type of dialog element that
               generated the error message.
        :param str dialog_node: The unique identifier of the dialog node that
               generated the error message.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.dialog_node = dialog_node

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSourceDialogNode':
        """Initialize a LogMessageSourceDialogNode object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceDialogNode JSON'
            )
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in LogMessageSourceDialogNode JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessageSourceDialogNode object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogMessageSourceDialogNode object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessageSourceDialogNode') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessageSourceDialogNode') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessageSourceHandler(LogMessageSource):
    """
    An object that identifies the dialog element that generated the error message.

    :param str type: A string that indicates the type of dialog element that
          generated the error message.
    :param str action: The unique identifier of the action that generated the error
          message.
    :param str step: (optional) The unique identifier of the step that generated the
          error message.
    :param str handler: The unique identifier of the handler that generated the
          error message.
    """

    def __init__(
        self,
        type: str,
        action: str,
        handler: str,
        *,
        step: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogMessageSourceHandler object.

        :param str type: A string that indicates the type of dialog element that
               generated the error message.
        :param str action: The unique identifier of the action that generated the
               error message.
        :param str handler: The unique identifier of the handler that generated the
               error message.
        :param str step: (optional) The unique identifier of the step that
               generated the error message.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.action = action
        self.step = step
        self.handler = handler

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSourceHandler':
        """Initialize a LogMessageSourceHandler object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceHandler JSON'
            )
        if (action := _dict.get('action')) is not None:
            args['action'] = action
        else:
            raise ValueError(
                'Required property \'action\' not present in LogMessageSourceHandler JSON'
            )
        if (step := _dict.get('step')) is not None:
            args['step'] = step
        if (handler := _dict.get('handler')) is not None:
            args['handler'] = handler
        else:
            raise ValueError(
                'Required property \'handler\' not present in LogMessageSourceHandler JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessageSourceHandler object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'step') and self.step is not None:
            _dict['step'] = self.step
        if hasattr(self, 'handler') and self.handler is not None:
            _dict['handler'] = self.handler
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogMessageSourceHandler object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessageSourceHandler') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessageSourceHandler') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessageSourceStep(LogMessageSource):
    """
    An object that identifies the dialog element that generated the error message.

    :param str type: A string that indicates the type of dialog element that
          generated the error message.
    :param str action: The unique identifier of the action that generated the error
          message.
    :param str step: The unique identifier of the step that generated the error
          message.
    """

    def __init__(
        self,
        type: str,
        action: str,
        step: str,
    ) -> None:
        """
        Initialize a LogMessageSourceStep object.

        :param str type: A string that indicates the type of dialog element that
               generated the error message.
        :param str action: The unique identifier of the action that generated the
               error message.
        :param str step: The unique identifier of the step that generated the error
               message.
        """
        # pylint: disable=super-init-not-called
        self.type = type
        self.action = action
        self.step = step

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSourceStep':
        """Initialize a LogMessageSourceStep object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceStep JSON'
            )
        if (action := _dict.get('action')) is not None:
            args['action'] = action
        else:
            raise ValueError(
                'Required property \'action\' not present in LogMessageSourceStep JSON'
            )
        if (step := _dict.get('step')) is not None:
            args['step'] = step
        else:
            raise ValueError(
                'Required property \'step\' not present in LogMessageSourceStep JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessageSourceStep object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'step') and self.step is not None:
            _dict['step'] = self.step
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogMessageSourceStep object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessageSourceStep') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessageSourceStep') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutputDebugTurnEventTurnEventActionFinished(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventActionFinished.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param str action_start_time: (optional) The time when the action started
          processing the message.
    :param str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :param str reason: (optional) The reason the action finished processing.
    :param dict action_variables: (optional) The state of all action variables at
          the time the action finished.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        action_start_time: Optional[str] = None,
        condition_type: Optional[str] = None,
        reason: Optional[str] = None,
        action_variables: Optional[dict] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventActionFinished object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param str action_start_time: (optional) The time when the action started
               processing the message.
        :param str condition_type: (optional) The type of condition (if any) that
               is defined for the action.
        :param str reason: (optional) The reason the action finished processing.
        :param dict action_variables: (optional) The state of all action variables
               at the time the action finished.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.action_start_time = action_start_time
        self.condition_type = condition_type
        self.reason = reason
        self.action_variables = action_variables

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'MessageOutputDebugTurnEventTurnEventActionFinished':
        """Initialize a MessageOutputDebugTurnEventTurnEventActionFinished object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (action_start_time := _dict.get('action_start_time')) is not None:
            args['action_start_time'] = action_start_time
        if (condition_type := _dict.get('condition_type')) is not None:
            args['condition_type'] = condition_type
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (action_variables := _dict.get('action_variables')) is not None:
            args['action_variables'] = action_variables
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventActionFinished object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self,
                   'action_start_time') and self.action_start_time is not None:
            _dict['action_start_time'] = self.action_start_time
        if hasattr(self, 'condition_type') and self.condition_type is not None:
            _dict['condition_type'] = self.condition_type
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self,
                   'action_variables') and self.action_variables is not None:
            _dict['action_variables'] = self.action_variables
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventActionFinished object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'MessageOutputDebugTurnEventTurnEventActionFinished'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'MessageOutputDebugTurnEventTurnEventActionFinished'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConditionTypeEnum(str, Enum):
        """
        The type of condition (if any) that is defined for the action.
        """

        USER_DEFINED = 'user_defined'
        WELCOME = 'welcome'
        ANYTHING_ELSE = 'anything_else'

    class ReasonEnum(str, Enum):
        """
        The reason the action finished processing.
        """

        ALL_STEPS_DONE = 'all_steps_done'
        NO_STEPS_VISITED = 'no_steps_visited'
        ENDED_BY_STEP = 'ended_by_step'
        CONNECT_TO_AGENT = 'connect_to_agent'
        MAX_RETRIES_REACHED = 'max_retries_reached'
        FALLBACK = 'fallback'


class MessageOutputDebugTurnEventTurnEventActionVisited(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventActionVisited.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param str action_start_time: (optional) The time when the action started
          processing the message.
    :param str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :param str reason: (optional) The reason the action was visited.
    :param str result_variable: (optional) The variable where the result of the call
          to the action is stored. Included only if **reason**=`subaction_return`.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        action_start_time: Optional[str] = None,
        condition_type: Optional[str] = None,
        reason: Optional[str] = None,
        result_variable: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventActionVisited object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param str action_start_time: (optional) The time when the action started
               processing the message.
        :param str condition_type: (optional) The type of condition (if any) that
               is defined for the action.
        :param str reason: (optional) The reason the action was visited.
        :param str result_variable: (optional) The variable where the result of the
               call to the action is stored. Included only if
               **reason**=`subaction_return`.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.action_start_time = action_start_time
        self.condition_type = condition_type
        self.reason = reason
        self.result_variable = result_variable

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventActionVisited':
        """Initialize a MessageOutputDebugTurnEventTurnEventActionVisited object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (action_start_time := _dict.get('action_start_time')) is not None:
            args['action_start_time'] = action_start_time
        if (condition_type := _dict.get('condition_type')) is not None:
            args['condition_type'] = condition_type
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        if (result_variable := _dict.get('result_variable')) is not None:
            args['result_variable'] = result_variable
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventActionVisited object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self,
                   'action_start_time') and self.action_start_time is not None:
            _dict['action_start_time'] = self.action_start_time
        if hasattr(self, 'condition_type') and self.condition_type is not None:
            _dict['condition_type'] = self.condition_type
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        if hasattr(self,
                   'result_variable') and self.result_variable is not None:
            _dict['result_variable'] = self.result_variable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventActionVisited object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventActionVisited') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventActionVisited') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConditionTypeEnum(str, Enum):
        """
        The type of condition (if any) that is defined for the action.
        """

        USER_DEFINED = 'user_defined'
        WELCOME = 'welcome'
        ANYTHING_ELSE = 'anything_else'

    class ReasonEnum(str, Enum):
        """
        The reason the action was visited.
        """

        INTENT = 'intent'
        INVOKE_SUBACTION = 'invoke_subaction'
        SUBACTION_RETURN = 'subaction_return'
        INVOKE_EXTERNAL = 'invoke_external'
        TOPIC_SWITCH = 'topic_switch'
        TOPIC_RETURN = 'topic_return'
        AGENT_REQUESTED = 'agent_requested'
        STEP_VALIDATION_FAILED = 'step_validation_failed'
        NO_ACTION_MATCHES = 'no_action_matches'


class MessageOutputDebugTurnEventTurnEventCallout(MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventCallout.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param TurnEventCalloutCallout callout: (optional)
    :param TurnEventCalloutError error: (optional)
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        callout: Optional['TurnEventCalloutCallout'] = None,
        error: Optional['TurnEventCalloutError'] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventCallout object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param TurnEventCalloutCallout callout: (optional)
        :param TurnEventCalloutError error: (optional)
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.callout = callout
        self.error = error

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventCallout':
        """Initialize a MessageOutputDebugTurnEventTurnEventCallout object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (callout := _dict.get('callout')) is not None:
            args['callout'] = TurnEventCalloutCallout.from_dict(callout)
        if (error := _dict.get('error')) is not None:
            args['error'] = TurnEventCalloutError.from_dict(error)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventCallout object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'callout') and self.callout is not None:
            if isinstance(self.callout, dict):
                _dict['callout'] = self.callout
            else:
                _dict['callout'] = self.callout.to_dict()
        if hasattr(self, 'error') and self.error is not None:
            if isinstance(self.error, dict):
                _dict['error'] = self.error
            else:
                _dict['error'] = self.error.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventCallout object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'MessageOutputDebugTurnEventTurnEventCallout') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'MessageOutputDebugTurnEventTurnEventCallout') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutputDebugTurnEventTurnEventHandlerVisited(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventHandlerVisited.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param str action_start_time: (optional) The time when the action started
          processing the message.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        action_start_time: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventHandlerVisited object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param str action_start_time: (optional) The time when the action started
               processing the message.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.action_start_time = action_start_time

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'MessageOutputDebugTurnEventTurnEventHandlerVisited':
        """Initialize a MessageOutputDebugTurnEventTurnEventHandlerVisited object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (action_start_time := _dict.get('action_start_time')) is not None:
            args['action_start_time'] = action_start_time
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventHandlerVisited object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self,
                   'action_start_time') and self.action_start_time is not None:
            _dict['action_start_time'] = self.action_start_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventHandlerVisited object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'MessageOutputDebugTurnEventTurnEventHandlerVisited'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'MessageOutputDebugTurnEventTurnEventHandlerVisited'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutputDebugTurnEventTurnEventNodeVisited(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventNodeVisited.

    :param str event: (optional) The type of turn event.
    :param TurnEventNodeSource source: (optional)
    :param str reason: (optional) The reason the dialog node was visited.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventNodeSource'] = None,
        reason: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventNodeVisited object.

        :param str event: (optional) The type of turn event.
        :param TurnEventNodeSource source: (optional)
        :param str reason: (optional) The reason the dialog node was visited.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.reason = reason

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventNodeVisited':
        """Initialize a MessageOutputDebugTurnEventTurnEventNodeVisited object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventNodeSource.from_dict(source)
        if (reason := _dict.get('reason')) is not None:
            args['reason'] = reason
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventNodeVisited object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'reason') and self.reason is not None:
            _dict['reason'] = self.reason
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventNodeVisited object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventNodeVisited') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventNodeVisited') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ReasonEnum(str, Enum):
        """
        The reason the dialog node was visited.
        """

        WELCOME = 'welcome'
        BRANCH_START = 'branch_start'
        TOPIC_SWITCH = 'topic_switch'
        TOPIC_RETURN = 'topic_return'
        TOPIC_SWITCH_WITHOUT_RETURN = 'topic_switch_without_return'
        JUMP = 'jump'


class MessageOutputDebugTurnEventTurnEventSearch(MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventSearch.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param TurnEventSearchError error: (optional)
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        error: Optional['TurnEventSearchError'] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventSearch object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param TurnEventSearchError error: (optional)
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.error = error

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventSearch':
        """Initialize a MessageOutputDebugTurnEventTurnEventSearch object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (error := _dict.get('error')) is not None:
            args['error'] = TurnEventSearchError.from_dict(error)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'error') and self.error is not None:
            if isinstance(self.error, dict):
                _dict['error'] = self.error
            else:
                _dict['error'] = self.error.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'MessageOutputDebugTurnEventTurnEventSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'MessageOutputDebugTurnEventTurnEventSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageOutputDebugTurnEventTurnEventStepAnswered(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventStepAnswered.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :param str action_start_time: (optional) The time when the action started
          processing the message.
    :param bool prompted: (optional) Whether the step was answered in response to a
          prompt from the assistant. If this property is `false`, the user provided the
          answer without visiting the step.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        condition_type: Optional[str] = None,
        action_start_time: Optional[str] = None,
        prompted: Optional[bool] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventStepAnswered object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param str condition_type: (optional) The type of condition (if any) that
               is defined for the action.
        :param str action_start_time: (optional) The time when the action started
               processing the message.
        :param bool prompted: (optional) Whether the step was answered in response
               to a prompt from the assistant. If this property is `false`, the user
               provided the answer without visiting the step.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.condition_type = condition_type
        self.action_start_time = action_start_time
        self.prompted = prompted

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventStepAnswered':
        """Initialize a MessageOutputDebugTurnEventTurnEventStepAnswered object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (condition_type := _dict.get('condition_type')) is not None:
            args['condition_type'] = condition_type
        if (action_start_time := _dict.get('action_start_time')) is not None:
            args['action_start_time'] = action_start_time
        if (prompted := _dict.get('prompted')) is not None:
            args['prompted'] = prompted
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventStepAnswered object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'condition_type') and self.condition_type is not None:
            _dict['condition_type'] = self.condition_type
        if hasattr(self,
                   'action_start_time') and self.action_start_time is not None:
            _dict['action_start_time'] = self.action_start_time
        if hasattr(self, 'prompted') and self.prompted is not None:
            _dict['prompted'] = self.prompted
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventStepAnswered object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventStepAnswered') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventStepAnswered') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConditionTypeEnum(str, Enum):
        """
        The type of condition (if any) that is defined for the action.
        """

        USER_DEFINED = 'user_defined'
        WELCOME = 'welcome'
        ANYTHING_ELSE = 'anything_else'


class MessageOutputDebugTurnEventTurnEventStepVisited(
        MessageOutputDebugTurnEvent):
    """
    MessageOutputDebugTurnEventTurnEventStepVisited.

    :param str event: (optional) The type of turn event.
    :param TurnEventActionSource source: (optional)
    :param str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :param str action_start_time: (optional) The time when the action started
          processing the message.
    :param bool has_question: (optional) Whether the step collects a customer
          response.
    """

    def __init__(
        self,
        *,
        event: Optional[str] = None,
        source: Optional['TurnEventActionSource'] = None,
        condition_type: Optional[str] = None,
        action_start_time: Optional[str] = None,
        has_question: Optional[bool] = None,
    ) -> None:
        """
        Initialize a MessageOutputDebugTurnEventTurnEventStepVisited object.

        :param str event: (optional) The type of turn event.
        :param TurnEventActionSource source: (optional)
        :param str condition_type: (optional) The type of condition (if any) that
               is defined for the action.
        :param str action_start_time: (optional) The time when the action started
               processing the message.
        :param bool has_question: (optional) Whether the step collects a customer
               response.
        """
        # pylint: disable=super-init-not-called
        self.event = event
        self.source = source
        self.condition_type = condition_type
        self.action_start_time = action_start_time
        self.has_question = has_question

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'MessageOutputDebugTurnEventTurnEventStepVisited':
        """Initialize a MessageOutputDebugTurnEventTurnEventStepVisited object from a json dictionary."""
        args = {}
        if (event := _dict.get('event')) is not None:
            args['event'] = event
        if (source := _dict.get('source')) is not None:
            args['source'] = TurnEventActionSource.from_dict(source)
        if (condition_type := _dict.get('condition_type')) is not None:
            args['condition_type'] = condition_type
        if (action_start_time := _dict.get('action_start_time')) is not None:
            args['action_start_time'] = action_start_time
        if (has_question := _dict.get('has_question')) is not None:
            args['has_question'] = has_question
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageOutputDebugTurnEventTurnEventStepVisited object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'event') and self.event is not None:
            _dict['event'] = self.event
        if hasattr(self, 'source') and self.source is not None:
            if isinstance(self.source, dict):
                _dict['source'] = self.source
            else:
                _dict['source'] = self.source.to_dict()
        if hasattr(self, 'condition_type') and self.condition_type is not None:
            _dict['condition_type'] = self.condition_type
        if hasattr(self,
                   'action_start_time') and self.action_start_time is not None:
            _dict['action_start_time'] = self.action_start_time
        if hasattr(self, 'has_question') and self.has_question is not None:
            _dict['has_question'] = self.has_question
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageOutputDebugTurnEventTurnEventStepVisited object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventStepVisited') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'MessageOutputDebugTurnEventTurnEventStepVisited') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ConditionTypeEnum(str, Enum):
        """
        The type of condition (if any) that is defined for the action.
        """

        USER_DEFINED = 'user_defined'
        WELCOME = 'welcome'
        ANYTHING_ELSE = 'anything_else'


class ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode(
        ProviderAuthenticationOAuth2Flows):
    """
    Non-private authentication settings for authorization-code flow.

    :param str token_url: (optional) The token URL.
    :param str refresh_url: (optional) The refresh token URL.
    :param str client_auth_type: (optional) The client authorization type.
    :param str content_type: (optional) The content type.
    :param str header_prefix: (optional) The prefix fo the header.
    :param str authorization_url: (optional) The authorization URL.
    :param str redirect_uri: (optional) The redirect URI.
    """

    def __init__(
        self,
        *,
        token_url: Optional[str] = None,
        refresh_url: Optional[str] = None,
        client_auth_type: Optional[str] = None,
        content_type: Optional[str] = None,
        header_prefix: Optional[str] = None,
        authorization_url: Optional[str] = None,
        redirect_uri: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode object.

        :param str token_url: (optional) The token URL.
        :param str refresh_url: (optional) The refresh token URL.
        :param str client_auth_type: (optional) The client authorization type.
        :param str content_type: (optional) The content type.
        :param str header_prefix: (optional) The prefix fo the header.
        :param str authorization_url: (optional) The authorization URL.
        :param str redirect_uri: (optional) The redirect URI.
        """
        # pylint: disable=super-init-not-called
        self.token_url = token_url
        self.refresh_url = refresh_url
        self.client_auth_type = client_auth_type
        self.content_type = content_type
        self.header_prefix = header_prefix
        self.authorization_url = authorization_url
        self.redirect_uri = redirect_uri

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode':
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode object from a json dictionary."""
        args = {}
        if (token_url := _dict.get('token_url')) is not None:
            args['token_url'] = token_url
        if (refresh_url := _dict.get('refresh_url')) is not None:
            args['refresh_url'] = refresh_url
        if (client_auth_type := _dict.get('client_auth_type')) is not None:
            args['client_auth_type'] = client_auth_type
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        if (header_prefix := _dict.get('header_prefix')) is not None:
            args['header_prefix'] = header_prefix
        if (authorization_url := _dict.get('authorization_url')) is not None:
            args['authorization_url'] = authorization_url
        if (redirect_uri := _dict.get('redirect_uri')) is not None:
            args['redirect_uri'] = redirect_uri
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token_url') and self.token_url is not None:
            _dict['token_url'] = self.token_url
        if hasattr(self, 'refresh_url') and self.refresh_url is not None:
            _dict['refresh_url'] = self.refresh_url
        if hasattr(self,
                   'client_auth_type') and self.client_auth_type is not None:
            _dict['client_auth_type'] = self.client_auth_type
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'header_prefix') and self.header_prefix is not None:
            _dict['header_prefix'] = self.header_prefix
        if hasattr(self,
                   'authorization_url') and self.authorization_url is not None:
            _dict['authorization_url'] = self.authorization_url
        if hasattr(self, 'redirect_uri') and self.redirect_uri is not None:
            _dict['redirect_uri'] = self.redirect_uri
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2AuthorizationCode'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ClientAuthTypeEnum(str, Enum):
        """
        The client authorization type.
        """

        BODY = 'Body'
        BASICAUTHHEADER = 'BasicAuthHeader'


class ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials(
        ProviderAuthenticationOAuth2Flows):
    """
    ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials.

    :param str token_url: (optional) The token URL.
    :param str refresh_url: (optional) The refresh token URL.
    :param str client_auth_type: (optional) The client authorization type.
    :param str content_type: (optional) The content type.
    :param str header_prefix: (optional) The prefix fo the header.
    """

    def __init__(
        self,
        *,
        token_url: Optional[str] = None,
        refresh_url: Optional[str] = None,
        client_auth_type: Optional[str] = None,
        content_type: Optional[str] = None,
        header_prefix: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials object.

        :param str token_url: (optional) The token URL.
        :param str refresh_url: (optional) The refresh token URL.
        :param str client_auth_type: (optional) The client authorization type.
        :param str content_type: (optional) The content type.
        :param str header_prefix: (optional) The prefix fo the header.
        """
        # pylint: disable=super-init-not-called
        self.token_url = token_url
        self.refresh_url = refresh_url
        self.client_auth_type = client_auth_type
        self.content_type = content_type
        self.header_prefix = header_prefix

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials':
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials object from a json dictionary."""
        args = {}
        if (token_url := _dict.get('token_url')) is not None:
            args['token_url'] = token_url
        if (refresh_url := _dict.get('refresh_url')) is not None:
            args['refresh_url'] = refresh_url
        if (client_auth_type := _dict.get('client_auth_type')) is not None:
            args['client_auth_type'] = client_auth_type
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        if (header_prefix := _dict.get('header_prefix')) is not None:
            args['header_prefix'] = header_prefix
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token_url') and self.token_url is not None:
            _dict['token_url'] = self.token_url
        if hasattr(self, 'refresh_url') and self.refresh_url is not None:
            _dict['refresh_url'] = self.refresh_url
        if hasattr(self,
                   'client_auth_type') and self.client_auth_type is not None:
            _dict['client_auth_type'] = self.client_auth_type
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'header_prefix') and self.header_prefix is not None:
            _dict['header_prefix'] = self.header_prefix
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2ClientCredentials'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ClientAuthTypeEnum(str, Enum):
        """
        The client authorization type.
        """

        BODY = 'Body'
        BASICAUTHHEADER = 'BasicAuthHeader'


class ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password(
        ProviderAuthenticationOAuth2Flows):
    """
    Non-private authentication settings for resource owner password flow.

    :param str token_url: (optional) The token URL.
    :param str refresh_url: (optional) The refresh token URL.
    :param str client_auth_type: (optional) The client authorization type.
    :param str content_type: (optional) The content type.
    :param str header_prefix: (optional) The prefix fo the header.
    :param ProviderAuthenticationOAuth2PasswordUsername username: (optional) The
          username for oauth2 authentication when the preferred flow is "password".
    """

    def __init__(
        self,
        *,
        token_url: Optional[str] = None,
        refresh_url: Optional[str] = None,
        client_auth_type: Optional[str] = None,
        content_type: Optional[str] = None,
        header_prefix: Optional[str] = None,
        username: Optional[
            'ProviderAuthenticationOAuth2PasswordUsername'] = None,
    ) -> None:
        """
        Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password object.

        :param str token_url: (optional) The token URL.
        :param str refresh_url: (optional) The refresh token URL.
        :param str client_auth_type: (optional) The client authorization type.
        :param str content_type: (optional) The content type.
        :param str header_prefix: (optional) The prefix fo the header.
        :param ProviderAuthenticationOAuth2PasswordUsername username: (optional)
               The username for oauth2 authentication when the preferred flow is
               "password".
        """
        # pylint: disable=super-init-not-called
        self.token_url = token_url
        self.refresh_url = refresh_url
        self.client_auth_type = client_auth_type
        self.content_type = content_type
        self.header_prefix = header_prefix
        self.username = username

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password':
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password object from a json dictionary."""
        args = {}
        if (token_url := _dict.get('token_url')) is not None:
            args['token_url'] = token_url
        if (refresh_url := _dict.get('refresh_url')) is not None:
            args['refresh_url'] = refresh_url
        if (client_auth_type := _dict.get('client_auth_type')) is not None:
            args['client_auth_type'] = client_auth_type
        if (content_type := _dict.get('content_type')) is not None:
            args['content_type'] = content_type
        if (header_prefix := _dict.get('header_prefix')) is not None:
            args['header_prefix'] = header_prefix
        if (username := _dict.get('username')) is not None:
            args[
                'username'] = ProviderAuthenticationOAuth2PasswordUsername.from_dict(
                    username)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token_url') and self.token_url is not None:
            _dict['token_url'] = self.token_url
        if hasattr(self, 'refresh_url') and self.refresh_url is not None:
            _dict['refresh_url'] = self.refresh_url
        if hasattr(self,
                   'client_auth_type') and self.client_auth_type is not None:
            _dict['client_auth_type'] = self.client_auth_type
        if hasattr(self, 'content_type') and self.content_type is not None:
            _dict['content_type'] = self.content_type
        if hasattr(self, 'header_prefix') and self.header_prefix is not None:
            _dict['header_prefix'] = self.header_prefix
        if hasattr(self, 'username') and self.username is not None:
            if isinstance(self.username, dict):
                _dict['username'] = self.username
            else:
                _dict['username'] = self.username.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderAuthenticationOAuth2FlowsProviderAuthenticationOAuth2Password'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ClientAuthTypeEnum(str, Enum):
        """
        The client authorization type.
        """

        BODY = 'Body'
        BASICAUTHHEADER = 'BasicAuthHeader'


class ProviderPrivateAuthenticationBasicFlow(ProviderPrivateAuthentication):
    """
    The private data for basic authentication.

    :param ProviderAuthenticationTypeAndValue password: (optional) The password for
          bearer authentication.
    """

    def __init__(
        self,
        *,
        password: Optional['ProviderAuthenticationTypeAndValue'] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationBasicFlow object.

        :param ProviderAuthenticationTypeAndValue password: (optional) The password
               for bearer authentication.
        """
        # pylint: disable=super-init-not-called
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ProviderPrivateAuthenticationBasicFlow':
        """Initialize a ProviderPrivateAuthenticationBasicFlow object from a json dictionary."""
        args = {}
        if (password := _dict.get('password')) is not None:
            args['password'] = ProviderAuthenticationTypeAndValue.from_dict(
                password)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationBasicFlow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'password') and self.password is not None:
            if isinstance(self.password, dict):
                _dict['password'] = self.password
            else:
                _dict['password'] = self.password.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationBasicFlow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderPrivateAuthenticationBasicFlow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderPrivateAuthenticationBasicFlow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthenticationBearerFlow(ProviderPrivateAuthentication):
    """
    The private data for bearer authentication.

    :param ProviderAuthenticationTypeAndValue token: (optional) The token for bearer
          authentication.
    """

    def __init__(
        self,
        *,
        token: Optional['ProviderAuthenticationTypeAndValue'] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationBearerFlow object.

        :param ProviderAuthenticationTypeAndValue token: (optional) The token for
               bearer authentication.
        """
        # pylint: disable=super-init-not-called
        self.token = token

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'ProviderPrivateAuthenticationBearerFlow':
        """Initialize a ProviderPrivateAuthenticationBearerFlow object from a json dictionary."""
        args = {}
        if (token := _dict.get('token')) is not None:
            args['token'] = ProviderAuthenticationTypeAndValue.from_dict(token)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationBearerFlow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'token') and self.token is not None:
            if isinstance(self.token, dict):
                _dict['token'] = self.token
            else:
                _dict['token'] = self.token.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationBearerFlow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderPrivateAuthenticationBearerFlow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderPrivateAuthenticationBearerFlow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthenticationOAuth2Flow(ProviderPrivateAuthentication):
    """
    The private data for oauth2 authentication.

    :param ProviderPrivateAuthenticationOAuth2FlowFlows flows: (optional) Scenarios
          performed by the API client to fetch an access token from the authorization
          server.
    """

    def __init__(
        self,
        *,
        flows: Optional['ProviderPrivateAuthenticationOAuth2FlowFlows'] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2Flow object.

        :param ProviderPrivateAuthenticationOAuth2FlowFlows flows: (optional)
               Scenarios performed by the API client to fetch an access token from the
               authorization server.
        """
        # pylint: disable=super-init-not-called
        self.flows = flows

    @classmethod
    def from_dict(cls,
                  _dict: Dict) -> 'ProviderPrivateAuthenticationOAuth2Flow':
        """Initialize a ProviderPrivateAuthenticationOAuth2Flow object from a json dictionary."""
        args = {}
        if (flows := _dict.get('flows')) is not None:
            args['flows'] = flows
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationOAuth2Flow object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'flows') and self.flows is not None:
            if isinstance(self.flows, dict):
                _dict['flows'] = self.flows
            else:
                _dict['flows'] = self.flows.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationOAuth2Flow object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ProviderPrivateAuthenticationOAuth2Flow') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ProviderPrivateAuthenticationOAuth2Flow') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode(
        ProviderPrivateAuthenticationOAuth2FlowFlows):
    """
    Private authentication settings for client credentials flow.

    :param str client_id: (optional) The client ID.
    :param str client_secret: (optional) The client secret.
    :param str access_token: (optional) The access token.
    :param str refresh_token: (optional) The refresh token.
    :param str authorization_code: (optional) The authorization code.
    """

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        authorization_code: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode object.

        :param str client_id: (optional) The client ID.
        :param str client_secret: (optional) The client secret.
        :param str access_token: (optional) The access token.
        :param str refresh_token: (optional) The refresh token.
        :param str authorization_code: (optional) The authorization code.
        """
        # pylint: disable=super-init-not-called
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.authorization_code = authorization_code

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode':
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode object from a json dictionary."""
        args = {}
        if (client_id := _dict.get('client_id')) is not None:
            args['client_id'] = client_id
        if (client_secret := _dict.get('client_secret')) is not None:
            args['client_secret'] = client_secret
        if (access_token := _dict.get('access_token')) is not None:
            args['access_token'] = access_token
        if (refresh_token := _dict.get('refresh_token')) is not None:
            args['refresh_token'] = refresh_token
        if (authorization_code := _dict.get('authorization_code')) is not None:
            args['authorization_code'] = authorization_code
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'client_secret') and self.client_secret is not None:
            _dict['client_secret'] = self.client_secret
        if hasattr(self, 'access_token') and self.access_token is not None:
            _dict['access_token'] = self.access_token
        if hasattr(self, 'refresh_token') and self.refresh_token is not None:
            _dict['refresh_token'] = self.refresh_token
        if hasattr(
                self,
                'authorization_code') and self.authorization_code is not None:
            _dict['authorization_code'] = self.authorization_code
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2AuthorizationCode'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials(
        ProviderPrivateAuthenticationOAuth2FlowFlows):
    """
    ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials.

    :param str client_id: (optional) The client ID.
    :param str client_secret: (optional) The client secret.
    :param str access_token: (optional) The access token.
    :param str refresh_token: (optional) The refresh token.
    """

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials object.

        :param str client_id: (optional) The client ID.
        :param str client_secret: (optional) The client secret.
        :param str access_token: (optional) The access token.
        :param str refresh_token: (optional) The refresh token.
        """
        # pylint: disable=super-init-not-called
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials':
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials object from a json dictionary."""
        args = {}
        if (client_id := _dict.get('client_id')) is not None:
            args['client_id'] = client_id
        if (client_secret := _dict.get('client_secret')) is not None:
            args['client_secret'] = client_secret
        if (access_token := _dict.get('access_token')) is not None:
            args['access_token'] = access_token
        if (refresh_token := _dict.get('refresh_token')) is not None:
            args['refresh_token'] = refresh_token
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'client_secret') and self.client_secret is not None:
            _dict['client_secret'] = self.client_secret
        if hasattr(self, 'access_token') and self.access_token is not None:
            _dict['access_token'] = self.access_token
        if hasattr(self, 'refresh_token') and self.refresh_token is not None:
            _dict['refresh_token'] = self.refresh_token
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2ClientCredentials'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password(
        ProviderPrivateAuthenticationOAuth2FlowFlows):
    """
    Private authentication settings for resource owner password flow.

    :param str client_id: (optional) The client ID.
    :param str client_secret: (optional) The client secret.
    :param str access_token: (optional) The access token.
    :param str refresh_token: (optional) The refresh token.
    :param ProviderPrivateAuthenticationOAuth2PasswordPassword password: (optional)
          The password for oauth2 authentication when the preferred flow is "password".
    """

    def __init__(
        self,
        *,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        password: Optional[
            'ProviderPrivateAuthenticationOAuth2PasswordPassword'] = None,
    ) -> None:
        """
        Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password object.

        :param str client_id: (optional) The client ID.
        :param str client_secret: (optional) The client secret.
        :param str access_token: (optional) The access token.
        :param str refresh_token: (optional) The refresh token.
        :param ProviderPrivateAuthenticationOAuth2PasswordPassword password:
               (optional) The password for oauth2 authentication when the preferred flow
               is "password".
        """
        # pylint: disable=super-init-not-called
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.password = password

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password':
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password object from a json dictionary."""
        args = {}
        if (client_id := _dict.get('client_id')) is not None:
            args['client_id'] = client_id
        if (client_secret := _dict.get('client_secret')) is not None:
            args['client_secret'] = client_secret
        if (access_token := _dict.get('access_token')) is not None:
            args['access_token'] = access_token
        if (refresh_token := _dict.get('refresh_token')) is not None:
            args['refresh_token'] = refresh_token
        if (password := _dict.get('password')) is not None:
            args[
                'password'] = ProviderPrivateAuthenticationOAuth2PasswordPassword.from_dict(
                    password)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'client_id') and self.client_id is not None:
            _dict['client_id'] = self.client_id
        if hasattr(self, 'client_secret') and self.client_secret is not None:
            _dict['client_secret'] = self.client_secret
        if hasattr(self, 'access_token') and self.access_token is not None:
            _dict['access_token'] = self.access_token
        if hasattr(self, 'refresh_token') and self.refresh_token is not None:
            _dict['refresh_token'] = self.refresh_token
        if hasattr(self, 'password') and self.password is not None:
            if isinstance(self.password, dict):
                _dict['password'] = self.password
            else:
                _dict['password'] = self.password.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'ProviderPrivateAuthenticationOAuth2FlowFlowsProviderPrivateAuthenticationOAuth2Password'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeAudio(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeAudio.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the audio clip.
    :param str title: (optional) The title or introductory text to show before the
          response.
    :param str description: (optional) The description to show with the the
          response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :param dict channel_options: (optional) For internal use only.
    :param str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the audio player cannot be seen.
    """

    def __init__(
        self,
        response_type: str,
        source: str,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
        channel_options: Optional[dict] = None,
        alt_text: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeAudio object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the audio clip.
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the the
               response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        :param dict channel_options: (optional) For internal use only.
        :param str alt_text: (optional) Descriptive text that can be used for
               screen readers or other situations where the audio player cannot be seen.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.source = source
        self.title = title
        self.description = description
        self.channels = channels
        self.channel_options = channel_options
        self.alt_text = alt_text

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeAudio':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeAudio object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeAudio JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeAudio JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        if (channel_options := _dict.get('channel_options')) is not None:
            args['channel_options'] = channel_options
        if (alt_text := _dict.get('alt_text')) is not None:
            args['alt_text'] = alt_text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeAudio object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        if hasattr(self,
                   'channel_options') and self.channel_options is not None:
            _dict['channel_options'] = self.channel_options
        if hasattr(self, 'alt_text') and self.alt_text is not None:
            _dict['alt_text'] = self.alt_text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeAudio object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeAudio') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeAudio') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeChannelTransfer(
        RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeChannelTransfer.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
           **Note:** The `channel_transfer` response type is not supported on IBM Cloud
          Pak for Data.
    :param str message_to_user: The message to display to the user when initiating a
          channel transfer.
    :param ChannelTransferInfo transfer_info: Information used by an integration to
          transfer the conversation to a different channel.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        message_to_user: str,
        transfer_info: 'ChannelTransferInfo',
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeChannelTransfer object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
                **Note:** The `channel_transfer` response type is not supported on IBM
               Cloud Pak for Data.
        :param str message_to_user: The message to display to the user when
               initiating a channel transfer.
        :param ChannelTransferInfo transfer_info: Information used by an
               integration to transfer the conversation to a different channel.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.message_to_user = message_to_user
        self.transfer_info = transfer_info
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeChannelTransfer object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if (message_to_user := _dict.get('message_to_user')) is not None:
            args['message_to_user'] = message_to_user
        else:
            raise ValueError(
                'Required property \'message_to_user\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if (transfer_info := _dict.get('transfer_info')) is not None:
            args['transfer_info'] = ChannelTransferInfo.from_dict(transfer_info)
        else:
            raise ValueError(
                'Required property \'transfer_info\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeChannelTransfer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self,
                   'message_to_user') and self.message_to_user is not None:
            _dict['message_to_user'] = self.message_to_user
        if hasattr(self, 'transfer_info') and self.transfer_info is not None:
            if isinstance(self.transfer_info, dict):
                _dict['transfer_info'] = self.transfer_info
            else:
                _dict['transfer_info'] = self.transfer_info.to_dict()
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeChannelTransfer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'RuntimeResponseGenericRuntimeResponseTypeChannelTransfer'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeConnectToAgent(
        RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeConnectToAgent.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str message_to_human_agent: (optional) A message to be sent to the human
          agent who will be taking over the conversation.
    :param AgentAvailabilityMessage agent_available: (optional) An optional message
          to be displayed to the user to indicate that the conversation will be
          transferred to the next available agent.
    :param AgentAvailabilityMessage agent_unavailable: (optional) An optional
          message to be displayed to the user to indicate that no online agent is
          available to take over the conversation.
    :param DialogNodeOutputConnectToAgentTransferInfo transfer_info: (optional)
          Routing or other contextual information to be used by target service desk
          systems.
    :param str topic: (optional) A label identifying the topic of the conversation,
          derived from the **title** property of the relevant node or the **topic**
          property of the dialog node response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        *,
        message_to_human_agent: Optional[str] = None,
        agent_available: Optional['AgentAvailabilityMessage'] = None,
        agent_unavailable: Optional['AgentAvailabilityMessage'] = None,
        transfer_info: Optional[
            'DialogNodeOutputConnectToAgentTransferInfo'] = None,
        topic: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str message_to_human_agent: (optional) A message to be sent to the
               human agent who will be taking over the conversation.
        :param AgentAvailabilityMessage agent_available: (optional) An optional
               message to be displayed to the user to indicate that the conversation will
               be transferred to the next available agent.
        :param AgentAvailabilityMessage agent_unavailable: (optional) An optional
               message to be displayed to the user to indicate that no online agent is
               available to take over the conversation.
        :param DialogNodeOutputConnectToAgentTransferInfo transfer_info: (optional)
               Routing or other contextual information to be used by target service desk
               systems.
        :param str topic: (optional) A label identifying the topic of the
               conversation, derived from the **title** property of the relevant node or
               the **topic** property of the dialog node response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.message_to_human_agent = message_to_human_agent
        self.agent_available = agent_available
        self.agent_unavailable = agent_unavailable
        self.transfer_info = transfer_info
        self.topic = topic
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeConnectToAgent JSON'
            )
        if (message_to_human_agent :=
                _dict.get('message_to_human_agent')) is not None:
            args['message_to_human_agent'] = message_to_human_agent
        if (agent_available := _dict.get('agent_available')) is not None:
            args['agent_available'] = AgentAvailabilityMessage.from_dict(
                agent_available)
        if (agent_unavailable := _dict.get('agent_unavailable')) is not None:
            args['agent_unavailable'] = AgentAvailabilityMessage.from_dict(
                agent_unavailable)
        if (transfer_info := _dict.get('transfer_info')) is not None:
            args[
                'transfer_info'] = DialogNodeOutputConnectToAgentTransferInfo.from_dict(
                    transfer_info)
        if (topic := _dict.get('topic')) is not None:
            args['topic'] = topic
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeConnectToAgent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'message_to_human_agent'
                  ) and self.message_to_human_agent is not None:
            _dict['message_to_human_agent'] = self.message_to_human_agent
        if hasattr(self,
                   'agent_available') and self.agent_available is not None:
            if isinstance(self.agent_available, dict):
                _dict['agent_available'] = self.agent_available
            else:
                _dict['agent_available'] = self.agent_available.to_dict()
        if hasattr(self,
                   'agent_unavailable') and self.agent_unavailable is not None:
            if isinstance(self.agent_unavailable, dict):
                _dict['agent_unavailable'] = self.agent_unavailable
            else:
                _dict['agent_unavailable'] = self.agent_unavailable.to_dict()
        if hasattr(self, 'transfer_info') and self.transfer_info is not None:
            if isinstance(self.transfer_info, dict):
                _dict['transfer_info'] = self.transfer_info
            else:
                _dict['transfer_info'] = self.transfer_info.to_dict()
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeConnectToAgent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'RuntimeResponseGenericRuntimeResponseTypeConnectToAgent'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeDate(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeDate.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    """

    def __init__(
        self,
        response_type: str,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeDate object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeDate':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeDate object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeDate JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeDate object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeDate object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeDate') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeDate') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeIframe(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeIframe.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the embeddable content.
    :param str title: (optional) The title or introductory text to show before the
          response.
    :param str description: (optional) The description to show with the the
          response.
    :param str image_url: (optional) The URL of an image that shows a preview of the
          embedded content.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        source: str,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        image_url: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeIframe object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the embeddable content.
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the the
               response.
        :param str image_url: (optional) The URL of an image that shows a preview
               of the embedded content.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.source = source
        self.title = title
        self.description = description
        self.image_url = image_url
        self.channels = channels

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeIframe':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeIframe object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeIframe JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeIframe JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (image_url := _dict.get('image_url')) is not None:
            args['image_url'] = image_url
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeIframe object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'image_url') and self.image_url is not None:
            _dict['image_url'] = self.image_url
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeIframe object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeIframe') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeIframe') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeImage(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeImage.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the image.
    :param str title: (optional) The title to show before the response.
    :param str description: (optional) The description to show with the the
          response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :param str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the image cannot be seen.
    """

    def __init__(
        self,
        response_type: str,
        source: str,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
        alt_text: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeImage object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the image.
        :param str title: (optional) The title to show before the response.
        :param str description: (optional) The description to show with the the
               response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        :param str alt_text: (optional) Descriptive text that can be used for
               screen readers or other situations where the image cannot be seen.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.source = source
        self.title = title
        self.description = description
        self.channels = channels
        self.alt_text = alt_text

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeImage':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeImage object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeImage JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeImage JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        if (alt_text := _dict.get('alt_text')) is not None:
            args['alt_text'] = alt_text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeImage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        if hasattr(self, 'alt_text') and self.alt_text is not None:
            _dict['alt_text'] = self.alt_text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeImage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeImage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeImage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeOption(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeOption.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str title: The title or introductory text to show before the response.
    :param str description: (optional) The description to show with the the
          response.
    :param str preference: (optional) The preferred type of control to display.
    :param List[DialogNodeOutputOptionsElement] options: An array of objects
          describing the options from which the user can choose.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        title: str,
        options: List['DialogNodeOutputOptionsElement'],
        *,
        description: Optional[str] = None,
        preference: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeOption object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str title: The title or introductory text to show before the
               response.
        :param List[DialogNodeOutputOptionsElement] options: An array of objects
               describing the options from which the user can choose.
        :param str description: (optional) The description to show with the the
               response.
        :param str preference: (optional) The preferred type of control to display.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.title = title
        self.description = description
        self.preference = preference
        self.options = options
        self.channels = channels

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeOption':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeOption object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        else:
            raise ValueError(
                'Required property \'title\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (preference := _dict.get('preference')) is not None:
            args['preference'] = preference
        if (options := _dict.get('options')) is not None:
            args['options'] = [
                DialogNodeOutputOptionsElement.from_dict(v) for v in options
            ]
        else:
            raise ValueError(
                'Required property \'options\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeOption object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        if hasattr(self, 'options') and self.options is not None:
            options_list = []
            for v in self.options:
                if isinstance(v, dict):
                    options_list.append(v)
                else:
                    options_list.append(v.to_dict())
            _dict['options'] = options_list
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeOption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeOption') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeOption') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PreferenceEnum(str, Enum):
        """
        The preferred type of control to display.
        """

        DROPDOWN = 'dropdown'
        BUTTON = 'button'


class RuntimeResponseGenericRuntimeResponseTypePause(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypePause.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param int time: How long to pause, in milliseconds.
    :param bool typing: (optional) Whether to send a "user is typing" event during
          the pause.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        time: int,
        *,
        typing: Optional[bool] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypePause object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param int time: How long to pause, in milliseconds.
        :param bool typing: (optional) Whether to send a "user is typing" event
               during the pause.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.time = time
        self.typing = typing
        self.channels = channels

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypePause':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypePause object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypePause JSON'
            )
        if (time := _dict.get('time')) is not None:
            args['time'] = time
        else:
            raise ValueError(
                'Required property \'time\' not present in RuntimeResponseGenericRuntimeResponseTypePause JSON'
            )
        if (typing := _dict.get('typing')) is not None:
            args['typing'] = typing
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypePause object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = self.time
        if hasattr(self, 'typing') and self.typing is not None:
            _dict['typing'] = self.typing
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypePause object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypePause') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypePause') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeSearch(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeSearch.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str header: The title or introductory text to show before the response.
          This text is defined in the search skill configuration.
    :param List[SearchResult] primary_results: An array of objects that contains the
          search results to be displayed in the initial response to the user.
    :param List[SearchResult] additional_results: An array of objects that contains
          additional search results that can be displayed to the user upon request.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        header: str,
        primary_results: List['SearchResult'],
        additional_results: List['SearchResult'],
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeSearch object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str header: The title or introductory text to show before the
               response. This text is defined in the search skill configuration.
        :param List[SearchResult] primary_results: An array of objects that
               contains the search results to be displayed in the initial response to the
               user.
        :param List[SearchResult] additional_results: An array of objects that
               contains additional search results that can be displayed to the user upon
               request.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.header = header
        self.primary_results = primary_results
        self.additional_results = additional_results
        self.channels = channels

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeSearch':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeSearch object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if (header := _dict.get('header')) is not None:
            args['header'] = header
        else:
            raise ValueError(
                'Required property \'header\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if (primary_results := _dict.get('primary_results')) is not None:
            args['primary_results'] = [
                SearchResult.from_dict(v) for v in primary_results
            ]
        else:
            raise ValueError(
                'Required property \'primary_results\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if (additional_results := _dict.get('additional_results')) is not None:
            args['additional_results'] = [
                SearchResult.from_dict(v) for v in additional_results
            ]
        else:
            raise ValueError(
                'Required property \'additional_results\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeSearch object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'header') and self.header is not None:
            _dict['header'] = self.header
        if hasattr(self,
                   'primary_results') and self.primary_results is not None:
            primary_results_list = []
            for v in self.primary_results:
                if isinstance(v, dict):
                    primary_results_list.append(v)
                else:
                    primary_results_list.append(v.to_dict())
            _dict['primary_results'] = primary_results_list
        if hasattr(
                self,
                'additional_results') and self.additional_results is not None:
            additional_results_list = []
            for v in self.additional_results:
                if isinstance(v, dict):
                    additional_results_list.append(v)
                else:
                    additional_results_list.append(v.to_dict())
            _dict['additional_results'] = additional_results_list
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeSearch object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeSearch') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self,
            other: 'RuntimeResponseGenericRuntimeResponseTypeSearch') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeSuggestion(
        RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeSuggestion.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str title: The title or introductory text to show before the response.
    :param List[DialogSuggestion] suggestions: An array of objects describing the
          possible matching dialog nodes from which the user can choose.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        title: str,
        suggestions: List['DialogSuggestion'],
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeSuggestion object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str title: The title or introductory text to show before the
               response.
        :param List[DialogSuggestion] suggestions: An array of objects describing
               the possible matching dialog nodes from which the user can choose.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.title = title
        self.suggestions = suggestions
        self.channels = channels

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'RuntimeResponseGenericRuntimeResponseTypeSuggestion':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeSuggestion object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        else:
            raise ValueError(
                'Required property \'title\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if (suggestions := _dict.get('suggestions')) is not None:
            args['suggestions'] = [
                DialogSuggestion.from_dict(v) for v in suggestions
            ]
        else:
            raise ValueError(
                'Required property \'suggestions\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeSuggestion object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'suggestions') and self.suggestions is not None:
            suggestions_list = []
            for v in self.suggestions:
                if isinstance(v, dict):
                    suggestions_list.append(v)
                else:
                    suggestions_list.append(v.to_dict())
            _dict['suggestions'] = suggestions_list
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeSuggestion object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'RuntimeResponseGenericRuntimeResponseTypeSuggestion'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'RuntimeResponseGenericRuntimeResponseTypeSuggestion'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeText(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeText.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str text: The text of the response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        text: str,
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeText object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str text: The text of the response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.text = text
        self.channels = channels

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeText':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeText object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeText JSON'
            )
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in RuntimeResponseGenericRuntimeResponseTypeText JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeText object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeText object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeText') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeText') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeUserDefined(
        RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeUserDefined.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param dict user_defined: An object containing any properties for the
          user-defined response type.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
        self,
        response_type: str,
        user_defined: dict,
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeUserDefined object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param dict user_defined: An object containing any properties for the
               user-defined response type.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.user_defined = user_defined
        self.channels = channels

    @classmethod
    def from_dict(
            cls, _dict: Dict
    ) -> 'RuntimeResponseGenericRuntimeResponseTypeUserDefined':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeUserDefined object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeUserDefined JSON'
            )
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        else:
            raise ValueError(
                'Required property \'user_defined\' not present in RuntimeResponseGenericRuntimeResponseTypeUserDefined JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeUserDefined object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'user_defined') and self.user_defined is not None:
            _dict['user_defined'] = self.user_defined
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeUserDefined object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
            self, other: 'RuntimeResponseGenericRuntimeResponseTypeUserDefined'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
            self, other: 'RuntimeResponseGenericRuntimeResponseTypeUserDefined'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGenericRuntimeResponseTypeVideo(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeVideo.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the video.
    :param str title: (optional) The title or introductory text to show before the
          response.
    :param str description: (optional) The description to show with the the
          response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :param dict channel_options: (optional) For internal use only.
    :param str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the video cannot be seen.
    """

    def __init__(
        self,
        response_type: str,
        source: str,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
        channel_options: Optional[dict] = None,
        alt_text: Optional[str] = None,
    ) -> None:
        """
        Initialize a RuntimeResponseGenericRuntimeResponseTypeVideo object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the video.
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the the
               response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended. If
               **channels** is present, the response is intended for a built-in
               integration and should not be handled by an API client.
        :param dict channel_options: (optional) For internal use only.
        :param str alt_text: (optional) Descriptive text that can be used for
               screen readers or other situations where the video cannot be seen.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.source = source
        self.title = title
        self.description = description
        self.channels = channels
        self.channel_options = channel_options
        self.alt_text = alt_text

    @classmethod
    def from_dict(
            cls,
            _dict: Dict) -> 'RuntimeResponseGenericRuntimeResponseTypeVideo':
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeVideo object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeVideo JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeVideo JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        if (channel_options := _dict.get('channel_options')) is not None:
            args['channel_options'] = channel_options
        if (alt_text := _dict.get('alt_text')) is not None:
            args['alt_text'] = alt_text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGenericRuntimeResponseTypeVideo object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'channels') and self.channels is not None:
            channels_list = []
            for v in self.channels:
                if isinstance(v, dict):
                    channels_list.append(v)
                else:
                    channels_list.append(v.to_dict())
            _dict['channels'] = channels_list
        if hasattr(self,
                   'channel_options') and self.channel_options is not None:
            _dict['channel_options'] = self.channel_options
        if hasattr(self, 'alt_text') and self.alt_text is not None:
            _dict['alt_text'] = self.alt_text
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this RuntimeResponseGenericRuntimeResponseTypeVideo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeVideo') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self,
               other: 'RuntimeResponseGenericRuntimeResponseTypeVideo') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
