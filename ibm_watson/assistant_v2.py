# coding: utf-8

# (C) Copyright IBM Corp. 2019, 2023.
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

# IBM OpenAPI SDK Code Generator Version: 3.64.1-cee95189-20230124-211647
"""
The IBM Watson&trade; Assistant service combines machine learning, natural language
understanding, and an integrated dialog editor to create conversation flows between your
apps and your users.
The Assistant v2 API provides runtime methods your client application can use to send user
input to an assistant and receive a response.

API Version: 2.0
See: https://cloud.ibm.com/docs/assistant
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
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
               Specify dates in YYYY-MM-DD format. The current version is `2021-11-27`.

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
    # Assistants
    #########################

    def create_assistant(self,
                         *,
                         language: str = None,
                         name: str = None,
                         description: str = None,
                         **kwargs) -> DetailedResponse:
        """
        Create an assistant.

        Create a new assistant.
        This method is available only with Enterprise plans.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_assistant')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_assistants(self,
                        *,
                        page_limit: int = None,
                        include_count: bool = None,
                        sort: str = None,
                        cursor: str = None,
                        include_audit: bool = None,
                        **kwargs) -> DetailedResponse:
        """
        List assistants.

        List the assistants associated with a Watson Assistant service instance.
        This method is available only with Enterprise plans.

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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_assistants')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def delete_assistant(self, assistant_id: str, **kwargs) -> DetailedResponse:
        """
        Delete assistant.

        Delete an assistant.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_assistant')
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
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Sessions
    #########################

    def create_session(self,
                       assistant_id: str,
                       *,
                       analytics: 'RequestAnalytics' = None,
                       **kwargs) -> DetailedResponse:
        """
        Create a session.

        Create a new session. A session is used to send user input to a skill and receive
        responses. It also maintains the state of the conversation. A session persists
        until it is deleted, or until it times out because of inactivity. (For more
        information, see the
        [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-assistant-settings).

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_session')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def delete_session(self, assistant_id: str, session_id: str,
                       **kwargs) -> DetailedResponse:
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
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_session')
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
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Message
    #########################

    def message(self,
                assistant_id: str,
                session_id: str,
                *,
                input: 'MessageInput' = None,
                context: 'MessageContext' = None,
                user_id: str = None,
                **kwargs) -> DetailedResponse:
        """
        Send user input to assistant (stateful).

        Send user input to an assistant and receive a response, with conversation state
        (including context data) stored by Watson Assistant for the duration of the
        session.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
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
        :rtype: DetailedResponse with `dict` result representing a `MessageResponse` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if not session_id:
            raise ValueError('session_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='message')
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

        path_param_keys = ['assistant_id', 'session_id']
        path_param_values = self.encode_path_vars(assistant_id, session_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/sessions/{session_id}/message'.format(
            **path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def message_stateless(self,
                          assistant_id: str,
                          *,
                          input: 'MessageInputStateless' = None,
                          context: 'MessageContextStateless' = None,
                          user_id: str = None,
                          **kwargs) -> DetailedResponse:
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
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param MessageInputStateless input: (optional) An input object that
               includes the input text.
        :param MessageContextStateless context: (optional) Context data for the
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
        :rtype: DetailedResponse with `dict` result representing a `MessageResponseStateless` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        if input is not None:
            input = convert_model(input)
        if context is not None:
            context = convert_model(context)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='message_stateless')
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

        path_param_keys = ['assistant_id']
        path_param_values = self.encode_path_vars(assistant_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v2/assistants/{assistant_id}/message'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Bulk classify
    #########################

    def bulk_classify(self, skill_id: str, input: List['BulkClassifyUtterance'],
                      **kwargs) -> DetailedResponse:
        """
        Identify intents and entities in multiple user utterances.

        Send multiple user inputs to a dialog skill in a single request and receive
        information about the intents and entities recognized in each input. This method
        is useful for testing and comparing the performance of different skills or skill
        versions.
        This method is available only with Enterprise with Data Isolation plans.

        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the Watson Assistant user interface, open the skill settings and click
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='bulk_classify')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Logs
    #########################

    def list_logs(self,
                  assistant_id: str,
                  *,
                  sort: str = None,
                  filter: str = None,
                  page_limit: int = None,
                  cursor: str = None,
                  **kwargs) -> DetailedResponse:
        """
        List log events for an assistant.

        List the events from the log of an assistant.
        This method requires Manager access, and is available only with Plus and
        Enterprise plans.
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
                To find the environment ID or assistant ID in the Watson Assistant user
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
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogCollection` object
        """

        if not assistant_id:
            raise ValueError('assistant_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_logs')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id: str, **kwargs) -> DetailedResponse:
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
        Watson
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_user_data')
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
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Environments
    #########################

    def list_environments(self,
                          assistant_id: str,
                          *,
                          page_limit: int = None,
                          include_count: bool = None,
                          sort: str = None,
                          cursor: str = None,
                          include_audit: bool = None,
                          **kwargs) -> DetailedResponse:
        """
        List environments.

        List the environments associated with an assistant.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_environments')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def get_environment(self,
                        assistant_id: str,
                        environment_id: str,
                        *,
                        include_audit: bool = None,
                        **kwargs) -> DetailedResponse:
        """
        Get environment.

        Get information about an environment. For more information about environments, see
        [Environments](https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-publish-overview#environments).
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the Watson Assistant user interface, open the
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_environment')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_environment(self,
                           assistant_id: str,
                           environment_id: str,
                           *,
                           name: str = None,
                           description: str = None,
                           session_timeout: int = None,
                           skill_references: List['EnvironmentSkill'] = None,
                           **kwargs) -> DetailedResponse:
        """
        Update environment.

        Update an environment with new or modified data. For more information about
        environments, see
        [Environments](https://cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-publish-overview#environments).
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str environment_id: Unique identifier of the environment. To find
               the environment ID in the Watson Assistant user interface, open the
               environment settings and click **API Details**. **Note:** Currently, the
               API does not support creating environments.
        :param str name: (optional) The name of the environment.
        :param str description: (optional) The description of the environment.
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
        if skill_references is not None:
            skill_references = [convert_model(x) for x in skill_references]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_environment')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Releases
    #########################

    def create_release(self,
                       assistant_id: str,
                       *,
                       description: str = None,
                       **kwargs) -> DetailedResponse:
        """
        Create release.

        Create a new release using the current content of the dialog and action skills in
        the draft environment. (In the Watson Assistant user interface, a release is
        called a *version*.)
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='create_release')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def list_releases(self,
                      assistant_id: str,
                      *,
                      page_limit: int = None,
                      include_count: bool = None,
                      sort: str = None,
                      cursor: str = None,
                      include_audit: bool = None,
                      **kwargs) -> DetailedResponse:
        """
        List releases.

        List the releases associated with an assistant. (In the Watson Assistant user
        interface, a release is called a *version*.)
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='list_releases')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def get_release(self,
                    assistant_id: str,
                    release: str,
                    *,
                    include_audit: bool = None,
                    **kwargs) -> DetailedResponse:
        """
        Get release.

        Get information about a release.
        Release data is not available until publishing of the release completes. If
        publishing is still in progress, you can continue to poll by calling the same
        request again and checking the value of the **status** property. When processing
        has completed, the request returns the release data.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_release')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def delete_release(self, assistant_id: str, release: str,
                       **kwargs) -> DetailedResponse:
        """
        Delete release.

        Delete a release. (In the Watson Assistant user interface, a release is called a
        *version*.)
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='delete_release')
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
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def deploy_release(self,
                       assistant_id: str,
                       release: str,
                       environment_id: str,
                       *,
                       include_audit: bool = None,
                       **kwargs) -> DetailedResponse:
        """
        Deploy release.

        Update the environment with the content of the release. All snapshots saved as
        part of the release become active in the environment.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='deploy_release')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    #########################
    # Skills
    #########################

    def get_skill(self, assistant_id: str, skill_id: str,
                  **kwargs) -> DetailedResponse:
        """
        Get skill.

        Get information about a skill.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the Watson Assistant user interface, open the skill settings and click
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='get_skill')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def update_skill(self,
                     assistant_id: str,
                     skill_id: str,
                     *,
                     name: str = None,
                     description: str = None,
                     workspace: dict = None,
                     dialog_settings: dict = None,
                     search_settings: 'SearchSettings' = None,
                     **kwargs) -> DetailedResponse:
        """
        Update skill.

        Update a skill with new or modified data.
          **Note:** The update is performed asynchronously; you can see the status of the
        update by calling the **Get skill** method and checking the value of the
        **status** property.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
               interface, open the assistant settings and scroll to the **Environments**
               section.
               **Note:** If you are using the classic Watson Assistant experience, always
               use the assistant ID. To find the assistant ID in the user interface, open
               the assistant settings and click API Details.
        :param str skill_id: Unique identifier of the skill. To find the skill ID
               in the Watson Assistant user interface, open the skill settings and click
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='update_skill')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def export_skills(self,
                      assistant_id: str,
                      *,
                      include_audit: bool = None,
                      **kwargs) -> DetailedResponse:
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
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='export_skills')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response

    def import_skills(self,
                      assistant_id: str,
                      assistant_skills: List['SkillImport'],
                      assistant_state: 'AssistantState',
                      *,
                      include_audit: bool = None,
                      **kwargs) -> DetailedResponse:
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
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='import_skills')
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
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data)

        response = self.send(request, **kwargs)
        return response

    def import_skills_status(self, assistant_id: str,
                             **kwargs) -> DetailedResponse:
        """
        Get status of skills import.

        Retrieve the status of an asynchronous import operation previously initiated by
        using the **Import skills** method.
        This method is available only with Enterprise plans.

        :param str assistant_id: The assistant ID or the environment ID of the
               environment where the assistant is deployed, depending on the type of
               request:
                - For message, session, and log requests, specify the environment ID of
               the environment where the assistant is deployed.
                - For all other requests, specify the assistant ID of the assistant.
                To find the environment ID or assistant ID in the Watson Assistant user
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
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V2',
                                      operation_id='import_skills_status')
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
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


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


##############################################################################
# Models
##############################################################################


class AgentAvailabilityMessage():
    """
    AgentAvailabilityMessage.

    :attr str message: (optional) The text of the message.
    """

    def __init__(self, *, message: str = None) -> None:
        """
        Initialize a AgentAvailabilityMessage object.

        :param str message: (optional) The text of the message.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AgentAvailabilityMessage':
        """Initialize a AgentAvailabilityMessage object from a json dictionary."""
        args = {}
        if 'message' in _dict:
            args['message'] = _dict.get('message')
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


class AssistantCollection():
    """
    AssistantCollection.

    :attr List[AssistantData] assistants: An array of objects describing the
          assistants associated with the instance.
    :attr Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(self, assistants: List['AssistantData'],
                 pagination: 'Pagination') -> None:
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
        if 'assistants' in _dict:
            args['assistants'] = [
                AssistantData.from_dict(v) for v in _dict.get('assistants')
            ]
        else:
            raise ValueError(
                'Required property \'assistants\' not present in AssistantCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination.from_dict(_dict.get('pagination'))
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


class AssistantData():
    """
    AssistantData.

    :attr str assistant_id: (optional) The unique identifier of the assistant.
    :attr str name: (optional) The name of the assistant. This string cannot contain
          carriage return, newline, or tab characters.
    :attr str description: (optional) The description of the assistant. This string
          cannot contain carriage return, newline, or tab characters.
    :attr str language: The language of the assistant.
    :attr List[AssistantSkill] assistant_skills: (optional) An array of skill
          references identifying the skills associated with the assistant.
    :attr List[EnvironmentReference] assistant_environments: (optional) An array of
          objects describing the environments defined for the assistant.
    """

    def __init__(
            self,
            language: str,
            *,
            assistant_id: str = None,
            name: str = None,
            description: str = None,
            assistant_skills: List['AssistantSkill'] = None,
            assistant_environments: List['EnvironmentReference'] = None
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
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in AssistantData JSON'
            )
        if 'assistant_skills' in _dict:
            args['assistant_skills'] = [
                AssistantSkill.from_dict(v)
                for v in _dict.get('assistant_skills')
            ]
        if 'assistant_environments' in _dict:
            args['assistant_environments'] = [
                EnvironmentReference.from_dict(v)
                for v in _dict.get('assistant_environments')
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


class AssistantSkill():
    """
    AssistantSkill.

    :attr str skill_id: The skill ID of the skill.
    :attr str type: (optional) The type of the skill.
    """

    def __init__(self, skill_id: str, *, type: str = None) -> None:
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
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in AssistantSkill JSON'
            )
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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


class AssistantState():
    """
    Status information about the skills for the assistant. Included in responses only if
    **status**=`Available`.

    :attr bool action_disabled: Whether the action skill is disabled in the draft
          environment.
    :attr bool dialog_disabled: Whether the dialog skill is disabled in the draft
          environment.
    """

    def __init__(self, action_disabled: bool, dialog_disabled: bool) -> None:
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
        if 'action_disabled' in _dict:
            args['action_disabled'] = _dict.get('action_disabled')
        else:
            raise ValueError(
                'Required property \'action_disabled\' not present in AssistantState JSON'
            )
        if 'dialog_disabled' in _dict:
            args['dialog_disabled'] = _dict.get('dialog_disabled')
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


class BaseEnvironmentOrchestration():
    """
    The search skill orchestration settings for the environment.

    :attr bool search_skill_fallback: (optional) Whether assistants deployed to the
          environment fall back to a search skill when responding to messages that do not
          match any intent. If no search skill is configured for the assistant, this
          property is ignored.
    """

    def __init__(self, *, search_skill_fallback: bool = None) -> None:
        """
        Initialize a BaseEnvironmentOrchestration object.

        :param bool search_skill_fallback: (optional) Whether assistants deployed
               to the environment fall back to a search skill when responding to messages
               that do not match any intent. If no search skill is configured for the
               assistant, this property is ignored.
        """
        self.search_skill_fallback = search_skill_fallback

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BaseEnvironmentOrchestration':
        """Initialize a BaseEnvironmentOrchestration object from a json dictionary."""
        args = {}
        if 'search_skill_fallback' in _dict:
            args['search_skill_fallback'] = _dict.get('search_skill_fallback')
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


class BaseEnvironmentReleaseReference():
    """
    An object describing the release that is currently deployed in the environment.

    :attr str release: (optional) The name of the deployed release.
    """

    def __init__(self, *, release: str = None) -> None:
        """
        Initialize a BaseEnvironmentReleaseReference object.

        :param str release: (optional) The name of the deployed release.
        """
        self.release = release

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BaseEnvironmentReleaseReference':
        """Initialize a BaseEnvironmentReleaseReference object from a json dictionary."""
        args = {}
        if 'release' in _dict:
            args['release'] = _dict.get('release')
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


class BulkClassifyOutput():
    """
    BulkClassifyOutput.

    :attr BulkClassifyUtterance input: (optional) The user input utterance to
          classify.
    :attr List[RuntimeEntity] entities: (optional) An array of entities identified
          in the utterance.
    :attr List[RuntimeIntent] intents: (optional) An array of intents recognized in
          the utterance.
    """

    def __init__(self,
                 *,
                 input: 'BulkClassifyUtterance' = None,
                 entities: List['RuntimeEntity'] = None,
                 intents: List['RuntimeIntent'] = None) -> None:
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
        if 'input' in _dict:
            args['input'] = BulkClassifyUtterance.from_dict(_dict.get('input'))
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity.from_dict(v) for v in _dict.get('entities')
            ]
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent.from_dict(v) for v in _dict.get('intents')
            ]
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


class BulkClassifyResponse():
    """
    BulkClassifyResponse.

    :attr List[BulkClassifyOutput] output: (optional) An array of objects that
          contain classification information for the submitted input utterances.
    """

    def __init__(self, *, output: List['BulkClassifyOutput'] = None) -> None:
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
        if 'output' in _dict:
            args['output'] = [
                BulkClassifyOutput.from_dict(v) for v in _dict.get('output')
            ]
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


class BulkClassifyUtterance():
    """
    The user input utterance to classify.

    :attr str text: The text of the input utterance.
    """

    def __init__(self, text: str) -> None:
        """
        Initialize a BulkClassifyUtterance object.

        :param str text: The text of the input utterance.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'BulkClassifyUtterance':
        """Initialize a BulkClassifyUtterance object from a json dictionary."""
        args = {}
        if 'text' in _dict:
            args['text'] = _dict.get('text')
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


class CaptureGroup():
    """
    CaptureGroup.

    :attr str group: A recognized capture group for the entity.
    :attr List[int] location: (optional) Zero-based character offsets that indicate
          where the entity value begins and ends in the input text.
    """

    def __init__(self, group: str, *, location: List[int] = None) -> None:
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
        if 'group' in _dict:
            args['group'] = _dict.get('group')
        else:
            raise ValueError(
                'Required property \'group\' not present in CaptureGroup JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
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


class ChannelTransferInfo():
    """
    Information used by an integration to transfer the conversation to a different
    channel.

    :attr ChannelTransferTarget target: An object specifying target channels
          available for the transfer. Each property of this object represents an available
          transfer target. Currently, the only supported property is **chat**,
          representing the web chat integration.
    """

    def __init__(self, target: 'ChannelTransferTarget') -> None:
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
        if 'target' in _dict:
            args['target'] = ChannelTransferTarget.from_dict(
                _dict.get('target'))
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


class ChannelTransferTarget():
    """
    An object specifying target channels available for the transfer. Each property of this
    object represents an available transfer target. Currently, the only supported property
    is **chat**, representing the web chat integration.

    :attr ChannelTransferTargetChat chat: (optional) Information for transferring to
          the web chat integration.
    """

    def __init__(self, *, chat: 'ChannelTransferTargetChat' = None) -> None:
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
        if 'chat' in _dict:
            args['chat'] = ChannelTransferTargetChat.from_dict(
                _dict.get('chat'))
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


class ChannelTransferTargetChat():
    """
    Information for transferring to the web chat integration.

    :attr str url: (optional) The URL of the target web chat.
    """

    def __init__(self, *, url: str = None) -> None:
        """
        Initialize a ChannelTransferTargetChat object.

        :param str url: (optional) The URL of the target web chat.
        """
        self.url = url

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ChannelTransferTargetChat':
        """Initialize a ChannelTransferTargetChat object from a json dictionary."""
        args = {}
        if 'url' in _dict:
            args['url'] = _dict.get('url')
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


class DialogLogMessage():
    """
    Dialog log message details.

    :attr str level: The severity of the log message.
    :attr str message: The text of the log message.
    :attr str code: A code that indicates the category to which the error message
          belongs.
    :attr LogMessageSource source: (optional) An object that identifies the dialog
          element that generated the error message.
    """

    def __init__(self,
                 level: str,
                 message: str,
                 code: str,
                 *,
                 source: 'LogMessageSource' = None) -> None:
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
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        else:
            raise ValueError(
                'Required property \'level\' not present in DialogLogMessage JSON'
            )
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        else:
            raise ValueError(
                'Required property \'message\' not present in DialogLogMessage JSON'
            )
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        else:
            raise ValueError(
                'Required property \'code\' not present in DialogLogMessage JSON'
            )
        if 'source' in _dict:
            args['source'] = LogMessageSource.from_dict(_dict.get('source'))
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


class DialogNodeAction():
    """
    DialogNodeAction.

    :attr str name: The name of the action.
    :attr str type: (optional) The type of action to invoke.
    :attr dict parameters: (optional) A map of key/value pairs to be provided to the
          action.
    :attr str result_variable: The location in the dialog context where the result
          of the action is stored.
    :attr str credentials: (optional) The name of the context variable that the
          client application will use to pass in credentials for the action.
    """

    def __init__(self,
                 name: str,
                 result_variable: str,
                 *,
                 type: str = None,
                 parameters: dict = None,
                 credentials: str = None) -> None:
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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in DialogNodeAction JSON'
            )
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'parameters' in _dict:
            args['parameters'] = _dict.get('parameters')
        if 'result_variable' in _dict:
            args['result_variable'] = _dict.get('result_variable')
        else:
            raise ValueError(
                'Required property \'result_variable\' not present in DialogNodeAction JSON'
            )
        if 'credentials' in _dict:
            args['credentials'] = _dict.get('credentials')
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


class DialogNodeOutputConnectToAgentTransferInfo():
    """
    Routing or other contextual information to be used by target service desk systems.

    :attr dict target: (optional)
    """

    def __init__(self, *, target: dict = None) -> None:
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
        if 'target' in _dict:
            args['target'] = _dict.get('target')
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


class DialogNodeOutputOptionsElement():
    """
    DialogNodeOutputOptionsElement.

    :attr str label: The user-facing label for the option.
    :attr DialogNodeOutputOptionsElementValue value: An object defining the message
          input to be sent to the assistant if the user selects the corresponding option.
    """

    def __init__(self, label: str,
                 value: 'DialogNodeOutputOptionsElementValue') -> None:
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
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogNodeOutputOptionsElement JSON'
            )
        if 'value' in _dict:
            args['value'] = DialogNodeOutputOptionsElementValue.from_dict(
                _dict.get('value'))
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


class DialogNodeOutputOptionsElementValue():
    """
    An object defining the message input to be sent to the assistant if the user selects
    the corresponding option.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    """

    def __init__(self, *, input: 'MessageInput' = None) -> None:
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
        if 'input' in _dict:
            args['input'] = MessageInput.from_dict(_dict.get('input'))
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


class DialogNodeVisited():
    """
    An objects containing detailed diagnostic information about a dialog node that was
    visited during processing of the input message.

    :attr str dialog_node: (optional) A dialog node that was visited during
          processing of the input message.
    :attr str title: (optional) The title of the dialog node.
    :attr str conditions: (optional) The conditions that trigger the dialog node.
    """

    def __init__(self,
                 *,
                 dialog_node: str = None,
                 title: str = None,
                 conditions: str = None) -> None:
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
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'conditions' in _dict:
            args['conditions'] = _dict.get('conditions')
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


class DialogSuggestion():
    """
    DialogSuggestion.

    :attr str label: The user-facing label for the suggestion. This label is taken
          from the **title** or **user_label** property of the corresponding dialog node,
          depending on the disambiguation options.
    :attr DialogSuggestionValue value: An object defining the message input to be
          sent to the assistant if the user selects the corresponding disambiguation
          option.
           **Note:** This entire message input object must be included in the request body
          of the next message sent to the assistant. Do not modify or remove any of the
          included properties.
    :attr dict output: (optional) The dialog output that will be returned from the
          Watson Assistant service if the user selects the corresponding option.
    """

    def __init__(self,
                 label: str,
                 value: 'DialogSuggestionValue',
                 *,
                 output: dict = None) -> None:
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
               the Watson Assistant service if the user selects the corresponding option.
        """
        self.label = label
        self.value = value
        self.output = output

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogSuggestion':
        """Initialize a DialogSuggestion object from a json dictionary."""
        args = {}
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogSuggestion JSON'
            )
        if 'value' in _dict:
            args['value'] = DialogSuggestionValue.from_dict(_dict.get('value'))
        else:
            raise ValueError(
                'Required property \'value\' not present in DialogSuggestion JSON'
            )
        if 'output' in _dict:
            args['output'] = _dict.get('output')
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


class DialogSuggestionValue():
    """
    An object defining the message input to be sent to the assistant if the user selects
    the corresponding disambiguation option.
     **Note:** This entire message input object must be included in the request body of
    the next message sent to the assistant. Do not modify or remove any of the included
    properties.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    """

    def __init__(self, *, input: 'MessageInput' = None) -> None:
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
        if 'input' in _dict:
            args['input'] = MessageInput.from_dict(_dict.get('input'))
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


class Environment():
    """
    Environment.

    :attr str name: (optional) The name of the environment.
    :attr str description: (optional) The description of the environment.
    :attr str assistant_id: (optional) The assistant ID of the assistant the
          environment is associated with.
    :attr str environment_id: (optional) The environment ID of the environment.
    :attr str environment: (optional) The type of the environment. All environments
          other than the `draft` and `live` environments have the type `staging`.
    :attr BaseEnvironmentReleaseReference release_reference: (optional) An object
          describing the release that is currently deployed in the environment.
    :attr BaseEnvironmentOrchestration orchestration: (optional) The search skill
          orchestration settings for the environment.
    :attr int session_timeout: The session inactivity timeout setting for the
          environment (in seconds).
    :attr List[IntegrationReference] integration_references: (optional) An array of
          objects describing the integrations that exist in the environment.
    :attr List[EnvironmentSkill] skill_references: An array of objects identifying
          the skills (such as action and dialog) that exist in the environment.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self,
                 session_timeout: int,
                 skill_references: List['EnvironmentSkill'],
                 *,
                 name: str = None,
                 description: str = None,
                 assistant_id: str = None,
                 environment_id: str = None,
                 environment: str = None,
                 release_reference: 'BaseEnvironmentReleaseReference' = None,
                 orchestration: 'BaseEnvironmentOrchestration' = None,
                 integration_references: List['IntegrationReference'] = None,
                 created: datetime = None,
                 updated: datetime = None) -> None:
        """
        Initialize a Environment object.

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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
        if 'release_reference' in _dict:
            args[
                'release_reference'] = BaseEnvironmentReleaseReference.from_dict(
                    _dict.get('release_reference'))
        if 'orchestration' in _dict:
            args['orchestration'] = BaseEnvironmentOrchestration.from_dict(
                _dict.get('orchestration'))
        if 'session_timeout' in _dict:
            args['session_timeout'] = _dict.get('session_timeout')
        else:
            raise ValueError(
                'Required property \'session_timeout\' not present in Environment JSON'
            )
        if 'integration_references' in _dict:
            args['integration_references'] = [
                IntegrationReference.from_dict(v)
                for v in _dict.get('integration_references')
            ]
        if 'skill_references' in _dict:
            args['skill_references'] = [
                EnvironmentSkill.from_dict(v)
                for v in _dict.get('skill_references')
            ]
        else:
            raise ValueError(
                'Required property \'skill_references\' not present in Environment JSON'
            )
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
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
        if hasattr(self, 'orchestration') and getattr(
                self, 'orchestration') is not None:
            if isinstance(getattr(self, 'orchestration'), dict):
                _dict['orchestration'] = getattr(self, 'orchestration')
            else:
                _dict['orchestration'] = getattr(self,
                                                 'orchestration').to_dict()
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


class EnvironmentCollection():
    """
    EnvironmentCollection.

    :attr List[Environment] environments: An array of objects describing the
          environments associated with an assistant.
    :attr Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(self, environments: List['Environment'],
                 pagination: 'Pagination') -> None:
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
        if 'environments' in _dict:
            args['environments'] = [
                Environment.from_dict(v) for v in _dict.get('environments')
            ]
        else:
            raise ValueError(
                'Required property \'environments\' not present in EnvironmentCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination.from_dict(_dict.get('pagination'))
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


class EnvironmentReference():
    """
    EnvironmentReference.

    :attr str name: (optional) The name of the environment.
    :attr str environment_id: (optional) The unique identifier of the environment.
    :attr str environment: (optional) The type of the environment. All environments
          other than the draft and live environments have the type `staging`.
    """

    def __init__(self,
                 *,
                 name: str = None,
                 environment_id: str = None,
                 environment: str = None) -> None:
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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'environment' in _dict:
            args['environment'] = _dict.get('environment')
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


class EnvironmentSkill():
    """
    EnvironmentSkill.

    :attr str skill_id: The skill ID of the skill.
    :attr str type: (optional) The type of the skill.
    :attr bool disabled: (optional) Whether the skill is disabled. A disabled skill
          in the draft environment does not handle any messages at run time, and it is not
          included in saved releases.
    :attr str snapshot: (optional) The name of the skill snapshot that is deployed
          to the environment (for example, `draft` or `1`).
    :attr str skill_reference: (optional) The type of skill identified by the skill
          reference. The possible values are `main skill` (for a dialog skill), `actions
          skill`, and `search skill`.
    """

    def __init__(self,
                 skill_id: str,
                 *,
                 type: str = None,
                 disabled: bool = None,
                 snapshot: str = None,
                 skill_reference: str = None) -> None:
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
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in EnvironmentSkill JSON'
            )
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        if 'snapshot' in _dict:
            args['snapshot'] = _dict.get('snapshot')
        if 'skill_reference' in _dict:
            args['skill_reference'] = _dict.get('skill_reference')
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


class IntegrationReference():
    """
    IntegrationReference.

    :attr str integration_id: (optional) The integration ID of the integration.
    :attr str type: (optional) The type of the integration.
    """

    def __init__(self, *, integration_id: str = None, type: str = None) -> None:
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
        if 'integration_id' in _dict:
            args['integration_id'] = _dict.get('integration_id')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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


class Log():
    """
    Log.

    :attr str log_id: A unique identifier for the logged event.
    :attr MessageRequest request: A stateful message request formatted for the
          Watson Assistant service.
    :attr MessageResponse response: A response from the Watson Assistant service.
    :attr str assistant_id: Unique identifier of the assistant.
    :attr str session_id: The ID of the session the message was part of.
    :attr str skill_id: The unique identifier of the skill that responded to the
          message.
    :attr str snapshot: The name of the snapshot (dialog skill version) that
          responded to the message (for example, `draft`).
    :attr str request_timestamp: The timestamp for receipt of the message.
    :attr str response_timestamp: The timestamp for the system response to the
          message.
    :attr str language: The language of the assistant to which the message request
          was made.
    :attr str customer_id: (optional) The customer ID specified for the message, if
          any.
    """

    def __init__(self,
                 log_id: str,
                 request: 'MessageRequest',
                 response: 'MessageResponse',
                 assistant_id: str,
                 session_id: str,
                 skill_id: str,
                 snapshot: str,
                 request_timestamp: str,
                 response_timestamp: str,
                 language: str,
                 *,
                 customer_id: str = None) -> None:
        """
        Initialize a Log object.

        :param str log_id: A unique identifier for the logged event.
        :param MessageRequest request: A stateful message request formatted for the
               Watson Assistant service.
        :param MessageResponse response: A response from the Watson Assistant
               service.
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
        if 'log_id' in _dict:
            args['log_id'] = _dict.get('log_id')
        else:
            raise ValueError(
                'Required property \'log_id\' not present in Log JSON')
        if 'request' in _dict:
            args['request'] = MessageRequest.from_dict(_dict.get('request'))
        else:
            raise ValueError(
                'Required property \'request\' not present in Log JSON')
        if 'response' in _dict:
            args['response'] = MessageResponse.from_dict(_dict.get('response'))
        else:
            raise ValueError(
                'Required property \'response\' not present in Log JSON')
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        else:
            raise ValueError(
                'Required property \'assistant_id\' not present in Log JSON')
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
        else:
            raise ValueError(
                'Required property \'session_id\' not present in Log JSON')
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in Log JSON')
        if 'snapshot' in _dict:
            args['snapshot'] = _dict.get('snapshot')
        else:
            raise ValueError(
                'Required property \'snapshot\' not present in Log JSON')
        if 'request_timestamp' in _dict:
            args['request_timestamp'] = _dict.get('request_timestamp')
        else:
            raise ValueError(
                'Required property \'request_timestamp\' not present in Log JSON'
            )
        if 'response_timestamp' in _dict:
            args['response_timestamp'] = _dict.get('response_timestamp')
        else:
            raise ValueError(
                'Required property \'response_timestamp\' not present in Log JSON'
            )
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Log JSON')
        if 'customer_id' in _dict:
            args['customer_id'] = _dict.get('customer_id')
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


class LogCollection():
    """
    LogCollection.

    :attr List[Log] logs: An array of objects describing log events.
    :attr LogPagination pagination: The pagination data for the returned objects.
          For more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(self, logs: List['Log'], pagination: 'LogPagination') -> None:
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
        if 'logs' in _dict:
            args['logs'] = [Log.from_dict(v) for v in _dict.get('logs')]
        else:
            raise ValueError(
                'Required property \'logs\' not present in LogCollection JSON')
        if 'pagination' in _dict:
            args['pagination'] = LogPagination.from_dict(
                _dict.get('pagination'))
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


class LogMessageSource():
    """
    An object that identifies the dialog element that generated the error message.

    """

    def __init__(self) -> None:
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
        msg = (
            "Cannot convert dictionary into an instance of base class 'LogMessageSource'. "
            + "The discriminator value should map to a valid subclass: {1}"
        ).format(", ".join([
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


class LogPagination():
    """
    The pagination data for the returned objects. For more information about using
    pagination, see [Pagination](#pagination).

    :attr str next_url: (optional) The URL that will return the next page of
          results, if any.
    :attr int matched: (optional) Reserved for future use.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self,
                 *,
                 next_url: str = None,
                 matched: int = None,
                 next_cursor: str = None) -> None:
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
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'matched' in _dict:
            args['matched'] = _dict.get('matched')
        if 'next_cursor' in _dict:
            args['next_cursor'] = _dict.get('next_cursor')
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


class MessageContext():
    """
    MessageContext.

    :attr MessageContextGlobal global_: (optional) Session context data that is
          shared by all skills used by the assistant.
    :attr MessageContextSkills skills: (optional) Context data specific to
          particular skills used by the assistant.
    :attr dict integrations: (optional) An object containing context data that is
          specific to particular integrations. For more information, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
    """

    def __init__(self,
                 *,
                 global_: 'MessageContextGlobal' = None,
                 skills: 'MessageContextSkills' = None,
                 integrations: dict = None) -> None:
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
        if 'global' in _dict:
            args['global_'] = MessageContextGlobal.from_dict(
                _dict.get('global'))
        if 'skills' in _dict:
            args['skills'] = MessageContextSkills.from_dict(_dict.get('skills'))
        if 'integrations' in _dict:
            args['integrations'] = _dict.get('integrations')
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


class MessageContextGlobal():
    """
    Session context data that is shared by all skills used by the assistant.

    :attr MessageContextGlobalSystem system: (optional) Built-in system properties
          that apply to all skills used by the assistant.
    :attr str session_id: (optional) The session ID.
    """

    def __init__(self,
                 *,
                 system: 'MessageContextGlobalSystem' = None,
                 session_id: str = None) -> None:
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
        if 'system' in _dict:
            args['system'] = MessageContextGlobalSystem.from_dict(
                _dict.get('system'))
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
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


class MessageContextGlobalStateless():
    """
    Session context data that is shared by all skills used by the assistant.

    :attr MessageContextGlobalSystem system: (optional) Built-in system properties
          that apply to all skills used by the assistant.
    :attr str session_id: (optional) The unique identifier of the session.
    """

    def __init__(self,
                 *,
                 system: 'MessageContextGlobalSystem' = None,
                 session_id: str = None) -> None:
        """
        Initialize a MessageContextGlobalStateless object.

        :param MessageContextGlobalSystem system: (optional) Built-in system
               properties that apply to all skills used by the assistant.
        :param str session_id: (optional) The unique identifier of the session.
        """
        self.system = system
        self.session_id = session_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextGlobalStateless':
        """Initialize a MessageContextGlobalStateless object from a json dictionary."""
        args = {}
        if 'system' in _dict:
            args['system'] = MessageContextGlobalSystem.from_dict(
                _dict.get('system'))
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextGlobalStateless object from a json dictionary."""
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
        """Return a `str` version of this MessageContextGlobalStateless object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextGlobalStateless') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextGlobalStateless') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextGlobalSystem():
    """
    Built-in system properties that apply to all skills used by the assistant.

    :attr str timezone: (optional) The user time zone. The assistant uses the time
          zone to correctly resolve relative time references.
    :attr str user_id: (optional) A string value that identifies the user who is
          interacting with the assistant. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property at the root of
          the message body. If **user_id** is specified in both locations in a message
          request, the value specified at the root is used.
    :attr int turn_count: (optional) A counter that is automatically incremented
          with each turn of the conversation. A value of 1 indicates that this is the the
          first turn of a new conversation, which can affect the behavior of some skills
          (for example, triggering the start node of a dialog).
    :attr str locale: (optional) The language code for localization in the user
          input. The specified locale overrides the default for the assistant, and is used
          for interpreting entity values in user input such as date values. For example,
          `04/03/2018` might be interpreted either as April 3 or March 4, depending on the
          locale.
           This property is included only if the new system entities are enabled for the
          skill.
    :attr str reference_time: (optional) The base time for interpreting any relative
          time mentions in the user input. The specified time overrides the current server
          time, and is used to calculate times mentioned in relative terms such as `now`
          or `tomorrow`. This can be useful for simulating past or future times for
          testing purposes, or when analyzing documents such as news articles.
          This value must be a UTC time value formatted according to ISO 8601 (for
          example, `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
          This property is included only if the new system entities are enabled for the
          skill.
    :attr str session_start_time: (optional) The time at which the session started.
          With the stateful `message` method, the start time is always present, and is set
          by the service based on the time the session was created. With the stateless
          `message` method, the start time is set by the service in the response to the
          first message, and should be returned as part of the context with each
          subsequent message in the session.
          This value is a UTC time value formatted according to ISO 8601 (for example,
          `2021-06-26T12:00:00Z` for noon UTC on 26 June 2021).
    :attr str state: (optional) An encoded string that represents the configuration
          state of the assistant at the beginning of the conversation. If you are using
          the stateless `message` method, save this value and then send it in the context
          of the subsequent message request to avoid disruptions if there are
          configuration changes during the conversation (such as a change to a skill the
          assistant uses).
    :attr bool skip_user_input: (optional) For internal use only.
    """

    def __init__(self,
                 *,
                 timezone: str = None,
                 user_id: str = None,
                 turn_count: int = None,
                 locale: str = None,
                 reference_time: str = None,
                 session_start_time: str = None,
                 state: str = None,
                 skip_user_input: bool = None) -> None:
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
        if 'timezone' in _dict:
            args['timezone'] = _dict.get('timezone')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        if 'turn_count' in _dict:
            args['turn_count'] = _dict.get('turn_count')
        if 'locale' in _dict:
            args['locale'] = _dict.get('locale')
        if 'reference_time' in _dict:
            args['reference_time'] = _dict.get('reference_time')
        if 'session_start_time' in _dict:
            args['session_start_time'] = _dict.get('session_start_time')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'skip_user_input' in _dict:
            args['skip_user_input'] = _dict.get('skip_user_input')
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


class MessageContextSkillAction():
    """
    Context variables that are used by the action skill.

    :attr dict user_defined: (optional) An object containing any arbitrary variables
          that can be read and written by a particular skill.
    :attr MessageContextSkillSystem system: (optional) System context data used by
          the skill.
    :attr dict action_variables: (optional) An object containing action variables.
          Action variables can be accessed only by steps in the same action, and do not
          persist after the action ends.
    :attr dict skill_variables: (optional) An object containing skill variables. (In
          the Watson Assistant user interface, skill variables are called _session
          variables_.) Skill variables can be accessed by any action and persist for the
          duration of the session.
    """

    def __init__(self,
                 *,
                 user_defined: dict = None,
                 system: 'MessageContextSkillSystem' = None,
                 action_variables: dict = None,
                 skill_variables: dict = None) -> None:
        """
        Initialize a MessageContextSkillAction object.

        :param dict user_defined: (optional) An object containing any arbitrary
               variables that can be read and written by a particular skill.
        :param MessageContextSkillSystem system: (optional) System context data
               used by the skill.
        :param dict action_variables: (optional) An object containing action
               variables. Action variables can be accessed only by steps in the same
               action, and do not persist after the action ends.
        :param dict skill_variables: (optional) An object containing skill
               variables. (In the Watson Assistant user interface, skill variables are
               called _session variables_.) Skill variables can be accessed by any action
               and persist for the duration of the session.
        """
        self.user_defined = user_defined
        self.system = system
        self.action_variables = action_variables
        self.skill_variables = skill_variables

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkillAction':
        """Initialize a MessageContextSkillAction object from a json dictionary."""
        args = {}
        if 'user_defined' in _dict:
            args['user_defined'] = _dict.get('user_defined')
        if 'system' in _dict:
            args['system'] = MessageContextSkillSystem.from_dict(
                _dict.get('system'))
        if 'action_variables' in _dict:
            args['action_variables'] = _dict.get('action_variables')
        if 'skill_variables' in _dict:
            args['skill_variables'] = _dict.get('skill_variables')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextSkillAction object from a json dictionary."""
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
        """Return a `str` version of this MessageContextSkillAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextSkillAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextSkillAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextSkillDialog():
    """
    Context variables that are used by the dialog skill.

    :attr dict user_defined: (optional) An object containing any arbitrary variables
          that can be read and written by a particular skill.
    :attr MessageContextSkillSystem system: (optional) System context data used by
          the skill.
    """

    def __init__(self,
                 *,
                 user_defined: dict = None,
                 system: 'MessageContextSkillSystem' = None) -> None:
        """
        Initialize a MessageContextSkillDialog object.

        :param dict user_defined: (optional) An object containing any arbitrary
               variables that can be read and written by a particular skill.
        :param MessageContextSkillSystem system: (optional) System context data
               used by the skill.
        """
        self.user_defined = user_defined
        self.system = system

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkillDialog':
        """Initialize a MessageContextSkillDialog object from a json dictionary."""
        args = {}
        if 'user_defined' in _dict:
            args['user_defined'] = _dict.get('user_defined')
        if 'system' in _dict:
            args['system'] = MessageContextSkillSystem.from_dict(
                _dict.get('system'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextSkillDialog object from a json dictionary."""
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
        """Return a `str` version of this MessageContextSkillDialog object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextSkillDialog') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextSkillDialog') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextSkillSystem():
    """
    System context data used by the skill.

    :attr str state: (optional) An encoded string that represents the current
          conversation state. By saving this value and then sending it in the context of a
          subsequent message request, you can return to an earlier point in the
          conversation. If you are using stateful sessions, you can also use a stored
          state value to restore a paused conversation whose session is expired.
    """

    # The set of defined properties for the class
    _properties = frozenset(['state'])

    def __init__(self, *, state: str = None, **kwargs) -> None:
        """
        Initialize a MessageContextSkillSystem object.

        :param str state: (optional) An encoded string that represents the current
               conversation state. By saving this value and then sending it in the context
               of a subsequent message request, you can return to an earlier point in the
               conversation. If you are using stateful sessions, you can also use a stored
               state value to restore a paused conversation whose session is expired.
        :param **kwargs: (optional) Any additional properties.
        """
        self.state = state
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkillSystem':
        """Initialize a MessageContextSkillSystem object from a json dictionary."""
        args = {}
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        args.update(
            {k: v for (k, v) in _dict.items() if k not in cls._properties})
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
        for _key in [
                k for k in vars(self).keys()
                if k not in MessageContextSkillSystem._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of MessageContextSkillSystem"""
        _dict = {}

        for _key in [
                k for k in vars(self).keys()
                if k not in MessageContextSkillSystem._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of MessageContextSkillSystem"""
        for _key in [
                k for k in vars(self).keys()
                if k not in MessageContextSkillSystem._properties
        ]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in MessageContextSkillSystem._properties:
                setattr(self, _key, _value)

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


class MessageContextSkills():
    """
    Context data specific to particular skills used by the assistant.

    :attr MessageContextSkillDialog main_skill: (optional) Context variables that
          are used by the dialog skill.
    :attr MessageContextSkillAction actions_skill: (optional) Context variables that
          are used by the action skill.
    """

    def __init__(self,
                 *,
                 main_skill: 'MessageContextSkillDialog' = None,
                 actions_skill: 'MessageContextSkillAction' = None) -> None:
        """
        Initialize a MessageContextSkills object.

        :param MessageContextSkillDialog main_skill: (optional) Context variables
               that are used by the dialog skill.
        :param MessageContextSkillAction actions_skill: (optional) Context
               variables that are used by the action skill.
        """
        self.main_skill = main_skill
        self.actions_skill = actions_skill

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextSkills':
        """Initialize a MessageContextSkills object from a json dictionary."""
        args = {}
        if 'main skill' in _dict:
            args['main_skill'] = MessageContextSkillDialog.from_dict(
                _dict.get('main skill'))
        if 'actions skill' in _dict:
            args['actions_skill'] = MessageContextSkillAction.from_dict(
                _dict.get('actions skill'))
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


class MessageContextStateless():
    """
    MessageContextStateless.

    :attr MessageContextGlobalStateless global_: (optional) Session context data
          that is shared by all skills used by the assistant.
    :attr MessageContextSkills skills: (optional) Context data specific to
          particular skills used by the assistant.
    :attr dict integrations: (optional) An object containing context data that is
          specific to particular integrations. For more information, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-integrations).
    """

    def __init__(self,
                 *,
                 global_: 'MessageContextGlobalStateless' = None,
                 skills: 'MessageContextSkills' = None,
                 integrations: dict = None) -> None:
        """
        Initialize a MessageContextStateless object.

        :param MessageContextGlobalStateless global_: (optional) Session context
               data that is shared by all skills used by the assistant.
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
    def from_dict(cls, _dict: Dict) -> 'MessageContextStateless':
        """Initialize a MessageContextStateless object from a json dictionary."""
        args = {}
        if 'global' in _dict:
            args['global_'] = MessageContextGlobalStateless.from_dict(
                _dict.get('global'))
        if 'skills' in _dict:
            args['skills'] = MessageContextSkills.from_dict(_dict.get('skills'))
        if 'integrations' in _dict:
            args['integrations'] = _dict.get('integrations')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextStateless object from a json dictionary."""
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
        """Return a `str` version of this MessageContextStateless object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextStateless') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextStateless') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInput():
    """
    An input object that includes the input text.

    :attr str message_type: (optional) The type of the message:
          - `text`: The user input is processed normally by the assistant.
          - `search`: Only search results are returned. (Any dialog or action skill is
          bypassed.)
          **Note:** A `search` message results in an error if no search skill is
          configured for the assistant.
    :attr str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :attr List[RuntimeIntent] intents: (optional) Intents to use when evaluating the
          user input. Include intents from the previous response to continue using those
          intents rather than trying to recognize intents in the new input.
    :attr List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :attr str suggestion_id: (optional) For internal use only.
    :attr List[MessageInputAttachment] attachments: (optional) An array of
          multimedia attachments to be sent with the message. Attachments are not
          processed by the assistant itself, but can be sent to external services by
          webhooks.
           **Note:** Attachments are not supported on IBM Cloud Pak for Data.
    :attr RequestAnalytics analytics: (optional) An optional object containing
          analytics data. Currently, this data is used only for events sent to the Segment
          extension.
    :attr MessageInputOptions options: (optional) Optional properties that control
          how the assistant responds.
    """

    def __init__(self,
                 *,
                 message_type: str = None,
                 text: str = None,
                 intents: List['RuntimeIntent'] = None,
                 entities: List['RuntimeEntity'] = None,
                 suggestion_id: str = None,
                 attachments: List['MessageInputAttachment'] = None,
                 analytics: 'RequestAnalytics' = None,
                 options: 'MessageInputOptions' = None) -> None:
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
        if 'message_type' in _dict:
            args['message_type'] = _dict.get('message_type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent.from_dict(v) for v in _dict.get('intents')
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity.from_dict(v) for v in _dict.get('entities')
            ]
        if 'suggestion_id' in _dict:
            args['suggestion_id'] = _dict.get('suggestion_id')
        if 'attachments' in _dict:
            args['attachments'] = [
                MessageInputAttachment.from_dict(v)
                for v in _dict.get('attachments')
            ]
        if 'analytics' in _dict:
            args['analytics'] = RequestAnalytics.from_dict(
                _dict.get('analytics'))
        if 'options' in _dict:
            args['options'] = MessageInputOptions.from_dict(
                _dict.get('options'))
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


class MessageInputAttachment():
    """
    A reference to a media file to be sent as an attachment with the message.

    :attr str url: The URL of the media file.
    :attr str media_type: (optional) The media content type (such as a MIME type) of
          the attachment.
    """

    def __init__(self, url: str, *, media_type: str = None) -> None:
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
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in MessageInputAttachment JSON'
            )
        if 'media_type' in _dict:
            args['media_type'] = _dict.get('media_type')
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


class MessageInputOptions():
    """
    Optional properties that control how the assistant responds.

    :attr bool restart: (optional) Whether to restart dialog processing at the root
          of the dialog, regardless of any previously visited nodes. **Note:** This does
          not affect `turn_count` or any other context variables.
    :attr bool alternate_intents: (optional) Whether to return more than one intent.
          Set to `true` to return all matching intents.
    :attr MessageInputOptionsSpelling spelling: (optional) Spelling correction
          options for the message. Any options specified on an individual message override
          the settings configured for the skill.
    :attr bool debug: (optional) Whether to return additional diagnostic
          information. Set to `true` to return additional information in the
          `output.debug` property. If you also specify **return_context**=`true`, the
          returned skill context includes the `system.state` property.
    :attr bool return_context: (optional) Whether to return session context with the
          response. If you specify `true`, the response includes the `context` property.
          If you also specify **debug**=`true`, the returned skill context includes the
          `system.state` property.
    :attr bool export: (optional) Whether to return session context, including full
          conversation state. If you specify `true`, the response includes the `context`
          property, and the skill context includes the `system.state` property.
          **Note:** If **export**=`true`, the context is returned regardless of the value
          of **return_context**.
    """

    def __init__(self,
                 *,
                 restart: bool = None,
                 alternate_intents: bool = None,
                 spelling: 'MessageInputOptionsSpelling' = None,
                 debug: bool = None,
                 return_context: bool = None,
                 export: bool = None) -> None:
        """
        Initialize a MessageInputOptions object.

        :param bool restart: (optional) Whether to restart dialog processing at the
               root of the dialog, regardless of any previously visited nodes. **Note:**
               This does not affect `turn_count` or any other context variables.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. Set to `true` to return all matching intents.
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
        self.spelling = spelling
        self.debug = debug
        self.return_context = return_context
        self.export = export

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInputOptions':
        """Initialize a MessageInputOptions object from a json dictionary."""
        args = {}
        if 'restart' in _dict:
            args['restart'] = _dict.get('restart')
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
        if 'spelling' in _dict:
            args['spelling'] = MessageInputOptionsSpelling.from_dict(
                _dict.get('spelling'))
        if 'debug' in _dict:
            args['debug'] = _dict.get('debug')
        if 'return_context' in _dict:
            args['return_context'] = _dict.get('return_context')
        if 'export' in _dict:
            args['export'] = _dict.get('export')
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


class MessageInputOptionsSpelling():
    """
    Spelling correction options for the message. Any options specified on an individual
    message override the settings configured for the skill.

    :attr bool suggestions: (optional) Whether to use spelling correction when
          processing the input. If spelling correction is used and **auto_correct** is
          `true`, any spelling corrections are automatically applied to the user input. If
          **auto_correct** is `false`, any suggested corrections are returned in the
          **output.spelling** property.
          This property overrides the value of the **spelling_suggestions** property in
          the workspace settings for the skill.
    :attr bool auto_correct: (optional) Whether to use autocorrection when
          processing the input. If this property is `true`, any corrections are
          automatically applied to the user input, and the original text is returned in
          the **output.spelling** property of the message response. This property
          overrides the value of the **spelling_auto_correct** property in the workspace
          settings for the skill.
    """

    def __init__(self,
                 *,
                 suggestions: bool = None,
                 auto_correct: bool = None) -> None:
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
        if 'suggestions' in _dict:
            args['suggestions'] = _dict.get('suggestions')
        if 'auto_correct' in _dict:
            args['auto_correct'] = _dict.get('auto_correct')
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


class MessageInputOptionsStateless():
    """
    Optional properties that control how the assistant responds.

    :attr bool restart: (optional) Whether to restart dialog processing at the root
          of the dialog, regardless of any previously visited nodes. **Note:** This does
          not affect `turn_count` or any other context variables.
    :attr bool alternate_intents: (optional) Whether to return more than one intent.
          Set to `true` to return all matching intents.
    :attr MessageInputOptionsSpelling spelling: (optional) Spelling correction
          options for the message. Any options specified on an individual message override
          the settings configured for the skill.
    :attr bool debug: (optional) Whether to return additional diagnostic
          information. Set to `true` to return additional information in the
          `output.debug` property.
    """

    def __init__(self,
                 *,
                 restart: bool = None,
                 alternate_intents: bool = None,
                 spelling: 'MessageInputOptionsSpelling' = None,
                 debug: bool = None) -> None:
        """
        Initialize a MessageInputOptionsStateless object.

        :param bool restart: (optional) Whether to restart dialog processing at the
               root of the dialog, regardless of any previously visited nodes. **Note:**
               This does not affect `turn_count` or any other context variables.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. Set to `true` to return all matching intents.
        :param MessageInputOptionsSpelling spelling: (optional) Spelling correction
               options for the message. Any options specified on an individual message
               override the settings configured for the skill.
        :param bool debug: (optional) Whether to return additional diagnostic
               information. Set to `true` to return additional information in the
               `output.debug` property.
        """
        self.restart = restart
        self.alternate_intents = alternate_intents
        self.spelling = spelling
        self.debug = debug

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageInputOptionsStateless':
        """Initialize a MessageInputOptionsStateless object from a json dictionary."""
        args = {}
        if 'restart' in _dict:
            args['restart'] = _dict.get('restart')
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
        if 'spelling' in _dict:
            args['spelling'] = MessageInputOptionsSpelling.from_dict(
                _dict.get('spelling'))
        if 'debug' in _dict:
            args['debug'] = _dict.get('debug')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInputOptionsStateless object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'restart') and self.restart is not None:
            _dict['restart'] = self.restart
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
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
        """Return a `str` version of this MessageInputOptionsStateless object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInputOptionsStateless') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInputOptionsStateless') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInputStateless():
    """
    An input object that includes the input text.

    :attr str message_type: (optional) The type of the message:
          - `text`: The user input is processed normally by the assistant.
          - `search`: Only search results are returned. (Any dialog or action skill is
          bypassed.)
          **Note:** A `search` message results in an error if no search skill is
          configured for the assistant.
    :attr str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :attr List[RuntimeIntent] intents: (optional) Intents to use when evaluating the
          user input. Include intents from the previous response to continue using those
          intents rather than trying to recognize intents in the new input.
    :attr List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :attr str suggestion_id: (optional) For internal use only.
    :attr List[MessageInputAttachment] attachments: (optional) An array of
          multimedia attachments to be sent with the message. Attachments are not
          processed by the assistant itself, but can be sent to external services by
          webhooks.
           **Note:** Attachments are not supported on IBM Cloud Pak for Data.
    :attr RequestAnalytics analytics: (optional) An optional object containing
          analytics data. Currently, this data is used only for events sent to the Segment
          extension.
    :attr MessageInputOptionsStateless options: (optional) Optional properties that
          control how the assistant responds.
    """

    def __init__(self,
                 *,
                 message_type: str = None,
                 text: str = None,
                 intents: List['RuntimeIntent'] = None,
                 entities: List['RuntimeEntity'] = None,
                 suggestion_id: str = None,
                 attachments: List['MessageInputAttachment'] = None,
                 analytics: 'RequestAnalytics' = None,
                 options: 'MessageInputOptionsStateless' = None) -> None:
        """
        Initialize a MessageInputStateless object.

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
        :param MessageInputOptionsStateless options: (optional) Optional properties
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
    def from_dict(cls, _dict: Dict) -> 'MessageInputStateless':
        """Initialize a MessageInputStateless object from a json dictionary."""
        args = {}
        if 'message_type' in _dict:
            args['message_type'] = _dict.get('message_type')
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent.from_dict(v) for v in _dict.get('intents')
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity.from_dict(v) for v in _dict.get('entities')
            ]
        if 'suggestion_id' in _dict:
            args['suggestion_id'] = _dict.get('suggestion_id')
        if 'attachments' in _dict:
            args['attachments'] = [
                MessageInputAttachment.from_dict(v)
                for v in _dict.get('attachments')
            ]
        if 'analytics' in _dict:
            args['analytics'] = RequestAnalytics.from_dict(
                _dict.get('analytics'))
        if 'options' in _dict:
            args['options'] = MessageInputOptionsStateless.from_dict(
                _dict.get('options'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInputStateless object from a json dictionary."""
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
        """Return a `str` version of this MessageInputStateless object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageInputStateless') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageInputStateless') -> bool:
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


class MessageOutput():
    """
    Assistant output to be rendered or processed by the client.

    :attr List[RuntimeResponseGeneric] generic: (optional) Output intended for any
          channel. It is the responsibility of the client application to implement the
          supported response types.
    :attr List[RuntimeIntent] intents: (optional) An array of intents recognized in
          the user input, sorted in descending order of confidence.
    :attr List[RuntimeEntity] entities: (optional) An array of entities identified
          in the user input.
    :attr List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    :attr MessageOutputDebug debug: (optional) Additional detailed information about
          a message response and how it was generated.
    :attr dict user_defined: (optional) An object containing any custom properties
          included in the response. This object includes any arbitrary properties defined
          in the dialog JSON editor as part of the dialog node output.
    :attr MessageOutputSpelling spelling: (optional) Properties describing any
          spelling corrections in the user input that was received.
    """

    def __init__(self,
                 *,
                 generic: List['RuntimeResponseGeneric'] = None,
                 intents: List['RuntimeIntent'] = None,
                 entities: List['RuntimeEntity'] = None,
                 actions: List['DialogNodeAction'] = None,
                 debug: 'MessageOutputDebug' = None,
                 user_defined: dict = None,
                 spelling: 'MessageOutputSpelling' = None) -> None:
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
        if 'generic' in _dict:
            args['generic'] = [
                RuntimeResponseGeneric.from_dict(v)
                for v in _dict.get('generic')
            ]
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent.from_dict(v) for v in _dict.get('intents')
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity.from_dict(v) for v in _dict.get('entities')
            ]
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction.from_dict(v) for v in _dict.get('actions')
            ]
        if 'debug' in _dict:
            args['debug'] = MessageOutputDebug.from_dict(_dict.get('debug'))
        if 'user_defined' in _dict:
            args['user_defined'] = _dict.get('user_defined')
        if 'spelling' in _dict:
            args['spelling'] = MessageOutputSpelling.from_dict(
                _dict.get('spelling'))
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


class MessageOutputDebug():
    """
    Additional detailed information about a message response and how it was generated.

    :attr List[DialogNodeVisited] nodes_visited: (optional) An array of objects
          containing detailed diagnostic information about dialog nodes that were visited
          during processing of the input message.
    :attr List[DialogLogMessage] log_messages: (optional) An array of up to 50
          messages logged with the request.
    :attr bool branch_exited: (optional) Assistant sets this to true when this
          message response concludes or interrupts a dialog.
    :attr str branch_exited_reason: (optional) When `branch_exited` is set to `true`
          by the assistant, the `branch_exited_reason` specifies whether the dialog
          completed by itself or got interrupted.
    :attr List[MessageOutputDebugTurnEvent] turn_events: (optional) An array of
          objects containing detailed diagnostic information about dialog nodes and
          actions that were visited during processing of the input message.
          This property is present only if the assistant has an action skill.
    """

    def __init__(
            self,
            *,
            nodes_visited: List['DialogNodeVisited'] = None,
            log_messages: List['DialogLogMessage'] = None,
            branch_exited: bool = None,
            branch_exited_reason: str = None,
            turn_events: List['MessageOutputDebugTurnEvent'] = None) -> None:
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
        if 'nodes_visited' in _dict:
            args['nodes_visited'] = [
                DialogNodeVisited.from_dict(v)
                for v in _dict.get('nodes_visited')
            ]
        if 'log_messages' in _dict:
            args['log_messages'] = [
                DialogLogMessage.from_dict(v) for v in _dict.get('log_messages')
            ]
        if 'branch_exited' in _dict:
            args['branch_exited'] = _dict.get('branch_exited')
        if 'branch_exited_reason' in _dict:
            args['branch_exited_reason'] = _dict.get('branch_exited_reason')
        if 'turn_events' in _dict:
            args['turn_events'] = [
                MessageOutputDebugTurnEvent.from_dict(v)
                for v in _dict.get('turn_events')
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


class MessageOutputDebugTurnEvent():
    """
    MessageOutputDebugTurnEvent.

    """

    def __init__(self) -> None:
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
        msg = (
            "Cannot convert dictionary into an instance of base class 'MessageOutputDebugTurnEvent'. "
            + "The discriminator value should map to a valid subclass: {1}"
        ).format(", ".join([
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


class MessageOutputSpelling():
    """
    Properties describing any spelling corrections in the user input that was received.

    :attr str text: (optional) The user input text that was used to generate the
          response. If spelling autocorrection is enabled, this text reflects any spelling
          corrections that were applied.
    :attr str original_text: (optional) The original user input text. This property
          is returned only if autocorrection is enabled and the user input was corrected.
    :attr str suggested_text: (optional) Any suggested corrections of the input
          text. This property is returned only if spelling correction is enabled and
          autocorrection is disabled.
    """

    def __init__(self,
                 *,
                 text: str = None,
                 original_text: str = None,
                 suggested_text: str = None) -> None:
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
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'original_text' in _dict:
            args['original_text'] = _dict.get('original_text')
        if 'suggested_text' in _dict:
            args['suggested_text'] = _dict.get('suggested_text')
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


class MessageRequest():
    """
    A stateful message request formatted for the Watson Assistant service.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    :attr MessageContext context: (optional) Context data for the conversation. You
          can use this property to set or modify context variables, which can also be
          accessed by dialog nodes. The context is stored by the assistant on a
          per-session basis.
          **Note:** The total size of the context data stored for a stateful session
          cannot exceed 100KB.
    :attr str user_id: (optional) A string value that identifies the user who is
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

    def __init__(self,
                 *,
                 input: 'MessageInput' = None,
                 context: 'MessageContext' = None,
                 user_id: str = None) -> None:
        """
        Initialize a MessageRequest object.

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
        """
        self.input = input
        self.context = context
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageRequest':
        """Initialize a MessageRequest object from a json dictionary."""
        args = {}
        if 'input' in _dict:
            args['input'] = MessageInput.from_dict(_dict.get('input'))
        if 'context' in _dict:
            args['context'] = MessageContext.from_dict(_dict.get('context'))
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageRequest object from a json dictionary."""
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
        """Return a `str` version of this MessageRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageResponse():
    """
    A response from the Watson Assistant service.

    :attr MessageOutput output: Assistant output to be rendered or processed by the
          client.
    :attr MessageContext context: (optional) Context data for the conversation. You
          can use this property to access context variables. The context is stored by the
          assistant on a per-session basis.
          **Note:** The context is included in message responses only if
          **return_context**=`true` in the message request. Full context is always
          included in logs.
    :attr str user_id: A string value that identifies the user who is interacting
          with the assistant. The client must provide a unique identifier for each
          individual end user who accesses the application. For user-based plans, this
          user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context.
    """

    def __init__(self,
                 output: 'MessageOutput',
                 user_id: str,
                 *,
                 context: 'MessageContext' = None) -> None:
        """
        Initialize a MessageResponse object.

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
        """
        self.output = output
        self.context = context
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageResponse':
        """Initialize a MessageResponse object from a json dictionary."""
        args = {}
        if 'output' in _dict:
            args['output'] = MessageOutput.from_dict(_dict.get('output'))
        else:
            raise ValueError(
                'Required property \'output\' not present in MessageResponse JSON'
            )
        if 'context' in _dict:
            args['context'] = MessageContext.from_dict(_dict.get('context'))
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        else:
            raise ValueError(
                'Required property \'user_id\' not present in MessageResponse JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageResponse object from a json dictionary."""
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
        """Return a `str` version of this MessageResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageResponseStateless():
    """
    A stateless response from the Watson Assistant service.

    :attr MessageOutput output: Assistant output to be rendered or processed by the
          client.
    :attr MessageContextStateless context: Context data for the conversation. You
          can use this property to access context variables. The context is not stored by
          the assistant; to maintain session state, include the context from the response
          in the next message.
    :attr str user_id: (optional) A string value that identifies the user who is
          interacting with the assistant. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.global.session_id**.
          **Note:** This property is the same as the **user_id** property in the global
          system context.
    """

    def __init__(self,
                 output: 'MessageOutput',
                 context: 'MessageContextStateless',
                 *,
                 user_id: str = None) -> None:
        """
        Initialize a MessageResponseStateless object.

        :param MessageOutput output: Assistant output to be rendered or processed
               by the client.
        :param MessageContextStateless context: Context data for the conversation.
               You can use this property to access context variables. The context is not
               stored by the assistant; to maintain session state, include the context
               from the response in the next message.
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
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageResponseStateless':
        """Initialize a MessageResponseStateless object from a json dictionary."""
        args = {}
        if 'output' in _dict:
            args['output'] = MessageOutput.from_dict(_dict.get('output'))
        else:
            raise ValueError(
                'Required property \'output\' not present in MessageResponseStateless JSON'
            )
        if 'context' in _dict:
            args['context'] = MessageContextStateless.from_dict(
                _dict.get('context'))
        else:
            raise ValueError(
                'Required property \'context\' not present in MessageResponseStateless JSON'
            )
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageResponseStateless object from a json dictionary."""
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
        """Return a `str` version of this MessageResponseStateless object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageResponseStateless') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageResponseStateless') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Pagination():
    """
    The pagination data for the returned objects. For more information about using
    pagination, see [Pagination](#pagination).

    :attr str refresh_url: The URL that will return the same page of results.
    :attr str next_url: (optional) The URL that will return the next page of
          results.
    :attr int total: (optional) The total number of objects that satisfy the
          request. This total includes all results, not just those included in the current
          page.
    :attr int matched: (optional) Reserved for future use.
    :attr str refresh_cursor: (optional) A token identifying the current page of
          results.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self,
                 refresh_url: str,
                 *,
                 next_url: str = None,
                 total: int = None,
                 matched: int = None,
                 refresh_cursor: str = None,
                 next_cursor: str = None) -> None:
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
        if 'refresh_url' in _dict:
            args['refresh_url'] = _dict.get('refresh_url')
        else:
            raise ValueError(
                'Required property \'refresh_url\' not present in Pagination JSON'
            )
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'total' in _dict:
            args['total'] = _dict.get('total')
        if 'matched' in _dict:
            args['matched'] = _dict.get('matched')
        if 'refresh_cursor' in _dict:
            args['refresh_cursor'] = _dict.get('refresh_cursor')
        if 'next_cursor' in _dict:
            args['next_cursor'] = _dict.get('next_cursor')
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


class Release():
    """
    Release.

    :attr str release: (optional) The name of the release. The name is the version
          number (an integer), returned as a string.
    :attr str description: (optional) The description of the release.
    :attr List[EnvironmentReference] environment_references: (optional) An array of
          objects describing the environments where this release has been deployed.
    :attr ReleaseContent content: (optional) An object identifying the versionable
          content objects (such as skill snapshots) that are included in the release.
    :attr str status: (optional) The current status of the release:
           - **Available**: The release is available for deployment.
           - **Failed**: An asynchronous publish operation has failed.
           - **Processing**: An asynchronous publish operation has not yet completed.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self,
                 *,
                 release: str = None,
                 description: str = None,
                 environment_references: List['EnvironmentReference'] = None,
                 content: 'ReleaseContent' = None,
                 status: str = None,
                 created: datetime = None,
                 updated: datetime = None) -> None:
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
        if 'release' in _dict:
            args['release'] = _dict.get('release')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'environment_references' in _dict:
            args['environment_references'] = [
                EnvironmentReference.from_dict(v)
                for v in _dict.get('environment_references')
            ]
        if 'content' in _dict:
            args['content'] = ReleaseContent.from_dict(_dict.get('content'))
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
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


class ReleaseCollection():
    """
    ReleaseCollection.

    :attr List[Release] releases: An array of objects describing the releases
          associated with an assistant.
    :attr Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(self, releases: List['Release'],
                 pagination: 'Pagination') -> None:
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
        if 'releases' in _dict:
            args['releases'] = [
                Release.from_dict(v) for v in _dict.get('releases')
            ]
        else:
            raise ValueError(
                'Required property \'releases\' not present in ReleaseCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination.from_dict(_dict.get('pagination'))
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


class ReleaseContent():
    """
    An object identifying the versionable content objects (such as skill snapshots) that
    are included in the release.

    :attr List[ReleaseSkill] skills: (optional) The skill snapshots that are
          included in the release.
    """

    def __init__(self, *, skills: List['ReleaseSkill'] = None) -> None:
        """
        Initialize a ReleaseContent object.

        """
        self.skills = skills

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ReleaseContent':
        """Initialize a ReleaseContent object from a json dictionary."""
        args = {}
        if 'skills' in _dict:
            args['skills'] = [
                ReleaseSkill.from_dict(v) for v in _dict.get('skills')
            ]
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


class ReleaseSkill():
    """
    ReleaseSkill.

    :attr str skill_id: The skill ID of the skill.
    :attr str type: (optional) The type of the skill.
    :attr str snapshot: (optional) The name of the skill snapshot that is saved as
          part of the release (for example, `draft` or `1`).
    """

    def __init__(self,
                 skill_id: str,
                 *,
                 type: str = None,
                 snapshot: str = None) -> None:
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
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        else:
            raise ValueError(
                'Required property \'skill_id\' not present in ReleaseSkill JSON'
            )
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'snapshot' in _dict:
            args['snapshot'] = _dict.get('snapshot')
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


class RequestAnalytics():
    """
    An optional object containing analytics data. Currently, this data is used only for
    events sent to the Segment extension.

    :attr str browser: (optional) The browser that was used to send the message that
          triggered the event.
    :attr str device: (optional) The type of device that was used to send the
          message that triggered the event.
    :attr str page_url: (optional) The URL of the web page that was used to send the
          message that triggered the event.
    """

    def __init__(self,
                 *,
                 browser: str = None,
                 device: str = None,
                 page_url: str = None) -> None:
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
        if 'browser' in _dict:
            args['browser'] = _dict.get('browser')
        if 'device' in _dict:
            args['device'] = _dict.get('device')
        if 'pageUrl' in _dict:
            args['page_url'] = _dict.get('pageUrl')
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


class ResponseGenericChannel():
    """
    ResponseGenericChannel.

    :attr str channel: (optional) A channel for which the response is intended.
    """

    def __init__(self, *, channel: str = None) -> None:
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
        if 'channel' in _dict:
            args['channel'] = _dict.get('channel')
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


class RuntimeEntity():
    """
    The entity value that was recognized in the user input.

    :attr str entity: An entity detected in the input.
    :attr List[int] location: (optional) An array of zero-based character offsets
          that indicate where the detected entity values begin and end in the input text.
    :attr str value: The term in the input text that was recognized as an entity
          value.
    :attr float confidence: (optional) A decimal percentage that represents Watson's
          confidence in the recognized entity.
    :attr List[CaptureGroup] groups: (optional) The recognized capture groups for
          the entity, as defined by the entity pattern.
    :attr RuntimeEntityInterpretation interpretation: (optional) An object
          containing detailed information about the entity recognized in the user input.
          This property is included only if the new system entities are enabled for the
          skill.
          For more information about how the new system entities are interpreted, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-beta-system-entities).
    :attr List[RuntimeEntityAlternative] alternatives: (optional) An array of
          possible alternative values that the user might have intended instead of the
          value returned in the **value** property. This property is returned only for
          `@sys-time` and `@sys-date` entities when the user's input is ambiguous.
          This property is included only if the new system entities are enabled for the
          skill.
    :attr RuntimeEntityRole role: (optional) An object describing the role played by
          a system entity that is specifies the beginning or end of a range recognized in
          the user input. This property is included only if the new system entities are
          enabled for the skill.
    :attr str skill: (optional) The skill that recognized the entity value.
          Currently, the only possible values are `main skill` for the dialog skill (if
          enabled) and `actions skill` for the action skill.
          This property is present only if the assistant has both a dialog skill and an
          action skill.
    """

    def __init__(self,
                 entity: str,
                 value: str,
                 *,
                 location: List[int] = None,
                 confidence: float = None,
                 groups: List['CaptureGroup'] = None,
                 interpretation: 'RuntimeEntityInterpretation' = None,
                 alternatives: List['RuntimeEntityAlternative'] = None,
                 role: 'RuntimeEntityRole' = None,
                 skill: str = None) -> None:
        """
        Initialize a RuntimeEntity object.

        :param str entity: An entity detected in the input.
        :param str value: The term in the input text that was recognized as an
               entity value.
        :param List[int] location: (optional) An array of zero-based character
               offsets that indicate where the detected entity values begin and end in the
               input text.
        :param float confidence: (optional) A decimal percentage that represents
               Watson's confidence in the recognized entity.
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
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in RuntimeEntity JSON'
            )
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in RuntimeEntity JSON')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'groups' in _dict:
            args['groups'] = [
                CaptureGroup.from_dict(v) for v in _dict.get('groups')
            ]
        if 'interpretation' in _dict:
            args['interpretation'] = RuntimeEntityInterpretation.from_dict(
                _dict.get('interpretation'))
        if 'alternatives' in _dict:
            args['alternatives'] = [
                RuntimeEntityAlternative.from_dict(v)
                for v in _dict.get('alternatives')
            ]
        if 'role' in _dict:
            args['role'] = RuntimeEntityRole.from_dict(_dict.get('role'))
        if 'skill' in _dict:
            args['skill'] = _dict.get('skill')
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


class RuntimeEntityAlternative():
    """
    An alternative value for the recognized entity.

    :attr str value: (optional) The entity value that was recognized in the user
          input.
    :attr float confidence: (optional) A decimal percentage that represents Watson's
          confidence in the recognized entity.
    """

    def __init__(self, *, value: str = None, confidence: float = None) -> None:
        """
        Initialize a RuntimeEntityAlternative object.

        :param str value: (optional) The entity value that was recognized in the
               user input.
        :param float confidence: (optional) A decimal percentage that represents
               Watson's confidence in the recognized entity.
        """
        self.value = value
        self.confidence = confidence

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntityAlternative':
        """Initialize a RuntimeEntityAlternative object from a json dictionary."""
        args = {}
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
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


class RuntimeEntityInterpretation():
    """
    RuntimeEntityInterpretation.

    :attr str calendar_type: (optional) The calendar used to represent a recognized
          date (for example, `Gregorian`).
    :attr str datetime_link: (optional) A unique identifier used to associate a
          recognized time and date. If the user input contains a date and time that are
          mentioned together (for example, `Today at 5`, the same **datetime_link** value
          is returned for both the `@sys-date` and `@sys-time` entities).
    :attr str festival: (optional) A locale-specific holiday name (such as
          `thanksgiving` or `christmas`). This property is included when a `@sys-date`
          entity is recognized based on a holiday name in the user input.
    :attr str granularity: (optional) The precision or duration of a time range
          specified by a recognized `@sys-time` or `@sys-date` entity.
    :attr str range_link: (optional) A unique identifier used to associate multiple
          recognized `@sys-date`, `@sys-time`, or `@sys-number` entities that are
          recognized as a range of values in the user's input (for example, `from July 4
          until July 14` or `from 20 to 25`).
    :attr str range_modifier: (optional) The word in the user input that indicates
          that a `sys-date` or `sys-time` entity is part of an implied range where only
          one date or time is specified (for example, `since` or `until`).
    :attr float relative_day: (optional) A recognized mention of a relative day,
          represented numerically as an offset from the current date (for example, `-1`
          for `yesterday` or `10` for `in ten days`).
    :attr float relative_month: (optional) A recognized mention of a relative month,
          represented numerically as an offset from the current month (for example, `1`
          for `next month` or `-3` for `three months ago`).
    :attr float relative_week: (optional) A recognized mention of a relative week,
          represented numerically as an offset from the current week (for example, `2` for
          `in two weeks` or `-1` for `last week).
    :attr float relative_weekend: (optional) A recognized mention of a relative date
          range for a weekend, represented numerically as an offset from the current
          weekend (for example, `0` for `this weekend` or `-1` for `last weekend`).
    :attr float relative_year: (optional) A recognized mention of a relative year,
          represented numerically as an offset from the current year (for example, `1` for
          `next year` or `-5` for `five years ago`).
    :attr float specific_day: (optional) A recognized mention of a specific date,
          represented numerically as the date within the month (for example, `30` for
          `June 30`.).
    :attr str specific_day_of_week: (optional) A recognized mention of a specific
          day of the week as a lowercase string (for example, `monday`).
    :attr float specific_month: (optional) A recognized mention of a specific month,
          represented numerically (for example, `7` for `July`).
    :attr float specific_quarter: (optional) A recognized mention of a specific
          quarter, represented numerically (for example, `3` for `the third quarter`).
    :attr float specific_year: (optional) A recognized mention of a specific year
          (for example, `2016`).
    :attr float numeric_value: (optional) A recognized numeric value, represented as
          an integer or double.
    :attr str subtype: (optional) The type of numeric value recognized in the user
          input (`integer` or `rational`).
    :attr str part_of_day: (optional) A recognized term for a time that was
          mentioned as a part of the day in the user's input (for example, `morning` or
          `afternoon`).
    :attr float relative_hour: (optional) A recognized mention of a relative hour,
          represented numerically as an offset from the current hour (for example, `3` for
          `in three hours` or `-1` for `an hour ago`).
    :attr float relative_minute: (optional) A recognized mention of a relative time,
          represented numerically as an offset in minutes from the current time (for
          example, `5` for `in five minutes` or `-15` for `fifteen minutes ago`).
    :attr float relative_second: (optional) A recognized mention of a relative time,
          represented numerically as an offset in seconds from the current time (for
          example, `10` for `in ten seconds` or `-30` for `thirty seconds ago`).
    :attr float specific_hour: (optional) A recognized specific hour mentioned as
          part of a time value (for example, `10` for `10:15 AM`.).
    :attr float specific_minute: (optional) A recognized specific minute mentioned
          as part of a time value (for example, `15` for `10:15 AM`.).
    :attr float specific_second: (optional) A recognized specific second mentioned
          as part of a time value (for example, `30` for `10:15:30 AM`.).
    :attr str timezone: (optional) A recognized time zone mentioned as part of a
          time value (for example, `EST`).
    """

    def __init__(self,
                 *,
                 calendar_type: str = None,
                 datetime_link: str = None,
                 festival: str = None,
                 granularity: str = None,
                 range_link: str = None,
                 range_modifier: str = None,
                 relative_day: float = None,
                 relative_month: float = None,
                 relative_week: float = None,
                 relative_weekend: float = None,
                 relative_year: float = None,
                 specific_day: float = None,
                 specific_day_of_week: str = None,
                 specific_month: float = None,
                 specific_quarter: float = None,
                 specific_year: float = None,
                 numeric_value: float = None,
                 subtype: str = None,
                 part_of_day: str = None,
                 relative_hour: float = None,
                 relative_minute: float = None,
                 relative_second: float = None,
                 specific_hour: float = None,
                 specific_minute: float = None,
                 specific_second: float = None,
                 timezone: str = None) -> None:
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
        if 'calendar_type' in _dict:
            args['calendar_type'] = _dict.get('calendar_type')
        if 'datetime_link' in _dict:
            args['datetime_link'] = _dict.get('datetime_link')
        if 'festival' in _dict:
            args['festival'] = _dict.get('festival')
        if 'granularity' in _dict:
            args['granularity'] = _dict.get('granularity')
        if 'range_link' in _dict:
            args['range_link'] = _dict.get('range_link')
        if 'range_modifier' in _dict:
            args['range_modifier'] = _dict.get('range_modifier')
        if 'relative_day' in _dict:
            args['relative_day'] = _dict.get('relative_day')
        if 'relative_month' in _dict:
            args['relative_month'] = _dict.get('relative_month')
        if 'relative_week' in _dict:
            args['relative_week'] = _dict.get('relative_week')
        if 'relative_weekend' in _dict:
            args['relative_weekend'] = _dict.get('relative_weekend')
        if 'relative_year' in _dict:
            args['relative_year'] = _dict.get('relative_year')
        if 'specific_day' in _dict:
            args['specific_day'] = _dict.get('specific_day')
        if 'specific_day_of_week' in _dict:
            args['specific_day_of_week'] = _dict.get('specific_day_of_week')
        if 'specific_month' in _dict:
            args['specific_month'] = _dict.get('specific_month')
        if 'specific_quarter' in _dict:
            args['specific_quarter'] = _dict.get('specific_quarter')
        if 'specific_year' in _dict:
            args['specific_year'] = _dict.get('specific_year')
        if 'numeric_value' in _dict:
            args['numeric_value'] = _dict.get('numeric_value')
        if 'subtype' in _dict:
            args['subtype'] = _dict.get('subtype')
        if 'part_of_day' in _dict:
            args['part_of_day'] = _dict.get('part_of_day')
        if 'relative_hour' in _dict:
            args['relative_hour'] = _dict.get('relative_hour')
        if 'relative_minute' in _dict:
            args['relative_minute'] = _dict.get('relative_minute')
        if 'relative_second' in _dict:
            args['relative_second'] = _dict.get('relative_second')
        if 'specific_hour' in _dict:
            args['specific_hour'] = _dict.get('specific_hour')
        if 'specific_minute' in _dict:
            args['specific_minute'] = _dict.get('specific_minute')
        if 'specific_second' in _dict:
            args['specific_second'] = _dict.get('specific_second')
        if 'timezone' in _dict:
            args['timezone'] = _dict.get('timezone')
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


class RuntimeEntityRole():
    """
    An object describing the role played by a system entity that is specifies the
    beginning or end of a range recognized in the user input. This property is included
    only if the new system entities are enabled for the skill.

    :attr str type: (optional) The relationship of the entity to the range.
    """

    def __init__(self, *, type: str = None) -> None:
        """
        Initialize a RuntimeEntityRole object.

        :param str type: (optional) The relationship of the entity to the range.
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'RuntimeEntityRole':
        """Initialize a RuntimeEntityRole object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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


class RuntimeIntent():
    """
    An intent identified in the user input.

    :attr str intent: The name of the recognized intent.
    :attr float confidence: (optional) A decimal percentage that represents Watson's
          confidence in the intent. If you are specifying an intent as part of a request,
          but you do not have a calculated confidence value, specify `1`.
    :attr str skill: (optional) The skill that identified the intent. Currently, the
          only possible values are `main skill` for the dialog skill (if enabled) and
          `actions skill` for the action skill.
          This property is present only if the assistant has both a dialog skill and an
          action skill.
    """

    def __init__(self,
                 intent: str,
                 *,
                 confidence: float = None,
                 skill: str = None) -> None:
        """
        Initialize a RuntimeIntent object.

        :param str intent: The name of the recognized intent.
        :param float confidence: (optional) A decimal percentage that represents
               Watson's confidence in the intent. If you are specifying an intent as part
               of a request, but you do not have a calculated confidence value, specify
               `1`.
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
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in RuntimeIntent JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'skill' in _dict:
            args['skill'] = _dict.get('skill')
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


class RuntimeResponseGeneric():
    """
    RuntimeResponseGeneric.

    """

    def __init__(self) -> None:
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
        msg = (
            "Cannot convert dictionary into an instance of base class 'RuntimeResponseGeneric'. "
            + "The discriminator value should map to a valid subclass: {1}"
        ).format(", ".join([
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


class SearchResult():
    """
    SearchResult.

    :attr str id: The unique identifier of the document in the Discovery service
          collection.
          This property is included in responses from search skills, which are available
          only to Plus or Enterprise plan users.
    :attr SearchResultMetadata result_metadata: An object containing search result
          metadata from the Discovery service.
    :attr str body: (optional) A description of the search result. This is taken
          from an abstract, summary, or highlight field in the Discovery service response,
          as specified in the search skill configuration.
    :attr str title: (optional) The title of the search result. This is taken from a
          title or name field in the Discovery service response, as specified in the
          search skill configuration.
    :attr str url: (optional) The URL of the original data object in its native data
          source.
    :attr SearchResultHighlight highlight: (optional) An object containing segments
          of text from search results with query-matching text highlighted using HTML
          `<em>` tags.
    :attr List[SearchResultAnswer] answers: (optional) An array specifying segments
          of text within the result that were identified as direct answers to the search
          query. Currently, only the single answer with the highest confidence (if any) is
          returned.
          **Notes:**
           - Answer finding is available only if the search skill is connected to a
          Discovery v2 service instance.
           - Answer finding is not supported on IBM Cloud Pak for Data.
    """

    def __init__(self,
                 id: str,
                 result_metadata: 'SearchResultMetadata',
                 *,
                 body: str = None,
                 title: str = None,
                 url: str = None,
                 highlight: 'SearchResultHighlight' = None,
                 answers: List['SearchResultAnswer'] = None) -> None:
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
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError(
                'Required property \'id\' not present in SearchResult JSON')
        if 'result_metadata' in _dict:
            args['result_metadata'] = SearchResultMetadata.from_dict(
                _dict.get('result_metadata'))
        else:
            raise ValueError(
                'Required property \'result_metadata\' not present in SearchResult JSON'
            )
        if 'body' in _dict:
            args['body'] = _dict.get('body')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        if 'highlight' in _dict:
            args['highlight'] = SearchResultHighlight.from_dict(
                _dict.get('highlight'))
        if 'answers' in _dict:
            args['answers'] = [
                SearchResultAnswer.from_dict(v) for v in _dict.get('answers')
            ]
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


class SearchResultAnswer():
    """
    An object specifing a segment of text that was identified as a direct answer to the
    search query.

    :attr str text: The text of the answer.
    :attr float confidence: The confidence score for the answer, as returned by the
          Discovery service.
    """

    def __init__(self, text: str, confidence: float) -> None:
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
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in SearchResultAnswer JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
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


class SearchResultHighlight():
    """
    An object containing segments of text from search results with query-matching text
    highlighted using HTML `<em>` tags.

    :attr List[str] body: (optional) An array of strings containing segments taken
          from body text in the search results, with query-matching substrings
          highlighted.
    :attr List[str] title: (optional) An array of strings containing segments taken
          from title text in the search results, with query-matching substrings
          highlighted.
    :attr List[str] url: (optional) An array of strings containing segments taken
          from URLs in the search results, with query-matching substrings highlighted.
    """

    # The set of defined properties for the class
    _properties = frozenset(['body', 'title', 'url'])

    def __init__(self,
                 *,
                 body: List[str] = None,
                 title: List[str] = None,
                 url: List[str] = None,
                 **kwargs) -> None:
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
        :param **kwargs: (optional) Any additional properties.
        """
        self.body = body
        self.title = title
        self.url = url
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchResultHighlight':
        """Initialize a SearchResultHighlight object from a json dictionary."""
        args = {}
        if 'body' in _dict:
            args['body'] = _dict.get('body')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        args.update(
            {k: v for (k, v) in _dict.items() if k not in cls._properties})
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
        for _key in [
                k for k in vars(self).keys()
                if k not in SearchResultHighlight._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return a dictionary of arbitrary properties from this instance of SearchResultHighlight"""
        _dict = {}

        for _key in [
                k for k in vars(self).keys()
                if k not in SearchResultHighlight._properties
        ]:
            _dict[_key] = getattr(self, _key)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of arbitrary properties to this instance of SearchResultHighlight"""
        for _key in [
                k for k in vars(self).keys()
                if k not in SearchResultHighlight._properties
        ]:
            delattr(self, _key)

        for _key, _value in _dict.items():
            if _key not in SearchResultHighlight._properties:
                setattr(self, _key, _value)

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


class SearchResultMetadata():
    """
    An object containing search result metadata from the Discovery service.

    :attr float confidence: (optional) The confidence score for the given result, as
          returned by the Discovery service.
    :attr float score: (optional) An unbounded measure of the relevance of a
          particular result, dependent on the query and matching document. A higher score
          indicates a greater match to the query parameters.
    """

    def __init__(self,
                 *,
                 confidence: float = None,
                 score: float = None) -> None:
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
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'score' in _dict:
            args['score'] = _dict.get('score')
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


class SearchSettings():
    """
    An object describing the search skill configuration.

    :attr SearchSettingsDiscovery discovery: Configuration settings for the Watson
          Discovery service instance used by the search integration.
    :attr SearchSettingsMessages messages: The messages included with responses from
          the search integration.
    :attr SearchSettingsSchemaMapping schema_mapping: The mapping between fields in
          the Watson Discovery collection and properties in the search response.
    """

    def __init__(self, discovery: 'SearchSettingsDiscovery',
                 messages: 'SearchSettingsMessages',
                 schema_mapping: 'SearchSettingsSchemaMapping') -> None:
        """
        Initialize a SearchSettings object.

        :param SearchSettingsDiscovery discovery: Configuration settings for the
               Watson Discovery service instance used by the search integration.
        :param SearchSettingsMessages messages: The messages included with
               responses from the search integration.
        :param SearchSettingsSchemaMapping schema_mapping: The mapping between
               fields in the Watson Discovery collection and properties in the search
               response.
        """
        self.discovery = discovery
        self.messages = messages
        self.schema_mapping = schema_mapping

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SearchSettings':
        """Initialize a SearchSettings object from a json dictionary."""
        args = {}
        if 'discovery' in _dict:
            args['discovery'] = SearchSettingsDiscovery.from_dict(
                _dict.get('discovery'))
        else:
            raise ValueError(
                'Required property \'discovery\' not present in SearchSettings JSON'
            )
        if 'messages' in _dict:
            args['messages'] = SearchSettingsMessages.from_dict(
                _dict.get('messages'))
        else:
            raise ValueError(
                'Required property \'messages\' not present in SearchSettings JSON'
            )
        if 'schema_mapping' in _dict:
            args['schema_mapping'] = SearchSettingsSchemaMapping.from_dict(
                _dict.get('schema_mapping'))
        else:
            raise ValueError(
                'Required property \'schema_mapping\' not present in SearchSettings JSON'
            )
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


class SearchSettingsDiscovery():
    """
    Configuration settings for the Watson Discovery service instance used by the search
    integration.

    :attr str instance_id: The ID for the Watson Discovery service instance.
    :attr str project_id: The ID for the Watson Discovery project.
    :attr str url: The URL for the Watson Discovery service instance.
    :attr int max_primary_results: (optional) The maximum number of primary results
          to include in the response.
    :attr int max_total_results: (optional) The maximum total number of primary and
          additional results to include in the response.
    :attr float confidence_threshold: (optional) The minimum confidence threshold
          for included results. Any results with a confidence below this threshold will be
          discarded.
    :attr bool highlight: (optional) Whether to include the most relevant passages
          of text in the **highlight** property of each result.
    :attr bool find_answers: (optional) Whether to use the answer finding feature to
          emphasize answers within highlighted passages. This property is ignored if
          **highlight**=`false`.
          **Notes:**
           - Answer finding is available only if the search skill is connected to a
          Discovery v2 service instance.
           - Answer finding is not supported on IBM Cloud Pak for Data.
    :attr SearchSettingsDiscoveryAuthentication authentication: Authentication
          information for the Watson Discovery service. For more information, see the
          [Watson Discovery
          documentation](https://cloud.ibm.com/apidocs/discovery-data#authentication).
           **Note:** You must specify either **basic** or **bearer**, but not both.
    """

    def __init__(self,
                 instance_id: str,
                 project_id: str,
                 url: str,
                 authentication: 'SearchSettingsDiscoveryAuthentication',
                 *,
                 max_primary_results: int = None,
                 max_total_results: int = None,
                 confidence_threshold: float = None,
                 highlight: bool = None,
                 find_answers: bool = None) -> None:
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
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        else:
            raise ValueError(
                'Required property \'instance_id\' not present in SearchSettingsDiscovery JSON'
            )
        if 'project_id' in _dict:
            args['project_id'] = _dict.get('project_id')
        else:
            raise ValueError(
                'Required property \'project_id\' not present in SearchSettingsDiscovery JSON'
            )
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsDiscovery JSON'
            )
        if 'max_primary_results' in _dict:
            args['max_primary_results'] = _dict.get('max_primary_results')
        if 'max_total_results' in _dict:
            args['max_total_results'] = _dict.get('max_total_results')
        if 'confidence_threshold' in _dict:
            args['confidence_threshold'] = _dict.get('confidence_threshold')
        if 'highlight' in _dict:
            args['highlight'] = _dict.get('highlight')
        if 'find_answers' in _dict:
            args['find_answers'] = _dict.get('find_answers')
        if 'authentication' in _dict:
            args[
                'authentication'] = SearchSettingsDiscoveryAuthentication.from_dict(
                    _dict.get('authentication'))
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


class SearchSettingsDiscoveryAuthentication():
    """
    Authentication information for the Watson Discovery service. For more information, see
    the [Watson Discovery
    documentation](https://cloud.ibm.com/apidocs/discovery-data#authentication).
     **Note:** You must specify either **basic** or **bearer**, but not both.

    :attr str basic: (optional) The HTTP basic authentication credentials for Watson
          Discovery. Specify your Watson Discovery API key in the format
          `apikey:{apikey}`.
    :attr str bearer: (optional) The authentication bearer token for Watson
          Discovery.
    """

    def __init__(self, *, basic: str = None, bearer: str = None) -> None:
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
        if 'basic' in _dict:
            args['basic'] = _dict.get('basic')
        if 'bearer' in _dict:
            args['bearer'] = _dict.get('bearer')
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


class SearchSettingsMessages():
    """
    The messages included with responses from the search integration.

    :attr str success: The message to include in the response to a successful query.
    :attr str error: The message to include in the response when the query
          encounters an error.
    :attr str no_result: The message to include in the response when there is no
          result from the query.
    """

    def __init__(self, success: str, error: str, no_result: str) -> None:
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
        if 'success' in _dict:
            args['success'] = _dict.get('success')
        else:
            raise ValueError(
                'Required property \'success\' not present in SearchSettingsMessages JSON'
            )
        if 'error' in _dict:
            args['error'] = _dict.get('error')
        else:
            raise ValueError(
                'Required property \'error\' not present in SearchSettingsMessages JSON'
            )
        if 'no_result' in _dict:
            args['no_result'] = _dict.get('no_result')
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


class SearchSettingsSchemaMapping():
    """
    The mapping between fields in the Watson Discovery collection and properties in the
    search response.

    :attr str url: The field in the collection to map to the **url** property of the
          response.
    :attr str body: The field in the collection to map to the **body** property in
          the response.
    :attr str title: The field in the collection to map to the **title** property
          for the schema.
    """

    def __init__(self, url: str, body: str, title: str) -> None:
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
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in SearchSettingsSchemaMapping JSON'
            )
        if 'body' in _dict:
            args['body'] = _dict.get('body')
        else:
            raise ValueError(
                'Required property \'body\' not present in SearchSettingsSchemaMapping JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
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


class SearchSkillWarning():
    """
    A warning describing an error in the search skill configuration.

    :attr str code: (optional) The error code.
    :attr str path: (optional) The location of the error in the search skill
          configuration object.
    :attr str message: (optional) The error message.
    """

    def __init__(self,
                 *,
                 code: str = None,
                 path: str = None,
                 message: str = None) -> None:
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
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'path' in _dict:
            args['path'] = _dict.get('path')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
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


class SessionResponse():
    """
    SessionResponse.

    :attr str session_id: The session ID.
    """

    def __init__(self, session_id: str) -> None:
        """
        Initialize a SessionResponse object.

        :param str session_id: The session ID.
        """
        self.session_id = session_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SessionResponse':
        """Initialize a SessionResponse object from a json dictionary."""
        args = {}
        if 'session_id' in _dict:
            args['session_id'] = _dict.get('session_id')
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


class Skill():
    """
    Skill.

    :attr str name: (optional) The name of the skill. This string cannot contain
          carriage return, newline, or tab characters.
    :attr str description: (optional) The description of the skill. This string
          cannot contain carriage return, newline, or tab characters.
    :attr dict workspace: (optional) An object containing the conversational content
          of an action or dialog skill.
    :attr str skill_id: (optional) The skill ID of the skill.
    :attr str status: (optional) The current status of the skill:
           - **Available**: The skill is available and ready to process messages.
           - **Failed**: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - **Non Existent**: The skill does not exist.
           - **Processing**: An asynchronous operation has not yet completed.
           - **Training**: The skill is training based on new data.
    :attr List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :attr str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :attr dict dialog_settings: (optional) For internal use only.
    :attr str assistant_id: (optional) The unique identifier of the assistant the
          skill is associated with.
    :attr str workspace_id: (optional) The unique identifier of the workspace that
          contains the skill content. Included only for action and dialog skills.
    :attr str environment_id: (optional) The unique identifier of the environment
          where the skill is defined. For action and dialog skills, this is always the
          draft environment.
    :attr bool valid: (optional) Whether the skill is structurally valid.
    :attr str next_snapshot_version: (optional) The name that will be given to the
          next snapshot that is created for the skill. A snapshot of each versionable
          skill is saved for each new release of an assistant.
    :attr SearchSettings search_settings: (optional) An object describing the search
          skill configuration.
    :attr List[SearchSkillWarning] warnings: (optional) An array of warnings
          describing errors with the search skill configuration. Included only for search
          skills.
    :attr str language: The language of the skill.
    :attr str type: The type of skill.
    """

    def __init__(self,
                 language: str,
                 type: str,
                 *,
                 name: str = None,
                 description: str = None,
                 workspace: dict = None,
                 skill_id: str = None,
                 status: str = None,
                 status_errors: List['StatusError'] = None,
                 status_description: str = None,
                 dialog_settings: dict = None,
                 assistant_id: str = None,
                 workspace_id: str = None,
                 environment_id: str = None,
                 valid: bool = None,
                 next_snapshot_version: str = None,
                 search_settings: 'SearchSettings' = None,
                 warnings: List['SearchSkillWarning'] = None) -> None:
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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'workspace' in _dict:
            args['workspace'] = _dict.get('workspace')
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_errors' in _dict:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in _dict.get('status_errors')
            ]
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        if 'dialog_settings' in _dict:
            args['dialog_settings'] = _dict.get('dialog_settings')
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'valid' in _dict:
            args['valid'] = _dict.get('valid')
        if 'next_snapshot_version' in _dict:
            args['next_snapshot_version'] = _dict.get('next_snapshot_version')
        if 'search_settings' in _dict:
            args['search_settings'] = SearchSettings.from_dict(
                _dict.get('search_settings'))
        if 'warnings' in _dict:
            args['warnings'] = [
                SearchSkillWarning.from_dict(v) for v in _dict.get('warnings')
            ]
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Skill JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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


class SkillImport():
    """
    SkillImport.

    :attr str name: (optional) The name of the skill. This string cannot contain
          carriage return, newline, or tab characters.
    :attr str description: (optional) The description of the skill. This string
          cannot contain carriage return, newline, or tab characters.
    :attr dict workspace: (optional) An object containing the conversational content
          of an action or dialog skill.
    :attr str skill_id: (optional) The skill ID of the skill.
    :attr str status: (optional) The current status of the skill:
           - **Available**: The skill is available and ready to process messages.
           - **Failed**: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - **Non Existent**: The skill does not exist.
           - **Processing**: An asynchronous operation has not yet completed.
           - **Training**: The skill is training based on new data.
    :attr List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    :attr str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :attr dict dialog_settings: (optional) For internal use only.
    :attr str assistant_id: (optional) The unique identifier of the assistant the
          skill is associated with.
    :attr str workspace_id: (optional) The unique identifier of the workspace that
          contains the skill content. Included only for action and dialog skills.
    :attr str environment_id: (optional) The unique identifier of the environment
          where the skill is defined. For action and dialog skills, this is always the
          draft environment.
    :attr bool valid: (optional) Whether the skill is structurally valid.
    :attr str next_snapshot_version: (optional) The name that will be given to the
          next snapshot that is created for the skill. A snapshot of each versionable
          skill is saved for each new release of an assistant.
    :attr SearchSettings search_settings: (optional) An object describing the search
          skill configuration.
    :attr List[SearchSkillWarning] warnings: (optional) An array of warnings
          describing errors with the search skill configuration. Included only for search
          skills.
    :attr str language: The language of the skill.
    :attr str type: The type of skill.
    """

    def __init__(self,
                 language: str,
                 type: str,
                 *,
                 name: str = None,
                 description: str = None,
                 workspace: dict = None,
                 skill_id: str = None,
                 status: str = None,
                 status_errors: List['StatusError'] = None,
                 status_description: str = None,
                 dialog_settings: dict = None,
                 assistant_id: str = None,
                 workspace_id: str = None,
                 environment_id: str = None,
                 valid: bool = None,
                 next_snapshot_version: str = None,
                 search_settings: 'SearchSettings' = None,
                 warnings: List['SearchSkillWarning'] = None) -> None:
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
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'workspace' in _dict:
            args['workspace'] = _dict.get('workspace')
        if 'skill_id' in _dict:
            args['skill_id'] = _dict.get('skill_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_errors' in _dict:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in _dict.get('status_errors')
            ]
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        if 'dialog_settings' in _dict:
            args['dialog_settings'] = _dict.get('dialog_settings')
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        if 'environment_id' in _dict:
            args['environment_id'] = _dict.get('environment_id')
        if 'valid' in _dict:
            args['valid'] = _dict.get('valid')
        if 'next_snapshot_version' in _dict:
            args['next_snapshot_version'] = _dict.get('next_snapshot_version')
        if 'search_settings' in _dict:
            args['search_settings'] = SearchSettings.from_dict(
                _dict.get('search_settings'))
        if 'warnings' in _dict:
            args['warnings'] = [
                SearchSkillWarning.from_dict(v) for v in _dict.get('warnings')
            ]
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in SkillImport JSON'
            )
        if 'type' in _dict:
            args['type'] = _dict.get('type')
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
        SEARCH = 'search'


class SkillsAsyncRequestStatus():
    """
    SkillsAsyncRequestStatus.

    :attr str assistant_id: (optional) The assistant ID of the assistant.
    :attr str status: (optional) The current status of the asynchronous operation:
           - `Available`: An asynchronous export is available.
           - `Completed`: An asynchronous import operation has completed successfully.
           - `Failed`: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - `Processing`: An asynchronous operation has not yet completed.
    :attr str status_description: (optional) The description of the failed
          asynchronous operation. Included only if **status**=`Failed`.
    :attr List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail. Included only if
          **status**=`Failed`.
    """

    def __init__(self,
                 *,
                 assistant_id: str = None,
                 status: str = None,
                 status_description: str = None,
                 status_errors: List['StatusError'] = None) -> None:
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
        if 'assistant_id' in _dict:
            args['assistant_id'] = _dict.get('assistant_id')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'status_description' in _dict:
            args['status_description'] = _dict.get('status_description')
        if 'status_errors' in _dict:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in _dict.get('status_errors')
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


class SkillsExport():
    """
    SkillsExport.

    :attr List[Skill] assistant_skills: An array of objects describing the skills
          for the assistant. Included in responses only if **status**=`Available`.
    :attr AssistantState assistant_state: Status information about the skills for
          the assistant. Included in responses only if **status**=`Available`.
    """

    def __init__(self, assistant_skills: List['Skill'],
                 assistant_state: 'AssistantState') -> None:
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
        if 'assistant_skills' in _dict:
            args['assistant_skills'] = [
                Skill.from_dict(v) for v in _dict.get('assistant_skills')
            ]
        else:
            raise ValueError(
                'Required property \'assistant_skills\' not present in SkillsExport JSON'
            )
        if 'assistant_state' in _dict:
            args['assistant_state'] = AssistantState.from_dict(
                _dict.get('assistant_state'))
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


class StatusError():
    """
    An object describing an error that occurred during processing of an asynchronous
    operation.

    :attr str message: (optional) The text of the error message.
    """

    def __init__(self, *, message: str = None) -> None:
        """
        Initialize a StatusError object.

        :param str message: (optional) The text of the error message.
        """
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'StatusError':
        """Initialize a StatusError object from a json dictionary."""
        args = {}
        if 'message' in _dict:
            args['message'] = _dict.get('message')
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


class TurnEventActionSource():
    """
    TurnEventActionSource.

    :attr str type: (optional) The type of turn event.
    :attr str action: (optional) An action that was visited during processing of the
          message.
    :attr str action_title: (optional) The title of the action.
    :attr str condition: (optional) The condition that triggered the dialog node.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 action: str = None,
                 action_title: str = None,
                 condition: str = None) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        if 'action_title' in _dict:
            args['action_title'] = _dict.get('action_title')
        if 'condition' in _dict:
            args['condition'] = _dict.get('condition')
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


class TurnEventCalloutCallout():
    """
    TurnEventCalloutCallout.

    :attr str type: (optional) The type of callout. Currently, the only supported
          value is `integration_interaction` (for calls to extensions).
    :attr dict internal: (optional) For internal use only.
    :attr str result_variable: (optional) The name of the variable where the callout
          result is stored.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 internal: dict = None,
                 result_variable: str = None) -> None:
        """
        Initialize a TurnEventCalloutCallout object.

        :param str type: (optional) The type of callout. Currently, the only
               supported value is `integration_interaction` (for calls to extensions).
        :param dict internal: (optional) For internal use only.
        :param str result_variable: (optional) The name of the variable where the
               callout result is stored.
        """
        self.type = type
        self.internal = internal
        self.result_variable = result_variable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'TurnEventCalloutCallout':
        """Initialize a TurnEventCalloutCallout object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'internal' in _dict:
            args['internal'] = _dict.get('internal')
        if 'result_variable' in _dict:
            args['result_variable'] = _dict.get('result_variable')
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


class TurnEventCalloutError():
    """
    TurnEventCalloutError.

    :attr str message: (optional) Any error message returned by a failed call to an
          external service.
    """

    def __init__(self, *, message: str = None) -> None:
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
        if 'message' in _dict:
            args['message'] = _dict.get('message')
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


class TurnEventNodeSource():
    """
    TurnEventNodeSource.

    :attr str type: (optional) The type of turn event.
    :attr str dialog_node: (optional) A dialog node that was visited during
          processing of the input message.
    :attr str title: (optional) The title of the dialog node.
    :attr str condition: (optional) The condition that triggered the dialog node.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 dialog_node: str = None,
                 title: str = None,
                 condition: str = None) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'condition' in _dict:
            args['condition'] = _dict.get('condition')
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


class TurnEventSearchError():
    """
    TurnEventSearchError.

    :attr str message: (optional) Any error message returned by a failed call to a
          search skill.
    """

    def __init__(self, *, message: str = None) -> None:
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
        if 'message' in _dict:
            args['message'] = _dict.get('message')
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


class LogMessageSourceAction(LogMessageSource):
    """
    An object that identifies the dialog element that generated the error message.

    :attr str type: A string that indicates the type of dialog element that
          generated the error message.
    :attr str action: The unique identifier of the action that generated the error
          message.
    """

    def __init__(self, type: str, action: str) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceAction JSON'
            )
        if 'action' in _dict:
            args['action'] = _dict.get('action')
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

    :attr str type: A string that indicates the type of dialog element that
          generated the error message.
    :attr str dialog_node: The unique identifier of the dialog node that generated
          the error message.
    """

    def __init__(self, type: str, dialog_node: str) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceDialogNode JSON'
            )
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
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

    :attr str type: A string that indicates the type of dialog element that
          generated the error message.
    :attr str action: The unique identifier of the action that generated the error
          message.
    :attr str step: (optional) The unique identifier of the step that generated the
          error message.
    :attr str handler: The unique identifier of the handler that generated the error
          message.
    """

    def __init__(self,
                 type: str,
                 action: str,
                 handler: str,
                 *,
                 step: str = None) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceHandler JSON'
            )
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError(
                'Required property \'action\' not present in LogMessageSourceHandler JSON'
            )
        if 'step' in _dict:
            args['step'] = _dict.get('step')
        if 'handler' in _dict:
            args['handler'] = _dict.get('handler')
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

    :attr str type: A string that indicates the type of dialog element that
          generated the error message.
    :attr str action: The unique identifier of the action that generated the error
          message.
    :attr str step: The unique identifier of the step that generated the error
          message.
    """

    def __init__(self, type: str, action: str, step: str) -> None:
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
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in LogMessageSourceStep JSON'
            )
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError(
                'Required property \'action\' not present in LogMessageSourceStep JSON'
            )
        if 'step' in _dict:
            args['step'] = _dict.get('step')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr str action_start_time: (optional) The time when the action started
          processing the message.
    :attr str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :attr str reason: (optional) The reason the action finished processing.
    :attr dict action_variables: (optional) The state of all action variables at the
          time the action finished.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 action_start_time: str = None,
                 condition_type: str = None,
                 reason: str = None,
                 action_variables: dict = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'action_start_time' in _dict:
            args['action_start_time'] = _dict.get('action_start_time')
        if 'condition_type' in _dict:
            args['condition_type'] = _dict.get('condition_type')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'action_variables' in _dict:
            args['action_variables'] = _dict.get('action_variables')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr str action_start_time: (optional) The time when the action started
          processing the message.
    :attr str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :attr str reason: (optional) The reason the action was visited.
    :attr str result_variable: (optional) The variable where the result of the call
          to the action is stored. Included only if **reason**=`subaction_return`.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 action_start_time: str = None,
                 condition_type: str = None,
                 reason: str = None,
                 result_variable: str = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'action_start_time' in _dict:
            args['action_start_time'] = _dict.get('action_start_time')
        if 'condition_type' in _dict:
            args['condition_type'] = _dict.get('condition_type')
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
        if 'result_variable' in _dict:
            args['result_variable'] = _dict.get('result_variable')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr TurnEventCalloutCallout callout: (optional)
    :attr TurnEventCalloutError error: (optional)
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 callout: 'TurnEventCalloutCallout' = None,
                 error: 'TurnEventCalloutError' = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'callout' in _dict:
            args['callout'] = TurnEventCalloutCallout.from_dict(
                _dict.get('callout'))
        if 'error' in _dict:
            args['error'] = TurnEventCalloutError.from_dict(_dict.get('error'))
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr str action_start_time: (optional) The time when the action started
          processing the message.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 action_start_time: str = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'action_start_time' in _dict:
            args['action_start_time'] = _dict.get('action_start_time')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventNodeSource source: (optional)
    :attr str reason: (optional) The reason the dialog node was visited.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventNodeSource' = None,
                 reason: str = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventNodeSource.from_dict(_dict.get('source'))
        if 'reason' in _dict:
            args['reason'] = _dict.get('reason')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr TurnEventSearchError error: (optional)
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 error: 'TurnEventSearchError' = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'error' in _dict:
            args['error'] = TurnEventSearchError.from_dict(_dict.get('error'))
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :attr str action_start_time: (optional) The time when the action started
          processing the message.
    :attr bool prompted: (optional) Whether the step was answered in response to a
          prompt from the assistant. If this property is `false`, the user provided the
          answer without visiting the step.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 condition_type: str = None,
                 action_start_time: str = None,
                 prompted: bool = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'condition_type' in _dict:
            args['condition_type'] = _dict.get('condition_type')
        if 'action_start_time' in _dict:
            args['action_start_time'] = _dict.get('action_start_time')
        if 'prompted' in _dict:
            args['prompted'] = _dict.get('prompted')
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

    :attr str event: (optional) The type of turn event.
    :attr TurnEventActionSource source: (optional)
    :attr str condition_type: (optional) The type of condition (if any) that is
          defined for the action.
    :attr str action_start_time: (optional) The time when the action started
          processing the message.
    :attr bool has_question: (optional) Whether the step collects a customer
          response.
    """

    def __init__(self,
                 *,
                 event: str = None,
                 source: 'TurnEventActionSource' = None,
                 condition_type: str = None,
                 action_start_time: str = None,
                 has_question: bool = None) -> None:
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
        if 'event' in _dict:
            args['event'] = _dict.get('event')
        if 'source' in _dict:
            args['source'] = TurnEventActionSource.from_dict(
                _dict.get('source'))
        if 'condition_type' in _dict:
            args['condition_type'] = _dict.get('condition_type')
        if 'action_start_time' in _dict:
            args['action_start_time'] = _dict.get('action_start_time')
        if 'has_question' in _dict:
            args['has_question'] = _dict.get('has_question')
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


class RuntimeResponseGenericRuntimeResponseTypeAudio(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeAudio.

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str source: The `https:` URL of the audio clip.
    :attr str title: (optional) The title or introductory text to show before the
          response.
    :attr str description: (optional) The description to show with the the response.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :attr dict channel_options: (optional) For internal use only.
    :attr str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the audio player cannot be seen.
    """

    def __init__(self,
                 response_type: str,
                 source: str,
                 *,
                 title: str = None,
                 description: str = None,
                 channels: List['ResponseGenericChannel'] = None,
                 channel_options: dict = None,
                 alt_text: str = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeAudio JSON'
            )
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeAudio JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
            ]
        if 'channel_options' in _dict:
            args['channel_options'] = _dict.get('channel_options')
        if 'alt_text' in _dict:
            args['alt_text'] = _dict.get('alt_text')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
           **Note:** The `channel_transfer` response type is not supported on IBM Cloud
          Pak for Data.
    :attr str message_to_user: The message to display to the user when initiating a
          channel transfer.
    :attr ChannelTransferInfo transfer_info: Information used by an integration to
          transfer the conversation to a different channel.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 message_to_user: str,
                 transfer_info: 'ChannelTransferInfo',
                 *,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if 'message_to_user' in _dict:
            args['message_to_user'] = _dict.get('message_to_user')
        else:
            raise ValueError(
                'Required property \'message_to_user\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if 'transfer_info' in _dict:
            args['transfer_info'] = ChannelTransferInfo.from_dict(
                _dict.get('transfer_info'))
        else:
            raise ValueError(
                'Required property \'transfer_info\' not present in RuntimeResponseGenericRuntimeResponseTypeChannelTransfer JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str message_to_human_agent: (optional) A message to be sent to the human
          agent who will be taking over the conversation.
    :attr AgentAvailabilityMessage agent_available: (optional) An optional message
          to be displayed to the user to indicate that the conversation will be
          transferred to the next available agent.
    :attr AgentAvailabilityMessage agent_unavailable: (optional) An optional message
          to be displayed to the user to indicate that no online agent is available to
          take over the conversation.
    :attr DialogNodeOutputConnectToAgentTransferInfo transfer_info: (optional)
          Routing or other contextual information to be used by target service desk
          systems.
    :attr str topic: (optional) A label identifying the topic of the conversation,
          derived from the **title** property of the relevant node or the **topic**
          property of the dialog node response.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(
            self,
            response_type: str,
            *,
            message_to_human_agent: str = None,
            agent_available: 'AgentAvailabilityMessage' = None,
            agent_unavailable: 'AgentAvailabilityMessage' = None,
            transfer_info: 'DialogNodeOutputConnectToAgentTransferInfo' = None,
            topic: str = None,
            channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeConnectToAgent JSON'
            )
        if 'message_to_human_agent' in _dict:
            args['message_to_human_agent'] = _dict.get('message_to_human_agent')
        if 'agent_available' in _dict:
            args['agent_available'] = AgentAvailabilityMessage.from_dict(
                _dict.get('agent_available'))
        if 'agent_unavailable' in _dict:
            args['agent_unavailable'] = AgentAvailabilityMessage.from_dict(
                _dict.get('agent_unavailable'))
        if 'transfer_info' in _dict:
            args[
                'transfer_info'] = DialogNodeOutputConnectToAgentTransferInfo.from_dict(
                    _dict.get('transfer_info'))
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    """

    def __init__(self, response_type: str) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str source: The `https:` URL of the embeddable content.
    :attr str title: (optional) The title or introductory text to show before the
          response.
    :attr str description: (optional) The description to show with the the response.
    :attr str image_url: (optional) The URL of an image that shows a preview of the
          embedded content.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 source: str,
                 *,
                 title: str = None,
                 description: str = None,
                 image_url: str = None,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeIframe JSON'
            )
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeIframe JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'image_url' in _dict:
            args['image_url'] = _dict.get('image_url')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str source: The `https:` URL of the image.
    :attr str title: (optional) The title to show before the response.
    :attr str description: (optional) The description to show with the the response.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :attr str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the image cannot be seen.
    """

    def __init__(self,
                 response_type: str,
                 source: str,
                 *,
                 title: str = None,
                 description: str = None,
                 channels: List['ResponseGenericChannel'] = None,
                 alt_text: str = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeImage JSON'
            )
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeImage JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
            ]
        if 'alt_text' in _dict:
            args['alt_text'] = _dict.get('alt_text')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str title: The title or introductory text to show before the response.
    :attr str description: (optional) The description to show with the the response.
    :attr str preference: (optional) The preferred type of control to display.
    :attr List[DialogNodeOutputOptionsElement] options: An array of objects
          describing the options from which the user can choose.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 title: str,
                 options: List['DialogNodeOutputOptionsElement'],
                 *,
                 description: str = None,
                 preference: str = None,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError(
                'Required property \'title\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        if 'options' in _dict:
            args['options'] = [
                DialogNodeOutputOptionsElement.from_dict(v)
                for v in _dict.get('options')
            ]
        else:
            raise ValueError(
                'Required property \'options\' not present in RuntimeResponseGenericRuntimeResponseTypeOption JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr int time: How long to pause, in milliseconds.
    :attr bool typing: (optional) Whether to send a "user is typing" event during
          the pause.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 time: int,
                 *,
                 typing: bool = None,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypePause JSON'
            )
        if 'time' in _dict:
            args['time'] = _dict.get('time')
        else:
            raise ValueError(
                'Required property \'time\' not present in RuntimeResponseGenericRuntimeResponseTypePause JSON'
            )
        if 'typing' in _dict:
            args['typing'] = _dict.get('typing')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str header: The title or introductory text to show before the response.
          This text is defined in the search skill configuration.
    :attr List[SearchResult] primary_results: An array of objects that contains the
          search results to be displayed in the initial response to the user.
    :attr List[SearchResult] additional_results: An array of objects that contains
          additional search results that can be displayed to the user upon request.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 header: str,
                 primary_results: List['SearchResult'],
                 additional_results: List['SearchResult'],
                 *,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if 'header' in _dict:
            args['header'] = _dict.get('header')
        else:
            raise ValueError(
                'Required property \'header\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if 'primary_results' in _dict:
            args['primary_results'] = [
                SearchResult.from_dict(v) for v in _dict.get('primary_results')
            ]
        else:
            raise ValueError(
                'Required property \'primary_results\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if 'additional_results' in _dict:
            args['additional_results'] = [
                SearchResult.from_dict(v)
                for v in _dict.get('additional_results')
            ]
        else:
            raise ValueError(
                'Required property \'additional_results\' not present in RuntimeResponseGenericRuntimeResponseTypeSearch JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str title: The title or introductory text to show before the response.
    :attr List[DialogSuggestion] suggestions: An array of objects describing the
          possible matching dialog nodes from which the user can choose.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 title: str,
                 suggestions: List['DialogSuggestion'],
                 *,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        else:
            raise ValueError(
                'Required property \'title\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if 'suggestions' in _dict:
            args['suggestions'] = [
                DialogSuggestion.from_dict(v) for v in _dict.get('suggestions')
            ]
        else:
            raise ValueError(
                'Required property \'suggestions\' not present in RuntimeResponseGenericRuntimeResponseTypeSuggestion JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str text: The text of the response.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 text: str,
                 *,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeText JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in RuntimeResponseGenericRuntimeResponseTypeText JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr dict user_defined: An object containing any properties for the
          user-defined response type.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    """

    def __init__(self,
                 response_type: str,
                 user_defined: dict,
                 *,
                 channels: List['ResponseGenericChannel'] = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeUserDefined JSON'
            )
        if 'user_defined' in _dict:
            args['user_defined'] = _dict.get('user_defined')
        else:
            raise ValueError(
                'Required property \'user_defined\' not present in RuntimeResponseGenericRuntimeResponseTypeUserDefined JSON'
            )
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
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

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :attr str source: The `https:` URL of the video.
    :attr str title: (optional) The title or introductory text to show before the
          response.
    :attr str description: (optional) The description to show with the the response.
    :attr List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended. If **channels** is
          present, the response is intended for a built-in integration and should not be
          handled by an API client.
    :attr dict channel_options: (optional) For internal use only.
    :attr str alt_text: (optional) Descriptive text that can be used for screen
          readers or other situations where the video cannot be seen.
    """

    def __init__(self,
                 response_type: str,
                 source: str,
                 *,
                 title: str = None,
                 description: str = None,
                 channels: List['ResponseGenericChannel'] = None,
                 channel_options: dict = None,
                 alt_text: str = None) -> None:
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
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGenericRuntimeResponseTypeVideo JSON'
            )
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        else:
            raise ValueError(
                'Required property \'source\' not present in RuntimeResponseGenericRuntimeResponseTypeVideo JSON'
            )
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'channels' in _dict:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v)
                for v in _dict.get('channels')
            ]
        if 'channel_options' in _dict:
            args['channel_options'] = _dict.get('channel_options')
        if 'alt_text' in _dict:
            args['alt_text'] = _dict.get('alt_text')
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
