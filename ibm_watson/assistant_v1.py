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
The IBM Watson&trade; Assistant service combines machine learning, natural language
understanding, and an integrated dialog editor to create conversation flows between your
apps and your users.
The Assistant v1 API provides authoring methods your application can use to create or
update a workspace.

API Version: 1.0
See: https://cloud.ibm.com/docs/assistant
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional
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


class AssistantV1(BaseService):
    """The Assistant V1 service."""

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
    # Message
    #########################

    def message(
        self,
        workspace_id: str,
        *,
        input: Optional['MessageInput'] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        alternate_intents: Optional[bool] = None,
        context: Optional['Context'] = None,
        output: Optional['OutputData'] = None,
        user_id: Optional[str] = None,
        nodes_visited_details: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get response to user input.

        Send user input to a workspace and receive a response.
        **Important:** This method has been superseded by the new v2 runtime API. The v2
        API offers significant advantages, including ease of deployment, automatic state
        management, versioning, and search capabilities. For more information, see the
        [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-api-overview).

        :param str workspace_id: Unique identifier of the workspace.
        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param List[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param List[RuntimeEntity] entities: (optional) Entities to use when
               evaluating the message. Include entities from the previous response to
               continue using those entities rather than detecting entities in the new
               input.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. A value of `true` indicates that all matching intents are returned.
        :param Context context: (optional) State information for the conversation.
               To maintain state, include the context from the previous response.
        :param OutputData output: (optional) An output object that includes the
               response to the user, the dialog nodes that were triggered, and messages
               from the log.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the workspace. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.conversation_id**.
               **Note:** This property is the same as the **user_id** property in the
               context metadata. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        :param bool nodes_visited_details: (optional) Whether to include additional
               diagnostic information about the dialog nodes that were visited during
               processing of the message.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `MessageResponse` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if input is not None:
            input = convert_model(input)
        if intents is not None:
            intents = [convert_model(x) for x in intents]
        if entities is not None:
            entities = [convert_model(x) for x in entities]
        if context is not None:
            context = convert_model(context)
        if output is not None:
            output = convert_model(output)
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='message',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'nodes_visited_details': nodes_visited_details,
        }

        data = {
            'input': input,
            'intents': intents,
            'entities': entities,
            'alternate_intents': alternate_intents,
            'context': context,
            'output': output,
            'user_id': user_id,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/message'.format(**path_param_dict)
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
        workspace_id: str,
        *,
        input: Optional[List['BulkClassifyUtterance']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Identify intents and entities in multiple user utterances.

        Send multiple user inputs to a workspace in a single request and receive
        information about the intents and entities recognized in each input. This method
        is useful for testing and comparing the performance of different workspaces.
        This method is available only with Enterprise with Data Isolation plans.

        :param str workspace_id: Unique identifier of the workspace.
        :param List[BulkClassifyUtterance] input: (optional) An array of input
               utterances to classify.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `BulkClassifyResponse` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if input is not None:
            input = [convert_model(x) for x in input]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/bulk_classify'.format(
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
    # Workspaces
    #########################

    def list_workspaces(
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
        List workspaces.

        List the workspaces associated with a Watson Assistant service instance.

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
        :rtype: DetailedResponse with `dict` result representing a `WorkspaceCollection` object
        """

        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_workspaces',
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

        url = '/v1/workspaces'
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_workspace(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        language: Optional[str] = None,
        dialog_nodes: Optional[List['DialogNode']] = None,
        counterexamples: Optional[List['Counterexample']] = None,
        metadata: Optional[dict] = None,
        learning_opt_out: Optional[bool] = None,
        system_settings: Optional['WorkspaceSystemSettings'] = None,
        webhooks: Optional[List['Webhook']] = None,
        intents: Optional[List['CreateIntent']] = None,
        entities: Optional[List['CreateEntity']] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create workspace.

        Create a workspace based on component objects. You must provide workspace
        components defining the content of the new workspace.
        **Note:** The new workspace data cannot be larger than 1.5 MB. For larger
        requests, use the **Create workspace asynchronously** method.

        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param List[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param List[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param List[Webhook] webhooks: (optional)
        :param List[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param List[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if dialog_nodes is not None:
            dialog_nodes = [convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [convert_model(x) for x in counterexamples]
        if system_settings is not None:
            system_settings = convert_model(system_settings)
        if webhooks is not None:
            webhooks = [convert_model(x) for x in webhooks]
        if intents is not None:
            intents = [convert_model(x) for x in intents]
        if entities is not None:
            entities = [convert_model(x) for x in entities]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_workspace',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'name': name,
            'description': description,
            'language': language,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'webhooks': webhooks,
            'intents': intents,
            'entities': entities,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/workspaces'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_workspace(
        self,
        workspace_id: str,
        *,
        export: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        sort: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get information about a workspace.

        Get information about a workspace, optionally including all workspace content.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param str sort: (optional) Indicates how the returned workspace data will
               be sorted. This parameter is valid only if **export**=`true`. Specify
               `sort=stable` to sort all workspace objects by unique identifier, in
               ascending alphabetical order.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_workspace',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
            'sort': sort,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_workspace(
        self,
        workspace_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        language: Optional[str] = None,
        dialog_nodes: Optional[List['DialogNode']] = None,
        counterexamples: Optional[List['Counterexample']] = None,
        metadata: Optional[dict] = None,
        learning_opt_out: Optional[bool] = None,
        system_settings: Optional['WorkspaceSystemSettings'] = None,
        webhooks: Optional[List['Webhook']] = None,
        intents: Optional[List['CreateIntent']] = None,
        entities: Optional[List['CreateEntity']] = None,
        append: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update workspace.

        Update an existing workspace with new or modified data. You must provide component
        objects defining the content of the updated workspace.
        **Note:** The new workspace data cannot be larger than 1.5 MB. For larger
        requests, use the **Update workspace asynchronously** method.

        :param str workspace_id: Unique identifier of the workspace.
        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param List[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param List[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param List[Webhook] webhooks: (optional)
        :param List[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param List[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the object. If **append**=`false`, elements included
               in the new data completely replace the corresponding existing elements,
               including all subelements. For example, if the new data for a workspace
               includes **entities** and **append**=`false`, all existing entities in the
               workspace are discarded and replaced with the new entities.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if dialog_nodes is not None:
            dialog_nodes = [convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [convert_model(x) for x in counterexamples]
        if system_settings is not None:
            system_settings = convert_model(system_settings)
        if webhooks is not None:
            webhooks = [convert_model(x) for x in webhooks]
        if intents is not None:
            intents = [convert_model(x) for x in intents]
        if entities is not None:
            entities = [convert_model(x) for x in entities]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_workspace',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'append': append,
            'include_audit': include_audit,
        }

        data = {
            'name': name,
            'description': description,
            'language': language,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'webhooks': webhooks,
            'intents': intents,
            'entities': entities,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def delete_workspace(
        self,
        workspace_id: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete workspace.

        Delete a workspace from the service instance.

        :param str workspace_id: Unique identifier of the workspace.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_workspace',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_workspace_async(
        self,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        language: Optional[str] = None,
        dialog_nodes: Optional[List['DialogNode']] = None,
        counterexamples: Optional[List['Counterexample']] = None,
        metadata: Optional[dict] = None,
        learning_opt_out: Optional[bool] = None,
        system_settings: Optional['WorkspaceSystemSettings'] = None,
        webhooks: Optional[List['Webhook']] = None,
        intents: Optional[List['CreateIntent']] = None,
        entities: Optional[List['CreateEntity']] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create workspace asynchronously.

        Create a workspace asynchronously based on component objects. You must provide
        workspace components defining the content of the new workspace.
        A successful call to this method only initiates asynchronous creation of the
        workspace. The new workspace is not available until processing completes. To check
        the status of the asynchronous operation, use the **Get information about a
        workspace** method.

        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param List[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param List[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param List[Webhook] webhooks: (optional)
        :param List[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param List[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if dialog_nodes is not None:
            dialog_nodes = [convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [convert_model(x) for x in counterexamples]
        if system_settings is not None:
            system_settings = convert_model(system_settings)
        if webhooks is not None:
            webhooks = [convert_model(x) for x in webhooks]
        if intents is not None:
            intents = [convert_model(x) for x in intents]
        if entities is not None:
            entities = [convert_model(x) for x in entities]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_workspace_async',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        data = {
            'name': name,
            'description': description,
            'language': language,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'webhooks': webhooks,
            'intents': intents,
            'entities': entities,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/workspaces_async'
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def update_workspace_async(
        self,
        workspace_id: str,
        *,
        name: Optional[str] = None,
        description: Optional[str] = None,
        language: Optional[str] = None,
        dialog_nodes: Optional[List['DialogNode']] = None,
        counterexamples: Optional[List['Counterexample']] = None,
        metadata: Optional[dict] = None,
        learning_opt_out: Optional[bool] = None,
        system_settings: Optional['WorkspaceSystemSettings'] = None,
        webhooks: Optional[List['Webhook']] = None,
        intents: Optional[List['CreateIntent']] = None,
        entities: Optional[List['CreateEntity']] = None,
        append: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update workspace asynchronously.

        Update an existing workspace asynchronously with new or modified data. You must
        provide component objects defining the content of the updated workspace.
        A successful call to this method only initiates an asynchronous update of the
        workspace. The updated workspace is not available until processing completes. To
        check the status of the asynchronous operation, use the **Get information about a
        workspace** method.

        :param str workspace_id: Unique identifier of the workspace.
        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param List[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param List[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param List[Webhook] webhooks: (optional)
        :param List[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param List[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the object. If **append**=`false`, elements included
               in the new data completely replace the corresponding existing elements,
               including all subelements. For example, if the new data for a workspace
               includes **entities** and **append**=`false`, all existing entities in the
               workspace are discarded and replaced with the new entities.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if dialog_nodes is not None:
            dialog_nodes = [convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [convert_model(x) for x in counterexamples]
        if system_settings is not None:
            system_settings = convert_model(system_settings)
        if webhooks is not None:
            webhooks = [convert_model(x) for x in webhooks]
        if intents is not None:
            intents = [convert_model(x) for x in intents]
        if entities is not None:
            entities = [convert_model(x) for x in entities]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_workspace_async',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'append': append,
        }

        data = {
            'name': name,
            'description': description,
            'language': language,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'webhooks': webhooks,
            'intents': intents,
            'entities': entities,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces_async/{workspace_id}'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def export_workspace_async(
        self,
        workspace_id: str,
        *,
        include_audit: Optional[bool] = None,
        sort: Optional[str] = None,
        verbose: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Export workspace asynchronously.

        Export the entire workspace asynchronously, including all workspace content.
        A successful call to this method only initiates an asynchronous export. The
        exported JSON data is not available until processing completes. After the initial
        request is submitted, you can continue to poll by calling the same request again
        and checking the value of the **status** property. When processing has completed,
        the request returns the exported JSON data. Remember that the usual rate limits
        apply.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param str sort: (optional) Indicates how the returned workspace data will
               be sorted. Specify `sort=stable` to sort all workspace objects by unique
               identifier, in ascending alphabetical order.
        :param bool verbose: (optional) Whether the response should include the
               `counts` property, which indicates how many of each component (such as
               intents and entities) the workspace contains.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Workspace` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='export_workspace_async',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
            'sort': sort,
            'verbose': verbose,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces_async/{workspace_id}/export'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Intents
    #########################

    def list_intents(
        self,
        workspace_id: str,
        *,
        export: Optional[bool] = None,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List intents.

        List the intents for a workspace.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned intents will be
               sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `IntentCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_intents',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_intent(
        self,
        workspace_id: str,
        intent: str,
        *,
        description: Optional[str] = None,
        examples: Optional[List['Example']] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create intent.

        Create a new intent.
        If you want to create multiple intents with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param List[Example] examples: (optional) An array of user input examples
               for the intent.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Intent` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if examples is not None:
            examples = [convert_model(x) for x in examples]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_intent',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'intent': intent,
            'description': description,
            'examples': examples,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_intent(
        self,
        workspace_id: str,
        intent: str,
        *,
        export: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get intent.

        Get information about an intent, optionally including all intent content.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Intent` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_intent',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent']
        path_param_values = self.encode_path_vars(workspace_id, intent)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_intent(
        self,
        workspace_id: str,
        intent: str,
        *,
        new_intent: Optional[str] = None,
        new_description: Optional[str] = None,
        new_examples: Optional[List['Example']] = None,
        append: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update intent.

        Update an existing intent with new or modified data. You must provide component
        objects defining the content of the updated intent.
        If you want to update multiple intents with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str new_intent: (optional) The name of the intent. This string must
               conform to the following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str new_description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param List[Example] new_examples: (optional) An array of user input
               examples for the intent.
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the object. If **append**=`false`, elements included
               in the new data completely replace the corresponding existing elements,
               including all subelements. For example, if the new data for the intent
               includes **examples** and **append**=`false`, all existing examples for the
               intent are discarded and replaced with the new examples.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Intent` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        if new_examples is not None:
            new_examples = [convert_model(x) for x in new_examples]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_intent',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'append': append,
            'include_audit': include_audit,
        }

        data = {
            'intent': new_intent,
            'description': new_description,
            'examples': new_examples,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent']
        path_param_values = self.encode_path_vars(workspace_id, intent)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}'.format(
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

    def delete_intent(
        self,
        workspace_id: str,
        intent: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete intent.

        Delete an intent from a workspace.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_intent',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent']
        path_param_values = self.encode_path_vars(workspace_id, intent)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}'.format(
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
    # Examples
    #########################

    def list_examples(
        self,
        workspace_id: str,
        intent: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List user input examples.

        List the user input examples for an intent, optionally including contextual entity
        mentions.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned examples will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ExampleCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_examples',
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

        path_param_keys = ['workspace_id', 'intent']
        path_param_values = self.encode_path_vars(workspace_id, intent)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}/examples'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_example(
        self,
        workspace_id: str,
        intent: str,
        text: str,
        *,
        mentions: Optional[List['Mention']] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create user input example.

        Add a new user input example to an intent.
        If you want to add multiple examples with a single API call, consider using the
        **[Update intent](#update-intent)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of a user input example. This string must conform
               to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[Mention] mentions: (optional) An array of contextual entity
               mentions.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Example` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        if mentions is not None:
            mentions = [convert_model(x) for x in mentions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_example',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'text': text,
            'mentions': mentions,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent']
        path_param_values = self.encode_path_vars(workspace_id, intent)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}/examples'.format(
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

    def get_example(
        self,
        workspace_id: str,
        intent: str,
        text: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get user input example.

        Get information about a user input example.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Example` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_example',
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

        path_param_keys = ['workspace_id', 'intent', 'text']
        path_param_values = self.encode_path_vars(workspace_id, intent, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}/examples/{text}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_example(
        self,
        workspace_id: str,
        intent: str,
        text: str,
        *,
        new_text: Optional[str] = None,
        new_mentions: Optional[List['Mention']] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update user input example.

        Update the text of a user input example.
        If you want to update multiple examples with a single API call, consider using the
        **[Update intent](#update-intent)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param str new_text: (optional) The text of the user input example. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[Mention] new_mentions: (optional) An array of contextual entity
               mentions.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Example` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        if not text:
            raise ValueError('text must be provided')
        if new_mentions is not None:
            new_mentions = [convert_model(x) for x in new_mentions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_example',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'text': new_text,
            'mentions': new_mentions,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent', 'text']
        path_param_values = self.encode_path_vars(workspace_id, intent, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}/examples/{text}'.format(
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

    def delete_example(
        self,
        workspace_id: str,
        intent: str,
        text: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete user input example.

        Delete a user input example from an intent.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not intent:
            raise ValueError('intent must be provided')
        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_example',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'intent', 'text']
        path_param_values = self.encode_path_vars(workspace_id, intent, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/intents/{intent}/examples/{text}'.format(
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
    # Counterexamples
    #########################

    def list_counterexamples(
        self,
        workspace_id: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List counterexamples.

        List the counterexamples for a workspace. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned counterexamples
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CounterexampleCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_counterexamples',
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/counterexamples'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_counterexample(
        self,
        workspace_id: str,
        text: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create counterexample.

        Add a new counterexample to a workspace. Counterexamples are examples that have
        been marked as irrelevant input.
        If you want to add multiple counterexamples with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input marked as irrelevant input. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Counterexample` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_counterexample',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'text': text,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/counterexamples'.format(
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

    def get_counterexample(
        self,
        workspace_id: str,
        text: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get counterexample.

        Get information about a counterexample. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Counterexample` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_counterexample',
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

        path_param_keys = ['workspace_id', 'text']
        path_param_values = self.encode_path_vars(workspace_id, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/counterexamples/{text}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_counterexample(
        self,
        workspace_id: str,
        text: str,
        *,
        new_text: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update counterexample.

        Update the text of a counterexample. Counterexamples are examples that have been
        marked as irrelevant input.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param str new_text: (optional) The text of a user input marked as
               irrelevant input. This string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Counterexample` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_counterexample',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'text': new_text,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'text']
        path_param_values = self.encode_path_vars(workspace_id, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/counterexamples/{text}'.format(
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

    def delete_counterexample(
        self,
        workspace_id: str,
        text: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete counterexample.

        Delete a counterexample from a workspace. Counterexamples are examples that have
        been marked as irrelevant input.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not text:
            raise ValueError('text must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_counterexample',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'text']
        path_param_values = self.encode_path_vars(workspace_id, text)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/counterexamples/{text}'.format(
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
    # Entities
    #########################

    def list_entities(
        self,
        workspace_id: str,
        *,
        export: Optional[bool] = None,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List entities.

        List the entities for a workspace.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned entities will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EntityCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_entities',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_entity(
        self,
        workspace_id: str,
        entity: str,
        *,
        description: Optional[str] = None,
        metadata: Optional[dict] = None,
        fuzzy_match: Optional[bool] = None,
        values: Optional[List['CreateValue']] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create entity.

        Create a new entity, or enable a system entity.
        If you want to create multiple entities with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, and hyphen
               characters.
               - If you specify an entity name beginning with the reserved prefix `sys-`,
               it must be the name of a system entity that you want to enable. (Any entity
               content specified with the request is ignored.).
        :param str description: (optional) The description of the entity. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the
               entity.
        :param List[CreateValue] values: (optional) An array of objects describing
               the entity values.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Entity` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if values is not None:
            values = [convert_model(x) for x in values]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_entity',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'entity': entity,
            'description': description,
            'metadata': metadata,
            'fuzzy_match': fuzzy_match,
            'values': values,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities'.format(**path_param_dict)
        request = self.prepare_request(
            method='POST',
            url=url,
            headers=headers,
            params=params,
            data=data,
        )

        response = self.send(request, **kwargs)
        return response

    def get_entity(
        self,
        workspace_id: str,
        entity: str,
        *,
        export: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get entity.

        Get information about an entity, optionally including all entity content.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Entity` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_entity',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_entity(
        self,
        workspace_id: str,
        entity: str,
        *,
        new_entity: Optional[str] = None,
        new_description: Optional[str] = None,
        new_metadata: Optional[dict] = None,
        new_fuzzy_match: Optional[bool] = None,
        new_values: Optional[List['CreateValue']] = None,
        append: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update entity.

        Update an existing entity with new or modified data. You must provide component
        objects defining the content of the updated entity.
        If you want to update multiple entities with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str new_entity: (optional) The name of the entity. This string must
               conform to the following restrictions:
               - It can contain only Unicode alphanumeric, underscore, and hyphen
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str new_description: (optional) The description of the entity. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict new_metadata: (optional) Any metadata related to the entity.
        :param bool new_fuzzy_match: (optional) Whether to use fuzzy matching for
               the entity.
        :param List[CreateValue] new_values: (optional) An array of objects
               describing the entity values.
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the entity. If **append**=`false`, elements included
               in the new data completely replace the corresponding existing elements,
               including all subelements. For example, if the new data for the entity
               includes **values** and **append**=`false`, all existing values for the
               entity are discarded and replaced with the new values.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Entity` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if new_values is not None:
            new_values = [convert_model(x) for x in new_values]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_entity',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'append': append,
            'include_audit': include_audit,
        }

        data = {
            'entity': new_entity,
            'description': new_description,
            'metadata': new_metadata,
            'fuzzy_match': new_fuzzy_match,
            'values': new_values,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}'.format(
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

    def delete_entity(
        self,
        workspace_id: str,
        entity: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete entity.

        Delete an entity from a workspace, or disable a system entity.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_entity',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}'.format(
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
    # Mentions
    #########################

    def list_mentions(
        self,
        workspace_id: str,
        entity: str,
        *,
        export: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List entity mentions.

        List mentions for a contextual entity. An entity mention is an occurrence of a
        contextual entity in the context of an intent user input example.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `EntityMentionCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_mentions',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/mentions'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    #########################
    # Values
    #########################

    def list_values(
        self,
        workspace_id: str,
        entity: str,
        *,
        export: Optional[bool] = None,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List entity values.

        List the values for an entity.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned entity values
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ValueCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_values',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
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

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_value(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        *,
        metadata: Optional[dict] = None,
        type: Optional[str] = None,
        synonyms: Optional[List[str]] = None,
        patterns: Optional[List[str]] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create entity value.

        Create a new value for an entity.
        If you want to create multiple entity values with a single API call, consider
        using the **[Update entity](#update-entity)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param str type: (optional) Specifies the type of entity value.
        :param List[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Value` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_value',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'value': value,
            'metadata': metadata,
            'type': type,
            'synonyms': synonyms,
            'patterns': patterns,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity']
        path_param_values = self.encode_path_vars(workspace_id, entity)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values'.format(
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

    def get_value(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        *,
        export: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get entity value.

        Get information about an entity value.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Value` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_value',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value']
        path_param_values = self.encode_path_vars(workspace_id, entity, value)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_value(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        *,
        new_value: Optional[str] = None,
        new_metadata: Optional[dict] = None,
        new_type: Optional[str] = None,
        new_synonyms: Optional[List[str]] = None,
        new_patterns: Optional[List[str]] = None,
        append: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update entity value.

        Update an existing entity value with new or modified data. You must provide
        component objects defining the content of the updated entity value.
        If you want to update multiple entity values with a single API call, consider
        using the **[Update entity](#update-entity)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str new_value: (optional) The text of the entity value. This string
               must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict new_metadata: (optional) Any metadata related to the entity
               value.
        :param str new_type: (optional) Specifies the type of entity value.
        :param List[str] new_synonyms: (optional) An array of synonyms for the
               entity value. A value can specify either synonyms or patterns (depending on
               the value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[str] new_patterns: (optional) An array of patterns for the
               entity value. A value can specify either synonyms or patterns (depending on
               the value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the entity value. If **append**=`false`, elements
               included in the new data completely replace the corresponding existing
               elements, including all subelements. For example, if the new data for the
               entity value includes **synonyms** and **append**=`false`, all existing
               synonyms for the entity value are discarded and replaced with the new
               synonyms.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Value` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_value',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'append': append,
            'include_audit': include_audit,
        }

        data = {
            'value': new_value,
            'metadata': new_metadata,
            'type': new_type,
            'synonyms': new_synonyms,
            'patterns': new_patterns,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value']
        path_param_values = self.encode_path_vars(workspace_id, entity, value)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}'.format(
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

    def delete_value(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete entity value.

        Delete a value from an entity.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_value',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value']
        path_param_values = self.encode_path_vars(workspace_id, entity, value)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}'.format(
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
    # Synonyms
    #########################

    def list_synonyms(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List entity value synonyms.

        List the synonyms for an entity value.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned entity value
               synonyms will be sorted. To reverse the sort order, prefix the value with a
               minus sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `SynonymCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_synonyms',
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

        path_param_keys = ['workspace_id', 'entity', 'value']
        path_param_values = self.encode_path_vars(workspace_id, entity, value)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}/synonyms'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_synonym(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        synonym: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create entity value synonym.

        Add a new synonym to an entity value.
        If you want to create multiple synonyms with a single API call, consider using the
        **[Update entity](#update-entity)** or **[Update entity
        value](#update-entity-value)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Synonym` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        if synonym is None:
            raise ValueError('synonym must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_synonym',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'synonym': synonym,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value']
        path_param_values = self.encode_path_vars(workspace_id, entity, value)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}/synonyms'.format(
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

    def get_synonym(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        synonym: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get entity value synonym.

        Get information about a synonym of an entity value.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Synonym` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        if not synonym:
            raise ValueError('synonym must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_synonym',
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

        path_param_keys = ['workspace_id', 'entity', 'value', 'synonym']
        path_param_values = self.encode_path_vars(workspace_id, entity, value,
                                                  synonym)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}/synonyms/{synonym}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_synonym(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        synonym: str,
        *,
        new_synonym: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update entity value synonym.

        Update an existing entity value synonym with new text.
        If you want to update multiple synonyms with a single API call, consider using the
        **[Update entity](#update-entity)** or **[Update entity
        value](#update-entity-value)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param str new_synonym: (optional) The text of the synonym. This string
               must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Synonym` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        if not synonym:
            raise ValueError('synonym must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_synonym',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'synonym': new_synonym,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value', 'synonym']
        path_param_values = self.encode_path_vars(workspace_id, entity, value,
                                                  synonym)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}/synonyms/{synonym}'.format(
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

    def delete_synonym(
        self,
        workspace_id: str,
        entity: str,
        value: str,
        synonym: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete entity value synonym.

        Delete a synonym from an entity value.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not entity:
            raise ValueError('entity must be provided')
        if not value:
            raise ValueError('value must be provided')
        if not synonym:
            raise ValueError('synonym must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_synonym',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'entity', 'value', 'synonym']
        path_param_values = self.encode_path_vars(workspace_id, entity, value,
                                                  synonym)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/entities/{entity}/values/{value}/synonyms/{synonym}'.format(
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
    # Dialog nodes
    #########################

    def list_dialog_nodes(
        self,
        workspace_id: str,
        *,
        page_limit: Optional[int] = None,
        include_count: Optional[bool] = None,
        sort: Optional[str] = None,
        cursor: Optional[str] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List dialog nodes.

        List the dialog nodes for a workspace.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param bool include_count: (optional) Whether to include information about
               the number of records that satisfy the request, regardless of the page
               limit. If this parameter is `true`, the `pagination` object in the response
               includes the `total` property.
        :param str sort: (optional) The attribute by which returned dialog nodes
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DialogNodeCollection` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_dialog_nodes',
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/dialog_nodes'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def create_dialog_node(
        self,
        workspace_id: str,
        dialog_node: str,
        *,
        description: Optional[str] = None,
        conditions: Optional[str] = None,
        parent: Optional[str] = None,
        previous_sibling: Optional[str] = None,
        output: Optional['DialogNodeOutput'] = None,
        context: Optional['DialogNodeContext'] = None,
        metadata: Optional[dict] = None,
        next_step: Optional['DialogNodeNextStep'] = None,
        title: Optional[str] = None,
        type: Optional[str] = None,
        event_name: Optional[str] = None,
        variable: Optional[str] = None,
        actions: Optional[List['DialogNodeAction']] = None,
        digress_in: Optional[str] = None,
        digress_out: Optional[str] = None,
        digress_out_slots: Optional[str] = None,
        user_label: Optional[str] = None,
        disambiguation_opt_out: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Create dialog node.

        Create a new dialog node.
        If you want to create multiple dialog nodes with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The unique ID of the dialog node. This is an
               internal identifier used to refer to the dialog node from other dialog
               nodes and in the diagnostic information included with message responses.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str description: (optional) The description of the dialog node. This
               string cannot contain carriage return, newline, or tab characters.
        :param str conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str parent: (optional) The unique ID of the parent dialog node. This
               property is omitted if the dialog node has no parent.
        :param str previous_sibling: (optional) The unique ID of the previous
               sibling dialog node. This property is omitted if the dialog node has no
               previous sibling.
        :param DialogNodeOutput output: (optional) The output of the dialog node.
               For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param DialogNodeContext context: (optional) The context for the dialog
               node.
        :param dict metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute
               following this dialog node.
        :param str title: (optional) A human-readable name for the dialog node. If
               the node is included in disambiguation, this title is used to populate the
               **label** property of the corresponding suggestion in the `suggestion`
               response type (unless it is overridden by the **user_label** property). The
               title is also used to populate the **topic** property in the
               `connect_to_agent` response type.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where
               output is stored.
        :param List[DialogNodeAction] actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str digress_in: (optional) Whether this top-level dialog node can be
               digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned
               to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to
               top-level nodes while filling out slots.
        :param str user_label: (optional) A label that can be displayed externally
               to describe the purpose of the node to users. If set, this label is used to
               identify the node in disambiguation responses (overriding the value of the
               **title** property).
        :param bool disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions. Valid only when
               **type**=`standard` or `frame`.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DialogNode` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if output is not None:
            output = convert_model(output)
        if context is not None:
            context = convert_model(context)
        if next_step is not None:
            next_step = convert_model(next_step)
        if actions is not None:
            actions = [convert_model(x) for x in actions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='create_dialog_node',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'dialog_node': dialog_node,
            'description': description,
            'conditions': conditions,
            'parent': parent,
            'previous_sibling': previous_sibling,
            'output': output,
            'context': context,
            'metadata': metadata,
            'next_step': next_step,
            'title': title,
            'type': type,
            'event_name': event_name,
            'variable': variable,
            'actions': actions,
            'digress_in': digress_in,
            'digress_out': digress_out,
            'digress_out_slots': digress_out_slots,
            'user_label': user_label,
            'disambiguation_opt_out': disambiguation_opt_out,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/dialog_nodes'.format(
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

    def get_dialog_node(
        self,
        workspace_id: str,
        dialog_node: str,
        *,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Get dialog node.

        Get information about a dialog node.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example,
               `node_1_1479323581900`).
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DialogNode` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not dialog_node:
            raise ValueError('dialog_node must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='get_dialog_node',
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

        path_param_keys = ['workspace_id', 'dialog_node']
        path_param_values = self.encode_path_vars(workspace_id, dialog_node)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/dialog_nodes/{dialog_node}'.format(
            **path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def update_dialog_node(
        self,
        workspace_id: str,
        dialog_node: str,
        *,
        new_dialog_node: Optional[str] = None,
        new_description: Optional[str] = None,
        new_conditions: Optional[str] = None,
        new_parent: Optional[str] = None,
        new_previous_sibling: Optional[str] = None,
        new_output: Optional['DialogNodeOutput'] = None,
        new_context: Optional['DialogNodeContext'] = None,
        new_metadata: Optional[dict] = None,
        new_next_step: Optional['DialogNodeNextStep'] = None,
        new_title: Optional[str] = None,
        new_type: Optional[str] = None,
        new_event_name: Optional[str] = None,
        new_variable: Optional[str] = None,
        new_actions: Optional[List['DialogNodeAction']] = None,
        new_digress_in: Optional[str] = None,
        new_digress_out: Optional[str] = None,
        new_digress_out_slots: Optional[str] = None,
        new_user_label: Optional[str] = None,
        new_disambiguation_opt_out: Optional[bool] = None,
        include_audit: Optional[bool] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        Update dialog node.

        Update an existing dialog node with new or modified data.
        If you want to update multiple dialog nodes with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example,
               `node_1_1479323581900`).
        :param str new_dialog_node: (optional) The unique ID of the dialog node.
               This is an internal identifier used to refer to the dialog node from other
               dialog nodes and in the diagnostic information included with message
               responses.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str new_description: (optional) The description of the dialog node.
               This string cannot contain carriage return, newline, or tab characters.
        :param str new_conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str new_parent: (optional) The unique ID of the parent dialog node.
               This property is omitted if the dialog node has no parent.
        :param str new_previous_sibling: (optional) The unique ID of the previous
               sibling dialog node. This property is omitted if the dialog node has no
               previous sibling.
        :param DialogNodeOutput new_output: (optional) The output of the dialog
               node. For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param DialogNodeContext new_context: (optional) The context for the dialog
               node.
        :param dict new_metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep new_next_step: (optional) The next step to
               execute following this dialog node.
        :param str new_title: (optional) A human-readable name for the dialog node.
               If the node is included in disambiguation, this title is used to populate
               the **label** property of the corresponding suggestion in the `suggestion`
               response type (unless it is overridden by the **user_label** property). The
               title is also used to populate the **topic** property in the
               `connect_to_agent` response type.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str new_type: (optional) How the dialog node is processed.
        :param str new_event_name: (optional) How an `event_handler` node is
               processed.
        :param str new_variable: (optional) The location in the dialog context
               where output is stored.
        :param List[DialogNodeAction] new_actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str new_digress_in: (optional) Whether this top-level dialog node
               can be digressed into.
        :param str new_digress_out: (optional) Whether this dialog node can be
               returned to after a digression.
        :param str new_digress_out_slots: (optional) Whether the user can digress
               to top-level nodes while filling out slots.
        :param str new_user_label: (optional) A label that can be displayed
               externally to describe the purpose of the node to users. If set, this label
               is used to identify the node in disambiguation responses (overriding the
               value of the **title** property).
        :param bool new_disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions. Valid only when
               **type**=`standard` or `frame`.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `DialogNode` object
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not dialog_node:
            raise ValueError('dialog_node must be provided')
        if new_output is not None:
            new_output = convert_model(new_output)
        if new_context is not None:
            new_context = convert_model(new_context)
        if new_next_step is not None:
            new_next_step = convert_model(new_next_step)
        if new_actions is not None:
            new_actions = [convert_model(x) for x in new_actions]
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='update_dialog_node',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'include_audit': include_audit,
        }

        data = {
            'dialog_node': new_dialog_node,
            'description': new_description,
            'conditions': new_conditions,
            'parent': new_parent,
            'previous_sibling': new_previous_sibling,
            'output': new_output,
            'context': new_context,
            'metadata': new_metadata,
            'next_step': new_next_step,
            'title': new_title,
            'type': new_type,
            'event_name': new_event_name,
            'variable': new_variable,
            'actions': new_actions,
            'digress_in': new_digress_in,
            'digress_out': new_digress_out,
            'digress_out_slots': new_digress_out_slots,
            'user_label': new_user_label,
            'disambiguation_opt_out': new_disambiguation_opt_out,
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'dialog_node']
        path_param_values = self.encode_path_vars(workspace_id, dialog_node)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/dialog_nodes/{dialog_node}'.format(
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

    def delete_dialog_node(
        self,
        workspace_id: str,
        dialog_node: str,
        **kwargs,
    ) -> DetailedResponse:
        """
        Delete dialog node.

        Delete a dialog node from a workspace.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example,
               `node_1_1479323581900`).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        if not dialog_node:
            raise ValueError('dialog_node must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='delete_dialog_node',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['workspace_id', 'dialog_node']
        path_param_values = self.encode_path_vars(workspace_id, dialog_node)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/dialog_nodes/{dialog_node}'.format(
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
    # Logs
    #########################

    def list_logs(
        self,
        workspace_id: str,
        *,
        sort: Optional[str] = None,
        filter: Optional[str] = None,
        page_limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List log events in a workspace.

        List the events from the log of a specific workspace.
        This method requires Manager access.
        **Note:** If you use the **cursor** parameter to retrieve results one page at a
        time, subsequent requests must be no more than 5 minutes apart. Any returned value
        for the **cursor** parameter becomes invalid after 5 minutes. For more information
        about using pagination, see [Pagination](#pagination).

        :param str workspace_id: Unique identifier of the workspace.
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

        if not workspace_id:
            raise ValueError('workspace_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
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

        path_param_keys = ['workspace_id']
        path_param_values = self.encode_path_vars(workspace_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v1/workspaces/{workspace_id}/logs'.format(**path_param_dict)
        request = self.prepare_request(
            method='GET',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response

    def list_all_logs(
        self,
        filter: str,
        *,
        sort: Optional[str] = None,
        page_limit: Optional[int] = None,
        cursor: Optional[str] = None,
        **kwargs,
    ) -> DetailedResponse:
        """
        List log events in all workspaces.

        List the events from the logs of all workspaces in the service instance.
        **Note:** If you use the **cursor** parameter to retrieve results one page at a
        time, subsequent requests must be no more than 5 minutes apart. Any returned value
        for the **cursor** parameter becomes invalid after 5 minutes. For more information
        about using pagination, see [Pagination](#pagination).

        :param str filter: A cacheable parameter that limits the results to those
               matching the specified filter. You must specify a filter query that
               includes a value for `language`, as well as a value for
               `request.context.system.assistant_id`, `workspace_id`, or
               `request.context.metadata.deployment`. These required filters must be
               specified using the exact match (`::`) operator. For more information, see
               the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-filter-reference#filter-reference).
        :param str sort: (optional) How to sort the returned log events. You can
               sort by **request_timestamp**. To reverse the sort order, prefix the
               parameter value with a minus sign (`-`).
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogCollection` object
        """

        if not filter:
            raise ValueError('filter must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
            operation_id='list_all_logs',
        )
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'sort': sort,
            'page_limit': page_limit,
            'cursor': cursor,
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        url = '/v1/logs'
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
        sdk_headers = get_sdk_headers(
            service_name=self.DEFAULT_SERVICE_NAME,
            service_version='V1',
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

        url = '/v1/user_data'
        request = self.prepare_request(
            method='DELETE',
            url=url,
            headers=headers,
            params=params,
        )

        response = self.send(request, **kwargs)
        return response


class ListWorkspacesEnums:
    """
    Enums for list_workspaces parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned workspaces will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        NAME = 'name'
        UPDATED = 'updated'


class GetWorkspaceEnums:
    """
    Enums for get_workspace parameters.
    """

    class Sort(str, Enum):
        """
        Indicates how the returned workspace data will be sorted. This parameter is valid
        only if **export**=`true`. Specify `sort=stable` to sort all workspace objects by
        unique identifier, in ascending alphabetical order.
        """

        STABLE = 'stable'


class ExportWorkspaceAsyncEnums:
    """
    Enums for export_workspace_async parameters.
    """

    class Sort(str, Enum):
        """
        Indicates how the returned workspace data will be sorted. Specify `sort=stable` to
        sort all workspace objects by unique identifier, in ascending alphabetical order.
        """

        STABLE = 'stable'


class ListIntentsEnums:
    """
    Enums for list_intents parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned intents will be sorted. To reverse the sort order,
        prefix the value with a minus sign (`-`).
        """

        INTENT = 'intent'
        UPDATED = 'updated'


class ListExamplesEnums:
    """
    Enums for list_examples parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned examples will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        TEXT = 'text'
        UPDATED = 'updated'


class ListCounterexamplesEnums:
    """
    Enums for list_counterexamples parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned counterexamples will be sorted. To reverse the
        sort order, prefix the value with a minus sign (`-`).
        """

        TEXT = 'text'
        UPDATED = 'updated'


class ListEntitiesEnums:
    """
    Enums for list_entities parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned entities will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        ENTITY = 'entity'
        UPDATED = 'updated'


class ListValuesEnums:
    """
    Enums for list_values parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned entity values will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        VALUE = 'value'
        UPDATED = 'updated'


class ListSynonymsEnums:
    """
    Enums for list_synonyms parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned entity value synonyms will be sorted. To reverse
        the sort order, prefix the value with a minus sign (`-`).
        """

        SYNONYM = 'synonym'
        UPDATED = 'updated'


class ListDialogNodesEnums:
    """
    Enums for list_dialog_nodes parameters.
    """

    class Sort(str, Enum):
        """
        The attribute by which returned dialog nodes will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """

        DIALOG_NODE = 'dialog_node'
        UPDATED = 'updated'


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
    A recognized capture group for a pattern-based entity.

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


class Context:
    """
    State information for the conversation. To maintain state, include the context from
    the previous response.

    :param str conversation_id: (optional) The unique identifier of the
          conversation. The conversation ID cannot contain any of the following
          characters: `+` `=` `&&` `||` `>` `<` `!` `(` `)` `{` `}` `[` `]` `^` `"` `~`
          `*` `?` `:` `\` `/`.
    :param dict system: (optional) For internal use only.
    :param MessageContextMetadata metadata: (optional) Metadata related to the
          message.

    This type supports additional properties of type object. Any context variable.
    """

    # The set of defined properties for the class
    _properties = frozenset(['conversation_id', 'system', 'metadata'])

    def __init__(
        self,
        *,
        conversation_id: Optional[str] = None,
        system: Optional[dict] = None,
        metadata: Optional['MessageContextMetadata'] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a Context object.

        :param str conversation_id: (optional) The unique identifier of the
               conversation. The conversation ID cannot contain any of the following
               characters: `+` `=` `&&` `||` `>` `<` `!` `(` `)` `{` `}` `[` `]` `^` `"`
               `~` `*` `?` `:` `\` `/`.
        :param dict system: (optional) For internal use only.
        :param MessageContextMetadata metadata: (optional) Metadata related to the
               message.
        :param object **kwargs: (optional) Any context variable.
        """
        self.conversation_id = conversation_id
        self.system = system
        self.metadata = metadata
        for k, v in kwargs.items():
            if k not in Context._properties:
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
    def from_dict(cls, _dict: Dict) -> 'Context':
        """Initialize a Context object from a json dictionary."""
        args = {}
        if (conversation_id := _dict.get('conversation_id')) is not None:
            args['conversation_id'] = conversation_id
        if (system := _dict.get('system')) is not None:
            args['system'] = system
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = MessageContextMetadata.from_dict(metadata)
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
        """Initialize a Context object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'conversation_id') and self.conversation_id is not None:
            _dict['conversation_id'] = self.conversation_id
        if hasattr(self, 'system') and self.system is not None:
            _dict['system'] = self.system
        if hasattr(self, 'metadata') and self.metadata is not None:
            if isinstance(self.metadata, dict):
                _dict['metadata'] = self.metadata
            else:
                _dict['metadata'] = self.metadata.to_dict()
        for k in [
                _k for _k in vars(self).keys() if _k not in Context._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of Context in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys() if _k not in Context._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of Context"""
        for k in [
                _k for _k in vars(self).keys() if _k not in Context._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in Context._properties:
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
        """Return a `str` version of this Context object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Context') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Context') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Counterexample:
    """
    Counterexample.

    :param str text: The text of a user input marked as irrelevant input. This
          string must conform to the following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        text: str,
        *,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Counterexample object.

        :param str text: The text of a user input marked as irrelevant input. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        """
        self.text = text
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Counterexample':
        """Initialize a Counterexample object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in Counterexample JSON')
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Counterexample object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Counterexample object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Counterexample') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Counterexample') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CounterexampleCollection:
    """
    CounterexampleCollection.

    :param List[Counterexample] counterexamples: An array of objects describing the
          examples marked as irrelevant input.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        counterexamples: List['Counterexample'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a CounterexampleCollection object.

        :param List[Counterexample] counterexamples: An array of objects describing
               the examples marked as irrelevant input.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.counterexamples = counterexamples
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CounterexampleCollection':
        """Initialize a CounterexampleCollection object from a json dictionary."""
        args = {}
        if (counterexamples := _dict.get('counterexamples')) is not None:
            args['counterexamples'] = [
                Counterexample.from_dict(v) for v in counterexamples
            ]
        else:
            raise ValueError(
                'Required property \'counterexamples\' not present in CounterexampleCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in CounterexampleCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CounterexampleCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'counterexamples') and self.counterexamples is not None:
            counterexamples_list = []
            for v in self.counterexamples:
                if isinstance(v, dict):
                    counterexamples_list.append(v)
                else:
                    counterexamples_list.append(v.to_dict())
            _dict['counterexamples'] = counterexamples_list
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
        """Return a `str` version of this CounterexampleCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CounterexampleCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CounterexampleCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateEntity:
    """
    CreateEntity.

    :param str entity: The name of the entity. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, and hyphen characters.
          - If you specify an entity name beginning with the reserved prefix `sys-`, it
          must be the name of a system entity that you want to enable. (Any entity content
          specified with the request is ignored.).
    :param str description: (optional) The description of the entity. This string
          cannot contain carriage return, newline, or tab characters.
    :param dict metadata: (optional) Any metadata related to the entity.
    :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the
          entity.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param List[CreateValue] values: (optional) An array of objects describing the
          entity values.
    """

    def __init__(
        self,
        entity: str,
        *,
        description: Optional[str] = None,
        metadata: Optional[dict] = None,
        fuzzy_match: Optional[bool] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        values: Optional[List['CreateValue']] = None,
    ) -> None:
        """
        Initialize a CreateEntity object.

        :param str entity: The name of the entity. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, and hyphen
               characters.
               - If you specify an entity name beginning with the reserved prefix `sys-`,
               it must be the name of a system entity that you want to enable. (Any entity
               content specified with the request is ignored.).
        :param str description: (optional) The description of the entity. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the
               entity.
        :param List[CreateValue] values: (optional) An array of objects describing
               the entity values.
        """
        self.entity = entity
        self.description = description
        self.metadata = metadata
        self.fuzzy_match = fuzzy_match
        self.created = created
        self.updated = updated
        self.values = values

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateEntity':
        """Initialize a CreateEntity object from a json dictionary."""
        args = {}
        if (entity := _dict.get('entity')) is not None:
            args['entity'] = entity
        else:
            raise ValueError(
                'Required property \'entity\' not present in CreateEntity JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (fuzzy_match := _dict.get('fuzzy_match')) is not None:
            args['fuzzy_match'] = fuzzy_match
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (values := _dict.get('values')) is not None:
            args['values'] = [CreateValue.from_dict(v) for v in values]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateEntity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'fuzzy_match') and self.fuzzy_match is not None:
            _dict['fuzzy_match'] = self.fuzzy_match
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'values') and self.values is not None:
            values_list = []
            for v in self.values:
                if isinstance(v, dict):
                    values_list.append(v)
                else:
                    values_list.append(v.to_dict())
            _dict['values'] = values_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateEntity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateEntity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateEntity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateIntent:
    """
    CreateIntent.

    :param str intent: The name of the intent. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
          characters.
          - It cannot begin with the reserved prefix `sys-`.
    :param str description: (optional) The description of the intent. This string
          cannot contain carriage return, newline, or tab characters.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param List[Example] examples: (optional) An array of user input examples for
          the intent.
    """

    def __init__(
        self,
        intent: str,
        *,
        description: Optional[str] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        examples: Optional[List['Example']] = None,
    ) -> None:
        """
        Initialize a CreateIntent object.

        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param List[Example] examples: (optional) An array of user input examples
               for the intent.
        """
        self.intent = intent
        self.description = description
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateIntent':
        """Initialize a CreateIntent object from a json dictionary."""
        args = {}
        if (intent := _dict.get('intent')) is not None:
            args['intent'] = intent
        else:
            raise ValueError(
                'Required property \'intent\' not present in CreateIntent JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (examples := _dict.get('examples')) is not None:
            args['examples'] = [Example.from_dict(v) for v in examples]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateIntent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'examples') and self.examples is not None:
            examples_list = []
            for v in self.examples:
                if isinstance(v, dict):
                    examples_list.append(v)
                else:
                    examples_list.append(v.to_dict())
            _dict['examples'] = examples_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateIntent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateIntent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateIntent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateValue:
    """
    CreateValue.

    :param str value: The text of the entity value. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param dict metadata: (optional) Any metadata related to the entity value.
    :param str type: (optional) Specifies the type of entity value.
    :param List[str] synonyms: (optional) An array of synonyms for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A synonym must conform to the following resrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param List[str] patterns: (optional) An array of patterns for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A pattern is a regular expression; for more information about how
          to specify a pattern, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        value: str,
        *,
        metadata: Optional[dict] = None,
        type: Optional[str] = None,
        synonyms: Optional[List[str]] = None,
        patterns: Optional[List[str]] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a CreateValue object.

        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param str type: (optional) Specifies the type of entity value.
        :param List[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
        """
        self.value = value
        self.metadata = metadata
        self.type = type
        self.synonyms = synonyms
        self.patterns = patterns
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CreateValue':
        """Initialize a CreateValue object from a json dictionary."""
        args = {}
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError(
                'Required property \'value\' not present in CreateValue JSON')
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (synonyms := _dict.get('synonyms')) is not None:
            args['synonyms'] = synonyms
        if (patterns := _dict.get('patterns')) is not None:
            args['patterns'] = patterns
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateValue object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = self.synonyms
        if hasattr(self, 'patterns') and self.patterns is not None:
            _dict['patterns'] = self.patterns
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CreateValue object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CreateValue') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CreateValue') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specifies the type of entity value.
        """

        SYNONYMS = 'synonyms'
        PATTERNS = 'patterns'


class DialogNode:
    """
    DialogNode.

    :param str dialog_node: The unique ID of the dialog node. This is an internal
          identifier used to refer to the dialog node from other dialog nodes and in the
          diagnostic information included with message responses.
          This string can contain only Unicode alphanumeric, space, underscore, hyphen,
          and dot characters.
    :param str description: (optional) The description of the dialog node. This
          string cannot contain carriage return, newline, or tab characters.
    :param str conditions: (optional) The condition that will trigger the dialog
          node. This string cannot contain carriage return, newline, or tab characters.
    :param str parent: (optional) The unique ID of the parent dialog node. This
          property is omitted if the dialog node has no parent.
    :param str previous_sibling: (optional) The unique ID of the previous sibling
          dialog node. This property is omitted if the dialog node has no previous
          sibling.
    :param DialogNodeOutput output: (optional) The output of the dialog node. For
          more information about how to specify dialog node output, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
    :param DialogNodeContext context: (optional) The context for the dialog node.
    :param dict metadata: (optional) The metadata for the dialog node.
    :param DialogNodeNextStep next_step: (optional) The next step to execute
          following this dialog node.
    :param str title: (optional) A human-readable name for the dialog node. If the
          node is included in disambiguation, this title is used to populate the **label**
          property of the corresponding suggestion in the `suggestion` response type
          (unless it is overridden by the **user_label** property). The title is also used
          to populate the **topic** property in the `connect_to_agent` response type.
          This string can contain only Unicode alphanumeric, space, underscore, hyphen,
          and dot characters.
    :param str type: (optional) How the dialog node is processed.
    :param str event_name: (optional) How an `event_handler` node is processed.
    :param str variable: (optional) The location in the dialog context where output
          is stored.
    :param List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions to be invoked by the dialog node.
    :param str digress_in: (optional) Whether this top-level dialog node can be
          digressed into.
    :param str digress_out: (optional) Whether this dialog node can be returned to
          after a digression.
    :param str digress_out_slots: (optional) Whether the user can digress to
          top-level nodes while filling out slots.
    :param str user_label: (optional) A label that can be displayed externally to
          describe the purpose of the node to users. If set, this label is used to
          identify the node in disambiguation responses (overriding the value of the
          **title** property).
    :param bool disambiguation_opt_out: (optional) Whether the dialog node should be
          excluded from disambiguation suggestions. Valid only when **type**=`standard` or
          `frame`.
    :param bool disabled: (optional) For internal use only.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        dialog_node: str,
        *,
        description: Optional[str] = None,
        conditions: Optional[str] = None,
        parent: Optional[str] = None,
        previous_sibling: Optional[str] = None,
        output: Optional['DialogNodeOutput'] = None,
        context: Optional['DialogNodeContext'] = None,
        metadata: Optional[dict] = None,
        next_step: Optional['DialogNodeNextStep'] = None,
        title: Optional[str] = None,
        type: Optional[str] = None,
        event_name: Optional[str] = None,
        variable: Optional[str] = None,
        actions: Optional[List['DialogNodeAction']] = None,
        digress_in: Optional[str] = None,
        digress_out: Optional[str] = None,
        digress_out_slots: Optional[str] = None,
        user_label: Optional[str] = None,
        disambiguation_opt_out: Optional[bool] = None,
        disabled: Optional[bool] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a DialogNode object.

        :param str dialog_node: The unique ID of the dialog node. This is an
               internal identifier used to refer to the dialog node from other dialog
               nodes and in the diagnostic information included with message responses.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str description: (optional) The description of the dialog node. This
               string cannot contain carriage return, newline, or tab characters.
        :param str conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str parent: (optional) The unique ID of the parent dialog node. This
               property is omitted if the dialog node has no parent.
        :param str previous_sibling: (optional) The unique ID of the previous
               sibling dialog node. This property is omitted if the dialog node has no
               previous sibling.
        :param DialogNodeOutput output: (optional) The output of the dialog node.
               For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param DialogNodeContext context: (optional) The context for the dialog
               node.
        :param dict metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute
               following this dialog node.
        :param str title: (optional) A human-readable name for the dialog node. If
               the node is included in disambiguation, this title is used to populate the
               **label** property of the corresponding suggestion in the `suggestion`
               response type (unless it is overridden by the **user_label** property). The
               title is also used to populate the **topic** property in the
               `connect_to_agent` response type.
               This string can contain only Unicode alphanumeric, space, underscore,
               hyphen, and dot characters.
        :param str type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where
               output is stored.
        :param List[DialogNodeAction] actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str digress_in: (optional) Whether this top-level dialog node can be
               digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned
               to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to
               top-level nodes while filling out slots.
        :param str user_label: (optional) A label that can be displayed externally
               to describe the purpose of the node to users. If set, this label is used to
               identify the node in disambiguation responses (overriding the value of the
               **title** property).
        :param bool disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions. Valid only when
               **type**=`standard` or `frame`.
        """
        self.dialog_node = dialog_node
        self.description = description
        self.conditions = conditions
        self.parent = parent
        self.previous_sibling = previous_sibling
        self.output = output
        self.context = context
        self.metadata = metadata
        self.next_step = next_step
        self.title = title
        self.type = type
        self.event_name = event_name
        self.variable = variable
        self.actions = actions
        self.digress_in = digress_in
        self.digress_out = digress_out
        self.digress_out_slots = digress_out_slots
        self.user_label = user_label
        self.disambiguation_opt_out = disambiguation_opt_out
        self.disabled = disabled
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNode':
        """Initialize a DialogNode object from a json dictionary."""
        args = {}
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in DialogNode JSON'
            )
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (conditions := _dict.get('conditions')) is not None:
            args['conditions'] = conditions
        if (parent := _dict.get('parent')) is not None:
            args['parent'] = parent
        if (previous_sibling := _dict.get('previous_sibling')) is not None:
            args['previous_sibling'] = previous_sibling
        if (output := _dict.get('output')) is not None:
            args['output'] = DialogNodeOutput.from_dict(output)
        if (context := _dict.get('context')) is not None:
            args['context'] = DialogNodeContext.from_dict(context)
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (next_step := _dict.get('next_step')) is not None:
            args['next_step'] = DialogNodeNextStep.from_dict(next_step)
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (event_name := _dict.get('event_name')) is not None:
            args['event_name'] = event_name
        if (variable := _dict.get('variable')) is not None:
            args['variable'] = variable
        if (actions := _dict.get('actions')) is not None:
            args['actions'] = [DialogNodeAction.from_dict(v) for v in actions]
        if (digress_in := _dict.get('digress_in')) is not None:
            args['digress_in'] = digress_in
        if (digress_out := _dict.get('digress_out')) is not None:
            args['digress_out'] = digress_out
        if (digress_out_slots := _dict.get('digress_out_slots')) is not None:
            args['digress_out_slots'] = digress_out_slots
        if (user_label := _dict.get('user_label')) is not None:
            args['user_label'] = user_label
        if (disambiguation_opt_out :=
                _dict.get('disambiguation_opt_out')) is not None:
            args['disambiguation_opt_out'] = disambiguation_opt_out
        if (disabled := _dict.get('disabled')) is not None:
            args['disabled'] = disabled
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNode object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = self.conditions
        if hasattr(self, 'parent') and self.parent is not None:
            _dict['parent'] = self.parent
        if hasattr(self,
                   'previous_sibling') and self.previous_sibling is not None:
            _dict['previous_sibling'] = self.previous_sibling
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
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'next_step') and self.next_step is not None:
            if isinstance(self.next_step, dict):
                _dict['next_step'] = self.next_step
            else:
                _dict['next_step'] = self.next_step.to_dict()
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'event_name') and self.event_name is not None:
            _dict['event_name'] = self.event_name
        if hasattr(self, 'variable') and self.variable is not None:
            _dict['variable'] = self.variable
        if hasattr(self, 'actions') and self.actions is not None:
            actions_list = []
            for v in self.actions:
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
        if hasattr(self, 'digress_in') and self.digress_in is not None:
            _dict['digress_in'] = self.digress_in
        if hasattr(self, 'digress_out') and self.digress_out is not None:
            _dict['digress_out'] = self.digress_out
        if hasattr(self,
                   'digress_out_slots') and self.digress_out_slots is not None:
            _dict['digress_out_slots'] = self.digress_out_slots
        if hasattr(self, 'user_label') and self.user_label is not None:
            _dict['user_label'] = self.user_label
        if hasattr(self, 'disambiguation_opt_out'
                  ) and self.disambiguation_opt_out is not None:
            _dict['disambiguation_opt_out'] = self.disambiguation_opt_out
        if hasattr(self, 'disabled') and getattr(self, 'disabled') is not None:
            _dict['disabled'] = getattr(self, 'disabled')
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNode object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNode') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNode') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        How the dialog node is processed.
        """

        STANDARD = 'standard'
        EVENT_HANDLER = 'event_handler'
        FRAME = 'frame'
        SLOT = 'slot'
        RESPONSE_CONDITION = 'response_condition'
        FOLDER = 'folder'

    class EventNameEnum(str, Enum):
        """
        How an `event_handler` node is processed.
        """

        FOCUS = 'focus'
        INPUT = 'input'
        FILLED = 'filled'
        VALIDATE = 'validate'
        FILLED_MULTIPLE = 'filled_multiple'
        GENERIC = 'generic'
        NOMATCH = 'nomatch'
        NOMATCH_RESPONSES_DEPLETED = 'nomatch_responses_depleted'
        DIGRESSION_RETURN_PROMPT = 'digression_return_prompt'

    class DigressInEnum(str, Enum):
        """
        Whether this top-level dialog node can be digressed into.
        """

        NOT_AVAILABLE = 'not_available'
        RETURNS = 'returns'
        DOES_NOT_RETURN = 'does_not_return'

    class DigressOutEnum(str, Enum):
        """
        Whether this dialog node can be returned to after a digression.
        """

        ALLOW_RETURNING = 'allow_returning'
        ALLOW_ALL = 'allow_all'
        ALLOW_ALL_NEVER_RETURN = 'allow_all_never_return'

    class DigressOutSlotsEnum(str, Enum):
        """
        Whether the user can digress to top-level nodes while filling out slots.
        """

        NOT_ALLOWED = 'not_allowed'
        ALLOW_RETURNING = 'allow_returning'
        ALLOW_ALL = 'allow_all'


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
        CLOUD_FUNCTION = 'cloud_function'
        WEB_ACTION = 'web_action'
        WEBHOOK = 'webhook'


class DialogNodeCollection:
    """
    An array of dialog nodes.

    :param List[DialogNode] dialog_nodes: An array of objects describing the dialog
          nodes defined for the workspace.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        dialog_nodes: List['DialogNode'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a DialogNodeCollection object.

        :param List[DialogNode] dialog_nodes: An array of objects describing the
               dialog nodes defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.dialog_nodes = dialog_nodes
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeCollection':
        """Initialize a DialogNodeCollection object from a json dictionary."""
        args = {}
        if (dialog_nodes := _dict.get('dialog_nodes')) is not None:
            args['dialog_nodes'] = [
                DialogNode.from_dict(v) for v in dialog_nodes
            ]
        else:
            raise ValueError(
                'Required property \'dialog_nodes\' not present in DialogNodeCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in DialogNodeCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_nodes') and self.dialog_nodes is not None:
            dialog_nodes_list = []
            for v in self.dialog_nodes:
                if isinstance(v, dict):
                    dialog_nodes_list.append(v)
                else:
                    dialog_nodes_list.append(v.to_dict())
            _dict['dialog_nodes'] = dialog_nodes_list
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
        """Return a `str` version of this DialogNodeCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeContext:
    """
    The context for the dialog node.

    :param dict integrations: (optional) Context data intended for specific
          integrations.

    This type supports additional properties of type object. Any context variable.
    """

    # The set of defined properties for the class
    _properties = frozenset(['integrations'])

    def __init__(
        self,
        *,
        integrations: Optional[dict] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a DialogNodeContext object.

        :param dict integrations: (optional) Context data intended for specific
               integrations.
        :param object **kwargs: (optional) Any context variable.
        """
        self.integrations = integrations
        for k, v in kwargs.items():
            if k not in DialogNodeContext._properties:
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
    def from_dict(cls, _dict: Dict) -> 'DialogNodeContext':
        """Initialize a DialogNodeContext object from a json dictionary."""
        args = {}
        if (integrations := _dict.get('integrations')) is not None:
            args['integrations'] = integrations
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
        """Initialize a DialogNodeContext object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'integrations') and self.integrations is not None:
            _dict['integrations'] = self.integrations
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeContext._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of DialogNodeContext in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeContext._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of DialogNodeContext"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeContext._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in DialogNodeContext._properties:
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
        """Return a `str` version of this DialogNodeContext object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeContext') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeContext') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeNextStep:
    """
    The next step to execute following this dialog node.

    :param str behavior: What happens after the dialog node completes. The valid
          values depend on the node type:
          - The following values are valid for any node:
            - `get_user_input`
            - `skip_user_input`
            - `jump_to`
          - If the node is of type `event_handler` and its parent node is of type `slot`
          or `frame`, additional values are also valid:
            - if **event_name**=`filled` and the type of the parent node is `slot`:
              - `reprompt`
              - `skip_all_slots`
          - if **event_name**=`nomatch` and the type of the parent node is `slot`:
              - `reprompt`
              - `skip_slot`
              - `skip_all_slots`
          - if **event_name**=`generic` and the type of the parent node is `frame`:
              - `reprompt`
              - `skip_slot`
              - `skip_all_slots`
               If you specify `jump_to`, then you must also specify a value for the
          `dialog_node` property.
    :param str dialog_node: (optional) The unique ID of the dialog node to process
          next. This parameter is required if **behavior**=`jump_to`.
    :param str selector: (optional) Which part of the dialog node to process next.
    """

    def __init__(
        self,
        behavior: str,
        *,
        dialog_node: Optional[str] = None,
        selector: Optional[str] = None,
    ) -> None:
        """
        Initialize a DialogNodeNextStep object.

        :param str behavior: What happens after the dialog node completes. The
               valid values depend on the node type:
               - The following values are valid for any node:
                 - `get_user_input`
                 - `skip_user_input`
                 - `jump_to`
               - If the node is of type `event_handler` and its parent node is of type
               `slot` or `frame`, additional values are also valid:
                 - if **event_name**=`filled` and the type of the parent node is `slot`:
                   - `reprompt`
                   - `skip_all_slots`
               - if **event_name**=`nomatch` and the type of the parent node is `slot`:
                   - `reprompt`
                   - `skip_slot`
                   - `skip_all_slots`
               - if **event_name**=`generic` and the type of the parent node is `frame`:
                   - `reprompt`
                   - `skip_slot`
                   - `skip_all_slots`
                    If you specify `jump_to`, then you must also specify a value for the
               `dialog_node` property.
        :param str dialog_node: (optional) The unique ID of the dialog node to
               process next. This parameter is required if **behavior**=`jump_to`.
        :param str selector: (optional) Which part of the dialog node to process
               next.
        """
        self.behavior = behavior
        self.dialog_node = dialog_node
        self.selector = selector

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeNextStep':
        """Initialize a DialogNodeNextStep object from a json dictionary."""
        args = {}
        if (behavior := _dict.get('behavior')) is not None:
            args['behavior'] = behavior
        else:
            raise ValueError(
                'Required property \'behavior\' not present in DialogNodeNextStep JSON'
            )
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        if (selector := _dict.get('selector')) is not None:
            args['selector'] = selector
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeNextStep object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'behavior') and self.behavior is not None:
            _dict['behavior'] = self.behavior
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'selector') and self.selector is not None:
            _dict['selector'] = self.selector
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeNextStep object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeNextStep') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeNextStep') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class BehaviorEnum(str, Enum):
        """
        What happens after the dialog node completes. The valid values depend on the node
        type:
        - The following values are valid for any node:
          - `get_user_input`
          - `skip_user_input`
          - `jump_to`
        - If the node is of type `event_handler` and its parent node is of type `slot` or
        `frame`, additional values are also valid:
          - if **event_name**=`filled` and the type of the parent node is `slot`:
            - `reprompt`
            - `skip_all_slots`
        - if **event_name**=`nomatch` and the type of the parent node is `slot`:
            - `reprompt`
            - `skip_slot`
            - `skip_all_slots`
        - if **event_name**=`generic` and the type of the parent node is `frame`:
            - `reprompt`
            - `skip_slot`
            - `skip_all_slots`
             If you specify `jump_to`, then you must also specify a value for the
        `dialog_node` property.
        """

        GET_USER_INPUT = 'get_user_input'
        SKIP_USER_INPUT = 'skip_user_input'
        JUMP_TO = 'jump_to'
        REPROMPT = 'reprompt'
        SKIP_SLOT = 'skip_slot'
        SKIP_ALL_SLOTS = 'skip_all_slots'

    class SelectorEnum(str, Enum):
        """
        Which part of the dialog node to process next.
        """

        CONDITION = 'condition'
        CLIENT = 'client'
        USER_INPUT = 'user_input'
        BODY = 'body'


class DialogNodeOutput:
    """
    The output of the dialog node. For more information about how to specify dialog node
    output, see the
    [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-overview#dialog-overview-responses).

    :param List[DialogNodeOutputGeneric] generic: (optional) An array of objects
          describing the output defined for the dialog node.
    :param dict integrations: (optional) Output intended for specific integrations.
          For more information, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-responses-json).
    :param DialogNodeOutputModifiers modifiers: (optional) Options that modify how
          specified output is handled.

    This type supports additional properties of type object. Any additional data included
    in the dialog node output.
    """

    # The set of defined properties for the class
    _properties = frozenset(['generic', 'integrations', 'modifiers'])

    def __init__(
        self,
        *,
        generic: Optional[List['DialogNodeOutputGeneric']] = None,
        integrations: Optional[dict] = None,
        modifiers: Optional['DialogNodeOutputModifiers'] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a DialogNodeOutput object.

        :param List[DialogNodeOutputGeneric] generic: (optional) An array of
               objects describing the output defined for the dialog node.
        :param dict integrations: (optional) Output intended for specific
               integrations. For more information, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-dialog-responses-json).
        :param DialogNodeOutputModifiers modifiers: (optional) Options that modify
               how specified output is handled.
        :param object **kwargs: (optional) Any additional data included in the
               dialog node output.
        """
        self.generic = generic
        self.integrations = integrations
        self.modifiers = modifiers
        for k, v in kwargs.items():
            if k not in DialogNodeOutput._properties:
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
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutput':
        """Initialize a DialogNodeOutput object from a json dictionary."""
        args = {}
        if (generic := _dict.get('generic')) is not None:
            args['generic'] = [
                DialogNodeOutputGeneric.from_dict(v) for v in generic
            ]
        if (integrations := _dict.get('integrations')) is not None:
            args['integrations'] = integrations
        if (modifiers := _dict.get('modifiers')) is not None:
            args['modifiers'] = DialogNodeOutputModifiers.from_dict(modifiers)
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
        """Initialize a DialogNodeOutput object from a json dictionary."""
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
        if hasattr(self, 'integrations') and self.integrations is not None:
            _dict['integrations'] = self.integrations
        if hasattr(self, 'modifiers') and self.modifiers is not None:
            if isinstance(self.modifiers, dict):
                _dict['modifiers'] = self.modifiers
            else:
                _dict['modifiers'] = self.modifiers.to_dict()
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeOutput._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of DialogNodeOutput in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeOutput._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of DialogNodeOutput"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in DialogNodeOutput._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in DialogNodeOutput._properties:
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
        """Return a `str` version of this DialogNodeOutput object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeOutput') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeOutput') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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


class DialogNodeOutputGeneric:
    """
    DialogNodeOutputGeneric.

    """

    def __init__(self,) -> None:
        """
        Initialize a DialogNodeOutputGeneric object.

        """
        msg = "Cannot instantiate base class. Instead, instantiate one of the defined subclasses: {0}".format(
            ", ".join([
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeText',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypePause',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe'
            ]))
        raise Exception(msg)

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputGeneric':
        """Initialize a DialogNodeOutputGeneric object from a json dictionary."""
        disc_class = cls._get_class_by_discriminator(_dict)
        if disc_class != cls:
            return disc_class.from_dict(_dict)
        msg = "Cannot convert dictionary into an instance of base class 'DialogNodeOutputGeneric'. The discriminator value should map to a valid subclass: {1}".format(
            ", ".join([
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeText',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypePause',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio',
                'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe'
            ]))
        raise Exception(msg)

    @classmethod
    def _from_dict(cls, _dict: Dict):
        """Initialize a DialogNodeOutputGeneric object from a json dictionary."""
        return cls.from_dict(_dict)

    @classmethod
    def _get_class_by_discriminator(cls, _dict: Dict) -> object:
        mapping = {}
        mapping[
            'audio'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio'
        mapping[
            'channel_transfer'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer'
        mapping[
            'connect_to_agent'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent'
        mapping[
            'iframe'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe'
        mapping[
            'image'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage'
        mapping[
            'option'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption'
        mapping[
            'pause'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypePause'
        mapping[
            'search_skill'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill'
        mapping[
            'text'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeText'
        mapping[
            'user_defined'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined'
        mapping[
            'video'] = 'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo'
        disc_value = _dict.get('response_type')
        if disc_value is None:
            raise ValueError(
                'Discriminator property \'response_type\' not found in DialogNodeOutputGeneric JSON'
            )
        class_name = mapping.get(disc_value, disc_value)
        try:
            disc_class = getattr(sys.modules[__name__], class_name)
        except AttributeError:
            disc_class = cls
        if isinstance(disc_class, object):
            return disc_class
        raise TypeError('%s is not a discriminator class' % class_name)


class DialogNodeOutputModifiers:
    """
    Options that modify how specified output is handled.

    :param bool overwrite: (optional) Whether values in the output will overwrite
          output values in an array specified by previously executed dialog nodes. If this
          option is set to `false`, new values will be appended to previously specified
          values.
    """

    def __init__(
        self,
        *,
        overwrite: Optional[bool] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputModifiers object.

        :param bool overwrite: (optional) Whether values in the output will
               overwrite output values in an array specified by previously executed dialog
               nodes. If this option is set to `false`, new values will be appended to
               previously specified values.
        """
        self.overwrite = overwrite

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputModifiers':
        """Initialize a DialogNodeOutputModifiers object from a json dictionary."""
        args = {}
        if (overwrite := _dict.get('overwrite')) is not None:
            args['overwrite'] = overwrite
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputModifiers object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'overwrite') and self.overwrite is not None:
            _dict['overwrite'] = self.overwrite
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this DialogNodeOutputModifiers object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeOutputModifiers') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeOutputModifiers') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputOptionsElement:
    """
    DialogNodeOutputOptionsElement.

    :param str label: The user-facing label for the option.
    :param DialogNodeOutputOptionsElementValue value: An object defining the message
          input to be sent to the Watson Assistant service if the user selects the
          corresponding option.
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
               message input to be sent to the Watson Assistant service if the user
               selects the corresponding option.
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
    An object defining the message input to be sent to the Watson Assistant service if the
    user selects the corresponding option.

    :param MessageInput input: (optional) An input object that includes the input
          text.
    :param List[RuntimeIntent] intents: (optional) An array of intents to be used
          while processing the input.
          **Note:** This property is supported for backward compatibility with
          applications that use the v1 **Get response to user input** method.
    :param List[RuntimeEntity] entities: (optional) An array of entities to be used
          while processing the user input.
          **Note:** This property is supported for backward compatibility with
          applications that use the v1 **Get response to user input** method.
    """

    def __init__(
        self,
        *,
        input: Optional['MessageInput'] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputOptionsElementValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param List[RuntimeIntent] intents: (optional) An array of intents to be
               used while processing the input.
               **Note:** This property is supported for backward compatibility with
               applications that use the v1 **Get response to user input** method.
        :param List[RuntimeEntity] entities: (optional) An array of entities to be
               used while processing the user input.
               **Note:** This property is supported for backward compatibility with
               applications that use the v1 **Get response to user input** method.
        """
        self.input = input
        self.intents = intents
        self.entities = entities

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputOptionsElementValue':
        """Initialize a DialogNodeOutputOptionsElementValue object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
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


class DialogNodeOutputTextValuesElement:
    """
    DialogNodeOutputTextValuesElement.

    :param str text: (optional) The text of a response. This string can include
          newline characters (`\n`), Markdown tagging, or other special characters, if
          supported by the channel.
    """

    def __init__(
        self,
        *,
        text: Optional[str] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputTextValuesElement object.

        :param str text: (optional) The text of a response. This string can include
               newline characters (`\n`), Markdown tagging, or other special characters,
               if supported by the channel.
        """
        self.text = text

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeOutputTextValuesElement':
        """Initialize a DialogNodeOutputTextValuesElement object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputTextValuesElement object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputTextValuesElement object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeOutputTextValuesElement') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeOutputTextValuesElement') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeVisitedDetails:
    """
    DialogNodeVisitedDetails.

    :param str dialog_node: (optional) The unique ID of a dialog node that was
          triggered during processing of the input message.
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
        Initialize a DialogNodeVisitedDetails object.

        :param str dialog_node: (optional) The unique ID of a dialog node that was
               triggered during processing of the input message.
        :param str title: (optional) The title of the dialog node.
        :param str conditions: (optional) The conditions that trigger the dialog
               node.
        """
        self.dialog_node = dialog_node
        self.title = title
        self.conditions = conditions

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogNodeVisitedDetails':
        """Initialize a DialogNodeVisitedDetails object from a json dictionary."""
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
        """Initialize a DialogNodeVisitedDetails object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeVisitedDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'DialogNodeVisitedDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'DialogNodeVisitedDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestion:
    """
    DialogSuggestion.

    :param str label: The user-facing label for the disambiguation option. This
          label is taken from the **title** or **user_label** property of the
          corresponding dialog node.
    :param DialogSuggestionValue value: An object defining the message input,
          intents, and entities to be sent to the Watson Assistant service if the user
          selects the corresponding disambiguation option.
           **Note:** These properties must be included in the request body of the next
          message sent to the assistant. Do not modify or remove any of the included
          properties.
    :param dict output: (optional) The dialog output that will be returned from the
          Watson Assistant service if the user selects the corresponding option.
    :param str dialog_node: (optional) The unique ID of the dialog node that the
          **label** property is taken from. The **label** property is populated using the
          value of the dialog node's **title** or **user_label** property.
    """

    def __init__(
        self,
        label: str,
        value: 'DialogSuggestionValue',
        *,
        output: Optional[dict] = None,
        dialog_node: Optional[str] = None,
    ) -> None:
        """
        Initialize a DialogSuggestion object.

        :param str label: The user-facing label for the disambiguation option. This
               label is taken from the **title** or **user_label** property of the
               corresponding dialog node.
        :param DialogSuggestionValue value: An object defining the message input,
               intents, and entities to be sent to the Watson Assistant service if the
               user selects the corresponding disambiguation option.
                **Note:** These properties must be included in the request body of the
               next message sent to the assistant. Do not modify or remove any of the
               included properties.
        :param dict output: (optional) The dialog output that will be returned from
               the Watson Assistant service if the user selects the corresponding option.
        :param str dialog_node: (optional) The unique ID of the dialog node that
               the **label** property is taken from. The **label** property is populated
               using the value of the dialog node's **title** or **user_label** property.
        """
        self.label = label
        self.value = value
        self.output = output
        self.dialog_node = dialog_node

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
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
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
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
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
    An object defining the message input, intents, and entities to be sent to the Watson
    Assistant service if the user selects the corresponding disambiguation option.
     **Note:** These properties must be included in the request body of the next message
    sent to the assistant. Do not modify or remove any of the included properties.

    :param MessageInput input: (optional) An input object that includes the input
          text.
    :param List[RuntimeIntent] intents: (optional) An array of intents to be sent
          along with the user input.
    :param List[RuntimeEntity] entities: (optional) An array of entities to be sent
          along with the user input.
    """

    def __init__(
        self,
        *,
        input: Optional['MessageInput'] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
    ) -> None:
        """
        Initialize a DialogSuggestionValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param List[RuntimeIntent] intents: (optional) An array of intents to be
               sent along with the user input.
        :param List[RuntimeEntity] entities: (optional) An array of entities to be
               sent along with the user input.
        """
        self.input = input
        self.intents = intents
        self.entities = entities

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'DialogSuggestionValue':
        """Initialize a DialogSuggestionValue object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
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


class Entity:
    """
    Entity.

    :param str entity: The name of the entity. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, and hyphen characters.
          - If you specify an entity name beginning with the reserved prefix `sys-`, it
          must be the name of a system entity that you want to enable. (Any entity content
          specified with the request is ignored.).
    :param str description: (optional) The description of the entity. This string
          cannot contain carriage return, newline, or tab characters.
    :param dict metadata: (optional) Any metadata related to the entity.
    :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the
          entity.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param List[Value] values: (optional) An array of objects describing the entity
          values.
    """

    def __init__(
        self,
        entity: str,
        *,
        description: Optional[str] = None,
        metadata: Optional[dict] = None,
        fuzzy_match: Optional[bool] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        values: Optional[List['Value']] = None,
    ) -> None:
        """
        Initialize a Entity object.

        :param str entity: The name of the entity. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, and hyphen
               characters.
               - If you specify an entity name beginning with the reserved prefix `sys-`,
               it must be the name of a system entity that you want to enable. (Any entity
               content specified with the request is ignored.).
        :param str description: (optional) The description of the entity. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict metadata: (optional) Any metadata related to the entity.
        :param bool fuzzy_match: (optional) Whether to use fuzzy matching for the
               entity.
        :param List[Value] values: (optional) An array of objects describing the
               entity values.
        """
        self.entity = entity
        self.description = description
        self.metadata = metadata
        self.fuzzy_match = fuzzy_match
        self.created = created
        self.updated = updated
        self.values = values

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Entity':
        """Initialize a Entity object from a json dictionary."""
        args = {}
        if (entity := _dict.get('entity')) is not None:
            args['entity'] = entity
        else:
            raise ValueError(
                'Required property \'entity\' not present in Entity JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (fuzzy_match := _dict.get('fuzzy_match')) is not None:
            args['fuzzy_match'] = fuzzy_match
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (values := _dict.get('values')) is not None:
            args['values'] = [Value.from_dict(v) for v in values]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Entity object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'fuzzy_match') and self.fuzzy_match is not None:
            _dict['fuzzy_match'] = self.fuzzy_match
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'values') and self.values is not None:
            values_list = []
            for v in self.values:
                if isinstance(v, dict):
                    values_list.append(v)
                else:
                    values_list.append(v.to_dict())
            _dict['values'] = values_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Entity object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Entity') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Entity') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityCollection:
    """
    An array of objects describing the entities for the workspace.

    :param List[Entity] entities: An array of objects describing the entities
          defined for the workspace.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        entities: List['Entity'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a EntityCollection object.

        :param List[Entity] entities: An array of objects describing the entities
               defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.entities = entities
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityCollection':
        """Initialize a EntityCollection object from a json dictionary."""
        args = {}
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [Entity.from_dict(v) for v in entities]
        else:
            raise ValueError(
                'Required property \'entities\' not present in EntityCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in EntityCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityCollection object from a json dictionary."""
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
        """Return a `str` version of this EntityCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntityCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMention:
    """
    An object describing a contextual entity mention.

    :param str text: The text of the user input example.
    :param str intent: The name of the intent.
    :param List[int] location: An array of zero-based character offsets that
          indicate where the entity mentions begin and end in the input text.
    """

    def __init__(
        self,
        text: str,
        intent: str,
        location: List[int],
    ) -> None:
        """
        Initialize a EntityMention object.

        :param str text: The text of the user input example.
        :param str intent: The name of the intent.
        :param List[int] location: An array of zero-based character offsets that
               indicate where the entity mentions begin and end in the input text.
        """
        self.text = text
        self.intent = intent
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityMention':
        """Initialize a EntityMention object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in EntityMention JSON')
        if (intent := _dict.get('intent')) is not None:
            args['intent'] = intent
        else:
            raise ValueError(
                'Required property \'intent\' not present in EntityMention JSON'
            )
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError(
                'Required property \'location\' not present in EntityMention JSON'
            )
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
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
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


class EntityMentionCollection:
    """
    EntityMentionCollection.

    :param List[EntityMention] examples: An array of objects describing the entity
          mentions defined for an entity.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        examples: List['EntityMention'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a EntityMentionCollection object.

        :param List[EntityMention] examples: An array of objects describing the
               entity mentions defined for an entity.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'EntityMentionCollection':
        """Initialize a EntityMentionCollection object from a json dictionary."""
        args = {}
        if (examples := _dict.get('examples')) is not None:
            args['examples'] = [EntityMention.from_dict(v) for v in examples]
        else:
            raise ValueError(
                'Required property \'examples\' not present in EntityMentionCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in EntityMentionCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMentionCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            examples_list = []
            for v in self.examples:
                if isinstance(v, dict):
                    examples_list.append(v)
                else:
                    examples_list.append(v.to_dict())
            _dict['examples'] = examples_list
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
        """Return a `str` version of this EntityMentionCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'EntityMentionCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'EntityMentionCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Example:
    """
    Example.

    :param str text: The text of a user input example. This string must conform to
          the following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param List[Mention] mentions: (optional) An array of contextual entity
          mentions.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        text: str,
        *,
        mentions: Optional[List['Mention']] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Example object.

        :param str text: The text of a user input example. This string must conform
               to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[Mention] mentions: (optional) An array of contextual entity
               mentions.
        """
        self.text = text
        self.mentions = mentions
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Example':
        """Initialize a Example object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        else:
            raise ValueError(
                'Required property \'text\' not present in Example JSON')
        if (mentions := _dict.get('mentions')) is not None:
            args['mentions'] = [Mention.from_dict(v) for v in mentions]
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Example object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'mentions') and self.mentions is not None:
            mentions_list = []
            for v in self.mentions:
                if isinstance(v, dict):
                    mentions_list.append(v)
                else:
                    mentions_list.append(v.to_dict())
            _dict['mentions'] = mentions_list
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Example object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Example') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Example') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExampleCollection:
    """
    ExampleCollection.

    :param List[Example] examples: An array of objects describing the examples
          defined for the intent.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        examples: List['Example'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a ExampleCollection object.

        :param List[Example] examples: An array of objects describing the examples
               defined for the intent.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ExampleCollection':
        """Initialize a ExampleCollection object from a json dictionary."""
        args = {}
        if (examples := _dict.get('examples')) is not None:
            args['examples'] = [Example.from_dict(v) for v in examples]
        else:
            raise ValueError(
                'Required property \'examples\' not present in ExampleCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ExampleCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExampleCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            examples_list = []
            for v in self.examples:
                if isinstance(v, dict):
                    examples_list.append(v)
                else:
                    examples_list.append(v.to_dict())
            _dict['examples'] = examples_list
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
        """Return a `str` version of this ExampleCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ExampleCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ExampleCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Intent:
    """
    Intent.

    :param str intent: The name of the intent. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
          characters.
          - It cannot begin with the reserved prefix `sys-`.
    :param str description: (optional) The description of the intent. This string
          cannot contain carriage return, newline, or tab characters.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param List[Example] examples: (optional) An array of user input examples for
          the intent.
    """

    def __init__(
        self,
        intent: str,
        *,
        description: Optional[str] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        examples: Optional[List['Example']] = None,
    ) -> None:
        """
        Initialize a Intent object.

        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param List[Example] examples: (optional) An array of user input examples
               for the intent.
        """
        self.intent = intent
        self.description = description
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Intent':
        """Initialize a Intent object from a json dictionary."""
        args = {}
        if (intent := _dict.get('intent')) is not None:
            args['intent'] = intent
        else:
            raise ValueError(
                'Required property \'intent\' not present in Intent JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (examples := _dict.get('examples')) is not None:
            args['examples'] = [Example.from_dict(v) for v in examples]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Intent object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'examples') and self.examples is not None:
            examples_list = []
            for v in self.examples:
                if isinstance(v, dict):
                    examples_list.append(v)
                else:
                    examples_list.append(v.to_dict())
            _dict['examples'] = examples_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Intent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Intent') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Intent') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IntentCollection:
    """
    IntentCollection.

    :param List[Intent] intents: An array of objects describing the intents defined
          for the workspace.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        intents: List['Intent'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a IntentCollection object.

        :param List[Intent] intents: An array of objects describing the intents
               defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.intents = intents
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'IntentCollection':
        """Initialize a IntentCollection object from a json dictionary."""
        args = {}
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [Intent.from_dict(v) for v in intents]
        else:
            raise ValueError(
                'Required property \'intents\' not present in IntentCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in IntentCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntentCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intents') and self.intents is not None:
            intents_list = []
            for v in self.intents:
                if isinstance(v, dict):
                    intents_list.append(v)
                else:
                    intents_list.append(v.to_dict())
            _dict['intents'] = intents_list
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
        """Return a `str` version of this IntentCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'IntentCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'IntentCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Log:
    """
    Log.

    :param MessageRequest request: A request sent to the workspace, including the
          user input and context.
    :param MessageResponse response: The response sent by the workspace, including
          the output text, detected intents and entities, and context.
    :param str log_id: A unique identifier for the logged event.
    :param str request_timestamp: The timestamp for receipt of the message.
    :param str response_timestamp: The timestamp for the system response to the
          message.
    :param str workspace_id: The unique identifier of the workspace where the
          request was made.
    :param str language: The language of the workspace where the message request was
          made.
    """

    def __init__(
        self,
        request: 'MessageRequest',
        response: 'MessageResponse',
        log_id: str,
        request_timestamp: str,
        response_timestamp: str,
        workspace_id: str,
        language: str,
    ) -> None:
        """
        Initialize a Log object.

        :param MessageRequest request: A request sent to the workspace, including
               the user input and context.
        :param MessageResponse response: The response sent by the workspace,
               including the output text, detected intents and entities, and context.
        :param str log_id: A unique identifier for the logged event.
        :param str request_timestamp: The timestamp for receipt of the message.
        :param str response_timestamp: The timestamp for the system response to the
               message.
        :param str workspace_id: The unique identifier of the workspace where the
               request was made.
        :param str language: The language of the workspace where the message
               request was made.
        """
        self.request = request
        self.response = response
        self.log_id = log_id
        self.request_timestamp = request_timestamp
        self.response_timestamp = response_timestamp
        self.workspace_id = workspace_id
        self.language = language

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Log':
        """Initialize a Log object from a json dictionary."""
        args = {}
        if (request := _dict.get('request')) is not None:
            args['request'] = MessageRequest.from_dict(request)
        else:
            raise ValueError(
                'Required property \'request\' not present in Log JSON')
        if (response := _dict.get('response')) is not None:
            args['response'] = MessageResponse.from_dict(response)
        else:
            raise ValueError(
                'Required property \'response\' not present in Log JSON')
        if (log_id := _dict.get('log_id')) is not None:
            args['log_id'] = log_id
        else:
            raise ValueError(
                'Required property \'log_id\' not present in Log JSON')
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
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in Log JSON')
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in Log JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Log object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
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
        if hasattr(self, 'log_id') and self.log_id is not None:
            _dict['log_id'] = self.log_id
        if hasattr(self,
                   'request_timestamp') and self.request_timestamp is not None:
            _dict['request_timestamp'] = self.request_timestamp
        if hasattr(
                self,
                'response_timestamp') and self.response_timestamp is not None:
            _dict['response_timestamp'] = self.response_timestamp
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
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


class LogMessage:
    """
    Log message details.

    :param str level: The severity of the log message.
    :param str msg: The text of the log message.
    :param str code: A code that indicates the category to which the error message
          belongs.
    :param LogMessageSource source: (optional) An object that identifies the dialog
          element that generated the error message.
    """

    def __init__(
        self,
        level: str,
        msg: str,
        code: str,
        *,
        source: Optional['LogMessageSource'] = None,
    ) -> None:
        """
        Initialize a LogMessage object.

        :param str level: The severity of the log message.
        :param str msg: The text of the log message.
        :param str code: A code that indicates the category to which the error
               message belongs.
        :param LogMessageSource source: (optional) An object that identifies the
               dialog element that generated the error message.
        """
        self.level = level
        self.msg = msg
        self.code = code
        self.source = source

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessage':
        """Initialize a LogMessage object from a json dictionary."""
        args = {}
        if (level := _dict.get('level')) is not None:
            args['level'] = level
        else:
            raise ValueError(
                'Required property \'level\' not present in LogMessage JSON')
        if (msg := _dict.get('msg')) is not None:
            args['msg'] = msg
        else:
            raise ValueError(
                'Required property \'msg\' not present in LogMessage JSON')
        if (code := _dict.get('code')) is not None:
            args['code'] = code
        else:
            raise ValueError(
                'Required property \'code\' not present in LogMessage JSON')
        if (source := _dict.get('source')) is not None:
            args['source'] = LogMessageSource.from_dict(source)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessage object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'msg') and self.msg is not None:
            _dict['msg'] = self.msg
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
        """Return a `str` version of this LogMessage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessage') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessage') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LevelEnum(str, Enum):
        """
        The severity of the log message.
        """

        INFO = 'info'
        ERROR = 'error'
        WARN = 'warn'


class LogMessageSource:
    """
    An object that identifies the dialog element that generated the error message.

    :param str type: (optional) A string that indicates the type of dialog element
          that generated the error message.
    :param str dialog_node: (optional) The unique identifier of the dialog node that
          generated the error message.
    """

    def __init__(
        self,
        *,
        type: Optional[str] = None,
        dialog_node: Optional[str] = None,
    ) -> None:
        """
        Initialize a LogMessageSource object.

        :param str type: (optional) A string that indicates the type of dialog
               element that generated the error message.
        :param str dialog_node: (optional) The unique identifier of the dialog node
               that generated the error message.
        """
        self.type = type
        self.dialog_node = dialog_node

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogMessageSource':
        """Initialize a LogMessageSource object from a json dictionary."""
        args = {}
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessageSource object from a json dictionary."""
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
        """Return a `str` version of this LogMessageSource object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogMessageSource') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogMessageSource') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        A string that indicates the type of dialog element that generated the error
        message.
        """

        DIALOG_NODE = 'dialog_node'


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


class Mention:
    """
    A mention of a contextual entity.

    :param str entity: The name of the entity.
    :param List[int] location: An array of zero-based character offsets that
          indicate where the entity mentions begin and end in the input text.
    """

    def __init__(
        self,
        entity: str,
        location: List[int],
    ) -> None:
        """
        Initialize a Mention object.

        :param str entity: The name of the entity.
        :param List[int] location: An array of zero-based character offsets that
               indicate where the entity mentions begin and end in the input text.
        """
        self.entity = entity
        self.location = location

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Mention':
        """Initialize a Mention object from a json dictionary."""
        args = {}
        if (entity := _dict.get('entity')) is not None:
            args['entity'] = entity
        else:
            raise ValueError(
                'Required property \'entity\' not present in Mention JSON')
        if (location := _dict.get('location')) is not None:
            args['location'] = location
        else:
            raise ValueError(
                'Required property \'location\' not present in Mention JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Mention object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Mention object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Mention') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Mention') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextMetadata:
    """
    Metadata related to the message.

    :param str deployment: (optional) A label identifying the deployment
          environment, used for filtering log data. This string cannot contain carriage
          return, newline, or tab characters.
    :param str user_id: (optional) A string value that identifies the user who is
          interacting with the workspace. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.conversation_id**.
          **Note:** This property is the same as the **user_id** property at the root of
          the message body. If **user_id** is specified in both locations in a message
          request, the value specified at the root is used.
    """

    def __init__(
        self,
        *,
        deployment: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageContextMetadata object.

        :param str deployment: (optional) A label identifying the deployment
               environment, used for filtering log data. This string cannot contain
               carriage return, newline, or tab characters.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the workspace. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.conversation_id**.
               **Note:** This property is the same as the **user_id** property at the root
               of the message body. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        """
        self.deployment = deployment
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageContextMetadata':
        """Initialize a MessageContextMetadata object from a json dictionary."""
        args = {}
        if (deployment := _dict.get('deployment')) is not None:
            args['deployment'] = deployment
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextMetadata object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployment') and self.deployment is not None:
            _dict['deployment'] = self.deployment
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this MessageContextMetadata object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'MessageContextMetadata') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'MessageContextMetadata') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInput:
    """
    An input object that includes the input text.

    :param str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    :param bool spelling_suggestions: (optional) Whether to use spelling correction
          when processing the input. This property overrides the value of the
          **spelling_suggestions** property in the workspace settings.
    :param bool spelling_auto_correct: (optional) Whether to use autocorrection when
          processing the input. If spelling correction is used and this property is
          `false`, any suggested corrections are returned in the **suggested_text**
          property of the message response. If this property is `true`, any corrections
          are automatically applied to the user input, and the original text is returned
          in the **original_text** property of the message response. This property
          overrides the value of the **spelling_auto_correct** property in the workspace
          settings.
    :param str suggested_text: (optional) Any suggested corrections of the input
          text. This property is returned only if spelling correction is enabled and
          autocorrection is disabled.
    :param str original_text: (optional) The original user input text. This property
          is returned only if autocorrection is enabled and the user input was corrected.

    This type supports additional properties of type object. Any additional data included
    with the message input.
    """

    # The set of defined properties for the class
    _properties = frozenset([
        'text', 'spelling_suggestions', 'spelling_auto_correct',
        'suggested_text', 'original_text'
    ])

    def __init__(
        self,
        *,
        text: Optional[str] = None,
        spelling_suggestions: Optional[bool] = None,
        spelling_auto_correct: Optional[bool] = None,
        suggested_text: Optional[str] = None,
        original_text: Optional[str] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a MessageInput object.

        :param str text: (optional) The text of the user input. This string cannot
               contain carriage return, newline, or tab characters.
        :param bool spelling_suggestions: (optional) Whether to use spelling
               correction when processing the input. This property overrides the value of
               the **spelling_suggestions** property in the workspace settings.
        :param bool spelling_auto_correct: (optional) Whether to use autocorrection
               when processing the input. If spelling correction is used and this property
               is `false`, any suggested corrections are returned in the
               **suggested_text** property of the message response. If this property is
               `true`, any corrections are automatically applied to the user input, and
               the original text is returned in the **original_text** property of the
               message response. This property overrides the value of the
               **spelling_auto_correct** property in the workspace settings.
        :param object **kwargs: (optional) Any additional data included with the
               message input.
        """
        self.text = text
        self.spelling_suggestions = spelling_suggestions
        self.spelling_auto_correct = spelling_auto_correct
        self.suggested_text = suggested_text
        self.original_text = original_text
        for k, v in kwargs.items():
            if k not in MessageInput._properties:
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
    def from_dict(cls, _dict: Dict) -> 'MessageInput':
        """Initialize a MessageInput object from a json dictionary."""
        args = {}
        if (text := _dict.get('text')) is not None:
            args['text'] = text
        if (spelling_suggestions :=
                _dict.get('spelling_suggestions')) is not None:
            args['spelling_suggestions'] = spelling_suggestions
        if (spelling_auto_correct :=
                _dict.get('spelling_auto_correct')) is not None:
            args['spelling_auto_correct'] = spelling_auto_correct
        if (suggested_text := _dict.get('suggested_text')) is not None:
            args['suggested_text'] = suggested_text
        if (original_text := _dict.get('original_text')) is not None:
            args['original_text'] = original_text
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
        """Initialize a MessageInput object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'spelling_suggestions'
                  ) and self.spelling_suggestions is not None:
            _dict['spelling_suggestions'] = self.spelling_suggestions
        if hasattr(self, 'spelling_auto_correct'
                  ) and self.spelling_auto_correct is not None:
            _dict['spelling_auto_correct'] = self.spelling_auto_correct
        if hasattr(self, 'suggested_text') and getattr(
                self, 'suggested_text') is not None:
            _dict['suggested_text'] = getattr(self, 'suggested_text')
        if hasattr(self, 'original_text') and getattr(
                self, 'original_text') is not None:
            _dict['original_text'] = getattr(self, 'original_text')
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageInput._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of MessageInput in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageInput._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of MessageInput"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in MessageInput._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in MessageInput._properties:
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


class MessageRequest:
    """
    A request sent to the workspace, including the user input and context.

    :param MessageInput input: (optional) An input object that includes the input
          text.
    :param List[RuntimeIntent] intents: (optional) Intents to use when evaluating
          the user input. Include intents from the previous response to continue using
          those intents rather than trying to recognize intents in the new input.
    :param List[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :param bool alternate_intents: (optional) Whether to return more than one
          intent. A value of `true` indicates that all matching intents are returned.
    :param Context context: (optional) State information for the conversation. To
          maintain state, include the context from the previous response.
    :param OutputData output: (optional) An output object that includes the response
          to the user, the dialog nodes that were triggered, and messages from the log.
    :param List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    :param str user_id: (optional) A string value that identifies the user who is
          interacting with the workspace. The client must provide a unique identifier for
          each individual end user who accesses the application. For user-based plans,
          this user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.conversation_id**.
          **Note:** This property is the same as the **user_id** property in the context
          metadata. If **user_id** is specified in both locations in a message request,
          the value specified at the root is used.
    """

    def __init__(
        self,
        *,
        input: Optional['MessageInput'] = None,
        intents: Optional[List['RuntimeIntent']] = None,
        entities: Optional[List['RuntimeEntity']] = None,
        alternate_intents: Optional[bool] = None,
        context: Optional['Context'] = None,
        output: Optional['OutputData'] = None,
        actions: Optional[List['DialogNodeAction']] = None,
        user_id: Optional[str] = None,
    ) -> None:
        """
        Initialize a MessageRequest object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param List[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param List[RuntimeEntity] entities: (optional) Entities to use when
               evaluating the message. Include entities from the previous response to
               continue using those entities rather than detecting entities in the new
               input.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. A value of `true` indicates that all matching intents are returned.
        :param Context context: (optional) State information for the conversation.
               To maintain state, include the context from the previous response.
        :param OutputData output: (optional) An output object that includes the
               response to the user, the dialog nodes that were triggered, and messages
               from the log.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the workspace. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               user-based plans, this user ID is used to identify unique users for billing
               purposes. This string cannot contain carriage return, newline, or tab
               characters. If no value is specified in the input, **user_id** is
               automatically set to the value of **context.conversation_id**.
               **Note:** This property is the same as the **user_id** property in the
               context metadata. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        """
        self.input = input
        self.intents = intents
        self.entities = entities
        self.alternate_intents = alternate_intents
        self.context = context
        self.output = output
        self.actions = actions
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageRequest':
        """Initialize a MessageRequest object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        if (alternate_intents := _dict.get('alternate_intents')) is not None:
            args['alternate_intents'] = alternate_intents
        if (context := _dict.get('context')) is not None:
            args['context'] = Context.from_dict(context)
        if (output := _dict.get('output')) is not None:
            args['output'] = OutputData.from_dict(output)
        if (actions := _dict.get('actions')) is not None:
            args['actions'] = [DialogNodeAction.from_dict(v) for v in actions]
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
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
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'output') and self.output is not None:
            if isinstance(self.output, dict):
                _dict['output'] = self.output
            else:
                _dict['output'] = self.output.to_dict()
        if hasattr(self, 'actions') and getattr(self, 'actions') is not None:
            actions_list = []
            for v in getattr(self, 'actions'):
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
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


class MessageResponse:
    """
    The response sent by the workspace, including the output text, detected intents and
    entities, and context.

    :param MessageInput input: An input object that includes the input text.
    :param List[RuntimeIntent] intents: An array of intents recognized in the user
          input, sorted in descending order of confidence.
    :param List[RuntimeEntity] entities: An array of entities identified in the user
          input.
    :param bool alternate_intents: (optional) Whether to return more than one
          intent. A value of `true` indicates that all matching intents are returned.
    :param Context context: State information for the conversation. To maintain
          state, include the context from the previous response.
    :param OutputData output: An output object that includes the response to the
          user, the dialog nodes that were triggered, and messages from the log.
    :param List[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    :param str user_id: A string value that identifies the user who is interacting
          with the workspace. The client must provide a unique identifier for each
          individual end user who accesses the application. For user-based plans, this
          user ID is used to identify unique users for billing purposes. This string
          cannot contain carriage return, newline, or tab characters. If no value is
          specified in the input, **user_id** is automatically set to the value of
          **context.conversation_id**.
          **Note:** This property is the same as the **user_id** property in the context
          metadata. If **user_id** is specified in both locations in a message request,
          the value specified at the root is used.
    """

    def __init__(
        self,
        input: 'MessageInput',
        intents: List['RuntimeIntent'],
        entities: List['RuntimeEntity'],
        context: 'Context',
        output: 'OutputData',
        user_id: str,
        *,
        alternate_intents: Optional[bool] = None,
        actions: Optional[List['DialogNodeAction']] = None,
    ) -> None:
        """
        Initialize a MessageResponse object.

        :param MessageInput input: An input object that includes the input text.
        :param List[RuntimeIntent] intents: An array of intents recognized in the
               user input, sorted in descending order of confidence.
        :param List[RuntimeEntity] entities: An array of entities identified in the
               user input.
        :param Context context: State information for the conversation. To maintain
               state, include the context from the previous response.
        :param OutputData output: An output object that includes the response to
               the user, the dialog nodes that were triggered, and messages from the log.
        :param str user_id: A string value that identifies the user who is
               interacting with the workspace. The client must provide a unique identifier
               for each individual end user who accesses the application. For user-based
               plans, this user ID is used to identify unique users for billing purposes.
               This string cannot contain carriage return, newline, or tab characters. If
               no value is specified in the input, **user_id** is automatically set to the
               value of **context.conversation_id**.
               **Note:** This property is the same as the **user_id** property in the
               context metadata. If **user_id** is specified in both locations in a
               message request, the value specified at the root is used.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. A value of `true` indicates that all matching intents are returned.
        """
        self.input = input
        self.intents = intents
        self.entities = entities
        self.alternate_intents = alternate_intents
        self.context = context
        self.output = output
        self.actions = actions
        self.user_id = user_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'MessageResponse':
        """Initialize a MessageResponse object from a json dictionary."""
        args = {}
        if (input := _dict.get('input')) is not None:
            args['input'] = MessageInput.from_dict(input)
        else:
            raise ValueError(
                'Required property \'input\' not present in MessageResponse JSON'
            )
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [RuntimeIntent.from_dict(v) for v in intents]
        else:
            raise ValueError(
                'Required property \'intents\' not present in MessageResponse JSON'
            )
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [RuntimeEntity.from_dict(v) for v in entities]
        else:
            raise ValueError(
                'Required property \'entities\' not present in MessageResponse JSON'
            )
        if (alternate_intents := _dict.get('alternate_intents')) is not None:
            args['alternate_intents'] = alternate_intents
        if (context := _dict.get('context')) is not None:
            args['context'] = Context.from_dict(context)
        else:
            raise ValueError(
                'Required property \'context\' not present in MessageResponse JSON'
            )
        if (output := _dict.get('output')) is not None:
            args['output'] = OutputData.from_dict(output)
        else:
            raise ValueError(
                'Required property \'output\' not present in MessageResponse JSON'
            )
        if (actions := _dict.get('actions')) is not None:
            args['actions'] = [DialogNodeAction.from_dict(v) for v in actions]
        if (user_id := _dict.get('user_id')) is not None:
            args['user_id'] = user_id
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
        if hasattr(self, 'input') and self.input is not None:
            if isinstance(self.input, dict):
                _dict['input'] = self.input
            else:
                _dict['input'] = self.input.to_dict()
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
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'context') and self.context is not None:
            if isinstance(self.context, dict):
                _dict['context'] = self.context
            else:
                _dict['context'] = self.context.to_dict()
        if hasattr(self, 'output') and self.output is not None:
            if isinstance(self.output, dict):
                _dict['output'] = self.output
            else:
                _dict['output'] = self.output.to_dict()
        if hasattr(self, 'actions') and getattr(self, 'actions') is not None:
            actions_list = []
            for v in getattr(self, 'actions'):
                if isinstance(v, dict):
                    actions_list.append(v)
                else:
                    actions_list.append(v.to_dict())
            _dict['actions'] = actions_list
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


class OutputData:
    """
    An output object that includes the response to the user, the dialog nodes that were
    triggered, and messages from the log.

    :param List[str] nodes_visited: (optional) An array of the nodes that were
          triggered to create the response, in the order in which they were visited. This
          information is useful for debugging and for tracing the path taken through the
          node tree.
    :param List[DialogNodeVisitedDetails] nodes_visited_details: (optional) An array
          of objects containing detailed diagnostic information about the nodes that were
          triggered during processing of the input message. Included only if
          **nodes_visited_details** is set to `true` in the message request.
    :param List[LogMessage] log_messages: An array of up to 50 messages logged with
          the request.
    :param List[RuntimeResponseGeneric] generic: (optional) Output intended for any
          channel. It is the responsibility of the client application to implement the
          supported response types.

    This type supports additional properties of type object. Any additional data included
    with the output.
    """

    # The set of defined properties for the class
    _properties = frozenset(
        ['nodes_visited', 'nodes_visited_details', 'log_messages', 'generic'])

    def __init__(
        self,
        log_messages: List['LogMessage'],
        *,
        nodes_visited: Optional[List[str]] = None,
        nodes_visited_details: Optional[
            List['DialogNodeVisitedDetails']] = None,
        generic: Optional[List['RuntimeResponseGeneric']] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a OutputData object.

        :param List[LogMessage] log_messages: An array of up to 50 messages logged
               with the request.
        :param List[str] nodes_visited: (optional) An array of the nodes that were
               triggered to create the response, in the order in which they were visited.
               This information is useful for debugging and for tracing the path taken
               through the node tree.
        :param List[DialogNodeVisitedDetails] nodes_visited_details: (optional) An
               array of objects containing detailed diagnostic information about the nodes
               that were triggered during processing of the input message. Included only
               if **nodes_visited_details** is set to `true` in the message request.
        :param List[RuntimeResponseGeneric] generic: (optional) Output intended for
               any channel. It is the responsibility of the client application to
               implement the supported response types.
        :param object **kwargs: (optional) Any additional data included with the
               output.
        """
        self.nodes_visited = nodes_visited
        self.nodes_visited_details = nodes_visited_details
        self.log_messages = log_messages
        self.generic = generic
        for k, v in kwargs.items():
            if k not in OutputData._properties:
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
    def from_dict(cls, _dict: Dict) -> 'OutputData':
        """Initialize a OutputData object from a json dictionary."""
        args = {}
        if (nodes_visited := _dict.get('nodes_visited')) is not None:
            args['nodes_visited'] = nodes_visited
        if (nodes_visited_details :=
                _dict.get('nodes_visited_details')) is not None:
            args['nodes_visited_details'] = [
                DialogNodeVisitedDetails.from_dict(v)
                for v in nodes_visited_details
            ]
        if (log_messages := _dict.get('log_messages')) is not None:
            args['log_messages'] = [
                LogMessage.from_dict(v) for v in log_messages
            ]
        else:
            raise ValueError(
                'Required property \'log_messages\' not present in OutputData JSON'
            )
        if (generic := _dict.get('generic')) is not None:
            args['generic'] = [
                RuntimeResponseGeneric.from_dict(v) for v in generic
            ]
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
        """Initialize a OutputData object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nodes_visited') and self.nodes_visited is not None:
            _dict['nodes_visited'] = self.nodes_visited
        if hasattr(self, 'nodes_visited_details'
                  ) and self.nodes_visited_details is not None:
            nodes_visited_details_list = []
            for v in self.nodes_visited_details:
                if isinstance(v, dict):
                    nodes_visited_details_list.append(v)
                else:
                    nodes_visited_details_list.append(v.to_dict())
            _dict['nodes_visited_details'] = nodes_visited_details_list
        if hasattr(self, 'log_messages') and self.log_messages is not None:
            log_messages_list = []
            for v in self.log_messages:
                if isinstance(v, dict):
                    log_messages_list.append(v)
                else:
                    log_messages_list.append(v.to_dict())
            _dict['log_messages'] = log_messages_list
        if hasattr(self, 'generic') and self.generic is not None:
            generic_list = []
            for v in self.generic:
                if isinstance(v, dict):
                    generic_list.append(v)
                else:
                    generic_list.append(v.to_dict())
            _dict['generic'] = generic_list
        for k in [
                _k for _k in vars(self).keys()
                if _k not in OutputData._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of OutputData in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in OutputData._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of OutputData"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in OutputData._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in OutputData._properties:
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
        """Return a `str` version of this OutputData object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'OutputData') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'OutputData') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


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


class ResponseGenericChannel:
    """
    ResponseGenericChannel.

    :param str channel: (optional) A channel for which the response is intended.
           **Note:** On IBM Cloud Pak for Data, only `chat` is supported.
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
                **Note:** On IBM Cloud Pak for Data, only `chat` is supported.
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

    class ChannelEnum(str, Enum):
        """
        A channel for which the response is intended.
         **Note:** On IBM Cloud Pak for Data, only `chat` is supported.
        """

        CHAT = 'chat'
        FACEBOOK = 'facebook'
        INTERCOM = 'intercom'
        SLACK = 'slack'
        TEXT_MESSAGING = 'text_messaging'
        VOICE_TELEPHONY = 'voice_telephony'
        WHATSAPP = 'whatsapp'


class RuntimeEntity:
    """
    A term from the request that was identified as an entity.

    :param str entity: An entity detected in the input.
    :param List[int] location: (optional) An array of zero-based character offsets
          that indicate where the detected entity values begin and end in the input text.
    :param str value: The entity value that was recognized in the user input.
    :param float confidence: (optional) A decimal percentage that represents
          confidence in the recognized entity.
    :param List[CaptureGroup] groups: (optional) The recognized capture groups for
          the entity, as defined by the entity pattern.
    :param RuntimeEntityInterpretation interpretation: (optional) An object
          containing detailed information about the entity recognized in the user input.
          For more information about how system entities are interpreted, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-system-entities).
    :param List[RuntimeEntityAlternative] alternatives: (optional) An array of
          possible alternative values that the user might have intended instead of the
          value returned in the **value** property. This property is returned only for
          `@sys-time` and `@sys-date` entities when the user's input is ambiguous.
          This property is included only if the new system entities are enabled for the
          workspace.
    :param RuntimeEntityRole role: (optional) An object describing the role played
          by a system entity that is specifies the beginning or end of a range recognized
          in the user input. This property is included only if the new system entities are
          enabled for the workspace.
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
    ) -> None:
        """
        Initialize a RuntimeEntity object.

        :param str entity: An entity detected in the input.
        :param str value: The entity value that was recognized in the user input.
        :param List[int] location: (optional) An array of zero-based character
               offsets that indicate where the detected entity values begin and end in the
               input text.
        :param float confidence: (optional) A decimal percentage that represents
               confidence in the recognized entity.
        :param List[CaptureGroup] groups: (optional) The recognized capture groups
               for the entity, as defined by the entity pattern.
        :param RuntimeEntityInterpretation interpretation: (optional) An object
               containing detailed information about the entity recognized in the user
               input.
               For more information about how system entities are interpreted, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-system-entities).
        :param List[RuntimeEntityAlternative] alternatives: (optional) An array of
               possible alternative values that the user might have intended instead of
               the value returned in the **value** property. This property is returned
               only for `@sys-time` and `@sys-date` entities when the user's input is
               ambiguous.
               This property is included only if the new system entities are enabled for
               the workspace.
        :param RuntimeEntityRole role: (optional) An object describing the role
               played by a system entity that is specifies the beginning or end of a range
               recognized in the user input. This property is included only if the new
               system entities are enabled for the workspace.
        """
        self.entity = entity
        self.location = location
        self.value = value
        self.confidence = confidence
        self.groups = groups
        self.interpretation = interpretation
        self.alternatives = alternatives
        self.role = role

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
    only if the new system entities are enabled for the workspace.

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
    """

    def __init__(
        self,
        intent: str,
        *,
        confidence: Optional[float] = None,
    ) -> None:
        """
        Initialize a RuntimeIntent object.

        :param str intent: The name of the recognized intent.
        :param float confidence: (optional) A decimal percentage that represents
               confidence in the intent. If you are specifying an intent as part of a
               request, but you do not have a calculated confidence value, specify `1`.
        """
        self.intent = intent
        self.confidence = confidence

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
                'RuntimeResponseGenericRuntimeResponseTypeUserDefined',
                'RuntimeResponseGenericRuntimeResponseTypeVideo',
                'RuntimeResponseGenericRuntimeResponseTypeAudio',
                'RuntimeResponseGenericRuntimeResponseTypeIframe'
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
                'RuntimeResponseGenericRuntimeResponseTypeUserDefined',
                'RuntimeResponseGenericRuntimeResponseTypeVideo',
                'RuntimeResponseGenericRuntimeResponseTypeAudio',
                'RuntimeResponseGenericRuntimeResponseTypeIframe'
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
        mapping['iframe'] = 'RuntimeResponseGenericRuntimeResponseTypeIframe'
        mapping['image'] = 'RuntimeResponseGenericRuntimeResponseTypeImage'
        mapping['option'] = 'RuntimeResponseGenericRuntimeResponseTypeOption'
        mapping[
            'suggestion'] = 'RuntimeResponseGenericRuntimeResponseTypeSuggestion'
        mapping['pause'] = 'RuntimeResponseGenericRuntimeResponseTypePause'
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


class Synonym:
    """
    Synonym.

    :param str synonym: The text of the synonym. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        synonym: str,
        *,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Synonym object.

        :param str synonym: The text of the synonym. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        """
        self.synonym = synonym
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Synonym':
        """Initialize a Synonym object from a json dictionary."""
        args = {}
        if (synonym := _dict.get('synonym')) is not None:
            args['synonym'] = synonym
        else:
            raise ValueError(
                'Required property \'synonym\' not present in Synonym JSON')
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Synonym object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'synonym') and self.synonym is not None:
            _dict['synonym'] = self.synonym
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Synonym object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Synonym') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Synonym') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SynonymCollection:
    """
    SynonymCollection.

    :param List[Synonym] synonyms: An array of synonyms.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        synonyms: List['Synonym'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a SynonymCollection object.

        :param List[Synonym] synonyms: An array of synonyms.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.synonyms = synonyms
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'SynonymCollection':
        """Initialize a SynonymCollection object from a json dictionary."""
        args = {}
        if (synonyms := _dict.get('synonyms')) is not None:
            args['synonyms'] = [Synonym.from_dict(v) for v in synonyms]
        else:
            raise ValueError(
                'Required property \'synonyms\' not present in SynonymCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in SynonymCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SynonymCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            synonyms_list = []
            for v in self.synonyms:
                if isinstance(v, dict):
                    synonyms_list.append(v)
                else:
                    synonyms_list.append(v.to_dict())
            _dict['synonyms'] = synonyms_list
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
        """Return a `str` version of this SynonymCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'SynonymCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'SynonymCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Value:
    """
    Value.

    :param str value: The text of the entity value. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param dict metadata: (optional) Any metadata related to the entity value.
    :param str type: Specifies the type of entity value.
    :param List[str] synonyms: (optional) An array of synonyms for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A synonym must conform to the following resrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :param List[str] patterns: (optional) An array of patterns for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A pattern is a regular expression; for more information about how
          to specify a pattern, see the
          [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(
        self,
        value: str,
        type: str,
        *,
        metadata: Optional[dict] = None,
        synonyms: Optional[List[str]] = None,
        patterns: Optional[List[str]] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
    ) -> None:
        """
        Initialize a Value object.

        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param str type: Specifies the type of entity value.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param List[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param List[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/assistant?topic=assistant-entities#entities-create-dictionary-based).
        """
        self.value = value
        self.metadata = metadata
        self.type = type
        self.synonyms = synonyms
        self.patterns = patterns
        self.created = created
        self.updated = updated

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Value':
        """Initialize a Value object from a json dictionary."""
        args = {}
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError(
                'Required property \'value\' not present in Value JSON')
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (type := _dict.get('type')) is not None:
            args['type'] = type
        else:
            raise ValueError(
                'Required property \'type\' not present in Value JSON')
        if (synonyms := _dict.get('synonyms')) is not None:
            args['synonyms'] = synonyms
        if (patterns := _dict.get('patterns')) is not None:
            args['patterns'] = patterns
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Value object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = self.synonyms
        if hasattr(self, 'patterns') and self.patterns is not None:
            _dict['patterns'] = self.patterns
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Value object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Value') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Value') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Specifies the type of entity value.
        """

        SYNONYMS = 'synonyms'
        PATTERNS = 'patterns'


class ValueCollection:
    """
    ValueCollection.

    :param List[Value] values: An array of entity values.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        values: List['Value'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a ValueCollection object.

        :param List[Value] values: An array of entity values.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.values = values
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ValueCollection':
        """Initialize a ValueCollection object from a json dictionary."""
        args = {}
        if (values := _dict.get('values')) is not None:
            args['values'] = [Value.from_dict(v) for v in values]
        else:
            raise ValueError(
                'Required property \'values\' not present in ValueCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ValueCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'values') and self.values is not None:
            values_list = []
            for v in self.values:
                if isinstance(v, dict):
                    values_list.append(v)
                else:
                    values_list.append(v.to_dict())
            _dict['values'] = values_list
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
        """Return a `str` version of this ValueCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ValueCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ValueCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Webhook:
    """
    A webhook that can be used by dialog nodes to make programmatic calls to an external
    function.
    **Note:** Currently, only a single webhook named `main_webhook` is supported.

    :param str url: The URL for the external service or application to which you
          want to send HTTP POST requests.
    :param str name: The name of the webhook. Currently, `main_webhook` is the only
          supported value.
    :param List[WebhookHeader] headers_: (optional) An optional array of HTTP
          headers to pass with the HTTP request.
    """

    def __init__(
        self,
        url: str,
        name: str,
        *,
        headers_: Optional[List['WebhookHeader']] = None,
    ) -> None:
        """
        Initialize a Webhook object.

        :param str url: The URL for the external service or application to which
               you want to send HTTP POST requests.
        :param str name: The name of the webhook. Currently, `main_webhook` is the
               only supported value.
        :param List[WebhookHeader] headers_: (optional) An optional array of HTTP
               headers to pass with the HTTP request.
        """
        self.url = url
        self.name = name
        self.headers_ = headers_

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Webhook':
        """Initialize a Webhook object from a json dictionary."""
        args = {}
        if (url := _dict.get('url')) is not None:
            args['url'] = url
        else:
            raise ValueError(
                'Required property \'url\' not present in Webhook JSON')
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in Webhook JSON')
        if (headers_ := _dict.get('headers')) is not None:
            args['headers_'] = [WebhookHeader.from_dict(v) for v in headers_]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Webhook object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'headers_') and self.headers_ is not None:
            headers_list = []
            for v in self.headers_:
                if isinstance(v, dict):
                    headers_list.append(v)
                else:
                    headers_list.append(v.to_dict())
            _dict['headers'] = headers_list
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Webhook object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Webhook') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Webhook') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WebhookHeader:
    """
    A key/value pair defining an HTTP header and a value.

    :param str name: The name of an HTTP header (for example, `Authorization`).
    :param str value: The value of an HTTP header.
    """

    def __init__(
        self,
        name: str,
        value: str,
    ) -> None:
        """
        Initialize a WebhookHeader object.

        :param str name: The name of an HTTP header (for example, `Authorization`).
        :param str value: The value of an HTTP header.
        """
        self.name = name
        self.value = value

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WebhookHeader':
        """Initialize a WebhookHeader object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in WebhookHeader JSON')
        if (value := _dict.get('value')) is not None:
            args['value'] = value
        else:
            raise ValueError(
                'Required property \'value\' not present in WebhookHeader JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebhookHeader object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WebhookHeader object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WebhookHeader') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WebhookHeader') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Workspace:
    """
    Workspace.

    :param str name: The name of the workspace. This string cannot contain carriage
          return, newline, or tab characters.
    :param str description: (optional) The description of the workspace. This string
          cannot contain carriage return, newline, or tab characters.
    :param str language: The language of the workspace.
    :param str workspace_id: (optional) The workspace ID of the workspace.
    :param List[DialogNode] dialog_nodes: (optional) An array of objects describing
          the dialog nodes in the workspace.
    :param List[Counterexample] counterexamples: (optional) An array of objects
          defining input examples that have been marked as irrelevant input.
    :param datetime created: (optional) The timestamp for creation of the object.
    :param datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :param dict metadata: (optional) Any metadata related to the workspace.
    :param bool learning_opt_out: Whether training data from the workspace
          (including artifacts such as intents and entities) can be used by IBM for
          general service improvements. `true` indicates that workspace training data is
          not to be used.
    :param WorkspaceSystemSettings system_settings: (optional) Global settings for
          the workspace.
    :param str status: (optional) The current status of the workspace:
           - **Available**: The workspace is available and ready to process messages.
           - **Failed**: An asynchronous operation has failed. See the **status_errors**
          property for more information about the cause of the failure.
           - **Non Existent**: The workspace does not exist.
           - **Processing**: An asynchronous operation has not yet completed.
           - **Training**: The workspace is training based on new data such as intents or
          examples.
    :param List[StatusError] status_errors: (optional) An array of messages about
          errors that caused an asynchronous operation to fail.
    :param List[Webhook] webhooks: (optional)
    :param List[Intent] intents: (optional) An array of intents.
    :param List[Entity] entities: (optional) An array of objects describing the
          entities for the workspace.
    :param WorkspaceCounts counts: (optional) An object containing properties that
          indicate how many intents, entities, and dialog nodes are defined in the
          workspace. This property is included only in responses from the **Export
          workspace asynchronously** method, and only when the **verbose** query parameter
          is set to `true`.
    """

    def __init__(
        self,
        name: str,
        language: str,
        learning_opt_out: bool,
        *,
        description: Optional[str] = None,
        workspace_id: Optional[str] = None,
        dialog_nodes: Optional[List['DialogNode']] = None,
        counterexamples: Optional[List['Counterexample']] = None,
        created: Optional[datetime] = None,
        updated: Optional[datetime] = None,
        metadata: Optional[dict] = None,
        system_settings: Optional['WorkspaceSystemSettings'] = None,
        status: Optional[str] = None,
        status_errors: Optional[List['StatusError']] = None,
        webhooks: Optional[List['Webhook']] = None,
        intents: Optional[List['Intent']] = None,
        entities: Optional[List['Entity']] = None,
        counts: Optional['WorkspaceCounts'] = None,
    ) -> None:
        """
        Initialize a Workspace object.

        :param str name: The name of the workspace. This string cannot contain
               carriage return, newline, or tab characters.
        :param str language: The language of the workspace.
        :param bool learning_opt_out: Whether training data from the workspace
               (including artifacts such as intents and entities) can be used by IBM for
               general service improvements. `true` indicates that workspace training data
               is not to be used.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param List[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param List[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param List[Webhook] webhooks: (optional)
        :param List[Intent] intents: (optional) An array of intents.
        :param List[Entity] entities: (optional) An array of objects describing the
               entities for the workspace.
        """
        self.name = name
        self.description = description
        self.language = language
        self.workspace_id = workspace_id
        self.dialog_nodes = dialog_nodes
        self.counterexamples = counterexamples
        self.created = created
        self.updated = updated
        self.metadata = metadata
        self.learning_opt_out = learning_opt_out
        self.system_settings = system_settings
        self.status = status
        self.status_errors = status_errors
        self.webhooks = webhooks
        self.intents = intents
        self.entities = entities
        self.counts = counts

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Workspace':
        """Initialize a Workspace object from a json dictionary."""
        args = {}
        if (name := _dict.get('name')) is not None:
            args['name'] = name
        else:
            raise ValueError(
                'Required property \'name\' not present in Workspace JSON')
        if (description := _dict.get('description')) is not None:
            args['description'] = description
        if (language := _dict.get('language')) is not None:
            args['language'] = language
        else:
            raise ValueError(
                'Required property \'language\' not present in Workspace JSON')
        if (workspace_id := _dict.get('workspace_id')) is not None:
            args['workspace_id'] = workspace_id
        if (dialog_nodes := _dict.get('dialog_nodes')) is not None:
            args['dialog_nodes'] = [
                DialogNode.from_dict(v) for v in dialog_nodes
            ]
        if (counterexamples := _dict.get('counterexamples')) is not None:
            args['counterexamples'] = [
                Counterexample.from_dict(v) for v in counterexamples
            ]
        if (created := _dict.get('created')) is not None:
            args['created'] = string_to_datetime(created)
        if (updated := _dict.get('updated')) is not None:
            args['updated'] = string_to_datetime(updated)
        if (metadata := _dict.get('metadata')) is not None:
            args['metadata'] = metadata
        if (learning_opt_out := _dict.get('learning_opt_out')) is not None:
            args['learning_opt_out'] = learning_opt_out
        else:
            raise ValueError(
                'Required property \'learning_opt_out\' not present in Workspace JSON'
            )
        if (system_settings := _dict.get('system_settings')) is not None:
            args['system_settings'] = WorkspaceSystemSettings.from_dict(
                system_settings)
        if (status := _dict.get('status')) is not None:
            args['status'] = status
        if (status_errors := _dict.get('status_errors')) is not None:
            args['status_errors'] = [
                StatusError.from_dict(v) for v in status_errors
            ]
        if (webhooks := _dict.get('webhooks')) is not None:
            args['webhooks'] = [Webhook.from_dict(v) for v in webhooks]
        if (intents := _dict.get('intents')) is not None:
            args['intents'] = [Intent.from_dict(v) for v in intents]
        if (entities := _dict.get('entities')) is not None:
            args['entities'] = [Entity.from_dict(v) for v in entities]
        if (counts := _dict.get('counts')) is not None:
            args['counts'] = WorkspaceCounts.from_dict(counts)
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Workspace object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'workspace_id') and getattr(
                self, 'workspace_id') is not None:
            _dict['workspace_id'] = getattr(self, 'workspace_id')
        if hasattr(self, 'dialog_nodes') and self.dialog_nodes is not None:
            dialog_nodes_list = []
            for v in self.dialog_nodes:
                if isinstance(v, dict):
                    dialog_nodes_list.append(v)
                else:
                    dialog_nodes_list.append(v.to_dict())
            _dict['dialog_nodes'] = dialog_nodes_list
        if hasattr(self,
                   'counterexamples') and self.counterexamples is not None:
            counterexamples_list = []
            for v in self.counterexamples:
                if isinstance(v, dict):
                    counterexamples_list.append(v)
                else:
                    counterexamples_list.append(v.to_dict())
            _dict['counterexamples'] = counterexamples_list
        if hasattr(self, 'created') and getattr(self, 'created') is not None:
            _dict['created'] = datetime_to_string(getattr(self, 'created'))
        if hasattr(self, 'updated') and getattr(self, 'updated') is not None:
            _dict['updated'] = datetime_to_string(getattr(self, 'updated'))
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self,
                   'learning_opt_out') and self.learning_opt_out is not None:
            _dict['learning_opt_out'] = self.learning_opt_out
        if hasattr(self,
                   'system_settings') and self.system_settings is not None:
            if isinstance(self.system_settings, dict):
                _dict['system_settings'] = self.system_settings
            else:
                _dict['system_settings'] = self.system_settings.to_dict()
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
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            webhooks_list = []
            for v in self.webhooks:
                if isinstance(v, dict):
                    webhooks_list.append(v)
                else:
                    webhooks_list.append(v.to_dict())
            _dict['webhooks'] = webhooks_list
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
        if hasattr(self, 'counts') and getattr(self, 'counts') is not None:
            if isinstance(getattr(self, 'counts'), dict):
                _dict['counts'] = getattr(self, 'counts')
            else:
                _dict['counts'] = getattr(self, 'counts').to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Workspace object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Workspace') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Workspace') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(str, Enum):
        """
        The current status of the workspace:
         - **Available**: The workspace is available and ready to process messages.
         - **Failed**: An asynchronous operation has failed. See the **status_errors**
        property for more information about the cause of the failure.
         - **Non Existent**: The workspace does not exist.
         - **Processing**: An asynchronous operation has not yet completed.
         - **Training**: The workspace is training based on new data such as intents or
        examples.
        """

        AVAILABLE = 'Available'
        FAILED = 'Failed'
        NON_EXISTENT = 'Non Existent'
        PROCESSING = 'Processing'
        TRAINING = 'Training'
        UNAVAILABLE = 'Unavailable'


class WorkspaceCollection:
    """
    WorkspaceCollection.

    :param List[Workspace] workspaces: An array of objects describing the workspaces
          associated with the service instance.
    :param Pagination pagination: The pagination data for the returned objects. For
          more information about using pagination, see [Pagination](#pagination).
    """

    def __init__(
        self,
        workspaces: List['Workspace'],
        pagination: 'Pagination',
    ) -> None:
        """
        Initialize a WorkspaceCollection object.

        :param List[Workspace] workspaces: An array of objects describing the
               workspaces associated with the service instance.
        :param Pagination pagination: The pagination data for the returned objects.
               For more information about using pagination, see [Pagination](#pagination).
        """
        self.workspaces = workspaces
        self.pagination = pagination

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceCollection':
        """Initialize a WorkspaceCollection object from a json dictionary."""
        args = {}
        if (workspaces := _dict.get('workspaces')) is not None:
            args['workspaces'] = [Workspace.from_dict(v) for v in workspaces]
        else:
            raise ValueError(
                'Required property \'workspaces\' not present in WorkspaceCollection JSON'
            )
        if (pagination := _dict.get('pagination')) is not None:
            args['pagination'] = Pagination.from_dict(pagination)
        else:
            raise ValueError(
                'Required property \'pagination\' not present in WorkspaceCollection JSON'
            )
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'workspaces') and self.workspaces is not None:
            workspaces_list = []
            for v in self.workspaces:
                if isinstance(v, dict):
                    workspaces_list.append(v)
                else:
                    workspaces_list.append(v.to_dict())
            _dict['workspaces'] = workspaces_list
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
        """Return a `str` version of this WorkspaceCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceCounts:
    """
    An object containing properties that indicate how many intents, entities, and dialog
    nodes are defined in the workspace. This property is included only in responses from
    the **Export workspace asynchronously** method, and only when the **verbose** query
    parameter is set to `true`.

    :param int intent: (optional) The number of intents defined in the workspace.
    :param int entity: (optional) The number of entities defined in the workspace.
    :param int node: (optional) The number of nodes defined in the workspace.
    """

    def __init__(
        self,
        *,
        intent: Optional[int] = None,
        entity: Optional[int] = None,
        node: Optional[int] = None,
    ) -> None:
        """
        Initialize a WorkspaceCounts object.

        :param int intent: (optional) The number of intents defined in the
               workspace.
        :param int entity: (optional) The number of entities defined in the
               workspace.
        :param int node: (optional) The number of nodes defined in the workspace.
        """
        self.intent = intent
        self.entity = entity
        self.node = node

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceCounts':
        """Initialize a WorkspaceCounts object from a json dictionary."""
        args = {}
        if (intent := _dict.get('intent')) is not None:
            args['intent'] = intent
        if (entity := _dict.get('entity')) is not None:
            args['entity'] = entity
        if (node := _dict.get('node')) is not None:
            args['node'] = node
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceCounts object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'node') and self.node is not None:
            _dict['node'] = self.node
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkspaceCounts object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceCounts') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceCounts') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettings:
    """
    Global settings for the workspace.

    :param WorkspaceSystemSettingsTooling tooling: (optional) Workspace settings
          related to the Watson Assistant user interface.
    :param WorkspaceSystemSettingsDisambiguation disambiguation: (optional)
          Workspace settings related to the disambiguation feature.
    :param dict human_agent_assist: (optional) For internal use only.
    :param bool spelling_suggestions: (optional) Whether spelling correction is
          enabled for the workspace.
    :param bool spelling_auto_correct: (optional) Whether autocorrection is enabled
          for the workspace. If spelling correction is enabled and this property is
          `false`, any suggested corrections are returned in the **suggested_text**
          property of the message response. If this property is `true`, any corrections
          are automatically applied to the user input, and the original text is returned
          in the **original_text** property of the message response.
    :param WorkspaceSystemSettingsSystemEntities system_entities: (optional)
          Workspace settings related to the behavior of system entities.
    :param WorkspaceSystemSettingsOffTopic off_topic: (optional) Workspace settings
          related to detection of irrelevant input.
    :param WorkspaceSystemSettingsNlp nlp: (optional) Workspace settings related to
          the version of the training algorithms currently used by the skill.

    This type supports additional properties of type object. For internal use only.
    """

    # The set of defined properties for the class
    _properties = frozenset([
        'tooling', 'disambiguation', 'human_agent_assist',
        'spelling_suggestions', 'spelling_auto_correct', 'system_entities',
        'off_topic', 'nlp'
    ])

    def __init__(
        self,
        *,
        tooling: Optional['WorkspaceSystemSettingsTooling'] = None,
        disambiguation: Optional[
            'WorkspaceSystemSettingsDisambiguation'] = None,
        human_agent_assist: Optional[dict] = None,
        spelling_suggestions: Optional[bool] = None,
        spelling_auto_correct: Optional[bool] = None,
        system_entities: Optional[
            'WorkspaceSystemSettingsSystemEntities'] = None,
        off_topic: Optional['WorkspaceSystemSettingsOffTopic'] = None,
        nlp: Optional['WorkspaceSystemSettingsNlp'] = None,
        **kwargs: Optional[object],
    ) -> None:
        """
        Initialize a WorkspaceSystemSettings object.

        :param WorkspaceSystemSettingsTooling tooling: (optional) Workspace
               settings related to the Watson Assistant user interface.
        :param WorkspaceSystemSettingsDisambiguation disambiguation: (optional)
               Workspace settings related to the disambiguation feature.
        :param dict human_agent_assist: (optional) For internal use only.
        :param bool spelling_suggestions: (optional) Whether spelling correction is
               enabled for the workspace.
        :param bool spelling_auto_correct: (optional) Whether autocorrection is
               enabled for the workspace. If spelling correction is enabled and this
               property is `false`, any suggested corrections are returned in the
               **suggested_text** property of the message response. If this property is
               `true`, any corrections are automatically applied to the user input, and
               the original text is returned in the **original_text** property of the
               message response.
        :param WorkspaceSystemSettingsSystemEntities system_entities: (optional)
               Workspace settings related to the behavior of system entities.
        :param WorkspaceSystemSettingsOffTopic off_topic: (optional) Workspace
               settings related to detection of irrelevant input.
        :param WorkspaceSystemSettingsNlp nlp: (optional) Workspace settings
               related to the version of the training algorithms currently used by the
               skill.
        :param object **kwargs: (optional) For internal use only.
        """
        self.tooling = tooling
        self.disambiguation = disambiguation
        self.human_agent_assist = human_agent_assist
        self.spelling_suggestions = spelling_suggestions
        self.spelling_auto_correct = spelling_auto_correct
        self.system_entities = system_entities
        self.off_topic = off_topic
        self.nlp = nlp
        for k, v in kwargs.items():
            if k not in WorkspaceSystemSettings._properties:
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
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettings':
        """Initialize a WorkspaceSystemSettings object from a json dictionary."""
        args = {}
        if (tooling := _dict.get('tooling')) is not None:
            args['tooling'] = WorkspaceSystemSettingsTooling.from_dict(tooling)
        if (disambiguation := _dict.get('disambiguation')) is not None:
            args[
                'disambiguation'] = WorkspaceSystemSettingsDisambiguation.from_dict(
                    disambiguation)
        if (human_agent_assist := _dict.get('human_agent_assist')) is not None:
            args['human_agent_assist'] = human_agent_assist
        if (spelling_suggestions :=
                _dict.get('spelling_suggestions')) is not None:
            args['spelling_suggestions'] = spelling_suggestions
        if (spelling_auto_correct :=
                _dict.get('spelling_auto_correct')) is not None:
            args['spelling_auto_correct'] = spelling_auto_correct
        if (system_entities := _dict.get('system_entities')) is not None:
            args[
                'system_entities'] = WorkspaceSystemSettingsSystemEntities.from_dict(
                    system_entities)
        if (off_topic := _dict.get('off_topic')) is not None:
            args['off_topic'] = WorkspaceSystemSettingsOffTopic.from_dict(
                off_topic)
        if (nlp := _dict.get('nlp')) is not None:
            args['nlp'] = WorkspaceSystemSettingsNlp.from_dict(nlp)
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
        """Initialize a WorkspaceSystemSettings object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tooling') and self.tooling is not None:
            if isinstance(self.tooling, dict):
                _dict['tooling'] = self.tooling
            else:
                _dict['tooling'] = self.tooling.to_dict()
        if hasattr(self, 'disambiguation') and self.disambiguation is not None:
            if isinstance(self.disambiguation, dict):
                _dict['disambiguation'] = self.disambiguation
            else:
                _dict['disambiguation'] = self.disambiguation.to_dict()
        if hasattr(
                self,
                'human_agent_assist') and self.human_agent_assist is not None:
            _dict['human_agent_assist'] = self.human_agent_assist
        if hasattr(self, 'spelling_suggestions'
                  ) and self.spelling_suggestions is not None:
            _dict['spelling_suggestions'] = self.spelling_suggestions
        if hasattr(self, 'spelling_auto_correct'
                  ) and self.spelling_auto_correct is not None:
            _dict['spelling_auto_correct'] = self.spelling_auto_correct
        if hasattr(self,
                   'system_entities') and self.system_entities is not None:
            if isinstance(self.system_entities, dict):
                _dict['system_entities'] = self.system_entities
            else:
                _dict['system_entities'] = self.system_entities.to_dict()
        if hasattr(self, 'off_topic') and self.off_topic is not None:
            if isinstance(self.off_topic, dict):
                _dict['off_topic'] = self.off_topic
            else:
                _dict['off_topic'] = self.off_topic.to_dict()
        if hasattr(self, 'nlp') and self.nlp is not None:
            if isinstance(self.nlp, dict):
                _dict['nlp'] = self.nlp
            else:
                _dict['nlp'] = self.nlp.to_dict()
        for k in [
                _k for _k in vars(self).keys()
                if _k not in WorkspaceSystemSettings._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def get_properties(self) -> Dict:
        """Return the additional properties from this instance of WorkspaceSystemSettings in the form of a dict."""
        _dict = {}
        for k in [
                _k for _k in vars(self).keys()
                if _k not in WorkspaceSystemSettings._properties
        ]:
            _dict[k] = getattr(self, k)
        return _dict

    def set_properties(self, _dict: dict):
        """Set a dictionary of additional properties in this instance of WorkspaceSystemSettings"""
        for k in [
                _k for _k in vars(self).keys()
                if _k not in WorkspaceSystemSettings._properties
        ]:
            delattr(self, k)
        for k, v in _dict.items():
            if k not in WorkspaceSystemSettings._properties:
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
        """Return a `str` version of this WorkspaceSystemSettings object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettings') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettings') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsDisambiguation:
    """
    Workspace settings related to the disambiguation feature.

    :param str prompt: (optional) The text of the introductory prompt that
          accompanies disambiguation options presented to the user.
    :param str none_of_the_above_prompt: (optional) The user-facing label for the
          option users can select if none of the suggested options is correct. If no value
          is specified for this property, this option does not appear.
    :param bool enabled: (optional) Whether the disambiguation feature is enabled
          for the workspace.
    :param str sensitivity: (optional) The sensitivity of the disambiguation feature
          to intent detection uncertainty. Higher sensitivity means that the
          disambiguation feature is triggered more often and includes more choices.
    :param bool randomize: (optional) Whether the order in which disambiguation
          suggestions are presented should be randomized (but still influenced by relative
          confidence).
    :param int max_suggestions: (optional) The maximum number of disambigation
          suggestions that can be included in a `suggestion` response.
    :param str suggestion_text_policy: (optional) For internal use only.
    """

    def __init__(
        self,
        *,
        prompt: Optional[str] = None,
        none_of_the_above_prompt: Optional[str] = None,
        enabled: Optional[bool] = None,
        sensitivity: Optional[str] = None,
        randomize: Optional[bool] = None,
        max_suggestions: Optional[int] = None,
        suggestion_text_policy: Optional[str] = None,
    ) -> None:
        """
        Initialize a WorkspaceSystemSettingsDisambiguation object.

        :param str prompt: (optional) The text of the introductory prompt that
               accompanies disambiguation options presented to the user.
        :param str none_of_the_above_prompt: (optional) The user-facing label for
               the option users can select if none of the suggested options is correct. If
               no value is specified for this property, this option does not appear.
        :param bool enabled: (optional) Whether the disambiguation feature is
               enabled for the workspace.
        :param str sensitivity: (optional) The sensitivity of the disambiguation
               feature to intent detection uncertainty. Higher sensitivity means that the
               disambiguation feature is triggered more often and includes more choices.
        :param bool randomize: (optional) Whether the order in which disambiguation
               suggestions are presented should be randomized (but still influenced by
               relative confidence).
        :param int max_suggestions: (optional) The maximum number of disambigation
               suggestions that can be included in a `suggestion` response.
        :param str suggestion_text_policy: (optional) For internal use only.
        """
        self.prompt = prompt
        self.none_of_the_above_prompt = none_of_the_above_prompt
        self.enabled = enabled
        self.sensitivity = sensitivity
        self.randomize = randomize
        self.max_suggestions = max_suggestions
        self.suggestion_text_policy = suggestion_text_policy

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettingsDisambiguation':
        """Initialize a WorkspaceSystemSettingsDisambiguation object from a json dictionary."""
        args = {}
        if (prompt := _dict.get('prompt')) is not None:
            args['prompt'] = prompt
        if (none_of_the_above_prompt :=
                _dict.get('none_of_the_above_prompt')) is not None:
            args['none_of_the_above_prompt'] = none_of_the_above_prompt
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        if (sensitivity := _dict.get('sensitivity')) is not None:
            args['sensitivity'] = sensitivity
        if (randomize := _dict.get('randomize')) is not None:
            args['randomize'] = randomize
        if (max_suggestions := _dict.get('max_suggestions')) is not None:
            args['max_suggestions'] = max_suggestions
        if (suggestion_text_policy :=
                _dict.get('suggestion_text_policy')) is not None:
            args['suggestion_text_policy'] = suggestion_text_policy
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsDisambiguation object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'prompt') and self.prompt is not None:
            _dict['prompt'] = self.prompt
        if hasattr(self, 'none_of_the_above_prompt'
                  ) and self.none_of_the_above_prompt is not None:
            _dict['none_of_the_above_prompt'] = self.none_of_the_above_prompt
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        if hasattr(self, 'sensitivity') and self.sensitivity is not None:
            _dict['sensitivity'] = self.sensitivity
        if hasattr(self, 'randomize') and self.randomize is not None:
            _dict['randomize'] = self.randomize
        if hasattr(self,
                   'max_suggestions') and self.max_suggestions is not None:
            _dict['max_suggestions'] = self.max_suggestions
        if hasattr(self, 'suggestion_text_policy'
                  ) and self.suggestion_text_policy is not None:
            _dict['suggestion_text_policy'] = self.suggestion_text_policy
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkspaceSystemSettingsDisambiguation object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettingsDisambiguation') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettingsDisambiguation') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SensitivityEnum(str, Enum):
        """
        The sensitivity of the disambiguation feature to intent detection uncertainty.
        Higher sensitivity means that the disambiguation feature is triggered more often
        and includes more choices.
        """

        AUTO = 'auto'
        HIGH = 'high'
        MEDIUM_HIGH = 'medium_high'
        MEDIUM = 'medium'
        MEDIUM_LOW = 'medium_low'
        LOW = 'low'


class WorkspaceSystemSettingsNlp:
    """
    Workspace settings related to the version of the training algorithms currently used by
    the skill.

    :param str model: (optional) The policy the skill follows for selecting the
          algorithm version to use. For more information, see the
          [documentation](/docs/watson-assistant?topic=watson-assistant-algorithm-version).
           On IBM Cloud, you can specify `latest`, `previous`, or `beta`.
           On IBM Cloud Pak for Data, you can specify either `beta` or the date of the
          version you want to use, in `YYYY-MM-DD` format.
    """

    def __init__(
        self,
        *,
        model: Optional[str] = None,
    ) -> None:
        """
        Initialize a WorkspaceSystemSettingsNlp object.

        :param str model: (optional) The policy the skill follows for selecting the
               algorithm version to use. For more information, see the
               [documentation](/docs/watson-assistant?topic=watson-assistant-algorithm-version).
                On IBM Cloud, you can specify `latest`, `previous`, or `beta`.
                On IBM Cloud Pak for Data, you can specify either `beta` or the date of
               the version you want to use, in `YYYY-MM-DD` format.
        """
        self.model = model

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettingsNlp':
        """Initialize a WorkspaceSystemSettingsNlp object from a json dictionary."""
        args = {}
        if (model := _dict.get('model')) is not None:
            args['model'] = model
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsNlp object from a json dictionary."""
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
        """Return a `str` version of this WorkspaceSystemSettingsNlp object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettingsNlp') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettingsNlp') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsOffTopic:
    """
    Workspace settings related to detection of irrelevant input.

    :param bool enabled: (optional) Whether enhanced irrelevance detection is
          enabled for the workspace.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a WorkspaceSystemSettingsOffTopic object.

        :param bool enabled: (optional) Whether enhanced irrelevance detection is
               enabled for the workspace.
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettingsOffTopic':
        """Initialize a WorkspaceSystemSettingsOffTopic object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsOffTopic object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkspaceSystemSettingsOffTopic object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettingsOffTopic') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettingsOffTopic') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsSystemEntities:
    """
    Workspace settings related to the behavior of system entities.

    :param bool enabled: (optional) Whether the new system entities are enabled for
          the workspace.
    """

    def __init__(
        self,
        *,
        enabled: Optional[bool] = None,
    ) -> None:
        """
        Initialize a WorkspaceSystemSettingsSystemEntities object.

        :param bool enabled: (optional) Whether the new system entities are enabled
               for the workspace.
        """
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettingsSystemEntities':
        """Initialize a WorkspaceSystemSettingsSystemEntities object from a json dictionary."""
        args = {}
        if (enabled := _dict.get('enabled')) is not None:
            args['enabled'] = enabled
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsSystemEntities object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkspaceSystemSettingsSystemEntities object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettingsSystemEntities') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettingsSystemEntities') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsTooling:
    """
    Workspace settings related to the Watson Assistant user interface.

    :param bool store_generic_responses: (optional) Whether the dialog JSON editor
          displays text responses within the `output.generic` object.
    """

    def __init__(
        self,
        *,
        store_generic_responses: Optional[bool] = None,
    ) -> None:
        """
        Initialize a WorkspaceSystemSettingsTooling object.

        :param bool store_generic_responses: (optional) Whether the dialog JSON
               editor displays text responses within the `output.generic` object.
        """
        self.store_generic_responses = store_generic_responses

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'WorkspaceSystemSettingsTooling':
        """Initialize a WorkspaceSystemSettingsTooling object from a json dictionary."""
        args = {}
        if (store_generic_responses :=
                _dict.get('store_generic_responses')) is not None:
            args['store_generic_responses'] = store_generic_responses
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsTooling object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'store_generic_responses'
                  ) and self.store_generic_responses is not None:
            _dict['store_generic_responses'] = self.store_generic_responses
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this WorkspaceSystemSettingsTooling object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'WorkspaceSystemSettingsTooling') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'WorkspaceSystemSettingsTooling') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the audio clip.
    :param str title: (optional) An optional title to show before the response.
    :param str description: (optional) An optional description to show with the
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the audio clip.
        :param str title: (optional) An optional title to show before the response.
        :param str description: (optional) An optional description to show with the
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
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio JSON'
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
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeAudio'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
           **Note:** The `channel_transfer` response type is not supported on IBM Cloud
          Pak for Data.
    :param str message_to_user: The message to display to the user when initiating a
          channel transfer.
    :param ChannelTransferInfo transfer_info: Information used by an integration to
          transfer the conversation to a different channel.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer object.

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
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.message_to_user = message_to_user
        self.transfer_info = transfer_info
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer JSON'
            )
        if (message_to_user := _dict.get('message_to_user')) is not None:
            args['message_to_user'] = message_to_user
        else:
            raise ValueError(
                'Required property \'message_to_user\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer JSON'
            )
        if (transfer_info := _dict.get('transfer_info')) is not None:
            args['transfer_info'] = ChannelTransferInfo.from_dict(transfer_info)
        else:
            raise ValueError(
                'Required property \'transfer_info\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other:
        'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other:
        'DialogNodeOutputGenericDialogNodeOutputResponseTypeChannelTransfer'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str message_to_human_agent: (optional) An optional message to be sent to
          the human agent who will be taking over the conversation.
    :param AgentAvailabilityMessage agent_available: (optional) An optional message
          to be displayed to the user to indicate that the conversation will be
          transferred to the next available agent.
    :param AgentAvailabilityMessage agent_unavailable: (optional) An optional
          message to be displayed to the user to indicate that no online agent is
          available to take over the conversation.
    :param DialogNodeOutputConnectToAgentTransferInfo transfer_info: (optional)
          Routing or other contextual information to be used by target service desk
          systems.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
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
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str message_to_human_agent: (optional) An optional message to be
               sent to the human agent who will be taking over the conversation.
        :param AgentAvailabilityMessage agent_available: (optional) An optional
               message to be displayed to the user to indicate that the conversation will
               be transferred to the next available agent.
        :param AgentAvailabilityMessage agent_unavailable: (optional) An optional
               message to be displayed to the user to indicate that no online agent is
               available to take over the conversation.
        :param DialogNodeOutputConnectToAgentTransferInfo transfer_info: (optional)
               Routing or other contextual information to be used by target service desk
               systems.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.message_to_human_agent = message_to_human_agent
        self.agent_available = agent_available
        self.agent_unavailable = agent_unavailable
        self.transfer_info = transfer_info
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent JSON'
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
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeConnectToAgent'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the embeddable content.
    :param str title: (optional) An optional title to show before the response.
    :param str description: (optional) An optional description to show with the
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the embeddable content.
        :param str title: (optional) An optional title to show before the response.
        :param str description: (optional) An optional description to show with the
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
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe JSON'
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
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeIframe'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeImage(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeImage.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the image.
    :param str title: (optional) An optional title to show before the response.
    :param str description: (optional) An optional description to show with the
          response.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeImage object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the image.
        :param str title: (optional) An optional title to show before the response.
        :param str description: (optional) An optional description to show with the
               response.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
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
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeImage object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeImage JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeImage JSON'
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
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeImage object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeImage object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeImage'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeOption(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeOption.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str title: An optional title to show before the response.
    :param str description: (optional) An optional description to show with the
          response.
    :param str preference: (optional) The preferred type of control to display, if
          supported by the channel.
    :param List[DialogNodeOutputOptionsElement] options: An array of objects
          describing the options from which the user can choose. You can include up to 20
          options.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeOption object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str title: An optional title to show before the response.
        :param List[DialogNodeOutputOptionsElement] options: An array of objects
               describing the options from which the user can choose. You can include up
               to 20 options.
        :param str description: (optional) An optional description to show with the
               response.
        :param str preference: (optional) The preferred type of control to display,
               if supported by the channel.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
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
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeOption object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeOption JSON'
            )
        if (title := _dict.get('title')) is not None:
            args['title'] = title
        else:
            raise ValueError(
                'Required property \'title\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeOption JSON'
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
                'Required property \'options\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeOption JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeOption object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeOption object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeOption'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class PreferenceEnum(str, Enum):
        """
        The preferred type of control to display, if supported by the channel.
        """

        DROPDOWN = 'dropdown'
        BUTTON = 'button'


class DialogNodeOutputGenericDialogNodeOutputResponseTypePause(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypePause.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param int time: How long to pause, in milliseconds. The valid values are from 0
          to 10000.
    :param bool typing: (optional) Whether to send a "user is typing" event during
          the pause. Ignored if the channel does not support this event.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypePause object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param int time: How long to pause, in milliseconds. The valid values are
               from 0 to 10000.
        :param bool typing: (optional) Whether to send a "user is typing" event
               during the pause. Ignored if the channel does not support this event.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.time = time
        self.typing = typing
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypePause':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypePause object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypePause JSON'
            )
        if (time := _dict.get('time')) is not None:
            args['time'] = time
        else:
            raise ValueError(
                'Required property \'time\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypePause JSON'
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
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypePause object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypePause object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypePause'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypePause'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
          **Note:** The **search_skill** response type is used only by the v2 runtime API.
    :param str query: The text of the search query. This can be either a
          natural-language query or a query that uses the Discovery query language syntax,
          depending on the value of the **query_type** property. For more information, see
          the [Discovery service
          documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-operators#query-operators).
    :param str query_type: The type of the search query.
    :param str filter: (optional) An optional filter that narrows the set of
          documents to be searched. For more information, see the [Discovery service
          documentation]([Discovery service
          documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-parameters#filter).
    :param str discovery_version: (optional) The version of the Discovery service
          API to use for the query.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
    """

    def __init__(
        self,
        response_type: str,
        query: str,
        query_type: str,
        *,
        filter: Optional[str] = None,
        discovery_version: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
               **Note:** The **search_skill** response type is used only by the v2 runtime
               API.
        :param str query: The text of the search query. This can be either a
               natural-language query or a query that uses the Discovery query language
               syntax, depending on the value of the **query_type** property. For more
               information, see the [Discovery service
               documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-operators#query-operators).
        :param str query_type: The type of the search query.
        :param str filter: (optional) An optional filter that narrows the set of
               documents to be searched. For more information, see the [Discovery service
               documentation]([Discovery service
               documentation](https://cloud.ibm.com/docs/discovery?topic=discovery-query-parameters#filter).
        :param str discovery_version: (optional) The version of the Discovery
               service API to use for the query.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.query = query
        self.query_type = query_type
        self.filter = filter
        self.discovery_version = discovery_version
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill JSON'
            )
        if (query := _dict.get('query')) is not None:
            args['query'] = query
        else:
            raise ValueError(
                'Required property \'query\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill JSON'
            )
        if (query_type := _dict.get('query_type')) is not None:
            args['query_type'] = query_type
        else:
            raise ValueError(
                'Required property \'query_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill JSON'
            )
        if (filter := _dict.get('filter')) is not None:
            args['filter'] = filter
        if (discovery_version := _dict.get('discovery_version')) is not None:
            args['discovery_version'] = discovery_version
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'query_type') and self.query_type is not None:
            _dict['query_type'] = self.query_type
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self,
                   'discovery_version') and self.discovery_version is not None:
            _dict['discovery_version'] = self.discovery_version
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeSearchSkill'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class QueryTypeEnum(str, Enum):
        """
        The type of the search query.
        """

        NATURAL_LANGUAGE = 'natural_language'
        DISCOVERY_QUERY_LANGUAGE = 'discovery_query_language'


class DialogNodeOutputGenericDialogNodeOutputResponseTypeText(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeText.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param List[DialogNodeOutputTextValuesElement] values: A list of one or more
          objects defining text responses.
    :param str selection_policy: (optional) How a response is selected from the
          list, if more than one response is specified.
    :param str delimiter: (optional) The delimiter to use as a separator between
          responses when `selection_policy`=`multiline`.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
    """

    def __init__(
        self,
        response_type: str,
        values: List['DialogNodeOutputTextValuesElement'],
        *,
        selection_policy: Optional[str] = None,
        delimiter: Optional[str] = None,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeText object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param List[DialogNodeOutputTextValuesElement] values: A list of one or
               more objects defining text responses.
        :param str selection_policy: (optional) How a response is selected from the
               list, if more than one response is specified.
        :param str delimiter: (optional) The delimiter to use as a separator
               between responses when `selection_policy`=`multiline`.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.values = values
        self.selection_policy = selection_policy
        self.delimiter = delimiter
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeText':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeText object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeText JSON'
            )
        if (values := _dict.get('values')) is not None:
            args['values'] = [
                DialogNodeOutputTextValuesElement.from_dict(v) for v in values
            ]
        else:
            raise ValueError(
                'Required property \'values\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeText JSON'
            )
        if (selection_policy := _dict.get('selection_policy')) is not None:
            args['selection_policy'] = selection_policy
        if (delimiter := _dict.get('delimiter')) is not None:
            args['delimiter'] = delimiter
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeText object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'values') and self.values is not None:
            values_list = []
            for v in self.values:
                if isinstance(v, dict):
                    values_list.append(v)
                else:
                    values_list.append(v.to_dict())
            _dict['values'] = values_list
        if hasattr(self,
                   'selection_policy') and self.selection_policy is not None:
            _dict['selection_policy'] = self.selection_policy
        if hasattr(self, 'delimiter') and self.delimiter is not None:
            _dict['delimiter'] = self.delimiter
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeText object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeText'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeText'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SelectionPolicyEnum(str, Enum):
        """
        How a response is selected from the list, if more than one response is specified.
        """

        SEQUENTIAL = 'sequential'
        RANDOM = 'random'
        MULTILINE = 'multiline'


class DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param dict user_defined: An object containing any properties for the
          user-defined response type. The total size of this object cannot exceed 5000
          bytes.
    :param List[ResponseGenericChannel] channels: (optional) An array of objects
          specifying channels for which the response is intended.
    """

    def __init__(
        self,
        response_type: str,
        user_defined: dict,
        *,
        channels: Optional[List['ResponseGenericChannel']] = None,
    ) -> None:
        """
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param dict user_defined: An object containing any properties for the
               user-defined response type. The total size of this object cannot exceed
               5000 bytes.
        :param List[ResponseGenericChannel] channels: (optional) An array of
               objects specifying channels for which the response is intended.
        """
        # pylint: disable=super-init-not-called
        self.response_type = response_type
        self.user_defined = user_defined
        self.channels = channels

    @classmethod
    def from_dict(
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined JSON'
            )
        if (user_defined := _dict.get('user_defined')) is not None:
            args['user_defined'] = user_defined
        else:
            raise ValueError(
                'Required property \'user_defined\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined JSON'
            )
        if (channels := _dict.get('channels')) is not None:
            args['channels'] = [
                ResponseGenericChannel.from_dict(v) for v in channels
            ]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self,
        other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeUserDefined'
    ) -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo(
        DialogNodeOutputGeneric):
    """
    DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the video.
    :param str title: (optional) An optional title to show before the response.
    :param str description: (optional) An optional description to show with the
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
        Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
        :param str source: The `https:` URL of the video.
        :param str title: (optional) An optional title to show before the response.
        :param str description: (optional) An optional description to show with the
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
        cls, _dict: Dict
    ) -> 'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo':
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo object from a json dictionary."""
        args = {}
        if (response_type := _dict.get('response_type')) is not None:
            args['response_type'] = response_type
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo JSON'
            )
        if (source := _dict.get('source')) is not None:
            args['source'] = source
        else:
            raise ValueError(
                'Required property \'source\' not present in DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo JSON'
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
        """Initialize a DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo object from a json dictionary."""
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
        """Return a `str` version of this DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo'
    ) -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(
        self, other: 'DialogNodeOutputGenericDialogNodeOutputResponseTypeVideo'
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
    :param str description: (optional) The description to show with the response.
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
        :param str description: (optional) The description to show with the
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
          present, the response is intended only for a built-in integration and should not
          be handled by an API client.
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
               **channels** is present, the response is intended only for a built-in
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
    :param str dialog_node: (optional) The unique ID of the dialog node that the
          **topic** property is taken from. The **topic** property is populated using the
          value of the dialog node's **title** property.
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
        dialog_node: Optional[str] = None,
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
        :param str dialog_node: (optional) The unique ID of the dialog node that
               the **topic** property is taken from. The **topic** property is populated
               using the value of the dialog node's **title** property.
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
        self.dialog_node = dialog_node
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
        if (dialog_node := _dict.get('dialog_node')) is not None:
            args['dialog_node'] = dialog_node
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
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
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


class RuntimeResponseGenericRuntimeResponseTypeIframe(RuntimeResponseGeneric):
    """
    RuntimeResponseGenericRuntimeResponseTypeIframe.

    :param str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
    :param str source: The `https:` URL of the embeddable content.
    :param str title: (optional) The title or introductory text to show before the
          response.
    :param str description: (optional) The description to show with the response.
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
        :param str description: (optional) The description to show with the
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
    :param str title: (optional) The title or introductory text to show before the
          response.
    :param str description: (optional) The description to show with the response.
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
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the
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
    :param str description: (optional) The description to show with the response.
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
        :param str description: (optional) The description to show with the
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
    :param str description: (optional) The description to show with the response.
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
        :param str description: (optional) The description to show with the
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
