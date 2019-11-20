# coding: utf-8

# (C) Copyright IBM Corp. 2019.
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
The IBM Watson&trade; Assistant service combines machine learning, natural language
understanding, and an integrated dialog editor to create conversation flows between your
apps and your users.
The Assistant v1 API provides authoring methods your application can use to create or
update a workspace.
"""

import json
from .common import get_sdk_headers
from enum import Enum
from ibm_cloud_sdk_core import BaseService
from ibm_cloud_sdk_core import datetime_to_string, string_to_datetime
from ibm_cloud_sdk_core import get_authenticator_from_environment
from ibm_cloud_sdk_core import read_external_sources

##############################################################################
# Service
##############################################################################


class AssistantV1(BaseService):
    """The Assistant V1 service."""

    default_service_url = 'https://gateway.watsonplatform.net/assistant/api'

    def __init__(
            self,
            version,
            authenticator=None,
    ):
        """
        Construct a new client for the Assistant service.

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

        service_url = self.default_service_url
        disable_ssl_verification = False

        config = read_external_sources('assistant')
        if config.get('URL'):
            service_url = config.get('URL')
        if config.get('DISABLE_SSL'):
            disable_ssl_verification = config.get('DISABLE_SSL')

        if not authenticator:
            authenticator = get_authenticator_from_environment('assistant')

        BaseService.__init__(self,
                             service_url=service_url,
                             authenticator=authenticator,
                             disable_ssl_verification=disable_ssl_verification)
        self.version = version

    #########################
    # Message
    #########################

    def message(self,
                workspace_id,
                *,
                input=None,
                intents=None,
                entities=None,
                alternate_intents=None,
                context=None,
                output=None,
                nodes_visited_details=None,
                **kwargs):
        """
        Get response to user input.

        Send user input to a workspace and receive a response.
        **Important:** This method has been superseded by the new v2 runtime API. The v2
        API offers significant advantages, including ease of deployment, automatic state
        management, versioning, and search capabilities. For more information, see the
        [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-api-overview).
        There is no rate limit for this operation.

        :param str workspace_id: Unique identifier of the workspace.
        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param list[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param list[RuntimeEntity] entities: (optional) Entities to use when
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
        :param bool nodes_visited_details: (optional) Whether to include additional
               diagnostic information about the dialog nodes that were visited during
               processing of the message.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if input is not None:
            input = self._convert_model(input)
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if context is not None:
            context = self._convert_model(context)
        if output is not None:
            output = self._convert_model(output)

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'message')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'nodes_visited_details': nodes_visited_details
        }

        data = {
            'input': input,
            'intents': intents,
            'entities': entities,
            'alternate_intents': alternate_intents,
            'context': context,
            'output': output
        }

        url = '/v1/workspaces/{0}/message'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Workspaces
    #########################

    def list_workspaces(self,
                        *,
                        page_limit=None,
                        sort=None,
                        cursor=None,
                        include_audit=None,
                        **kwargs):
        """
        List workspaces.

        List the workspaces associated with a Watson Assistant service instance.
        This operation is limited to 500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned workspaces will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_workspaces')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_workspace(self,
                         *,
                         name=None,
                         description=None,
                         language=None,
                         metadata=None,
                         learning_opt_out=None,
                         system_settings=None,
                         intents=None,
                         entities=None,
                         dialog_nodes=None,
                         counterexamples=None,
                         webhooks=None,
                         **kwargs):
        """
        Create workspace.

        Create a workspace based on component objects. You must provide workspace
        components defining the content of the new workspace.
        This operation is limited to 30 requests per 30 minutes. For more information, see
        **Rate limiting**.

        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param list[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param list[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param list[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param list[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param list[Webhook] webhooks: (optional)
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if system_settings is not None:
            system_settings = self._convert_model(system_settings)
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [self._convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [self._convert_model(x) for x in counterexamples]
        if webhooks is not None:
            webhooks = [self._convert_model(x) for x in webhooks]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_workspace')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'name': name,
            'description': description,
            'language': language,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'webhooks': webhooks
        }

        url = '/v1/workspaces'
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_workspace(self,
                      workspace_id,
                      *,
                      export=None,
                      include_audit=None,
                      sort=None,
                      **kwargs):
        """
        Get information about a workspace.

        Get information about a workspace, optionally including all workspace content.
        With **export**=`false`, this operation is limited to 6000 requests per 5 minutes.
        With **export**=`true`, the limit is 20 requests per 30 minutes. For more
        information, see **Rate limiting**.

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
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_workspace')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit,
            'sort': sort
        }

        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_workspace(self,
                         workspace_id,
                         *,
                         name=None,
                         description=None,
                         language=None,
                         metadata=None,
                         learning_opt_out=None,
                         system_settings=None,
                         intents=None,
                         entities=None,
                         dialog_nodes=None,
                         counterexamples=None,
                         webhooks=None,
                         append=None,
                         **kwargs):
        """
        Update workspace.

        Update an existing workspace with new or modified data. You must provide component
        objects defining the content of the updated workspace.
        This operation is limited to 30 request per 30 minutes. For more information, see
        **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str name: (optional) The name of the workspace. This string cannot
               contain carriage return, newline, or tab characters.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param str language: (optional) The language of the workspace.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param bool learning_opt_out: (optional) Whether training data from the
               workspace (including artifacts such as intents and entities) can be used by
               IBM for general service improvements. `true` indicates that workspace
               training data is not to be used.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param list[CreateIntent] intents: (optional) An array of objects defining
               the intents for the workspace.
        :param list[CreateEntity] entities: (optional) An array of objects
               describing the entities for the workspace.
        :param list[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param list[Counterexample] counterexamples: (optional) An array of objects
               defining input examples that have been marked as irrelevant input.
        :param list[Webhook] webhooks: (optional)
        :param bool append: (optional) Whether the new data is to be appended to
               the existing data in the workspace. If **append**=`false`, elements
               included in the new data completely replace the corresponding existing
               elements, including all subelements. For example, if the new data includes
               **entities** and **append**=`false`, all existing entities in the workspace
               are discarded and replaced with the new entities.
               If **append**=`true`, existing elements are preserved, and the new elements
               are added. If any elements in the new data collide with existing elements,
               the update request fails.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if system_settings is not None:
            system_settings = self._convert_model(system_settings)
        if intents is not None:
            intents = [self._convert_model(x) for x in intents]
        if entities is not None:
            entities = [self._convert_model(x) for x in entities]
        if dialog_nodes is not None:
            dialog_nodes = [self._convert_model(x) for x in dialog_nodes]
        if counterexamples is not None:
            counterexamples = [self._convert_model(x) for x in counterexamples]
        if webhooks is not None:
            webhooks = [self._convert_model(x) for x in webhooks]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_workspace')
        headers.update(sdk_headers)

        params = {'version': self.version, 'append': append}

        data = {
            'name': name,
            'description': description,
            'language': language,
            'metadata': metadata,
            'learning_opt_out': learning_opt_out,
            'system_settings': system_settings,
            'intents': intents,
            'entities': entities,
            'dialog_nodes': dialog_nodes,
            'counterexamples': counterexamples,
            'webhooks': webhooks
        }

        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_workspace(self, workspace_id, **kwargs):
        """
        Delete workspace.

        Delete a workspace from the service instance.
        This operation is limited to 30 requests per 30 minutes. For more information, see
        **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_workspace')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}'.format(*self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Intents
    #########################

    def list_intents(self,
                     workspace_id,
                     *,
                     export=None,
                     page_limit=None,
                     sort=None,
                     cursor=None,
                     include_audit=None,
                     **kwargs):
        """
        List intents.

        List the intents for a workspace.
        With **export**=`false`, this operation is limited to 2000 requests per 30
        minutes. With **export**=`true`, the limit is 400 requests per 30 minutes. For
        more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned intents will be
               sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_intents')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_intent(self,
                      workspace_id,
                      intent,
                      *,
                      description=None,
                      examples=None,
                      **kwargs):
        """
        Create intent.

        Create a new intent.
        If you want to create multiple intents with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 2000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param list[Example] examples: (optional) An array of user input examples
               for the intent.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if examples is not None:
            examples = [self._convert_model(x) for x in examples]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_intent')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'intent': intent,
            'description': description,
            'examples': examples
        }

        url = '/v1/workspaces/{0}/intents'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_intent(self,
                   workspace_id,
                   intent,
                   *,
                   export=None,
                   include_audit=None,
                   **kwargs):
        """
        Get intent.

        Get information about an intent, optionally including all intent content.
        With **export**=`false`, this operation is limited to 6000 requests per 5 minutes.
        With **export**=`true`, the limit is 400 requests per 30 minutes. For more
        information, see **Rate limiting**.

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
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_intent')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/intents/{1}'.format(
            *self._encode_path_vars(workspace_id, intent))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_intent(self,
                      workspace_id,
                      intent,
                      *,
                      new_intent=None,
                      new_description=None,
                      new_examples=None,
                      **kwargs):
        """
        Update intent.

        Update an existing intent with new or modified data. You must provide component
        objects defining the content of the updated intent.
        If you want to update multiple intents with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 2000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str new_intent: (optional) The name of the intent. This string must
               conform to the following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str new_description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param list[Example] new_examples: (optional) An array of user input
               examples for the intent.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if new_examples is not None:
            new_examples = [self._convert_model(x) for x in new_examples]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_intent')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'intent': new_intent,
            'description': new_description,
            'examples': new_examples
        }

        url = '/v1/workspaces/{0}/intents/{1}'.format(
            *self._encode_path_vars(workspace_id, intent))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_intent(self, workspace_id, intent, **kwargs):
        """
        Delete intent.

        Delete an intent from a workspace.
        This operation is limited to 2000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_intent')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/intents/{1}'.format(
            *self._encode_path_vars(workspace_id, intent))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Examples
    #########################

    def list_examples(self,
                      workspace_id,
                      intent,
                      *,
                      page_limit=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List user input examples.

        List the user input examples for an intent, optionally including contextual entity
        mentions.
        This operation is limited to 2500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned examples will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_examples')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_example(self,
                       workspace_id,
                       intent,
                       text,
                       *,
                       mentions=None,
                       **kwargs):
        """
        Create user input example.

        Add a new user input example to an intent.
        If you want to add multiple exaples with a single API call, consider using the
        **[Update intent](#update-intent)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of a user input example. This string must conform
               to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[Mention] mentions: (optional) An array of contextual entity
               mentions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        if mentions is not None:
            mentions = [self._convert_model(x) for x in mentions]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'text': text, 'mentions': mentions}

        url = '/v1/workspaces/{0}/intents/{1}/examples'.format(
            *self._encode_path_vars(workspace_id, intent))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_example(self,
                    workspace_id,
                    intent,
                    text,
                    *,
                    include_audit=None,
                    **kwargs):
        """
        Get user input example.

        Get information about a user input example.
        This operation is limited to 6000 requests per 5 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_example')
        headers.update(sdk_headers)

        params = {'version': self.version, 'include_audit': include_audit}

        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_example(self,
                       workspace_id,
                       intent,
                       text,
                       *,
                       new_text=None,
                       new_mentions=None,
                       **kwargs):
        """
        Update user input example.

        Update the text of a user input example.
        If you want to update multiple examples with a single API call, consider using the
        **[Update intent](#update-intent)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param str new_text: (optional) The text of the user input example. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[Mention] new_mentions: (optional) An array of contextual entity
               mentions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')
        if new_mentions is not None:
            new_mentions = [self._convert_model(x) for x in new_mentions]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'text': new_text, 'mentions': new_mentions}

        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_example(self, workspace_id, intent, text, **kwargs):
        """
        Delete user input example.

        Delete a user input example from an intent.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str intent: The intent name.
        :param str text: The text of the user input example.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if intent is None:
            raise ValueError('intent must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_example')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/intents/{1}/examples/{2}'.format(
            *self._encode_path_vars(workspace_id, intent, text))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Counterexamples
    #########################

    def list_counterexamples(self,
                             workspace_id,
                             *,
                             page_limit=None,
                             sort=None,
                             cursor=None,
                             include_audit=None,
                             **kwargs):
        """
        List counterexamples.

        List the counterexamples for a workspace. Counterexamples are examples that have
        been marked as irrelevant input.
        This operation is limited to 2500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned counterexamples
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'list_counterexamples')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_counterexample(self, workspace_id, text, **kwargs):
        """
        Create counterexample.

        Add a new counterexample to a workspace. Counterexamples are examples that have
        been marked as irrelevant input.
        If you want to add multiple counterexamples with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input marked as irrelevant input. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'create_counterexample')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'text': text}

        url = '/v1/workspaces/{0}/counterexamples'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_counterexample(self,
                           workspace_id,
                           text,
                           *,
                           include_audit=None,
                           **kwargs):
        """
        Get counterexample.

        Get information about a counterexample. Counterexamples are examples that have
        been marked as irrelevant input.
        This operation is limited to 6000 requests per 5 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'get_counterexample')
        headers.update(sdk_headers)

        params = {'version': self.version, 'include_audit': include_audit}

        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_counterexample(self,
                              workspace_id,
                              text,
                              *,
                              new_text=None,
                              **kwargs):
        """
        Update counterexample.

        Update the text of a counterexample. Counterexamples are examples that have been
        marked as irrelevant input.
        If you want to update multiple counterexamples with a single API call, consider
        using the **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param str new_text: (optional) The text of a user input marked as
               irrelevant input. This string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'update_counterexample')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'text': new_text}

        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_counterexample(self, workspace_id, text, **kwargs):
        """
        Delete counterexample.

        Delete a counterexample from a workspace. Counterexamples are examples that have
        been marked as irrelevant input.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str text: The text of a user input counterexample (for example,
               `What are you wearing?`).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if text is None:
            raise ValueError('text must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'delete_counterexample')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/counterexamples/{1}'.format(
            *self._encode_path_vars(workspace_id, text))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Entities
    #########################

    def list_entities(self,
                      workspace_id,
                      *,
                      export=None,
                      page_limit=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List entities.

        List the entities for a workspace.
        With **export**=`false`, this operation is limited to 1000 requests per 30
        minutes. With **export**=`true`, the limit is 200 requests per 30 minutes. For
        more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned entities will
               be sorted. To reverse the sort order, prefix the value with a minus sign
               (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_entities')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_entity(self,
                      workspace_id,
                      entity,
                      *,
                      description=None,
                      metadata=None,
                      fuzzy_match=None,
                      values=None,
                      **kwargs):
        """
        Create entity.

        Create a new entity, or enable a system entity.
        If you want to create multiple entities with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

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
        :param list[CreateValue] values: (optional) An array of objects describing
               the entity values.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if values is not None:
            values = [self._convert_model(x) for x in values]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_entity')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'entity': entity,
            'description': description,
            'metadata': metadata,
            'fuzzy_match': fuzzy_match,
            'values': values
        }

        url = '/v1/workspaces/{0}/entities'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_entity(self,
                   workspace_id,
                   entity,
                   *,
                   export=None,
                   include_audit=None,
                   **kwargs):
        """
        Get entity.

        Get information about an entity, optionally including all entity content.
        With **export**=`false`, this operation is limited to 6000 requests per 5 minutes.
        With **export**=`true`, the limit is 200 requests per 30 minutes. For more
        information, see **Rate limiting**.

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
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_entity')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities/{1}'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_entity(self,
                      workspace_id,
                      entity,
                      *,
                      new_entity=None,
                      new_description=None,
                      new_metadata=None,
                      new_fuzzy_match=None,
                      new_values=None,
                      **kwargs):
        """
        Update entity.

        Update an existing entity with new or modified data. You must provide component
        objects defining the content of the updated entity.
        If you want to update multiple entities with a single API call, consider using the
        **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

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
        :param list[CreateValue] new_values: (optional) An array of objects
               describing the entity values.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if new_values is not None:
            new_values = [self._convert_model(x) for x in new_values]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_entity')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'entity': new_entity,
            'description': new_description,
            'metadata': new_metadata,
            'fuzzy_match': new_fuzzy_match,
            'values': new_values
        }

        url = '/v1/workspaces/{0}/entities/{1}'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_entity(self, workspace_id, entity, **kwargs):
        """
        Delete entity.

        Delete an entity from a workspace, or disable a system entity.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_entity')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/entities/{1}'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Mentions
    #########################

    def list_mentions(self,
                      workspace_id,
                      entity,
                      *,
                      export=None,
                      include_audit=None,
                      **kwargs):
        """
        List entity mentions.

        List mentions for a contextual entity. An entity mention is an occurrence of a
        contextual entity in the context of an intent user input example.
        This operation is limited to 200 requests per 30 minutes. For more information,
        see **Rate limiting**.

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
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_mentions')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities/{1}/mentions'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Values
    #########################

    def list_values(self,
                    workspace_id,
                    entity,
                    *,
                    export=None,
                    page_limit=None,
                    sort=None,
                    cursor=None,
                    include_audit=None,
                    **kwargs):
        """
        List entity values.

        List the values for an entity.
        This operation is limited to 2500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param bool export: (optional) Whether to include all element content in
               the returned data. If **export**=`false`, the returned data includes only
               information about the element itself. If **export**=`true`, all content,
               including subelements, is included.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned entity values
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_values')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities/{1}/values'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_value(self,
                     workspace_id,
                     entity,
                     value,
                     *,
                     metadata=None,
                     type=None,
                     synonyms=None,
                     patterns=None,
                     **kwargs):
        """
        Create entity value.

        Create a new value for an entity.
        If you want to create multiple entity values with a single API call, consider
        using the **[Update entity](#update-entity)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param str type: (optional) Specifies the type of entity value.
        :param list[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_value')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'value': value,
            'metadata': metadata,
            'type': type,
            'synonyms': synonyms,
            'patterns': patterns
        }

        url = '/v1/workspaces/{0}/entities/{1}/values'.format(
            *self._encode_path_vars(workspace_id, entity))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_value(self,
                  workspace_id,
                  entity,
                  value,
                  *,
                  export=None,
                  include_audit=None,
                  **kwargs):
        """
        Get entity value.

        Get information about an entity value.
        This operation is limited to 6000 requests per 5 minutes. For more information,
        see **Rate limiting**.

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
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_value')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'export': export,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_value(self,
                     workspace_id,
                     entity,
                     value,
                     *,
                     new_value=None,
                     new_metadata=None,
                     new_type=None,
                     new_synonyms=None,
                     new_patterns=None,
                     **kwargs):
        """
        Update entity value.

        Update an existing entity value with new or modified data. You must provide
        component objects defining the content of the updated entity value.
        If you want to update multiple entity values with a single API call, consider
        using the **[Update entity](#update-entity)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

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
        :param list[str] new_synonyms: (optional) An array of synonyms for the
               entity value. A value can specify either synonyms or patterns (depending on
               the value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[str] new_patterns: (optional) An array of patterns for the
               entity value. A value can specify either synonyms or patterns (depending on
               the value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_value')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {
            'value': new_value,
            'metadata': new_metadata,
            'type': new_type,
            'synonyms': new_synonyms,
            'patterns': new_patterns
        }

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_value(self, workspace_id, entity, value, **kwargs):
        """
        Delete entity value.

        Delete a value from an entity.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_value')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Synonyms
    #########################

    def list_synonyms(self,
                      workspace_id,
                      entity,
                      value,
                      *,
                      page_limit=None,
                      sort=None,
                      cursor=None,
                      include_audit=None,
                      **kwargs):
        """
        List entity value synonyms.

        List the synonyms for an entity value.
        This operation is limited to 2500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned entity value
               synonyms will be sorted. To reverse the sort order, prefix the value with a
               minus sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_synonyms')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_synonym(self, workspace_id, entity, value, synonym, **kwargs):
        """
        Create entity value synonym.

        Add a new synonym to an entity value.
        If you want to create multiple synonyms with a single API call, consider using the
        **[Update entity](#update-entity)** or **[Update entity
        value](#update-entity-value)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        if synonym is None:
            raise ValueError('synonym must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'create_synonym')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'synonym': synonym}

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms'.format(
            *self._encode_path_vars(workspace_id, entity, value))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_synonym(self,
                    workspace_id,
                    entity,
                    value,
                    synonym,
                    *,
                    include_audit=None,
                    **kwargs):
        """
        Get entity value synonym.

        Get information about a synonym of an entity value.
        This operation is limited to 6000 requests per 5 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        if synonym is None:
            raise ValueError('synonym must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_synonym')
        headers.update(sdk_headers)

        params = {'version': self.version, 'include_audit': include_audit}

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_synonym(self,
                       workspace_id,
                       entity,
                       value,
                       synonym,
                       *,
                       new_synonym=None,
                       **kwargs):
        """
        Update entity value synonym.

        Update an existing entity value synonym with new text.
        If you want to update multiple synonyms with a single API call, consider using the
        **[Update entity](#update-entity)** or **[Update entity
        value](#update-entity-value)** method instead.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param str new_synonym: (optional) The text of the synonym. This string
               must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        if synonym is None:
            raise ValueError('synonym must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'update_synonym')
        headers.update(sdk_headers)

        params = {'version': self.version}

        data = {'synonym': new_synonym}

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_synonym(self, workspace_id, entity, value, synonym, **kwargs):
        """
        Delete entity value synonym.

        Delete a synonym from an entity value.
        This operation is limited to 1000 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str entity: The name of the entity.
        :param str value: The text of the entity value.
        :param str synonym: The text of the synonym.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if entity is None:
            raise ValueError('entity must be provided')
        if value is None:
            raise ValueError('value must be provided')
        if synonym is None:
            raise ValueError('synonym must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_synonym')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/entities/{1}/values/{2}/synonyms/{3}'.format(
            *self._encode_path_vars(workspace_id, entity, value, synonym))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Dialog nodes
    #########################

    def list_dialog_nodes(self,
                          workspace_id,
                          *,
                          page_limit=None,
                          sort=None,
                          cursor=None,
                          include_audit=None,
                          **kwargs):
        """
        List dialog nodes.

        List the dialog nodes for a workspace.
        This operation is limited to 2500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str sort: (optional) The attribute by which returned dialog nodes
               will be sorted. To reverse the sort order, prefix the value with a minus
               sign (`-`).
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_dialog_nodes')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'page_limit': page_limit,
            'sort': sort,
            'cursor': cursor,
            'include_audit': include_audit
        }

        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def create_dialog_node(self,
                           workspace_id,
                           dialog_node,
                           *,
                           description=None,
                           conditions=None,
                           parent=None,
                           previous_sibling=None,
                           output=None,
                           context=None,
                           metadata=None,
                           next_step=None,
                           title=None,
                           type=None,
                           event_name=None,
                           variable=None,
                           actions=None,
                           digress_in=None,
                           digress_out=None,
                           digress_out_slots=None,
                           user_label=None,
                           disambiguation_opt_out=None,
                           **kwargs):
        """
        Create dialog node.

        Create a new dialog node.
        If you want to create multiple dialog nodes with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str description: (optional) The description of the dialog node. This
               string cannot contain carriage return, newline, or tab characters.
        :param str conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str parent: (optional) The ID of the parent dialog node. This
               property is omitted if the dialog node has no parent.
        :param str previous_sibling: (optional) The ID of the previous sibling
               dialog node. This property is omitted if the dialog node has no previous
               sibling.
        :param DialogNodeOutput output: (optional) The output of the dialog node.
               For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param dict context: (optional) The context for the dialog node.
        :param dict metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute
               following this dialog node.
        :param str title: (optional) The alias used to identify the dialog node.
               This string must conform to the following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where
               output is stored.
        :param list[DialogNodeAction] actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str digress_in: (optional) Whether this top-level dialog node can be
               digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned
               to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to
               top-level nodes while filling out slots.
        :param str user_label: (optional) A label that can be displayed externally
               to describe the purpose of the node to users.
        :param bool disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if output is not None:
            output = self._convert_model(output)
        if next_step is not None:
            next_step = self._convert_model(next_step)
        if actions is not None:
            actions = [self._convert_model(x) for x in actions]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'create_dialog_node')
        headers.update(sdk_headers)

        params = {'version': self.version}

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
            'disambiguation_opt_out': disambiguation_opt_out
        }

        url = '/v1/workspaces/{0}/dialog_nodes'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def get_dialog_node(self,
                        workspace_id,
                        dialog_node,
                        *,
                        include_audit=None,
                        **kwargs):
        """
        Get dialog node.

        Get information about a dialog node.
        This operation is limited to 6000 requests per 5 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param bool include_audit: (optional) Whether to include the audit
               properties (`created` and `updated` timestamps) in the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'get_dialog_node')
        headers.update(sdk_headers)

        params = {'version': self.version, 'include_audit': include_audit}

        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def update_dialog_node(self,
                           workspace_id,
                           dialog_node,
                           *,
                           new_dialog_node=None,
                           new_description=None,
                           new_conditions=None,
                           new_parent=None,
                           new_previous_sibling=None,
                           new_output=None,
                           new_context=None,
                           new_metadata=None,
                           new_next_step=None,
                           new_title=None,
                           new_type=None,
                           new_event_name=None,
                           new_variable=None,
                           new_actions=None,
                           new_digress_in=None,
                           new_digress_out=None,
                           new_digress_out_slots=None,
                           new_user_label=None,
                           new_disambiguation_opt_out=None,
                           **kwargs):
        """
        Update dialog node.

        Update an existing dialog node with new or modified data.
        If you want to update multiple dialog nodes with a single API call, consider using
        the **[Update workspace](#update-workspace)** method instead.
        This operation is limited to 500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param str new_dialog_node: (optional) The dialog node ID. This string must
               conform to the following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str new_description: (optional) The description of the dialog node.
               This string cannot contain carriage return, newline, or tab characters.
        :param str new_conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str new_parent: (optional) The ID of the parent dialog node. This
               property is omitted if the dialog node has no parent.
        :param str new_previous_sibling: (optional) The ID of the previous sibling
               dialog node. This property is omitted if the dialog node has no previous
               sibling.
        :param DialogNodeOutput new_output: (optional) The output of the dialog
               node. For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param dict new_context: (optional) The context for the dialog node.
        :param dict new_metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep new_next_step: (optional) The next step to
               execute following this dialog node.
        :param str new_title: (optional) The alias used to identify the dialog
               node. This string must conform to the following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str new_type: (optional) How the dialog node is processed.
        :param str new_event_name: (optional) How an `event_handler` node is
               processed.
        :param str new_variable: (optional) The location in the dialog context
               where output is stored.
        :param list[DialogNodeAction] new_actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str new_digress_in: (optional) Whether this top-level dialog node
               can be digressed into.
        :param str new_digress_out: (optional) Whether this dialog node can be
               returned to after a digression.
        :param str new_digress_out_slots: (optional) Whether the user can digress
               to top-level nodes while filling out slots.
        :param str new_user_label: (optional) A label that can be displayed
               externally to describe the purpose of the node to users.
        :param bool new_disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')
        if new_output is not None:
            new_output = self._convert_model(new_output)
        if new_next_step is not None:
            new_next_step = self._convert_model(new_next_step)
        if new_actions is not None:
            new_actions = [self._convert_model(x) for x in new_actions]

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'update_dialog_node')
        headers.update(sdk_headers)

        params = {'version': self.version}

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
            'disambiguation_opt_out': new_disambiguation_opt_out
        }

        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       data=data,
                                       accept_json=True)
        response = self.send(request)
        return response

    def delete_dialog_node(self, workspace_id, dialog_node, **kwargs):
        """
        Delete dialog node.

        Delete a dialog node from a workspace.
        This operation is limited to 500 requests per 30 minutes. For more information,
        see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str dialog_node: The dialog node ID (for example, `get_order`).
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')
        if dialog_node is None:
            raise ValueError('dialog_node must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1',
                                      'delete_dialog_node')
        headers.update(sdk_headers)

        params = {'version': self.version}

        url = '/v1/workspaces/{0}/dialog_nodes/{1}'.format(
            *self._encode_path_vars(workspace_id, dialog_node))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # Logs
    #########################

    def list_logs(self,
                  workspace_id,
                  *,
                  sort=None,
                  filter=None,
                  page_limit=None,
                  cursor=None,
                  **kwargs):
        """
        List log events in a workspace.

        List the events from the log of a specific workspace.
        If **cursor** is not specified, this operation is limited to 40 requests per 30
        minutes. If **cursor** is specified, the limit is 120 requests per minute. For
        more information, see **Rate limiting**.

        :param str workspace_id: Unique identifier of the workspace.
        :param str sort: (optional) How to sort the returned log events. You can
               sort by **request_timestamp**. To reverse the sort order, prefix the
               parameter value with a minus sign (`-`).
        :param str filter: (optional) A cacheable parameter that limits the results
               to those matching the specified filter. For more information, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-filter-reference#filter-reference).
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if workspace_id is None:
            raise ValueError('workspace_id must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_logs')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'sort': sort,
            'filter': filter,
            'page_limit': page_limit,
            'cursor': cursor
        }

        url = '/v1/workspaces/{0}/logs'.format(
            *self._encode_path_vars(workspace_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    def list_all_logs(self,
                      filter,
                      *,
                      sort=None,
                      page_limit=None,
                      cursor=None,
                      **kwargs):
        """
        List log events in all workspaces.

        List the events from the logs of all workspaces in the service instance.
        If **cursor** is not specified, this operation is limited to 40 requests per 30
        minutes. If **cursor** is specified, the limit is 120 requests per minute. For
        more information, see **Rate limiting**.

        :param str filter: A cacheable parameter that limits the results to those
               matching the specified filter. You must specify a filter query that
               includes a value for `language`, as well as a value for
               `request.context.system.assistant_id`, `workspace_id`, or
               `request.context.metadata.deployment`. For more information, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-filter-reference#filter-reference).
        :param str sort: (optional) How to sort the returned log events. You can
               sort by **request_timestamp**. To reverse the sort order, prefix the
               parameter value with a minus sign (`-`).
        :param int page_limit: (optional) The number of records to return in each
               page of results.
        :param str cursor: (optional) A token identifying the page of results to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if filter is None:
            raise ValueError('filter must be provided')

        headers = {}
        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        sdk_headers = get_sdk_headers('conversation', 'V1', 'list_all_logs')
        headers.update(sdk_headers)

        params = {
            'version': self.version,
            'filter': filter,
            'sort': sort,
            'page_limit': page_limit,
            'cursor': cursor
        }

        url = '/v1/logs'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response

    #########################
    # User data
    #########################

    def delete_user_data(self, customer_id, **kwargs):
        """
        Delete labeled data.

        Deletes all data associated with a specified customer ID. The method has no effect
        if no data is associated with the customer ID.
        You associate a customer ID with data by passing the `X-Watson-Metadata` header
        with a request that passes data. For more information about personal data and
        customer IDs, see [Information
        security](https://cloud.ibm.com/docs/services/assistant?topic=assistant-information-security#information-security).

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
        sdk_headers = get_sdk_headers('conversation', 'V1', 'delete_user_data')
        headers.update(sdk_headers)

        params = {'version': self.version, 'customer_id': customer_id}

        url = '/v1/user_data'
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers,
                                       params=params,
                                       accept_json=True)
        response = self.send(request)
        return response


class ListWorkspacesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned workspaces will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """
        NAME = 'name'
        UPDATED = 'updated'


class GetWorkspaceEnums(object):

    class Sort(Enum):
        """
        Indicates how the returned workspace data will be sorted. This parameter is valid
        only if **export**=`true`. Specify `sort=stable` to sort all workspace objects by
        unique identifier, in ascending alphabetical order.
        """
        STABLE = 'stable'


class ListIntentsEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned intents will be sorted. To reverse the sort order,
        prefix the value with a minus sign (`-`).
        """
        INTENT = 'intent'
        UPDATED = 'updated'


class ListExamplesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned examples will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """
        TEXT = 'text'
        UPDATED = 'updated'


class ListCounterexamplesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned counterexamples will be sorted. To reverse the
        sort order, prefix the value with a minus sign (`-`).
        """
        TEXT = 'text'
        UPDATED = 'updated'


class ListEntitiesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned entities will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """
        ENTITY = 'entity'
        UPDATED = 'updated'


class ListValuesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned entity values will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """
        VALUE = 'value'
        UPDATED = 'updated'


class ListSynonymsEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned entity value synonyms will be sorted. To reverse
        the sort order, prefix the value with a minus sign (`-`).
        """
        SYNONYM = 'synonym'
        UPDATED = 'updated'


class ListDialogNodesEnums(object):

    class Sort(Enum):
        """
        The attribute by which returned dialog nodes will be sorted. To reverse the sort
        order, prefix the value with a minus sign (`-`).
        """
        DIALOG_NODE = 'dialog_node'
        UPDATED = 'updated'


##############################################################################
# Models
##############################################################################


class CaptureGroup():
    """
    A recognized capture group for a pattern-based entity.

    :attr str group: A recognized capture group for the entity.
    :attr list[int] location: (optional) Zero-based character offsets that indicate
          where the entity value begins and ends in the input text.
    """

    def __init__(self, group, *, location=None):
        """
        Initialize a CaptureGroup object.

        :param str group: A recognized capture group for the entity.
        :param list[int] location: (optional) Zero-based character offsets that
               indicate where the entity value begins and ends in the input text.
        """
        self.group = group
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CaptureGroup object from a json dictionary."""
        args = {}
        valid_keys = ['group', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CaptureGroup: '
                + ', '.join(bad_keys))
        if 'group' in _dict:
            args['group'] = _dict.get('group')
        else:
            raise ValueError(
                'Required property \'group\' not present in CaptureGroup JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'group') and self.group is not None:
            _dict['group'] = self.group
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def __str__(self):
        """Return a `str` version of this CaptureGroup object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Context():
    """
    State information for the conversation. To maintain state, include the context from
    the previous response.

    :attr str conversation_id: (optional) The unique identifier of the conversation.
    :attr SystemResponse system: (optional) For internal use only.
    :attr MessageContextMetadata metadata: (optional) Metadata related to the
          message.
    """

    def __init__(self,
                 *,
                 conversation_id=None,
                 system=None,
                 metadata=None,
                 **kwargs):
        """
        Initialize a Context object.

        :param str conversation_id: (optional) The unique identifier of the
               conversation.
        :param SystemResponse system: (optional) For internal use only.
        :param MessageContextMetadata metadata: (optional) Metadata related to the
               message.
        :param **kwargs: (optional) Any additional properties.
        """
        self.conversation_id = conversation_id
        self.system = system
        self.metadata = metadata
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Context object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'conversation_id' in _dict:
            args['conversation_id'] = _dict.get('conversation_id')
            del xtra['conversation_id']
        if 'system' in _dict:
            args['system'] = SystemResponse._from_dict(_dict.get('system'))
            del xtra['system']
        if 'metadata' in _dict:
            args['metadata'] = MessageContextMetadata._from_dict(
                _dict.get('metadata'))
            del xtra['metadata']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'conversation_id') and self.conversation_id is not None:
            _dict['conversation_id'] = self.conversation_id
        if hasattr(self, 'system') and self.system is not None:
            _dict['system'] = self.system._to_dict()
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'conversation_id', 'system', 'metadata'}
        if not hasattr(self, '_additionalProperties'):
            super(Context, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(Context, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this Context object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Counterexample():
    """
    Counterexample.

    :attr str text: The text of a user input marked as irrelevant input. This string
          must conform to the following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self, text, *, created=None, updated=None):
        """
        Initialize a Counterexample object.

        :param str text: The text of a user input marked as irrelevant input. This
               string must conform to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        """
        self.text = text
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Counterexample object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'created', 'updated']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Counterexample: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Counterexample JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this Counterexample object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CounterexampleCollection():
    """
    CounterexampleCollection.

    :attr list[Counterexample] counterexamples: An array of objects describing the
          examples marked as irrelevant input.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, counterexamples, pagination):
        """
        Initialize a CounterexampleCollection object.

        :param list[Counterexample] counterexamples: An array of objects describing
               the examples marked as irrelevant input.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.counterexamples = counterexamples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CounterexampleCollection object from a json dictionary."""
        args = {}
        valid_keys = ['counterexamples', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CounterexampleCollection: '
                + ', '.join(bad_keys))
        if 'counterexamples' in _dict:
            args['counterexamples'] = [
                Counterexample._from_dict(x)
                for x in (_dict.get('counterexamples'))
            ]
        else:
            raise ValueError(
                'Required property \'counterexamples\' not present in CounterexampleCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in CounterexampleCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self,
                   'counterexamples') and self.counterexamples is not None:
            _dict['counterexamples'] = [
                x._to_dict() for x in self.counterexamples
            ]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this CounterexampleCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateEntity():
    """
    CreateEntity.

    :attr str entity: The name of the entity. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, and hyphen characters.
          - If you specify an entity name beginning with the reserved prefix `sys-`, it
          must be the name of a system entity that you want to enable. (Any entity content
          specified with the request is ignored.).
    :attr str description: (optional) The description of the entity. This string
          cannot contain carriage return, newline, or tab characters.
    :attr dict metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether to use fuzzy matching for the entity.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :attr list[CreateValue] values: (optional) An array of objects describing the
          entity values.
    """

    def __init__(self,
                 entity,
                 *,
                 description=None,
                 metadata=None,
                 fuzzy_match=None,
                 created=None,
                 updated=None,
                 values=None):
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
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        :param list[CreateValue] values: (optional) An array of objects describing
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
    def _from_dict(cls, _dict):
        """Initialize a CreateEntity object from a json dictionary."""
        args = {}
        valid_keys = [
            'entity', 'description', 'metadata', 'fuzzy_match', 'created',
            'updated', 'values'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CreateEntity: '
                + ', '.join(bad_keys))
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in CreateEntity JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict.get('fuzzy_match')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'values' in _dict:
            args['values'] = [
                CreateValue._from_dict(x) for x in (_dict.get('values'))
            ]
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateIntent():
    """
    CreateIntent.

    :attr str intent: The name of the intent. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
          characters.
          - It cannot begin with the reserved prefix `sys-`.
    :attr str description: (optional) The description of the intent. This string
          cannot contain carriage return, newline, or tab characters.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :attr list[Example] examples: (optional) An array of user input examples for the
          intent.
    """

    def __init__(self,
                 intent,
                 *,
                 description=None,
                 created=None,
                 updated=None,
                 examples=None):
        """
        Initialize a CreateIntent object.

        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        :param list[Example] examples: (optional) An array of user input examples
               for the intent.
        """
        self.intent = intent
        self.description = description
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateIntent object from a json dictionary."""
        args = {}
        valid_keys = ['intent', 'description', 'created', 'updated', 'examples']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CreateIntent: '
                + ', '.join(bad_keys))
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in CreateIntent JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateIntent object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class CreateValue():
    """
    CreateValue.

    :attr str value: The text of the entity value. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr dict metadata: (optional) Any metadata related to the entity value.
    :attr str type: (optional) Specifies the type of entity value.
    :attr list[str] synonyms: (optional) An array of synonyms for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A synonym must conform to the following resrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr list[str] patterns: (optional) An array of patterns for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A pattern is a regular expression; for more information about how
          to specify a pattern, see the
          [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self,
                 value,
                 *,
                 metadata=None,
                 type=None,
                 synonyms=None,
                 patterns=None,
                 created=None,
                 updated=None):
        """
        Initialize a CreateValue object.

        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param str type: (optional) Specifies the type of entity value.
        :param list[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        """
        self.value = value
        self.metadata = metadata
        self.type = type
        self.synonyms = synonyms
        self.patterns = patterns
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CreateValue object from a json dictionary."""
        args = {}
        valid_keys = [
            'value', 'metadata', 'type', 'synonyms', 'patterns', 'created',
            'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class CreateValue: '
                + ', '.join(bad_keys))
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in CreateValue JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'synonyms' in _dict:
            args['synonyms'] = _dict.get('synonyms')
        if 'patterns' in _dict:
            args['patterns'] = _dict.get('patterns')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this CreateValue object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        Specifies the type of entity value.
        """
        SYNONYMS = "synonyms"
        PATTERNS = "patterns"


class DialogNode():
    """
    DialogNode.

    :attr str dialog_node: The dialog node ID. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot
          characters.
    :attr str description: (optional) The description of the dialog node. This
          string cannot contain carriage return, newline, or tab characters.
    :attr str conditions: (optional) The condition that will trigger the dialog
          node. This string cannot contain carriage return, newline, or tab characters.
    :attr str parent: (optional) The ID of the parent dialog node. This property is
          omitted if the dialog node has no parent.
    :attr str previous_sibling: (optional) The ID of the previous sibling dialog
          node. This property is omitted if the dialog node has no previous sibling.
    :attr DialogNodeOutput output: (optional) The output of the dialog node. For
          more information about how to specify dialog node output, see the
          [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
    :attr dict context: (optional) The context for the dialog node.
    :attr dict metadata: (optional) The metadata for the dialog node.
    :attr DialogNodeNextStep next_step: (optional) The next step to execute
          following this dialog node.
    :attr str title: (optional) The alias used to identify the dialog node. This
          string must conform to the following restrictions:
          - It can contain only Unicode alphanumeric, space, underscore, hyphen, and dot
          characters.
    :attr str type: (optional) How the dialog node is processed.
    :attr str event_name: (optional) How an `event_handler` node is processed.
    :attr str variable: (optional) The location in the dialog context where output
          is stored.
    :attr list[DialogNodeAction] actions: (optional) An array of objects describing
          any actions to be invoked by the dialog node.
    :attr str digress_in: (optional) Whether this top-level dialog node can be
          digressed into.
    :attr str digress_out: (optional) Whether this dialog node can be returned to
          after a digression.
    :attr str digress_out_slots: (optional) Whether the user can digress to
          top-level nodes while filling out slots.
    :attr str user_label: (optional) A label that can be displayed externally to
          describe the purpose of the node to users.
    :attr bool disambiguation_opt_out: (optional) Whether the dialog node should be
          excluded from disambiguation suggestions.
    :attr bool disabled: (optional) For internal use only.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self,
                 dialog_node,
                 *,
                 description=None,
                 conditions=None,
                 parent=None,
                 previous_sibling=None,
                 output=None,
                 context=None,
                 metadata=None,
                 next_step=None,
                 title=None,
                 type=None,
                 event_name=None,
                 variable=None,
                 actions=None,
                 digress_in=None,
                 digress_out=None,
                 digress_out_slots=None,
                 user_label=None,
                 disambiguation_opt_out=None,
                 disabled=None,
                 created=None,
                 updated=None):
        """
        Initialize a DialogNode object.

        :param str dialog_node: The dialog node ID. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str description: (optional) The description of the dialog node. This
               string cannot contain carriage return, newline, or tab characters.
        :param str conditions: (optional) The condition that will trigger the
               dialog node. This string cannot contain carriage return, newline, or tab
               characters.
        :param str parent: (optional) The ID of the parent dialog node. This
               property is omitted if the dialog node has no parent.
        :param str previous_sibling: (optional) The ID of the previous sibling
               dialog node. This property is omitted if the dialog node has no previous
               sibling.
        :param DialogNodeOutput output: (optional) The output of the dialog node.
               For more information about how to specify dialog node output, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-dialog-overview#dialog-overview-responses).
        :param dict context: (optional) The context for the dialog node.
        :param dict metadata: (optional) The metadata for the dialog node.
        :param DialogNodeNextStep next_step: (optional) The next step to execute
               following this dialog node.
        :param str title: (optional) The alias used to identify the dialog node.
               This string must conform to the following restrictions:
               - It can contain only Unicode alphanumeric, space, underscore, hyphen, and
               dot characters.
        :param str type: (optional) How the dialog node is processed.
        :param str event_name: (optional) How an `event_handler` node is processed.
        :param str variable: (optional) The location in the dialog context where
               output is stored.
        :param list[DialogNodeAction] actions: (optional) An array of objects
               describing any actions to be invoked by the dialog node.
        :param str digress_in: (optional) Whether this top-level dialog node can be
               digressed into.
        :param str digress_out: (optional) Whether this dialog node can be returned
               to after a digression.
        :param str digress_out_slots: (optional) Whether the user can digress to
               top-level nodes while filling out slots.
        :param str user_label: (optional) A label that can be displayed externally
               to describe the purpose of the node to users.
        :param bool disambiguation_opt_out: (optional) Whether the dialog node
               should be excluded from disambiguation suggestions.
        :param bool disabled: (optional) For internal use only.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
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
    def _from_dict(cls, _dict):
        """Initialize a DialogNode object from a json dictionary."""
        args = {}
        valid_keys = [
            'dialog_node', 'description', 'conditions', 'parent',
            'previous_sibling', 'output', 'context', 'metadata', 'next_step',
            'title', 'type', 'event_name', 'variable', 'actions', 'digress_in',
            'digress_out', 'digress_out_slots', 'user_label',
            'disambiguation_opt_out', 'disabled', 'created', 'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNode: '
                + ', '.join(bad_keys))
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        else:
            raise ValueError(
                'Required property \'dialog_node\' not present in DialogNode JSON'
            )
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'conditions' in _dict:
            args['conditions'] = _dict.get('conditions')
        if 'parent' in _dict:
            args['parent'] = _dict.get('parent')
        if 'previous_sibling' in _dict:
            args['previous_sibling'] = _dict.get('previous_sibling')
        if 'output' in _dict:
            args['output'] = DialogNodeOutput._from_dict(_dict.get('output'))
        if 'context' in _dict:
            args['context'] = _dict.get('context')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'next_step' in _dict:
            args['next_step'] = DialogNodeNextStep._from_dict(
                _dict.get('next_step'))
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'event_name' in _dict:
            args['event_name'] = _dict.get('event_name')
        if 'variable' in _dict:
            args['variable'] = _dict.get('variable')
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in (_dict.get('actions'))
            ]
        if 'digress_in' in _dict:
            args['digress_in'] = _dict.get('digress_in')
        if 'digress_out' in _dict:
            args['digress_out'] = _dict.get('digress_out')
        if 'digress_out_slots' in _dict:
            args['digress_out_slots'] = _dict.get('digress_out_slots')
        if 'user_label' in _dict:
            args['user_label'] = _dict.get('user_label')
        if 'disambiguation_opt_out' in _dict:
            args['disambiguation_opt_out'] = _dict.get('disambiguation_opt_out')
        if 'disabled' in _dict:
            args['disabled'] = _dict.get('disabled')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
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
            _dict['output'] = self.output._to_dict()
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'next_step') and self.next_step is not None:
            _dict['next_step'] = self.next_step._to_dict()
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'event_name') and self.event_name is not None:
            _dict['event_name'] = self.event_name
        if hasattr(self, 'variable') and self.variable is not None:
            _dict['variable'] = self.variable
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x._to_dict() for x in self.actions]
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
        if hasattr(self, 'disabled') and self.disabled is not None:
            _dict['disabled'] = self.disabled
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNode object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        How the dialog node is processed.
        """
        STANDARD = "standard"
        EVENT_HANDLER = "event_handler"
        FRAME = "frame"
        SLOT = "slot"
        RESPONSE_CONDITION = "response_condition"
        FOLDER = "folder"

    class EventNameEnum(Enum):
        """
        How an `event_handler` node is processed.
        """
        FOCUS = "focus"
        INPUT = "input"
        FILLED = "filled"
        VALIDATE = "validate"
        FILLED_MULTIPLE = "filled_multiple"
        GENERIC = "generic"
        NOMATCH = "nomatch"
        NOMATCH_RESPONSES_DEPLETED = "nomatch_responses_depleted"
        DIGRESSION_RETURN_PROMPT = "digression_return_prompt"

    class DigressInEnum(Enum):
        """
        Whether this top-level dialog node can be digressed into.
        """
        NOT_AVAILABLE = "not_available"
        RETURNS = "returns"
        DOES_NOT_RETURN = "does_not_return"

    class DigressOutEnum(Enum):
        """
        Whether this dialog node can be returned to after a digression.
        """
        ALLOW_RETURNING = "allow_returning"
        ALLOW_ALL = "allow_all"
        ALLOW_ALL_NEVER_RETURN = "allow_all_never_return"

    class DigressOutSlotsEnum(Enum):
        """
        Whether the user can digress to top-level nodes while filling out slots.
        """
        NOT_ALLOWED = "not_allowed"
        ALLOW_RETURNING = "allow_returning"
        ALLOW_ALL = "allow_all"


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
                 name,
                 result_variable,
                 *,
                 type=None,
                 parameters=None,
                 credentials=None):
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
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeAction object from a json dictionary."""
        args = {}
        valid_keys = [
            'name', 'type', 'parameters', 'result_variable', 'credentials'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeAction: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this DialogNodeAction object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        The type of action to invoke.
        """
        CLIENT = "client"
        SERVER = "server"
        CLOUD_FUNCTION = "cloud_function"
        WEB_ACTION = "web_action"
        WEBHOOK = "webhook"


class DialogNodeCollection():
    """
    An array of dialog nodes.

    :attr list[DialogNode] dialog_nodes: An array of objects describing the dialog
          nodes defined for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, dialog_nodes, pagination):
        """
        Initialize a DialogNodeCollection object.

        :param list[DialogNode] dialog_nodes: An array of objects describing the
               dialog nodes defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.dialog_nodes = dialog_nodes
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeCollection object from a json dictionary."""
        args = {}
        valid_keys = ['dialog_nodes', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeCollection: '
                + ', '.join(bad_keys))
        if 'dialog_nodes' in _dict:
            args['dialog_nodes'] = [
                DialogNode._from_dict(x) for x in (_dict.get('dialog_nodes'))
            ]
        else:
            raise ValueError(
                'Required property \'dialog_nodes\' not present in DialogNodeCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in DialogNodeCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_nodes') and self.dialog_nodes is not None:
            _dict['dialog_nodes'] = [x._to_dict() for x in self.dialog_nodes]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeNextStep():
    """
    The next step to execute following this dialog node.

    :attr str behavior: What happens after the dialog node completes. The valid
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
    :attr str dialog_node: (optional) The ID of the dialog node to process next.
          This parameter is required if **behavior**=`jump_to`.
    :attr str selector: (optional) Which part of the dialog node to process next.
    """

    def __init__(self, behavior, *, dialog_node=None, selector=None):
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
        :param str dialog_node: (optional) The ID of the dialog node to process
               next. This parameter is required if **behavior**=`jump_to`.
        :param str selector: (optional) Which part of the dialog node to process
               next.
        """
        self.behavior = behavior
        self.dialog_node = dialog_node
        self.selector = selector

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeNextStep object from a json dictionary."""
        args = {}
        valid_keys = ['behavior', 'dialog_node', 'selector']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeNextStep: '
                + ', '.join(bad_keys))
        if 'behavior' in _dict:
            args['behavior'] = _dict.get('behavior')
        else:
            raise ValueError(
                'Required property \'behavior\' not present in DialogNodeNextStep JSON'
            )
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        if 'selector' in _dict:
            args['selector'] = _dict.get('selector')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'behavior') and self.behavior is not None:
            _dict['behavior'] = self.behavior
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'selector') and self.selector is not None:
            _dict['selector'] = self.selector
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeNextStep object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class BehaviorEnum(Enum):
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
        GET_USER_INPUT = "get_user_input"
        SKIP_USER_INPUT = "skip_user_input"
        JUMP_TO = "jump_to"
        REPROMPT = "reprompt"
        SKIP_SLOT = "skip_slot"
        SKIP_ALL_SLOTS = "skip_all_slots"

    class SelectorEnum(Enum):
        """
        Which part of the dialog node to process next.
        """
        CONDITION = "condition"
        CLIENT = "client"
        USER_INPUT = "user_input"
        BODY = "body"


class DialogNodeOutput():
    """
    The output of the dialog node. For more information about how to specify dialog node
    output, see the
    [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-dialog-overview#dialog-overview-responses).

    :attr list[DialogNodeOutputGeneric] generic: (optional) An array of objects
          describing the output defined for the dialog node.
    :attr DialogNodeOutputModifiers modifiers: (optional) Options that modify how
          specified output is handled.
    """

    def __init__(self, *, generic=None, modifiers=None, **kwargs):
        """
        Initialize a DialogNodeOutput object.

        :param list[DialogNodeOutputGeneric] generic: (optional) An array of
               objects describing the output defined for the dialog node.
        :param DialogNodeOutputModifiers modifiers: (optional) Options that modify
               how specified output is handled.
        :param **kwargs: (optional) Any additional properties.
        """
        self.generic = generic
        self.modifiers = modifiers
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutput object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'generic' in _dict:
            args['generic'] = [
                DialogNodeOutputGeneric._from_dict(x)
                for x in (_dict.get('generic'))
            ]
            del xtra['generic']
        if 'modifiers' in _dict:
            args['modifiers'] = DialogNodeOutputModifiers._from_dict(
                _dict.get('modifiers'))
            del xtra['modifiers']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'generic') and self.generic is not None:
            _dict['generic'] = [x._to_dict() for x in self.generic]
        if hasattr(self, 'modifiers') and self.modifiers is not None:
            _dict['modifiers'] = self.modifiers._to_dict()
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'generic', 'modifiers'}
        if not hasattr(self, '_additionalProperties'):
            super(DialogNodeOutput, self).__setattr__('_additionalProperties',
                                                      set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(DialogNodeOutput, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this DialogNodeOutput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputGeneric():
    """
    DialogNodeOutputGeneric.

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
          **Note:** The **search_skill** response type is available only for Plus and
          Premium users, and is used only by the v2 runtime API.
    :attr list[DialogNodeOutputTextValuesElement] values: (optional) A list of one
          or more objects defining text responses. Required when **response_type**=`text`.
    :attr str selection_policy: (optional) How a response is selected from the list,
          if more than one response is specified. Valid only when
          **response_type**=`text`.
    :attr str delimiter: (optional) The delimiter to use as a separator between
          responses when `selection_policy`=`multiline`.
    :attr int time: (optional) How long to pause, in milliseconds. The valid values
          are from 0 to 10000. Valid only when **response_type**=`pause`.
    :attr bool typing: (optional) Whether to send a "user is typing" event during
          the pause. Ignored if the channel does not support this event. Valid only when
          **response_type**=`pause`.
    :attr str source: (optional) The URL of the image. Required when
          **response_type**=`image`.
    :attr str title: (optional) An optional title to show before the response. Valid
          only when **response_type**=`image` or `option`.
    :attr str description: (optional) An optional description to show with the
          response. Valid only when **response_type**=`image` or `option`.
    :attr str preference: (optional) The preferred type of control to display, if
          supported by the channel. Valid only when **response_type**=`option`.
    :attr list[DialogNodeOutputOptionsElement] options: (optional) An array of
          objects describing the options from which the user can choose. You can include
          up to 20 options. Required when **response_type**=`option`.
    :attr str message_to_human_agent: (optional) An optional message to be sent to
          the human agent who will be taking over the conversation. Valid only when
          **reponse_type**=`connect_to_agent`.
    :attr str query: (optional) The text of the search query. This can be either a
          natural-language query or a query that uses the Discovery query language syntax,
          depending on the value of the **query_type** property. For more information, see
          the [Discovery service
          documentation](https://cloud.ibm.com/docs/services/discovery/query-operators.html#query-operators).
          Required when **response_type**=`search_skill`.
    :attr str query_type: (optional) The type of the search query. Required when
          **response_type**=`search_skill`.
    :attr str filter: (optional) An optional filter that narrows the set of
          documents to be searched. For more information, see the [Discovery service
          documentation]([Discovery service
          documentation](https://cloud.ibm.com/docs/services/discovery/query-parameters.html#filter).
    :attr str discovery_version: (optional) The version of the Discovery service API
          to use for the query.
    """

    def __init__(self,
                 response_type,
                 *,
                 values=None,
                 selection_policy=None,
                 delimiter=None,
                 time=None,
                 typing=None,
                 source=None,
                 title=None,
                 description=None,
                 preference=None,
                 options=None,
                 message_to_human_agent=None,
                 query=None,
                 query_type=None,
                 filter=None,
                 discovery_version=None):
        """
        Initialize a DialogNodeOutputGeneric object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
               **Note:** The **search_skill** response type is available only for Plus and
               Premium users, and is used only by the v2 runtime API.
        :param list[DialogNodeOutputTextValuesElement] values: (optional) A list of
               one or more objects defining text responses. Required when
               **response_type**=`text`.
        :param str selection_policy: (optional) How a response is selected from the
               list, if more than one response is specified. Valid only when
               **response_type**=`text`.
        :param str delimiter: (optional) The delimiter to use as a separator
               between responses when `selection_policy`=`multiline`.
        :param int time: (optional) How long to pause, in milliseconds. The valid
               values are from 0 to 10000. Valid only when **response_type**=`pause`.
        :param bool typing: (optional) Whether to send a "user is typing" event
               during the pause. Ignored if the channel does not support this event. Valid
               only when **response_type**=`pause`.
        :param str source: (optional) The URL of the image. Required when
               **response_type**=`image`.
        :param str title: (optional) An optional title to show before the response.
               Valid only when **response_type**=`image` or `option`.
        :param str description: (optional) An optional description to show with the
               response. Valid only when **response_type**=`image` or `option`.
        :param str preference: (optional) The preferred type of control to display,
               if supported by the channel. Valid only when **response_type**=`option`.
        :param list[DialogNodeOutputOptionsElement] options: (optional) An array of
               objects describing the options from which the user can choose. You can
               include up to 20 options. Required when **response_type**=`option`.
        :param str message_to_human_agent: (optional) An optional message to be
               sent to the human agent who will be taking over the conversation. Valid
               only when **reponse_type**=`connect_to_agent`.
        :param str query: (optional) The text of the search query. This can be
               either a natural-language query or a query that uses the Discovery query
               language syntax, depending on the value of the **query_type** property. For
               more information, see the [Discovery service
               documentation](https://cloud.ibm.com/docs/services/discovery/query-operators.html#query-operators).
               Required when **response_type**=`search_skill`.
        :param str query_type: (optional) The type of the search query. Required
               when **response_type**=`search_skill`.
        :param str filter: (optional) An optional filter that narrows the set of
               documents to be searched. For more information, see the [Discovery service
               documentation]([Discovery service
               documentation](https://cloud.ibm.com/docs/services/discovery/query-parameters.html#filter).
        :param str discovery_version: (optional) The version of the Discovery
               service API to use for the query.
        """
        self.response_type = response_type
        self.values = values
        self.selection_policy = selection_policy
        self.delimiter = delimiter
        self.time = time
        self.typing = typing
        self.source = source
        self.title = title
        self.description = description
        self.preference = preference
        self.options = options
        self.message_to_human_agent = message_to_human_agent
        self.query = query
        self.query_type = query_type
        self.filter = filter
        self.discovery_version = discovery_version

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputGeneric object from a json dictionary."""
        args = {}
        valid_keys = [
            'response_type', 'values', 'selection_policy', 'delimiter', 'time',
            'typing', 'source', 'title', 'description', 'preference', 'options',
            'message_to_human_agent', 'query', 'query_type', 'filter',
            'discovery_version'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeOutputGeneric: '
                + ', '.join(bad_keys))
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogNodeOutputGeneric JSON'
            )
        if 'values' in _dict:
            args['values'] = [
                DialogNodeOutputTextValuesElement._from_dict(x)
                for x in (_dict.get('values'))
            ]
        if 'selection_policy' in _dict:
            args['selection_policy'] = _dict.get('selection_policy')
        if 'delimiter' in _dict:
            args['delimiter'] = _dict.get('delimiter')
        if 'time' in _dict:
            args['time'] = _dict.get('time')
        if 'typing' in _dict:
            args['typing'] = _dict.get('typing')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        if 'options' in _dict:
            args['options'] = [
                DialogNodeOutputOptionsElement._from_dict(x)
                for x in (_dict.get('options'))
            ]
        if 'message_to_human_agent' in _dict:
            args['message_to_human_agent'] = _dict.get('message_to_human_agent')
        if 'query' in _dict:
            args['query'] = _dict.get('query')
        if 'query_type' in _dict:
            args['query_type'] = _dict.get('query_type')
        if 'filter' in _dict:
            args['filter'] = _dict.get('filter')
        if 'discovery_version' in _dict:
            args['discovery_version'] = _dict.get('discovery_version')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        if hasattr(self,
                   'selection_policy') and self.selection_policy is not None:
            _dict['selection_policy'] = self.selection_policy
        if hasattr(self, 'delimiter') and self.delimiter is not None:
            _dict['delimiter'] = self.delimiter
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = self.time
        if hasattr(self, 'typing') and self.typing is not None:
            _dict['typing'] = self.typing
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = [x._to_dict() for x in self.options]
        if hasattr(self, 'message_to_human_agent'
                  ) and self.message_to_human_agent is not None:
            _dict['message_to_human_agent'] = self.message_to_human_agent
        if hasattr(self, 'query') and self.query is not None:
            _dict['query'] = self.query
        if hasattr(self, 'query_type') and self.query_type is not None:
            _dict['query_type'] = self.query_type
        if hasattr(self, 'filter') and self.filter is not None:
            _dict['filter'] = self.filter
        if hasattr(self,
                   'discovery_version') and self.discovery_version is not None:
            _dict['discovery_version'] = self.discovery_version
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeOutputGeneric object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResponseTypeEnum(Enum):
        """
        The type of response returned by the dialog node. The specified response type must
        be supported by the client application or channel.
        **Note:** The **search_skill** response type is available only for Plus and
        Premium users, and is used only by the v2 runtime API.
        """
        TEXT = "text"
        PAUSE = "pause"
        IMAGE = "image"
        OPTION = "option"
        CONNECT_TO_AGENT = "connect_to_agent"
        SEARCH_SKILL = "search_skill"

    class SelectionPolicyEnum(Enum):
        """
        How a response is selected from the list, if more than one response is specified.
        Valid only when **response_type**=`text`.
        """
        SEQUENTIAL = "sequential"
        RANDOM = "random"
        MULTILINE = "multiline"

    class PreferenceEnum(Enum):
        """
        The preferred type of control to display, if supported by the channel. Valid only
        when **response_type**=`option`.
        """
        DROPDOWN = "dropdown"
        BUTTON = "button"

    class QueryTypeEnum(Enum):
        """
        The type of the search query. Required when **response_type**=`search_skill`.
        """
        NATURAL_LANGUAGE = "natural_language"
        DISCOVERY_QUERY_LANGUAGE = "discovery_query_language"


class DialogNodeOutputModifiers():
    """
    Options that modify how specified output is handled.

    :attr bool overwrite: (optional) Whether values in the output will overwrite
          output values in an array specified by previously executed dialog nodes. If this
          option is set to `false`, new values will be appended to previously specified
          values.
    """

    def __init__(self, *, overwrite=None):
        """
        Initialize a DialogNodeOutputModifiers object.

        :param bool overwrite: (optional) Whether values in the output will
               overwrite output values in an array specified by previously executed dialog
               nodes. If this option is set to `false`, new values will be appended to
               previously specified values.
        """
        self.overwrite = overwrite

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputModifiers object from a json dictionary."""
        args = {}
        valid_keys = ['overwrite']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeOutputModifiers: '
                + ', '.join(bad_keys))
        if 'overwrite' in _dict:
            args['overwrite'] = _dict.get('overwrite')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'overwrite') and self.overwrite is not None:
            _dict['overwrite'] = self.overwrite
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeOutputModifiers object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputOptionsElement():
    """
    DialogNodeOutputOptionsElement.

    :attr str label: The user-facing label for the option.
    :attr DialogNodeOutputOptionsElementValue value: An object defining the message
          input to be sent to the Watson Assistant service if the user selects the
          corresponding option.
    """

    def __init__(self, label, value):
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
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputOptionsElement object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'value']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeOutputOptionsElement: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogNodeOutputOptionsElement JSON'
            )
        if 'value' in _dict:
            args['value'] = DialogNodeOutputOptionsElementValue._from_dict(
                _dict.get('value'))
        else:
            raise ValueError(
                'Required property \'value\' not present in DialogNodeOutputOptionsElement JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeOutputOptionsElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputOptionsElementValue():
    """
    An object defining the message input to be sent to the Watson Assistant service if the
    user selects the corresponding option.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    :attr list[RuntimeIntent] intents: (optional) An array of intents to be used
          while processing the input.
          **Note:** This property is supported for backward compatibility with
          applications that use the v1 **Get response to user input** method.
    :attr list[RuntimeEntity] entities: (optional) An array of entities to be used
          while processing the user input.
          **Note:** This property is supported for backward compatibility with
          applications that use the v1 **Get response to user input** method.
    """

    def __init__(self, *, input=None, intents=None, entities=None):
        """
        Initialize a DialogNodeOutputOptionsElementValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param list[RuntimeIntent] intents: (optional) An array of intents to be
               used while processing the input.
               **Note:** This property is supported for backward compatibility with
               applications that use the v1 **Get response to user input** method.
        :param list[RuntimeEntity] entities: (optional) An array of entities to be
               used while processing the user input.
               **Note:** This property is supported for backward compatibility with
               applications that use the v1 **Get response to user input** method.
        """
        self.input = input
        self.intents = intents
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputOptionsElementValue object from a json dictionary."""
        args = {}
        valid_keys = ['input', 'intents', 'entities']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeOutputOptionsElementValue: '
                + ', '.join(bad_keys))
        if 'input' in _dict:
            args['input'] = MessageInput._from_dict(_dict.get('input'))
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input._to_dict()
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeOutputOptionsElementValue object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeOutputTextValuesElement():
    """
    DialogNodeOutputTextValuesElement.

    :attr str text: (optional) The text of a response. This string can include
          newline characters (`\n`), Markdown tagging, or other special characters, if
          supported by the channel.
    """

    def __init__(self, *, text=None):
        """
        Initialize a DialogNodeOutputTextValuesElement object.

        :param str text: (optional) The text of a response. This string can include
               newline characters (`\n`), Markdown tagging, or other special characters,
               if supported by the channel.
        """
        self.text = text

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeOutputTextValuesElement object from a json dictionary."""
        args = {}
        valid_keys = ['text']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeOutputTextValuesElement: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeOutputTextValuesElement object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogNodeVisitedDetails():
    """
    DialogNodeVisitedDetails.

    :attr str dialog_node: (optional) A dialog node that was triggered during
          processing of the input message.
    :attr str title: (optional) The title of the dialog node.
    :attr str conditions: (optional) The conditions that trigger the dialog node.
    """

    def __init__(self, *, dialog_node=None, title=None, conditions=None):
        """
        Initialize a DialogNodeVisitedDetails object.

        :param str dialog_node: (optional) A dialog node that was triggered during
               processing of the input message.
        :param str title: (optional) The title of the dialog node.
        :param str conditions: (optional) The conditions that trigger the dialog
               node.
        """
        self.dialog_node = dialog_node
        self.title = title
        self.conditions = conditions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogNodeVisitedDetails object from a json dictionary."""
        args = {}
        valid_keys = ['dialog_node', 'title', 'conditions']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogNodeVisitedDetails: '
                + ', '.join(bad_keys))
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'conditions' in _dict:
            args['conditions'] = _dict.get('conditions')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'conditions') and self.conditions is not None:
            _dict['conditions'] = self.conditions
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogNodeVisitedDetails object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestion():
    """
    DialogSuggestion.

    :attr str label: The user-facing label for the disambiguation option. This label
          is taken from the **title** or **user_label** property of the corresponding
          dialog node, depending on the disambiguation options.
    :attr DialogSuggestionValue value: An object defining the message input,
          intents, and entities to be sent to the Watson Assistant service if the user
          selects the corresponding disambiguation option.
    :attr DialogSuggestionOutput output: (optional) The dialog output that will be
          returned from the Watson Assistant service if the user selects the corresponding
          option.
    :attr str dialog_node: (optional) The ID of the dialog node that the **label**
          property is taken from. The **label** property is populated using the value of
          the dialog node's **user_label** property.
    """

    def __init__(self, label, value, *, output=None, dialog_node=None):
        """
        Initialize a DialogSuggestion object.

        :param str label: The user-facing label for the disambiguation option. This
               label is taken from the **title** or **user_label** property of the
               corresponding dialog node, depending on the disambiguation options.
        :param DialogSuggestionValue value: An object defining the message input,
               intents, and entities to be sent to the Watson Assistant service if the
               user selects the corresponding disambiguation option.
        :param DialogSuggestionOutput output: (optional) The dialog output that
               will be returned from the Watson Assistant service if the user selects the
               corresponding option.
        :param str dialog_node: (optional) The ID of the dialog node that the
               **label** property is taken from. The **label** property is populated using
               the value of the dialog node's **user_label** property.
        """
        self.label = label
        self.value = value
        self.output = output
        self.dialog_node = dialog_node

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestion object from a json dictionary."""
        args = {}
        valid_keys = ['label', 'value', 'output', 'dialog_node']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogSuggestion: '
                + ', '.join(bad_keys))
        if 'label' in _dict:
            args['label'] = _dict.get('label')
        else:
            raise ValueError(
                'Required property \'label\' not present in DialogSuggestion JSON'
            )
        if 'value' in _dict:
            args['value'] = DialogSuggestionValue._from_dict(_dict.get('value'))
        else:
            raise ValueError(
                'Required property \'value\' not present in DialogSuggestion JSON'
            )
        if 'output' in _dict:
            args['output'] = DialogSuggestionOutput._from_dict(
                _dict.get('output'))
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'label') and self.label is not None:
            _dict['label'] = self.label
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value._to_dict()
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output._to_dict()
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogSuggestion object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestionOutput():
    """
    The dialog output that will be returned from the Watson Assistant service if the user
    selects the corresponding option.

    :attr list[str] nodes_visited: (optional) An array of the nodes that were
          triggered to create the response, in the order in which they were visited. This
          information is useful for debugging and for tracing the path taken through the
          node tree.
    :attr list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An array
          of objects containing detailed diagnostic information about the nodes that were
          triggered during processing of the input message. Included only if
          **nodes_visited_details** is set to `true` in the message request.
    :attr list[str] text: An array of responses to the user.
    :attr list[DialogSuggestionResponseGeneric] generic: (optional) Output intended
          for any channel. It is the responsibility of the client application to implement
          the supported response types.
    """

    def __init__(self,
                 text,
                 *,
                 nodes_visited=None,
                 nodes_visited_details=None,
                 generic=None,
                 **kwargs):
        """
        Initialize a DialogSuggestionOutput object.

        :param list[str] text: An array of responses to the user.
        :param list[str] nodes_visited: (optional) An array of the nodes that were
               triggered to create the response, in the order in which they were visited.
               This information is useful for debugging and for tracing the path taken
               through the node tree.
        :param list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An
               array of objects containing detailed diagnostic information about the nodes
               that were triggered during processing of the input message. Included only
               if **nodes_visited_details** is set to `true` in the message request.
        :param list[DialogSuggestionResponseGeneric] generic: (optional) Output
               intended for any channel. It is the responsibility of the client
               application to implement the supported response types.
        :param **kwargs: (optional) Any additional properties.
        """
        self.nodes_visited = nodes_visited
        self.nodes_visited_details = nodes_visited_details
        self.text = text
        self.generic = generic
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestionOutput object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'nodes_visited' in _dict:
            args['nodes_visited'] = _dict.get('nodes_visited')
            del xtra['nodes_visited']
        if 'nodes_visited_details' in _dict:
            args['nodes_visited_details'] = [
                DialogNodeVisitedDetails._from_dict(x)
                for x in (_dict.get('nodes_visited_details'))
            ]
            del xtra['nodes_visited_details']
        if 'text' in _dict:
            args['text'] = _dict.get('text')
            del xtra['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in DialogSuggestionOutput JSON'
            )
        if 'generic' in _dict:
            args['generic'] = [
                DialogSuggestionResponseGeneric._from_dict(x)
                for x in (_dict.get('generic'))
            ]
            del xtra['generic']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nodes_visited') and self.nodes_visited is not None:
            _dict['nodes_visited'] = self.nodes_visited
        if hasattr(self, 'nodes_visited_details'
                  ) and self.nodes_visited_details is not None:
            _dict['nodes_visited_details'] = [
                x._to_dict() for x in self.nodes_visited_details
            ]
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'generic') and self.generic is not None:
            _dict['generic'] = [x._to_dict() for x in self.generic]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'nodes_visited', 'nodes_visited_details', 'text', 'generic'
        }
        if not hasattr(self, '_additionalProperties'):
            super(DialogSuggestionOutput,
                  self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(DialogSuggestionOutput, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this DialogSuggestionOutput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class DialogSuggestionResponseGeneric():
    """
    DialogSuggestionResponseGeneric.

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
          **Note:** The **suggestion** response type is part of the disambiguation
          feature, which is only available for Plus and Premium users. The
          **search_skill** response type is available only for Plus and Premium users, and
          is used only by the v2 runtime API.
    :attr str text: (optional) The text of the response.
    :attr int time: (optional) How long to pause, in milliseconds.
    :attr bool typing: (optional) Whether to send a "user is typing" event during
          the pause.
    :attr str source: (optional) The URL of the image.
    :attr str title: (optional) The title or introductory text to show before the
          response.
    :attr str description: (optional) The description to show with the the response.
    :attr str preference: (optional) The preferred type of control to display.
    :attr list[DialogNodeOutputOptionsElement] options: (optional) An array of
          objects describing the options from which the user can choose.
    :attr str message_to_human_agent: (optional) A message to be sent to the human
          agent who will be taking over the conversation.
    :attr str topic: (optional) A label identifying the topic of the conversation,
          derived from the **user_label** property of the relevant node.
    :attr str dialog_node: (optional) The ID of the dialog node that the **topic**
          property is taken from. The **topic** property is populated using the value of
          the dialog node's **user_label** property.
    """

    def __init__(self,
                 response_type,
                 *,
                 text=None,
                 time=None,
                 typing=None,
                 source=None,
                 title=None,
                 description=None,
                 preference=None,
                 options=None,
                 message_to_human_agent=None,
                 topic=None,
                 dialog_node=None):
        """
        Initialize a DialogSuggestionResponseGeneric object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
               **Note:** The **suggestion** response type is part of the disambiguation
               feature, which is only available for Plus and Premium users. The
               **search_skill** response type is available only for Plus and Premium
               users, and is used only by the v2 runtime API.
        :param str text: (optional) The text of the response.
        :param int time: (optional) How long to pause, in milliseconds.
        :param bool typing: (optional) Whether to send a "user is typing" event
               during the pause.
        :param str source: (optional) The URL of the image.
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the the
               response.
        :param str preference: (optional) The preferred type of control to display.
        :param list[DialogNodeOutputOptionsElement] options: (optional) An array of
               objects describing the options from which the user can choose.
        :param str message_to_human_agent: (optional) A message to be sent to the
               human agent who will be taking over the conversation.
        :param str topic: (optional) A label identifying the topic of the
               conversation, derived from the **user_label** property of the relevant
               node.
        :param str dialog_node: (optional) The ID of the dialog node that the
               **topic** property is taken from. The **topic** property is populated using
               the value of the dialog node's **user_label** property.
        """
        self.response_type = response_type
        self.text = text
        self.time = time
        self.typing = typing
        self.source = source
        self.title = title
        self.description = description
        self.preference = preference
        self.options = options
        self.message_to_human_agent = message_to_human_agent
        self.topic = topic
        self.dialog_node = dialog_node

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestionResponseGeneric object from a json dictionary."""
        args = {}
        valid_keys = [
            'response_type', 'text', 'time', 'typing', 'source', 'title',
            'description', 'preference', 'options', 'message_to_human_agent',
            'topic', 'dialog_node'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogSuggestionResponseGeneric: '
                + ', '.join(bad_keys))
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in DialogSuggestionResponseGeneric JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'time' in _dict:
            args['time'] = _dict.get('time')
        if 'typing' in _dict:
            args['typing'] = _dict.get('typing')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        if 'options' in _dict:
            args['options'] = [
                DialogNodeOutputOptionsElement._from_dict(x)
                for x in (_dict.get('options'))
            ]
        if 'message_to_human_agent' in _dict:
            args['message_to_human_agent'] = _dict.get('message_to_human_agent')
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = self.time
        if hasattr(self, 'typing') and self.typing is not None:
            _dict['typing'] = self.typing
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = [x._to_dict() for x in self.options]
        if hasattr(self, 'message_to_human_agent'
                  ) and self.message_to_human_agent is not None:
            _dict['message_to_human_agent'] = self.message_to_human_agent
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogSuggestionResponseGeneric object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResponseTypeEnum(Enum):
        """
        The type of response returned by the dialog node. The specified response type must
        be supported by the client application or channel.
        **Note:** The **suggestion** response type is part of the disambiguation feature,
        which is only available for Plus and Premium users. The **search_skill** response
        type is available only for Plus and Premium users, and is used only by the v2
        runtime API.
        """
        TEXT = "text"
        PAUSE = "pause"
        IMAGE = "image"
        OPTION = "option"
        CONNECT_TO_AGENT = "connect_to_agent"
        SEARCH_SKILL = "search_skill"

    class PreferenceEnum(Enum):
        """
        The preferred type of control to display.
        """
        DROPDOWN = "dropdown"
        BUTTON = "button"


class DialogSuggestionValue():
    """
    An object defining the message input, intents, and entities to be sent to the Watson
    Assistant service if the user selects the corresponding disambiguation option.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    :attr list[RuntimeIntent] intents: (optional) An array of intents to be sent
          along with the user input.
    :attr list[RuntimeEntity] entities: (optional) An array of entities to be sent
          along with the user input.
    """

    def __init__(self, *, input=None, intents=None, entities=None):
        """
        Initialize a DialogSuggestionValue object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param list[RuntimeIntent] intents: (optional) An array of intents to be
               sent along with the user input.
        :param list[RuntimeEntity] entities: (optional) An array of entities to be
               sent along with the user input.
        """
        self.input = input
        self.intents = intents
        self.entities = entities

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a DialogSuggestionValue object from a json dictionary."""
        args = {}
        valid_keys = ['input', 'intents', 'entities']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class DialogSuggestionValue: '
                + ', '.join(bad_keys))
        if 'input' in _dict:
            args['input'] = MessageInput._from_dict(_dict.get('input'))
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input._to_dict()
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        return _dict

    def __str__(self):
        """Return a `str` version of this DialogSuggestionValue object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Entity():
    """
    Entity.

    :attr str entity: The name of the entity. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, and hyphen characters.
          - If you specify an entity name beginning with the reserved prefix `sys-`, it
          must be the name of a system entity that you want to enable. (Any entity content
          specified with the request is ignored.).
    :attr str description: (optional) The description of the entity. This string
          cannot contain carriage return, newline, or tab characters.
    :attr dict metadata: (optional) Any metadata related to the entity.
    :attr bool fuzzy_match: (optional) Whether to use fuzzy matching for the entity.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :attr list[Value] values: (optional) An array of objects describing the entity
          values.
    """

    def __init__(self,
                 entity,
                 *,
                 description=None,
                 metadata=None,
                 fuzzy_match=None,
                 created=None,
                 updated=None,
                 values=None):
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
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        :param list[Value] values: (optional) An array of objects describing the
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
    def _from_dict(cls, _dict):
        """Initialize a Entity object from a json dictionary."""
        args = {}
        valid_keys = [
            'entity', 'description', 'metadata', 'fuzzy_match', 'created',
            'updated', 'values'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Entity: ' +
                ', '.join(bad_keys))
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in Entity JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'fuzzy_match' in _dict:
            args['fuzzy_match'] = _dict.get('fuzzy_match')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'values' in _dict:
            args['values'] = [
                Value._from_dict(x) for x in (_dict.get('values'))
            ]
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        return _dict

    def __str__(self):
        """Return a `str` version of this Entity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityCollection():
    """
    An array of objects describing the entities for the workspace.

    :attr list[Entity] entities: An array of objects describing the entities defined
          for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, entities, pagination):
        """
        Initialize a EntityCollection object.

        :param list[Entity] entities: An array of objects describing the entities
               defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.entities = entities
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityCollection object from a json dictionary."""
        args = {}
        valid_keys = ['entities', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntityCollection: '
                + ', '.join(bad_keys))
        if 'entities' in _dict:
            args['entities'] = [
                Entity._from_dict(x) for x in (_dict.get('entities'))
            ]
        else:
            raise ValueError(
                'Required property \'entities\' not present in EntityCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in EntityCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this EntityCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMention():
    """
    An object describing a contextual entity mention.

    :attr str text: The text of the user input example.
    :attr str intent: The name of the intent.
    :attr list[int] location: An array of zero-based character offsets that indicate
          where the entity mentions begin and end in the input text.
    """

    def __init__(self, text, intent, location):
        """
        Initialize a EntityMention object.

        :param str text: The text of the user input example.
        :param str intent: The name of the intent.
        :param list[int] location: An array of zero-based character offsets that
               indicate where the entity mentions begin and end in the input text.
        """
        self.text = text
        self.intent = intent
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMention object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'intent', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntityMention: '
                + ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in EntityMention JSON')
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in EntityMention JSON'
            )
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError(
                'Required property \'location\' not present in EntityMention JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def __str__(self):
        """Return a `str` version of this EntityMention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class EntityMentionCollection():
    """
    EntityMentionCollection.

    :attr list[EntityMention] examples: An array of objects describing the entity
          mentions defined for an entity.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, examples, pagination):
        """
        Initialize a EntityMentionCollection object.

        :param list[EntityMention] examples: An array of objects describing the
               entity mentions defined for an entity.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a EntityMentionCollection object from a json dictionary."""
        args = {}
        valid_keys = ['examples', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class EntityMentionCollection: '
                + ', '.join(bad_keys))
        if 'examples' in _dict:
            args['examples'] = [
                EntityMention._from_dict(x) for x in (_dict.get('examples'))
            ]
        else:
            raise ValueError(
                'Required property \'examples\' not present in EntityMentionCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in EntityMentionCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this EntityMentionCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Example():
    """
    Example.

    :attr str text: The text of a user input example. This string must conform to
          the following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr list[Mention] mentions: (optional) An array of contextual entity mentions.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self, text, *, mentions=None, created=None, updated=None):
        """
        Initialize a Example object.

        :param str text: The text of a user input example. This string must conform
               to the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[Mention] mentions: (optional) An array of contextual entity
               mentions.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        """
        self.text = text
        self.mentions = mentions
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Example object from a json dictionary."""
        args = {}
        valid_keys = ['text', 'mentions', 'created', 'updated']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Example: ' +
                ', '.join(bad_keys))
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        else:
            raise ValueError(
                'Required property \'text\' not present in Example JSON')
        if 'mentions' in _dict:
            args['mentions'] = [
                Mention._from_dict(x) for x in (_dict.get('mentions'))
            ]
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'mentions') and self.mentions is not None:
            _dict['mentions'] = [x._to_dict() for x in self.mentions]
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this Example object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ExampleCollection():
    """
    ExampleCollection.

    :attr list[Example] examples: An array of objects describing the examples
          defined for the intent.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, examples, pagination):
        """
        Initialize a ExampleCollection object.

        :param list[Example] examples: An array of objects describing the examples
               defined for the intent.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.examples = examples
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ExampleCollection object from a json dictionary."""
        args = {}
        valid_keys = ['examples', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ExampleCollection: '
                + ', '.join(bad_keys))
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in (_dict.get('examples'))
            ]
        else:
            raise ValueError(
                'Required property \'examples\' not present in ExampleCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ExampleCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ExampleCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Intent():
    """
    Intent.

    :attr str intent: The name of the intent. This string must conform to the
          following restrictions:
          - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
          characters.
          - It cannot begin with the reserved prefix `sys-`.
    :attr str description: (optional) The description of the intent. This string
          cannot contain carriage return, newline, or tab characters.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :attr list[Example] examples: (optional) An array of user input examples for the
          intent.
    """

    def __init__(self,
                 intent,
                 *,
                 description=None,
                 created=None,
                 updated=None,
                 examples=None):
        """
        Initialize a Intent object.

        :param str intent: The name of the intent. This string must conform to the
               following restrictions:
               - It can contain only Unicode alphanumeric, underscore, hyphen, and dot
               characters.
               - It cannot begin with the reserved prefix `sys-`.
        :param str description: (optional) The description of the intent. This
               string cannot contain carriage return, newline, or tab characters.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        :param list[Example] examples: (optional) An array of user input examples
               for the intent.
        """
        self.intent = intent
        self.description = description
        self.created = created
        self.updated = updated
        self.examples = examples

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Intent object from a json dictionary."""
        args = {}
        valid_keys = ['intent', 'description', 'created', 'updated', 'examples']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Intent: ' +
                ', '.join(bad_keys))
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in Intent JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'examples' in _dict:
            args['examples'] = [
                Example._from_dict(x) for x in (_dict.get('examples'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'examples') and self.examples is not None:
            _dict['examples'] = [x._to_dict() for x in self.examples]
        return _dict

    def __str__(self):
        """Return a `str` version of this Intent object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class IntentCollection():
    """
    IntentCollection.

    :attr list[Intent] intents: An array of objects describing the intents defined
          for the workspace.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, intents, pagination):
        """
        Initialize a IntentCollection object.

        :param list[Intent] intents: An array of objects describing the intents
               defined for the workspace.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.intents = intents
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a IntentCollection object from a json dictionary."""
        args = {}
        valid_keys = ['intents', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class IntentCollection: '
                + ', '.join(bad_keys))
        if 'intents' in _dict:
            args['intents'] = [
                Intent._from_dict(x) for x in (_dict.get('intents'))
            ]
        else:
            raise ValueError(
                'Required property \'intents\' not present in IntentCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in IntentCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this IntentCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Log():
    """
    Log.

    :attr MessageRequest request: A request sent to the workspace, including the
          user input and context.
    :attr MessageResponse response: The response sent by the workspace, including
          the output text, detected intents and entities, and context.
    :attr str log_id: A unique identifier for the logged event.
    :attr str request_timestamp: The timestamp for receipt of the message.
    :attr str response_timestamp: The timestamp for the system response to the
          message.
    :attr str workspace_id: The unique identifier of the workspace where the request
          was made.
    :attr str language: The language of the workspace where the message request was
          made.
    """

    def __init__(self, request, response, log_id, request_timestamp,
                 response_timestamp, workspace_id, language):
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
    def _from_dict(cls, _dict):
        """Initialize a Log object from a json dictionary."""
        args = {}
        valid_keys = [
            'request', 'response', 'log_id', 'request_timestamp',
            'response_timestamp', 'workspace_id', 'language'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Log: ' +
                ', '.join(bad_keys))
        if 'request' in _dict:
            args['request'] = MessageRequest._from_dict(_dict.get('request'))
        else:
            raise ValueError(
                'Required property \'request\' not present in Log JSON')
        if 'response' in _dict:
            args['response'] = MessageResponse._from_dict(_dict.get('response'))
        else:
            raise ValueError(
                'Required property \'response\' not present in Log JSON')
        if 'log_id' in _dict:
            args['log_id'] = _dict.get('log_id')
        else:
            raise ValueError(
                'Required property \'log_id\' not present in Log JSON')
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
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in Log JSON')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Log JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request') and self.request is not None:
            _dict['request'] = self.request._to_dict()
        if hasattr(self, 'response') and self.response is not None:
            _dict['response'] = self.response._to_dict()
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

    def __str__(self):
        """Return a `str` version of this Log object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogCollection():
    """
    LogCollection.

    :attr list[Log] logs: An array of objects describing log events.
    :attr LogPagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, logs, pagination):
        """
        Initialize a LogCollection object.

        :param list[Log] logs: An array of objects describing log events.
        :param LogPagination pagination: The pagination data for the returned
               objects.
        """
        self.logs = logs
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogCollection object from a json dictionary."""
        args = {}
        valid_keys = ['logs', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogCollection: '
                + ', '.join(bad_keys))
        if 'logs' in _dict:
            args['logs'] = [Log._from_dict(x) for x in (_dict.get('logs'))]
        else:
            raise ValueError(
                'Required property \'logs\' not present in LogCollection JSON')
        if 'pagination' in _dict:
            args['pagination'] = LogPagination._from_dict(
                _dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in LogCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'logs') and self.logs is not None:
            _dict['logs'] = [x._to_dict() for x in self.logs]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this LogCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class LogMessage():
    """
    Log message details.

    :attr str level: The severity of the log message.
    :attr str msg: The text of the log message.
    """

    def __init__(self, level, msg):
        """
        Initialize a LogMessage object.

        :param str level: The severity of the log message.
        :param str msg: The text of the log message.
        """
        self.level = level
        self.msg = msg

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogMessage object from a json dictionary."""
        args = {}
        valid_keys = ['level', 'msg']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogMessage: '
                + ', '.join(bad_keys))
        if 'level' in _dict:
            args['level'] = _dict.get('level')
        else:
            raise ValueError(
                'Required property \'level\' not present in LogMessage JSON')
        if 'msg' in _dict:
            args['msg'] = _dict.get('msg')
        else:
            raise ValueError(
                'Required property \'msg\' not present in LogMessage JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'level') and self.level is not None:
            _dict['level'] = self.level
        if hasattr(self, 'msg') and self.msg is not None:
            _dict['msg'] = self.msg
        return _dict

    def __str__(self):
        """Return a `str` version of this LogMessage object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class LevelEnum(Enum):
        """
        The severity of the log message.
        """
        INFO = "info"
        ERROR = "error"
        WARN = "warn"


class LogPagination():
    """
    The pagination data for the returned objects.

    :attr str next_url: (optional) The URL that will return the next page of
          results, if any.
    :attr int matched: (optional) Reserved for future use.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self, *, next_url=None, matched=None, next_cursor=None):
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
    def _from_dict(cls, _dict):
        """Initialize a LogPagination object from a json dictionary."""
        args = {}
        valid_keys = ['next_url', 'matched', 'next_cursor']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class LogPagination: '
                + ', '.join(bad_keys))
        if 'next_url' in _dict:
            args['next_url'] = _dict.get('next_url')
        if 'matched' in _dict:
            args['matched'] = _dict.get('matched')
        if 'next_cursor' in _dict:
            args['next_cursor'] = _dict.get('next_cursor')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'next_url') and self.next_url is not None:
            _dict['next_url'] = self.next_url
        if hasattr(self, 'matched') and self.matched is not None:
            _dict['matched'] = self.matched
        if hasattr(self, 'next_cursor') and self.next_cursor is not None:
            _dict['next_cursor'] = self.next_cursor
        return _dict

    def __str__(self):
        """Return a `str` version of this LogPagination object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Mention():
    """
    A mention of a contextual entity.

    :attr str entity: The name of the entity.
    :attr list[int] location: An array of zero-based character offsets that indicate
          where the entity mentions begin and end in the input text.
    """

    def __init__(self, entity, location):
        """
        Initialize a Mention object.

        :param str entity: The name of the entity.
        :param list[int] location: An array of zero-based character offsets that
               indicate where the entity mentions begin and end in the input text.
        """
        self.entity = entity
        self.location = location

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Mention object from a json dictionary."""
        args = {}
        valid_keys = ['entity', 'location']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Mention: ' +
                ', '.join(bad_keys))
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in Mention JSON')
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError(
                'Required property \'location\' not present in Mention JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'entity') and self.entity is not None:
            _dict['entity'] = self.entity
        if hasattr(self, 'location') and self.location is not None:
            _dict['location'] = self.location
        return _dict

    def __str__(self):
        """Return a `str` version of this Mention object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageContextMetadata():
    """
    Metadata related to the message.

    :attr str deployment: (optional) A label identifying the deployment environment,
          used for filtering log data. This string cannot contain carriage return,
          newline, or tab characters.
    :attr str user_id: (optional) A string value that identifies the user who is
          interacting with the workspace. The client must provide a unique identifier for
          each individual end user who accesses the application. For Plus and Premium
          plans, this user ID is used to identify unique users for billing purposes. This
          string cannot contain carriage return, newline, or tab characters.
    """

    def __init__(self, *, deployment=None, user_id=None):
        """
        Initialize a MessageContextMetadata object.

        :param str deployment: (optional) A label identifying the deployment
               environment, used for filtering log data. This string cannot contain
               carriage return, newline, or tab characters.
        :param str user_id: (optional) A string value that identifies the user who
               is interacting with the workspace. The client must provide a unique
               identifier for each individual end user who accesses the application. For
               Plus and Premium plans, this user ID is used to identify unique users for
               billing purposes. This string cannot contain carriage return, newline, or
               tab characters.
        """
        self.deployment = deployment
        self.user_id = user_id

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageContextMetadata object from a json dictionary."""
        args = {}
        valid_keys = ['deployment', 'user_id']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MessageContextMetadata: '
                + ', '.join(bad_keys))
        if 'deployment' in _dict:
            args['deployment'] = _dict.get('deployment')
        if 'user_id' in _dict:
            args['user_id'] = _dict.get('user_id')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'deployment') and self.deployment is not None:
            _dict['deployment'] = self.deployment
        if hasattr(self, 'user_id') and self.user_id is not None:
            _dict['user_id'] = self.user_id
        return _dict

    def __str__(self):
        """Return a `str` version of this MessageContextMetadata object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageInput():
    """
    An input object that includes the input text.

    :attr str text: (optional) The text of the user input. This string cannot
          contain carriage return, newline, or tab characters.
    """

    def __init__(self, *, text=None, **kwargs):
        """
        Initialize a MessageInput object.

        :param str text: (optional) The text of the user input. This string cannot
               contain carriage return, newline, or tab characters.
        :param **kwargs: (optional) Any additional properties.
        """
        self.text = text
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageInput object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'text' in _dict:
            args['text'] = _dict.get('text')
            del xtra['text']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {'text'}
        if not hasattr(self, '_additionalProperties'):
            super(MessageInput, self).__setattr__('_additionalProperties',
                                                  set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(MessageInput, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this MessageInput object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageRequest():
    """
    A request sent to the workspace, including the user input and context.

    :attr MessageInput input: (optional) An input object that includes the input
          text.
    :attr list[RuntimeIntent] intents: (optional) Intents to use when evaluating the
          user input. Include intents from the previous response to continue using those
          intents rather than trying to recognize intents in the new input.
    :attr list[RuntimeEntity] entities: (optional) Entities to use when evaluating
          the message. Include entities from the previous response to continue using those
          entities rather than detecting entities in the new input.
    :attr bool alternate_intents: (optional) Whether to return more than one intent.
          A value of `true` indicates that all matching intents are returned.
    :attr Context context: (optional) State information for the conversation. To
          maintain state, include the context from the previous response.
    :attr OutputData output: (optional) An output object that includes the response
          to the user, the dialog nodes that were triggered, and messages from the log.
    :attr list[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    """

    def __init__(self,
                 *,
                 input=None,
                 intents=None,
                 entities=None,
                 alternate_intents=None,
                 context=None,
                 output=None,
                 actions=None):
        """
        Initialize a MessageRequest object.

        :param MessageInput input: (optional) An input object that includes the
               input text.
        :param list[RuntimeIntent] intents: (optional) Intents to use when
               evaluating the user input. Include intents from the previous response to
               continue using those intents rather than trying to recognize intents in the
               new input.
        :param list[RuntimeEntity] entities: (optional) Entities to use when
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
        :param list[DialogNodeAction] actions: (optional) An array of objects
               describing any actions requested by the dialog node.
        """
        self.input = input
        self.intents = intents
        self.entities = entities
        self.alternate_intents = alternate_intents
        self.context = context
        self.output = output
        self.actions = actions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageRequest object from a json dictionary."""
        args = {}
        valid_keys = [
            'input', 'intents', 'entities', 'alternate_intents', 'context',
            'output', 'actions'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MessageRequest: '
                + ', '.join(bad_keys))
        if 'input' in _dict:
            args['input'] = MessageInput._from_dict(_dict.get('input'))
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict.get('context'))
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict.get('output'))
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in (_dict.get('actions'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input._to_dict()
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context._to_dict()
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output._to_dict()
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x._to_dict() for x in self.actions]
        return _dict

    def __str__(self):
        """Return a `str` version of this MessageRequest object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class MessageResponse():
    """
    The response sent by the workspace, including the output text, detected intents and
    entities, and context.

    :attr MessageInput input: An input object that includes the input text.
    :attr list[RuntimeIntent] intents: An array of intents recognized in the user
          input, sorted in descending order of confidence.
    :attr list[RuntimeEntity] entities: An array of entities identified in the user
          input.
    :attr bool alternate_intents: (optional) Whether to return more than one intent.
          A value of `true` indicates that all matching intents are returned.
    :attr Context context: State information for the conversation. To maintain
          state, include the context from the previous response.
    :attr OutputData output: An output object that includes the response to the
          user, the dialog nodes that were triggered, and messages from the log.
    :attr list[DialogNodeAction] actions: (optional) An array of objects describing
          any actions requested by the dialog node.
    """

    def __init__(self,
                 input,
                 intents,
                 entities,
                 context,
                 output,
                 *,
                 alternate_intents=None,
                 actions=None):
        """
        Initialize a MessageResponse object.

        :param MessageInput input: An input object that includes the input text.
        :param list[RuntimeIntent] intents: An array of intents recognized in the
               user input, sorted in descending order of confidence.
        :param list[RuntimeEntity] entities: An array of entities identified in the
               user input.
        :param Context context: State information for the conversation. To maintain
               state, include the context from the previous response.
        :param OutputData output: An output object that includes the response to
               the user, the dialog nodes that were triggered, and messages from the log.
        :param bool alternate_intents: (optional) Whether to return more than one
               intent. A value of `true` indicates that all matching intents are returned.
        :param list[DialogNodeAction] actions: (optional) An array of objects
               describing any actions requested by the dialog node.
        """
        self.input = input
        self.intents = intents
        self.entities = entities
        self.alternate_intents = alternate_intents
        self.context = context
        self.output = output
        self.actions = actions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a MessageResponse object from a json dictionary."""
        args = {}
        valid_keys = [
            'input', 'intents', 'entities', 'alternate_intents', 'context',
            'output', 'actions'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class MessageResponse: '
                + ', '.join(bad_keys))
        if 'input' in _dict:
            args['input'] = MessageInput._from_dict(_dict.get('input'))
        else:
            raise ValueError(
                'Required property \'input\' not present in MessageResponse JSON'
            )
        if 'intents' in _dict:
            args['intents'] = [
                RuntimeIntent._from_dict(x) for x in (_dict.get('intents'))
            ]
        else:
            raise ValueError(
                'Required property \'intents\' not present in MessageResponse JSON'
            )
        if 'entities' in _dict:
            args['entities'] = [
                RuntimeEntity._from_dict(x) for x in (_dict.get('entities'))
            ]
        else:
            raise ValueError(
                'Required property \'entities\' not present in MessageResponse JSON'
            )
        if 'alternate_intents' in _dict:
            args['alternate_intents'] = _dict.get('alternate_intents')
        if 'context' in _dict:
            args['context'] = Context._from_dict(_dict.get('context'))
        else:
            raise ValueError(
                'Required property \'context\' not present in MessageResponse JSON'
            )
        if 'output' in _dict:
            args['output'] = OutputData._from_dict(_dict.get('output'))
        else:
            raise ValueError(
                'Required property \'output\' not present in MessageResponse JSON'
            )
        if 'actions' in _dict:
            args['actions'] = [
                DialogNodeAction._from_dict(x) for x in (_dict.get('actions'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'input') and self.input is not None:
            _dict['input'] = self.input._to_dict()
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self,
                   'alternate_intents') and self.alternate_intents is not None:
            _dict['alternate_intents'] = self.alternate_intents
        if hasattr(self, 'context') and self.context is not None:
            _dict['context'] = self.context._to_dict()
        if hasattr(self, 'output') and self.output is not None:
            _dict['output'] = self.output._to_dict()
        if hasattr(self, 'actions') and self.actions is not None:
            _dict['actions'] = [x._to_dict() for x in self.actions]
        return _dict

    def __str__(self):
        """Return a `str` version of this MessageResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class OutputData():
    """
    An output object that includes the response to the user, the dialog nodes that were
    triggered, and messages from the log.

    :attr list[str] nodes_visited: (optional) An array of the nodes that were
          triggered to create the response, in the order in which they were visited. This
          information is useful for debugging and for tracing the path taken through the
          node tree.
    :attr list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An array
          of objects containing detailed diagnostic information about the nodes that were
          triggered during processing of the input message. Included only if
          **nodes_visited_details** is set to `true` in the message request.
    :attr list[LogMessage] log_messages: An array of up to 50 messages logged with
          the request.
    :attr list[str] text: An array of responses to the user.
    :attr list[RuntimeResponseGeneric] generic: (optional) Output intended for any
          channel. It is the responsibility of the client application to implement the
          supported response types.
    """

    def __init__(self,
                 log_messages,
                 text,
                 *,
                 nodes_visited=None,
                 nodes_visited_details=None,
                 generic=None,
                 **kwargs):
        """
        Initialize a OutputData object.

        :param list[LogMessage] log_messages: An array of up to 50 messages logged
               with the request.
        :param list[str] text: An array of responses to the user.
        :param list[str] nodes_visited: (optional) An array of the nodes that were
               triggered to create the response, in the order in which they were visited.
               This information is useful for debugging and for tracing the path taken
               through the node tree.
        :param list[DialogNodeVisitedDetails] nodes_visited_details: (optional) An
               array of objects containing detailed diagnostic information about the nodes
               that were triggered during processing of the input message. Included only
               if **nodes_visited_details** is set to `true` in the message request.
        :param list[RuntimeResponseGeneric] generic: (optional) Output intended for
               any channel. It is the responsibility of the client application to
               implement the supported response types.
        :param **kwargs: (optional) Any additional properties.
        """
        self.nodes_visited = nodes_visited
        self.nodes_visited_details = nodes_visited_details
        self.log_messages = log_messages
        self.text = text
        self.generic = generic
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a OutputData object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        if 'nodes_visited' in _dict:
            args['nodes_visited'] = _dict.get('nodes_visited')
            del xtra['nodes_visited']
        if 'nodes_visited_details' in _dict:
            args['nodes_visited_details'] = [
                DialogNodeVisitedDetails._from_dict(x)
                for x in (_dict.get('nodes_visited_details'))
            ]
            del xtra['nodes_visited_details']
        if 'log_messages' in _dict:
            args['log_messages'] = [
                LogMessage._from_dict(x) for x in (_dict.get('log_messages'))
            ]
            del xtra['log_messages']
        else:
            raise ValueError(
                'Required property \'log_messages\' not present in OutputData JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
            del xtra['text']
        else:
            raise ValueError(
                'Required property \'text\' not present in OutputData JSON')
        if 'generic' in _dict:
            args['generic'] = [
                RuntimeResponseGeneric._from_dict(x)
                for x in (_dict.get('generic'))
            ]
            del xtra['generic']
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'nodes_visited') and self.nodes_visited is not None:
            _dict['nodes_visited'] = self.nodes_visited
        if hasattr(self, 'nodes_visited_details'
                  ) and self.nodes_visited_details is not None:
            _dict['nodes_visited_details'] = [
                x._to_dict() for x in self.nodes_visited_details
            ]
        if hasattr(self, 'log_messages') and self.log_messages is not None:
            _dict['log_messages'] = [x._to_dict() for x in self.log_messages]
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'generic') and self.generic is not None:
            _dict['generic'] = [x._to_dict() for x in self.generic]
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {
            'nodes_visited', 'nodes_visited_details', 'log_messages', 'text',
            'generic'
        }
        if not hasattr(self, '_additionalProperties'):
            super(OutputData, self).__setattr__('_additionalProperties', set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(OutputData, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this OutputData object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Pagination():
    """
    The pagination data for the returned objects.

    :attr str refresh_url: The URL that will return the same page of results.
    :attr str next_url: (optional) The URL that will return the next page of
          results.
    :attr int total: (optional) Reserved for future use.
    :attr int matched: (optional) Reserved for future use.
    :attr str refresh_cursor: (optional) A token identifying the current page of
          results.
    :attr str next_cursor: (optional) A token identifying the next page of results.
    """

    def __init__(self,
                 refresh_url,
                 *,
                 next_url=None,
                 total=None,
                 matched=None,
                 refresh_cursor=None,
                 next_cursor=None):
        """
        Initialize a Pagination object.

        :param str refresh_url: The URL that will return the same page of results.
        :param str next_url: (optional) The URL that will return the next page of
               results.
        :param int total: (optional) Reserved for future use.
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
    def _from_dict(cls, _dict):
        """Initialize a Pagination object from a json dictionary."""
        args = {}
        valid_keys = [
            'refresh_url', 'next_url', 'total', 'matched', 'refresh_cursor',
            'next_cursor'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Pagination: '
                + ', '.join(bad_keys))
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

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this Pagination object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeEntity():
    """
    A term from the request that was identified as an entity.

    :attr str entity: An entity detected in the input.
    :attr list[int] location: An array of zero-based character offsets that indicate
          where the detected entity values begin and end in the input text.
    :attr str value: The entity value that was recognized in the user input.
    :attr float confidence: (optional) A decimal percentage that represents Watson's
          confidence in the recognized entity.
    :attr dict metadata: (optional) Any metadata for the entity.
    :attr list[CaptureGroup] groups: (optional) The recognized capture groups for
          the entity, as defined by the entity pattern.
    """

    def __init__(self,
                 entity,
                 location,
                 value,
                 *,
                 confidence=None,
                 metadata=None,
                 groups=None):
        """
        Initialize a RuntimeEntity object.

        :param str entity: An entity detected in the input.
        :param list[int] location: An array of zero-based character offsets that
               indicate where the detected entity values begin and end in the input text.
        :param str value: The entity value that was recognized in the user input.
        :param float confidence: (optional) A decimal percentage that represents
               Watson's confidence in the recognized entity.
        :param dict metadata: (optional) Any metadata for the entity.
        :param list[CaptureGroup] groups: (optional) The recognized capture groups
               for the entity, as defined by the entity pattern.
        """
        self.entity = entity
        self.location = location
        self.value = value
        self.confidence = confidence
        self.metadata = metadata
        self.groups = groups

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeEntity object from a json dictionary."""
        args = {}
        valid_keys = [
            'entity', 'location', 'value', 'confidence', 'metadata', 'groups'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RuntimeEntity: '
                + ', '.join(bad_keys))
        if 'entity' in _dict:
            args['entity'] = _dict.get('entity')
        else:
            raise ValueError(
                'Required property \'entity\' not present in RuntimeEntity JSON'
            )
        if 'location' in _dict:
            args['location'] = _dict.get('location')
        else:
            raise ValueError(
                'Required property \'location\' not present in RuntimeEntity JSON'
            )
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in RuntimeEntity JSON')
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'groups' in _dict:
            args['groups'] = [
                CaptureGroup._from_dict(x) for x in (_dict.get('groups'))
            ]
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self, 'groups') and self.groups is not None:
            _dict['groups'] = [x._to_dict() for x in self.groups]
        return _dict

    def __str__(self):
        """Return a `str` version of this RuntimeEntity object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeIntent():
    """
    An intent identified in the user input.

    :attr str intent: The name of the recognized intent.
    :attr float confidence: A decimal percentage that represents Watson's confidence
          in the intent.
    """

    def __init__(self, intent, confidence):
        """
        Initialize a RuntimeIntent object.

        :param str intent: The name of the recognized intent.
        :param float confidence: A decimal percentage that represents Watson's
               confidence in the intent.
        """
        self.intent = intent
        self.confidence = confidence

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeIntent object from a json dictionary."""
        args = {}
        valid_keys = ['intent', 'confidence']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RuntimeIntent: '
                + ', '.join(bad_keys))
        if 'intent' in _dict:
            args['intent'] = _dict.get('intent')
        else:
            raise ValueError(
                'Required property \'intent\' not present in RuntimeIntent JSON'
            )
        if 'confidence' in _dict:
            args['confidence'] = _dict.get('confidence')
        else:
            raise ValueError(
                'Required property \'confidence\' not present in RuntimeIntent JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'intent') and self.intent is not None:
            _dict['intent'] = self.intent
        if hasattr(self, 'confidence') and self.confidence is not None:
            _dict['confidence'] = self.confidence
        return _dict

    def __str__(self):
        """Return a `str` version of this RuntimeIntent object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class RuntimeResponseGeneric():
    """
    RuntimeResponseGeneric.

    :attr str response_type: The type of response returned by the dialog node. The
          specified response type must be supported by the client application or channel.
          **Note:** The **suggestion** response type is part of the disambiguation
          feature, which is only available for Plus and Premium users.
    :attr str text: (optional) The text of the response.
    :attr int time: (optional) How long to pause, in milliseconds.
    :attr bool typing: (optional) Whether to send a "user is typing" event during
          the pause.
    :attr str source: (optional) The URL of the image.
    :attr str title: (optional) The title or introductory text to show before the
          response.
    :attr str description: (optional) The description to show with the the response.
    :attr str preference: (optional) The preferred type of control to display.
    :attr list[DialogNodeOutputOptionsElement] options: (optional) An array of
          objects describing the options from which the user can choose.
    :attr str message_to_human_agent: (optional) A message to be sent to the human
          agent who will be taking over the conversation.
    :attr str topic: (optional) A label identifying the topic of the conversation,
          derived from the **user_label** property of the relevant node.
    :attr str dialog_node: (optional) The ID of the dialog node that the **topic**
          property is taken from. The **topic** property is populated using the value of
          the dialog node's **user_label** property.
    :attr list[DialogSuggestion] suggestions: (optional) An array of objects
          describing the possible matching dialog nodes from which the user can choose.
          **Note:** The **suggestions** property is part of the disambiguation feature,
          which is only available for Plus and Premium users.
    """

    def __init__(self,
                 response_type,
                 *,
                 text=None,
                 time=None,
                 typing=None,
                 source=None,
                 title=None,
                 description=None,
                 preference=None,
                 options=None,
                 message_to_human_agent=None,
                 topic=None,
                 dialog_node=None,
                 suggestions=None):
        """
        Initialize a RuntimeResponseGeneric object.

        :param str response_type: The type of response returned by the dialog node.
               The specified response type must be supported by the client application or
               channel.
               **Note:** The **suggestion** response type is part of the disambiguation
               feature, which is only available for Plus and Premium users.
        :param str text: (optional) The text of the response.
        :param int time: (optional) How long to pause, in milliseconds.
        :param bool typing: (optional) Whether to send a "user is typing" event
               during the pause.
        :param str source: (optional) The URL of the image.
        :param str title: (optional) The title or introductory text to show before
               the response.
        :param str description: (optional) The description to show with the the
               response.
        :param str preference: (optional) The preferred type of control to display.
        :param list[DialogNodeOutputOptionsElement] options: (optional) An array of
               objects describing the options from which the user can choose.
        :param str message_to_human_agent: (optional) A message to be sent to the
               human agent who will be taking over the conversation.
        :param str topic: (optional) A label identifying the topic of the
               conversation, derived from the **user_label** property of the relevant
               node.
        :param str dialog_node: (optional) The ID of the dialog node that the
               **topic** property is taken from. The **topic** property is populated using
               the value of the dialog node's **user_label** property.
        :param list[DialogSuggestion] suggestions: (optional) An array of objects
               describing the possible matching dialog nodes from which the user can
               choose.
               **Note:** The **suggestions** property is part of the disambiguation
               feature, which is only available for Plus and Premium users.
        """
        self.response_type = response_type
        self.text = text
        self.time = time
        self.typing = typing
        self.source = source
        self.title = title
        self.description = description
        self.preference = preference
        self.options = options
        self.message_to_human_agent = message_to_human_agent
        self.topic = topic
        self.dialog_node = dialog_node
        self.suggestions = suggestions

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a RuntimeResponseGeneric object from a json dictionary."""
        args = {}
        valid_keys = [
            'response_type', 'text', 'time', 'typing', 'source', 'title',
            'description', 'preference', 'options', 'message_to_human_agent',
            'topic', 'dialog_node', 'suggestions'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class RuntimeResponseGeneric: '
                + ', '.join(bad_keys))
        if 'response_type' in _dict:
            args['response_type'] = _dict.get('response_type')
        else:
            raise ValueError(
                'Required property \'response_type\' not present in RuntimeResponseGeneric JSON'
            )
        if 'text' in _dict:
            args['text'] = _dict.get('text')
        if 'time' in _dict:
            args['time'] = _dict.get('time')
        if 'typing' in _dict:
            args['typing'] = _dict.get('typing')
        if 'source' in _dict:
            args['source'] = _dict.get('source')
        if 'title' in _dict:
            args['title'] = _dict.get('title')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'preference' in _dict:
            args['preference'] = _dict.get('preference')
        if 'options' in _dict:
            args['options'] = [
                DialogNodeOutputOptionsElement._from_dict(x)
                for x in (_dict.get('options'))
            ]
        if 'message_to_human_agent' in _dict:
            args['message_to_human_agent'] = _dict.get('message_to_human_agent')
        if 'topic' in _dict:
            args['topic'] = _dict.get('topic')
        if 'dialog_node' in _dict:
            args['dialog_node'] = _dict.get('dialog_node')
        if 'suggestions' in _dict:
            args['suggestions'] = [
                DialogSuggestion._from_dict(x)
                for x in (_dict.get('suggestions'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'response_type') and self.response_type is not None:
            _dict['response_type'] = self.response_type
        if hasattr(self, 'text') and self.text is not None:
            _dict['text'] = self.text
        if hasattr(self, 'time') and self.time is not None:
            _dict['time'] = self.time
        if hasattr(self, 'typing') and self.typing is not None:
            _dict['typing'] = self.typing
        if hasattr(self, 'source') and self.source is not None:
            _dict['source'] = self.source
        if hasattr(self, 'title') and self.title is not None:
            _dict['title'] = self.title
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'preference') and self.preference is not None:
            _dict['preference'] = self.preference
        if hasattr(self, 'options') and self.options is not None:
            _dict['options'] = [x._to_dict() for x in self.options]
        if hasattr(self, 'message_to_human_agent'
                  ) and self.message_to_human_agent is not None:
            _dict['message_to_human_agent'] = self.message_to_human_agent
        if hasattr(self, 'topic') and self.topic is not None:
            _dict['topic'] = self.topic
        if hasattr(self, 'dialog_node') and self.dialog_node is not None:
            _dict['dialog_node'] = self.dialog_node
        if hasattr(self, 'suggestions') and self.suggestions is not None:
            _dict['suggestions'] = [x._to_dict() for x in self.suggestions]
        return _dict

    def __str__(self):
        """Return a `str` version of this RuntimeResponseGeneric object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class ResponseTypeEnum(Enum):
        """
        The type of response returned by the dialog node. The specified response type must
        be supported by the client application or channel.
        **Note:** The **suggestion** response type is part of the disambiguation feature,
        which is only available for Plus and Premium users.
        """
        TEXT = "text"
        PAUSE = "pause"
        IMAGE = "image"
        OPTION = "option"
        CONNECT_TO_AGENT = "connect_to_agent"
        SUGGESTION = "suggestion"

    class PreferenceEnum(Enum):
        """
        The preferred type of control to display.
        """
        DROPDOWN = "dropdown"
        BUTTON = "button"


class Synonym():
    """
    Synonym.

    :attr str synonym: The text of the synonym. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self, synonym, *, created=None, updated=None):
        """
        Initialize a Synonym object.

        :param str synonym: The text of the synonym. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        """
        self.synonym = synonym
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Synonym object from a json dictionary."""
        args = {}
        valid_keys = ['synonym', 'created', 'updated']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Synonym: ' +
                ', '.join(bad_keys))
        if 'synonym' in _dict:
            args['synonym'] = _dict.get('synonym')
        else:
            raise ValueError(
                'Required property \'synonym\' not present in Synonym JSON')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'synonym') and self.synonym is not None:
            _dict['synonym'] = self.synonym
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this Synonym object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SynonymCollection():
    """
    SynonymCollection.

    :attr list[Synonym] synonyms: An array of synonyms.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, synonyms, pagination):
        """
        Initialize a SynonymCollection object.

        :param list[Synonym] synonyms: An array of synonyms.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.synonyms = synonyms
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SynonymCollection object from a json dictionary."""
        args = {}
        valid_keys = ['synonyms', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class SynonymCollection: '
                + ', '.join(bad_keys))
        if 'synonyms' in _dict:
            args['synonyms'] = [
                Synonym._from_dict(x) for x in (_dict.get('synonyms'))
            ]
        else:
            raise ValueError(
                'Required property \'synonyms\' not present in SynonymCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in SynonymCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'synonyms') and self.synonyms is not None:
            _dict['synonyms'] = [x._to_dict() for x in self.synonyms]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this SynonymCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class SystemResponse():
    """
    For internal use only.

    """

    def __init__(self, **kwargs):
        """
        Initialize a SystemResponse object.

        :param **kwargs: (optional) Any additional properties.
        """
        for _key, _value in kwargs.items():
            setattr(self, _key, _value)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a SystemResponse object from a json dictionary."""
        args = {}
        xtra = _dict.copy()
        args.update(xtra)
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, '_additionalProperties'):
            for _key in self._additionalProperties:
                _value = getattr(self, _key, None)
                if _value is not None:
                    _dict[_key] = _value
        return _dict

    def __setattr__(self, name, value):
        properties = {}
        if not hasattr(self, '_additionalProperties'):
            super(SystemResponse, self).__setattr__('_additionalProperties',
                                                    set())
        if name not in properties:
            self._additionalProperties.add(name)
        super(SystemResponse, self).__setattr__(name, value)

    def __str__(self):
        """Return a `str` version of this SystemResponse object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Value():
    """
    Value.

    :attr str value: The text of the entity value. This string must conform to the
          following restrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr dict metadata: (optional) Any metadata related to the entity value.
    :attr str type: Specifies the type of entity value.
    :attr list[str] synonyms: (optional) An array of synonyms for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A synonym must conform to the following resrictions:
          - It cannot contain carriage return, newline, or tab characters.
          - It cannot consist of only whitespace characters.
    :attr list[str] patterns: (optional) An array of patterns for the entity value.
          A value can specify either synonyms or patterns (depending on the value type),
          but not both. A pattern is a regular expression; for more information about how
          to specify a pattern, see the
          [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    """

    def __init__(self,
                 value,
                 type,
                 *,
                 metadata=None,
                 synonyms=None,
                 patterns=None,
                 created=None,
                 updated=None):
        """
        Initialize a Value object.

        :param str value: The text of the entity value. This string must conform to
               the following restrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param str type: Specifies the type of entity value.
        :param dict metadata: (optional) Any metadata related to the entity value.
        :param list[str] synonyms: (optional) An array of synonyms for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A synonym must conform to the following
               resrictions:
               - It cannot contain carriage return, newline, or tab characters.
               - It cannot consist of only whitespace characters.
        :param list[str] patterns: (optional) An array of patterns for the entity
               value. A value can specify either synonyms or patterns (depending on the
               value type), but not both. A pattern is a regular expression; for more
               information about how to specify a pattern, see the
               [documentation](https://cloud.ibm.com/docs/services/assistant?topic=assistant-entities#entities-create-dictionary-based).
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        """
        self.value = value
        self.metadata = metadata
        self.type = type
        self.synonyms = synonyms
        self.patterns = patterns
        self.created = created
        self.updated = updated

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Value object from a json dictionary."""
        args = {}
        valid_keys = [
            'value', 'metadata', 'type', 'synonyms', 'patterns', 'created',
            'updated'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Value: ' +
                ', '.join(bad_keys))
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in Value JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError(
                'Required property \'type\' not present in Value JSON')
        if 'synonyms' in _dict:
            args['synonyms'] = _dict.get('synonyms')
        if 'patterns' in _dict:
            args['patterns'] = _dict.get('patterns')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        return cls(**args)

    def _to_dict(self):
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
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        return _dict

    def __str__(self):
        """Return a `str` version of this Value object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(Enum):
        """
        Specifies the type of entity value.
        """
        SYNONYMS = "synonyms"
        PATTERNS = "patterns"


class ValueCollection():
    """
    ValueCollection.

    :attr list[Value] values: An array of entity values.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, values, pagination):
        """
        Initialize a ValueCollection object.

        :param list[Value] values: An array of entity values.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.values = values
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ValueCollection object from a json dictionary."""
        args = {}
        valid_keys = ['values', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class ValueCollection: '
                + ', '.join(bad_keys))
        if 'values' in _dict:
            args['values'] = [
                Value._from_dict(x) for x in (_dict.get('values'))
            ]
        else:
            raise ValueError(
                'Required property \'values\' not present in ValueCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in ValueCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'values') and self.values is not None:
            _dict['values'] = [x._to_dict() for x in self.values]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this ValueCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Webhook():
    """
    A webhook that can be used by dialog nodes to make programmatic calls to an external
    function.
    **Note:** Currently, only a single webhook named `main_webhook` is supported.

    :attr str url: The URL for the external service or application to which you want
          to send HTTP POST requests.
    :attr str name: The name of the webhook. Currently, `main_webhook` is the only
          supported value.
    :attr list[WebhookHeader] headers: (optional) An optional array of HTTP headers
          to pass with the HTTP request.
    """

    def __init__(self, url, name, *, headers=None):
        """
        Initialize a Webhook object.

        :param str url: The URL for the external service or application to which
               you want to send HTTP POST requests.
        :param str name: The name of the webhook. Currently, `main_webhook` is the
               only supported value.
        :param list[WebhookHeader] headers: (optional) An optional array of HTTP
               headers to pass with the HTTP request.
        """
        self.url = url
        self.name = name
        self.headers = headers

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Webhook object from a json dictionary."""
        args = {}
        valid_keys = ['url', 'name', 'headers']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Webhook: ' +
                ', '.join(bad_keys))
        if 'url' in _dict:
            args['url'] = _dict.get('url')
        else:
            raise ValueError(
                'Required property \'url\' not present in Webhook JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Webhook JSON')
        if 'headers' in _dict:
            args['headers'] = [
                WebhookHeader._from_dict(x) for x in (_dict.get('headers'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'url') and self.url is not None:
            _dict['url'] = self.url
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'headers') and self.headers is not None:
            _dict['headers'] = [x._to_dict() for x in self.headers]
        return _dict

    def __str__(self):
        """Return a `str` version of this Webhook object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WebhookHeader():
    """
    A key/value pair defining an HTTP header and a value.

    :attr str name: The name of an HTTP header (for example, `Authorization`).
    :attr str value: The value of an HTTP header.
    """

    def __init__(self, name, value):
        """
        Initialize a WebhookHeader object.

        :param str name: The name of an HTTP header (for example, `Authorization`).
        :param str value: The value of an HTTP header.
        """
        self.name = name
        self.value = value

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WebhookHeader object from a json dictionary."""
        args = {}
        valid_keys = ['name', 'value']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WebhookHeader: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in WebhookHeader JSON')
        if 'value' in _dict:
            args['value'] = _dict.get('value')
        else:
            raise ValueError(
                'Required property \'value\' not present in WebhookHeader JSON')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'value') and self.value is not None:
            _dict['value'] = self.value
        return _dict

    def __str__(self):
        """Return a `str` version of this WebhookHeader object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class Workspace():
    """
    Workspace.

    :attr str name: The name of the workspace. This string cannot contain carriage
          return, newline, or tab characters.
    :attr str description: (optional) The description of the workspace. This string
          cannot contain carriage return, newline, or tab characters.
    :attr str language: The language of the workspace.
    :attr dict metadata: (optional) Any metadata related to the workspace.
    :attr bool learning_opt_out: Whether training data from the workspace (including
          artifacts such as intents and entities) can be used by IBM for general service
          improvements. `true` indicates that workspace training data is not to be used.
    :attr WorkspaceSystemSettings system_settings: (optional) Global settings for
          the workspace.
    :attr str workspace_id: The workspace ID of the workspace.
    :attr str status: (optional) The current status of the workspace.
    :attr datetime created: (optional) The timestamp for creation of the object.
    :attr datetime updated: (optional) The timestamp for the most recent update to
          the object.
    :attr list[Intent] intents: (optional) An array of intents.
    :attr list[Entity] entities: (optional) An array of objects describing the
          entities for the workspace.
    :attr list[DialogNode] dialog_nodes: (optional) An array of objects describing
          the dialog nodes in the workspace.
    :attr list[Counterexample] counterexamples: (optional) An array of
          counterexamples.
    :attr list[Webhook] webhooks: (optional)
    """

    def __init__(self,
                 name,
                 language,
                 learning_opt_out,
                 workspace_id,
                 *,
                 description=None,
                 metadata=None,
                 system_settings=None,
                 status=None,
                 created=None,
                 updated=None,
                 intents=None,
                 entities=None,
                 dialog_nodes=None,
                 counterexamples=None,
                 webhooks=None):
        """
        Initialize a Workspace object.

        :param str name: The name of the workspace. This string cannot contain
               carriage return, newline, or tab characters.
        :param str language: The language of the workspace.
        :param bool learning_opt_out: Whether training data from the workspace
               (including artifacts such as intents and entities) can be used by IBM for
               general service improvements. `true` indicates that workspace training data
               is not to be used.
        :param str workspace_id: The workspace ID of the workspace.
        :param str description: (optional) The description of the workspace. This
               string cannot contain carriage return, newline, or tab characters.
        :param dict metadata: (optional) Any metadata related to the workspace.
        :param WorkspaceSystemSettings system_settings: (optional) Global settings
               for the workspace.
        :param str status: (optional) The current status of the workspace.
        :param datetime created: (optional) The timestamp for creation of the
               object.
        :param datetime updated: (optional) The timestamp for the most recent
               update to the object.
        :param list[Intent] intents: (optional) An array of intents.
        :param list[Entity] entities: (optional) An array of objects describing the
               entities for the workspace.
        :param list[DialogNode] dialog_nodes: (optional) An array of objects
               describing the dialog nodes in the workspace.
        :param list[Counterexample] counterexamples: (optional) An array of
               counterexamples.
        :param list[Webhook] webhooks: (optional)
        """
        self.name = name
        self.description = description
        self.language = language
        self.metadata = metadata
        self.learning_opt_out = learning_opt_out
        self.system_settings = system_settings
        self.workspace_id = workspace_id
        self.status = status
        self.created = created
        self.updated = updated
        self.intents = intents
        self.entities = entities
        self.dialog_nodes = dialog_nodes
        self.counterexamples = counterexamples
        self.webhooks = webhooks

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Workspace object from a json dictionary."""
        args = {}
        valid_keys = [
            'name', 'description', 'language', 'metadata', 'learning_opt_out',
            'system_settings', 'workspace_id', 'status', 'created', 'updated',
            'intents', 'entities', 'dialog_nodes', 'counterexamples', 'webhooks'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class Workspace: '
                + ', '.join(bad_keys))
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError(
                'Required property \'name\' not present in Workspace JSON')
        if 'description' in _dict:
            args['description'] = _dict.get('description')
        if 'language' in _dict:
            args['language'] = _dict.get('language')
        else:
            raise ValueError(
                'Required property \'language\' not present in Workspace JSON')
        if 'metadata' in _dict:
            args['metadata'] = _dict.get('metadata')
        if 'learning_opt_out' in _dict:
            args['learning_opt_out'] = _dict.get('learning_opt_out')
        else:
            raise ValueError(
                'Required property \'learning_opt_out\' not present in Workspace JSON'
            )
        if 'system_settings' in _dict:
            args['system_settings'] = WorkspaceSystemSettings._from_dict(
                _dict.get('system_settings'))
        if 'workspace_id' in _dict:
            args['workspace_id'] = _dict.get('workspace_id')
        else:
            raise ValueError(
                'Required property \'workspace_id\' not present in Workspace JSON'
            )
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'created' in _dict:
            args['created'] = string_to_datetime(_dict.get('created'))
        if 'updated' in _dict:
            args['updated'] = string_to_datetime(_dict.get('updated'))
        if 'intents' in _dict:
            args['intents'] = [
                Intent._from_dict(x) for x in (_dict.get('intents'))
            ]
        if 'entities' in _dict:
            args['entities'] = [
                Entity._from_dict(x) for x in (_dict.get('entities'))
            ]
        if 'dialog_nodes' in _dict:
            args['dialog_nodes'] = [
                DialogNode._from_dict(x) for x in (_dict.get('dialog_nodes'))
            ]
        if 'counterexamples' in _dict:
            args['counterexamples'] = [
                Counterexample._from_dict(x)
                for x in (_dict.get('counterexamples'))
            ]
        if 'webhooks' in _dict:
            args['webhooks'] = [
                Webhook._from_dict(x) for x in (_dict.get('webhooks'))
            ]
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'description') and self.description is not None:
            _dict['description'] = self.description
        if hasattr(self, 'language') and self.language is not None:
            _dict['language'] = self.language
        if hasattr(self, 'metadata') and self.metadata is not None:
            _dict['metadata'] = self.metadata
        if hasattr(self,
                   'learning_opt_out') and self.learning_opt_out is not None:
            _dict['learning_opt_out'] = self.learning_opt_out
        if hasattr(self,
                   'system_settings') and self.system_settings is not None:
            _dict['system_settings'] = self.system_settings._to_dict()
        if hasattr(self, 'workspace_id') and self.workspace_id is not None:
            _dict['workspace_id'] = self.workspace_id
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'created') and self.created is not None:
            _dict['created'] = datetime_to_string(self.created)
        if hasattr(self, 'updated') and self.updated is not None:
            _dict['updated'] = datetime_to_string(self.updated)
        if hasattr(self, 'intents') and self.intents is not None:
            _dict['intents'] = [x._to_dict() for x in self.intents]
        if hasattr(self, 'entities') and self.entities is not None:
            _dict['entities'] = [x._to_dict() for x in self.entities]
        if hasattr(self, 'dialog_nodes') and self.dialog_nodes is not None:
            _dict['dialog_nodes'] = [x._to_dict() for x in self.dialog_nodes]
        if hasattr(self,
                   'counterexamples') and self.counterexamples is not None:
            _dict['counterexamples'] = [
                x._to_dict() for x in self.counterexamples
            ]
        if hasattr(self, 'webhooks') and self.webhooks is not None:
            _dict['webhooks'] = [x._to_dict() for x in self.webhooks]
        return _dict

    def __str__(self):
        """Return a `str` version of this Workspace object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StatusEnum(Enum):
        """
        The current status of the workspace.
        """
        NON_EXISTENT = "Non Existent"
        TRAINING = "Training"
        FAILED = "Failed"
        AVAILABLE = "Available"
        UNAVAILABLE = "Unavailable"


class WorkspaceCollection():
    """
    WorkspaceCollection.

    :attr list[Workspace] workspaces: An array of objects describing the workspaces
          associated with the service instance.
    :attr Pagination pagination: The pagination data for the returned objects.
    """

    def __init__(self, workspaces, pagination):
        """
        Initialize a WorkspaceCollection object.

        :param list[Workspace] workspaces: An array of objects describing the
               workspaces associated with the service instance.
        :param Pagination pagination: The pagination data for the returned objects.
        """
        self.workspaces = workspaces
        self.pagination = pagination

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceCollection object from a json dictionary."""
        args = {}
        valid_keys = ['workspaces', 'pagination']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WorkspaceCollection: '
                + ', '.join(bad_keys))
        if 'workspaces' in _dict:
            args['workspaces'] = [
                Workspace._from_dict(x) for x in (_dict.get('workspaces'))
            ]
        else:
            raise ValueError(
                'Required property \'workspaces\' not present in WorkspaceCollection JSON'
            )
        if 'pagination' in _dict:
            args['pagination'] = Pagination._from_dict(_dict.get('pagination'))
        else:
            raise ValueError(
                'Required property \'pagination\' not present in WorkspaceCollection JSON'
            )
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'workspaces') and self.workspaces is not None:
            _dict['workspaces'] = [x._to_dict() for x in self.workspaces]
        if hasattr(self, 'pagination') and self.pagination is not None:
            _dict['pagination'] = self.pagination._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this WorkspaceCollection object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettings():
    """
    Global settings for the workspace.

    :attr WorkspaceSystemSettingsTooling tooling: (optional) Workspace settings
          related to the Watson Assistant user interface.
    :attr WorkspaceSystemSettingsDisambiguation disambiguation: (optional) Workspace
          settings related to the disambiguation feature.
          **Note:** This feature is available only to Plus and Premium users.
    :attr dict human_agent_assist: (optional) For internal use only.
    :attr WorkspaceSystemSettingsOffTopic off_topic: (optional) Workspace settings
          related to detection of irrelevant input.
    """

    def __init__(self,
                 *,
                 tooling=None,
                 disambiguation=None,
                 human_agent_assist=None,
                 off_topic=None):
        """
        Initialize a WorkspaceSystemSettings object.

        :param WorkspaceSystemSettingsTooling tooling: (optional) Workspace
               settings related to the Watson Assistant user interface.
        :param WorkspaceSystemSettingsDisambiguation disambiguation: (optional)
               Workspace settings related to the disambiguation feature.
               **Note:** This feature is available only to Plus and Premium users.
        :param dict human_agent_assist: (optional) For internal use only.
        :param WorkspaceSystemSettingsOffTopic off_topic: (optional) Workspace
               settings related to detection of irrelevant input.
        """
        self.tooling = tooling
        self.disambiguation = disambiguation
        self.human_agent_assist = human_agent_assist
        self.off_topic = off_topic

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettings object from a json dictionary."""
        args = {}
        valid_keys = [
            'tooling', 'disambiguation', 'human_agent_assist', 'off_topic'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WorkspaceSystemSettings: '
                + ', '.join(bad_keys))
        if 'tooling' in _dict:
            args['tooling'] = WorkspaceSystemSettingsTooling._from_dict(
                _dict.get('tooling'))
        if 'disambiguation' in _dict:
            args[
                'disambiguation'] = WorkspaceSystemSettingsDisambiguation._from_dict(
                    _dict.get('disambiguation'))
        if 'human_agent_assist' in _dict:
            args['human_agent_assist'] = _dict.get('human_agent_assist')
        if 'off_topic' in _dict:
            args['off_topic'] = WorkspaceSystemSettingsOffTopic._from_dict(
                _dict.get('off_topic'))
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'tooling') and self.tooling is not None:
            _dict['tooling'] = self.tooling._to_dict()
        if hasattr(self, 'disambiguation') and self.disambiguation is not None:
            _dict['disambiguation'] = self.disambiguation._to_dict()
        if hasattr(
                self,
                'human_agent_assist') and self.human_agent_assist is not None:
            _dict['human_agent_assist'] = self.human_agent_assist
        if hasattr(self, 'off_topic') and self.off_topic is not None:
            _dict['off_topic'] = self.off_topic._to_dict()
        return _dict

    def __str__(self):
        """Return a `str` version of this WorkspaceSystemSettings object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsDisambiguation():
    """
    Workspace settings related to the disambiguation feature.
    **Note:** This feature is available only to Plus and Premium users.

    :attr str prompt: (optional) The text of the introductory prompt that
          accompanies disambiguation options presented to the user.
    :attr str none_of_the_above_prompt: (optional) The user-facing label for the
          option users can select if none of the suggested options is correct. If no value
          is specified for this property, this option does not appear.
    :attr bool enabled: (optional) Whether the disambiguation feature is enabled for
          the workspace.
    :attr str sensitivity: (optional) The sensitivity of the disambiguation feature
          to intent detection conflicts. Set to **high** if you want the disambiguation
          feature to be triggered more often. This can be useful for testing or
          demonstration purposes.
    :attr bool randomize: (optional) Whether the order in which disambiguation
          suggestions are presented should be randomized (but still influenced by relative
          confidence).
    :attr int max_suggestions: (optional) The maximum number of disambigation
          suggestions that can be included in a `suggestion` response.
    :attr str suggestion_text_policy: (optional) For internal use only.
    """

    def __init__(self,
                 *,
                 prompt=None,
                 none_of_the_above_prompt=None,
                 enabled=None,
                 sensitivity=None,
                 randomize=None,
                 max_suggestions=None,
                 suggestion_text_policy=None):
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
               feature to intent detection conflicts. Set to **high** if you want the
               disambiguation feature to be triggered more often. This can be useful for
               testing or demonstration purposes.
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
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsDisambiguation object from a json dictionary."""
        args = {}
        valid_keys = [
            'prompt', 'none_of_the_above_prompt', 'enabled', 'sensitivity',
            'randomize', 'max_suggestions', 'suggestion_text_policy'
        ]
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WorkspaceSystemSettingsDisambiguation: '
                + ', '.join(bad_keys))
        if 'prompt' in _dict:
            args['prompt'] = _dict.get('prompt')
        if 'none_of_the_above_prompt' in _dict:
            args['none_of_the_above_prompt'] = _dict.get(
                'none_of_the_above_prompt')
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        if 'sensitivity' in _dict:
            args['sensitivity'] = _dict.get('sensitivity')
        if 'randomize' in _dict:
            args['randomize'] = _dict.get('randomize')
        if 'max_suggestions' in _dict:
            args['max_suggestions'] = _dict.get('max_suggestions')
        if 'suggestion_text_policy' in _dict:
            args['suggestion_text_policy'] = _dict.get('suggestion_text_policy')
        return cls(**args)

    def _to_dict(self):
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

    def __str__(self):
        """Return a `str` version of this WorkspaceSystemSettingsDisambiguation object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class SensitivityEnum(Enum):
        """
        The sensitivity of the disambiguation feature to intent detection conflicts. Set
        to **high** if you want the disambiguation feature to be triggered more often.
        This can be useful for testing or demonstration purposes.
        """
        AUTO = "auto"
        HIGH = "high"


class WorkspaceSystemSettingsOffTopic():
    """
    Workspace settings related to detection of irrelevant input.

    :attr bool enabled: (optional) Whether enhanced irrelevance detection is enabled
          for the workspace.
    """

    def __init__(self, *, enabled=None):
        """
        Initialize a WorkspaceSystemSettingsOffTopic object.

        :param bool enabled: (optional) Whether enhanced irrelevance detection is
               enabled for the workspace.
        """
        self.enabled = enabled

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsOffTopic object from a json dictionary."""
        args = {}
        valid_keys = ['enabled']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WorkspaceSystemSettingsOffTopic: '
                + ', '.join(bad_keys))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def __str__(self):
        """Return a `str` version of this WorkspaceSystemSettingsOffTopic object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class WorkspaceSystemSettingsTooling():
    """
    Workspace settings related to the Watson Assistant user interface.

    :attr bool store_generic_responses: (optional) Whether the dialog JSON editor
          displays text responses within the `output.generic` object.
    """

    def __init__(self, *, store_generic_responses=None):
        """
        Initialize a WorkspaceSystemSettingsTooling object.

        :param bool store_generic_responses: (optional) Whether the dialog JSON
               editor displays text responses within the `output.generic` object.
        """
        self.store_generic_responses = store_generic_responses

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a WorkspaceSystemSettingsTooling object from a json dictionary."""
        args = {}
        valid_keys = ['store_generic_responses']
        bad_keys = set(_dict.keys()) - set(valid_keys)
        if bad_keys:
            raise ValueError(
                'Unrecognized keys detected in dictionary for class WorkspaceSystemSettingsTooling: '
                + ', '.join(bad_keys))
        if 'store_generic_responses' in _dict:
            args['store_generic_responses'] = _dict.get(
                'store_generic_responses')
        return cls(**args)

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'store_generic_responses'
                  ) and self.store_generic_responses is not None:
            _dict['store_generic_responses'] = self.store_generic_responses
        return _dict

    def __str__(self):
        """Return a `str` version of this WorkspaceSystemSettingsTooling object."""
        return json.dumps(self._to_dict(), indent=2)

    def __eq__(self, other):
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
